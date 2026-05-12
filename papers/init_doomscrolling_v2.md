# INIT — DOOMSCROLLING V2: OPTIMAL STOPPING WITH SATIATION AND WELFARE CHARACTERIZATION
# EXECUTE IMMEDIATELY. Do not summarize, analyze, or ask questions.
# Read the INPUTS below, then execute the SETUP SEQUENCE step by step.
# Load prompts/00_init.md for the setup procedure, then run it with these inputs.
# This is not a document to review — it is a set of instructions to follow NOW.
#
# V2 of doomscrolling_2026. Incorporates independent steelman review feedback:
#   SF-1: Fix objective function (discounted cost, not c*T)
#   SF-2: Welfare can be positive or negative — reframe as characterization
#   SF-3: Add satiation — primary real-world stopping mechanism
#   AN-1: Lead with welfare analysis, not trap theorem
#   AN-2: Fix three citation mischaracterizations
#   AN-3: Relabel disguised limitations as limitations
#   AN-4: Distinguish total pool from above-threshold pool
#   AN-5: Engage with strategic experimentation literature

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Doomscrolling as Optimal Stopping Failure: Welfare Characterization Under Algorithmic Feeds with Satiation
SLUG: DOOMSCROLLING_V2
AUTHOR: James P Rice Jr.
TARGET_VENUE: Journal of Behavioral Decision Making
PIPELINE: PAPER

PROBLEM:
Models social media feed consumption as an optimal stopping problem where the
agent must decide when to stop scrolling. The feed is an infinite sequence of
items with stochastic reward. The agent discounts exponentially and pays a
per-period opportunity cost. Under a chronological (i.i.d.) feed, the optimal
stopping time is finite. Under an engagement-maximizing algorithmic feed (the
platform reorders items to maximize session duration), the stopping time can
become infinite — the attention trap.

V2 ADVANCES OVER V1:

1. SATIATION: The agent's utility is time-dependent: u_t(r) = phi(t) * u(r),
   where phi(t) is a decreasing satiation function with phi(1) = 1 and
   phi(t) -> 0 as t -> infinity. This models diminishing enjoyment over a
   scrolling session. The central question becomes: does the trap survive
   satiation? Under what conditions on phi does the algorithmic feed still
   produce infinite stopping times, and under what conditions does satiation
   break the trap? This is the primary real-world mechanism by which people
   stop scrolling, and v1 assumed it away entirely.

2. WELFARE CHARACTERIZATION (not "loss"): V1 framed Delta_W = W_chron - W_algo
   as a "welfare loss," but Delta_W can be negative — the trap can IMPROVE
   welfare when the platform places high-quality content. V2 derives the
   complete welfare characterization: the exact condition under which the
   algorithmic feed is welfare-improving vs. welfare-reducing. This reframes
   the policy question: regulation is justified only when the algorithmic
   feed is welfare-reducing, which depends on the platform's item selection
   strategy.

3. DISCOUNTED COST: V1 had an inconsistency between the objective function
   (undiscounted c*T) and the proofs (discounted delta^{t-1} * c). V2 uses
   the correct discounted formulation throughout:
   max_T E[sum_{t=1}^{T} delta^{t-1} (u_t(r_t) - c)]

4. CONTRIBUTION REORDERING: V1 led with the trap theorem (near-tautological)
   and buried the welfare analysis. V2 leads with the welfare characterization
   and the capping negative result. The trap theorem becomes a supporting
   lemma, not the headline.

5. STRATEGIC EXPERIMENTATION LITERATURE: V1 failed to engage with Kremer et al.
   (2014), Bergemann and Hege (1998/2005), and Che and Mierendorff (2019) —
   all of which study a strategic principal preventing an agent from stopping.
   V2 engages directly and distinguishes the permutation mechanism from
   information-provision mechanisms.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Optimal stopping framework
VALUE: Secretary problem variant — agent observes items sequentially, decides
       after each item whether to stop or continue, maximizing total discounted
       utility minus discounted opportunity cost of time. Discounted cost:
       sum_{t=1}^{T} delta^{t-1} (u_t(r_t) - c). NOT c*T.
UNIT: decision framework
TOLERANCE: exact — this is the foundational framework
SOURCE: Ferguson 1989 (historical survey) | Chow, Robbins, Siegmund 1971
        (theoretical foundations)
NOTES: Ferguson 1989 is a HISTORICAL SURVEY of the secretary problem, not a
       theoretical contribution. The theoretical foundations are from Chow,
       Robbins, and Siegmund (1971). Do NOT over-credit Ferguson as
       "establishing the modern theory."
DRIFT_RISK: HIGH — v1 had objective function inconsistency (c*T vs discounted).
             Author MUST use discounted cost in Definition AND proofs.

