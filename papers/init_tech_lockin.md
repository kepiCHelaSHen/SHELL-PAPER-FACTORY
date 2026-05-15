# INIT — FORMAL MODEL OF TECHNOLOGICAL LOCK-IN
# EXECUTE IMMEDIATELY. Do not summarize, analyze, or ask questions.
# Read the INPUTS below, then execute the SETUP SEQUENCE step by step.
# Load prompts/00_init.md for the setup procedure, then run it with these inputs.
# This is not a document to review — it is a set of instructions to follow NOW.

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: A Formal Model of Technological Lock-In: Switching Costs, Network Effects, and the Inefficiency Threshold
SLUG: TECH_LOCKIN_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: Research Policy
PIPELINE: PAPER

PROBLEM:
Formalizes technological lock-in as a game between adopters facing switching
costs and network externalities. An installed base of users on technology A
faces a superior technology B. Each user's payoff from switching depends on
how many others switch (network effect) and a private switching cost. Derives
the critical mass threshold: the minimum fraction of users who must switch
simultaneously for B to dominate A. Proves that this threshold increases with
switching costs and installed-base network effects, creating a region of
"inefficient lock-in" where the superior technology fails to be adopted even
though every user would prefer it if all switched. Derives the subsidy needed
to overcome lock-in and characterizes when lock-in is permanent vs. temporary.
The central contribution is the inefficiency threshold theorem: there exists a
closed-form critical mass as a function of switching costs and network effects,
below which the inferior technology persists indefinitely.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Switching cost (s)
VALUE: s > 0, explored parametrically
UNIT: utility units
TOLERANCE: parametric
SOURCE: Novel formalization building on Farrell & Saloner 1985; Klemperer 1987
NOTES: Private switching cost, heterogeneous across users. Distribution F(s)
       over the population. Key cases: uniform, exponential.
DRIFT_RISK: MEDIUM — Author may confuse switching costs with sunk costs.
             Switching costs are forward-looking (cost of migrating).
             Sunk costs are backward-looking (prior investment). Keep distinct.

PARAMETER: Network effect parameter (n)
VALUE: n >= 0, explored parametrically
UNIT: utility per adopter
TOLERANCE: parametric
SOURCE: Katz & Shapiro 1985; Farrell & Saloner 1985
NOTES: User's utility from technology X = intrinsic value v_X + n * (fraction
       using X). Network effects make the installed base self-reinforcing.
DRIFT_RISK: MEDIUM — Author may make network effects too complex (indirect,
             two-sided). Keep it direct: utility proportional to adoption share.

PARAMETER: Technology quality gap (delta)
VALUE: delta = v_B - v_A > 0 (B is intrinsically superior)
UNIT: utility units
TOLERANCE: parametric
SOURCE: Novel formalization
NOTES: B is objectively better than A. The lock-in question is: why doesn't
       B win? The answer is switching costs + network effects.
DRIFT_RISK: HIGH — Author may try to make delta endogenous or allow A to be
             superior in some dimensions. Keep it simple: B is strictly better,
             lock-in is the puzzle.

PARAMETER: Critical mass threshold (k*)
VALUE: To be derived in closed form as a function of s, n, delta
UNIT: fraction of population (0 to 1)
TOLERANCE: must be derived, not assumed
SOURCE: Novel derivation — this paper's contribution
NOTES: k* is the fraction of users who must switch simultaneously for
       switching to be individually rational for each of them. Below k*,
       no one switches. Above k*, everyone switches (tipping point).
DRIFT_RISK: HIGH — Author may assume the threshold rather than deriving
             it from the game structure. Must define the game, write payoffs,
             and solve for the equilibrium explicitly.

PARAMETER: Optimal subsidy (sigma*)
VALUE: To be derived as a function of s, n, delta
UNIT: utility units per user
TOLERANCE: must be derived
SOURCE: Novel derivation
NOTES: The subsidy that reduces the effective switching cost enough to
       bring k* to zero (making individual switching rational without
       coordination). Policy payoff of the model.
DRIFT_RISK: MEDIUM — must come from the game structure, not a welfare argument.

MILESTONES:

M1: Game-theoretic framework + definitions — define the technology adoption
    game (players, strategies, payoffs), switching costs, network effects,
    quality gap. Establish payoff functions for staying on A vs. switching to B.
    Introduction with literature gap: Arthur (1989) showed lock-in is possible
    but did not derive a closed-form critical mass threshold.

M2: Critical mass derivation + inefficiency threshold theorem — derive k* in
    closed form. Prove Theorem 1: for s > 0 and n > 0, k* > 0 (lock-in is
    possible). Characterize k* as a function of s, n, delta. Derive the
    optimal subsidy sigma*. Prove properties: k* increases in s and n,
    decreases in delta.

M3: Technology mapping + boundary conditions — map at least 3 historical
    technology transitions onto the model (e.g., QWERTY/Dvorak, VHS/Betamax,
    internal combustion/electric vehicles). Boundary conditions: s -> 0,
    n -> 0, delta -> infinity. Sensitivity analysis.

M4: Full paper — Introduction (lock-in as market failure), Related work
    (Arthur 1989, David 1985, Farrell & Saloner 1985, Katz & Shapiro 1985),
    Discussion (policy implications — subsidies, standards, interoperability),
    Conclusion. Self-contained Abstract.

