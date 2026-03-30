# SHELL v5.0 — Plumbing Fixes + Structured Innovation Log

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix 6 plumbing bugs that will cause pipeline failures, add structured innovation log for machine-parseable drift analysis, add cost tracking to run manifest, and document parallel comparison process.

**Architecture:** All changes are to existing prompt files and one Python script. No new architectural patterns. The structured innovation log replaces the free-form format with YAML blocks inside markdown, parseable by both humans and scripts. Plumbing fixes are minimal, targeted edits.

**Tech Stack:** Markdown prompts, Python 3, PowerShell

---

## File Map

| File | Action | What Changes |
|------|--------|-------------|
| `prompts/04_paper_orchestrator.md` | Modify | api.env absolute path, Editor revision loop, structured log format, cost tracking in manifest |
| `prompts/00_init.md` | Modify | Fix duplicate step numbering, structured log template |
| `prompts/run_milestone.md` | Modify | api.env absolute path, DRIFT_RISKS from frozen spec |
| `src/verify_citations.py` | Modify | Output directory relative to cwd |
| `state/innovation_log.md` | Modify | New structured format template |
| `BEST_PRACTICES.md` | Modify | Add parallel comparison process |
| `README.md` | Modify | Version bump to 5.0 |

---

### Task 1: Fix api.env absolute path

The orchestrator and run_milestone.md say "Load from api.env" but project directories don't have api.env. Use absolute path to SHELL's copy.

**Files:**
- Modify: `prompts/04_paper_orchestrator.md` (ENVIRONMENT section, ~line 44-48)
- Modify: `prompts/run_milestone.md` (api.env reference, ~line 51-53)

- [ ] **Step 1: Update 04_paper_orchestrator.md ENVIRONMENT section**

Replace:
```
Load from api.env:
- XAI_API_KEY → xAI API, model: grok-3 (Author role)
- OPENAI_API_KEY → OpenAI API, model: gpt-4o (Peer Reviewer role)
- Claude CLI handles your own calls natively (Editor + Orchestrator)
```

With:
```
Load API keys from D:\EXPERIMENTS\SHELL\api.env (absolute path — single
source of truth, never copied into project directories):
- XAI_API_KEY → xAI API, model: grok-3 (Author role)
- OPENAI_API_KEY → OpenAI API, model: gpt-4o (Peer Reviewer role)
- Claude CLI handles your own calls natively (Editor + Orchestrator)

Read the file, parse KEY="VALUE" lines. If the file is missing or a key
is empty, HALT and report: "API key not found. Check D:\EXPERIMENTS\SHELL\api.env"
```

- [ ] **Step 2: Update run_milestone.md api.env reference**

Replace:
```
Load API keys from api.env:
  XAI_API_KEY → xAI API for Author (Grok-3)
  OPENAI_API_KEY → OpenAI API for Peer Reviewer (GPT-4o)
```

With:
```
Load API keys from D:\EXPERIMENTS\SHELL\api.env (absolute path):
  XAI_API_KEY → xAI API for Author (Grok-3)
  OPENAI_API_KEY → OpenAI API for Peer Reviewer (GPT-4o)
```

- [ ] **Step 3: Commit**

```bash
git add prompts/04_paper_orchestrator.md prompts/run_milestone.md
git commit -m "fix: api.env absolute path — single source of truth in SHELL"
```

---

### Task 2: Fix DRIFT_RISKS extraction from frozen spec

run_milestone.md says it receives DRIFT_RISKS from run_pipeline.ps1 but the script never passes them. The orchestrator should extract them from the frozen spec's KNOWN PRIOR DRIFT RISK section.

**Files:**
- Modify: `prompts/run_milestone.md` (~line 92-95, INPUTS section)
- Modify: `prompts/04_paper_orchestrator.md` (each Author prompt)

- [ ] **Step 1: Update run_milestone.md INPUTS section**

Replace:
```
## INPUTS PASSED BY run_pipeline.ps1

SLUG: [project slug]
DRIFT_RISKS: [contents of KNOWN_DRIFT_RISKS from init file or frozen spec]
```

With:
```
## INPUTS PASSED BY run_pipeline.ps1

SLUG: [project slug]

## DRIFT_RISKS — EXTRACTED FROM FROZEN SPEC

Do NOT rely on run_pipeline.ps1 to pass drift risks. Read them directly
from spec/frozen_spec.md. The frozen spec contains a "KNOWN PRIOR DRIFT RISK"
section — extract all entries and pass them to the Author on every call.

If spec/frozen_spec.md has no drift risk section, log:
  "WARNING: No drift risks found in frozen spec. Author will generate without
   drift guidance."
```

