# INIT — THE ACADEMIC PUBLISHING GAME
# Pre-filled. Ready to run.
# claude --dangerously-skip-permissions papers/init_academic_publishing.md

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: The Academic Publishing Game: A Game-Theoretic Model of Review, Revision, and Journal Selection
SLUG: academic_publishing_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: Research Policy
PIPELINE: PAPER

PROBLEM:
Models academic publishing as a sequential game between authors (journal selection),
editors (referee selection, accept/reject), and referees (effort level, recommendation).
Derives Nash equilibrium and proves: (1) rational authors submit above their quality
level (submission inflation), (2) referees exert suboptimal effort because effort is
unobservable, (3) reject-and-resubmit is an equilibrium despite wasting surplus.
Proposes a two-sided matching mechanism that Pareto-improves on current equilibrium.

The paper is formal game theory — every claim is a theorem or proposition. The three
counterintuitive results must be derived as equilibrium properties, not illustrated
with anecdotes. The matching mechanism must be proven to Pareto-dominate the
status quo equilibrium, not merely argued to be better.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Author strategy space
VALUE: Journal ranking j in {1,...,J}, where author of quality q chooses
       submission target j(q) to maximize expected payoff
UNIT: discrete ordinal ranking
TOLERANCE: exact — this is a game-theoretic definition
SOURCE: Standard game theory — sequential game with incomplete information
NOTES: The key insight is that authors choose where to submit, not whether.
       The strategy space is the journal ranking, not the paper quality.
DRIFT_RISK: LOW — standard formulation

PARAMETER: Referee effort model
VALUE: Unobservable effort e in [0,1], moral hazard structure where referee
       chooses e to maximize personal utility (reputation, learning) minus
       cost of effort c(e), with c convex and c(0)=0
UNIT: continuous on [0,1]
TOLERANCE: exact — moral hazard structure is the mechanism
SOURCE: Holmstrom 1979 | Moral Hazard and Observability | Bell J. Econ. 10(1):74-91
NOTES: Referee effort is the hidden action. The editor cannot observe e, only
       the recommendation. This creates the moral hazard that drives result (2).
DRIFT_RISK: HIGH — Author may skip the moral hazard formalization and just
             assert that referees shirk. Must derive it from incentive structure.

PARAMETER: Paper quality distribution
VALUE: Continuous on [0,1] with CDF F(q) and density f(q)
UNIT: quality score on [0,1]
TOLERANCE: general — results should hold for any well-behaved F
SOURCE: Standard mechanism design assumption
NOTES: Do not assume uniform. Results should be stated for general F, with
       uniform as a special case for closed-form illustrations.
DRIFT_RISK: LOW — standard assumption

PARAMETER: Journal acceptance threshold
VALUE: t_j increasing in journal rank j, where journal j accepts papers
       with quality signal above t_j
UNIT: threshold on [0,1]
TOLERANCE: exact — this is a model parameter
SOURCE: Derived in the model — endogenous to journal optimization
NOTES: Higher-ranked journals have higher thresholds. The key result is that
       authors rationally aim above their quality level because the payoff
       function is convex in journal rank.
DRIFT_RISK: MEDIUM — Author may treat thresholds as exogenous rather than
             deriving them from journal optimization

PARAMETER: Submission inflation equilibrium
VALUE: In Nash equilibrium, author of quality q submits to journal j*(q) > j_true(q)
       where j_true(q) is the journal whose threshold matches q
SOURCE: Rice [this paper] — derived result
NOTES: This is counterintuitive result (1). It must be a theorem, not a claim.
       The proof relies on the convexity of expected payoff in journal rank
       combined with the option value of resubmission.
DRIFT_RISK: HIGH — Author may state this as obvious rather than deriving it

MILESTONES:

M1: Game structure and definitions — define the three-player sequential game
    (author, editor, referee), strategy spaces, payoff functions, information
    structure. Establish notation. State the timing of moves explicitly.

M2: Nash equilibrium derivation — prove the three counterintuitive results
    as theorems: (1) submission inflation, (2) referee moral hazard leading
    to suboptimal effort, (3) reject-and-resubmit as equilibrium. Each must
    be a formal proposition with proof.

M3: Matching mechanism — propose the two-sided matching mechanism (authors
    matched to journals based on quality signals). Prove it Pareto-dominates
    the status quo equilibrium. State boundary conditions and assumptions
    required for the Pareto result.

M4: Full paper — Introduction (publishing as a game), Related work (Ellison
    2002, Azar 2007, Card & DellaVigna 2013, Fudenberg & Tirole 1991),
    Discussion (practical implications, limitations, extensions to open
    access), Conclusion. Self-contained Abstract.

ORACLE:
The model is valid if and only if:
1. All three counterintuitive results are proven as formal theorems
2. Submission inflation is derived from the payoff structure, not asserted
3. Referee moral hazard is modeled via Holmstrom framework, not handwaved
4. Reject-and-resubmit equilibrium is shown to waste surplus quantitatively
5. The matching mechanism is formally proven to Pareto-dominate status quo

Peer Reviewer must verify: are the three results theorems with proofs,
or are they claims illustrated with examples? If the latter, REJECT.

