"""Zenodo publishing CLI — main orchestrator.

Usage:
    python -m src.zenodo                              # Default config
    python -m src.zenodo --config publish_config.yaml # Custom config
    python -m src.zenodo --sandbox-only               # Skip production
    python -m src.zenodo --papers SLUG1 SLUG2         # Subset
    python -m src.zenodo --skip-pdf                   # No PDF rendering
    python -m src.zenodo --skip-quality-gates         # Bypass gates (use with caution)
"""

import argparse
import sys
from pathlib import Path

from .config import load_config, load_tokens, BASE
from .api import ZenodoClient, ZenodoAPIError
from .quality_gates import run_quality_gates
from .metadata import build_metadata, extract_title
from .pdf import render_pdf
from .bundle import assemble_bundle
from .manifest import load_manifest, save_manifest, update_entry, is_published


def print_table(headers: list[str], rows: list[list[str]]):
    """Print a simple aligned table."""
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))

    fmt = " | ".join(f"{{:<{w}}}" for w in widths)
    sep = "-+-".join("-" * w for w in widths)

    print(fmt.format(*headers))
    print(sep)
    for row in rows:
        print(fmt.format(*[str(c) for c in row]))
    print()


def run(args):
    """Main publishing workflow."""
    print("=" * 60)
    print("SHELL ZENODO PUBLISHER")
    print("=" * 60)
    print()

    # Phase 0: Load config and tokens
    print("Phase 0: Loading configuration...")
    try:
        config = load_config(args.config)
        tokens = load_tokens()
    except (FileNotFoundError, RuntimeError) as e:
        print(f"  FATAL: {e}")
        return 1
    print(f"  Config: {args.config or 'publish_config.yaml'}")
    print(f"  Community: {config.get('community', 'none')}")
    print(f"  License: {config.get('license', 'cc-by-4.0')}")
    print(f"  Sandbox token: {'SET' if tokens['sandbox'] else 'MISSING'}")
    print(f"  Production token: {'SET' if tokens['production'] else 'MISSING'}")
    print()

    # Determine which papers to publish
    all_papers = [p["slug"] for p in config.get("papers", [])]
    if args.papers:
        selected = [s for s in args.papers if s in all_papers]
        if not selected:
            # Try partial match
            selected = [p for p in all_papers if any(s in p for s in args.papers)]
        if not selected:
            print(f"  No matching papers found for: {args.papers}")
            print(f"  Available: {all_papers}")
            return 1
    else:
        selected = all_papers

    print(f"  Papers selected: {len(selected)}")
    for s in selected:
        print(f"    - {s}")
    print()

    # Phase 1: Quality gates
    manifest = load_manifest()
    passing = []
    if args.skip_quality_gates:
        print("Phase 1: Quality gates SKIPPED (--skip-quality-gates)")
        passing = selected
    else:
        print("Phase 1: Running quality gates...")
        gate_rows = []
        for slug in selected:
            passed, issues = run_quality_gates(slug, config, manifest)
            status = "PASS" if passed else "FAIL"
            if any("SKIP:" in i for i in issues):
                status = "SKIP"
            gate_rows.append([slug.split("_2026")[0], status, "; ".join(issues[:2]) or "—"])
            if passed:
                passing.append(slug)

        print_table(["Paper", "Status", "Issues"], gate_rows)

    if not passing:
        print("No papers passed quality gates. Aborting.")
        return 1

    # Phase 2: PDF rendering
    pdf_paths = {}
    if args.skip_pdf:
        print("Phase 2: PDF rendering SKIPPED (--skip-pdf)")
    else:
        print("Phase 2: Rendering PDFs via pandoc...")
        for slug in passing:
            paper_path = BASE / "papers" / slug / "best_paper.md"
            pdf_path = BASE / "papers" / slug / "paper.pdf"
            title = extract_title(paper_path)
            author = config.get("author", {}).get("name", "Rice, James P Jr.")
            success = render_pdf(paper_path, pdf_path, title, author)
            if success:
                pdf_paths[slug] = pdf_path
        rendered = len(pdf_paths)
        print(f"  PDFs rendered: {rendered}/{len(passing)}")
        if rendered < len(passing):
            print("  (Papers without PDF will upload markdown only)")
        print()

    # Phase 3: Sandbox publish
    print("Phase 3: Publishing to SANDBOX...")
    sandbox_client = ZenodoClient(tokens["sandbox"], sandbox=True)
    sandbox_results = {}

    for slug in passing:
        print(f"\n  [{slug.split('_2026')[0]}]")
        try:
            # Create deposition
            dep = sandbox_client.create_deposition()
            dep_id = dep["id"]
            print(f"    Deposition created: {dep_id}")

            # Upload bundle
            bundle = assemble_bundle(slug, pdf_paths.get(slug))
            for filepath, upload_name in bundle:
                sandbox_client.upload_file(dep_id, filepath, upload_name)
                print(f"    Uploaded: {upload_name}")

            # Set metadata
            metadata = build_metadata(slug, config)
            sandbox_client.set_metadata(dep_id, metadata)
            print(f"    Metadata set: {metadata['title'][:50]}...")

            # Publish
            result = sandbox_client.publish(dep_id)
            record_url = result.get("links", {}).get("record_html",
                        result.get("links", {}).get("html", f"sandbox.zenodo.org/records/{dep_id}"))
            doi = result.get("doi", "pending")

            sandbox_results[slug] = {
                "deposition_id": dep_id,
                "record_url": record_url,
                "doi": doi,
            }
            update_entry(slug, "sandbox", sandbox_results[slug], manifest)
            print(f"    Published: {record_url}")

        except ZenodoAPIError as e:
            print(f"    FAILED: {e}")
            sandbox_results[slug] = {"error": str(e)}

    # Summary table
    print("\n" + "=" * 60)
    print("SANDBOX RESULTS")
    print("=" * 60)
    summary_rows = []
    for slug in passing:
        sr = sandbox_results.get(slug, {})
        status = "OK" if "record_url" in sr else "FAILED"
        url = sr.get("record_url", sr.get("error", "—"))[:60]
        summary_rows.append([slug.split("_2026")[0], status, url])
    print_table(["Paper", "Status", "URL"], summary_rows)

    successful = [s for s in passing if "record_url" in sandbox_results.get(s, {})]
    if not successful:
        print("All sandbox publishes failed. Aborting.")
        return 1

    # Phase 4: Interactive review gate
    if args.sandbox_only:
        print("--sandbox-only flag set. Stopping here.")
        print(f"Manifest saved: {len(successful)} papers in sandbox.")
        return 0

    print("=" * 60)
    print("REVIEW GATE")
    print("=" * 60)
    print()
    print("Sandbox records published. Review each at the URLs above.")
    print("Verify: titles, abstracts, files, formatting all look correct.")
    print()
    print("When satisfied, type 'publish' to proceed to PRODUCTION.")
    print("Type 'abort' to cancel (sandbox records remain for inspection).")
    print()

    while True:
        try:
            response = input(">>> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nAborted.")
            return 0

        if response == "publish":
            break
        elif response == "abort":
            print("Aborted. Sandbox records remain for manual inspection.")
            return 0
        else:
            print("Type 'publish' or 'abort'.")

    # Phase 5: Production publish
    print("\nPhase 5: Publishing to PRODUCTION...")
    prod_client = ZenodoClient(tokens["production"], sandbox=False)
    production_results = {}

    for slug in successful:
        print(f"\n  [{slug.split('_2026')[0]}]")
        try:
            dep = prod_client.create_deposition()
            dep_id = dep["id"]

            bundle = assemble_bundle(slug, pdf_paths.get(slug))
            for filepath, upload_name in bundle:
                prod_client.upload_file(dep_id, filepath, upload_name)

            metadata = build_metadata(slug, config)
            prod_client.set_metadata(dep_id, metadata)

            result = prod_client.publish(dep_id)
            doi = result.get("doi", "unknown")
            record_url = result.get("links", {}).get("record_html",
                        result.get("links", {}).get("html", ""))

            production_results[slug] = {
                "deposition_id": dep_id,
                "doi": doi,
                "record_url": record_url,
            }
            update_entry(slug, "production", production_results[slug], manifest)
            print(f"    DOI: {doi}")
            print(f"    URL: {record_url}")

            # Save DOI to paper directory
            doi_path = BASE / "papers" / slug / "doi.txt"
            doi_path.write_text(doi, encoding="utf-8")

        except ZenodoAPIError as e:
            print(f"    FAILED: {e}")
            production_results[slug] = {"error": str(e)}

    # Phase 6: Final summary
    print("\n" + "=" * 60)
    print("PUBLICATION COMPLETE")
    print("=" * 60)
    final_rows = []
    for slug in successful:
        pr = production_results.get(slug, {})
        doi = pr.get("doi", "FAILED")
        url = pr.get("record_url", pr.get("error", "—"))[:50]
        final_rows.append([slug.split("_2026")[0], doi, url])
    print_table(["Paper", "DOI", "URL"], final_rows)

    community = config.get("community")
    if community:
        print(f"Community: https://zenodo.org/communities/{community}")

    published_count = sum(1 for r in production_results.values() if "doi" in r)
    print(f"\n{published_count}/{len(successful)} papers published to production.")
    print(f"Manifest saved to: published_manifest.json")

    return 0


def main():
    parser = argparse.ArgumentParser(description="SHELL Zenodo Publisher")
    parser.add_argument("--config", type=Path, default=None,
                       help="Path to publish_config.yaml")
    parser.add_argument("--sandbox-only", action="store_true",
                       help="Publish to sandbox only, skip production")
    parser.add_argument("--papers", nargs="*",
                       help="Specific paper slugs (or partial matches)")
    parser.add_argument("--skip-pdf", action="store_true",
                       help="Skip PDF rendering, upload markdown only")
    parser.add_argument("--skip-quality-gates", action="store_true",
                       help="Skip quality gate checks (use with caution)")
    args = parser.parse_args()

    sys.exit(run(args))


if __name__ == "__main__":
    main()
