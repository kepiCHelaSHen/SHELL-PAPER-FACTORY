#!/usr/bin/env python3
"""
external_review.py — Automated adversarial review of THESIS papers.

Sends best_paper.md to GPT-4o, Grok-3, and Gemini 2.5 Flash using the
standardized review prompt from prompts/09_external_review.md.
Saves reviews, parses scores, and generates a summary scorecard.

Usage:
    python src/external_review.py --paper papers/SLUG_DATE_SEQ/best_paper.md
    python src/external_review.py --paper papers/SLUG_DATE_SEQ/best_paper.md --models gpt,grok
    python src/external_review.py --batch  # reviews all papers with best_paper.md
"""

import argparse
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

# Force UTF-8 on Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

SHELL_ROOT = Path(__file__).parent.parent
REVIEW_PROMPT_PATH = SHELL_ROOT / "prompts" / "09_external_review.md"
ENV_PATH = SHELL_ROOT / "api.env"

DIMENSIONS = [
    "Originality",
    "Mathematical Rigor",
    "Literature Awareness",
    "Intellectual Honesty",
    "Clarity of Writing",
    "Policy Relevance",
    "Conceptual Compression",
    "Empirical Grounding",
    "Publishability",
    "Overall Coherence",
]


def load_env():
    """Load API keys from api.env."""
    keys = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                v = v.strip().strip('"').strip("'")  # Strip quotes
                keys[k.strip()] = v
                os.environ[k.strip()] = v
    # Also check environment variables
    for var in ["OPENAI_API_KEY", "XAI_API_KEY", "GOOGLE_API_KEY"]:
        if var in os.environ and var not in keys:
            keys[var] = os.environ[var]
    return keys


def load_review_prompt():
    """Load the standardized review prompt."""
    text = REVIEW_PROMPT_PATH.read_text(encoding="utf-8")
    # Strip the header comments, keep just the prompt
    lines = text.splitlines()
    prompt_lines = []
    in_prompt = False
    for line in lines:
        if line.startswith("You are an independent"):
            in_prompt = True
        if in_prompt:
            prompt_lines.append(line)
    return "\n".join(prompt_lines)


def call_openai(paper_text: str, review_prompt: str, api_key: str) -> str:
    """Call GPT-4o via OpenAI API."""
    import urllib.request
    import urllib.error

    full_prompt = review_prompt.replace("[PASTE PAPER HERE]", paper_text)

    payload = json.dumps({
        "model": "gpt-4o",
        "messages": [{"role": "user", "content": full_prompt}],
        "temperature": 0.3,
        "max_tokens": 8000,
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
    )

    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["choices"][0]["message"]["content"]
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError) as e:
            if attempt < 2:
                wait = 10 * (attempt + 1)
                print(f"  GPT retry {attempt + 1}/3 in {wait}s: {e}")
                time.sleep(wait)
            else:
                return f"ERROR: GPT-4o API failed after 3 attempts: {e}"


def call_xai(paper_text: str, review_prompt: str, api_key: str) -> str:
    """Call Grok-3 via xAI API."""
    import urllib.request
    import urllib.error

    full_prompt = review_prompt.replace("[PASTE PAPER HERE]", paper_text)

    payload = json.dumps({
        "model": "grok-3-latest",
        "messages": [{"role": "user", "content": full_prompt}],
        "temperature": 0.3,
        "max_tokens": 8000,
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.x.ai/v1/chat/completions",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
    )

    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["choices"][0]["message"]["content"]
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError) as e:
            if attempt < 2:
                wait = 10 * (attempt + 1)
                print(f"  Grok retry {attempt + 1}/3 in {wait}s: {e}")
                time.sleep(wait)
            else:
                return f"ERROR: Grok-3 API failed after 3 attempts: {e}"


def call_gemini(paper_text: str, review_prompt: str, api_key: str) -> str:
    """Call Gemini 2.5 Flash via Google API."""
    import urllib.request
    import urllib.error

    full_prompt = review_prompt.replace("[PASTE PAPER HERE]", paper_text)

    payload = json.dumps({
        "contents": [{"parts": [{"text": full_prompt}]}],
        "generationConfig": {"temperature": 0.3, "maxOutputTokens": 8000},
    }).encode("utf-8")

    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}",
        data=payload,
        headers={"Content-Type": "application/json"},
    )

    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["candidates"][0]["content"]["parts"][0]["text"]
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError) as e:
            if attempt < 2:
                wait = 10 * (attempt + 1)
                print(f"  Gemini retry {attempt + 1}/3 in {wait}s: {e}")
                time.sleep(wait)
            else:
                return f"ERROR: Gemini API failed after 3 attempts: {e}"