KNOWN_DRIFT_RISKS:
- Making the model too simple by skipping referee moral hazard — the
  unobservable effort is what makes result (2) interesting, not just
  the fact that referees are busy
- Not deriving submission inflation formally — must show it emerges from
  the payoff structure (convexity + resubmission option), not just that
  authors are "optimistic"
- Not proving the Pareto improvement of the matching mechanism — must
  show formally that all three player types are weakly better off, with
  at least one strictly better off
- Conflating Nash equilibrium with dominant strategy — the equilibrium
  concept matters; be precise about which NE concept is used
- Citing Ellison 2002 without extending — Ellison models slowdown, not
  the full sequential game; must clearly state what is new
- Treating journal thresholds as exogenous — they should be endogenous
  to the journal's optimization problem
- Adding empirical sections — this is a theory paper; keep it formal
- Moralization about peer review being broken — the paper shows it is
  an equilibrium, which is more interesting than saying it is broken
- Missing the welfare analysis — must quantify the surplus wasted by
  reject-and-resubmit in equilibrium
- Orphan figure references — every figure must have clear formal content:
    Figure 1: Game tree showing timing of moves
    Figure 2: Submission inflation — j*(q) vs. j_true(q)
    Figure 3: Welfare comparison — status quo vs. matching mechanism

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory
Create D:\EXPERIMENTS\ACADEMIC_PUBLISHING\ with:
  spec/, state/, outputs/, results/raw/, results/validated/, results/final/,
  devlog/, src/, papers/, papers/academic_publishing_2026/,
  papers/academic_publishing_2026/figures/, prompts/

### Step 2 — Write CLAUDE.md
North star: game-theoretic model of academic publishing. Three NE results +
Pareto-improving matching mechanism. Frozen params table: Author strategy
(j in {1,...,J}), Referee effort (Holmstrom 1979), Quality dist (F on [0,1]),
Core results (3 theorems). Enforcements: theorems with proofs, Holmstrom
formalism, Pareto-dominance proven, no moralizing.

### Step 3 — Write spec/frozen_spec.md
Fill from FROZEN_SPEC_PARAMETERS above. Lock date today.
Locked by: James P Rice Jr.

### Step 4 — Initialize state files
state/state_vector.md — TURN: 0, MILESTONE: M1, MODE: INIT
state/innovation_log.md — header with project name and timestamp
state/dead_ends.md — header with project name

### Step 5 — Copy all prompts from SHELL
Copy from D:\EXPERIMENTS\SHELL\prompts\ into D:\EXPERIMENTS\ACADEMIC_PUBLISHING\prompts\:
  04_paper_orchestrator.md
  05_author.md
  06_peer_reviewer.md
  07_editor.md
  run_milestone.md
Do NOT copy 00_init.md — SHELL-level only.

Also write prompts/turn_prompts_log.md:
  # TURN PROMPTS LOG — academic_publishing_2026
  # Every exact prompt logged here. Required for reproducibility.
  [No entries yet. First entry written at Turn 1 M1.]

### Step 5b — Write run_pipeline.ps1

Write run_pipeline.ps1 in the project root (D:\EXPERIMENTS\ACADEMIC_PUBLISHING\) with
the slug set to "academic_publishing_2026". Use the template from
D:\EXPERIMENTS\SHELL\prompts\00_init.md Step 15, replacing [SLUG] with
academic_publishing_2026 and [SLUG] paths with ACADEMIC_PUBLISHING.

### Step 6 — Write STATUS.md
Phase: INIT -> PAPER PIPELINE
Turn: 0
What Is Done: Scaffolded. Spec locked.
What Is Next: Author writes M1 (Game structure + definitions).

### Step 7 — Write remaining required files
Write README.md, CHAIN_PROMPT.md, SACRED_FILES.md, BEST_PRACTICES.md,
devlog/DEV_LOG.md, outputs/options.md, outputs/state_vector_backup.md.
CHAIN_PROMPT.md must include:
  Pipeline: PAPER — Claude-only, milestone-by-milestone gating
  Author: Claude | Peer Reviewer: Claude | Editor: Claude

### Step 8 — Initialize git
  cd D:\EXPERIMENTS\ACADEMIC_PUBLISHING
  git init
  git add -A
  git commit -m "Turn 0 | Init | academic_publishing_2026"

### Step 9 — Print confirmation and hand off:
  PROJECT INITIALIZED: academic_publishing_2026
  Spec locked. All files created. Git initialized.
  Beginning paper pipeline — M1 (Game Structure + Definitions) first.
  Output: papers/academic_publishing_2026/paper.md
  Running. James P Rice Jr. reviews when done.

---

## HAND OFF — EXECUTE PAPER PIPELINE

Load prompts/04_paper_orchestrator.md.

Pass:
  PROBLEM: [full PROBLEM text above]
  DATA: No empirical data. All results derived analytically from the game model.
  SLUG: academic_publishing_2026
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS into every Author and Reviewer prompt]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every pass]

Run the full milestone pipeline: M1 -> M2 -> M3 -> M4.
Do not skip milestones. Do not open M2 until M1 is Peer Reviewer ACCEPT.
Halt only on HALT CONDITIONS.
When done write papers/academic_publishing_2026/paper.md and halt.
James P Rice Jr. reviews it.
