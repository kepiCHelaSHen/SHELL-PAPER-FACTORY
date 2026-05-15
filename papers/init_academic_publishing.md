# INIT — GAME-THEORETIC MODEL OF ACADEMIC PUBLISHING
# EXECUTE IMMEDIATELY. Do not summarize, analyze, or ask questions.
# Read the INPUTS below, then execute the SETUP SEQUENCE step by step.
# Load prompts/00_init.md for the setup procedure, then run it with these inputs.
# This is not a document to review — it is a set of instructions to follow NOW.

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: The Publication Game: A Game-Theoretic Model of Journal Submission, Review, and the Efficiency of Peer Review
SLUG: ACADEMIC_PUBLISHING_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: Research Policy
PIPELINE: PAPER

PROBLEM:
Models academic publishing as a three-player game between authors (who choose
where to submit), journals (who set acceptance standards), and reviewers (who
exert costly effort). Derives the Nash equilibrium submission strategy: authors
submit to the highest-prestige journal whose acceptance probability exceeds a
threshold determined by the cost of rejection (revision time, delay). Proves
that this equilibrium produces systematic inefficiency: papers are submitted
to journals above their quality level, leading to predictable rejection
cascades. Derives the expected number of submissions before acceptance as a
function of paper quality and journal prestige distribution. Proves that the
"top-down submission" norm (always start at the best journal) is individually
rational but socially wasteful, and derives the efficiency loss. Characterizes
the conditions under which desk rejection improves system efficiency.
The central contribution is the rejection cascade theorem: the expected number
of submissions grows logarithmically in the number of journals for papers in
the middle of the quality distribution, and the resulting delay constitutes a
quantifiable efficiency loss.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Paper quality (q)
VALUE: q in [0, 1], drawn from distribution G(q)
UNIT: dimensionless (normalized quality)
TOLERANCE: parametric — key cases: uniform, beta distributions
SOURCE: Novel formalization
NOTES: Quality is fixed and known to the author. Reviewers observe a noisy
       signal of quality. The model is about submission strategy, not about
       determining quality.
DRIFT_RISK: MEDIUM — Author may make quality endogenous (revision after
             rejection). Keep it fixed for the base model.

PARAMETER: Journal prestige / acceptance threshold (t_j)
VALUE: Journal j accepts papers with q >= t_j. Ordered: t_1 > t_2 > ... > t_n.
UNIT: dimensionless
TOLERANCE: parametric
SOURCE: Novel formalization building on Ellison 2002
NOTES: n journals with decreasing acceptance thresholds. Each journal accepts
       papers above its threshold. Noisy review adds uncertainty.
DRIFT_RISK: LOW — standard modeling choice for journal hierarchies

PARAMETER: Rejection cost (r)
VALUE: r > 0 (time, effort, delay cost of each submission-rejection cycle)
UNIT: utility units
TOLERANCE: parametric
SOURCE: Novel — captures revision time + resubmission delay
NOTES: Each submission-rejection costs the author r. The total cost of k
       rejections before acceptance is k*r. This creates the trade-off:
       aim high (higher prestige if accepted) vs. aim accurately (fewer
       rejections, lower total cost).
DRIFT_RISK: MEDIUM — Author may make r endogenous or journal-specific.
             Keep it constant for the base model.

PARAMETER: Review noise (sigma)
VALUE: sigma > 0
UNIT: standard deviation of reviewer signal
TOLERANCE: parametric
SOURCE: Novel formalization
NOTES: Reviewer observes signal s = q + epsilon, epsilon ~ N(0, sigma^2).
       Journal accepts if s >= t_j. This makes acceptance probabilistic
       even for papers near the threshold.
DRIFT_RISK: LOW — standard noisy signal model

PARAMETER: Expected submissions before acceptance (E[K])
VALUE: To be derived as a function of q, {t_j}, r, sigma
UNIT: count
TOLERANCE: must be derived, not assumed
SOURCE: Novel derivation — this paper's contribution
NOTES: Key result: E[K] grows logarithmically in n (number of journals) for
       papers with quality in the middle of the distribution.
DRIFT_RISK: HIGH — must be derived from the equilibrium strategy

MILESTONES:

M1: Game-theoretic framework + definitions — define the submission game
    (authors, journals, reviewers), quality distribution, prestige hierarchy,
    rejection cost, review noise. Establish payoff functions for submission
    strategy. Introduction with literature gap: Ellison (2002) showed
    publication delays increased but did not derive the equilibrium
    submission strategy or the efficiency loss from rejection cascades.

M2: Submission strategy derivation + rejection cascade theorem — derive the
    optimal submission strategy. Prove the rejection cascade result: E[K]
    grows logarithmically in n. Derive the efficiency loss (total wasted
    review effort across all papers). Prove that desk rejection reduces E[K].

M3: Application + boundary conditions — map the model onto real journal
    hierarchies using published acceptance rates and submission data.
    Boundary conditions: sigma -> 0 (perfect review), r -> 0 (costless
    rejection), n -> infinity. Sensitivity analysis.

M4: Full paper — Introduction (peer review as a market mechanism), Related work
    (Ellison 2002, Azar 2007, Card & DellaVigna 2013), Discussion (policy —
    desk rejection, cascaded review, consortium submission systems),
    Conclusion. Self-contained Abstract.

ORACLE:
The model is valid if and only if:
1. The submission game is formally defined with explicit payoff functions
2. The equilibrium submission strategy is derived from the payoffs
3. E[K] is characterized as a function of paper quality and system parameters
4. The efficiency loss is quantified
5. Desk rejection's effect on efficiency is proven