def parse_scores(review_text: str) -> dict:
    """Extract dimension scores from a review."""
    scores = {}
    for dim in DIMENSIONS:
        # Match many patterns: "Originality — 7.5/10", "Originality: 8/10",
        # "1. Originality — 6", "**Originality (8/10)**", "Originality | 7.5 |"
        # "**Originality:** 8/10", "**Originality:** 8"
        patterns = [
            rf"\**{re.escape(dim)}[:\*]*\**\s*(\d+\.?\d*)\s*/\s*10",
            rf"\**{re.escape(dim)}\**\s*\((\d+\.?\d*)/10\)",
            rf"\**{re.escape(dim)}\**\s*\((\d+\.?\d*)\)",
            rf"{re.escape(dim)}[:\s—\-]+(\d+\.?\d*)\s*/?\s*10",
            rf"{re.escape(dim)}[:\s—\-]+(\d+\.?\d*)",
            rf"\d+\.\s*\**{re.escape(dim)}\**[:\s—\-]+(\d+\.?\d*)",
            rf"{re.escape(dim)}\s*\|\s*(\d+\.?\d*)",
        ]
        for pattern in patterns:
            match = re.search(pattern, review_text, re.IGNORECASE)
            if match:
                score = float(match.group(1))
                if score <= 10:
                    scores[dim] = score
                    break
    return scores


def parse_composite(review_text: str) -> float:
    """Extract composite score from a review."""
    patterns = [
        r"[Cc]omposite[:\s]+\**(\d+\.?\d*)\s*/?\s*10",
        r"[Cc]omposite\s+[Ss]core[:\s]*\**(\d+\.?\d*)",
        r"\*\*(\d+\.?\d*)\s*/\s*10\*\*",
        r"[Aa]verage.*?(\d+\.?\d*)\s*/\s*10",
        r"(\d+\.?\d*)\s*/\s*10\s*$",
    ]
    for pattern in patterns:
        match = re.search(pattern, review_text, re.MULTILINE)
        if match:
            score = float(match.group(1))
            if score <= 10:
                return score
    # Fall back to averaging parsed scores
    scores = parse_scores(review_text)
    if scores:
        return round(sum(scores.values()) / len(scores), 2)
    return 0.0


def review_paper(paper_path: Path, models: list[str], keys: dict) -> dict:
    """Send a paper to all specified models for review."""
    paper_text = paper_path.read_text(encoding="utf-8", errors="replace")
    review_prompt = load_review_prompt()

    # Truncate if too long (some APIs have limits)
    if len(paper_text) > 100000:
        paper_text = paper_text[:100000] + "\n\n[TRUNCATED — paper exceeds 100K characters]"

    project_dir = paper_path.parent
    reviews_dir = project_dir / "reviews"
    reviews_dir.mkdir(exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    results = {}

    model_funcs = {
        "gpt": ("GPT-4o", call_openai, keys.get("OPENAI_API_KEY")),
        "grok": ("Grok-3", call_xai, keys.get("XAI_API_KEY")),
        "gemini": ("Gemini-2.5", call_gemini, keys.get("GOOGLE_API_KEY")),
    }

    def run_review(model_key):
        model_name, func, api_key = model_funcs[model_key]
        if not api_key:
            return model_key, f"SKIPPED: No API key for {model_name}"

        print(f"  Sending to {model_name}...")
        start = time.time()
        review = func(paper_text, review_prompt, api_key)
        elapsed = time.time() - start
        print(f"  {model_name} responded in {elapsed:.0f}s")

        # Save review
        review_file = reviews_dir / f"{model_key}_review_{today}.md"
        review_file.write_text(
            f"# {model_name} Review — {project_dir.name}\n"
            f"# Date: {today}\n"
            f"# Paper: {paper_path.name}\n\n"
            f"{review}",
            encoding="utf-8",
        )

        # Parse scores
        scores = parse_scores(review)
        composite = parse_composite(review)

        try:
            rel_path = str(review_file.relative_to(SHELL_ROOT))
        except ValueError:
            rel_path = str(review_file)

        return model_key, {
            "model": model_name,
            "composite": composite,
            "scores": scores,
            "review_file": rel_path,
            "elapsed_seconds": round(elapsed),
        }

    # Run reviews in parallel
    active_models = [m for m in models if m in model_funcs and model_funcs[m][2]]
    skipped = [m for m in models if m not in active_models]

    if skipped:
        missing_keys = [model_funcs.get(m, (m,))[0] for m in skipped if m in model_funcs]
        print(f"  Skipping (no API key): {', '.join(missing_keys)}")

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(run_review, m): m for m in active_models}
        for future in as_completed(futures):
            try:
                model_key, result = future.result()
                results[model_key] = result
            except Exception as e:
                model_key = futures[future]
                print(f"  {model_key} failed: {e}")
                results[model_key] = f"ERROR: {e}"

    return results


