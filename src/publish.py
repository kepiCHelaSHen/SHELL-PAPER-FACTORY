#!/usr/bin/env python3
"""
publish.py — Zenodo uploader for SHELL paper factory.
Run AFTER you have read and approved papers/[SLUG]/paper.md.

Usage:
    python src/publish.py --slug SLUG [--sandbox]

Requires:
    ZENODO_TOKEN in api.env (sandbox token and production token are different)

Flow:
    1. Reads papers/[SLUG]/paper.md
    2. Reads papers/[SLUG]/figures/ (if any)
    3. Creates a new Zenodo deposition (sandbox by default)
    4. Uploads paper + figures
    5. Sets metadata (title, description, author)
    6. Publishes and returns DOI
    7. Writes DOI to papers/[SLUG]/doi.txt
"""

import argparse
import json
import os
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

SANDBOX_URL = "https://sandbox.zenodo.org/api"
PRODUCTION_URL = "https://zenodo.org/api"
PAPERS_DIR = Path("papers")
API_ENV = Path("api.env")


def load_token(sandbox: bool) -> str:
    """Load Zenodo token from api.env."""
    key = "ZENODO_SANDBOX_TOKEN" if sandbox else "ZENODO_TOKEN"
    if not API_ENV.exists():
        sys.exit(f"ERROR: api.env not found. Add {key}=your_token to api.env.")
    for line in API_ENV.read_text().splitlines():
        if line.startswith(key + "="):
            return line.split("=", 1)[1].strip()
    sys.exit(f"ERROR: {key} not found in api.env.")


# ---------------------------------------------------------------------------
# Zenodo API helpers
# ---------------------------------------------------------------------------

def _auth_headers(token: str, content_type: str = None) -> dict:
    """Build Authorization header. Never pass token as URL query parameter."""
    headers = {"Authorization": f"Bearer {token}"}
    if content_type:
        headers["Content-Type"] = content_type
    return headers


def create_deposition(base_url: str, token: str) -> dict:
    import requests
    r = requests.post(
        f"{base_url}/deposit/depositions",
        json={},
        headers=_auth_headers(token, "application/json"),
    )
    r.raise_for_status()
    return r.json()


def upload_file(base_url: str, token: str, deposition_id: int, filepath: Path):
    import requests
    bucket_url = f"{base_url}/deposit/depositions/{deposition_id}/files"
    with open(filepath, "rb") as f:
        r = requests.post(
            bucket_url,
            headers=_auth_headers(token),
            data={"filename": filepath.name},
            files={"file": f},
        )
    r.raise_for_status()
    print(f"  Uploaded: {filepath.name}")


def set_metadata(base_url: str, token: str, deposition_id: int, metadata: dict):
    import requests
    r = requests.put(
        f"{base_url}/deposit/depositions/{deposition_id}",
        json={"metadata": metadata},
        headers=_auth_headers(token, "application/json"),
    )
    r.raise_for_status()


def publish(base_url: str, token: str, deposition_id: int) -> str:
    import requests
    r = requests.post(
        f"{base_url}/deposit/depositions/{deposition_id}/actions/publish",
        headers=_auth_headers(token),
    )
    r.raise_for_status()
    doi = r.json()["doi"]
    return doi


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Upload a paper to Zenodo.")
    parser.add_argument("--slug", required=True, help="Paper slug (folder name under papers/)")
    parser.add_argument("--sandbox", action="store_true", default=True,
                        help="Use Zenodo sandbox (default: True). Pass --no-sandbox for production.")
    parser.add_argument("--no-sandbox", dest="sandbox", action="store_false")
    args = parser.parse_args()

    paper_dir = PAPERS_DIR / args.slug
    paper_file = paper_dir / "paper.md"

    if not paper_file.exists():
        sys.exit(f"ERROR: {paper_file} not found. Has the paper been written and approved?")

    base_url = SANDBOX_URL if args.sandbox else PRODUCTION_URL
    env_label = "SANDBOX" if args.sandbox else "PRODUCTION"
    token = load_token(args.sandbox)

    print(f"\n📤 Publishing '{args.slug}' to Zenodo {env_label}")
    print(f"   Base URL: {base_url}\n")

    # Prompt for metadata (kept simple — extend as needed)
    title = input("Paper title: ").strip()
    description = input("One-sentence description: ").strip()
    author_name = input("Author name [James P Rice Jr.]: ").strip() or "James P Rice Jr."
    affiliation = input("Affiliation (or press Enter to skip): ").strip()

    author_entry = {"name": author_name}
    if affiliation:
        author_entry["affiliation"] = affiliation

    metadata = {
        "title": title,
        "upload_type": "publication",
        "publication_type": "preprint",
        "description": description,
        "creators": [author_entry],
        "access_right": "open",
        "license": "cc-by",
    }

    # Create deposition
    print("Creating deposition...")
    dep = create_deposition(base_url, token)
    dep_id = dep["id"]
    print(f"  Deposition ID: {dep_id}")

    # Upload paper
    print("Uploading files...")
    upload_file(base_url, token, dep_id, paper_file)

    # Upload figures if any
    figures_dir = paper_dir / "figures"
    if figures_dir.exists():
        for fig in sorted(figures_dir.iterdir()):
            if fig.is_file() and not fig.name.startswith("."):
                upload_file(base_url, token, dep_id, fig)

    # Set metadata
    print("Setting metadata...")
    set_metadata(base_url, token, dep_id, metadata)

    # Publish
    print("Publishing...")
    doi = publish(base_url, token, dep_id)

    # Save DOI
    doi_file = paper_dir / "doi.txt"
    doi_file.write_text(doi)

    print(f"\n✅ Published successfully.")
    print(f"   DOI: {doi}")
    print(f"   Saved to: {doi_file}")
    if args.sandbox:
        print(f"\n   ⚠️  This was SANDBOX. Run with --no-sandbox to publish for real.")


if __name__ == "__main__":
    main()
