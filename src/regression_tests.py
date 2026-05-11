#!/usr/bin/env python3
"""
regression_tests.py -- Regression testing for the SHELL paper pipeline.

Detects when later paper versions regress by losing correct results that
earlier versions had (e.g., v3 uses wrong ordering direction when v2 had
it right). Extracts formal claims, numerical results, and citations from
a paper, saves them as a fixture, and compares subsequent versions against
that fixture.

Usage:
    python src/regression_tests.py --extract papers/SLUG_001/paper.md
    python src/regression_tests.py --check papers/SLUG_002/paper.md --against papers/SLUG_001/regression_fixtures.json
    python src/regression_tests.py --report papers/SLUG_002/paper.md --against papers/SLUG_001/regression_fixtures.json
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path
from typing import Optional

SIMILARITY_THRESHOLD = 0.8


@dataclass
class Claim:
    """A formal claim extracted from a paper (theorem, lemma, etc.)."""
    kind: str          # theorem, lemma, proposition, corollary, definition
    number: str        # e.g. "1", "2.3"
    name: Optional[str]  # e.g. "Bayesian Convergence" or None
    statement: str     # first paragraph after the header

    @property
    def label(self) -> str:
        if self.name:
            return f"{self.kind} {self.number} ({self.name})"
        return f"{self.kind} {self.number}"


@dataclass
class Citation:
    """A citation extracted from the References section."""
    raw: str
    author: str
    year: str
    title: str


@dataclass
class RegressionReport:
    """Result of comparing a new paper against a fixture."""
    missing_theorems: list = field(default_factory=list)
    changed_theorems: list = field(default_factory=list)
    missing_citations: list = field(default_factory=list)
    missing_numbers: list = field(default_factory=list)
    new_theorems: list = field(default_factory=list)
    new_citations: list = field(default_factory=list)
    verdict: str = "CONSISTENT"

    def compute_verdict(self):
        if self.missing_theorems or self.changed_theorems or self.missing_citations or self.missing_numbers:
            self.verdict = "REGRESSION"
        elif self.new_theorems or self.new_citations:
            self.verdict = "EXTENDED"
        else:
            self.verdict = "CONSISTENT"

    def summary(self) -> str:
        lines = [f"Verdict: {self.verdict}"]
        if self.missing_theorems:
            lines.append(f"  MISSING theorems/lemmas ({len(self.missing_theorems)}):")
            for t in self.missing_theorems:
                lines.append(f"    - {t}")
        if self.changed_theorems:
            lines.append(f"  CHANGED theorems/lemmas ({len(self.changed_theorems)}):")
            for label, sim in self.changed_theorems:
                lines.append(f"    - {label} (similarity: {sim:.2f})")
        if self.missing_citations:
            lines.append(f"  MISSING citations ({len(self.missing_citations)}):")
            for c in self.missing_citations:
                lines.append(f"    - {c}")
        if self.missing_numbers:
            lines.append(f"  MISSING numerical results ({len(self.missing_numbers)}):")
            for n in self.missing_numbers:
                lines.append(f"    - {n}")
        if self.new_theorems:
            lines.append(f"  NEW theorems/lemmas ({len(self.new_theorems)}):")
            for t in self.new_theorems:
                lines.append(f"    - {t}")
        if self.new_citations:
            lines.append(f"  NEW citations ({len(self.new_citations)}):")
            for c in self.new_citations:
                lines.append(f"    - {c}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Extraction
# ---------------------------------------------------------------------------

_CLAIM_PATTERN = re.compile(
    r"\*\*(?P<kind>Theorem|Lemma|Proposition|Corollary|Definition)\s+"
    r"(?P<number>[\d.]+)"
    r"(?:\s*\((?P<name>[^)]+)\))?"
    r"\.\*\*\s*"
    r"(?P<statement>.+?)(?=\n\n|\n\*\*|\Z)",
    re.DOTALL | re.IGNORECASE,
)

_NUMBER_PATTERN = re.compile(
    r"(?:[≈=]\s*(\d+(?:\.\d+)?(?:%|\\%)?)|"
    r"(\d+(?:,\d{3})+(?:\.\d+)?)|"
    r"(\d+\.\d{2,}))"
)

_CITATION_PATTERN = re.compile(
    r"^\s*(?:\[[\d\w]+\]\s*)?(.+?)\s*[(\[]((?:19|20)\d{2})[)\]]\s*[.,]?\s*[\"\"\"]*(.+?)[\"\"\"]*[.,]?\s*$",
    re.MULTILINE,
)


def _extract_claims(text: str) -> list[dict]:
    """Extract formal claims (theorems, lemmas, etc.) from paper markdown."""
    claims = []
    for m in _CLAIM_PATTERN.finditer(text):
        statement = m.group("statement").strip()
        statement = re.sub(r"\s+", " ", statement)
        claims.append({
            "kind": m.group("kind").lower(),
            "number": m.group("number"),
            "name": m.group("name"),
            "statement": statement,
        })
    return claims


def _extract_abstract_claims(text: str) -> list[str]:
    """Extract key claims from the Abstract section."""
    abstract_match = re.search(
        r"#+\s*Abstract\s*\n(.*?)(?=\n#+\s|\Z)", text, re.DOTALL | re.IGNORECASE
    )
    if not abstract_match:
        abstract_match = re.search(
            r"\*\*Abstract[\.:]*\*\*\s*(.*?)(?=\n#+\s|\n\*\*|\Z)", text, re.DOTALL | re.IGNORECASE
        )
    if not abstract_match:
        return []
    abstract_text = abstract_match.group(1).strip()
    sentences = re.split(r"(?<=[.!?])\s+", abstract_text)
    claim_keywords = re.compile(r"\b(show|prove|demonstrate|establish|find|result|bound|converge)", re.IGNORECASE)
    return [s.strip() for s in sentences if claim_keywords.search(s)]


def _extract_numbers(text: str) -> list[str]:
    """Extract key numerical results from the paper."""
    numbers = set()
    for m in _NUMBER_PATTERN.finditer(text):
        val = m.group(1) or m.group(2) or m.group(3)
        if val:
            numbers.add(val)
    return sorted(numbers)


def _extract_citations(text: str) -> list[dict]:
    """Extract citations from the References section."""
    ref_match = re.search(r"#+\s*References\s*\n(.*)", text, re.DOTALL | re.IGNORECASE)
    if not ref_match:
        return []
    ref_text = ref_match.group(1)
    citations = []
    for m in _CITATION_PATTERN.finditer(ref_text):
        citations.append({
            "author": m.group(1).strip().rstrip(",").strip(),
            "year": m.group(2),
            "title": m.group(3).strip().rstrip(".").strip(),
            "raw": m.group(0).strip(),
        })
    if not citations:
        for line in ref_text.strip().splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            line = re.sub(r"^\s*[-\d\[\].*]+\s*", "", line)
            if len(line) > 10:
                year_match = re.search(r"((?:19|20)\d{2})", line)
                citations.append({
                    "author": line[:60].split(",")[0].split("(")[0].strip(),
                    "year": year_match.group(1) if year_match else "",
                    "title": line[:120],
                    "raw": line,
                })
    return citations


def _extract_metadata(paper_path: Path) -> dict:
    """Extract metadata from the paper path and content."""
    parts = paper_path.parent.name.split("_")
    version = parts[-1] if parts and parts[-1].isdigit() else "1"
    slug = "_".join(parts[:-1]) if len(parts) > 1 and parts[-1].isdigit() else paper_path.parent.name
    return {
        "slug": slug,
        "version": version,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "source_file": str(paper_path),
    }


def extract_fixtures(paper_path: str | Path) -> dict:
    """Extract all testable claims from a paper and return as a fixture dict."""
    paper_path = Path(paper_path)
    text = paper_path.read_text(encoding="utf-8")
    return {
        "metadata": _extract_metadata(paper_path),
        "claims": _extract_claims(text),
        "abstract_claims": _extract_abstract_claims(text),
        "numerical_results": _extract_numbers(text),
        "citations": _extract_citations(text),
    }


def save_fixtures(fixtures: dict, output_path: str | Path):
    """Save fixture dict to a JSON file."""
    output_path = Path(output_path)
    output_path.write_text(json.dumps(fixtures, indent=2, ensure_ascii=False), encoding="utf-8")


def _similarity(a: str, b: str) -> float:
    """Compute normalized similarity between two strings."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def _find_claim_in_list(target: dict, claims: list[dict]) -> tuple[Optional[dict], float]:
    """Find the best matching claim in a list, returning (match, similarity)."""
    best_match = None
    best_sim = 0.0
    for c in claims:
        if c["kind"] != target["kind"]:
            continue
        if c["number"] == target["number"] or (target["name"] and c.get("name") == target["name"]):
            sim = _similarity(target["statement"], c["statement"])
            if sim > best_sim:
                best_sim = sim
                best_match = c
    return best_match, best_sim


