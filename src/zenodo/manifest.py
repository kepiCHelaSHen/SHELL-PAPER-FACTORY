"""Published manifest tracking — state management for Zenodo uploads."""

import json
from pathlib import Path
from datetime import datetime

BASE = Path("C:/PROJECTS/SHELL")
MANIFEST_PATH = BASE / "published_manifest.json"


def load_manifest() -> dict:
    """Load the published manifest. Returns empty dict if not found."""
    if MANIFEST_PATH.exists():
        try:
            return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print(f"WARNING: Corrupt manifest at {MANIFEST_PATH}. Starting fresh.")
            return {}
    return {}


def save_manifest(manifest: dict):
    """Save the manifest to disk."""
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, default=str),
        encoding="utf-8"
    )


def is_published(slug: str, manifest: dict) -> bool:
    """Check if a paper has been published to production."""
    entry = manifest.get(slug, {})
    return entry.get("status") == "published"


def update_entry(slug: str, phase: str, data: dict, manifest: dict):
    """Update a manifest entry.

    phase: 'sandbox' or 'production'
    data: dict with deposition_id, doi, record_url, etc.
    """
    if slug not in manifest:
        manifest[slug] = {}

    manifest[slug][phase] = {
        **data,
        "published_at": datetime.now().isoformat(),
    }

    # Set overall status
    if phase == "production" and data.get("doi"):
        manifest[slug]["status"] = "published"
        manifest[slug]["doi"] = data["doi"]
    elif phase == "sandbox":
        manifest[slug]["status"] = "sandbox_only"

    save_manifest(manifest)
