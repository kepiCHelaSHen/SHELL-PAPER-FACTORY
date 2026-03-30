#!/usr/bin/env python3
"""
verify_citations.py — Parse a SHELL paper's References section and verify
each citation against the CrossRef API.

Usage:
    python src/verify_citations.py --paper papers/[SLUG]/paper.md
"""

import argparse
import os
import re
import sys
import time
from datetime import datetime
from difflib import SequenceMatcher

try:
    import requests
except ImportError:
    print("ERROR: 'requests' library is required. Install with: pip install requests")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
CROSSREF_API = "https://api.crossref.org/works"
CROSSREF_HEADERS = {
    "User-Agent": "VerifyCitations/1.0 (mailto:your-email@example.com)"
}
REQUEST_DELAY_S = 1.0
MATCH_THRESHOLD = 0.45  # minimum combined similarity to call it VERIFIED


# ---------------------------------------------------------------------------
# Citation parsing
# ---------------------------------------------------------------------------

def extract_references_section(text: str) -> str | None:
    """Return the raw text of the References section, or None."""
    # Match ## References or # References (with optional trailing text)
    pattern = re.compile(
        r'^(#{1,2})\s+References\b.*$',
        re.IGNORECASE | re.MULTILINE,
    )
    match = pattern.search(text)
    if not match:
        return None

    heading_level = len(match.group(1))
    start = match.end()

    # Find the next heading at the same level or higher (fewer #'s)
    next_heading = re.compile(
        r'^#{1,' + str(heading_level) + r'}\s+\S',
        re.MULTILINE,
    )
    end_match = next_heading.search(text, start)
    if end_match:
        return text[start:end_match.start()].strip()
    return text[start:].strip()


def parse_citation_line(line: str) -> dict | None:
    """
    Best-effort extraction of author(s), year, and title from a citation line.

    Handles several common formats:
      - "Author (Year) | Title | Journal | Vol:Pages"
      - "Author (Year). Title. Journal, Vol(Issue), Pages."
      - "[1] Author (Year). Title. ..."
      - "Author, A. B. (Year). Title. ..."
      - "Author et al. Year. Title. ..."
    Returns dict with keys: raw, authors, year, title  (any may be None)
    """
    raw = line.strip()
    if not raw:
        return None

    # Strip leading list markers like "- ", "* ", "[1] ", "1. "
    cleaned = re.sub(r'^[\-\*]\s+', '', raw)
    cleaned = re.sub(r'^\[\d+\]\s*', '', cleaned)
    cleaned = re.sub(r'^\d+\.\s+', '', cleaned)

    result = {"raw": raw, "authors": None, "year": None, "title": None}

    # --- Extract year (four-digit number in parentheses or standalone) ---
    year_paren = re.search(r'\((\d{4})\)', cleaned)
    year_bare = re.search(r'\b(19|20)\d{2}\b', cleaned)
    if year_paren:
        result["year"] = year_paren.group(1)
    elif year_bare:
        result["year"] = year_bare.group(0)

    # --- Extract authors: text before the year ---
    if year_paren:
        authors_text = cleaned[:year_paren.start()].strip().rstrip(',').strip()
    elif year_bare:
        authors_text = cleaned[:year_bare.start()].strip().rstrip(',').rstrip('.').strip()
    else:
        # No year found — take text before first period or pipe
        split = re.split(r'[|.]', cleaned, maxsplit=1)
        authors_text = split[0].strip() if split else cleaned

    if authors_text:
        result["authors"] = authors_text

    # --- Extract title: text after year, before next delimiter ---
    if year_paren:
        after_year = cleaned[year_paren.end():]
    elif year_bare:
        after_year = cleaned[year_bare.end():]
    else:
        after_year = ""

    after_year = after_year.lstrip(' .,;:|)')

    if after_year:
        # Pipe-delimited format
        if '|' in after_year:
            title_candidate = after_year.split('|')[0].strip()
        else:
            # Period-delimited: take up to second period (title may contain
            # an internal period for abbreviations)
            parts = re.split(r'\.\s', after_year, maxsplit=1)
            title_candidate = parts[0].strip().rstrip('.')
        if title_candidate:
            result["title"] = title_candidate

    # If we got nothing useful, skip it
    if not result["authors"] and not result["year"] and not result["title"]:
        return None

    return result


