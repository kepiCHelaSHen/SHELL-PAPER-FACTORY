#!/usr/bin/env python3
"""
consolidate.py — Extract and consolidate Steelman findings and dead-ends
across all SHELL paper runs into central logs.

Usage:
    python src/consolidate.py --backfill                    # One-time: populate from all existing files
    python src/consolidate.py --critique <path>             # Append from a single steelman critique
    python src/consolidate.py --dead-ends <path>            # Append from a single dead_ends file
    python src/consolidate.py --universal                   # Show high-recurrence items (2+ papers)
"""

import argparse
import re
from dataclasses import dataclass, field
from filelock import FileLock
from pathlib import Path
from typing import Optional


SHELL_ROOT = Path(__file__).parent.parent
FINDINGS_LOG = SHELL_ROOT / "STEELMAN_FINDINGS.md"
DEAD_ENDS_LOG = SHELL_ROOT / "DEAD_ENDS.md"

# --- Category rules ---

FINDING_CATEGORIES = [
    ("MATH_ERROR", [
        "proof", "theorem", "lemma", "contradict", "wrong result",
        "incorrect", "error in", "moment condition", "corollary",
        "invokes.*incorrectly", "missing condition",
    ]),
    ("SPEC_MATH_MISMATCH", [
        "spec", "promises", "cannot deliver", "phase transition",
        "does not deliver", "model cannot", "mathematically impossible",
    ]),
    ("ASSEMBLY_ERROR", [
        "duplicate", "tombstone", "placeholder", "assembly error",
        "appear twice", "sections.*twice", "missing proof",
    ]),
    ("CITATION_ERROR", [
        "citation", "reference", "orphan", "mischaracteriz", "cited",
        "wrong year", "cite.*source",
    ]),
    ("PROOF_STRATEGY_DRIFT", [
        "proof strategy", "technique", "hand-wav", "trivializ",
        "mean-field", "lineariz.*fail",
    ]),
    ("AUTHOR_TENDENCY", [
        "moraliz", "tautological", "asserted.*not derived",
        "scope disguise", "overclaim", "overstate", "stronger than.*supports",
        "under-defended", "circular", "load-bearing.*assumption",
    ]),
    ("FRAMING_OVERCLAIM", [
        "novelty", "inflation", "exaggerat", "oversell",
        "contribution.*not.*hard", "straightforward",
    ]),
]

DEAD_END_TYPES = [
    ("math_error", [
        "proof", "theorem", "lemma", "contradict", "wrong",
        "incorrect", "counterexample",
    ]),
    ("spec_impossible", [
        "spec", "cannot deliver", "phase transition",
        "mathematically impossible", "math cannot",
    ]),
    ("author_hallucination", [
        "placeholder", "from code execution", "empty",
        "fabricat", "hallucin", "does not execute",
    ]),
    ("citation_error", [
        "citation", "reference", "survey.*not.*theoretical",
        "mischaracteriz", "orphan",
    ]),
    ("scope_disguise", [
        "open problem", "future work", "limitation.*not",
        "scope disguise",
    ]),
    ("terminology_error", [
        "terminology", "sufficient statistic", "wrong term",
        "technical term",
    ]),
    ("assumed_not_derived", [
        "assumed.*not derived", "asserted.*not derived",
        "assumption.*derivation", "tautolog",
    ]),
    ("proof_technique_failed", [
        "proof.*fail", "technique.*fail", "approach.*fail",
        "decreasing.*order", "ordering.*error",
    ]),
    ("framing_overclaim", [
        "novelty.*overclaim", "oversell", "overclaim",
        "exaggerat", "inflat",
    ]),
    ("assembly_error", [
        "duplicate", "tombstone", "assembly", "absent",
        "missing proof", "sections.*twice",
    ]),
]


# --- Data classes ---

@dataclass
class Finding:
    id: str
    category: str
    title: str
    paper: str
    run: str
    severity: str
    detail: str
    recurrence: int = 1


@dataclass
class DeadEnd:
    id: str
    type_tag: str
    title: str
    paper: str
    version: str
    tried: str
    failed: str


# --- Parsing ---

