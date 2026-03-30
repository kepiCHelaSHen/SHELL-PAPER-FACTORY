# INIT — TECHNOLOGICAL LOCK-IN AS A COORDINATION FAILURE
# Pre-filled. Ready to run.
# claude --dangerously-skip-permissions papers/init_tech_lockin.md

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Technological Lock-In as a Coordination Failure: A Formal Model of Path Dependency with Network Externalities
SLUG: tech_lockin_2025
AUTHOR: James P Rice Jr.
TARGET_VENUE: Research Policy
PIPELINE: PAPER

PROBLEM:
Models technology adoption as a coordination game with network externalities.
Derives Nash equilibria and proves inferior technology can be stable (lock-in)
when network externality exceeds quality difference. Derives the exact "escape
velocity" — minimum coordinated switching coalition to move from inferior to
superior equilibrium. Shows escape velocity increases with network size,
explaining why lock-in is harder to break in larger markets.

The paper is formal game theory applied to technology adoption. Every claim
must be a theorem or proposition. Lock-in must be proven as an equilibrium
property, not just described as a historical pattern. The escape velocity
must be derived in closed form — not estimated numerically or illustrated
with examples.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Network externality function
VALUE: v_i(n_i) = alpha * n_i / N + q_i, where n_i is adopters of technology i,
       N is total population, alpha is externality strength, q_i is standalone
       quality of technology i
UNIT: utility
TOLERANCE: exact functional form — results derived from this specification
SOURCE: Katz & Shapiro 1985 | Network Externalities, Competition, and
        Compatibility | AER 75(3):424-440
NOTES: The additive separability of network effect and quality is what makes
       the model tractable. The ratio n_i/N normalizes the externality so
       results scale with population size.
DRIFT_RISK: LOW — standard framework

PARAMETER: Quality parameters
VALUE: q_A > q_B (technology A is objectively superior to technology B)
UNIT: utility
TOLERANCE: strict inequality required for lock-in to be meaningful
SOURCE: Model assumption — without quality difference, lock-in is trivial
NOTES: The entire interest of the model is that the inferior technology B
       can be adopted in equilibrium despite q_A > q_B. If q_A = q_B there
       is no lock-in, just indifference.
DRIFT_RISK: LOW — definitional

PARAMETER: Nash equilibrium concept
VALUE: Pure strategy Nash equilibrium in population game where each agent
       chooses technology A or B to maximize individual utility
UNIT: equilibrium concept
TOLERANCE: must be pure strategy NE — mixed strategies less interesting here
SOURCE: Standard game theory — population games
NOTES: There are generically two pure NE: all-A and all-B. The paper must
       show that all-B is stable despite q_A > q_B when alpha > q_A - q_B.
DRIFT_RISK: MEDIUM — Author may use wrong equilibrium concept or be imprecise
             about stability

PARAMETER: Escape velocity definition
VALUE: Minimum coalition size s* such that if s* agents simultaneously switch
       from B to A, then switching is individually rational for all remaining
       B-adopters — i.e., s* triggers a cascade to the all-A equilibrium
UNIT: number of agents (or fraction of N)
TOLERANCE: exact — this is the novel contribution
SOURCE: Novel definition — Rice [this paper]
NOTES: This is the core result. It must be derived as a closed-form function
       of N, alpha, q_A - q_B. The scaling with N is the key insight: larger
       networks are harder to unlock.
DRIFT_RISK: HIGH — Author may define escape velocity loosely or fail to derive
             closed form. Must be a theorem with explicit formula.

PARAMETER: Lock-in stability condition
VALUE: All-B equilibrium is stable when alpha > q_A - q_B (network externality
       exceeds quality gap)
SOURCE: Rice [this paper] — derived result
NOTES: This is the formal lock-in theorem. It must be stated precisely:
       when alpha > q_A - q_B, no individual agent has incentive to switch
       from B to A, even though A is objectively better.
DRIFT_RISK: MEDIUM — Author may state this informally rather than as a theorem

MILESTONES:

M1: Coordination game model and definitions — define the population game,
    strategy spaces, payoff functions, network externality. Establish notation.
    Define lock-in formally as a stable inferior equilibrium. Define escape
    velocity precisely.

M2: Lock-in theorem and escape velocity derivation — prove that all-B is a
    stable NE when alpha > q_A - q_B. Derive escape velocity s* in closed
    form as a function of N, alpha, and quality gap. Prove s* is unique.

M3: Network size scaling and boundary conditions — prove that s*/N is
    increasing in N (escape velocity grows faster than linearly with network
    size). Derive boundary conditions: what happens as alpha approaches
    q_A - q_B from above? What happens as N approaches infinity? Sensitivity
    analysis on all parameters.

M4: Full paper — Introduction (lock-in as coordination failure, not irrationality),
    Related work (Arthur 1989, David 1985, Katz & Shapiro 1985, Farrell &
    Saloner 1985, Liebowitz & Margolis 1995), Discussion (policy implications
    for antitrust, standardization, platform regulation), Conclusion.
    Self-contained Abstract.

ORACLE:
The model is valid if and only if:
1. Lock-in is proven as a Nash equilibrium property with explicit conditions
2. Escape velocity is derived as a closed-form function of N, alpha, q_A - q_B
3. The scaling result (larger networks = harder to unlock) is a theorem
4. The lock-in condition alpha > q_A - q_B is derived, not assumed
5. Competing explanations (switching costs, irrationality) are formally distinguished