def parse_references(ref_text: str) -> list[dict]:
    """
    Parse the references block into a list of citation dicts.
    Handles both one-citation-per-line and blank-line-separated paragraphs.
    """
    citations = []

    # If pipe-delimited table rows are present, parse as table
    lines = ref_text.splitlines()

    # Collapse multi-line citations: if a line doesn't look like a new
    # citation start, append it to the previous line.
    merged: list[str] = []
    new_entry_pat = re.compile(
        r'^(\s*[\-\*]\s+'           # bullet
        r'|\s*\[\d+\]\s*'          # [1] ...
        r'|\s*\d+\.\s+'            # 1. ...
        r'|\s*\|'                   # table row
        r'|\s*[A-Z][a-zA-Z])',     # starts with capital letter (author)
    )

    for line in lines:
        stripped = line.strip()
        # skip table header / separator rows
        if re.match(r'^\|?\s*[-:]+\s*\|', stripped):
            continue
        if not stripped:
            # blank line always starts a new entry
            merged.append("")
            continue
        if merged and merged[-1] and not new_entry_pat.match(line):
            merged[-1] = merged[-1] + " " + stripped
        else:
            merged.append(stripped)

    for entry in merged:
        entry = entry.strip()
        if not entry:
            continue
        parsed = parse_citation_line(entry)
        if parsed:
            citations.append(parsed)

    return citations


# ---------------------------------------------------------------------------
# CrossRef verification
# ---------------------------------------------------------------------------

def build_query(citation: dict) -> str:
    """Build a CrossRef query string from parsed citation fields."""
    parts = []
    if citation.get("title"):
        parts.append(citation["title"])
    if citation.get("authors"):
        # Use first author last-name token
        parts.append(citation["authors"].split(",")[0].split(" and ")[0])
    if citation.get("year"):
        parts.append(citation["year"])
    return " ".join(parts)


def extract_last_names(authors_str: str) -> list[str]:
    """Extract plausible last names from an author string."""
    # Remove common noise
    cleaned = re.sub(r'\b(et al\.?|and|&)\b', ' ', authors_str, flags=re.IGNORECASE)
    # Split on commas and spaces, keep tokens that start with uppercase
    tokens = re.findall(r'[A-Z][a-z]{2,}', cleaned)
    return [t.lower() for t in tokens]