PARAMETER: Satiation function
VALUE: phi: N -> (0,1] with phi(1) = 1, phi strictly decreasing, phi(t) -> 0
       as t -> infinity. Agent's per-period utility at time t is
       u_t(r) = phi(t) * u(r). The effective stopping threshold RISES over
       time because phi shrinks the utility.
UNIT: dimensionless multiplier
TOLERANCE: exact — phi must be formally specified, not hand-waved
SOURCE: Novel — Rice (this paper). Motivated by standard diminishing marginal
        utility over consumption sequences.
NOTES: The satiation function is the v2 innovation. The key result must
       characterize EXACTLY which phi functions preserve the trap and which
       break it. Candidate boundary: phi(t) decays slower than 1/t preserves
       the trap; faster than 1/t breaks it. This must be PROVEN, not asserted.
DRIFT_RISK: CRITICAL — Author may introduce phi but not derive the precise
             boundary condition. The satiation analysis MUST produce a theorem
             stating: "The trap persists if and only if [condition on phi]."

PARAMETER: Reward process
VALUE: Items have i.i.d. rewards from distribution F with finite mean mu and
       variance sigma^2. Each item yields base reward r_t ~ F independently.
       Agent's per-period utility from item t is u_t(r_t) = phi(t) * u(r_t).
UNIT: utility per item
TOLERANCE: i.i.d. is the baseline; algorithmic feed breaks i.i.d.
SOURCE: Standard stochastic process — i.i.d. sequence
DRIFT_RISK: MEDIUM — Author must formalize distinction between chronological
             and algorithmic feeds with satiation

PARAMETER: Algorithmic feed
VALUE: Platform chooses permutation sigma of available items to maximize E[T]
       where T is the stopping time under the agent's optimal policy given
       the reordered sequence AND satiation. The platform knows phi.
UNIT: permutation of item sequence
TOLERANCE: exact — adversarial mechanism
SOURCE: Rice v1 (this paper series)
NOTES: With satiation, the platform's problem is harder — it must overcome
       the rising threshold. The platform may need to place BETTER items
       later in the sequence (to compensate for phi decay), which is the
       opposite of v1's strategy. The optimal ordering under satiation must
       be derived, not assumed.
DRIFT_RISK: HIGH — Author may ignore how satiation changes the platform's
             optimal ordering strategy

PARAMETER: Discount factor
VALUE: Exponential delta in (0,1). Agent objective:
       max_{T} E[sum_{t=1}^{T} delta^{t-1} (phi(t) * u(r_t) - c)].
       With delta < 1, phi decreasing, and i.i.d. rewards, optimal stopping
       time is finite. Key question: does algorithmic reordering still yield
       T = infinity when phi -> 0?
SOURCE: Standard decision theory — exponential discounting
DRIFT_RISK: MEDIUM — Must use exponential only. Hyperbolic trivializes.

PARAMETER: Welfare characterization
VALUE: Delta_W = W_chron - W_algo. This can be POSITIVE (trap is welfare-reducing)
       or NEGATIVE (trap is welfare-improving). Must derive the exact condition
       on the platform's item selection strategy that determines the sign.
       Reframe: "When is the trap harmful?" not "The trap is harmful."
SOURCE: Standard welfare economics + Rice v1
NOTES: V1 treated Delta_W as always positive. V2 must derive the sign condition
       explicitly and reframe the policy discussion accordingly.
DRIFT_RISK: CRITICAL — Author may default to v1's "welfare loss" framing.
             Every use of "welfare loss" must be replaced with "welfare change"
             or "welfare characterization" unless the sign has been proven
             positive in the specific case under discussion.

PARAMETER: Above-threshold pool size
VALUE: N_above = |{x in X : phi(t) * u(q(x)) > c for some relevant t}|.
       Distinguish from total pool size N = |X|. The trap requires N_above
       to be large enough relative to the session length. With satiation,
       the effective above-threshold pool SHRINKS over time (because phi
       shrinks, raising the threshold). Must derive the effective pool size
       as a function of t and phi.
SOURCE: Novel — Rice v2
DRIFT_RISK: HIGH — v1 conflated total pool with above-threshold pool.
             Author MUST distinguish these throughout.

MILESTONES:

M1: Optimal stopping model with satiation — define phi, the time-dependent
    utility u_t, the agent's objective (discounted cost!), the chronological
    vs. algorithmic feed under satiation, reservation value under satiation
    (now time-dependent: s*(t)), welfare as characterization (not loss).
    Prove finite stopping under i.i.d. with satiation. Define platform's
    optimization problem under satiation. Literature positioning: engage with
    Kremer et al. 2014, Bergemann-Hege 1998/2005, Che-Mierendorff 2019
    alongside Ferguson (survey), Chow-Robbins-Siegmund (theory), EFK, Allcott.

