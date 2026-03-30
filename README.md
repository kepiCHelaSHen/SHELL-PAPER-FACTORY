# SHELL — Autonomous Academic Paper Generation Framework

**Author:** James P Rice Jr.
**Version:** 5.0
**Last Updated:** 2026-03-30

---

## What This Is

SHELL is a reusable scaffold for generating rigorous, publication-ready academic
papers using a milestone-gated, adversarial multi-agent pipeline. It is domain-agnostic
— formal theory, physics, economics, computational science, any STEM field where
formal reasoning applies.

You give the CLI a problem statement. It scaffolds a new project, locks a frozen spec,
and runs the paper through a four-milestone pipeline overnight. You wake up with a
paper in `papers/[slug]/paper.md`. You read it. When approved, you upload to Zenodo.

---

## Two Pipelines, Two Strategies

SHELL has two pipelines with different model strategies:

**Paper Pipeline** (04_paper_orchestrator.md) — Claude-only. All three roles
(Author, Peer Reviewer, Editor) are Claude with distinct personas and checklists.
Adversarial tension comes from the prompts. Writing quality and proof rigor are
the priority. No external API keys needed.

| Role | Model | Persona |
|------|-------|---------|
| Author | Claude | Senior researcher — confident, precise, no hedging |
| Peer Reviewer | Claude | Associate editor — 80% rejection rate, hostile to weak reasoning |
| Editor | Claude | Copy editor — 15 years at academic press, no patience for filler |

**Experiment Pipeline** (00_orchestrator.md) — Multi-model triangulation.
Three different LLMs prevent any single model's training prior from dominating.
This is the core mechanism from Rice (2026) for detecting specification drift.
See: https://zenodo.org/records/19217024

| Role | Model | Purpose |
|------|-------|---------|
| Builder | Grok-3 (xAI), temp 0.7 | Generates from its own prior |
| Critic | GPT-4o (OpenAI), temp 0.2 | Validates against frozen spec with a different prior |
| Reviewer | Claude | Third prior for quality and orchestration |

---

## The Pipeline

Every paper runs through four milestones in strict sequence. No milestone opens
until the previous one is approved by the Peer Reviewer.

| Milestone | What the Author Writes | Gate |
|-----------|----------------------|------|
| M1 | Definitions Block + Introduction | Peer Reviewer ACCEPT |
| M2 | Core Proof (lemmas, theorems, corollaries) | Peer Reviewer ACCEPT |
| M3 | Application + Boundary Conditions | Peer Reviewer ACCEPT |
| M4 | Abstract + Related Work + Discussion + Conclusion + References | Peer Reviewer ACCEPT → Editor ACCEPT |

The Abstract is written last, after all sections are locked.

---

## Quality Standards

### Author Rules (enforced by Peer Reviewer and Editor)

Every paper produced by SHELL must satisfy:

- **Formalism first** — Definitions Block before Introduction, before Abstract
- **Lean-ready proofs** — every hypothesis explicit, every step justified, no implicit assumptions
- **Literature gap formula** — every major prior work positioned as: "[X] proposed [Y] to solve [Z], but [Y] fails under [W]. We introduce [A]."
- **Adversarial stress-test** — Boundary Conditions section that actively tries to break the theory
- **Sensitivity analysis** — every primary parameter varied by order of magnitude; conclusion must hold or the scope must be restricted
- **Competing models** — every alternative framework explicitly rejected with a formal reason
- **Figure code output** — every figure reference includes Python/matplotlib code or exact data coordinates
- **Symbolic consistency** — every symbol defined in the Definitions Block, used consistently throughout
- **No redundant restatements** — every restatement of the core result must add a new logical layer; rephrasing without new information is cut
- **Tiered definitions** — standard textbook definitions get abbreviated treatment; novel objects get full formal rigor with visually distinct weight
- **Contextual anchors** — any constant, threshold, or empirical value cited in a Definition must have a citation or justification at first use, not later

### Peer Reviewer Checks (GPT-4o, temp 0.2)

The Peer Reviewer operates as an associate editor with an 80% rejection rate.
No benefit of the doubt. Key enforcement points:

- **Frozen spec compliance** — exact match required, no "close enough"
- **Symbolic consistency with decorated forms** — hat notation, subscript variants, and decorated symbols are treated as distinct; λ̂\_ML is not "obviously" λ and the relationship must be formally defined
- **Claims vs. support** — every claim traceable to data or a proven theorem
- **Overclaiming and underclaiming** — both flagged; weak claims on strong proofs are as problematic as strong claims on weak proofs
- **Natural enemy identification** — strongest opposing result must be named and precisely addressed
- **Figure code mandatory** — references without accompanying code or data are rejected

