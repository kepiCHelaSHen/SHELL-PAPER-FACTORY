# SHELL Code Review Report
# Date: 2026-06-08
# Reviewer: Claude Opus 4.6 (automated deep review)
# Scope: Full codebase — src/, scripts/, prompts/, docs/, config

---

## Executive Summary

SHELL (THESIS) v6.5 is a well-architected autonomous academic paper generation
pipeline with a strong adversarial validation framework. The codebase is
production-hardened with good error handling, structured logging, and a
compounding knowledge base (154 findings, 104 dead ends).

This review identified 28 issues: 3 CRITICAL, 12 IMPORTANT, 10 MODERATE, 3 MINOR.

The most urgent: one pipeline-breaking prompt contradiction that wastes $25-75
on every ASSAY-integrated paper run, and API keys exposed in plaintext.

---

## CRITICAL Issues

### CR-1: Pipeline-Breaking ASSAY Citation Contradiction

**Files:**
- `prompts/06_peer_reviewer.md` line ~120 (U8e)
- `prompts/05_author.md` lines 288-293 (Rule 5F)
- `prompts/07_editor.md` (E24)

**Problem:** The Peer Reviewer (U8e) demands: "Is the specific ASSAY report ID
cited for every ASSAY-derived number? If not: REJECT." The Author (Rule 5F)
demands: "NEVER cite 'ASSAY Report [ID]' in the paper body." The Editor (E24)
enforces the Author's rule by scanning for ASSAY report strings.

The Author cannot satisfy both agents simultaneously. Every ASSAY-integrated
paper either loops indefinitely or wastes a full pipeline run ($25-75).

**Fix:** Replace U8e in `prompts/06_peer_reviewer.md` with:
```
(e) **ASSAY values sourced.** Is every ASSAY-derived number traceable to a
public data source citation and a Data Appendix reference? If not: REJECT.
```

**Impact:** Pipeline-breaking. Every ASSAY-integrated run is affected.

---

### CR-2: Plaintext API Keys on Disk

**File:** `api.env`

Five live API keys in plaintext:
- XAI_API_KEY (xAI/Grok)
- OPENAI_API_KEY (OpenAI)
- ZENODO_SANDBOX_TOKEN
- ZENODO_TOKEN (production — can publish under your identity)
- GOOGLE_API_KEY

**Mitigating factor:** `.gitignore` lists `api.env`, `*.env`, `.env`. The file
is NOT tracked in git history. Keys are not in the repository.

**Remaining risk:** Keys sit in plaintext on disk. Any process running as the
user, any malware, or any accidental file share exposes all five keys. The
Zenodo production token is especially sensitive.

**Fix:**
1. Rotate all 5 keys immediately.
2. Move to environment variables set in user-level profile, or use Windows
   Credential Manager / AWS Secrets Manager (for future AWS deployment).
3. Verify with `git log --all -- api.env` that keys were never committed.

---

### CR-3: SSL Verification Globally Disabled

**Files:**
- `scripts/run_reviews.py` lines 50-52
- Likely also in `src/zenodo/api.py`

```python
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
```

**Problem:** Every API call (Grok, Gemini, Zenodo) is vulnerable to
man-in-the-middle attacks. An attacker on the network could intercept API keys
in transit or inject false review content.

**Fix:** Remove `CERT_NONE`. If a corporate proxy requires custom CA:
```python
ctx = ssl.create_default_context(cafile="/path/to/proxy-ca.pem")
```

---

## IMPORTANT Issues

### IMP-1: Duplicate Rule 6 in Author Prompt

**File:** `prompts/05_author.md`
- Line ~316: "## RULE 6 — FIGURE CODE OUTPUT"
- Line ~339: "## RULE 6 — CLAIMS VS. SUPPORT"

**Fix:** Renumber second RULE 6 to RULE 7. Cascade: current RULE 7 → 8,
RULE 8 → 9, RULE 9 → 10.

---

### IMP-2: LEARNINGS.md Contradicts Author Rule 5F

**File:** `LEARNINGS.md` lines 17-19

The "GOOD" example shows: "Setting phi = 7.39 (ASSAY Report PHI_EST, 95% CI
[5.0, 10.5])..." — the exact citation format Rule 5F bans.