Peer Reviewer must verify: is escape velocity a closed-form formula derived
from the model, or is it described qualitatively? If qualitative, REJECT.

KNOWN_DRIFT_RISKS:
- Conflating lock-in with switching costs — they are different mechanisms;
  lock-in in this model arises purely from network externalities, not from
  costs of switching; must state this distinction explicitly
- Not deriving escape velocity in closed form — the whole contribution is
  the formula; a qualitative description is not enough
- Citing Arthur 1989 without extending — Arthur showed path dependence via
  increasing returns; this paper derives the escape velocity, which Arthur
  did not; must clearly state the extension
- Citing David 1985 (QWERTY) as evidence — David's historical claims are
  contested (Liebowitz & Margolis 1990); use the formal model, not QWERTY
  anecdotes
- Confusing lock-in with market failure — lock-in is a coordination failure,
  which is a specific type of market failure; be precise
- Making the model too complex by adding dynamics — start with the static
  game; dynamics can be discussed as extensions
- Failing to address the Liebowitz & Margolis critique — they argue lock-in
  is empirically rare; the paper must engage this formally (the model shows
  lock-in is stable, not that it is inevitable)
- Missing the policy discussion — escape velocity has direct antitrust
  implications; include this in Discussion but keep it brief
- Orphan figure references — every figure must have clear formal content:
    Figure 1: Payoff functions showing two equilibria and lock-in region
    Figure 2: Escape velocity s* as a function of N for various alpha
    Figure 3: Phase diagram in (alpha, q_A - q_B) space

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory
Create D:\EXPERIMENTS\TECH_LOCKIN\ with:
  spec/, state/, outputs/, results/raw/, results/validated/, results/final/,
  devlog/, src/, papers/, papers/tech_lockin_2025/,
  papers/tech_lockin_2025/figures/, prompts/

### Step 2 — Write CLAUDE.md
North star: formal model of technology lock-in as coordination failure.
Lock-in stable when alpha > q_A - q_B. Escape velocity s*(N, alpha, delta_q)
in closed form. Enforcements: NE not irrationality, closed-form escape
velocity, scaling theorem, distinguish from Arthur 1989.

### Step 3 — Write spec/frozen_spec.md
Fill from FROZEN_SPEC_PARAMETERS above. Lock date today.
Locked by: James P Rice Jr.

### Step 4 — Initialize state files
state/state_vector.md — TURN: 0, MILESTONE: M1, MODE: INIT
state/innovation_log.md — header with project name and timestamp
state/dead_ends.md — header with project name

### Step 5 — Copy all prompts from SHELL
Copy from D:\EXPERIMENTS\SHELL\prompts\ into D:\EXPERIMENTS\TECH_LOCKIN\prompts\:
  04_paper_orchestrator.md
  05_author.md
  06_peer_reviewer.md
  07_editor.md
  run_milestone.md
Do NOT copy 00_init.md — SHELL-level only.

Also write prompts/turn_prompts_log.md:
  # TURN PROMPTS LOG — tech_lockin_2025
  # Every exact prompt logged here. Required for reproducibility.
  [No entries yet. First entry written at Turn 1 M1.]

### Step 5b — Write run_pipeline.ps1

Write run_pipeline.ps1 in the project root (D:\EXPERIMENTS\TECH_LOCKIN\) with
the slug set to "tech_lockin_2025". Use the template from
D:\EXPERIMENTS\SHELL\prompts\00_init.md Step 15, replacing [SLUG] with
tech_lockin_2025 and [SLUG] paths with TECH_LOCKIN.

### Step 6 — Write STATUS.md
Phase: INIT -> PAPER PIPELINE
Turn: 0
What Is Done: Scaffolded. Spec locked.
What Is Next: Author writes M1 (Coordination game model + definitions).

### Step 7 — Write remaining required files
Write README.md, CHAIN_PROMPT.md, SACRED_FILES.md, BEST_PRACTICES.md,
devlog/DEV_LOG.md, outputs/options.md, outputs/state_vector_backup.md.
CHAIN_PROMPT.md must include:
  Pipeline: PAPER — Claude-only, milestone-by-milestone gating
  Author: Claude | Peer Reviewer: Claude | Editor: Claude

### Step 8 — Initialize git
  cd D:\EXPERIMENTS\TECH_LOCKIN
  git init
  git add -A
  git commit -m "Turn 0 | Init | tech_lockin_2025"

### Step 9 — Print confirmation and hand off:
  PROJECT INITIALIZED: tech_lockin_2025
  Spec locked. All files created. Git initialized.
  Beginning paper pipeline — M1 (Coordination Game Model + Definitions) first.
  Output: papers/tech_lockin_2025/paper.md
  Running. James P Rice Jr. reviews when done.

---

## HAND OFF — EXECUTE PAPER PIPELINE

Load prompts/04_paper_orchestrator.md.

Pass:
  PROBLEM: [full PROBLEM text above]
  DATA: No empirical data. All results derived analytically from the game model.
  SLUG: tech_lockin_2025
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS into every Author and Reviewer prompt]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every pass]

Run the full milestone pipeline: M1 -> M2 -> M3 -> M4.
Do not skip milestones. Do not open M2 until M1 is Peer Reviewer ACCEPT.
Halt only on HALT CONDITIONS.
When done write papers/tech_lockin_2025/paper.md and halt.
James P Rice Jr. reviews it.
