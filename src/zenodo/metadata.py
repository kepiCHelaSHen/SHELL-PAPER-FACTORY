"""Build Zenodo metadata dict from paper content + config."""

import re
from pathlib import Path

BASE = Path("C:/PROJECTS/SHELL")


def extract_title(paper_path: Path) -> str:
    """Extract title from first '# ' heading in paper."""
    for line in paper_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return paper_path.parent.name  # fallback to slug


def extract_abstract(paper_path: Path) -> str:
    """Extract abstract section content."""
    text = paper_path.read_text(encoding="utf-8")
    match = re.search(r'##\s+Abstract\s*\n(.*?)(?=\n##\s|\Z)', text, re.DOTALL | re.IGNORECASE)
    if match:
        abstract = match.group(1).strip()
        # Truncate if too long (Zenodo has limits)
        if len(abstract) > 5000:
            abstract = abstract[:4997] + "..."
        return abstract
    return "Abstract not available."


def build_metadata(slug: str, config: dict) -> dict:
    """Build the full Zenodo metadata dict for a paper.

    Returns the dict ready to pass to ZenodoClient.set_metadata().
    """
    paper_path = BASE / "papers" / slug / "best_paper.md"
    title = extract_title(paper_path)
    abstract = extract_abstract(paper_path)

    # Author info from config
    author = config.get("author", {})
    creator = {"name": author.get("name", "Rice, James P Jr.")}
    if author.get("affiliation"):
        creator["affiliation"] = author["affiliation"]

    # Keywords: base + per-paper
    base_kw = config.get("base_keywords", [])
    paper_config = next((p for p in config.get("papers", []) if p["slug"] == slug), {})
    paper_kw = paper_config.get("keywords", [])
    keywords = base_kw + paper_kw

    # Notes
    notes = config.get("notes_template", "")

    # Build metadata
    metadata = {
        "title": title,
        "upload_type": "publication",
        "publication_type": config.get("publication_type", "workingpaper"),
        "description": abstract,
        "creators": [creator],
        "keywords": keywords,
        "access_right": "open",
        "license": config.get("license", "cc-by-4.0"),
        "notes": notes,
    }

    # Community (if specified)
    community = config.get("community")
    if community:
        metadata["communities"] = [{"identifier": community}]

    # Related identifiers (link to validation methodology paper)
    metadata["related_identifiers"] = [
        {
            "identifier": "10.5281/zenodo.19217024",
            "relation": "isDocumentedBy",
            "scheme": "doi"
        }
    ]

    return metadata
