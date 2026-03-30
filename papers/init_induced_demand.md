# INIT — INDUCED DEMAND AS A NASH EQUILIBRIUM
# Pre-filled. Ready to run.
# claude --dangerously-skip-permissions papers/init_induced_demand.md

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Induced Demand as a Nash Equilibrium: A Game-Theoretic Model of Why Wider Roads Create More Traffic
SLUG: induced_demand_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: Transportation Research Part B
PIPELINE: PAPER

PROBLEM:
Models road expansion as a congestion game. Derives Braess paradox conditions
for realistic networks. Proves induced demand is a Nash equilibrium phenomenon:
traffic returns to congestion level determined by value-of-time distribution.
Derives the "futility threshold" — minimum capacity increase needed to actually
reduce congestion in the long run.

The paper is formal game theory applied to transportation. Induced demand must
be proven as an equilibrium property under Wardrop user equilibrium, not
described as a behavioral tendency. The futility threshold must be a closed-form
expression derived from the model parameters — not a simulation result or
empirical estimate.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Congestion function
VALUE: BPR function t(x) = t_0 * (1 + alpha * (x/c)^beta), with alpha = 0.15,
       beta = 4, where t_0 is free-flow travel time, x is flow, c is capacity
UNIT: time (minutes)
TOLERANCE: alpha and beta are standard BPR values; results should be stated
           for general alpha, beta with BPR values as illustration
SOURCE: Bureau of Public Roads 1964 | Traffic Assignment Manual
NOTES: The BPR function is the workhorse of traffic assignment. The quartic
       form (beta=4) means congestion is highly nonlinear — small capacity
       changes near saturation have large travel time effects.
DRIFT_RISK: LOW — standard in transportation literature

PARAMETER: Wardrop user equilibrium
VALUE: Traffic distributes across routes such that no driver can reduce travel
       time by unilaterally switching routes; all used routes have equal travel
       time; unused routes have travel time >= equilibrium travel time
UNIT: equilibrium concept
TOLERANCE: exact — this is the foundational concept
SOURCE: Wardrop 1952 | Some Theoretical Aspects of Road Traffic Research |
        Proc. Inst. Civil Engineers 1(3):325-362
NOTES: Wardrop UE is the Nash equilibrium of the congestion game with a
       continuum of players. It is distinct from system optimum (SO) where
       total travel time is minimized. The gap between UE and SO is the
       price of anarchy — relevant but not the main contribution.
DRIFT_RISK: MEDIUM — Author may confuse UE with SO; must be explicit about
             which concept is used where

PARAMETER: Braess paradox
VALUE: Adding road capacity (or a new link) can increase total travel time
       at Wardrop equilibrium — proven for specific network topologies
UNIT: paradox condition (inequality)
TOLERANCE: must derive conditions, not just cite the existence of the paradox
SOURCE: Braess 1968 | Uber ein Paradoxon aus der Verkehrsplanung |
        Unternehmensforschung 12:258-268
NOTES: Braess showed the paradox for a specific 4-node network. The paper
       must derive conditions for when Braess paradox holds in general networks
       and connect this to induced demand.
DRIFT_RISK: HIGH — Author may treat Braess paradox as a curiosity rather
             than connecting it to induced demand as the same equilibrium
             phenomenon

PARAMETER: Value of time distribution
VALUE: Lognormal distribution across the driver population, with parameters
       mu and sigma calibrated to literature values
UNIT: $/hour
TOLERANCE: lognormal is standard; results should hold for general distributions
           with lognormal as special case
SOURCE: Small & Verhoef 2007 | The Economics of Urban Transportation |
        Routledge, Chapter 3
NOTES: The value of time distribution is what drives induced demand: when
       capacity increases, travel time drops, and drivers with lower value
       of time (previously priced out by congestion) enter the network.
       This is the mechanism — not "latent demand" as a black box.
