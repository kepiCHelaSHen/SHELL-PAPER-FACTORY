#!/usr/bin/env python3
"""
publish_manager.py — Publishing management tool for THESIS papers.

Scans completed papers, shows status, runs pre-flight checks, and publishes
to Zenodo (sandbox first, then production on confirmation).

Usage:
    python src/publish_manager.py                    # Interactive mode
    python src/publish_manager.py --list             # Just show status
    python src/publish_manager.py --publish 1,2,3    # Publish specific papers
    python src/publish_manager.py --publish all      # Publish all eligible
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

SHELL_ROOT = Path(__file__).parent.parent
PAPERS_DIR = SHELL_ROOT / "papers"
MANIFEST_PATH = SHELL_ROOT / "published_manifest.json"
API_ENV = SHELL_ROOT / "api.env"
MIN_SCORE = 7.5
MIN_REVIEWERS = 3

SANDBOX_URL = "https://sandbox.zenodo.org/api"
PRODUCTION_URL = "https://zenodo.org/api"


def load_token(sandbox: bool) -> str:
    """Load Zenodo token from api.env."""
    key = "ZENODO_SANDBOX_TOKEN" if sandbox else "ZENODO_TOKEN"
    val = os.environ.get(key)
    if val:
        return val.strip().strip('"').strip("'")
    if API_ENV.exists():
        for line in API_ENV.read_text(encoding="utf-8").splitlines():
            if line.startswith(key + "="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return ""


def load_manifest() -> dict:
    """Load the published manifest."""
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {}


def save_manifest(manifest: dict):
    """Save the published manifest."""
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, default=str), encoding="utf-8")


def scan_papers() -> list[dict]:
    """Scan all paper directories and collect metadata."""
    papers = []
    for project_dir in sorted(PAPERS_DIR.iterdir()):
        if not project_dir.is_dir():
            continue
        best_paper = project_dir / "best_paper.md"
        if not best_paper.exists():
            continue

        paper_text = best_paper.read_text(encoding="utf-8", errors="replace")
        lines = len(paper_text.splitlines())

        # Extract title from first heading
        title_match = re.search(r"^#\s+(.+)", paper_text, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else project_dir.name

        # Count reviews
        reviews_dir = project_dir / "reviews"
        reviews = {}
        if reviews_dir.exists():
            for review_file in reviews_dir.glob("*_review_*.md"):
                model = review_file.name.split("_")[0]
                text = review_file.read_text(encoding="utf-8", errors="replace")
                if "ERROR" not in text[:200]:
                    # Parse composite
                    composite = 0
                    for pattern in [
                        r"\**(\d+\.?\d*)\s*/\s*10\**",
                        r"[Cc]omposite[:\s]*\**(\d+\.?\d*)",
                        r"[Aa]verage.*?(\d+\.?\d*)\s*/\s*10",
                    ]:
                        match = re.search(pattern, text)
                        if match:
                            val = float(match.group(1))
                            if 1 <= val <= 10:
                                composite = val
                                break
                    reviews[model] = composite

        # Get verdict from state vector
        sv_path = project_dir / "state_vector.md"
        verdict = "UNKNOWN"
        if sv_path.exists():
            sv_text = sv_path.read_text(encoding="utf-8", errors="replace")
            for v in ["ACCEPT", "MINOR_REVISION", "MAJOR_REVISION", "REJECT"]:
                if v in sv_text:
                    verdict = v
                    break

        # Check manifest
        manifest = load_manifest()
        slug = project_dir.name
        published = slug in manifest

        # Compute average score
        scores = [s for s in reviews.values() if s > 0]
        avg_score = round(sum(scores) / len(scores), 2) if scores else 0

        papers.append({
            "slug": slug,
            "title": title,
            "path": project_dir,
            "lines": lines,
            "reviews": reviews,
            "review_count": len(scores),
            "avg_score": avg_score,
            "verdict": verdict,
            "published": published,
            "doi": manifest.get(slug, {}).get("doi", ""),
        })

    return papers


def preflight_check(paper: dict) -> tuple[bool, list[str]]:
    """Run pre-flight checks on a paper. Returns (pass, issues)."""
    issues = []
    paper_path = paper["path"] / "best_paper.md"
    text = paper_path.read_text(encoding="utf-8", errors="replace")

    # Check 1: No code blocks in the paper body
    code_blocks = re.findall(r"```python\s*\n#\s*Figure", text)
    if code_blocks:
        issues.append(f"FAIL: {len(code_blocks)} Python figure code blocks found (should be image refs)")

    # Check 2: No encoding artifacts
    encoding_issues = re.findall(r"ΓÇ[ö|ô|ö]|├ù|├å|╬[▓▒░]|Γò¼", text)
    if encoding_issues:
        issues.append(f"WARN: {len(encoding_issues)} potential encoding artifacts found")

    # Check 3: Score threshold
    if paper["avg_score"] < MIN_SCORE:
        issues.append(f"FAIL: Average score {paper['avg_score']} below threshold {MIN_SCORE}")

    # Check 4: Minimum reviewers
    if paper["review_count"] < MIN_REVIEWERS:
        issues.append(f"FAIL: Only {paper['review_count']} reviews (need {MIN_REVIEWERS})")

    # Check 5: Already published
    if paper["published"]:
        issues.append(f"SKIP: Already published with DOI {paper['doi']}")

    # Check 6: Has figures directory with rendered images
    figures_dir = paper["path"] / "run1" / "figures"
    if not figures_dir.exists():
        figures_dir = paper["path"] / "figures"
    if figures_dir.exists():
        png_count = len(list(figures_dir.glob("*.png")))
        if png_count == 0:
            issues.append("WARN: No rendered PNG figures found")

    passed = not any(i.startswith("FAIL") for i in issues)
    return passed, issues


def extract_metadata(paper: dict) -> dict:
    """Extract Zenodo metadata from a paper."""
    paper_path = paper["path"] / "best_paper.md"
    text = paper_path.read_text(encoding="utf-8", errors="replace")

    # Get abstract
    abstract_match = re.search(
        r"##\s*Abstract\s*\n(.*?)(?=\n##|\n---|\n#[^#])",
        text, re.DOTALL
    )
    abstract = abstract_match.group(1).strip()[:2000] if abstract_match else paper["title"]

    # Get keywords from title
    keywords = ["autonomous paper generation", "adversarial validation", "THESIS"]

    metadata = {
        "title": paper["title"],
        "upload_type": "publication",
        "publication_type": "workingpaper",
        "description": abstract,
        "creators": [{"name": "Rice, James P Jr.", "affiliation": "Independent Researcher"}],
        "keywords": keywords,
        "access_right": "open",
        "license": "cc-by-4.0",
        "notes": (
            f"Generated autonomously by THESIS v6.3 (SHELL paper factory). "
            f"Average independent review score: {paper['avg_score']}/10 across "
            f"{paper['review_count']} AI reviewers (GPT-4o, Grok-3, Gemini 2.5). "
            f"Validation framework: Rice (2026), DOI: 10.5281/zenodo.19217024"
        ),
    }
    return metadata


def publish_to_zenodo(paper: dict, sandbox: bool = True) -> dict:
    """Publish a paper to Zenodo. Returns {doi, record_url, deposition_id}."""
    try:
        import requests
    except ImportError:
        print("ERROR: requests library required. Run: pip install requests")
        return {}

    base_url = SANDBOX_URL if sandbox else PRODUCTION_URL
    token = load_token(sandbox)
    if not token:
        env_label = "SANDBOX" if sandbox else "PRODUCTION"
        print(f"ERROR: No Zenodo {env_label} token found in api.env")
        return {}

    headers = {"Authorization": f"Bearer {token}"}
    headers_json = {**headers, "Content-Type": "application/json"}

    # Create deposition
    r = requests.post(f"{base_url}/deposit/depositions", json={}, headers=headers_json)
    if r.status_code != 201:
        print(f"ERROR: Failed to create deposition: {r.status_code} {r.text[:200]}")
        return {}
    deposition = r.json()
    dep_id = deposition["id"]

    # Upload best_paper.md
    paper_path = paper["path"] / "best_paper.md"
    with open(paper_path, "rb") as f:
        r = requests.post(
            f"{base_url}/deposit/depositions/{dep_id}/files",
            headers=headers,
            data={"filename": f"{paper['slug']}_paper.md"},
            files={"file": f},
        )
    if r.status_code not in (200, 201):
        print(f"ERROR: Failed to upload paper: {r.status_code}")
        return {}

    # Upload figures
    for fig_dir in [paper["path"] / "run1" / "figures", paper["path"] / "figures"]:
        if fig_dir.exists():
            for fig in fig_dir.glob("*.png"):
                with open(fig, "rb") as f:
                    requests.post(
                        f"{base_url}/deposit/depositions/{dep_id}/files",
                        headers=headers,
                        data={"filename": fig.name},
                        files={"file": f},
                    )

    # Upload reviews
    reviews_dir = paper["path"] / "reviews"
    if reviews_dir.exists():
        for review in reviews_dir.glob("*_review_*.md"):
            with open(review, "rb") as f:
                requests.post(
                    f"{base_url}/deposit/depositions/{dep_id}/files",
                    headers=headers,
                    data={"filename": review.name},
                    files={"file": f},
                )

    # Set metadata
    metadata = extract_metadata(paper)
    r = requests.put(
        f"{base_url}/deposit/depositions/{dep_id}",
        json={"metadata": metadata},
        headers=headers_json,
    )
    if r.status_code != 200:
        print(f"ERROR: Failed to set metadata: {r.status_code} {r.text[:200]}")
        return {}

    # Publish
    r = requests.post(
        f"{base_url}/deposit/depositions/{dep_id}/actions/publish",
        headers=headers,
    )
    if r.status_code != 202:
        print(f"ERROR: Failed to publish: {r.status_code} {r.text[:200]}")
        return {}

    result = r.json()
    doi = result.get("doi", "")
    record_url = result.get("links", {}).get("record_html", "")

    return {
        "doi": doi,
        "record_url": record_url,
        "deposition_id": dep_id,
        "published_at": datetime.now().isoformat(),
        "sandbox": sandbox,
    }


def review_sandbox_record(paper: dict, sandbox_result: dict) -> list[str]:
    """Review a sandbox record for errors before production publish.
    Returns list of issues. Items starting with BLOCK prevent production."""
    issues = []
    paper_path = paper["path"] / "best_paper.md"
    text = paper_path.read_text(encoding="utf-8", errors="replace")

    # 1. Check paper text for sensitive data
    sensitive_patterns = [
        (r"[A-Za-z0-9_\-]+_API_KEY", "API key reference found in paper text"),
        (r"C:\\[A-Za-z].*\\", "Windows file path found in paper text"),
        (r"/c/PROJECTS/", "Unix project path found in paper text"),
        (r"api\.env", "api.env reference found in paper text"),
        (r"sk-proj-[A-Za-z0-9]", "OpenAI API key pattern found"),
        (r"xai-[A-Za-z0-9]{10,}", "xAI API key pattern found"),
        (r"AIzaSy[A-Za-z0-9]{30,}", "Google API key pattern found"),
    ]
    for pattern, msg in sensitive_patterns:
        if re.search(pattern, text):
            issues.append(f"BLOCK: {msg}")

    # 2. Check for encoding artifacts
    encoding_hits = re.findall(r"\xc3\x87|\xc3\x82|\xc2\xb6|\xe2\x80[\x93\x94\x99\x9c\x9d]|\xef\xbb\xbf|[\u0080-\u009f]", text.encode("utf-8", errors="replace").decode("utf-8", errors="replace"))
    # Also check for common mojibake patterns
    encoding_hits += re.findall(r"&[a-z]+;|&#\d+;", text)  # HTML entities in markdown
    if len(encoding_hits) > 5:
        issues.append(f"BLOCK: {len(encoding_hits)} encoding artifacts found — paper will look broken on Zenodo")
    elif encoding_hits:
        issues.append(f"WARN: {len(encoding_hits)} minor encoding artifacts found")

    # 3. Check for remaining code blocks that should be figures
    figure_code = re.findall(r"```python\s*\n#\s*Figure", text)
    if figure_code:
        issues.append(f"BLOCK: {len(figure_code)} figure code blocks remain (should be image refs)")

    # 4. Check for placeholder text
    placeholders = re.findall(
        r"\[from code execution\]|\[placeholder\]|\[TODO\]|\[PASTE.*HERE\]|\[INSERT\]",
        text, re.IGNORECASE
    )
    if placeholders:
        issues.append(f"BLOCK: {len(placeholders)} placeholder text found")

    # 5. Check title is reasonable
    if len(paper["title"]) < 10:
        issues.append("BLOCK: Title too short — may be parsing error")
    if paper["title"].startswith("Figure") or paper["title"].startswith("Table"):
        issues.append("BLOCK: Title appears to be a figure/table caption, not a paper title")

    # 6. Check abstract exists and is reasonable
    abstract_match = re.search(
        r"##\s*Abstract\s*\n(.*?)(?=\n##|\n---|\n#[^#])",
        text, re.DOTALL
    )
    if not abstract_match:
        issues.append("BLOCK: No abstract section found")
    elif len(abstract_match.group(1).strip()) < 100:
        issues.append("WARN: Abstract is very short (< 100 chars)")

    # 7. Check figures exist on disk
    fig_refs = re.findall(r"!\[.*?\]\((.*?)\)", text)
    for fig_ref in fig_refs:
        fig_path = paper["path"] / fig_ref
        if not fig_path.exists():
            # Try relative to run1
            fig_path2 = paper["path"] / "run1" / fig_ref
            if not fig_path2.exists():
                issues.append(f"WARN: Referenced figure not found: {fig_ref}")

    # 8. Check that uploaded files include the paper
    if not sandbox_result.get("deposition_id"):
        issues.append("BLOCK: No deposition ID from sandbox — upload may have failed")

    # 9. Check for "illustrative" used with ASSAY-computed values
    assay_refs = re.findall(r"ASSAY", text)
    illustrative_near_assay = re.findall(
        r"illustrative.{0,100}ASSAY|ASSAY.{0,100}illustrative",
        text, re.IGNORECASE
    )
    if illustrative_near_assay:
        issues.append(f"WARN: 'illustrative' used near ASSAY references ({len(illustrative_near_assay)} instances)")

    # 10. Check references section exists
    if not re.search(r"##\s*References", text):
        issues.append("WARN: No References section found")

    # 11. Check paper isn't too short
    line_count = len(text.splitlines())
    if line_count < 100:
        issues.append(f"WARN: Paper is only {line_count} lines — may be incomplete")

    # 12. Check author name appears
    if "Rice" not in text and "rice" not in text.lower():
        issues.append("WARN: Author name not found in paper text")

    return issues


def display_table(papers: list[dict]):
    """Display papers in a table."""
    print()
    print("=" * 90)
    print(f"{'#':<3} {'Paper':<40} {'Score':<6} {'Rev':<4} {'Verdict':<12} {'Status':<12}")
    print("-" * 90)
    for i, p in enumerate(papers, 1):
        status = f"DOI: {p['doi'][:20]}" if p["published"] else "NOT PUBLISHED"
        score_str = f"{p['avg_score']:.2f}" if p["avg_score"] > 0 else "—"
        print(f"{i:<3} {p['title'][:38]:<40} {score_str:<6} {p['review_count']:<4} {p['verdict']:<12} {status:<12}")
    print("=" * 90)
    print()


def main():
    parser = argparse.ArgumentParser(description="THESIS Paper Publishing Manager")
    parser.add_argument("--list", action="store_true", help="List papers and exit")
    parser.add_argument("--publish", type=str, help="Publish papers: 'all' or comma-separated numbers")
    parser.add_argument("--sandbox-only", action="store_true", help="Only publish to sandbox, skip production")
    args = parser.parse_args()

    papers = scan_papers()
    if not papers:
        print("No papers found with best_paper.md")
        return

    # Sort by score descending
    papers.sort(key=lambda p: p["avg_score"], reverse=True)

    if args.list:
        display_table(papers)
        return

    display_table(papers)

    # Determine which to publish
    if args.publish:
        selection = args.publish
    else:
        selection = input("Publish which? (1-N, 'all', comma-separated, or 'q' to quit): ").strip()

    if selection.lower() in ("q", "quit", ""):
        print("Cancelled.")
        return

    if selection.lower() == "all":
        selected = list(range(len(papers)))
    else:
        try:
            selected = [int(x.strip()) - 1 for x in selection.split(",")]
        except ValueError:
            print("Invalid selection.")
            return

    # Pre-flight checks
    print("\n--- Pre-flight Checks ---\n")
    eligible = []
    for idx in selected:
        if idx < 0 or idx >= len(papers):
            print(f"  [{idx+1}] INVALID INDEX")
            continue
        p = papers[idx]
        passed, issues = preflight_check(p)
        status = "PASS" if passed else "FAIL"
        print(f"  [{idx+1}] {p['title'][:40]}: {status}")
        for issue in issues:
            print(f"      {issue}")
        if passed:
            eligible.append(p)

    if not eligible:
        print("\nNo papers passed pre-flight checks.")
        return

    print(f"\n{len(eligible)} paper(s) passed pre-flight. Publishing to SANDBOX first...\n")

    # Sandbox publish
    sandbox_results = {}
    for p in eligible:
        print(f"  Publishing to sandbox: {p['title'][:50]}...")
        result = publish_to_zenodo(p, sandbox=True)
        if result:
            sandbox_results[p["slug"]] = result
            print(f"    Sandbox DOI: {result.get('doi', 'N/A')}")
            print(f"    Record: {result.get('record_url', 'N/A')}")
        else:
            print(f"    SANDBOX FAILED — skipping this paper")

    if not sandbox_results:
        print("\nAll sandbox publishes failed.")
        return

    if args.sandbox_only:
        print(f"\n{len(sandbox_results)} papers published to SANDBOX only (--sandbox-only flag).")
        return

    # Agent review of sandbox records
    print(f"\n--- Agent Review of Sandbox Records ---\n")
    review_failures = []
    for p in eligible:
        if p["slug"] not in sandbox_results:
            continue
        sr = sandbox_results[p["slug"]]
        issues = review_sandbox_record(p, sr)
        if issues:
            print(f"  [{p['title'][:40]}]: {len(issues)} issue(s)")
            for issue in issues:
                print(f"    - {issue}")
            if any(i.startswith("BLOCK") for i in issues):
                review_failures.append(p["slug"])
        else:
            print(f"  [{p['title'][:40]}]: CLEAN")

    if review_failures:
        print(f"\n{len(review_failures)} paper(s) failed agent review. Fix before production.")
        eligible = [p for p in eligible if p["slug"] not in review_failures]
        if not eligible:
            print("No papers passed agent review.")
            return

    # Production confirmation
    print(f"\n{len(eligible)} paper(s) passed all checks (preflight + sandbox + agent review).")
    confirm = input("Publish to PRODUCTION? (yes/no): ").strip().lower()

    if confirm != "yes":
        print("Cancelled. Sandbox records remain.")
        return

    # Production publish
    print("\nPublishing to PRODUCTION...\n")
    manifest = load_manifest()

    for p in eligible:
        if p["slug"] not in sandbox_results:
            continue
        print(f"  Publishing: {p['title'][:50]}...")
        result = publish_to_zenodo(p, sandbox=False)
        if result:
            manifest[p["slug"]] = {
                "doi": result["doi"],
                "record_url": result["record_url"],
                "deposition_id": result["deposition_id"],
                "published_at": result["published_at"],
                "title": p["title"],
                "score": p["avg_score"],
                "reviews": p["review_count"],
            }
            print(f"    DOI: {result['doi']}")
            print(f"    URL: {result['record_url']}")

            # Save DOI to paper directory
            doi_file = p["path"] / "doi.txt"
            doi_file.write_text(result["doi"], encoding="utf-8")
        else:
            print(f"    PRODUCTION FAILED")

    save_manifest(manifest)
    print(f"\nPublished {len(manifest)} papers. Manifest saved to {MANIFEST_PATH}")


if __name__ == "__main__":
    main()
