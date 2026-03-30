# BEST PRACTICES
# Distilled from hard-won experience. Updated when something breaks.
# Read this before starting any new experiment or paper.
# Author: James P Rice Jr.

---

## Loop Integrity

- **Lock the spec before starting.** No exceptions. If you need to change the spec
  mid-loop, halt, document, version the spec file, restart from Turn 0.
- **Never edit previous innovation_log or dead_ends entries.** Append only.
  The audit trail is the whole point.
- **State vector is ground truth.** If your memory of where you are disagrees with
  state_vector.md, the file wins.
- **Back up state vector before any reversion.** Write to outputs/state_vector_backup.md
  first. Then revert. Never revert blind.

---

## Prompting

- **One section at a time.** Never ask the Author to write the whole paper at once.
  Section-by-section consensus produces better science and is easier to debug.
- **Give the Author only what it needs.** Pass: the section prompt, the locked
  prior sections (for continuity), the relevant data. Nothing else. Noise causes drift.
- **Exact prompt logging is non-negotiable.** Log every prompt in turn_prompts_log.md
  before sending it. If you can't reproduce a result, the experiment didn't happen.
- **The Peer Reviewer must see the data, not just the claims.** Pass raw results
  alongside the draft section. If Reviewer only sees prose, it can't catch overclaiming.

---

## Figures

- **SVG source, always.** Never rasterize your working file. SVG → PNG/PDF at export.
- **Lock the color palette in figure_spec.md before generating any figures.**
  Changing colors mid-paper means regenerating everything.
- **Caption format:** "**Figure N.** [What it shows]. [What to conclude from it]."
  Two sentences. Mandatory. The Editor gate enforces this.
- **Figures from recent sieve work are the gold standard.** When in doubt, match those.
- **Figure Agent runs after Results section is locked.** Not before. Figures must
  match committed claims, not draft claims.

---

## Zenodo / Publication

- **You read the paper first.** Every time. No automated Zenodo upload.
- **Sandbox before production.** Test the Zenodo API call against the sandbox endpoint.
  Confirm the bundle looks right. Then flip to production.
- **DOI goes in the paper footer.** After you get the DOI back, add it, re-render,
  final upload. The published PDF and the Zenodo record must match.
- **Bundle contents:** paper.pdf + figures/final/* + data/ (if public) + README.md.
  No scratch files, no state vectors, no prompt logs in the upload.

---

## Drift Prevention

- **Check frozen_spec.md at the start of every session.** Not optional.
  LLM prior is the enemy. The spec is the antidote.
- **Flag anomalies immediately.** If a metric moves the wrong direction, set FLAG:
  ANOMALY in state_vector.md before doing anything else. Do not paper over it.
- **Dead ends are permanent.** Once something is in dead_ends.md it is never retried,
  even if it seems like a good idea again. If you think the dead end was wrong,
  write a new entry explaining why, get Peer Reviewer sign-off, then retry.

---

## Context Resets

- **Assume every new session is a cold start.** Read in this order:
  1. CLAUDE.md (north star, 2 minutes)
  2. state/state_vector.md (where you are)
  3. state/dead_ends.md (what not to do)
  4. prompts/00_orchestrator.md (how to run the loop)
- **Do not rely on chat history.** It will be gone. Everything important lives in files.

---

## Proof-Strategy Drift (learned 2026-03-30)

For papers where the intellectual contribution lives in the proof strategy
(not just the structural scaffolding), the frozen spec and drift risks must
constrain HOW the proof is constructed — not just WHAT is proven.

**The problem:** The pipeline's structural rules (boundary conditions, sensitivity
tables, competing models) guarantee good scaffolding. But for pure formal theory
papers, the quality lives in formalization choices and proof strategies that the
pipeline cannot infer. Without explicit guidance, the Author may choose a trivially
simple formalization that produces a correct but uninteresting result.

**Example:** Common Knowledge paper v2 used a dual proof strategy (partition-meet
+ induction, 17 steps) and a general Sacred File formalization (non-trivial
partition). The v4 pipeline run produced a correct but near-trivial result
(constant reading function, trivial partition). Both are technically correct.
Only one is publishable.

**The fix:** For proof-strategy-dependent papers, add PROOF STRATEGY and
FORMALIZATION entries to KNOWN_DRIFT_RISKS in the init file:

```
- PROOF STRATEGY: The proof of X must use technique Y (martingale convergence,
  induction on knowledge depth, coalition stability), not the simpler technique Z.
- FORMALIZATION: The model must use the general version (non-trivial partition,
  non-constant function), not the special case that trivializes the result.
```

**Which papers need this?** Papers where:
- The core result is a proof technique, not a calculation
- There are multiple valid formalizations of different generality
- A simpler formalization would make the result trivially obvious
- The proof structure IS the contribution (not just the theorem statement)

Papers that are primarily analytical derivations (survival analysis, NE calculations,
closed-form thresholds) do NOT need proof-strategy drift risks. The pipeline
handles these well on its own.

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
