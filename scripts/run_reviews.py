#!/usr/bin/env python3
"""Run v2 external reviews on all 6 papers via GPT-4o and Grok-3 in parallel."""

import os
import json
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
import urllib.request
import urllib.error
import ssl

BASE = Path("C:/PROJECTS/SHELL")
REVIEW_PROMPT = (BASE / "prompts" / "09_external_review.md").read_text(encoding="utf-8")
REVIEW_PROMPT = REVIEW_PROMPT.replace("[PASTE PAPER HERE]", "")
DATE = date.today().isoformat()

PAPERS = [
    "DRUG_SPENDING_2026_2026-05-15_003",
    "HOSPITAL_PRICING_2026_2026-05-15_003",
    "OPIOID_PRESCRIBING_2026_2026-05-15_003",
    "REPLICATION_CRISIS_2026_2026-05-15_003",
    "TECH_LOCKIN_2026_2026-05-15_003",
    "VACCINE_GAME_2026_2026-05-15_002",
]

OPENAI_KEY = os.environ["OPENAI_API_KEY"]
XAI_KEY = os.environ["XAI_API_KEY"]

# Allow unverified SSL for corporate environments
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def call_api(url, api_key, model, prompt, max_tokens=8192):
    """Call an OpenAI-compatible chat API."""
    body = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
        "max_tokens": max_tokens,
    }).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
    )
    with urllib.request.urlopen(req, timeout=600, context=ctx) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


def review_paper(slug, model_name, url, api_key, model_id):
    """Run a single review and save to disk."""
    paper_path = BASE / "papers" / slug / "best_paper.md"
    out_path = BASE / "papers" / slug / "reviews" / f"{model_name}_review_{DATE}.md"

    paper_content = paper_path.read_text(encoding="utf-8")
    full_prompt = f"{REVIEW_PROMPT}\n\n---\n\n{paper_content}"

    print(f"  Starting {model_name} review of {slug}...", flush=True)
    try:
        result = call_api(url, api_key, model_id, full_prompt)
        out_path.write_text(result, encoding="utf-8")
        print(f"  DONE: {model_name} x {slug} ({len(result)} chars)", flush=True)
        return (slug, model_name, "OK", len(result))
    except Exception as e:
        error_msg = f"ERROR: {e}"
        out_path.write_text(error_msg, encoding="utf-8")
        print(f"  FAIL: {model_name} x {slug}: {e}", flush=True)
        return (slug, model_name, "FAIL", str(e))


def main():
    tasks = []
    for slug in PAPERS:
        tasks.append((slug, "GPT4o", "https://api.openai.com/v1/chat/completions", OPENAI_KEY, "gpt-4o"))
        tasks.append((slug, "Grok3", "https://api.x.ai/v1/chat/completions", XAI_KEY, "grok-3-latest"))

    print(f"Launching {len(tasks)} reviews...")
    results = []

    # Run 4 at a time to avoid rate limits
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(review_paper, *t): t for t in tasks}
        for future in as_completed(futures):
            results.append(future.result())

    print(f"\n{'='*60}")
    print(f"RESULTS: {sum(1 for r in results if r[2]=='OK')}/{len(results)} succeeded")
    for slug, model, status, detail in sorted(results):
        print(f"  {slug} x {model}: {status} ({detail})")


if __name__ == "__main__":
    main()
