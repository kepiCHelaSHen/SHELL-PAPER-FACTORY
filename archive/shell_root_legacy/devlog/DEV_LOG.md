# DEVELOPMENT LOG
# Human-written. Append-only. One entry per working session.
# This is the scratchpad for decisions, observations, and direction changes that
# didn't fit neatly into the structured logs. Think of it as the lab notebook.

---
# ENTRY FORMAT

## [DATE] — Session [N]
**Status at start:** [one line]
**What I did:**
- [bullet]
- [bullet]
**What I decided and why:**
[prose — this is where you record judgment calls]
**Blockers / open questions:**
- [item]
**Status at end:** [one line]

---

## [DATE] — Session 1
**Status at start:** Scaffolding complete. No experiment loaded yet.
**What I did:**
- Built SHELL directory structure
- Wrote all prompt files, spec templates, state files
**What I decided and why:**
Paper factory design chosen — builder/critic/reviewer loop adapted for section-by-section
consensus writing. Manual review gate before Zenodo. Output format: clean Markdown
for review in VS Code / Obsidian.
**Blockers / open questions:**
- paper_spec.md not yet written — need to decide target structure before prompts can be finalized
- figure_spec.md not yet written — need to port standards from recent sieve figures
**Status at end:** Scaffold done. Ready to initialize first paper experiment.