ORACLE:
The model is valid if and only if:
1. The adoption game is formally defined with explicit payoff functions
2. The critical mass k* is derived from the game's equilibrium conditions
3. k* > 0 is proven as a theorem for positive switching costs and network effects
4. The technology mapping uses real historical examples with cited parameters
5. The optimal subsidy is derived from the equilibrium condition

Peer Reviewer must verify: is k* derived from the payoff functions,
or is it assumed? If assumed, REJECT.

KNOWN_DRIFT_RISKS:
- Assuming the critical mass threshold rather than deriving it — the
  derivation from the game's payoff structure IS the contribution
- Confusing lock-in with switching costs alone — lock-in requires BOTH
  switching costs AND network effects. Without network effects, individual
  switching is rational whenever delta > s.
- Making the model too complex (dynamic, multi-technology, heterogeneous
  network effects) — keep it a clean static coordination game first
- Not citing Arthur (1989) as the natural enemy — must show what is new
  beyond the existing lock-in literature
- Treating QWERTY/Dvorak as established fact — David (1985) claimed
  QWERTY is inefficient, Liebowitz & Margolis (1990) contested this.
  Present both sides.
- Overstating policy implications — subsidy is derived from the model.
  Real-world technology transitions depend on many factors the model
  does not capture.
- Using made-up switching cost estimates — cite published estimates or
  present as illustrative with conditional language
- Orphan figure references — every figure must have code.
  Minimum figures:
    Figure 1: Critical mass k* as a function of switching cost s for different n
    Figure 2: Phase diagram — regions of lock-in vs. adoption in (s, n) space
    Figure 3: Technology map — historical cases plotted on the model

# === CROSS-PAPER FINDINGS ===

- [F-005] POLICY LANGUAGE OVERSHOOTS MODEL SCOPE — scope policy claims precisely.
- [F-002] "ILLUSTRATIVE" COMPONENT THAT IS LOAD-BEARING — k* and the theorem ARE the contribution.
- [F-036/F-024] FIGURES CODE-ONLY — render figures, don't leave code blocks.
- [F-015] MISSING DATA/CODE AVAILABILITY STATEMENT — include one.
- [F-006] NOTATION OVERLOAD — s is switching cost, n is network effect, delta is quality gap. Single meanings.
- [F-037] RELATED WORK TOO LONG — keep under 600 words.
- [F-014] EM DASH IN TITLE — use colon format.
- [DE-015/058/065/080] SCOPE DISGUISE — limitations are limitations.
- [DE-038] PLACEHOLDER VALUES IN TABLES — real cited values or conditional language.
- [F-034] DO NOT CLAIM LEAN-READINESS.

# === LESSONS FROM PRIOR RUNS ===

- THEOREM FRAMING — if k* follows from solving a coordination game, frame as
  "closed-form characterization." Value is in the mapping, not proof difficulty.
- CONDITION THE MAPPING — historical examples are illustrative. Say so.
- NATURAL ENEMY — Arthur (1989) is the competitor. Show the advance clearly.

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory (auto-versioned)
Resolve using auto-versioning:
1. List all existing directories matching C:\PROJECTS\SHELL\papers\TECH_LOCKIN_2026_*
2. If none: TECH_LOCKIN_2026_[TODAY]_001
3. If some: increment highest sequence number
Store as RESOLVED_DIR.

Create RESOLVED_DIR with subdirectories:
  figures/, outputs/, results/raw/, results/final/, devlog/, prompts/

### Step 2 — Write CLAUDE.md
  # Technological Lock-In — NORTH STAR

  ## What We Are Building
  A game-theoretic model deriving the critical mass threshold for technology
  switching under network effects and switching costs.

  ## The Core Claim
  A closed-form critical mass k* exists. Below k*, the inferior technology
  persists. Above k*, the superior technology wins. k* is derived from the
  game's payoff structure.

  ## Frozen Parameters (quick reference)
  | Parameter | Value | Source |
  |-----------|-------|--------|
  | Switching cost s | parametric | Farrell & Saloner 1985 |
  | Network effect n | parametric | Katz & Shapiro 1985 |
  | Quality gap delta | v_B - v_A > 0 | Novel |
  | Critical mass k* | derived | Novel |

  ## Critical Enforcements
  - k* must be DERIVED from payoff functions, not assumed
  - Lock-in requires both switching costs AND network effects
  - Historical examples are illustrative, not empirical validation
  - Individual rationality vs coordination failure must be kept distinct

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
Follow the same pattern as other SHELL init files. All content derivable from INPUTS above.

### Step 7 — Initialize git
  git init && git add -A && git commit -m "Turn 0 | Init | TECH_LOCKIN_2026"

---

## HAND OFF — EXECUTE PAPER PIPELINE

DO NOT STOP HERE. Read prompts/04_paper_orchestrator.md NOW and execute it.
You are the Orchestrator. Begin at INITIALIZE.

YOUR INPUTS:
  PROBLEM: [the full PROBLEM text above]
  DATA: No empirical data. All results derived analytically.
  SLUG: TECH_LOCKIN_2026
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS above]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every review pass]

BEGIN NOW. Run M1. Do not ask for confirmation. Execute the pipeline.
