"""Assemble upload bundle for a Zenodo deposition."""

import re
from pathlib import Path

BASE = Path("C:/PROJECTS/SHELL")


def find_figures(paper_dir: Path) -> list[Path]:
    """Find all figure files for a paper."""
    figures = []
    # Check multiple possible figure locations
    for fig_dir in [
        paper_dir / "run1" / "figures",
        paper_dir / "run2" / "figures",
        paper_dir / "run3" / "figures",
        paper_dir / "figures",
    ]:
        if fig_dir.exists():
            for f in sorted(fig_dir.iterdir()):
                if f.suffix.lower() in (".png", ".svg", ".pdf") and not f.name.startswith("."):
                    figures.append(f)
            if figures:
                break  # Use the first directory that has figures
    return figures


def extract_supplementary(paper_path: Path) -> str | None:
    """Extract Supplementary Materials section from paper."""
    text = paper_path.read_text(encoding="utf-8")
    match = re.search(r'^##\s+Supplementary Materials\s*\n(.*)', text,
                     re.MULTILINE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return None


def assemble_bundle(slug: str, pdf_path: Path | None) -> list[tuple[Path, str]]:
    """Assemble the complete upload bundle.

    Returns list of (local_path, upload_filename) tuples.
    """
    paper_dir = BASE / "papers" / slug
    best_paper = paper_dir / "best_paper.md"
    bundle = []

    # 1. PDF (if rendered)
    if pdf_path and pdf_path.exists():
        bundle.append((pdf_path, f"{slug}_paper.pdf"))

    # 2. Markdown source
    bundle.append((best_paper, f"{slug}_paper.md"))

    # 3. Supplementary materials as separate file (if present)
    supp_text = extract_supplementary(best_paper)
    if supp_text:
        supp_path = paper_dir / "supplementary_materials.md"
        supp_path.write_text(supp_text, encoding="utf-8")
        bundle.append((supp_path, f"{slug}_supplementary.md"))

    # 4. Figures (flat filenames — Zenodo doesn't support subdirectories)
    figures = find_figures(paper_dir)
    for fig in figures:
        bundle.append((fig, fig.name))

    return bundle
