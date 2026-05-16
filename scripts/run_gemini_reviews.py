#!/usr/bin/env python3
"""Run v2 external reviews on all 6 papers via Gemini 2.5 Pro."""

import os
import json
import ssl
import urllib.request
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date

BASE = Path("C:/PROJECTS/SHELL")
REVIEW_PROMPT = (BASE / "prompts" / "09_external_review.md").read_text(encoding="utf-8")
REVIEW_PROMPT = REVIEW_PROMPT.replace("[PASTE PAPER HERE]", "")
DATE = date.today().isoformat()

# Load key from api.env if not in environment
GOOGLE_KEY = os.environ.get("GOOGLE_API_KEY", "")
if not GOOGLE_KEY:
    env_path = BASE / "api.env"
    for line in env_path.read_text().splitlines():
        if line.startswith("GOOGLE_API_KEY="):
            GOOGLE_KEY = line.split("=", 1)[1].strip().strip('"')
            break

if not GOOGLE_KEY:
    raise RuntimeError("GOOGLE_API_KEY not found")

PAPERS = [
    "REPLICATION_CRISIS_2026_2026-05-15_003",
    "TECH_LOCKIN_2026_2026-05-15_003",
    "VACCINE_GAME_2026_2026-05-15_002",
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def call_gemini(prompt):
    """Call Gemini 2.5 Pro via Google AI Studio API."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-pro:generateContent?key={GOOGLE_KEY}"
    body = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 16384,
        }
    }).encode("utf-8")

    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600, context=ctx) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    return data["candidates"][0]["content"]["parts"][0]["text"]


def review_paper(slug):
    """Run a single Gemini review and save to disk."""
    paper_path = BASE / "papers" / slug / "best_paper.md"
    out_path = BASE / "papers" / slug / "reviews" / f"Gemini25Pro_review_{DATE}.md"

    paper_content = paper_path.read_text(encoding="utf-8")
    full_prompt = f"{REVIEW_PROMPT}\n\n---\n\n{paper_content}"

    print(f"  Starting Gemini review of {slug}...", flush=True)
    try:
        result = call_gemini(full_prompt)
        out_path.write_text(result, encoding="utf-8")
        print(f"  DONE: Gemini x {slug} ({len(result)} chars)", flush=True)
        return (slug, "OK", len(result))
    except Exception as e:
        error_msg = f"ERROR: {e}"
        out_path.write_text(error_msg, encoding="utf-8")
        print(f"  FAIL: Gemini x {slug}: {e}", flush=True)
        return (slug, "FAIL", str(e))


def main():
    print(f"Launching 6 Gemini 2.5 Pro reviews...")
    results = []

    # 1 at a time to stay within Gemini rate limits
    with ThreadPoolExecutor(max_workers=1) as executor:
        futures = {executor.submit(review_paper, slug): slug for slug in PAPERS}
        for future in as_completed(futures):
            results.append(future.result())

    print(f"\n{'='*60}")
    print(f"RESULTS: {sum(1 for r in results if r[1]=='OK')}/{len(results)} succeeded")
    for slug, status, detail in sorted(results):
        print(f"  {slug}: {status} ({detail})")


if __name__ == "__main__":
    main()