LEARNINGS.md is mandatory reading (per CLAUDE.md), so agents encounter
contradictory guidance on every run.

**Fix:** Update the example to:
```
"Setting phi = 7.39 (95% CI [5.0, 10.5]; computed from Camerer et al.
replication data via bootstrap, n = 21; see Data Appendix) in Theorem 1
yields phi* = 2.0 for psychology..."
```

---

### IMP-3: Lean-Ready Proofs Unconditional vs Venue-Specific

**Files:**
- `prompts/05_author.md` Rule 3 (unconditional: "Every proof must be Lean-ready")
- `prompts/04_paper_orchestrator.md` lines 474-479 (venue-conditional)

**Fix:** Add to Rule 3:
```
The level of proof formalism is determined by the frozen spec's target venue.
For formal theory venues (Econometrica, JET), structure proofs for machine-
verification readiness. For applied venues (PNAS, Health Affairs, JHE),
proofs should be rigorous but need not claim Lean/Coq readiness.
```

---

### IMP-4: extract_verdict() Fragile Parsing

**File:** `src/quality_loop.py` lines 293-307

The first branch checks for "ACCEPT" anywhere in the text. A critique
mentioning "ACCEPT" in discussion (not the verdict section) triggers false
positives. The `re.DOTALL` fallback can match across sections incorrectly.

**Fix:** Remove the first branch entirely. Rely solely on the regex that
specifically searches the VERDICT section:
```python
def extract_verdict(critique: str) -> str:
    verdict_match = re.search(
        r"##\s*VERDICT\s*\n+\s*[-*]?\s*(ACCEPT|MAJOR_REVISION|REJECT)",
        critique, re.IGNORECASE,
    )
    if verdict_match:
        return verdict_match.group(1).upper()
    # Fallback: search for verdict keywords in order of severity
    for v in ["REJECT", "MAJOR_REVISION", "ACCEPT"]:
        if re.search(rf"##\s*VERDICT.*?{v}", critique, re.IGNORECASE | re.DOTALL):
            return v
    return "UNKNOWN"
```

---

### IMP-5: No API Response Validation

**File:** `scripts/run_reviews.py` lines 59-73

```python
return data["choices"][0]["message"]["content"]
```

Crashes on unexpected response structure (empty choices, missing content key).

**Fix:**
```python
choices = data.get("choices", [])
if not choices:
    return "ERROR: Empty response from API"
content = choices[0].get("message", {}).get("content", "")
if not content:
    return "ERROR: No content in API response"
return content
```

Same pattern needed for `call_gemini()` on line ~90.

---

### IMP-6: No Cost Controls or Token Budget

The pipeline has no mechanism to track or limit API spending. A 5-iteration x
4-milestone x 3-run loop could burn significant tokens with no automatic stop.

**Fix:** Add a `MAX_DISPATCHES` parameter to the orchestrator (default: 30).
Track cumulative dispatches. If exceeded, halt with reason. Also log estimated
token count per dispatch for post-run cost analysis.

---

### IMP-7: No Concurrency Safety for Shared Files

`consolidate.py` uses read-modify-write on STEELMAN_FINDINGS.md and
DEAD_ENDS.md. `launch-shell.ps1` opens 4 concurrent Claude sessions. Two
simultaneous `consolidate.py` runs can corrupt the findings database.

**Fix:** Add file locking via `filelock` library (pip install filelock):
```python
from filelock import FileLock
lock = FileLock(str(log_path) + ".lock", timeout=30)
with lock:
    text = log_path.read_text(...)
    # ... modify ...
    log_path.write_text(text, ...)
```

---

### IMP-8: No Unit Tests

Zero `test_*.py` files. No `tests/` directory. The regex-heavy parsing
functions are the most likely to break silently:

- `extract_verdict()` in quality_loop.py
- `parse_citation_line()` in verify_citations.py
- `categorize_finding()` in consolidate.py
- `is_duplicate()` in consolidate.py
- `check_match()` in verify_citations.py
- `_extract_claims()` in regression_tests.py

**Fix:** Create `tests/` directory with unit tests for each parsing function.
Priority: `extract_verdict` (pipeline-critical) and `parse_citation_line`
(customer-facing output).

---

### IMP-9: No Timeout on Paper Generation