def extract_paper_name(path: Path) -> str:
    """Extract paper name from path like papers/CONSPIRACY_BAYES_2026-05-12_001/."""
    name = path.parent.name
    # Strip date and sequence: CONSPIRACY_BAYES_2026-05-12_001 -> CONSPIRACY_BAYES
    cleaned = re.sub(r"_\d{4}-\d{2}-\d{2}_\d{3}$", "", name)
    return cleaned


def extract_run_number(path: Path) -> str:
    """Extract run number from directory name like ..._001."""
    match = re.search(r"_(\d{3})$", path.parent.name)
    return match.group(1) if match else "?"


def categorize_finding(text: str, section: str) -> str:
    """Assign a category based on keyword matching."""
    text_lower = text.lower()
    for category, keywords in FINDING_CATEGORIES:
        for kw in keywords:
            if re.search(kw, text_lower):
                return category
    # Fallback by section
    if section == "structural":
        return "MATH_ERROR"
    if section == "framing":
        return "FRAMING_OVERCLAIM"
    return "AUTHOR_TENDENCY"


def categorize_dead_end(text: str) -> str:
    """Assign a type tag based on keyword matching."""
    text_lower = text.lower()
    for type_tag, keywords in DEAD_END_TYPES:
        for kw in keywords:
            if re.search(kw, text_lower):
                return type_tag
    return "math_error"  # safe default


def parse_steelman_critique(path: Path) -> list[Finding]:
    """Parse a steelman_full_paper_critique.md into typed findings."""
    text = path.read_text(encoding="utf-8", errors="replace")
    paper = extract_paper_name(path)
    run = extract_run_number(path)
    findings = []

    sections = {
        "structural": "",
        "framing": "",
        "minor": "",
    }

    # Split into sections (include parenthetical like "(would cause rejection)")
    parts = re.split(r"(##\s*(?:STRUCTURAL ISSUES|FRAMING & POSITIONING|MINOR ISSUES|VERDICT|REVISION INSTRUCTIONS)[^\n]*)", text)

    current_section = None
    for part in parts:
        part_stripped = part.strip()
        if re.match(r"##\s*STRUCTURAL ISSUES", part_stripped):
            current_section = "structural"
        elif re.match(r"##\s*FRAMING", part_stripped):
            current_section = "framing"
        elif re.match(r"##\s*MINOR", part_stripped):
            current_section = "minor"
        elif re.match(r"##\s*(VERDICT|REVISION)", part_stripped):
            current_section = None
        elif current_section:
            sections[current_section] = part_stripped

    # Extract individual items from each section
    for section_name, section_text in sections.items():
        if not section_text or "none identified" in section_text.lower():
            continue

        severity = {
            "structural": "STRUCTURAL",
            "framing": "FRAMING",
            "minor": "MINOR",
        }[section_name]

        # Split on numbered items
        items = re.split(r"\n\s*\d+\.\s+", "\n" + section_text)
        for item in items:
            item = item.strip()
            if not item or len(item) < 20:
                continue
            # Skip section header remnants
            if re.match(r"^\(would (cause|appear)", item, re.IGNORECASE):
                continue
            if item.lower().startswith("none identified"):
                continue

            # Extract bold title if present
            title_match = re.match(r"\*\*(.+?)\*\*", item)
            title = title_match.group(1).rstrip(".") if title_match else item[:80]

            # First sentence as detail
            detail = item.split("\n")[0]
            if len(detail) > 200:
                detail = detail[:197] + "..."

            category = categorize_finding(item, section_name)

            findings.append(Finding(
                id="",  # assigned later
                category=category,
                title=title,
                paper=paper,
                run=run,
                severity=severity,
                detail=detail,
            ))

    return findings


