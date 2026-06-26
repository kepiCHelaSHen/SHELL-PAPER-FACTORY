#!/usr/bin/env python3
"""Generate a targeted revision brief from external reviews.

Reads review files, extracts the Minimum Viable Revision items and weakest
features, and produces a structured revision brief that can be used to
dispatch a targeted revision agent.

Usage:
  python scripts/revise_from_review.py SLUG                    # Latest reviews, print brief
  python scripts/revise_from_review.py SLUG --date 2026-05-15  # Specific date
  python scripts/revise_from_review.py SLUG --dry-run          # Just print, don't save

The revision brief is saved to: papers/[SLUG]/revision_brief_YYYY-MM-DD.md
"""

import argparse
import re
import sys
from pathlib import Path
from datetime import date

BASE = Path(__file__).resolve().parent.parent


def extract_section(text: str, heading_pattern: str) -> str:
    """Extract text under a markdown heading until the next heading of same or higher level."""
    match = re.search(heading_pattern, text, re.MULTILINE)
    if not match:
        return ""
    start = match.end()
    # Find next heading of same or higher level
    level = text[match.start():match.end()].count('#')
    next_heading = re.search(r'^#{1,' + str(level) + r'}\s', text[start:], re.MULTILINE)
    end = start + next_heading.start() if next_heading else len(text)
    return text[start:end].strip()


def extract_revision_items(review_path: Path) -> list[str]:
    """Parse the '4H. Minimum Viable Revision' section."""
    text = review_path.read_text(encoding="utf-8")
    section = extract_section(text, r'^###?\s+4H\.?\s+Minimum Viable Revision')
    if not section:
        return []
    # Extract numbered items or bullet points
    items = re.findall(r'^\s*(?:\d+\.|\-|\*)\s+(.+)', section, re.MULTILINE)
    return items if items else [section.strip()]


def extract_weaknesses(review_path: Path) -> list[str]:
    """Parse the '4C. Weakest Features' section."""
    text = review_path.read_text(encoding="utf-8")
    section = extract_section(text, r'^###?\s+4C\.?\s+Weakest Features')
    if not section:
        return []
    items = re.findall(r'^\s*(?:\d+\.|\-|\*)\s+(.+)', section, re.MULTILINE)
    return items if items else [section.strip()]


def extract_low_scores(review_path: Path, threshold: int = 5) -> list[tuple[str, int, str]]:
    """Find D-scores at or below threshold with their dimension names."""
    text = review_path.read_text(encoding="utf-8")
    results = []
    matches = re.findall(
        r'\*\*D(\d{1,2})\.\s+([^*]+)\*\*.*?(?:SCORE|Score):\s*(\d+)',
        text, re.DOTALL
    )
    for dim_num, dim_name, score in matches:
        if int(score) <= threshold:
            results.append((f"D{dim_num}", int(score), dim_name.strip()))
    return results


def extract_adversarial_test(review_path: Path) -> str:
    """Parse the '4G. Adversarial Stress Test' section."""
    text = review_path.read_text(encoding="utf-8")
    return extract_section(text, r'^###?\s+4G\.?\s+Adversarial Stress Test')


def find_reviews(slug: str, date_str: str | None = None) -> dict[str, Path]:
    """Find review files for a given slug and optional date."""
    papers_dir = BASE / "papers"
    # Find the paper directory
    matching_dirs = [d for d in papers_dir.iterdir() if d.is_dir() and d.name.startswith(slug)]
    if not matching_dirs:
        return {}
    paper_dir = matching_dirs[0]
    reviews_dir = paper_dir / "reviews"
    if not reviews_dir.exists():
        return {}

    result = {}
    for f in sorted(reviews_dir.iterdir()):
        if not f.name.endswith(".md"):
            continue
        # Skip legacy files
        if f.name.startswith(("gemini_", "gpt_", "grok_")):
            continue
        match = re.match(r'^(.+?)_review_(\d{4}-\d{2}-\d{2})\.md$', f.name)
        if not match:
            continue
        model = match.group(1)
        file_date = match.group(2)
        if date_str and file_date != date_str:
            continue
        # Take latest if no date specified
        result[model] = f

    return result


def build_revision_brief(slug: str, reviews: dict[str, Path]) -> str:
    """Combine feedback from all reviewers into a unified revision brief."""
    lines = []
    lines.append(f"# REVISION BRIEF — {slug}")
    lines.append(f"# Generated: {date.today().isoformat()}")
    lines.append(f"# Sources: {', '.join(reviews.keys())}")
    lines.append("")
    lines.append("## Instructions for Revision Agent")
    lines.append("")
    lines.append("Address each item below. Make TARGETED edits only.")
    lines.append("Do NOT rewrite the entire paper. Preserve all content not flagged.")
    lines.append("Save revised paper to the next run directory.")
    lines.append("")

    for model, path in sorted(reviews.items()):
        lines.append(f"---")
        lines.append(f"## From {model}")
        lines.append("")

        # Minimum viable revision
        items = extract_revision_items(path)
        if items:
            lines.append("### Minimum Viable Revision")
            for i, item in enumerate(items, 1):
                lines.append(f"{i}. {item}")
            lines.append("")

        # Weaknesses
        weaknesses = extract_weaknesses(path)
        if weaknesses:
            lines.append("### Weakest Features")
            for w in weaknesses:
                lines.append(f"- {w}")
            lines.append("")

        # Low scores
        low = extract_low_scores(path)
        if low:
            lines.append("### Low-Scoring Dimensions (≤5)")
            for dim, score, name in low:
                lines.append(f"- **{dim} ({name})**: {score}/10")
            lines.append("")

        # Adversarial stress test
        stress = extract_adversarial_test(path)
        if stress:
            lines.append("### Adversarial Stress Test to Address")
            lines.append(stress)
            lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate revision brief from reviews.")
    parser.add_argument("slug", help="Paper slug (or prefix)")
    parser.add_argument("--date", type=str, default=None,
                       help="Review date (YYYY-MM-DD). Default: latest.")
    parser.add_argument("--dry-run", action="store_true",
                       help="Print brief without saving to file.")
    parser.add_argument("--threshold", type=int, default=5,
                       help="Score threshold for flagging low dimensions (default: 5)")
    args = parser.parse_args()

    reviews = find_reviews(args.slug, args.date)
    if not reviews:
        print(f"No reviews found for '{args.slug}'" +
              (f" on date {args.date}" if args.date else ""))
        return 1

    brief = build_revision_brief(args.slug, reviews)
    print(brief)

    if not args.dry_run:
        # Find paper directory and save
        papers_dir = BASE / "papers"
        matching_dirs = [d for d in papers_dir.iterdir()
                        if d.is_dir() and d.name.startswith(args.slug)]
        if matching_dirs:
            date_str = args.date or date.today().isoformat()
            out_path = matching_dirs[0] / f"revision_brief_{date_str}.md"
            out_path.write_text(brief, encoding="utf-8")
            print(f"\nBrief saved to: {out_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
