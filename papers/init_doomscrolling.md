# INIT — DOOMSCROLLING AS OPTIMAL STOPPING FAILURE
# Pre-filled. Ready to run.
# claude --dangerously-skip-permissions papers/init_doomscrolling.md

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Doomscrolling as Optimal Stopping Failure: A Formal Model of Infinite Scroll and Attention Traps
SLUG: doomscrolling_2025
AUTHOR: James P Rice Jr.
TARGET_VENUE: Journal of Behavioral Decision Making
PIPELINE: PAPER

PROBLEM:
Models social media feed consumption as an optimal stopping problem where the
agent must decide when to stop scrolling. The feed is an infinite sequence of
items with stochastic reward (dopamine/novelty). Proves that the optimal stopping
rule exists under standard conditions but that algorithmic feed design (which
learns the agent's reward function and maximizes engagement) shifts the stopping
threshold so that the agent never stops — creating a "trap" where continued
scrolling is always marginally rational but globally suboptimal. Derives the
welfare loss from the trap and the platform design changes that would restore
finite stopping times.

The paper is formal decision theory and mechanism design. The trap property must
be proven as a theorem — that algorithmic feed optimization eliminates finite
stopping times under specific conditions. The welfare loss must be quantified
analytically. Platform design fixes must be shown to restore finite stopping
times, not merely argued to be helpful.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Optimal stopping framework
VALUE: Secretary problem variant — agent observes items sequentially, decides
       after each item whether to stop or continue, with the goal of maximizing
       total discounted utility minus opportunity cost of time
UNIT: decision framework
TOLERANCE: exact — this is the foundational framework
SOURCE: Ferguson 1989 | Who Solved the Secretary Problem? | Statistical
        Science 4(3):282-289
NOTES: The classical secretary problem maximizes the probability of selecting
       the best item. Here the agent maximizes cumulative discounted utility
       (not just best-item probability), making it a stopping-time problem
       with ongoing rewards rather than a single-selection problem.
DRIFT_RISK: MEDIUM — Author may default to classical secretary problem
             formulation rather than the cumulative reward variant needed here

PARAMETER: Reward process
VALUE: Items have i.i.d. rewards from distribution F with finite mean mu and
       variance sigma^2. Each item yields reward r_t ~ F independently.
       Agent's per-period utility from item t is u(r_t).
UNIT: utility per item
TOLERANCE: i.i.d. is the baseline; algorithmic feed breaks i.i.d. (this is
           the key mechanism)
SOURCE: Standard stochastic process — i.i.d. sequence
NOTES: The i.i.d. assumption holds for a chronological (non-algorithmic) feed.
       The algorithmic feed reorders items to maximize engagement, breaking
       the i.i.d. structure. The transition from i.i.d. to algorithmic
       ordering is where the trap emerges.
DRIFT_RISK: HIGH — Author may not formalize the distinction between
             chronological and algorithmic feeds precisely enough

PARAMETER: Algorithmic feed
VALUE: Platform observes agent's reward function (or estimates it) and
       reorders items to maximize total engagement time T. Formally: platform
       chooses a permutation sigma of available items to maximize E[T] where
       T is the stopping time under the agent's optimal policy given the
       reordered sequence.
UNIT: permutation of item sequence
TOLERANCE: exact — this is the adversarial mechanism
SOURCE: Novel formalization — Rice [this paper]
NOTES: The platform is not malicious in the model — it maximizes engagement,
       which is its objective. The trap is an emergent property of the
       interaction between the agent's optimal stopping rule and the
       platform's engagement maximization. Must formalize this as a
       principal-agent or mechanism design problem.
DRIFT_RISK: HIGH — Author may treat the platform as a black box rather than
             formalizing its optimization problem. The platform's objective
             must be stated mathematically.

PARAMETER: Discount factor
VALUE: Exponential delta in (0,1). Agent objective: max_{T} E[sum delta^t u(r_t) - c*T].
       With delta < 1 and i.i.d. rewards, optimal stopping time is finite
       (reservation value theorem). Algorithmic reordering makes reservation
       value unreachable -> T = infinity.
SOURCE: Standard decision theory — exponential discounting
DRIFT_RISK: MEDIUM — Author may use hyperbolic discounting, which trivializes
             the result; must use exponential to show trap is feed manipulation

PARAMETER: Welfare measure
VALUE: W = E[sum delta^t u(r_t)] - c*T. Welfare loss = W*(chronological) -
       W*(algorithmic). Must derive in closed form or bound analytically.
SOURCE: Standard welfare economics
DRIFT_RISK: MEDIUM — Author may show welfare decreases without quantifying

MILESTONES:

M1: Optimal stopping model and definitions — define the reward process, agent's
    objective, stopping rule, chronological vs. algorithmic feed. Establish
    notation. Prove that under i.i.d. rewards with delta < 1, the optimal
    stopping time is finite (reservation value theorem). Define welfare.
    Define the platform's optimization problem formally.

M2: Trap theorem and welfare loss derivation — prove that algorithmic feed
    optimization (reordering items to maximize engagement) eliminates finite
    stopping times under specified conditions. This is the central theorem:
    the agent's optimal stopping rule, when facing an adversarially ordered
    feed, yields T = infinity (or T > any finite bound). Derive the welfare
    loss analytically. State all conditions required for the trap.

M3: Platform design fix and boundary conditions — propose feed design
    modifications that restore finite stopping times (e.g., chronological
    intervals, reward capping, mandatory stopping points). Prove that these
    modifications restore finite T while preserving some engagement. State
    boundary conditions: when does the trap fail (e.g., very high opportunity
    cost, very low delta)? Sensitivity analysis on delta, c, and reward
    distribution parameters.

M4: Full paper — Introduction (the doomscrolling phenomenon, formalized),
    Related work (secretary problem literature, attention economics, platform
    design — Ely et al. 2020, Allcott et al. 2020, addiction models),
    Discussion (policy implications, relationship to attention regulation,
    limitations of the static model), Conclusion. Self-contained Abstract.

ORACLE:
The model is valid if and only if:
1. The optimal stopping framework is correctly specified with finite stopping
   under i.i.d. rewards proven as a baseline
2. The algorithmic feed's optimization problem is formalized, not described
3. The trap property (elimination of finite stopping times) is proven as a theorem
4. The welfare loss is quantified analytically, not just signed
5. Platform design fixes are proven to restore finite stopping, not just proposed

Peer Reviewer must verify: is the trap property a proven theorem with explicit
conditions, or is it an intuitive argument? If intuitive, REJECT.

KNOWN_DRIFT_RISKS:
- Making the model too informal — this is a common risk for "fun" topics;
  every claim must be a theorem or proposition with proof; no informal
  arguments about dopamine or addiction
- Not proving the trap property formally — the theorem that algorithmic
  feeds eliminate finite stopping times is the contribution; without a
  proof, the paper is a blog post
- Moralizing about social media instead of doing math — the paper must be
  dispassionate; the trap is a mathematical property, not a moral judgment;
  the math is more powerful than the moralizing
- Confusing optimal stopping with addiction models — addiction changes
  preferences; this model has fixed preferences, trap is structural
- Using hyperbolic discounting — trivializes the result; must use
  exponential to show trap is feed manipulation, not self-control failure
- Not formalizing platform's optimization problem — must specify objective
  function, strategy space, and information set
- Failing to quantify welfare loss — must quantify HOW MUCH, not just sign
- Missing boundary conditions — high opportunity cost agents escape; derive
- Orphan figure references — every figure must have clear formal content:
    Figure 1: Optimal stopping under i.i.d. vs. algorithmic feed
    Figure 2: Welfare loss as a function of algorithmic feed strength
    Figure 3: Platform design fix — stopping time restoration

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory
Create D:\EXPERIMENTS\DOOMSCROLLING\ with:
  spec/, state/, outputs/, results/raw/, results/validated/, results/final/,
  devlog/, src/, papers/, papers/doomscrolling_2025/,
  papers/doomscrolling_2025/figures/, prompts/

### Step 2 — Write CLAUDE.md
North star: optimal stopping model proving algorithmic feeds create attention
traps. Finite stopping under i.i.d.; algorithmic reordering -> T = infinity.
Frozen params: secretary problem variant (Ferguson 1989), i.i.d. rewards,
engagement-maximizing permutation, exponential delta < 1. Enforcements:
trap as theorem, exponential discounting only, platform objective formalized,
welfare loss quantified, no moralizing.

### Step 3 — Write spec/frozen_spec.md
Fill from FROZEN_SPEC_PARAMETERS above. Lock date today.
Locked by: James P Rice Jr.

### Step 4 — Initialize state files
state/state_vector.md — TURN: 0, MILESTONE: M1, MODE: INIT
state/innovation_log.md — header with project name and timestamp
state/dead_ends.md — header with project name

### Step 5 — Copy all prompts from SHELL
Copy from D:\EXPERIMENTS\SHELL\prompts\ into D:\EXPERIMENTS\DOOMSCROLLING\prompts\:
  04_paper_orchestrator.md
  05_author.md
  06_peer_reviewer.md
  07_editor.md
  run_milestone.md
Do NOT copy 00_init.md — SHELL-level only.

Also write prompts/turn_prompts_log.md:
  # TURN PROMPTS LOG — doomscrolling_2025
  # Every exact prompt logged here. Required for reproducibility.
  [No entries yet. First entry written at Turn 1 M1.]

### Step 5b — Write run_pipeline.ps1

Write run_pipeline.ps1 in the project root (D:\EXPERIMENTS\DOOMSCROLLING\) with
the slug set to "doomscrolling_2025". Use the template from
D:\EXPERIMENTS\SHELL\prompts\00_init.md Step 15, replacing [SLUG] with
doomscrolling_2025 and [SLUG] paths with DOOMSCROLLING.

### Step 6 — Write STATUS.md
Phase: INIT -> PAPER PIPELINE
Turn: 0
What Is Done: Scaffolded. Spec locked.
What Is Next: Author writes M1 (Optimal stopping model + definitions).

### Step 7 — Write remaining required files
Write README.md, CHAIN_PROMPT.md, SACRED_FILES.md, BEST_PRACTICES.md,
devlog/DEV_LOG.md, outputs/options.md, outputs/state_vector_backup.md.
CHAIN_PROMPT.md must include:
  Pipeline: PAPER — Claude-only, milestone-by-milestone gating
  Author: Claude | Peer Reviewer: Claude | Editor: Claude

### Step 8 — Initialize git
  cd D:\EXPERIMENTS\DOOMSCROLLING
  git init
  git add -A
  git commit -m "Turn 0 | Init | doomscrolling_2025"

### Step 9 — Print confirmation and hand off:
  PROJECT INITIALIZED: doomscrolling_2025
  Spec locked. All files created. Git initialized.
  Beginning paper pipeline — M1 (Optimal Stopping Model + Definitions) first.
  Output: papers/doomscrolling_2025/paper.md
  Running. James P Rice Jr. reviews when done.

---

## HAND OFF — EXECUTE PAPER PIPELINE

Load prompts/04_paper_orchestrator.md.

Pass:
  PROBLEM: [full PROBLEM text above]
  DATA: No empirical data. All results derived analytically from the
        optimal stopping model.
  SLUG: doomscrolling_2025
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS into every Author and Reviewer prompt]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every pass]

Run the full milestone pipeline: M1 -> M2 -> M3 -> M4.
Do not skip milestones. Do not open M2 until M1 is Peer Reviewer ACCEPT.
Halt only on HALT CONDITIONS.
When done write papers/doomscrolling_2025/paper.md and halt.
James P Rice Jr. reviews it.