- [ ] **Step 2: Commit**

```bash
git add prompts/run_milestone.md
git commit -m "fix: extract DRIFT_RISKS from frozen spec, not run_pipeline.ps1"
```

---

### Task 3: Fix Editor rejection loop

When the Editor rejects, the pipeline currently implies Claude self-edits. It should route back to the Author (Grok-3) for revision, maintaining triangulation.

**Files:**
- Modify: `prompts/04_paper_orchestrator.md` (Editor section near line 307-316)

- [ ] **Step 1: Update Editor section in 04_paper_orchestrator.md**

Replace:
```
Editor ACCEPT → write final paper → run figure generation.
Editor REJECT → apply fixes, re-run Editor. Max 3 loops.
```

With:
```
Editor ACCEPT → write final paper → run figure generation.
Editor REJECT → send rejection list back to Author (Grok-3) for revision:

  API: xAI | model: grok-3 | temperature: 0.7 | max_tokens: 12000
  System: [full contents of prompts/05_author.md]
  User:
    MILESTONE: M4 — Editorial Revision
    YOUR TASK: Fix every issue listed below. Do not introduce new problems.
    Return the full revised paper.
    EDITOR REJECTION LIST: [numbered list from Editor]
    CURRENT DRAFT: [full contents of M4_draft.md]

  Write revised output to papers/[SLUG]/M4_draft.md. Re-run Editor.
  Max 3 Editor loops. If Editor still rejects after 3: log issues in
  innovation log, write paper anyway with EDITORIAL_WARNING flag.
```

- [ ] **Step 2: Commit**

```bash
git add prompts/04_paper_orchestrator.md
git commit -m "fix: Editor rejection routes to Author (Grok-3), not self-edit"
```

---

### Task 4: Fix verify_citations.py output directory

The script writes relative to its own location (SHELL/outputs/) instead of the project's outputs/ directory.

**Files:**
- Modify: `src/verify_citations.py` (~line 438-443)

- [ ] **Step 1: Replace output directory logic**

Replace lines 438-443:
```python
    # Ensure output directory exists
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "outputs")
    out_dir = os.path.normpath(out_dir)
    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, "citation_verification.md")
```

With:
```python
    # Write to outputs/ in current working directory (the project root)
    out_dir = os.path.join(os.getcwd(), "outputs")
    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, "citation_verification.md")
```

- [ ] **Step 2: Commit**

```bash
git add src/verify_citations.py
git commit -m "fix: citation report writes to project outputs/ not SHELL outputs/"
```

---

### Task 5: Fix duplicate step numbering in 00_init.md

Step 16 appears twice (git init and print confirmation).

**Files:**
- Modify: `prompts/00_init.md` (~line 367-378)

- [ ] **Step 1: Renumber steps**

Change second "Step 16" (print confirmation) to "Step 17".
Change current "Step 17" (hand off) to "Step 18".

- [ ] **Step 2: Commit**

```bash
git add prompts/00_init.md
git commit -m "fix: duplicate step numbering in 00_init.md"
```

---

### Task 6: Add spec fingerprinting

Compute SHA-256 of frozen_spec.md at init. Verify at each milestone start. If hash changed, the spec was tampered — halt immediately.

**Files:**
- Modify: `prompts/04_paper_orchestrator.md` (INITIALIZE section + milestone loop)
- Modify: `prompts/run_milestone.md` (ON STARTUP section)

- [ ] **Step 1: Add fingerprint to INITIALIZE in 04_paper_orchestrator.md**

After step 5 in the INITIALIZE section (git init), add:

```
6. Compute frozen spec fingerprint:
     Run: python -c "import hashlib; print(hashlib.sha256(open('spec/frozen_spec.md','rb').read()).hexdigest())"
     Store the output as SPEC_FINGERPRINT.
     Write to papers/[SLUG]/state_vector.md:
       SPEC_FINGERPRINT: [hash]
```

- [ ] **Step 2: Add verification to THE MILESTONE LOOP in 04_paper_orchestrator.md**

Before each milestone begins (before the Author call), add to the milestone loop intro:

```
Before each milestone, verify spec integrity:
  Run: python -c "import hashlib; print(hashlib.sha256(open('spec/frozen_spec.md','rb').read()).hexdigest())"
  Compare result to SPEC_FINGERPRINT in papers/[SLUG]/state_vector.md.
  If mismatch: HALT immediately.
    Write: "SPEC INTEGRITY FAILURE — frozen_spec.md was modified after lock.
            Expected: [stored hash]. Got: [current hash]."
    This is a fatal error. The experiment is invalid.
```

