"""Verify sandbox records before production publish.

Fetches each sandbox deposition and runs automated checks on:
- Title and description populated
- Files uploaded correctly (count, types, sizes)
- Metadata complete (keywords, license, author)
- Community tag present (if configured)
- No sensitive data leaked (API keys, file paths)

Usage:
    python -m src.zenodo.verify_sandbox
    python -m src.zenodo.verify_sandbox --papers DRUG_SPENDING
"""

import argparse
import re
import sys
from pathlib import Path

from .config import load_config, load_tokens, BASE
from .api import ZenodoClient, ZenodoAPIError
from .manifest import load_manifest


def check_deposition(client: ZenodoClient, dep_id: int, slug: str,
                     config: dict) -> tuple[list[str], list[str]]:
    """Check a sandbox deposition for issues.

    Returns (errors: list[str], warnings: list[str])
    """
    errors = []
    warnings = []

    try:
        dep = client.get_deposition(dep_id)
    except ZenodoAPIError as e:
        errors.append(f"Cannot fetch deposition {dep_id}: {e}")
        return errors, warnings

    metadata = dep.get("metadata", {})
    files = dep.get("files", [])

    # 1. Title check
    title = metadata.get("title", "")
    if not title or len(title) < 10:
        errors.append(f"Title too short or missing: '{title}'")
    if title.startswith("Figure") or title.startswith("Table"):
        errors.append(f"Title looks like a caption: '{title}'")

    # 2. Description/abstract
    desc = metadata.get("description", "")
    if not desc or len(desc) < 50:
        errors.append("Description/abstract missing or too short")
    if len(desc) > 5000:
        warnings.append(f"Description very long ({len(desc)} chars) — may display poorly")

    # 3. Files check
    if not files:
        errors.append("No files uploaded")
    else:
        filenames = [f.get("key", f.get("filename", "")) for f in files]
        has_paper = any("paper" in fn.lower() for fn in filenames)
        if not has_paper:
            errors.append(f"No paper file found. Files: {filenames}")

        # Check for zero-byte files
        for f in files:
            size = f.get("size", f.get("filesize", 0))
            name = f.get("key", f.get("filename", "unknown"))
            if size == 0:
                errors.append(f"Zero-byte file: {name}")
            elif size < 100:
                warnings.append(f"Very small file ({size} bytes): {name}")

    # 4. Keywords
    keywords = metadata.get("keywords", [])
    if not keywords:
        warnings.append("No keywords set")
    elif len(keywords) < 3:
        warnings.append(f"Only {len(keywords)} keywords (recommend 4+)")

    # 5. License
    license_val = metadata.get("license", {})
    if not license_val:
        errors.append("No license set")

    # 6. Author/creators
    creators = metadata.get("creators", [])
    if not creators:
        errors.append("No creators/authors set")
    elif not creators[0].get("name"):
        errors.append("Creator name is empty")

    # 7. Community check
    communities = metadata.get("communities", [])
    expected_community = config.get("community")
    if expected_community and not communities:
        warnings.append(f"Community '{expected_community}' not attached (may need to create it first)")

    # 8. Sensitive data in description
    sensitive_patterns = [
        (r'sk-proj-', "OpenAI API key pattern"),
        (r'xai-', "xAI API key pattern"),
        (r'AIzaSy', "Google API key pattern"),
        (r'C:\\\\', "Windows file path"),
        (r'/c/PROJECTS/', "Unix file path"),
        (r'api\.env', "api.env reference"),
        (r'ASSAY Report ASSAY-', "ASSAY internal report ID"),
    ]
    for pattern, label in sensitive_patterns:
        if re.search(pattern, desc, re.IGNORECASE):
            errors.append(f"SENSITIVE DATA in description: {label}")

    # 9. Notes/related identifiers
    notes = metadata.get("notes", "")
    if not notes:
        warnings.append("No notes field set")

    related = metadata.get("related_identifiers", [])
    if not related:
        warnings.append("No related identifiers (should link to validation methodology DOI)")

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description="Verify sandbox Zenodo records.")
    parser.add_argument("--papers", nargs="*", help="Specific slugs to check")
    args = parser.parse_args()

    config = load_config()
    tokens = load_tokens()
    manifest = load_manifest()
    client = ZenodoClient(tokens["sandbox"], sandbox=True)

    # Find sandbox entries in manifest
    entries = {}
    for slug, data in manifest.items():
        if "sandbox" in data and data["sandbox"].get("deposition_id"):
            if args.papers:
                if any(p in slug for p in args.papers):
                    entries[slug] = data["sandbox"]["deposition_id"]
            else:
                entries[slug] = data["sandbox"]["deposition_id"]

    if not entries:
        print("No sandbox records found in manifest.")
        print("Run: python -m src.zenodo --sandbox-only")
        return 1

    print(f"Verifying {len(entries)} sandbox records...\n")

    all_pass = True
    for slug, dep_id in sorted(entries.items()):
        short = slug.split("_2026")[0]
        print(f"  [{short}] (deposition {dep_id})")

        errors, warnings = check_deposition(client, dep_id, slug, config)

        if errors:
            all_pass = False
            for e in errors:
                print(f"    ERROR: {e}")
        if warnings:
            for w in warnings:
                print(f"    WARN:  {w}")
        if not errors and not warnings:
            print(f"    OK — all checks pass")
        print()

    if all_pass:
        print("=" * 50)
        print("ALL RECORDS PASS — ready for production publish.")
    else:
        print("=" * 50)
        print("ISSUES FOUND — fix before production publish.")

    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
