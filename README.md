# SHELL — Autonomous Academic Paper Generation Framework

**Author:** James P Rice Jr.
**Version:** 6.1
**Last Updated:** 2026-05-12

---

## What This Is

SHELL is a reusable scaffold for generating rigorous, publication-ready academic
papers using a milestone-gated, adversarial multi-agent pipeline. It is domain-agnostic
— formal theory, physics, economics, computational science, any STEM field where
formal reasoning applies.

You give the CLI a problem statement. It scaffolds a new project, locks a frozen spec,
and runs the paper through a four-milestone pipeline. The quality loop then steelmans
the finished paper, injects revision instructions, and regenerates until the Steelman
accepts or max runs are reached.

Based on Rice (2026), "A Deterministic Validation Loop for LLM-Generated Scientific
Code" (DOI: 10.5281/zenodo.19217024).

---

## The Pipeline

Every paper runs through four milestones in strict sequence. No milestone opens
until the previous one is approved by the Peer Reviewer.

| Milestone | What the Author Writes | Gate |
|-----------|----------------------|------|
| M1 | Definitions Block + Introduction | Peer Reviewer ACCEPT → Steelman (GATING) |
| M2 | Core Proof (lemmas, theorems, corollaries) | Peer Reviewer ACCEPT → Steelman (GATING) |
| M3 | Application + Boundary Conditions | Peer Reviewer ACCEPT → Steelman (ADVISORY) |
| M4 | Abstract + Related Work + Discussion + Conclusion + References | Peer Reviewer ACCEPT → Steelman (ADVISORY) → Editor ACCEPT |

### Roles (all Claude, distinct personas)

| Role | Prompt | What it does |
|------|--------|-------------|
| Author | 05_author.md | Writes the paper — confident, precise, no hedging |
| Peer Reviewer | 06_peer_reviewer.md | Science gate — 80% rejection rate, hostile to weak reasoning |
| Steelman | 08_steelman.md | Hostile external referee — catches what peer review misses |
| Editor | 07_editor.md | Editorial gate — clarity, consistency, format (M4 only) |

### Steelman Modes

| Mode | When | Effect |
|------|------|--------|
| GATING | M1, M2 | Can block milestone with STRUCTURAL_FLAG or NOVELTY_KILL |
| ADVISORY | M3, M4 | Writes critique, milestone locks regardless |
| V2_DRIFT | Post-pipeline | Generates drift risks for next version's init file |

---

## Quality Loop

The quality loop (`run_quality_loop.ps1`) automates the generate-review-revise cycle:

```
Run 1: Generate paper (M1→M2→M3→M4)
         ↓ Ctrl+C when done
Full-paper Steelman: reads paper.md end-to-end as hostile referee
         ↓ verdict: ACCEPT / MAJOR_REVISION / REJECT
If not ACCEPT: extract revision instructions → patch init file
         ↓
Run 2: Generate with revision constraints baked in
         ↓ Ctrl+C when done
Steelman again → repeat until ACCEPT or max runs
```

### Usage

```powershell
cd C:\PROJECTS\SHELL
.\run_quality_loop.ps1 -InitFile papers/init_[topic].md -MaxRuns 3
```

When Claude shows the `❯` prompt after paper completion, press **Ctrl+C twice** to
continue the loop. The Steelman runs automatically, then the next paper generates.

### Logs

All output logged to `logs/quality_loop_[timestamp].log`. Steelman critiques saved
to each project's `steelman_full_paper_critique.md`.

---

## Directory Structure

### SHELL root (the framework)

