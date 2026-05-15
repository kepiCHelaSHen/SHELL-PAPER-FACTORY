# SHELL — Autonomous Academic Paper Generation Framework

**Author:** James P Rice Jr.
**Version:** 6.3 (Agent Dispatch Architecture)
**Last Updated:** 2026-05-15

---

## What This Is

SHELL is an autonomous pipeline for generating rigorous, publication-ready
academic papers. It is domain-agnostic — formal theory, economics, game theory,
epidemiology, any field where formal reasoning applies.

You give it an init file with a research question and frozen spec. It scaffolds
a project, runs the paper through a four-milestone adversarial pipeline with
agent-dispatched roles, steelmans the finished paper, and iterates until the
Steelman accepts. No human intervention required.

**Results (2026-05-14):** 4 papers generated autonomously, all passed Steelman
review, independently validated by GPT-4o, Grok-3, and Gemini 2.5 at an
average score of 7.92/10 across 12 reviews. Every reviewer confirmed:
"Would I believe a competent researcher wrote this? Yes."

Based on Rice (2026), "A Deterministic Validation Loop for LLM-Generated
Scientific Code" (DOI: 10.5281/zenodo.19217024).

---

## The Five-Component Framework

| Component | Implementation | How Preserved |
|-----------|---------------|---------------|
| 1. Immutable Spec | frozen_spec.md + SHA256 | Fingerprint verified before every milestone |
| 2. Prior-Drift Detection | Peer Reviewer checks | Every draft checked against spec parameters |
| 3. Adversarial Role Separation | Agent dispatch | Each role is a separate agent with fresh context |
| 4. Statistical Validation | Figure execution | Code blocks extracted, executed, verified |
| 5. Persistent State | state_vector + logs | Files are the memory, not context |

---

## The Pipeline

Four milestones in strict sequence. No milestone opens until the previous one
is approved by the Peer Reviewer.

| Milestone | What the Author Writes | Gate |
|-----------|----------------------|------|
| M1 | Definitions Block + Introduction | Peer Reviewer ACCEPT -> Steelman (GATING) |
| M2 | Core Proof (lemmas, theorems, corollaries) | Peer Reviewer ACCEPT -> Steelman (GATING) |
| M3 | Application + Boundary Conditions | Peer Reviewer ACCEPT -> Steelman (ADVISORY) |
| M4 | Abstract + Related Work + Discussion + Conclusion | Peer Reviewer ACCEPT -> Steelman (ADVISORY) -> Editor ACCEPT |

### Roles (Agent Dispatch Model)

Each role runs as a **separate agent with a fresh context window**. The
Orchestrator passes only what that role needs. This prevents context saturation.

| Role | Prompt | What it does |
|------|--------|-------------|
| Author | 05_author.md | Writes the paper — confident, precise, no hedging |
| Peer Reviewer | 06_peer_reviewer.md | Science gate — hostile to weak reasoning |
| Steelman | 08_steelman.md | Hostile external referee — catches what peer review misses |
| Editor | 07_editor.md | Editorial gate — clarity, consistency, format (M4 only) |

---

## Quality Loop (Internal)

The quality loop runs **inside a single Claude session**. No Ctrl+C needed.
No re-scaffolding between runs. One invocation, fully autonomous.

```
Run 1: Scaffold -> M1 -> M2 -> M3 -> M4 -> Steelman
         |
         verdict: ACCEPT or MINOR_REVISION -> done
         verdict: MAJOR_REVISION -> feed steelman feedback to Run 2
         |
Run 2: M1 -> M2 -> M3 -> M4 -> Steelman (max 3 runs)
```

Outputs go in `run1/`, `run2/`, `run3/` subdirectories within one project.
Best paper copied to `best_paper.md`.

### Usage

```powershell
cd C:\PROJECTS\SHELL
.\run_quality_loop.ps1 -InitFile papers/init_[topic].md
```

---

## Consolidated Findings System

Every Steelman critique and dead end is automatically consolidated into
central cross-paper logs:

| File | Count | Purpose |
|------|-------|---------|
| STEELMAN_FINDINGS.md | 154 findings | Typed, categorized issues across all papers |
| DEAD_ENDS.md | 104 entries | Failed approaches — never repeat |

These findings are pre-loaded into init files as KNOWN_DRIFT_RISKS, enabling
papers to avoid known mistakes on Run 1. The database grows with every paper
generated — each run makes the next one better.

### Categories

**Findings:** MATH_ERROR, SPEC_MATH_MISMATCH, AUTHOR_TENDENCY, CITATION_ERROR,
ASSEMBLY_ERROR, PROOF_STRATEGY_DRIFT, FRAMING_OVERCLAIM

**Dead Ends:** proof_technique_failed, spec_impossible, author_hallucination,
citation_error, scope_disguise, terminology_error, math_error,
assumed_not_derived, framing_overclaim, assembly_error

---

## System Signature (from 12 independent reviews)

