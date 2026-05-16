#!/usr/bin/env python3
"""Run v2 external reviews via Gemini 2.5 Pro (primary) and Grok-3 (adversarial).

GPT-4o dropped from the review panel — it gave MINOR_REVISION to all 6 papers
uniformly, detected AI on 0/6, and assigned flat 200h/Senior Faculty to everything.
It does not discriminate and is not useful as an adversarial reviewer.

Model roles:
  - Gemini 2.5 Pro: Primary reviewer. Most detailed, widest score range (2-10),
    best discrimination. 16384 max tokens to avoid truncation.
  - Grok-3: Adversarial reviewer. Harshest, best AI detection, most willing
    to reject. 8192 max tokens (sufficient for its terser style).

Usage:
  source api.env && python3 scripts/run_reviews.py [SLUG ...]

  With no args, reviews all papers found in papers/*/best_paper.md.
  With args, reviews only the named slugs.
"""

import os
import json
import sys
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
import urllib.request
import ssl

BASE = Path("C:/PROJECTS/SHELL")
DATE = date.today().isoformat()

# Load API keys — check env first, fall back to api.env
def load_key(env_name):
    val = os.environ.get(env_name, "")
    if val:
        return val.strip().strip('"')
    env_file = BASE / "api.env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if line.startswith(f"{env_name}="):
                return line.split("=", 1)[1].strip().strip('"')
    raise RuntimeError(f"{env_name} not found in environment or api.env")

XAI_KEY = load_key("XAI_API_KEY")
GOOGLE_KEY = load_key("GOOGLE_API_KEY")

# SSL context for environments with corporate proxies
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Review prompt — loaded once, paper content appended per call
REVIEW_PROMPT = (BASE / "prompts" / "09_external_review.md").read_text(encoding="utf-8")
REVIEW_PROMPT = REVIEW_PROMPT.replace("[PASTE PAPER HERE]", "")


def call_openai_compatible(url, api_key, model, prompt, max_tokens):
    """Call an OpenAI-compatible chat completions API."""
    body = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
        "max_tokens": max_tokens,
    }).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    })
    with urllib.request.urlopen(req, timeout=600, context=ctx) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


def call_gemini(prompt, max_tokens):
    """Call Gemini via Google AI Studio API."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-pro:generateContent?key={GOOGLE_KEY}"
    body = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.3, "maxOutputTokens": max_tokens},
    }).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})

    # Gemini rate-limits aggressively — retry with backoff
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=600, context=ctx) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except urllib.request.HTTPError as e:
            if e.code == 503 and attempt < 2:
                wait = 30 * (attempt + 1)
                print(f"    Gemini 503, retrying in {wait}s...", flush=True)
                time.sleep(wait)
            else:
                raise


def review_paper(slug, model_name, call_fn, max_tokens):
    """Run a single review and save to disk."""
    paper_path = BASE / "papers" / slug / "best_paper.md"
    reviews_dir = BASE / "papers" / slug / "reviews"
    reviews_dir.mkdir(exist_ok=True)
    out_path = reviews_dir / f"{model_name}_review_{DATE}.md"

    if not paper_path.exists():
        print(f"  SKIP: {slug} — no best_paper.md", flush=True)
        return (slug, model_name, "SKIP", "no best_paper.md")

    paper_content = paper_path.read_text(encoding="utf-8")
    full_prompt = f"{REVIEW_PROMPT}\n\n---\n\n{paper_content}"

    print(f"  Starting {model_name} review of {slug}...", flush=True)
    try:
        result = call_fn(full_prompt, max_tokens)
        out_path.write_text(result, encoding="utf-8")
        print(f"  DONE: {model_name} x {slug} ({len(result)} chars)", flush=True)
        return (slug, model_name, "OK", len(result))
    except Exception as e:
        error_msg = f"ERROR: {e}"
        out_path.write_text(error_msg, encoding="utf-8")
        print(f"  FAIL: {model_name} x {slug}: {e}", flush=True)
        return (slug, model_name, "FAIL", str(e))


def discover_papers():
    """Find all paper slugs that have a best_paper.md."""
    papers_dir = BASE / "papers"
    slugs = []
    for d in sorted(papers_dir.iterdir()):
        if d.is_dir() and (d / "best_paper.md").exists():
            slugs.append(d.name)
    return slugs


def main():
    # Determine which papers to review
    if len(sys.argv) > 1:
        slugs = sys.argv[1:]
    else:
        slugs = discover_papers()

    if not slugs:
        print("No papers found to review.")
        return

    # Build task list: Gemini (primary) + Grok (adversarial) for each paper
    tasks = []
    for slug in slugs:
        tasks.append((slug, "Gemini25Pro", lambda p, mt: call_gemini(p, mt), 16384))
        tasks.append((slug, "Grok3", lambda p, mt: call_openai_compatible(
            "https://api.x.ai/v1/chat/completions", XAI_KEY, "grok-3-latest", p, mt
        ), 8192))

    print(f"Launching {len(tasks)} reviews ({len(slugs)} papers x 2 models: Gemini 2.5 Pro + Grok-3)")
    print(f"GPT-4o excluded — see docstring for rationale.")
    print()

    results = []
    # 2 concurrent to respect Gemini rate limits
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = {executor.submit(review_paper, *t): t for t in tasks}
        for future in as_completed(futures):
            results.append(future.result())

    # Summary
    print(f"\n{'='*60}")
    ok = sum(1 for r in results if r[2] == "OK")
    print(f"RESULTS: {ok}/{len(results)} succeeded")
    for slug, model, status, detail in sorted(results):
        print(f"  {slug} x {model}: {status} ({detail})")

    # Flag cross-model disagreements if both succeeded
    print(f"\nReview files saved to papers/[SLUG]/reviews/")
    print(f"Next: parse reviews and check for cross-model disagreements >3 points.")


if __name__ == "__main__":
    main()