def generate_scorecard(all_results: dict, output_path: Path):
    """Generate a summary scorecard across all papers and models."""
    lines = [
        "# External Review Scorecard",
        f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
    ]

    # Summary table
    lines.append("## Summary")
    lines.append("")
    header = "| Paper | GPT | Grok | Gemini | Avg |"
    sep = "|-------|-----|------|--------|-----|"
    lines.extend([header, sep])

    for paper, reviews in all_results.items():
        scores = []
        cells = []
        for model in ["gpt", "grok", "gemini"]:
            if model in reviews and isinstance(reviews[model], dict):
                comp = reviews[model]["composite"]
                scores.append(comp)
                cells.append(f"{comp}")
            else:
                cells.append("—")
        avg = round(sum(scores) / len(scores), 2) if scores else 0
        lines.append(f"| {paper} | {cells[0]} | {cells[1]} | {cells[2]} | **{avg}** |")

    lines.append("")

    # Dimension averages across all reviews
    lines.append("## System Signature (all reviews)")
    lines.append("")
    lines.append("| Dimension | Average |")
    lines.append("|-----------|---------|")

    dim_totals = {d: [] for d in DIMENSIONS}
    for paper, reviews in all_results.items():
        for model, data in reviews.items():
            if isinstance(data, dict) and "scores" in data:
                for dim, score in data["scores"].items():
                    if dim in dim_totals:
                        dim_totals[dim].append(score)

    for dim in DIMENSIONS:
        vals = dim_totals[dim]
        avg = round(sum(vals) / len(vals), 1) if vals else 0
        lines.append(f"| {dim} | {avg} |")

    lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nScorecard saved to {output_path}")


def find_papers(batch: bool, paper_path: str = None) -> list[Path]:
    """Find papers to review."""
    if paper_path:
        p = Path(paper_path)
        if not p.exists():
            # Try relative to SHELL_ROOT
            p = SHELL_ROOT / paper_path
        if p.exists():
            return [p]
        print(f"ERROR: Paper not found: {paper_path}")
        sys.exit(1)

    if batch:
        papers = []
        papers_dir = SHELL_ROOT / "papers"
        for project in sorted(papers_dir.iterdir()):
            if project.is_dir():
                bp = project / "best_paper.md"
                if bp.exists():
                    papers.append(bp)
        return papers

    print("ERROR: Specify --paper or --batch")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Automated external review of THESIS papers")
    parser.add_argument("--paper", type=str, help="Path to best_paper.md")
    parser.add_argument("--batch", action="store_true", help="Review all papers with best_paper.md")
    parser.add_argument("--models", type=str, default="gpt,grok,gemini",
                        help="Comma-separated list of models (default: gpt,grok,gemini)")
    args = parser.parse_args()

    keys = load_env()
    models = [m.strip() for m in args.models.split(",")]
    papers = find_papers(args.batch, args.paper)

    if not papers:
        print("No papers found to review.")
        return

    print(f"Reviewing {len(papers)} paper(s) with models: {', '.join(models)}")
    print(f"API keys available: {', '.join(k for k in ['OPENAI_API_KEY', 'XAI_API_KEY', 'GOOGLE_API_KEY'] if k in keys)}")
    print()

    all_results = {}

    for paper_path in papers:
        project_name = paper_path.parent.name
        print(f"=== {project_name} ===")
        results = review_paper(paper_path, models, keys)
        all_results[project_name] = results

        # Print quick summary
        for model, data in results.items():
            if isinstance(data, dict):
                print(f"  {data['model']}: {data['composite']} ({data['elapsed_seconds']}s)")
                if data["scores"]:
                    for dim, score in sorted(data["scores"].items()):
                        color = "+" if score >= 7 else ("-" if score < 5 else " ")
                        print(f"    {color} {dim}: {score}")
            else:
                print(f"  {model}: {data}")
        print()

    # Generate scorecard
    scorecard_path = SHELL_ROOT / "outputs" / "review_scorecard.md"
    scorecard_path.parent.mkdir(exist_ok=True)
    generate_scorecard(all_results, scorecard_path)

    # Also save raw results as JSON
    json_path = SHELL_ROOT / "outputs" / "review_results.json"
    json_path.write_text(
        json.dumps(all_results, indent=2, default=str),
        encoding="utf-8",
    )
    print(f"Raw results saved to {json_path}")


if __name__ == "__main__":
    main()