def similarity(a: str, b: str) -> float:
    """Simple sequence-matcher ratio between two strings (lowered)."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def check_match(citation: dict, item: dict) -> tuple[bool, str, str]:
    """
    Check if a CrossRef result item plausibly matches our citation.
    Returns (is_match, display_title, doi).
    """
    doi = item.get("DOI", "")
    titles = item.get("title", [])
    display_title = titles[0] if titles else "(no title)"

    # --- Year check ---
    year_ok = False
    if citation.get("year"):
        pub_year = None
        for date_field in ("published-print", "published-online", "issued"):
            dp = item.get(date_field, {}).get("date-parts", [[]])
            if dp and dp[0] and dp[0][0]:
                pub_year = str(dp[0][0])
                break
        if pub_year == citation["year"]:
            year_ok = True

    # --- Author check ---
    author_ok = False
    cr_authors = item.get("author", [])
    cr_last_names = [a.get("family", "").lower() for a in cr_authors if a.get("family")]
    if citation.get("authors"):
        cite_last_names = extract_last_names(citation["authors"])
        for cln in cite_last_names:
            for crln in cr_last_names:
                if similarity(cln, crln) > 0.8:
                    author_ok = True
                    break
            if author_ok:
                break

    # --- Title check ---
    title_sim = 0.0
    if citation.get("title") and titles:
        title_sim = similarity(citation["title"], titles[0])

    # Decision: require year + (author or decent title), or strong title match
    score = 0.0
    if year_ok:
        score += 0.25
    if author_ok:
        score += 0.25
    score += title_sim * 0.5  # title similarity scaled into [0, 0.5]

    is_match = score >= MATCH_THRESHOLD
    return is_match, display_title, doi


def query_crossref(citation: dict) -> tuple[str, str, str]:
    """
    Query CrossRef for a citation.
    Returns (status, matched_title, doi).
    status is one of: VERIFIED, UNVERIFIED, ERROR
    """
    query = build_query(citation)
    if not query.strip():
        return "UNVERIFIED", "Insufficient data to query", "\u2014"

    params = {"query": query, "rows": 3}
    try:
        resp = requests.get(
            CROSSREF_API,
            params=params,
            headers=CROSSREF_HEADERS,
            timeout=30,
        )
        resp.raise_for_status()
    except requests.RequestException as exc:
        return "ERROR", f"Network error: {exc}", "\u2014"

    try:
        data = resp.json()
        items = data.get("message", {}).get("items", [])
    except (ValueError, KeyError):
        return "ERROR", "Invalid API response", "\u2014"

    if not items:
        return "UNVERIFIED", "No results from CrossRef", "\u2014"

    for item in items:
        is_match, title, doi = check_match(citation, item)
        if is_match:
            return "VERIFIED", title, doi

    # Return best candidate info even if unverified
    best = items[0]
    best_title = best.get("title", ["(unknown)"])[0]
    return "UNVERIFIED", f"Best: {best_title}", "\u2014"


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def short_citation(citation: dict) -> str:
    """Produce a compact label like 'Aumann (1976)'."""
    parts = []
    if citation.get("authors"):
        # first last name
        names = extract_last_names(citation["authors"])
        if names:
            parts.append(names[0].capitalize())
        else:
            parts.append(citation["authors"][:30])
    if citation.get("year"):
        parts.append(f"({citation['year']})")
    if not parts and citation.get("title"):
        parts.append(citation["title"][:40])
    return " ".join(parts) if parts else citation["raw"][:50]


def generate_report(
    paper_path: str,
    citations: list[dict],
    results: list[tuple[str, str, str]],
) -> str:
    """Build the markdown verification report."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# Citation Verification Report",
        f"# Paper: {os.path.basename(paper_path)}",
        f"# Verified: {now}",
        "",
        "| # | Citation | CrossRef Match | DOI | Status |",
        "|---|----------|---------------|-----|--------|",
    ]

    verified_count = 0
    unverified_entries: list[tuple[int, dict]] = []

    for i, (citation, (status, match_title, doi)) in enumerate(
        zip(citations, results), start=1
    ):
        label = short_citation(citation)
        # Escape pipes in text for markdown table
        match_title_safe = match_title.replace("|", "\\|")
        label_safe = label.replace("|", "\\|")
        doi_display = doi if doi != "\u2014" else "\u2014"

        lines.append(
            f"| {i} | {label_safe} | {match_title_safe} | {doi_display} | {status} |"
        )

        if status == "VERIFIED":
            verified_count += 1
        else:
            unverified_entries.append((i, citation))

    total = len(citations)
    unverified_count = total - verified_count

    lines.append("")
    lines.append(
        f"Summary: {verified_count}/{total} citations verified. "
        f"{unverified_count} unverified."
    )

    if unverified_entries:
        lines.append("")
        lines.append("## Unverified Citations (require manual check)")
        lines.append("")
        for idx, cit in unverified_entries:
            lines.append(f"- **[{idx}]** {cit['raw']}")

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Verify paper citations against CrossRef API."
    )
    parser.add_argument(
        "--paper",
        required=True,
        help="Path to the paper markdown file (e.g., papers/slug/paper.md)",
    )
    args = parser.parse_args()

    paper_path = args.paper
    if not os.path.isfile(paper_path):
        print(f"ERROR: File not found: {paper_path}")
        sys.exit(1)

    with open(paper_path, "r", encoding="utf-8") as fh:
        text = fh.read()

    # --- Extract references ---
    ref_section = extract_references_section(text)
    if ref_section is None:
        print("No References section found in the paper. Nothing to verify.")
        sys.exit(0)

    citations = parse_references(ref_section)
    if not citations:
        print("References section found but no parseable citations detected.")
        sys.exit(0)

    print(f"Found {len(citations)} citation(s). Verifying against CrossRef...\n")

    # --- Query CrossRef for each ---
    results: list[tuple[str, str, str]] = []
    for i, cit in enumerate(citations, start=1):
        label = short_citation(cit)
        print(f"  [{i}/{len(citations)}] {label} ... ", end="", flush=True)
        status, match_title, doi = query_crossref(cit)
        print(status)
        results.append((status, match_title, doi))
        if i < len(citations):
            time.sleep(REQUEST_DELAY_S)

    # --- Generate report ---
    report = generate_report(paper_path, citations, results)

    # Ensure output directory exists
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "outputs")
    out_dir = os.path.normpath(out_dir)
    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, "citation_verification.md")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(report)

    # --- Summary to stdout ---
    verified = sum(1 for s, _, _ in results if s == "VERIFIED")
    total = len(citations)
    errors = sum(1 for s, _, _ in results if s == "ERROR")

    print()
    print("=" * 60)
    print(f"  VERIFIED:   {verified}/{total}")
    print(f"  UNVERIFIED: {total - verified - errors}/{total}")
    if errors:
        print(f"  ERRORS:     {errors}/{total}")
    print(f"  Report written to: {out_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()