def parse_dead_ends(path: Path) -> list[DeadEnd]:
    """Parse a dead_ends.md into typed dead-ends."""
    text = path.read_text(encoding="utf-8", errors="replace")
    paper = extract_paper_name(path)

    # Try to extract version from headers
    version_match = re.search(r"(V\d+|v\d+)", path.parent.name)
    version = version_match.group(1) if version_match else "v1"

    dead_ends = []

    # Try v5 format first: [Turn N] Run M MX REJECT: ...
    v5_items = re.split(r"\n(?=\[Turn \d+\])", "\n" + text)
    v5_items = [i.strip() for i in v5_items if re.match(r"\[Turn \d+\].*REJECT", i.strip())]

    if v5_items:
        items = v5_items
    else:
        # Fall back to numbered items (v3/v4 format)
        items = re.split(r"\n\s*\d+\.\s+", "\n" + text)
        # Also catch "- " bullet items that aren't sub-bullets
        if len(items) <= 1:
            items = re.split(r"\n- (?=[A-Z])", "\n" + text)

    for item in items:
        item = item.strip()
        if not item or len(item) < 15:
            continue
        # Skip headers, metadata, and revision/fix entries
        if item.startswith("#") or item.startswith("===") or item.startswith("[No additional"):
            continue
        if item.startswith("[No dead ends"):
            continue
        # Skip FIXES entries — we want failures, not corrections
        if re.match(r"\[Turn \d+\].*Revision:", item) or "FIXES APPLIED:" in item:
            continue

        # Extract title: first line or text before first colon/dash
        first_line = item.split("\n")[0].strip()

        # v5 format: extract the REJECT description
        v5_match = re.match(r"\[Turn \d+\] Run \d+ M\d+ REJECT:\s*(.*)", first_line)
        if v5_match:
            title = v5_match.group(1)[:80].rstrip(".")
        else:
            title_match = re.match(r"([A-Z][A-Z_ ]+):", first_line)
            if title_match:
                title = title_match.group(1).strip()
            else:
                title = first_line[:80].rstrip(".")

        # Check for version headers in context
        version_ctx = re.search(r"(?:From |##\s*)(V\d+|v\d+|Run \d+)", item)
        if version_ctx:
            version = version_ctx.group(1)

        type_tag = categorize_dead_end(item)

        # Split into tried/failed if possible
        tried = first_line
        failed_match = re.search(
            r"(?:REASON:|Why it failed:|failed|but|error|wrong|not|cannot|don't|DO NOT)",
            item, re.IGNORECASE,
        )
        if failed_match:
            failed = item[failed_match.start():].split("\n")[0].strip()
        else:
            failed = ""

        dead_ends.append(DeadEnd(
            id="",  # assigned later
            type_tag=type_tag,
            title=title,
            paper=paper,
            version=version,
            tried=tried,
            failed=failed if failed else "See detail above.",
        ))

    return dead_ends


# --- Log management ---

def load_existing_ids(path: Path) -> tuple[set[str], int]:
    """Load existing IDs from a consolidated log. Returns (set of IDs, max number)."""
    if not path.exists():
        return set(), 0

    text = path.read_text(encoding="utf-8", errors="replace")
    return _extract_ids_from_text(text)


def _extract_ids_from_text(text: str) -> tuple[set[str], int]:
    """Extract IDs and max number from already-loaded text (avoids re-reading file under lock)."""
    ids = set(re.findall(r"\[([A-Z]+-\d+)\]", text))
    numbers = [int(re.search(r"\d+", i).group()) for i in ids if re.search(r"\d+", i)]
    max_num = max(numbers) if numbers else 0
    return ids, max_num


def is_duplicate(title: str, paper: str, existing_text: str) -> Optional[str]:
    """Check if a finding with similar title+paper already exists. Returns the ID if so."""
    # Normalize for comparison
    title_words = set(re.findall(r"\w+", title.lower()))
    if len(title_words) < 3:
        return None

    # Look for entries with same paper
    pattern = rf"\[((?:F|DE)-\d+)\]\s+(.+)\n-\s+\*\*Paper:\*\*\s+{re.escape(paper)}"
    for match in re.finditer(pattern, existing_text):
        existing_id = match.group(1)
        existing_title = match.group(2)
        existing_words = set(re.findall(r"\w+", existing_title.lower()))
        overlap = len(title_words & existing_words) / max(len(title_words | existing_words), 1)
        if overlap > 0.5:
            return existing_id

    return None


def increment_recurrence(log_path: Path, finding_id: str) -> None:
    """Increment the recurrence count for an existing finding."""
    lock = FileLock(str(log_path) + ".lock", timeout=30)
    with lock:
        text = log_path.read_text(encoding="utf-8", errors="replace")
        pattern = rf"(\[{re.escape(finding_id)}\].*?Recurrence:\*\*\s*)(\d+)"
        match = re.search(pattern, text, re.DOTALL)
        if match:
            old_count = int(match.group(2))
            text = text[:match.start(2)] + str(old_count + 1) + text[match.end(2):]
            log_path.write_text(text, encoding="utf-8")