DRIFT_RISK: HIGH — Author may treat induced demand as behavioral ("more
             roads attract more drivers") rather than as an equilibrium
             property of the value-of-time distribution

PARAMETER: Futility threshold
VALUE: Minimum capacity increase delta_c* such that long-run equilibrium
       congestion is strictly lower than pre-expansion congestion, derived
       as a function of the value-of-time distribution, BPR parameters,
       and current capacity
SOURCE: Rice [this paper] — derived result
NOTES: This is the core novel contribution. Below the futility threshold,
       capacity expansion is fully absorbed by induced demand. Above it,
       some congestion relief persists. The threshold must be a closed-form
       expression.
DRIFT_RISK: HIGH — Author may not derive this formally; may just show that
             induced demand exists without quantifying when expansion works

MILESTONES:

M1: Congestion game model and definitions — define the network, BPR
    congestion function, Wardrop UE, value-of-time distribution, induced
    demand formally. Establish notation. Distinguish UE from SO explicitly.

M2: Induced demand as Nash equilibrium theorem and Braess conditions —
    prove that capacity expansion leads to new UE where induced demand
    restores congestion to the level determined by the value-of-time
    distribution. Derive Braess paradox conditions for general networks.
    State induced demand theorem formally.

M3: Futility threshold derivation and boundary conditions — derive the
    minimum capacity increase delta_c* that produces lasting congestion
    relief. Prove it as a closed-form expression. Sensitivity analysis:
    how does futility threshold vary with BPR parameters, value-of-time
    distribution parameters, and network topology? Boundary conditions:
    what happens as capacity approaches infinity?

M4: Full paper — Introduction (the highway expansion puzzle), Related work
    (Downs 1962, Braess 1968, Wardrop 1952, Duranton & Turner 2011,
    Goodwin 1996, Small & Verhoef 2007), Discussion (policy implications
    for congestion pricing vs. capacity expansion, limitations of static
    model), Conclusion. Self-contained Abstract.

ORACLE:
The model is valid if and only if:
1. Induced demand is proven as a Wardrop UE property via value-of-time distribution
2. Braess paradox conditions are derived for general networks, not just cited
3. The futility threshold is a closed-form expression, not a numerical result
4. UE and SO are clearly distinguished throughout
5. The mechanism is the value-of-time distribution, not "latent demand" as a black box

Peer Reviewer must verify: is the futility threshold a derived formula or a
described concept? If described without derivation, REJECT.

KNOWN_DRIFT_RISKS:
- Treating induced demand as behavioral rather than equilibrium — the mechanism
  is that lower congestion makes driving rational for agents with lower value
  of time, restoring congestion to its equilibrium level; this is game theory,
  not psychology
- Not deriving futility threshold formally — the closed-form expression is the
  contribution; without it, the paper is a survey
- Confusing system optimum with user equilibrium — the paper is about UE
  (what actually happens), not SO (what a planner would want); must be
  explicit about this distinction at every stage
- Treating Braess paradox as separate from induced demand — they are both
  manifestations of the same equilibrium phenomenon; the paper must unify them
- Citing Duranton & Turner 2011 as the result — their result is empirical
  (VKT elasticity ~ 1); this paper provides the theoretical foundation
  explaining WHY the elasticity is near 1
- Adding simulation results — theory paper; simulations illustrate, not replace
- Moralizing about car culture — expansion futility is math, not politics
- Missing congestion pricing connection — mention in Discussion
- Failing to address dynamic traffic assignment — state static UE limitation
- Orphan figure references — every figure must have clear formal content:
    Figure 1: BPR congestion function and equilibrium with/without expansion
    Figure 2: Induced demand mechanism — value-of-time distribution shift
    Figure 3: Futility threshold as function of capacity for various distributions

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory
Create D:\EXPERIMENTS\INDUCED_DEMAND\ with:
  spec/, state/, outputs/, results/raw/, results/validated/, results/final/,
  devlog/, src/, papers/, papers/induced_demand_2026/,
  papers/induced_demand_2026/figures/, prompts/

### Step 2 — Write CLAUDE.md
North star: congestion game proving induced demand is Wardrop UE property.
Futility threshold delta_c* in closed form. Frozen params: BPR (alpha=0.15,
beta=4), Wardrop UE, lognormal VOT. Enforcements: equilibrium not behavior,
closed-form futility threshold, UE vs. SO distinguished, Braess unified.

### Step 3 — Write spec/frozen_spec.md
Fill from FROZEN_SPEC_PARAMETERS above. Lock date today.
Locked by: James P Rice Jr.

### Step 4 — Initialize state files
state/state_vector.md — TURN: 0, MILESTONE: M1, MODE: INIT
state/innovation_log.md — header with project name and timestamp
state/dead_ends.md — header with project name

### Step 5 — Copy all prompts from SHELL
Copy from D:\EXPERIMENTS\SHELL\prompts\ into D:\EXPERIMENTS\INDUCED_DEMAND\prompts\:
  04_paper_orchestrator.md
  05_author.md
  06_peer_reviewer.md
  07_editor.md
  run_milestone.md
Do NOT copy 00_init.md — SHELL-level only.

Also write prompts/turn_prompts_log.md:
  # TURN PROMPTS LOG — induced_demand_2026
  # Every exact prompt logged here. Required for reproducibility.
  [No entries yet. First entry written at Turn 1 M1.]

### Step 5b — Write run_pipeline.ps1

Write run_pipeline.ps1 in the project root (D:\EXPERIMENTS\INDUCED_DEMAND\) with
the slug set to "induced_demand_2026". Use the template from
D:\EXPERIMENTS\SHELL\prompts\00_init.md Step 15, replacing [SLUG] with
induced_demand_2026 and [SLUG] paths with INDUCED_DEMAND.

### Step 6 — Write STATUS.md
Phase: INIT -> PAPER PIPELINE
Turn: 0
What Is Done: Scaffolded. Spec locked.
What Is Next: Author writes M1 (Congestion game model + definitions).

### Step 7 — Write remaining required files
Write README.md, CHAIN_PROMPT.md, SACRED_FILES.md, BEST_PRACTICES.md,
devlog/DEV_LOG.md, outputs/options.md, outputs/state_vector_backup.md.
CHAIN_PROMPT.md must include:
  Pipeline: PAPER — Claude-only, milestone-by-milestone gating
  Author: Claude | Peer Reviewer: Claude | Editor: Claude

### Step 8 — Initialize git
  cd D:\EXPERIMENTS\INDUCED_DEMAND
  git init
  git add -A
  git commit -m "Turn 0 | Init | induced_demand_2026"

### Step 9 — Print confirmation and hand off:
  PROJECT INITIALIZED: induced_demand_2026
  Spec locked. All files created. Git initialized.
  Beginning paper pipeline — M1 (Congestion Game Model + Definitions) first.
  Output: papers/induced_demand_2026/paper.md
  Running. James P Rice Jr. reviews when done.

---

## HAND OFF — EXECUTE PAPER PIPELINE

Load prompts/04_paper_orchestrator.md.

Pass:
  PROBLEM: [full PROBLEM text above]
  DATA: No empirical data. All results derived analytically from the game model.
        Duranton & Turner 2011 referenced for empirical motivation only.
  SLUG: induced_demand_2026
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS into every Author and Reviewer prompt]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every pass]

Run the full milestone pipeline: M1 -> M2 -> M3 -> M4.
Do not skip milestones. Do not open M2 until M1 is Peer Reviewer ACCEPT.
Halt only on HALT CONDITIONS.
When done write papers/induced_demand_2026/paper.md and halt.
James P Rice Jr. reviews it.
