# SHELL v7 Roadmap — End-to-End Autonomous Research Pipeline
# Date: 2026-06-08
# Focus: PROSPECT → ASSAY → SHELL closed loop
# Principle: What needs to be done. No time estimates.

---

## Guiding Priorities

1. End-to-end loop first (PROSPECT → ASSAY → SHELL without manual handoffs)
2. Fix what's broken before optimizing what works
3. Quality improvements that cost $0 (prompt changes) before cost optimizations
4. Every change validated against a canonical regression test

---

## Phase 1: Fix What's Broken

These are bugs and contradictions that waste money on every run.

### 1.1 Fix CR-1: ASSAY Citation Contradiction
- File: `prompts/06_peer_reviewer.md` U8e
- Change: Replace "ASSAY report ID cited" with "public data source cited + Data Appendix reference"
- Validates: Run any ASSAY-integrated paper, confirm no PR/Author loop

### 1.2 Fix IMP-1: Duplicate Rule 6 in Author Prompt
- File: `prompts/05_author.md`
- Change: Renumber second RULE 6 → RULE 7, cascade through RULE 10

### 1.3 Fix IMP-2: LEARNINGS.md Contradictory Example
- File: `LEARNINGS.md` lines 17-19
- Change: Update "GOOD" example to use public-data-source citation format

### 1.4 Fix IMP-3: Lean-Ready Proofs
- File: `prompts/05_author.md` Rule 3
- Change: Add venue-conditional clause

### 1.5 Rotate API Keys
- File: `api.env`
- Change: Rotate all 5 keys. Verify `git log --all -- api.env` shows no history.

### 1.6 Fix CR-3: SSL Verification
- File: `scripts/run_reviews.py` lines 50-52
- Change: Remove `CERT_NONE`. Add proxy CA cert if needed.

### 1.7 Fix IMP-4: extract_verdict()
- File: `src/quality_loop.py` lines 293-307
- Change: Remove first branch, rely on VERDICT section regex only

### 1.8 Fix IMP-5: API Response Validation
- File: `scripts/run_reviews.py`
- Change: Add defensive `.get()` access on API response structure

---

## Phase 2: Quality Improvements (Prompt Changes, $0 Cost)

Address the four consistent weaknesses identified by paper reviews:
trivial formalism, repetition, mechanical hedging, no surprise.

### 2.1 Add Formalism Budget to Author Prompt
- File: `prompts/05_author.md`
- Add rule: Max 2 numbered Theorems per paper. Result earns Theorem status
  ONLY if proof technique is non-obvious. Everything else is Proposition,
  Remark, or inline observation.

### 2.2 Add Hedging Budget to Author Prompt
- File: `prompts/05_author.md`
- Add rule: Max 5 self-qualifications total. State each limitation ONCE,
  in ONE location. Leave 2 obvious objections for the reviewer to find.

### 2.3 Add Deduplication Agent to Pipeline
- File: `prompts/04_paper_orchestrator.md`
- Add step after M4 assembly, before full-paper Steelman:
  Dispatch Sonnet agent to find and remove duplicate claims/caveats.
  Instruction: keep best version, delete all others. No length target.

### 2.4 Strengthen Rule 0E (No Performative Formalism)
- File: `prompts/05_author.md`
- Expand: "If a result follows from substitution, the chain rule, or the
  definition of the objects, it is NOT a Theorem. State it as a Remark or
  inline observation. Reviewers penalize formalism that performs rigor
  without providing insight."

### 2.5 Add Discovery-Framing Guidance
- File: `prompts/05_author.md`
- Add rule: "When the paper reports a finding discovered from data (not
  derived from theory), lead with the finding. The discovery IS the
  contribution. The mathematical framework is the lens, not the result.
  Do not inflate the framework to compensate for simple math."

---

## Phase 3: Cost Optimizations

### 3.1 Model Selection Per Role
- File: `prompts/04_paper_orchestrator.md`
- Change: Specify model per dispatch:
  - Author: opus
  - Steelman GATING: opus
  - Peer Reviewer: sonnet
  - Editor: sonnet
  - Steelman ADVISORY: sonnet
  - Deduplication agent: sonnet
  - Init validation: sonnet