Peer Reviewer must verify: is the submission strategy derived from the game,
or is the "top-down" norm simply assumed? If assumed, REJECT.

KNOWN_DRIFT_RISKS:
- Assuming authors submit top-down rather than deriving it as an equilibrium
  outcome — the derivation IS the contribution
- Making the model too complex (dynamic revision, learning from rejections,
  journal reputation dynamics) — keep it a clean static game
- Not citing Ellison (2002) as the natural enemy — must show what is new
- Confusing acceptance threshold with quality — noisy review means
  acceptance is probabilistic, not deterministic
- Moralizing about peer review being "broken" — the model shows
  peer review is individually rational but socially inefficient.
  That is a game theory result, not a normative judgment.
- Using made-up acceptance rates — cite published data where available
  (e.g., Card & DellaVigna 2013 for top economics journals)
- Treating review effort as free — reviewers have opportunity costs.
  This is part of the efficiency loss calculation.
- Orphan figure references — minimum figures:
    Figure 1: Optimal submission threshold as a function of paper quality
    Figure 2: Expected submissions E[K] as a function of quality for different n
    Figure 3: Efficiency loss (total wasted reviews) as a function of system parameters

# === CROSS-PAPER FINDINGS ===

- [F-005] POLICY LANGUAGE OVERSHOOTS MODEL SCOPE — scope precisely.
- [F-002] "ILLUSTRATIVE" COMPONENT LOAD-BEARING — the cascade theorem IS it.
- [F-036/F-024] FIGURES CODE-ONLY — render, don't leave code blocks.
- [F-015] MISSING DATA/CODE AVAILABILITY STATEMENT — include one.
- [F-006] NOTATION OVERLOAD — q is quality, t is threshold, r is rejection cost. Single meanings.
- [F-037] RELATED WORK TOO LONG — under 600 words.
- [F-014] EM DASH IN TITLE — use colon format.
- [DE-015/058/065/080] SCOPE DISGUISE — limitations are limitations.
- [DE-038] PLACEHOLDER VALUES — real data or conditional language.
- [F-034] DO NOT CLAIM LEAN-READINESS.

# === LESSONS FROM PRIOR RUNS ===

- THEOREM FRAMING — logarithmic growth of E[K] is the key result. Frame as
  characterization theorem, value in interpretation.
- CONDITION THE MAPPING — acceptance rate data is illustrative.
- NATURAL ENEMY — Ellison (2002). Show the advance.

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory (auto-versioned)
Resolve using auto-versioning:
1. List all existing directories matching C:\PROJECTS\SHELL\papers\ACADEMIC_PUBLISHING_2026_*
2. If none: ACADEMIC_PUBLISHING_2026_[TODAY]_001
3. If some: increment highest sequence number
Store as RESOLVED_DIR.

Create RESOLVED_DIR with subdirectories:
  figures/, outputs/, results/raw/, results/final/, devlog/, prompts/

### Step 2 — Write CLAUDE.md
  # The Publication Game — NORTH STAR

  ## What We Are Building
  A game-theoretic model of journal submission deriving the equilibrium strategy
  and proving rejection cascades are individually rational but socially wasteful.

  ## The Core Claim
  The expected number of submissions before acceptance grows logarithmically
  in the number of journals. Desk rejection reduces this inefficiency.

  ## Frozen Parameters (quick reference)
  | Parameter | Value | Source |
  |-----------|-------|--------|
  | Paper quality q | [0,1] | Novel |
  | Journal threshold t_j | ordered | Novel (Ellison 2002 style) |
  | Rejection cost r | r > 0 | Novel |
  | Review noise sigma | sigma > 0 | Standard |

  ## Critical Enforcements
  - Submission strategy DERIVED from payoffs, not assumed
  - Rejection cascade theorem formally proven
  - Real acceptance rate data where available
  - Individual rationality vs social efficiency kept distinct

### Step 3 — Write frozen_spec.md
Fill from FROZEN_SPEC_PARAMETERS above. Lock date today.
Locked by: James P Rice Jr.

### Step 4 — Initialize state files
state_vector.md — TURN: 0, MILESTONE: M1, MODE: INIT
innovation_log.md — header with project name and timestamp
dead_ends.md — header with project name

### Step 5 — Copy all prompts from SHELL
Copy from C:\PROJECTS\SHELL\prompts\ into RESOLVED_DIR\prompts\:
  04_paper_orchestrator.md, 05_author.md, 06_peer_reviewer.md,
  07_editor.md, 08_steelman.md

### Step 6 — Write STATUS.md, README.md, CHAIN_PROMPT.md, SACRED_FILES.md, BEST_PRACTICES.md, devlog/DEV_LOG.md
Follow the same pattern as other SHELL init files. Content derivable from INPUTS above.

### Step 7 — Initialize git
  git init && git add -A && git commit -m "Turn 0 | Init | ACADEMIC_PUBLISHING_2026"

---

## HAND OFF — EXECUTE PAPER PIPELINE

DO NOT STOP HERE. Read prompts/04_paper_orchestrator.md NOW and execute it.
You are the Orchestrator. Begin at INITIALIZE.

YOUR INPUTS:
  PROBLEM: [the full PROBLEM text above]
  DATA: No empirical data beyond cited acceptance rates. All results derived analytically.
  SLUG: ACADEMIC_PUBLISHING_2026
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS above]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every review pass]

BEGIN NOW. Run M1. Do not ask for confirmation. Execute the pipeline.