**File:** `src/quality_loop.py` lines 160-166

`process.wait()` has no timeout. A stuck Claude session blocks indefinitely.

**Fix:** Add configurable timeout (default 60 minutes):
```python
try:
    process.wait(timeout=3600)
except subprocess.TimeoutExpired:
    process.terminate()
    log("WARNING: Claude CLI timed out after 60 minutes", meta_log)
```

---

### IMP-10: Google API Key in URL Query Parameter

**File:** `scripts/run_reviews.py` line 78

The API key is passed as a URL query parameter, visible in server logs, proxy
logs, and network monitoring. Combined with disabled SSL (CR-3), this
compounds the exposure risk. This is a Google API design constraint — the
Generative AI API requires the key in the URL.

**Fix:** After fixing CR-3 (re-enable SSL), the key is at least encrypted in
transit. Document this as an accepted residual risk.

---

### IMP-11: Dead Code (TeeWriter)

**File:** `src/quality_loop.py` lines 42-60

`TeeWriter` class is defined but never instantiated anywhere in the codebase.
Likely a remnant from an earlier logging approach.

**Fix:** Remove the class.

---

### IMP-12: `--dangerously-skip-permissions` Universal Usage

Found in 30+ locations across `.ps1`, `.py`, `.md` files. Gives the LLM
unrestricted file system and shell access. External review content from
Grok/Gemini flows back into Claude contexts, creating a prompt injection
surface.

**Fix (short-term):** Document as accepted risk with explicit threat model.
**Fix (long-term, for AWS):** Replace Claude CLI with direct API calls
(`anthropic.messages.create()`). No permissions flag needed — you control
exactly what the model can do.

---

## MODERATE Issues

### MOD-1: Hardcoded Paths in scripts/

**Files:** `scripts/run_reviews.py`, `scripts/parse_reviews.py`,
`scripts/revise_from_review.py` — all hardcode `Path("C:/PROJECTS/SHELL")`.

The `src/` files correctly use `Path(__file__).parent.parent`.

**Fix:** Use `Path(__file__).resolve().parent.parent` in all scripts.

---

### MOD-2: Legacy Code Not Cleaned Up

`src/run_pipeline.ps1` (75 lines) is a legacy v3/v4 milestone runner.
`quality_loop.py` implements the old external quality loop with init-file
patching. Both are superseded by the v5 orchestrator.

**Fix:** Rename to `_legacy_run_pipeline.ps1` and `_legacy_quality_loop.py`,
or move to an `archive/` directory.

---

### MOD-3: Editor Checklist Overlap with Steelman

`prompts/07_editor.md` has 24 checklist items (E1-E24). Items E16-E20 overlap
with Steelman checks (ST1-ST5). Each includes "If the Steelman critique
flagged X, verify whether the Author addressed it" — but the cognitive load
risks shallow reviews across all 24 items.

**Fix:** Split into "core editorial" (E1-E15) always run, and "Steelman
verification" (E16-E24) conditional on Steelman having flagged issues.

---

### MOD-4: Lambda Closure Pattern in run_reviews.py

**File:** `scripts/run_reviews.py` lines 154-159