def check_regressions(new_paper_path: str | Path, fixture_path: str | Path) -> RegressionReport:
    """Compare a new paper against a saved fixture and report regressions."""
    new_paper_path = Path(new_paper_path)
    fixture_path = Path(fixture_path)

    old = json.loads(fixture_path.read_text(encoding="utf-8"))
    new = extract_fixtures(new_paper_path)
    report = RegressionReport()

    old_claims = old.get("claims", [])
    new_claims = new.get("claims", [])

    for oc in old_claims:
        label = f"{oc['kind']} {oc['number']}" + (f" ({oc['name']})" if oc.get("name") else "")
        match, sim = _find_claim_in_list(oc, new_claims)
        if match is None:
            report.missing_theorems.append(label)
        elif sim < SIMILARITY_THRESHOLD:
            report.changed_theorems.append((label, sim))

    old_labels = {(c["kind"], c["number"]) for c in old_claims}
    for nc in new_claims:
        if (nc["kind"], nc["number"]) not in old_labels:
            label = f"{nc['kind']} {nc['number']}" + (f" ({nc['name']})" if nc.get("name") else "")
            report.new_theorems.append(label)

    old_nums = set(old.get("numerical_results", []))
    new_nums = set(new.get("numerical_results", []))
    report.missing_numbers = sorted(old_nums - new_nums)

    old_cites = {(c["author"], c["year"]) for c in old.get("citations", [])}
    new_cites = {(c["author"], c["year"]) for c in new.get("citations", [])}
    for author, year in old_cites - new_cites:
        report.missing_citations.append(f"{author} ({year})")
    for author, year in new_cites - old_cites:
        report.new_citations.append(f"{author} ({year})")

    report.compute_verdict()
    return report


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    """CLI entry point for regression testing."""
    parser = argparse.ArgumentParser(
        description="Regression testing for SHELL paper pipeline"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--extract", metavar="PAPER", help="Extract claims and save fixture")
    group.add_argument("--check", metavar="PAPER", help="Compare paper against fixture and save new fixture")
    group.add_argument("--report", metavar="PAPER", help="Compare paper against fixture (report only)")
    parser.add_argument("--against", metavar="FIXTURE", help="Path to fixture JSON for comparison")
    parser.add_argument("--output", metavar="PATH", help="Override output path for fixture JSON")

    args = parser.parse_args()

    if args.extract:
        paper_path = Path(args.extract)
        if not paper_path.exists():
            print(f"Error: {paper_path} not found", file=sys.stderr)
            sys.exit(1)
        fixtures = extract_fixtures(paper_path)
        out_path = Path(args.output) if args.output else paper_path.parent / "regression_fixtures.json"
        save_fixtures(fixtures, out_path)
        n_claims = len(fixtures["claims"])
        n_cites = len(fixtures["citations"])
        n_nums = len(fixtures["numerical_results"])
        print(f"Extracted {n_claims} claims, {n_cites} citations, {n_nums} numerical results")
        print(f"Fixture saved to {out_path}")

    elif args.check or args.report:
        paper_path = Path(args.check or args.report)
        if not paper_path.exists():
            print(f"Error: {paper_path} not found", file=sys.stderr)
            sys.exit(1)
        if not args.against:
            print("Error: --against is required for --check and --report", file=sys.stderr)
            sys.exit(1)
        fixture_path = Path(args.against)
        if not fixture_path.exists():
            print(f"Error: {fixture_path} not found", file=sys.stderr)
            sys.exit(1)

        report = check_regressions(paper_path, fixture_path)
        print(report.summary())

        if args.check:
            new_fixtures = extract_fixtures(paper_path)
            out_path = Path(args.output) if args.output else paper_path.parent / "regression_fixtures.json"
            save_fixtures(new_fixtures, out_path)
            print(f"\nNew fixture saved to {out_path}")

        if report.verdict == "REGRESSION":
            sys.exit(1)


if __name__ == "__main__":
    main()