### Editor Checks (Claude)

The Editor operates as a senior copy editor with no patience for unclear prose.
Science is already approved; editorial quality is the gate:

- **Definition hierarchy** — novel formal objects must have stronger visual weight than standard inherited definitions; visually indistinguishable treatment is flagged
- **Tone transitions** — register shifts between sections (formal→adversarial, technical→interpretive) require bridge sentences; surprise tone changes are flagged
- **Symbol consistency** — full paper scan against Definitions Block symbol table
- **Clarity** — filler phrases ("It is worth noting," "Interestingly") cut without mercy
- **Abstract standalone** — must communicate problem, method, result, implication without any undefined terms

---

## Directory Structure

```
[PROJECT_NAME]/
│
├── README.md
├── CHAIN_PROMPT.md              ← Master doc. Wins all conflicts.
├── CLAUDE.md                    ← North star. Read every session.
├── STATUS.md                    ← Current state in plain English.
├── SACRED_FILES.md              ← Files never modified after lock.
├── BEST_PRACTICES.md            ← Project-specific rules.
├── api.env                      ← API keys. Never commit.
├── .gitignore
│
├── prompts/
│   ├── 04_paper_orchestrator.md ← The pipeline. Run this with Claude CLI.
│   ├── 05_author.md             ← Writes the paper, milestone by milestone.
│   ├── 06_peer_reviewer.md      ← Science gate. ACCEPT or REJECT.
│   ├── 07_editor.md             ← Editorial gate. Clarity, consistency, format.
│   └── turn_prompts_log.md      ← Every exact prompt logged (auto-populated).
│
├── spec/
│   └── frozen_spec.md           ← Locked parameters. Never modify after lock.
│
├── state/
│   ├── state_vector.md          ← Current loop state. Save game.
│   ├── innovation_log.md        ← Append-only audit trail.
│   └── dead_ends.md             ← Failed approaches. Do not repeat.
│
├── outputs/
│   ├── state_vector_backup.md   ← Pre-operation snapshot.
│   └── options.md               ← Candidate approaches not yet committed.
│
├── results/
│   ├── raw/                     ← Per-milestone locked outputs (M1, M2, M3, M4)
│   ├── validated/               ← Peer Reviewer approved
│   └── final/                   ← Final paper copy
│
├── papers/
│   ├── init_[topic].md          ← Pre-filled paper init files
│   └── [slug]/
│       ├── M1_draft.md          ← Author output per milestone
│       ├── M2_draft.md
│       ├── M3_draft.md
│       ├── M4_draft.md
│       ├── paper.md             ← FINAL — read this before uploading
│       ├── figures/             ← Generated figure code and exports
│       └── state_vector.md      ← Paper pipeline state
│
├── src/
│   └── [experiment code if needed]
│
└── devlog/
    └── DEV_LOG.md               ← Session-by-session human log
```

---

## How to Start a New Paper

**Step 1** — Write a pre-filled init file in SHELL/papers/:

```
papers/init_[topic].md
```

Use `prompts/00_init.md` as the template. Fill in: PROJECT_NAME, SLUG, PROBLEM,
FROZEN_SPEC_PARAMETERS, MILESTONES, ORACLE, KNOWN_DRIFT_RISKS.

**Step 2** — Run the CLI:

```powershell
cd D:\EXPERIMENTS\SHELL
claude --dangerously-skip-permissions papers/init_[topic].md
```

The CLI will:
1. Create `D:\EXPERIMENTS\[SLUG]\` with full directory structure
2. Write all required files (README, CHAIN_PROMPT, SACRED_FILES, BEST_PRACTICES, devlog, etc.)
3. Lock the frozen spec
4. Initialize git
5. Run the four-milestone paper pipeline
6. Stop at `papers/[slug]/paper.md` — AWAITING REVIEW

**Step 3** — Read the paper in VS Code or Obsidian. When approved, upload to Zenodo manually.

---

## Halt Conditions

The pipeline halts and reports if:
- Any milestone Author loop exceeds 5 turns without Peer Reviewer ACCEPT
- Peer Reviewer identifies a structurally unfixable flaw (false central claim, etc.)
- A STOP file is placed in the project root

On halt: full report written to `outputs/halt_report.md`. Git commit made.

---

## Archive

`archive/` contains before/after paper comparisons from shell upgrade sessions.
Use these to verify that prompt changes produce measurable quality improvements.

---

## Citation

Rice, J. P. Jr. (2026). A Deterministic Validation Loop for LLM-Generated
Scientific Code: Framework, Implementation, and Empirical Validation.
Zenodo preprint. DOI: 10.5281/zenodo.19217024
https://zenodo.org/records/19217024
