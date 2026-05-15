# INIT — VACCINATION AS A PUBLIC GOODS GAME
# EXECUTE IMMEDIATELY. Do not summarize, analyze, or ask questions.
# Read the INPUTS below, then execute the SETUP SEQUENCE step by step.
# Load prompts/00_init.md for the setup procedure, then run it with these inputs.
# This is not a document to review — it is a set of instructions to follow NOW.

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Vaccination as a Public Goods Game: Nash Equilibria and the Free-Rider Threshold
SLUG: VACCINE_GAME_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: Journal of Mathematical Biology
PIPELINE: PAPER

PROBLEM:
Models vaccination decisions as a public goods game where each agent chooses
whether to vaccinate (costly, private benefit + externality) or free-ride
(costless, benefits from herd immunity). Derives the Nash equilibrium
vaccination rate as a closed-form function of vaccine efficacy, disease
transmissibility (R0), and vaccine cost/risk ratio. Proves that the Nash
equilibrium vaccination rate is always below the social optimum (herd immunity
threshold), and quantifies the free-rider gap as a function of R0. Derives the
exact subsidy needed to close the gap. The central contribution is the
free-rider gap theorem: rational self-interested agents always under-vaccinate,
and the gap is worst for moderately transmissible diseases.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Basic reproduction number (R0)
VALUE: Varies by disease — measles ~15, COVID-19 ~3, influenza ~1.5
UNIT: dimensionless ratio (secondary infections per primary case)
TOLERANCE: explored parametrically (R0 from 1.1 to 20)
SOURCE: Anderson & May 1991; Fine et al. 2011 | Epidemiological Reviews 33:5-21
NOTES: R0 > 1 required for epidemic. Herd immunity threshold = 1 - 1/R0.
DRIFT_RISK: LOW — standard epidemiological parameter

PARAMETER: Vaccine efficacy (e)
VALUE: 0 < e <= 1 (perfect vaccine: e = 1)
UNIT: probability
TOLERANCE: explored parametrically
SOURCE: Standard epidemiological definition
NOTES: e = 1 for baseline model. Sensitivity analysis with e < 1.
       Effective reproduction number under vaccination: R_eff = R0 * (1 - e*p)
       where p is vaccination rate.
DRIFT_RISK: LOW — standard parameter

PARAMETER: Cost-risk ratio (c)
VALUE: c = cost_of_vaccination / cost_of_infection, c in (0, 1)
UNIT: dimensionless ratio
TOLERANCE: explored parametrically (c from 0.01 to 0.99)
SOURCE: Novel formalization — ratio captures the individual's trade-off
NOTES: c < 1 means vaccination is cheaper than infection (individually rational
       to vaccinate IF no herd immunity). c > 0 means vaccination is not free.
       The free-rider problem arises because herd immunity makes infection
       unlikely even without vaccination, reducing individual incentive.
DRIFT_RISK: HIGH — Author may confuse individual cost with social cost.
             Keep these strictly separate. Individual cost ratio c drives
             the Nash equilibrium. Social cost is what the subsidy corrects.

PARAMETER: Nash equilibrium vaccination rate (p*)
VALUE: p* = (1/e) * (1 - 1/R0) - (1 - c)/(e * R0 * c) [to be derived]
UNIT: probability
TOLERANCE: must be derived, not assumed
SOURCE: Novel derivation — this paper's contribution
NOTES: The exact formula depends on modeling choices. The key properties to
       prove: (1) p* < p_herd for all R0 > 1 and 0 < c < 1, (2) the gap
       p_herd - p* increases with R0 up to a point then decreases,
       (3) the gap is zero only if c = 0 (free vaccination).
DRIFT_RISK: HIGH — Author may assume the Nash equilibrium formula rather
             than deriving it from first principles. Must set up the game,
             define payoffs, and solve for the equilibrium explicitly.

PARAMETER: Herd immunity threshold (p_herd)
VALUE: p_herd = 1 - 1/R0 (for perfect vaccine, e = 1)
UNIT: probability
TOLERANCE: exact
SOURCE: Anderson & May 1991
NOTES: For imperfect vaccine: p_herd = (1 - 1/R0) / e.
DRIFT_RISK: LOW — textbook result

