# CHAIN PROMPT — SHELL MASTER DOCUMENT
# THIS FILE WINS ALL CONFLICTS WITH ANY OTHER FILE
# Pass this file in full at the start of every session.
# Update whenever a design decision is locked in.
# Last Updated: 2026-03-30

================================================================================
PURPOSE
================================================================================

This is the living master document for any experiment built on SHELL.
When you clone SHELL for a new experiment, customize every section below.
This file is the source of truth. If it conflicts with any other file, this wins.

================================================================================
EXPERIMENT IDENTITY
================================================================================

Name:           [EXPERIMENT NAME]
Full name:      [Full experiment name]
Location:       D:\EXPERIMENTS\[NAME]\
Status:         [CURRENT STATUS]
Target journal: [TARGET JOURNAL]
News hook:      [One sentence: why does this matter if LLMs get it wrong?]

Purpose:
  [One paragraph describing what this experiment tests and why it matters]

================================================================================
CONFIRMED DESIGN DECISIONS
================================================================================

[All locked-in decisions go here. Add new ones as they are confirmed.
Never remove a decision — if it changes, mark it SUPERSEDED and add the new one.]

--- FROZEN SPEC ---
  Spec file:    spec/frozen_spec.md
  Locked:       [DATE]
  Parameters:   [list]
  Oracle:       [how outputs are validated]

--- LOOP ARCHITECTURE (MULTI-MODEL TRIANGULATION) ---
  Three different LLMs prevent any single model's prior from dominating.
  See: Rice (2026) DOI: 10.5281/zenodo.19217024

  Experiment pipeline:
    Builder:      Grok-3 (xAI) | temperature 0.7 | generation
    Critic:       GPT-4o (OpenAI) | temperature 0.2 | validation
    Reviewer:     Claude | orchestrator + quality

  Paper pipeline:
    Author:       Grok-3 (xAI) | temperature 0.7 | generation
    Peer Reviewer: GPT-4o (OpenAI) | temperature 0.2 | validation
    Editor:       Claude | orchestrator + editorial

  Default mode: VALIDATION
  Seeds:        3 (development) | 30 (convergence)
  Sigma gate:   CV < 15%

--- MILESTONES ---
  M1: [description]
  M2: [description]
  M3: [description]
  M4: [integration and statistical validation]

--- SACRED FILES ---
  See SACRED_FILES.md. These files are never modified after lock.

================================================================================
FROZEN COEFFICIENTS
================================================================================

[Copy the frozen spec table here for quick reference]

| Parameter | Value | Unit | Source |
|-----------|-------|------|--------|
| [param]   | [val] | [u]  | [src]  |

================================================================================
ARCHITECTURE RULES
================================================================================

[Experiment-specific architecture rules that the Reviewer enforces.
Example from SIMSIV:
- Pure library: no UI, no print statements. All IO at the edges.
- All randomness via seeded generator. Same seed = identical results.
- Structured logging only. No bare print().
- Max 500 lines per file.]

================================================================================
KNOWN DEAD ENDS
================================================================================

[Summary of major dead ends. Full list in state/dead_ends.md]

================================================================================
CHANGE LOG
================================================================================

[DATE] | [WHAT CHANGED] | [WHY]