- [ ] **Step 3: Add verification to run_milestone.md ON STARTUP**

After reading the state vector (step 1 in ON STARTUP), add:

```
1b. Verify frozen spec integrity:
    If state vector contains SPEC_FINGERPRINT:
      Compute: python -c "import hashlib; print(hashlib.sha256(open('spec/frozen_spec.md','rb').read()).hexdigest())"
      Compare to stored fingerprint. Mismatch → HALT.
```

- [ ] **Step 4: Commit**

```bash
git add prompts/04_paper_orchestrator.md prompts/run_milestone.md
git commit -m "feat: spec fingerprinting — SHA-256 integrity check at every milestone"
```

---

### Task 7: Structured innovation log format

Replace free-form innovation log with YAML blocks inside markdown. Machine-parseable, human-readable.

**Files:**
- Modify: `state/innovation_log.md` (new template format)
- Modify: `prompts/04_paper_orchestrator.md` (milestone ACCEPT logging + drift report parsing)
- Modify: `prompts/00_init.md` (Step 10 innovation log template)

- [ ] **Step 1: Update innovation_log.md template in SHELL**

Replace current contents with:

```markdown
# INNOVATION LOG
# Append-only. Never edit previous entries. Add to bottom only.
# Managed by Orchestrator. One entry per milestone attempt.
# Format: YAML blocks inside markdown for machine + human readability.

=== EXPERIMENT: [EXPERIMENT NAME] ===
=== LOOP INITIALIZED: [TIMESTAMP] ===
=== FROZEN SPEC LOCKED: [spec/frozen_spec.md — confirmed] ===
=== MILESTONES: M1 | M2 | M3 | M4 ===

---

# ENTRY FORMAT — copy this block for each milestone attempt:
#
# ```yaml
# turn: [N]
# timestamp: [ISO 8601]
# milestone: [M1/M2/M3/M4]
# role: [AUTHOR/PEER_REVIEWER/EDITOR]
# model: [grok-3/gpt-4o/claude]
# action: [SUBMIT/ACCEPT/REJECT]
# details:
#   checklist_items_failed: []
#   parameters_drifted:
#     - parameter: [name]
#       author_value: [what was proposed]
#       spec_value: [correct value]
#       drift_type: [PARAMETER_DRIFT/OVERCLAIM/UNDERCLAIM/SYMBOLIC_ERROR/STRUCTURAL_ERROR/MISSING_SECTION]
#   notes: [free text]
# ```

[Loop entries begin below on Turn 1]
```

- [ ] **Step 2: Update 04_paper_orchestrator.md milestone ACCEPT/REJECT logging**

In THE MILESTONE LOOP section, after "Append to state/innovation_log.md", specify:

After each Author submission, append:
```yaml
turn: [N]
timestamp: [ISO 8601]
milestone: [current]
role: AUTHOR
model: grok-3
action: SUBMIT
details:
  notes: "[one-line summary of what was written]"
```

After each Peer Reviewer verdict, append:
```yaml
turn: [N]
timestamp: [ISO 8601]
milestone: [current]
role: PEER_REVIEWER
model: gpt-4o
action: [ACCEPT/REJECT]
details:
  checklist_items_failed: ["M2.1(a)", "U3"]
  parameters_drifted:
    - parameter: "[name]"
      author_value: "[proposed]"
      spec_value: "[correct]"
      drift_type: "[type]"
  notes: "[one-line summary]"
```

After each Editor verdict, append:
```yaml
turn: [N]
timestamp: [ISO 8601]
milestone: M4
role: EDITOR
model: claude
action: [ACCEPT/REJECT]
details:
  checklist_items_failed: ["E6", "E14"]
  notes: "[one-line summary]"
```

- [ ] **Step 3: Update DRIFT REPORT section to parse YAML**

In the DRIFT REPORT section, change the instruction from "parse the full innovation log" to:

```
Parse the innovation log (state/innovation_log.md). Each entry is a YAML
block fenced by triple backticks. Extract all entries where action: REJECT.

For each REJECT entry:
  - Read details.checklist_items_failed
  - Read details.parameters_drifted (if any)
  - Aggregate by parameter name across all milestones