PARAMETER: Optimal subsidy (s*)
VALUE: To be derived — the per-vaccination subsidy that makes p* = p_herd
UNIT: cost units (same as vaccination cost)
TOLERANCE: must be derived as a closed-form function of R0, e, c
SOURCE: Novel derivation
NOTES: This is the policy payoff. The subsidy compensates for the externality.
       Must be derived from the game-theoretic model, not asserted.
DRIFT_RISK: MEDIUM — Author may derive the subsidy from a welfare argument
             rather than from the game-theoretic equilibrium condition.

MILESTONES:

M1: Game-theoretic framework + definitions — define the vaccination game
    (players, strategies, payoffs), R0, herd immunity threshold, vaccine
    efficacy, cost-risk ratio. Establish the payoff functions for vaccinate
    vs. free-ride. Establish notation. Introduction with literature gap:
    Bauch & Earn (2004) showed the game-theoretic framing but did not derive
    closed-form equilibrium as a function of R0.

M2: Nash equilibrium derivation + free-rider gap theorem — derive the Nash
    equilibrium vaccination rate p* in closed form. Prove Theorem 1: p* < p_herd
    for all R0 > 1 and c > 0. Derive the free-rider gap Delta = p_herd - p*.
    Prove properties of Delta as a function of R0. Derive the optimal subsidy s*.

M3: Disease mapping + boundary conditions — map at least 4 diseases onto the
    model using published R0 and vaccine cost estimates. Show which diseases
    have the largest free-rider gap. Boundary conditions: R0 -> 1 (disease
    barely transmissible), R0 -> infinity (extremely transmissible), c -> 0
    (free vaccine), c -> 1 (vaccine as costly as infection).
    Sensitivity analysis table.

M4: Full paper — Introduction (vaccination as a collective action problem),
    Related work (Bauch & Earn 2004, Geoffard & Philipson 1997, Brito et al. 1991),
    Discussion (policy implications — subsidies, mandates, nudges),
    Conclusion. Self-contained Abstract.

ORACLE:
The model is valid if and only if:
1. The vaccination game is formally defined with explicit payoff functions
2. The Nash equilibrium p* is derived (not assumed) from the payoff functions
3. p* < p_herd is proven as a formal theorem for the stated parameter ranges
4. The free-rider gap is characterized as a function of R0
5. The optimal subsidy s* is derived from the equilibrium condition
6. The disease mapping uses cited R0 values, not invented ones

Peer Reviewer must verify: is p* derived from the game's payoff functions,
or is it assumed? If assumed, REJECT.

KNOWN_DRIFT_RISKS:
- Assuming the Nash equilibrium formula rather than deriving it from
  first principles — the derivation IS the contribution
- Confusing individual rationality with social optimality — the whole
  point is that individually rational agents under-vaccinate
- Using simulation results instead of analytical derivation — this is
  a theory paper, not a simulation paper
- Making the game too complex (heterogeneous agents, dynamic games,
  network effects) — keep it a clean symmetric static game first,
  discuss extensions as limitations
- Confusing R0 with R_effective — R0 is the basic reproduction number
  without intervention; R_eff = R0(1 - e*p) is with vaccination
- Moralizing about anti-vaxxers — the model shows rational agents
  free-ride. This is a game theory result, not a moral judgment.
- Not citing Bauch & Earn (2004) as the natural enemy — must show
  what is new beyond their framework
- Overstating policy implications — the subsidy is derived from the
  model's equilibrium condition. Real-world subsidies depend on
  administrative costs, compliance, and behavioral factors the model
  does not capture.
- Using made-up cost-risk ratios for specific diseases — cite WHO or
  published health economics estimates where available
- Orphan figure references — every figure must have Python/matplotlib code.
  The paper should include at minimum:
    Figure 1: Nash equilibrium p* and herd immunity threshold as functions of R0
    Figure 2: Free-rider gap Delta as a function of R0 for different cost ratios
    Figure 3: Disease map — 4+ diseases plotted with their R0 and free-rider gap

