#!/usr/bin/env python3
"""
paper_to_thread.py — Extract the compelling parts of a SHELL paper and
format them as an X (Twitter) thread.

Usage:
    python src/paper_to_thread.py --paper papers/[SLUG]/paper.md

Outputs:
    outputs/x_thread.md — the thread in markdown, ready to copy-paste
    Also prints to stdout.

The script parses the paper structure and extracts:
    1. The hook (counterintuitive result from Abstract)
    2. The problem (what the field gets wrong)
    3. The core result (key theorem/finding)
    4. The best figure reference
    5. The boundary condition drama ("we tried to break it")
    6. The punchline (implications)
    7. The link (DOI placeholder)

Each tweet is ≤280 characters. The thread is 7-12 tweets.
"""

import argparse
import os
import re
import sys
import textwrap


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def read_paper(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def extract_section(text: str, heading: str) -> str:
    """Extract content under a ## or ### heading until the next heading of same or higher level.
    Handles numbered headings like '## 2. Introduction'."""
    pattern = re.compile(
        r'^(#{1,3})\s+(?:\d+\.?\s*)*' + re.escape(heading) + r'\b.*$',
        re.IGNORECASE | re.MULTILINE,
    )
    match = pattern.search(text)
    if not match:
        return ""
    level = len(match.group(1))
    start = match.end()
    next_heading = re.compile(r'^#{1,' + str(level) + r'}\s+\S', re.MULTILINE)
    end_match = next_heading.search(text, start)
    if end_match:
        return text[start:end_match.start()].strip()
    return text[start:].strip()


def extract_abstract(text: str) -> str:
    return extract_section(text, "Abstract")


def extract_title(text: str) -> str:
    match = re.match(r'^#\s+(.+)$', text.strip(), re.MULTILINE)
    return match.group(1).strip() if match else "Untitled"


def extract_theorems(text: str) -> list:
    """Find all theorem statements — grab everything until Proof or next heading."""
    pattern = re.compile(
        r'\*\*Theorem\s+(\d+)\s*\(([^)]+)\)\.\*\*\s*(.+?)(?=\n\*Proof\.?\*|\n#{1,3}\s|\n\*\*(?:Theorem|Lemma|Corollary|Proposition|Definition))',
        re.DOTALL,
    )
    results = []
    for m in pattern.finditer(text):
        statement = m.group(3).strip()
        # Clean up: collapse newlines, remove excess whitespace
        statement = re.sub(r'\n+', ' ', statement)
        statement = re.sub(r'\s+', ' ', statement)
        results.append({
            "number": m.group(1),
            "name": m.group(2).strip(),
            "statement": statement[:600],
        })
    return results


def extract_boundary_conditions(text: str) -> str:
    for heading in ["Boundary Conditions", "Natural Enemy"]:
        section = extract_section(text, heading)
        if section:
            return section
    return ""


def extract_figure_refs(text: str) -> list:
    """Find figure references and their captions."""
    pattern = re.compile(r'\[Figure\s+(\d+):\s*([^\]]+)\]', re.IGNORECASE)
    return [{"number": m.group(1), "caption": m.group(2).strip()} for m in pattern.finditer(text)]


def extract_open_problems(text: str) -> str:
    return extract_section(text, "Open Problems")


def extract_conclusion(text: str) -> str:
    return extract_section(text, "Conclusion")


def first_sentences(text: str, n: int = 2) -> str:
    """Extract first n sentences from text."""
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return " ".join(sentences[:n])


def truncate_tweet(text: str, max_len: int = 275) -> str:
    """Truncate to tweet length, ending at a word boundary."""
    if len(text) <= max_len:
        return text
    truncated = text[:max_len]
    last_space = truncated.rfind(" ")
    if last_space > max_len - 50:
        truncated = truncated[:last_space]
    return truncated + "..."


# ---------------------------------------------------------------------------
# Thread generation
# ---------------------------------------------------------------------------

def generate_thread(paper_path: str, text: str) -> list:
    """Generate the X thread as a list of tweet strings."""
    title = extract_title(text)
    abstract = extract_abstract(text)
    theorems = extract_theorems(text)
    boundary = extract_boundary_conditions(text)
    figures = extract_figure_refs(text)
    conclusion = extract_conclusion(text)
    open_problems = extract_open_problems(text)

    tweets = []

    # Tweet 1: Hook — the title + one-line result
    # Find the most striking claim in the abstract
    abstract_sentences = re.split(r'(?<=[.!?])\s+', abstract.strip())
    # Look for sentences with strong result language
    result_sentence = ""
    for s in abstract_sentences:
        if any(w in s.lower() for w in ["proves", "shown", "derives", "theorem",
                "maximum-likelihood", "diverges", "eliminates", "impossible",
                "threshold", "if and only if"]):
            result_sentence = s
            break
    if not result_sentence and len(abstract_sentences) > 2:
        result_sentence = abstract_sentences[2]
    hook = truncate_tweet(f"New paper: {title}\n\n{result_sentence}")
    tweets.append(hook)

    # Tweet 2: The problem — what the field gets wrong
    intro = extract_section(text, "Introduction")
    if intro:
        # Look for gap formula patterns in intro
        gap_pattern = re.findall(
            r'([A-Z][^.]+(?:cannot|fails?|breaks?|no (?:inferential|mechanism)|insufficient|but )[^.]+\.)',
            intro,
        )
        if gap_pattern:
            tweets.append(truncate_tweet(f"The problem:\n\n{gap_pattern[0]}"))
        else:
            tweets.append(truncate_tweet(f"The problem:\n\n{first_sentences(intro, 2)}"))

    # Tweet 3-4: The core result — key theorem(s)
    if theorems:
        best = theorems[0]
        # Get a cleaner statement by taking more text
        thm_text = f"The key result — Theorem {best['number']} ({best['name']}):\n\n{first_sentences(best['statement'], 3)}"
        tweets.append(truncate_tweet(thm_text))

        if len(theorems) > 2:
            # Pick the most interesting-sounding later theorem
            for t in theorems[1:]:
                if any(w in t['name'].lower() for w in ["filter", "threshold",
                        "impossib", "collapse", "trap", "rational", "bound"]):
                    thm2_text = f"Theorem {t['number']} ({t['name']}):\n\n{first_sentences(t['statement'], 2)}"
                    tweets.append(truncate_tweet(thm2_text))
                    break

    # Tweet 5: The figure — most dramatic visual
    if figures:
        fig = figures[0]
        fig_text = f"Figure {fig['number']}: {fig['caption']}\n\n[attach figure_{fig['number']}.pdf]"
        tweets.append(truncate_tweet(fig_text))

    # Tweet 6: Boundary conditions — "we tried to break it"
    if boundary:
        boundary_first = first_sentences(boundary, 2)
        tweets.append(truncate_tweet(
            f"We tried to break it.\n\n{boundary_first}"
        ))

    # Tweet 7: Open problems — what's left
    if open_problems:
        op_first = first_sentences(open_problems, 2)
        tweets.append(truncate_tweet(f"What the paper doesn't solve:\n\n{op_first}"))

    # Tweet 8: The punchline — implications
    if conclusion:
        conclusion_first = first_sentences(conclusion, 2)
        tweets.append(truncate_tweet(f"Bottom line:\n\n{conclusion_first}"))

    # Tweet 9: Link + method credit
    tweets.append(truncate_tweet(
        "Full paper (open access): [Zenodo DOI link]\n\n"
        "Written using the DVL framework — a deterministic validation loop "
        "for LLM-generated scientific research.\n\n"
        "Framework paper: doi.org/10.5281/zenodo.19217024"
    ))

    return tweets


def format_thread(tweets: list) -> str:
    """Format tweets as a numbered markdown thread."""
    lines = ["# X Thread\n"]
    for i, tweet in enumerate(tweets, 1):
        char_count = len(tweet)
        lines.append(f"## Tweet {i}/{len(tweets)} ({char_count} chars)\n")
        lines.append(tweet)
        lines.append("")
        lines.append("---\n")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Convert a SHELL paper to an X (Twitter) thread."
    )
    parser.add_argument(
        "--paper", required=True,
        help="Path to paper.md",
    )
    parser.add_argument(
        "--output", default=None,
        help="Output path (default: outputs/x_thread.md in cwd)",
    )
    args = parser.parse_args()

    if not os.path.isfile(args.paper):
        print(f"ERROR: File not found: {args.paper}")
        sys.exit(1)

    text = read_paper(args.paper)
    tweets = generate_thread(args.paper, text)
    thread_md = format_thread(tweets)

    # Output
    out_path = args.output
    if not out_path:
        out_dir = os.path.join(os.getcwd(), "outputs")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "x_thread.md")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(thread_md)

    # Also print to stdout
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print(thread_md)
    print(f"\nThread saved to: {out_path}")
    print(f"Tweets: {len(tweets)}")


if __name__ == "__main__":
    main()