This structured format makes the drift report deterministic — no
interpretation needed, just extraction and aggregation.
```

- [ ] **Step 4: Update 00_init.md Step 10 innovation log template**

Replace the innovation log template in Step 10 with the new YAML-based format from Step 1 above, substituting [PROJECT_NAME] and [today] as before.

- [ ] **Step 5: Commit**

```bash
git add state/innovation_log.md prompts/04_paper_orchestrator.md prompts/00_init.md
git commit -m "feat: structured innovation log — YAML entries for machine-parseable drift analysis"
```

---

### Task 8: Cost tracking in run manifest

Add estimated token usage and cost to the run manifest.

**Files:**
- Modify: `prompts/04_paper_orchestrator.md` (run manifest section, ~line 523)

- [ ] **Step 1: Add cost tracking section to run manifest**

After the `## Git` section in the run manifest template, add:

```
  ## Estimated Cost
  | Role | Model | Calls | Est. Input Tokens | Est. Output Tokens | Est. Cost |
  |------|-------|-------|-------------------|-------------------|-----------|
  | Author | Grok-3 | [N] | [N]K | [N]K | $[X.XX] |
  | Peer Reviewer | GPT-4o | [N] | [N]K | [N]K | $[X.XX] |
  | Orchestrator Audit | GPT-4o | 1 | [N]K | [N]K | $[X.XX] |
  | Editor | Claude | [N] | CLI subscription | — | — |
  | Total (excl. Claude) | | | | | $[X.XX] |

  Note: Estimates based on prompt + response sizes. Actual billing may differ.
  Grok-3 pricing: ~$5/1M input, ~$15/1M output
  GPT-4o pricing: ~$2.50/1M input, ~$10/1M output
```

Also add to the MILESTONE LOOP: after each API call, the orchestrator should track:
```
  After every xAI or OpenAI API call, record:
    - Role + model
    - Approximate input token count (estimate from prompt length)
    - Output token count (from API response if available, else estimate)
  Accumulate these for the run manifest cost table.
```

- [ ] **Step 2: Commit**

```bash
git add prompts/04_paper_orchestrator.md
git commit -m "feat: cost tracking — estimated token usage and cost in run manifest"
```

---

### Task 9: Document parallel comparison process

Add the process for running the same paper twice and comparing outputs as a quality validation method.

**Files:**
- Modify: `BEST_PRACTICES.md`

- [ ] **Step 1: Add parallel comparison section to BEST_PRACTICES.md**

Append after the existing content:

```markdown
---

## Parallel Comparison (Statistical Validation for Papers)

To validate that the pipeline produces consistent results — the paper-pipeline
equivalent of multi-seed runs — run the same init file twice and compare:

1. Run the init file:
   ```powershell
   cd D:\EXPERIMENTS\SHELL
   claude --dangerously-skip-permissions papers/init_[topic].md
   ```

2. Archive the result:
   ```powershell
   cp D:\EXPERIMENTS\[SLUG]\papers\[slug]\paper.md D:\EXPERIMENTS\SHELL\archive\[slug]_run1\paper.md
   ```

3. Delete the project directory and run again:
   ```powershell
   rm -rf D:\EXPERIMENTS\[SLUG]
   claude --dangerously-skip-permissions papers/init_[topic].md
   ```

4. Compare the two papers:
   - Structural: do both have the same sections, same number of theorems, same definitions?
   - Claims: are the central claims identical or do they diverge?
   - Proofs: do both take the same proof path?
   - Figures: do both produce the same figures with the same code?

**What consistent results mean:** The pipeline is deterministic enough to trust.

**What divergent results mean:** The varying sections reveal where the Author's
(Grok-3) generation is stochastic. These sections need tighter prompting or
additional frozen spec parameters to constrain.

Run this on any new init file before producing a paper you intend to publish.
```

- [ ] **Step 2: Commit**

```bash
git add BEST_PRACTICES.md
git commit -m "docs: parallel comparison process for paper-level statistical validation"
```

---

### Task 10: Version bump and final commit

**Files:**
- Modify: `README.md` (version number)
- Modify: `prompts/04_paper_orchestrator.md` (version in drift report header)

- [ ] **Step 1: Update README.md version**

Change `**Version:** 4.0` to `**Version:** 5.0`

- [ ] **Step 2: Update drift report SHELL version**

In the drift report header template in 04_paper_orchestrator.md, change:
`SHELL Version: 4.0` to `SHELL Version: 5.0`

- [ ] **Step 3: Update run manifest SHELL version**

In the run manifest template, change:
`SHELL_VERSION: 4.0` to `SHELL_VERSION: 5.0`

- [ ] **Step 4: Final commit and push**

```bash
git add -A
git commit -m "SHELL v5.0 — plumbing fixes, structured log, cost tracking, parallel comparison"
git push
```