| Dimension | Average | Grade |
|-----------|---------|-------|
| Intellectual Honesty | 9.5 | A+ |
| Clarity of Writing | 9.1 | A |
| Conceptual Compression | 8.9 | A |
| Overall Coherence | 8.7 | A |
| Mathematical Rigor | 8.4 | A- |
| Literature Awareness | 8.1 | B+ |
| Policy Relevance | 7.9 | B+ |
| Publishability | 7.3 | B |
| Originality | 6.5 | B- |
| Empirical Grounding | 5.3 | C+ |

---

## Completed Papers

| Paper | Venue | Score | Time | Runs | Verdict |
|-------|-------|-------|------|------|---------|
| Replication Crisis | PNAS | 8.17 | 45 min | 1 | ACCEPT |
| Vaccine Game | J. Math Biology | 7.77 | 57 min | 1 | ACCEPT |
| Tech Lock-In | Research Policy | 7.72 | 92 min | 2 | MINOR_REV |
| Academic Publishing | Research Policy | 8.03 | 100 min | 1 | MINOR_REV |

All papers reviewed by GPT-4o, Grok-3, and Gemini 2.5 Flash.
100% "competent researcher" credibility pass rate.

---

## Directory Structure

```
C:\PROJECTS\SHELL\
├── README.md                    <- This file
├── CLAUDE.md                    <- Template north star
├── STEELMAN_FINDINGS.md         <- Cross-paper findings (154 entries)
├── DEAD_ENDS.md                 <- Cross-paper dead ends (104 entries)
├── BEST_PRACTICES.md            <- Hard-won operational rules
├── STATUS.md                    <- Current project status
├── run_quality_loop.ps1         <- Quality loop launcher
│
├── prompts/
│   ├── 00_init.md               <- Project scaffolding wizard
│   ├── 04_paper_orchestrator.md <- v5 agent dispatch orchestrator
│   ├── 05_author.md             <- Author persona
│   ├── 06_peer_reviewer.md      <- Peer reviewer persona
│   ├── 07_editor.md             <- Editor persona
│   ├── 08_steelman.md           <- Steelman persona
│   └── 09_external_review.md   <- Standardized AI review prompt
│
├── papers/
│   ├── PAPER_IDEAS.md           <- 115 formal theory paper ideas
│   ├── init_[topic].md          <- Init files for paper generation
│   └── [SLUG]_[DATE]_[SEQ]/    <- Generated papers (auto-versioned)
│       ├── best_paper.md        <- Best paper from quality loop
│       ├── frozen_spec.md       <- Locked parameters
│       ├── state_vector.md      <- Pipeline state
│       ├── innovation_log.md    <- Audit trail
│       ├── dead_ends.md         <- Failed approaches
│       ├── run1/                <- Run 1 outputs
│       │   ├── paper.md
│       │   ├── M1-M4_draft.md
│       │   ├── steelman_critique.md
│       │   └── figures/
│       ├── run2/ (if needed)
│       └── outputs/
│           ├── citation_verification.md
│           ├── drift_report.md
│           └── run_manifest.md
│
├── src/
│   ├── consolidate.py           <- Findings extraction + consolidation
│   ├── verify_citations.py      <- CrossRef citation checker
│   ├── regression_tests.py      <- Cross-run regression detection
│   ├── epistemic_metrics.py     <- Quality measurement
│   ├── publish.py               <- Zenodo uploader
│   └── paper_to_thread.py       <- Convert paper to X thread
│
├── logs/                        <- Quality loop logs
└── docs/
    ├── LESSONS_LEARNED.md       <- Operational lessons
    └── SHELL_V6_ROADMAP.md      <- Design principles
```

---

## How to Create a New Paper

### 1. Write the init file

Use `papers/init_replication_crisis.md` as the template. Every init file needs:
- Execution directive (lines 2-5)
- FROZEN_SPEC_PARAMETERS with drift risks
- MILESTONES (M1-M4)
- ORACLE (validation criteria)
- KNOWN_DRIFT_RISKS (paper-specific)
- CROSS-PAPER FINDINGS (from STEELMAN_FINDINGS.md)
- SETUP SEQUENCE with auto-versioning
- HAND OFF section (triggers the pipeline)

### 2. Run it

```powershell
cd C:\PROJECTS\SHELL
.\run_quality_loop.ps1 -InitFile papers/init_[topic].md
```

### 3. Review

Send `best_paper.md` to GPT, Grok, and Gemini using the standardized
review prompt at `prompts/09_external_review.md`.

---

## Sister Project: ASSAY

ASSAY (at C:\PROJECTS\ASSAY) is the companion analytics engine. Where SHELL
generates theory, ASSAY generates verified empirical evidence from data.
ASSAY outputs feed into SHELL papers as citable results, addressing the
empirical grounding gap (currently 5.3/10 average).

---

## Future: THESIS + ASSAY

SHELL will be renamed to **THESIS** when ready for product launch.
"THESIS generates the theory, ASSAY tests the evidence."