Lambdas in a loop capture variables by reference. Currently safe (captured
variables aren't used inside the lambda), but fragile — any future edit that
references loop variables inside the lambda will cause subtle bugs.

**Fix:** Use `functools.partial` instead of lambdas for API call wrappers.

---

### MOD-5: consolidate.py Reimports sys, io

**File:** `src/consolidate.py` line 529

`sys` already imported at module level. `io` imported inside `main()`.

**Fix:** Move `io` import to module level. Remove duplicate `sys` import.

---

### MOD-6: Version Number Inconsistencies

- `prompts/04_paper_orchestrator.md` line 923: `SHELL_VERSION: 6.3`
- `CLAUDE.md`: references v6.5
- `publish_config.yaml` line 14: v6.5
- `README.md` line 4: v6.3

**Fix:** Update all to consistent version number. When v7 ships, update all
simultaneously.

---

### MOD-7: verify_citations.py Writes to CWD

**File:** `src/verify_citations.py` lines 438-440

Output directory is `os.path.join(os.getcwd(), "outputs")` — relative to
wherever the script is invoked, not the paper's project directory.

**Fix:** Derive output from paper path:
```python
out_dir = os.path.join(os.path.dirname(os.path.abspath(args.paper)), "outputs")
```

---

### MOD-8: CrossRef Email Placeholder

**File:** `src/verify_citations.py` line 30

```python
"User-Agent": "VerifyCitations/1.0 (mailto:your-email@example.com)"
```

CrossRef uses mailto for polite pool routing. Placeholder email means
requests go through the anonymous pool with stricter rate limits.

**Fix:** Replace with actual email address.

---

### MOD-9: consolidate.py Full-File Read-Modify-Write at Scale

Every `append_finding()` or `append_dead_end()` reads the entire
STEELMAN_FINDINGS.md into memory, performs regex operations, and writes it
back. At 154 findings this is fine. At 1,000+ it will slow noticeably.

**Fix (future):** Migrate to structured format (JSON or SQLite) when finding
count exceeds ~500. For now, acceptable.

---

### MOD-10: No Self-Tests for Regression Fixture Extraction

`regression_tests.py` extracts fixtures via regex but has no tests for its
own extraction accuracy. A paper format change could silently break extraction.

**Fix:** Add tests with sample paper snippets that verify claim extraction,
citation extraction, and numerical result extraction produce expected output.

---

## MINOR Issues

### MIN-1: Inconsistent pathlib vs os.path Usage

`src/` files use `pathlib.Path` consistently. `verify_citations.py` uses
`os.path` throughout. `scripts/` use hardcoded strings.

**Fix:** Standardize on `pathlib.Path` across all files.

---

### MIN-2: Missing Type Hints

Several functions in `consolidate.py` and `quality_loop.py` lack return type
hints (`patch_init_file`, `backfill`, `show_universal`).

**Fix:** Add return type annotations to all public functions.

---

### MIN-3: paper_to_thread.py Hardcoded DOI

Line 218 hardcodes the DVL framework DOI and Zenodo reference. Not documented
in any operational guide.

**Fix:** Move DOI to a config constant or pull from publish_config.yaml.

---

## Issue Summary Table

| ID | Severity | Category | File(s) |
|----|----------|----------|---------|
| CR-1 | CRITICAL | Contradiction | 06_peer_reviewer.md vs 05_author.md |
| CR-2 | CRITICAL | Security | api.env |
| CR-3 | CRITICAL | Security | run_reviews.py |
| IMP-1 | IMPORTANT | Contradiction | 05_author.md |
| IMP-2 | IMPORTANT | Contradiction | LEARNINGS.md |
| IMP-3 | IMPORTANT | Contradiction | 05_author.md vs 04_orchestrator.md |
| IMP-4 | IMPORTANT | Code Quality | quality_loop.py |
| IMP-5 | IMPORTANT | Code Quality | run_reviews.py |
| IMP-6 | IMPORTANT | Architecture | Pipeline-wide |
| IMP-7 | IMPORTANT | Architecture | consolidate.py |
| IMP-8 | IMPORTANT | Testing | Project-wide |
| IMP-9 | IMPORTANT | Operations | quality_loop.py |
| IMP-10 | IMPORTANT | Security | run_reviews.py |
| IMP-11 | IMPORTANT | Code Quality | quality_loop.py |
| IMP-12 | IMPORTANT | Security | 30+ files |
| MOD-1 | MODERATE | Code Quality | scripts/*.py |
| MOD-2 | MODERATE | Architecture | run_pipeline.ps1, quality_loop.py |
| MOD-3 | MODERATE | Prompts | 07_editor.md |
| MOD-4 | MODERATE | Code Quality | run_reviews.py |
| MOD-5 | MODERATE | Code Quality | consolidate.py |
| MOD-6 | MODERATE | Documentation | Multiple |
| MOD-7 | MODERATE | Operations | verify_citations.py |
| MOD-8 | MODERATE | Operations | verify_citations.py |
| MOD-9 | MODERATE | Scalability | consolidate.py |
| MOD-10 | MODERATE | Testing | regression_tests.py |
| MIN-1 | MINOR | Code Quality | Mixed |
| MIN-2 | MINOR | Code Quality | Multiple |
| MIN-3 | MINOR | Documentation | paper_to_thread.py |