M2: Trap-under-satiation theorem and welfare characterization — prove:
    (a) For phi decaying sufficiently slowly, the trap persists (T* = infinity)
        even with satiation. Derive the precise boundary condition on phi.
    (b) For phi decaying faster than the boundary, the trap breaks (T* < inf).
    (c) Welfare characterization: derive the exact condition under which
        Delta_W > 0 (trap is harmful) vs. Delta_W < 0 (trap is beneficial).
        This is the central v2 contribution.
    (d) Negative result on reward capping: still holds under satiation.

M3: Platform design fixes under satiation + boundary conditions — propose
    fixes that restore finite stopping under satiation. Note that satiation
    itself is a partial fix — derive when it suffices. Boundary conditions:
    distinguish total pool from above-threshold pool, derive effective pool
    depletion rate under satiation. Sensitivity analysis. Competing models
    (include strategic experimentation literature). Limitations (not open
    problems): fixed pool is a limitation; single-agent is a limitation.
    Open problem (genuine): learning dynamics.

M4: Full paper — Abstract, Related Work (engage strategic experimentation
    literature properly), Discussion (lead with welfare characterization,
    address "is this obvious" objection, policy implications conditioned
    on sign of Delta_W), Conclusion. Fix all citation characterizations:
    Ferguson = historical survey, Bayraktar-Zhou replaced with Riedel 2009,
    Bursztyn et al. accurately described.

ORACLE:
The model is valid if and only if:
1. The objective function uses discounted cost throughout (Definition AND proofs)
2. Satiation function phi is formally specified with a proven boundary condition
   for trap persistence vs. breakdown
3. The welfare characterization derives the SIGN CONDITION for Delta_W, not
   just the magnitude
4. The trap-under-satiation theorem states precise conditions on phi
5. The above-threshold pool is distinguished from the total pool
6. Platform design fixes account for satiation
7. The strategic experimentation literature is engaged (not just cited)
8. Ferguson is correctly characterized as a historical survey
9. "Welfare loss" language is replaced with "welfare change/characterization"
   except where sign is proven positive

Peer Reviewer must verify: does the paper prove WHEN the trap is harmful
(Delta_W > 0) vs. beneficial (Delta_W < 0)? If it only proves the trap
exists without characterizing welfare sign: REJECT.

KNOWN_DRIFT_RISKS:

- V1 REGRESSION: Objective function inconsistency — c*T (undiscounted) vs
  delta^{t-1} * c (discounted). V2 MUST use discounted cost exclusively.
  If the Author writes c*T anywhere, REJECT immediately.

- V1 REGRESSION: Welfare framing — v1 treated Delta_W as always positive.
  V2 must derive the sign condition. If the Author writes "welfare loss"
  without proving Delta_W > 0 in the specific case: REJECT.

- V1 REGRESSION: Ferguson over-credit — Ferguson 1989 is a historical survey.
  Theoretical foundations are Chow-Robbins-Siegmund 1971. If the Author
  writes "Ferguson established the theory": REJECT.

- V1 REGRESSION: Citation mischaracterization — Bayraktar-Zhou 2017 is
  about arbitrage in mathematical finance, NOT optimal stopping under
  ambiguity. Replace with Riedel (2009, Econometrica). Bursztyn et al. 2022
  is "Opinions as Facts" about belief formation, NOT about "network effects
  in social media adoption."

- SATIATION HAND-WAVE: Author may introduce phi but not derive the precise
  boundary condition for trap persistence. The satiation analysis MUST
  produce a theorem: "The trap persists iff [condition on phi]." Without
  this theorem, the satiation extension is window dressing.

- NEAR-TAUTOLOGY DODGE: The trap theorem (items above threshold => agent
  continues) is structurally simple. Author MUST lead with welfare
  characterization and capping negative result, not with the trap. The
  trap becomes a supporting lemma. If the Author leads with "we prove
  the agent never stops" as the headline contribution: flag for reordering.

- SCOPE DISGUISE: "Multi-agent interaction" and "endogenous item creation"
  are LIMITATIONS of the single-agent fixed-pool model, not open problems.
  Author must label them as limitations. "Learning dynamics" is a genuine
  open problem.

- POOL CONFLATION: Author must distinguish total item pool N from
  above-threshold pool N_above. With satiation, N_above(t) shrinks over
  time. If the Author writes "platforms have millions of items" without
  specifying above-threshold count: flag.

- STRATEGIC EXPERIMENTATION GAP: Must engage with Kremer, Mansour, Perry
  (2014, AER); Bergemann and Hege (1998/2005); Che and Mierendorff (2019,
  Econometrica). These study a strategic principal sustaining engagement
  via information provision. The distinction: our platform reorders items
  with direct utility; they provide information signals. If the Author
  does not cite and distinguish from at least two of these: REJECT.