def append_finding(finding: Finding, log_path: Path) -> str:
    """Append a finding under its category header. Returns the assigned ID."""
    lock = FileLock(str(log_path) + ".lock", timeout=30)
    with lock:
        text = log_path.read_text(encoding="utf-8", errors="replace")

        # Check for duplicate — increment recurrence inline (already holding lock)
        dup_id = is_duplicate(finding.title, finding.paper, text)
        if dup_id:
            pattern = rf"(\[{re.escape(dup_id)}\].*?Recurrence:\*\*\s*)(\d+)"
            match = re.search(pattern, text, re.DOTALL)
            if match:
                old_count = int(match.group(2))
                text = text[:match.start(2)] + str(old_count + 1) + text[match.end(2):]
                log_path.write_text(text, encoding="utf-8")
            return dup_id

        # Assign ID from already-loaded text (avoid re-reading outside lock)
        _, max_num = _extract_ids_from_text(text)
        finding.id = f"F-{max_num + 1:03d}"

        entry = (
            f"\n### [{finding.id}] {finding.title}\n"
            f"- **Paper:** {finding.paper} | **Run:** {finding.run} | **Severity:** {finding.severity}\n"
            f"- {finding.detail}\n"
            f"- **Recurrence:** {finding.recurrence}\n"
        )

        # Find the category header and insert before the next category
        cat_pattern = rf"(## {re.escape(finding.category)}\n)"
        cat_match = re.search(cat_pattern, text)
        if cat_match:
            insert_pos = cat_match.end()
            # Find next ## header
            next_header = re.search(r"\n## ", text[insert_pos:])
            if next_header:
                insert_pos = insert_pos + next_header.start()
            else:
                insert_pos = len(text)
            text = text[:insert_pos] + entry + text[insert_pos:]
        else:
            # Category doesn't exist yet, append at end
            text += f"\n## {finding.category}\n{entry}"

        log_path.write_text(text, encoding="utf-8")
        return finding.id


def append_dead_end(de: DeadEnd, log_path: Path) -> str:
    """Append a dead-end under its type tag header. Returns the assigned ID."""
    lock = FileLock(str(log_path) + ".lock", timeout=30)
    with lock:
        text = log_path.read_text(encoding="utf-8", errors="replace")

        # Check for duplicate
        dup_id = is_duplicate(de.title, de.paper, text)
        if dup_id:
            return dup_id

        # Assign ID from already-loaded text (avoid re-reading outside lock)
        _, max_num = _extract_ids_from_text(text)
        de.id = f"DE-{max_num + 1:03d}"

        entry = (
            f"\n### [{de.id}] {de.title}\n"
            f"- **Paper:** {de.paper} | **Version:** {de.version}\n"
            f"- **Tried:** {de.tried}\n"
            f"- **Failed:** {de.failed}\n"
        )

        cat_pattern = rf"(## {re.escape(de.type_tag)}\n)"
        cat_match = re.search(cat_pattern, text)
        if cat_match:
            insert_pos = cat_match.end()
            next_header = re.search(r"\n## ", text[insert_pos:])
            if next_header:
                insert_pos = insert_pos + next_header.start()
            else:
                insert_pos = len(text)
            text = text[:insert_pos] + entry + text[insert_pos:]
        else:
            text += f"\n## {de.type_tag}\n{entry}"

        log_path.write_text(text, encoding="utf-8")
        return de.id


# --- Backfill ---

