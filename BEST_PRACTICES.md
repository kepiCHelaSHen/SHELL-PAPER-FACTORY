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