- Expected savings: ~$6.50/run (~40% of dispatch costs)

### 3.2 Skip Advisory Steelman on M3 and M4
- File: `prompts/04_paper_orchestrator.md`
- Change: Remove Steelman dispatch for ADVISORY mode milestones.
  Full-paper Steelman at the end reviews everything.
- Expected savings: ~$3/run (2 fewer dispatches)

### 3.3 Merge M3+M4 into Single Author Dispatch
- File: `prompts/04_paper_orchestrator.md`
- Change: After M2 locks, dispatch Author once for Sections 3-7
  (Application, Boundary Conditions, Related Work, Discussion, Conclusion,
  Abstract, References). Single PR pass on combined output.
- Keep M1 and M2 separately gated (cascading dependency protection).
- Expected savings: ~$4/run (2 fewer dispatches)

### 3.4 Compact Findings Pre-Loading
- File: `src/consolidate.py`
- Add: `--compact` flag that outputs only universal findings (recurrence >= 2)
  in one-line format, optionally filtered by topic keywords.
- Expected savings: ~$0.89/run (20K fewer input tokens)

---

## Phase 4: End-to-End Pipeline (PROSPECT → ASSAY → SHELL)

This is the primary focus. Close the loop so discoveries flow automatically
from raw data to published papers.

### 4.1 Init File Generator from PROSPECT Findings
- New file: `src/generate_init.py`
- Input: PROSPECT finding YAML + ASSAY integration_block.yaml
- Output: Complete SHELL init file with:
  - Research question derived from finding description
  - Frozen spec with ASSAY-computed parameters
  - KNOWN_DRIFT_RISKS from compact universal findings
  - ASSAY integration block references
  - Target venue (inferred from domain)
- Eliminates manual init writing (saves 30-60 min, prevents bad inits)

### 4.2 Init Validation Gate
- New step in pipeline, before expensive paper generation
- Dispatch one Sonnet agent (~$1) to validate:
  - Frozen spec complete?
  - ASSAY integration block accessible and within model domain?
  - KNOWN_DRIFT_RISKS populated?
  - Research question produces falsifiable prediction?
- PASS → proceed. FAIL → halt with specific issues.

### 4.3 PROSPECT → ASSAY Handoff Automation
- New file: `src/prospect_to_assay.py`
- Input: PROSPECT finding YAML (status: assay_ready)
- Output: ASSAY frozen_analysis_spec.md generated from finding metadata
- Triggers ASSAY pipeline on the finding
- On ASSAY completion: marks finding status as `assay_verified` or `assay_failed`

### 4.4 ASSAY → SHELL Handoff Automation
- New file: `src/assay_to_shell.py`
- Input: ASSAY integration_block.yaml (from verified report)
- Calls `generate_init.py` to create SHELL init
- Calls init validation gate
- On PASS: triggers SHELL pipeline
- On completion: triggers external review

### 4.5 Pipeline Orchestrator (Full Loop)
- New file: `src/run_discovery.py`
- Input: PROSPECT finding YAML or dataset name
- Orchestrates: PROSPECT → ASSAY → SHELL → External Review
- Tracks state across all three systems
- Logs to a unified discovery_log.md
- This is the entry point for the commercial product

### 4.6 Surprise Scorer for Finding Ranking
- New file: `src/surprise_score.py`
- Input: PROSPECT finding YAML
- Computes:
  - Scale score: dollar magnitude or population affected
  - Testability score: does the finding produce a quantifiable prediction?
  - Novelty score: semantic distance from existing papers (via OpenAlex API
    or local embedding if available)
- Output: ranked findings list
- Top findings get priority for ASSAY → SHELL pipeline

---

## Phase 5: Canonical Regression Testing

### 5.1 Establish Drug Spending as Canonical Test
- File: `papers/init_DRUG_SPENDING.md` (existing)
- Baseline: Gemini 9.18, Grok 8.09 (v6.5 scores)
- After ANY pipeline change:
  1. Run Drug Spending through modified pipeline
  2. Run external reviews
  3. Compare scores via `parse_reviews.py --baseline 2026-05-15`
  4. If any dimension drops >1 point: revert the change