# === CROSS-PAPER FINDINGS (from STEELMAN_FINDINGS.md) ===
# Systemic Claude Author tendencies. Address ALL proactively.

- [F-005] POLICY LANGUAGE OVERSHOOTS MODEL SCOPE — scope policy claims to what
  the model actually proves. "Subsidies close the gap" is valid. "Subsidies
  solve vaccine hesitancy" is not — the model has no behavioral component.

- [F-002] "ILLUSTRATIVE" COMPONENT THAT IS LOAD-BEARING — the Nash equilibrium
  derivation and free-rider gap theorem ARE the contribution. Do not present
  them as "one of several results."

- [F-036/F-024] FIGURES CODE-ONLY — figures must appear as rendered images in
  the paper, not code blocks. Code goes in figures/figure_N.py.

- [F-015] MISSING DATA/CODE AVAILABILITY STATEMENT — include a statement.

- [F-006] NOTATION OVERLOAD — R0 is reproduction number ONLY. Do not reuse R
  for anything else. p is vaccination rate, e is efficacy, c is cost ratio.

- [F-037] RELATED WORK SECTION TOO LONG — keep Related Work under 600 words.

- [F-014] EM DASH IN TITLE — use colon or subtitle format.

- [DE-015/058/065/080] SCOPE DISGUISE — "heterogeneous agents" and "dynamic
  games" are limitations, not open problems.

- [DE-038] PLACEHOLDER VALUES IN TABLES — disease mapping table MUST have real
  R0 values from cited sources.

- [F-034] DO NOT CLAIM LEAN-READINESS unless the init file requests it.

# === LESSONS FROM PRIOR RUNS ===

- THEOREM FRAMING — if the core result is elementary (solving a payoff equation),
  frame it as a "closed-form characterization" whose value is in the
  interpretation and disease mapping, not proof difficulty.

- CONDITION THE MAPPING — use language like "Under the cited R0 estimates,
  measles has the largest free-rider gap." Do not present point estimates as
  established facts. Report ranges where possible.

- NATURAL ENEMY — Bauch & Earn (2004) is the natural competitor. Derive their
  result as a special case if possible. Show explicitly what is new: the
  closed-form gap characterization and the subsidy derivation.

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory (auto-versioned)
Resolve the project directory using auto-versioning:
1. List all existing directories matching C:\PROJECTS\SHELL\papers\VACCINE_GAME_2026_*
2. If none exist: use VACCINE_GAME_2026_[TODAY]_001
3. If some exist: find the highest sequence number, increment by 1,
   use VACCINE_GAME_2026_[TODAY]_[NEXT_SEQ]
Store as RESOLVED_DIR. Use RESOLVED_DIR for ALL paths below.

Create RESOLVED_DIR with subdirectories:
  figures/, outputs/, results/raw/, results/final/,
  devlog/, prompts/

### Step 2 — Write CLAUDE.md
  # Vaccination as a Public Goods Game — NORTH STAR

  ## What We Are Building
  A game-theoretic model proving rational agents under-vaccinate relative to
  the social optimum, with the free-rider gap derived as a function of R0.

  ## The Core Claim
  The Nash equilibrium vaccination rate is always below the herd immunity
  threshold for any R0 > 1 and positive vaccination cost. The gap is
  characterized in closed form and the optimal subsidy is derived.

  ## Frozen Parameters (quick reference)
  | Parameter | Value | Source |
  |-----------|-------|--------|
  | R0 | 1.1 - 20 (by disease) | Anderson & May 1991 |
  | Herd immunity | 1 - 1/R0 | Standard |
  | Vaccine efficacy | 0 < e <= 1 | Standard |
  | Cost ratio | c in (0,1) | Novel formalization |

  ## Critical Enforcements
  - Nash equilibrium must be DERIVED from payoff functions, not assumed
  - Free-rider gap theorem must be formally proven
  - Disease mapping must use cited R0 values
  - Individual rationality vs social optimality must be kept distinct

