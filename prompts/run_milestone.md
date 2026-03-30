# RUN MILESTONE — Single milestone runner
# Called once per milestone by run_pipeline.ps1
# Reads state vector, runs ONE milestone, updates state, exits cleanly.
# Never runs more than one milestone per invocation.

---

## YOUR JOB

Read the state vector. Identify the next pending milestone. Run it. Update
the state vector. Exit. Do not run the next milestone. One milestone per call.

---

## ON STARTUP — READ THESE IN ORDER

1. papers/[SLUG]/state_vector.md — identifies current milestone and status
1b. Verify frozen spec integrity:
    If state vector contains SPEC_FINGERPRINT:
      Run: python -c "import hashlib; print(hashlib.sha256(open('spec/frozen_spec.md','rb').read()).hexdigest())"
      Compare to stored fingerprint. Mismatch → HALT immediately.
      Write: "SPEC INTEGRITY FAILURE — frozen_spec.md modified after lock."
2. spec/frozen_spec.md — frozen parameters (pass to Peer Reviewer)
3. results/raw/[SLUG]_M1.md — if exists, locked M1 content
4. results/raw/[SLUG]_M2.md — if exists, locked M2 content
5. results/raw/[SLUG]_M3.md — if exists, locked M3 content

The state vector tells you exactly what to do:

  STATUS: M1 LOCKED, MILESTONE: M2 → Run M2
  STATUS: M2 LOCKED, MILESTONE: M3 → Run M3
  STATUS: M3 LOCKED, MILESTONE: M4 → Run M4
  STATUS: M4 LOCKED → Paper complete. Print completion message. Exit.
  STATUS: INIT, MILESTONE: M1 → Run M1

---

## RESUME LOGIC

If a draft file exists for the current milestone (e.g. M2_draft.md) but the
milestone is NOT locked in the state vector, the Author already wrote the draft
but the Peer Reviewer did not finish. DO NOT ask the Author to rewrite.
Instead, go directly to the Peer Reviewer with the existing draft.

---

## RUNNING A MILESTONE

Follow the milestone spec in prompts/04_paper_orchestrator.md exactly.

All roles are handled by you (Claude) with distinct personas:
  Author → read prompts/05_author.md, adopt Author persona, write
  Peer Reviewer → read prompts/06_peer_reviewer.md, adopt Peer Reviewer persona, review
  Editor → read prompts/07_editor.md, adopt Editor persona, edit

No external API keys needed for the paper pipeline.

Author call → Peer Reviewer call → loop until ACCEPT (max 5) → lock milestone.

On ACCEPT:
  1. Write locked content to results/raw/[SLUG]_M[N].md
  2. Update papers/[SLUG]/state_vector.md:
       STATUS: M[N] LOCKED
       MILESTONE: M[N+1]
       TURN: [increment]
       Add row to History table
  3. Update state/innovation_log.md — append entry
  4. git add -A && git commit -m "Turn [N] | M[milestone] | LOCKED"
  5. Print: ✅ M[N] LOCKED — run_pipeline.ps1 will now call M[N+1]
  6. Exit.

On max loops exceeded (5 Author/Reviewer loops without ACCEPT):
  1. Write STATUS: HALTED | M[N] | loop limit to state vector
  2. Write halt report to outputs/halt_report.md
  3. git add -A && git commit -m "HALTED | M[N] | loop limit"
  4. Print: ❌ HALTED on M[N] — check outputs/halt_report.md
  5. Exit.

---

## MILESTONE DEFINITIONS

M1: Definitions Block + Introduction
M2: Core Proof (lemmas, theorems, corollaries)
M3: Application + Boundary Conditions (includes sensitivity analysis,
    competing models, natural enemy, assumption violations, edge cases)
M4: Abstract (last) + Related Work + Discussion + Conclusion + References
    → after Peer Reviewer ACCEPT, run Editor pass
    → Editor ACCEPT → run Figure Generation (extract, execute, verify)
    → write papers/[SLUG]/paper.md + results/final/[SLUG]_final.md
    → Update STATUS: AWAITING_REVIEW

---

## INPUTS PASSED BY run_pipeline.ps1

SLUG: [project slug]

## DRIFT_RISKS — EXTRACTED FROM FROZEN SPEC

Do NOT rely on run_pipeline.ps1 to pass drift risks. Read them directly
from spec/frozen_spec.md. The frozen spec contains a "KNOWN PRIOR DRIFT RISK"
section — extract all entries and pass them to the Author on every call.

If spec/frozen_spec.md has no drift risk section, log:
  "WARNING: No drift risks found in frozen spec. Author will generate without
   drift guidance."
