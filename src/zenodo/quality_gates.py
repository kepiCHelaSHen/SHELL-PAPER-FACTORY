"""Pre-flight quality gates for Zenodo publication."""

import re
from pathlib import Path

BASE = Path("C:/PROJECTS/SHELL")


def parse_review_scores(review_path: Path) -> dict:
    """Extract key scores from a review file."""
    text = review_path.read_text(encoding="utf-8")
    result = {"dimensions": {}, "booleans": {}, "composite": None}

    # D-scores
    for match in re.finditer(r'\*\*D(\d{1,2})\.\s+[^*]+\*\*.*?(?:SCORE|Score):\s*(\d+)', text, re.DOTALL):
        result["dimensions"][f"D{match.group(1)}"] = int(match.group(2))

    # Composite
    comp = re.search(r'[Ww]eighted\s+[Cc]omposite\s*[=≈]\s*(\d+\.?\d*)', text)
    if comp:
        result["composite"] = float(comp.group(1))

    # B1 AI detection
    b1 = re.search(r'\*\*B1\..*?[Vv]erdict:?\s*\*?\*?\s*([A-Z][A-Z_]+)', text, re.DOTALL)
    if b1:
        result["booleans"]["B1"] = b1.group(1)

    # B3 Citation fabrication
    b3 = re.search(r'\*\*B3\..*?[Vv]erdict:?\s*\*?\*?\s*([A-Z][A-Z_]+)', text, re.DOTALL)
    if b3:
        result["booleans"]["B3"] = b3.group(1)

    return result


def run_quality_gates(slug: str, config: dict, manifest: dict) -> tuple[bool, list[str]]:
    """Run all pre-flight checks on a paper.

    Returns (pass, list_of_issues).
    """
    issues = []
    gates = config.get("quality_gates", {})
    paper_dir = BASE / "papers" / slug

    # 1. Paper exists
    best_paper = paper_dir / "best_paper.md"
    if not best_paper.exists():
        issues.append("FAIL: best_paper.md not found")
        return False, issues

    paper_text = best_paper.read_text(encoding="utf-8")
    paper_lines = paper_text.splitlines()

    if len(paper_lines) < 100:
        issues.append(f"FAIL: Paper too short ({len(paper_lines)} lines, need 100+)")

    # 2. Title extractable
    title_match = re.search(r'^#\s+(.+)', paper_text, re.MULTILINE)
    if not title_match:
        issues.append("FAIL: No '# Title' heading found in paper")

    # 3. Abstract exists
    if "## Abstract" not in paper_text and "## abstract" not in paper_text.lower():
        issues.append("FAIL: No '## Abstract' section found")

    # 4. Reviews exist
    reviews_dir = paper_dir / "reviews"
    min_reviewers = gates.get("min_reviewers", 2)
    review_files = []
    if reviews_dir.exists():
        review_files = [f for f in reviews_dir.iterdir()
                       if f.name.endswith(".md")
                       and not f.name.startswith(("gemini_", "gpt_", "grok_"))
                       and "_review_" in f.name]
    if len(review_files) < min_reviewers:
        issues.append(f"FAIL: Only {len(review_files)} reviews found (need {min_reviewers}+)")

    # 5-8. Score checks (only if reviews exist)
    if review_files:
        composites = []
        for rf in review_files:
            scores = parse_review_scores(rf)

            # Composite score
            if scores["composite"]:
                composites.append(scores["composite"])

            # Dimensional floor
            dim_floor = gates.get("auto_fail_dimension_below", 3)
            for dim, score in scores["dimensions"].items():
                if score <= dim_floor:
                    issues.append(f"WARN: {rf.name} has {dim}={score} (≤{dim_floor})")

            # B1 AI detection
            if gates.get("block_on_ai_detection", False):
                b1 = scores["booleans"].get("B1", "")
                if "YES_LIKELY_AI" in b1:
                    issues.append(f"FAIL: {rf.name} B1=YES_LIKELY_AI")

            # B3 Citation fabrication
            if gates.get("block_on_citation_fabrication", True):
                b3 = scores["booleans"].get("B3", "")
                if "LIKELY_FABRICATED" in b3:
                    issues.append(f"FAIL: {rf.name} B3=LIKELY_FABRICATED")

        # Average composite
        min_score = gates.get("min_composite_score", 7.5)
        if composites:
            avg = sum(composites) / len(composites)
            if avg < min_score:
                issues.append(f"FAIL: Average composite {avg:.2f} < {min_score}")

    # 9. Already published
    if slug in manifest and manifest[slug].get("status") == "published":
        issues.append("SKIP: Already published (in manifest)")
        return False, issues

    # Determine pass/fail
    has_fail = any(i.startswith("FAIL:") for i in issues)
    return not has_fail, issues
