# SHELL (THESIS) — Autonomous Academic Paper Generation Framework
# Read this at the start of every session. Two minutes or less.

## What We Are Building
An autonomous pipeline that generates rigorous, publication-ready academic papers
through adversarial multi-agent validation, with empirical evidence from the ASSAY
companion analytics engine.

## Key Files — READ IN THIS ORDER
1. `LEARNINGS.md` — **READ THIS FIRST.** Accumulated operational knowledge from
   every mistake and success. Covers init quality, Steelman classification, agent
   dispatch, ASSAY integration, cost management. Ignoring this file costs money.
2. `STATUS.md` — Current project state, completed papers, what's next.
3. `STEELMAN_FINDINGS.md` — 154 cross-paper findings. Pre-load relevant ones into inits.
4. `DEAD_ENDS.md` — 104 failed approaches. Never repeat.
5. `BEST_PRACTICES.md` — Operational rules.
6. `prompts/04_paper_orchestrator.md` — v5 agent dispatch orchestrator.
7. `prompts/09_external_review.md` — Standardized AI review prompt.

## Critical Rules
- **LEARNINGS.md is mandatory reading.** It exists because mistakes cost $25-75 each.
- Every init file must point to SPECIFIC ASSAY integration block paths. No "if available."
- ASSAY data must be CALIBRATED against the model, not just cited as context.
- Sanity check ALL ASSAY values against model domain constraints before writing inits.
- Steelman STRUCTURAL = mathematical errors ONLY. Everything else is FRAMING.
- Never suggest manual workarounds. Fix the system.
- Never hack around broken components. Fix the root cause.

## ASSAY Integration
- ASSAY reports live at C:\PROJECTS\ASSAY\reports\[SLUG]\integration_block.yaml
- Each integration block has computed values, CIs, forbidden_interpretations, and figure paths.
- The Author must USE these values to test model predictions, not just mention them.
- Negative ASSAY results (model doesn't fit data) make papers MORE credible.

## Architecture
- v5 Agent Dispatch: Author/Reviewer/Steelman/Editor as separate agents, fresh contexts
- Internal quality loop: max 3 runs, stops on ACCEPT or MINOR_REVISION
- Consolidated findings ratchet: every paper makes the next one better
- Papers auto-version to papers/[SLUG]_[DATE]_[SEQ]/run1/, run2/, run3/

## Current Status
See STATUS.md.

## Do Not Touch
See SACRED_FILES.md.