### Step 3 — Write frozen_spec.md
Fill from FROZEN_SPEC_PARAMETERS above. Lock date today.
Locked by: James P Rice Jr.

### Step 4 — Initialize state files
state_vector.md — TURN: 0, MILESTONE: M1, MODE: INIT
innovation_log.md — header with project name and timestamp
dead_ends.md — header with project name

### Step 5 — Copy all prompts from SHELL
Copy from C:\PROJECTS\SHELL\prompts\ into RESOLVED_DIR\prompts\:
  04_paper_orchestrator.md
  05_author.md
  06_peer_reviewer.md
  07_editor.md
  08_steelman.md
Do NOT copy 00_init.md — SHELL-level only.

Also write prompts/turn_prompts_log.md:
  # TURN PROMPTS LOG — VACCINE_GAME_2026
  # Every exact prompt logged here. Required for reproducibility.
  [No entries yet. First entry written at Turn 1 M1.]

### Step 6 — Write STATUS.md
Phase: INIT -> PAPER PIPELINE
Turn: 0
What Is Done: Scaffolded. Spec locked.
What Is Next: Author writes M1 (game-theoretic framework, payoff definitions).

### Step 7 — Write remaining required files

Write README.md:
  # Vaccination as a Public Goods Game
  **Author:** James P Rice Jr.
  **Target:** Journal of Mathematical Biology
  **Status:** In progress
  ## What This Is
  A game-theoretic model deriving the Nash equilibrium vaccination rate and
  proving it always falls below the herd immunity threshold.

Write CHAIN_PROMPT.md:
  # CHAIN PROMPT — Vaccine Game Paper | THIS FILE WINS ALL CONFLICTS
  Name: Vaccination as a Public Goods Game
  Author: James P Rice Jr.
  Core claim: Nash equilibrium vaccination rate < herd immunity threshold
  for all R0 > 1 and c > 0. Free-rider gap and optimal subsidy derived.
  Pipeline: PAPER — Claude-only, milestone-by-milestone gating.
  [today] | Initialized from SHELL v6.2

Write SACRED_FILES.md:
  # SACRED FILES | Lock date: [today] | Locked by: James P Rice Jr.
  | File | Reason | Locked |
  |------|--------|--------|
  | frozen_spec.md | Oracle. Never modify after lock. | [today] |

Write BEST_PRACTICES.md:
  # BEST PRACTICES — Vaccine Game Paper
  - Nash equilibrium must be derived from payoff functions, not assumed.
  - Free-rider gap must be a formal theorem.
  - Disease mapping uses cited R0 values from Anderson & May 1991 or WHO.
  - Individual rationality != social optimality. Keep distinct throughout.
  - Natural enemy: Bauch & Earn 2004. Show what is new.
  - Sensitivity analysis required: R0 in [1.1, 20], c in (0, 1).
  - Milestone-by-milestone. No section opens until previous is locked.

Write devlog/DEV_LOG.md:
  # DEVELOPMENT LOG — VACCINE_GAME_2026
  ## [today] — Session 1
  Initialized from SHELL v6.2. Spec locked. All files created.

### Step 8 — Initialize git
  cd RESOLVED_DIR
  git init
  git add -A
  git commit -m "Turn 0 | Init | VACCINE_GAME_2026"

### Step 9 — Print confirmation and hand off

---

## HAND OFF — EXECUTE PAPER PIPELINE

DO NOT STOP HERE. The setup is complete. Now you must execute the paper pipeline.

Read prompts/04_paper_orchestrator.md NOW and follow every instruction in it.
You are the Orchestrator. Begin at the INITIALIZE section. This is not a file
to summarize — it is your operating manual. Execute it.

YOUR INPUTS:
  PROBLEM: [the full PROBLEM text from the INPUTS section above]
  DATA: No empirical data beyond cited epidemiological parameters. All results derived analytically from the game-theoretic model.
  SLUG: VACCINE_GAME_2026
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS above into every Author and Reviewer prompt]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every review pass]

BEGIN NOW. Run M1. Do not ask for confirmation. Do not summarize the orchestrator.
Execute it. Write the paper.