def backfill() -> None:
    """Scan all papers/ and archive/ directories for existing critiques and dead-ends."""
    papers_dir = SHELL_ROOT / "papers"
    archive_dir = SHELL_ROOT / "archive"

    # Collect all steelman critiques
    critique_paths = sorted(papers_dir.glob("*/steelman_full_paper_critique.md"))
    critique_paths += sorted(archive_dir.glob("*/steelman_full_paper_critique.md"))

    print(f"Found {len(critique_paths)} steelman critiques")
    for cp in critique_paths:
        findings = parse_steelman_critique(cp)
        print(f"  {cp.parent.name}: {len(findings)} findings")
        for f in findings:
            fid = append_finding(f, FINDINGS_LOG)
            print(f"    [{fid}] {f.category}: {f.title[:60]}")

    # Collect all dead-ends
    dead_end_paths = sorted(papers_dir.glob("*/dead_ends.md"))
    dead_end_paths += sorted(archive_dir.glob("*/dead_ends.md"))

    print(f"\nFound {len(dead_end_paths)} dead-ends files")
    for dep in dead_end_paths:
        dead_ends = parse_dead_ends(dep)
        print(f"  {dep.parent.name}: {len(dead_ends)} dead-ends")
        for de in dead_ends:
            deid = append_dead_end(de, DEAD_ENDS_LOG)
            print(f"    [{deid}] {de.type_tag}: {de.title[:60]}")


# --- Universal findings ---

def show_universal() -> None:
    """Show findings with recurrence >= 2 across different papers."""
    if not FINDINGS_LOG.exists():
        print("No findings log found. Run --backfill first.")
        return

    text = FINDINGS_LOG.read_text(encoding="utf-8", errors="replace")

    print("=== UNIVERSAL FINDINGS (recurrence >= 2) ===\n")
    print("Pre-load these into every init file's KNOWN_DRIFT_RISKS:\n")

    # Find entries with Recurrence >= 2
    pattern = r"### \[([A-Z]+-\d+)\] (.+)\n.*?Recurrence:\*\*\s*(\d+)"
    for match in re.finditer(pattern, text, re.DOTALL):
        fid = match.group(1)
        title = match.group(2)
        recurrence = int(match.group(3))
        if recurrence >= 2:
            print(f"- [{fid}] {title} ({recurrence} occurrences)")

    # Also check dead-ends that appear across multiple papers
    if DEAD_ENDS_LOG.exists():
        de_text = DEAD_ENDS_LOG.read_text(encoding="utf-8", errors="replace")
        print("\n=== UNIVERSAL DEAD ENDS ===\n")
        # Group by type_tag, show types with 3+ entries
        type_counts = {}
        for match in re.finditer(r"### \[(DE-\d+)\] (.+)\n-\s+\*\*Paper:\*\*\s+(\S+)", de_text):
            de_type_match = re.search(rf"## (\w+).*?{re.escape(match.group(1))}", de_text, re.DOTALL)
            if de_type_match:
                ttype = de_type_match.group(1)
                type_counts.setdefault(ttype, []).append(
                    (match.group(1), match.group(2), match.group(3))
                )
        for ttype, entries in sorted(type_counts.items()):
            papers = set(e[2] for e in entries)
            if len(papers) >= 2:
                print(f"\n## {ttype} (across {len(papers)} papers)")
                for deid, title, paper in entries:
                    print(f"  - [{deid}] {title} ({paper})")


# --- Main ---

def main():
    # Force UTF-8 output on Windows
    import sys, io
    if sys.platform == "win32":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Consolidate Steelman findings and dead-ends")
    parser.add_argument("--backfill", action="store_true", help="Backfill from all existing files")
    parser.add_argument("--critique", type=str, help="Append from a single steelman critique file")
    parser.add_argument("--dead-ends", type=str, help="Append from a single dead_ends file")
    parser.add_argument("--universal", action="store_true", help="Show high-recurrence universal items")
    args = parser.parse_args()

    if args.backfill:
        backfill()
    elif args.critique:
        path = Path(args.critique)
        if not path.exists():
            print(f"ERROR: {path} not found")
            return
        findings = parse_steelman_critique(path)
        print(f"Extracted {len(findings)} findings from {path.name}")
        for f in findings:
            fid = append_finding(f, FINDINGS_LOG)
            print(f"  [{fid}] {f.category}: {f.title[:60]}")
    elif args.dead_ends:
        path = Path(args.dead_ends)
        if not path.exists():
            print(f"ERROR: {path} not found")
            return
        dead_ends = parse_dead_ends(path)
        print(f"Extracted {len(dead_ends)} dead-ends from {path.name}")
        for de in dead_ends:
            deid = append_dead_end(de, DEAD_ENDS_LOG)
            print(f"  [{deid}] {de.type_tag}: {de.title[:60]}")
    elif args.universal:
        show_universal()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