### 5.2 Add Discovery-Paper Canary
- After Phase 4 is complete, generate one paper from a PROSPECT finding
  (e.g., wound care $3.26B) through the full loop
- This becomes the second canary — tests the end-to-end pipeline
- Baseline its external review scores
- Run after any pipeline change that affects the PROSPECT → SHELL flow

### 5.3 Automated Regression Script
- New file: `src/regression_canary.py`
- Runs canonical paper, runs external reviews, compares against baseline
- Outputs: PASS (all dimensions within tolerance) or FAIL (with specifics)
- Called after every significant pipeline change

---

## Phase 6: Infrastructure Hardening (Pre-AWS)

### 6.1 Unit Tests for Critical Parsing Functions
- New directory: `tests/`
- Priority test targets:
  - `extract_verdict()` — pipeline-critical decision function
  - `parse_citation_line()` — customer-facing output
  - `categorize_finding()` — findings database integrity
  - `is_duplicate()` — deduplication accuracy
  - `_extract_claims()` — regression fixture integrity

### 6.2 Remove Hardcoded Paths
- Files: `scripts/run_reviews.py`, `scripts/parse_reviews.py`,
  `scripts/revise_from_review.py`
- Change: Use `Path(__file__).resolve().parent.parent`

### 6.3 Add File Locking to consolidate.py
- Use `filelock` library for read-modify-write on shared files
- Prevents corruption when multiple sessions run concurrently

### 6.4 Add Dispatch Timeout to quality_loop.py
- Add configurable timeout (default 60 min) to `process.wait()`
- Log warning before termination

### 6.5 Clean Up Legacy Code
- Move `src/run_pipeline.ps1` and legacy `quality_loop.py` external loop
  to `archive/` directory
- Update README to clarify current entry points

### 6.6 Replace Claude CLI with Direct API Calls
- Required for AWS deployment (no CLI in containers)
- Each agent dispatch becomes `anthropic.messages.create()` call
- Enables: model selection per role, token tracking, cost metering
- Eliminates: `--dangerously-skip-permissions` security concern
- This is the largest single engineering task in the roadmap

---

## Phase 7: Paper Quality Scoring and Feedback Loop

### 7.1 Automated Findings Analysis
- New file: `src/analyze_findings.py`
- Input: STEELMAN_FINDINGS.md, DEAD_ENDS.md
- Output: Statistics on finding categories, recurrence patterns,
  which checklist items trigger most rejections
- Identifies systematic Author tendencies for targeted prompt fixes

### 7.2 External Review Score Tracking
- New file: `src/track_scores.py`
- Input: All review files across all papers
- Output: Dimension-by-dimension trend analysis
- Answers: "Is D1 (originality) improving over time? Which prompt
  changes correlated with score improvements?"

### 7.3 Prompt A/B Testing Framework
- Modify orchestrator to accept `--prompt-variant` flag
- Run same init with variant A and variant B prompts
- Compare external review scores
- Merge whichever variant scores higher

---

## Dependency Map

```
Phase 1 (fixes) ← must be first, everything depends on correct pipeline
  ↓
Phase 2 (quality prompts) ← no dependencies, pure prompt edits
  ↓
Phase 5.1 (establish canary) ← needed before any further changes
  ↓
Phase 3 (cost optimization) ← validate each change against canary
  ↓
Phase 4 (end-to-end loop) ← the main goal, builds on fixed + optimized pipeline
  ↓
Phase 6 (infrastructure) ← hardens for AWS deployment
  ↓
Phase 7 (feedback loop) ← compounds quality over time
```

---

## What This Roadmap Does NOT Include

- AWS deployment architecture (separate document when Phase 6 is complete)
- Pricing model and customer acquisition (business decision, not engineering)
- PROSPECT or ASSAY modifications (those systems are working; focus is on
  SHELL optimization and the handoff automation)
- Novel research methodology (the surprise scorer in 4.6 is the bridge;
  deeper novelty ideas are a research agenda, not an engineering roadmap)