```
C:\PROJECTS\SHELL\
├── README.md                    ← This file
├── CLAUDE.md                    ← Template north star for new projects
├── CHAIN_PROMPT.md              ← Template master doc
├── BEST_PRACTICES.md            ← Hard-won lessons
├── SACRED_FILES.md              ← Template for locked files list
├── STATUS.md                    ← Template for current status
├── api.env                      ← API keys (never committed)
├── run_quality_loop.ps1         ← The quality loop (PowerShell)
├── run_dvl_papers.ps1           ← Batch runner for all papers
│
├── prompts/
│   ├── 00_init.md               ← Project scaffolding wizard
│   ├── 00_orchestrator.md       ← Multi-model experiment loop
│   ├── 04_paper_orchestrator.md ← Paper pipeline (Claude-only)
│   ├── 05_author.md             ← Author persona
│   ├── 06_peer_reviewer.md      ← Peer reviewer persona
│   ├── 07_editor.md             ← Editor persona
│   ├── 08_steelman.md           ← Steelman persona (hostile referee)
│   └── run_milestone.md         ← Single milestone executor
│
├── papers/
│   ├── init_[topic].md          ← Pre-filled paper init files
│   └── [SLUG]_[DATE]_[SEQ]/    ← Auto-versioned generated papers
│
├── src/
│   ├── quality_loop.py          ← Python quality loop (deprecated — use .ps1)
│   ├── regression_tests.py      ← Claim extraction + cross-run regression detection
│   ├── epistemic_metrics.py     ← Read-only measurement tool
│   ├── publish.py               ← Zenodo uploader
│   ├── verify_citations.py      ← CrossRef citation checker
│   ├── paper_to_thread.py       ← Convert paper to X thread
│   └── triangulation_experiment.py ← Multi-model consensus test
│
├── logs/                        ← Quality loop logs
├── archive/                     ← Old paper versions
└── docs/
    ├── SHELL_V6_ROADMAP.md      ← 10 design principles + implementation plan
    ├── LESSONS_LEARNED.md       ← What worked, what didn't, hard rules
    └── FEEDBACK_2026-05-11_JAMES_RICE.md ← Raw design feedback
```

### Generated paper project (flattened structure)

```
papers/[SLUG]_[DATE]_[SEQ]/
├── paper.md                     ← Final paper
├── frozen_spec.md               ← Locked parameters (at root, not in spec/)
├── state_vector.md              ← Pipeline state (at root, not in state/)
├── innovation_log.md            ← Append-only audit trail
├── dead_ends.md                 ← Failed approaches
├── M1_draft.md ... M4_draft.md  ← Milestone drafts
├── steelman_full_paper_critique.md ← Quality loop steelman output
├── regression_fixtures.json     ← Extracted claims for cross-run comparison
├── figures/                     ← Python scripts + rendered PDFs
├── results/raw/                 ← Locked milestone outputs
├── results/final/               ← Final paper copy
├── outputs/                     ← Citation verification, drift report, manifest
├── prompts/                     ← Copied from SHELL
└── .git/                        ← Per-project git history
```

---

## How to Create a New Paper

### Writing the init file

Every init file MUST have:

1. **Execution directive** (lines 2-5):
   ```
   # EXECUTE IMMEDIATELY. Do not summarize, analyze, or ask questions.
   # Read the INPUTS below, then execute the SETUP SEQUENCE step by step.
   # Load prompts/00_init.md for the setup procedure, then run it with these inputs.
   # This is not a document to review — it is a set of instructions to follow NOW.
   ```

2. **HAND OFF section** (at the bottom, after KNOWN_DRIFT_RISKS):
   ```
   ## HAND OFF — EXECUTE PAPER PIPELINE
   DO NOT STOP AFTER SCAFFOLDING. DO NOT ASK FOR PERMISSION.
   [explicit pipeline trigger — see docs/LESSONS_LEARNED.md for template]
   ```

Without BOTH, Claude will either summarize the file or scaffold then stop.

### Running a single paper

```powershell
cd C:\PROJECTS\SHELL
claude --dangerously-skip-permissions papers/init_[topic].md
```

### Running the quality loop

```powershell
.\run_quality_loop.ps1 -InitFile papers/init_[topic].md -MaxRuns 3
```

### Measuring quality across runs

```powershell
python src/epistemic_metrics.py --compare papers/[SLUG]_*
```

---

## Technical Notes

### Claude CLI on Windows

Claude CLI (npm/Ink-based) kills its parent process on exit. All scripts must use
`cmd /c claude.cmd` to isolate the exit. See `docs/LESSONS_LEARNED.md` for details.

### Auto-versioning

Projects scaffold to `papers/[SLUG]_[YYYY-MM-DD]_[SEQ]/` where SEQ auto-increments.
Multiple runs of the same paper create separate directories — nothing is overwritten.

### API Keys

Stored as Windows environment variables (`XAI_API_KEY`, `OPENAI_API_KEY`).
Python scripts check `os.environ` first, fall back to `api.env`.

---

## Current Papers

### Bayesian Epistemology Trilogy

| # | Paper | Init File | Status |
|---|-------|-----------|--------|
| 1 | Conspiracy Beliefs as Bayesian Updating | `init_conspiracy_bayes.md` | 3 runs, Steelman ACCEPT |
| 2 | Echo Chambers (Heterogeneous Information) | `init_echo_chambers_v2_heterogeneous.md` | In progress |
| 3 | Misinformation Persistence as Equilibrium | `init_misinformation.md` | Not started (depends on 1+2) |

### Other Papers

See `papers/PAPER_IDEAS.md` for the full catalog of 115 formal theory paper ideas.