- PROOF STRATEGY (satiation Bellman): With satiation, the Bellman equation
  is non-stationary: V_t(s) = max(0, phi(t)*s - c + delta * E[V_{t+1}(u(r))]).
  The reservation value s*(t) is now time-dependent and increasing (because
  phi(t) is decreasing, making items less valuable). The trap requires the
  platform to place items good enough to exceed the RISING threshold
  s*(t)/phi(t). Derive when this is feasible.

- PROOF STRATEGY (welfare sign): The sign of Delta_W depends on whether
  the chronological agent's selective consumption (stop early, avoid bad
  items) outperforms the algorithmic agent's exhaustive consumption (scroll
  forever through all items, including declining-utility ones). With
  satiation, the algorithmic agent's late-session items have low utility
  (phi is small), so exhaustive consumption is worse. Derive the crossover
  point formally.

- FIGURE SPECIFICATION:
    Figure 1: Stopping threshold s*(t) under satiation (rising) vs. without
    Figure 2: Welfare Delta_W as a function of phi decay rate — showing
              positive region (trap harmful) and negative region (trap beneficial)
    Figure 3: Platform design fix effectiveness under satiation

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 0 — Resolve project directory
Base slug: DOOMSCROLLING_V2
Check existing: C:\PROJECTS\SHELL\papers\DOOMSCROLLING_V2*
Use auto-versioning: DOOMSCROLLING_V2_[YYYY-MM-DD]_001

### Step 1 — Create project directory
Create resolved directory with:
  figures/, results/raw/, results/final/, outputs/, devlog/, prompts/

### Step 2 — Write CLAUDE.md
North star: optimal stopping with satiation proving algorithmic feeds create
attention traps that may be welfare-improving or welfare-reducing depending
on platform item selection. V2 advances: satiation, welfare sign condition,
discounted cost, strategic experimentation engagement.

### Step 3 — Write frozen_spec.md
Fill from FROZEN_SPEC_PARAMETERS above. Lock date today.
Locked by: James P Rice Jr.
Include v1 reference: C:\PROJECTS\SHELL\papers\DOOMSCROLLING\paper.md

### Step 4 — Initialize state files
state_vector.md — TURN: 0, MILESTONE: M1, MODE: INIT
innovation_log.md — header with project name and timestamp
dead_ends.md — header; add entry: "V1 treated Delta_W as always positive.
  V1 used undiscounted cost c*T. V1 ignored satiation. V1 mischaracterized
  Ferguson, Bayraktar-Zhou, Bursztyn. Do not repeat."

### Step 5 — Copy all prompts from SHELL
Copy from C:\PROJECTS\SHELL\prompts\ into project prompts/:
  04_paper_orchestrator.md
  05_author.md
  06_peer_reviewer.md
  07_editor.md
  08_steelman.md
  run_milestone.md

Also write prompts/turn_prompts_log.md

### Step 5b — Write run_pipeline.ps1
Use template from C:\PROJECTS\SHELL\prompts\00_init.md Step 15.

### Step 6 — Write STATUS.md
Phase: INIT -> PAPER PIPELINE
Turn: 0
What Is Done: Scaffolded. Spec locked. V1 feedback incorporated.
What Is Next: Author writes M1 (Optimal stopping model with satiation).

### Step 7 — Write remaining required files
README.md, CHAIN_PROMPT.md, SACRED_FILES.md, BEST_PRACTICES.md,
devlog/DEV_LOG.md, outputs/options.md, outputs/state_vector_backup.md.

### Step 8 — Initialize git
  cd [RESOLVED_DIR]
  git init
  git add -A
  git commit -m "Turn 0 | Init | doomscrolling_v2"

### Step 9 — Print confirmation and hand off:
  PROJECT INITIALIZED: doomscrolling_v2
  V2 of doomscrolling_2026. Steelman feedback incorporated.
  Key v2 advances: satiation, welfare sign condition, discounted cost.
  Beginning paper pipeline — M1 first.
  Running. James P Rice Jr. reviews when done.

---

## HAND OFF — EXECUTE PAPER PIPELINE

DO NOT STOP HERE. The setup is complete. Now you must execute the paper pipeline.

Read prompts/04_paper_orchestrator.md NOW and follow every instruction in it.
You are the Orchestrator. Begin at the INITIALIZE section.

YOUR INPUTS:
  PROBLEM: [the full PROBLEM text from the INPUTS section above, including V2 ADVANCES]
  DATA: No empirical data. All results derived analytically from the optimal stopping model with satiation.
  SLUG: [RESOLVED_SLUG]
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS above into every Author and Reviewer prompt]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every review pass]

BEGIN NOW. Run M1. Do not ask for confirmation. Do not summarize the orchestrator.
Execute it. Write the paper.
