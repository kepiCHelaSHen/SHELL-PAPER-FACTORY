# INIT — VACCINATION AS A PUBLIC GOODS GAME
# Pre-filled. Ready to run.
# claude --dangerously-skip-permissions papers/init_vaccine_game.md

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Vaccination as a Public Goods Game: Nash Equilibria and the Free-Rider Threshold
SLUG: vaccine_game_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: Journal of Mathematical Biology
PIPELINE: PAPER

PROBLEM:
Models vaccination decisions as a public goods game where each agent chooses whether
to vaccinate (costly, private benefit + externality) or free-ride (benefits from herd
immunity). Derives the Nash equilibrium vaccination rate as a function of vaccine
efficacy, disease transmissibility (R0), and vaccine cost/risk ratio. Proves that the
Nash equilibrium vaccination rate is always below the social optimum (herd immunity
threshold), and quantifies the gap. Derives the exact subsidy needed to close the gap.
The central failure of existing models is treating vaccination as an individual decision
rather than a strategic interaction. This paper formalizes the game, derives the
equilibrium, proves the gap theorem, and gives the policymaker the exact price tag
for closing it.

FROZEN_SPEC_PARAMETERS:

PARAMETER: R0 baseline
VALUE: 15 (measles)
UNIT: dimensionless
TOLERANCE: Range 12-18 explored in sensitivity analysis
SOURCE: Anderson & May 1991 | Infectious Diseases of Humans | Oxford University Press
NOTES: R0 = 15 is the central estimate for measles. Sensitivity analysis must cover
       the full 12-18 range and show results hold across it.
DRIFT_RISK: LOW — well-established parameter

PARAMETER: Herd immunity threshold
VALUE: 1 - 1/R0
UNIT: fraction of population
TOLERANCE: exact — this is a derived quantity
SOURCE: Standard epidemiology (Anderson & May 1991)
NOTES: For R0=15, threshold = 14/15 ≈ 0.933. This is the social optimum the Nash
       equilibrium must be compared against.
DRIFT_RISK: LOW — standard result

PARAMETER: Vaccine efficacy
VALUE: 0.95 (measles vaccine)
UNIT: probability
TOLERANCE: ± 0.02
SOURCE: WHO position paper on measles vaccines (2017)
NOTES: Effective coverage = efficacy * vaccination rate. The model must distinguish
       nominal vaccination rate from effective immunization rate.
DRIFT_RISK: LOW — well-established parameter

PARAMETER: Game structure
VALUE: Symmetric 2-strategy (Vaccinate / Free-ride), N players, well-mixed population
UNIT: N/A
TOLERANCE: N/A
SOURCE: Bauch & Earn 2004 | PNAS 101(36):13391-13394
NOTES: This is the canonical vaccination game structure. The model extends Bauch &
       Earn by deriving the exact gap and the subsidy formula.
DRIFT_RISK: MEDIUM — Author may drift into SIR dynamics instead of maintaining
             game-theoretic framework throughout

PARAMETER: Cost/risk ratio
VALUE: c/r where c = vaccine cost (including side-effect risk), r = disease cost
UNIT: dimensionless ratio
TOLERANCE: explored parametrically (c/r from 0.01 to 0.5)
SOURCE: Bauch & Earn 2004; Fine & Clarkson 1986
NOTES: The Nash equilibrium vaccination rate is a decreasing function of c/r.
       The paper must derive this relationship explicitly.
DRIFT_RISK: MEDIUM — Author may fix c/r rather than deriving the full functional form

MILESTONES:

M1: Formal model setup — define agents, strategies (Vaccinate/Free-ride), payoff
    functions as explicit functions of R0, vaccine efficacy, and c/r. Establish the
    public goods structure: vaccination creates a positive externality. Show why
    this is a public goods game, not merely an optimization problem. Establish notation.

M2: Nash equilibrium derivation + gap theorem — derive the symmetric Nash equilibrium
    vaccination rate p* as a function of R0, efficacy, and c/r. Prove Theorem 1:
    p* < 1 - 1/R0 for all R0 > 1 and c/r > 0 (the gap theorem). Quantify the gap
    as a function of parameters.

M3: Subsidy mechanism + boundary conditions — derive the exact per-vaccine subsidy s*
    that makes Vaccinate a dominant strategy (or shifts Nash equilibrium to herd
    immunity threshold). Analyze boundary conditions: what happens as R0 -> 1,
    as c/r -> 0, as efficacy -> 1. Sensitivity analysis table.

M4: Full paper — Introduction (vaccination as strategic interaction), Related work
    (Bauch & Earn 2004, Fine & Clarkson 1986, Geoffard & Philipson 1997),
    Discussion (policy implications, limitations of well-mixed assumption),
    Conclusion. Self-contained Abstract.

ORACLE:
The model is valid if and only if:
1. Payoff functions are explicitly defined for both strategies as functions of
   the population vaccination rate, R0, efficacy, and c/r
2. The Nash equilibrium vaccination rate p* is derived analytically
3. The gap theorem (p* < 1 - 1/R0) is proven as a formal theorem, not observed
4. The gap is quantified as a closed-form expression
5. The subsidy s* is derived as a function of the gap

Peer Reviewer must verify: does the gap theorem follow from the payoff structure,
or is it merely stated? If stated without proof, REJECT.

KNOWN_DRIFT_RISKS:
- Reverting to SIR epidemic dynamics instead of game-theoretic framework
- Confusing individual rationality (Nash equilibrium) with social optimality
  (herd immunity threshold) — these must be formally distinguished
- Using wrong R0 values or failing to do sensitivity analysis across R0 range
- Treating vaccination as a one-shot game when sequential dynamics matter —
  state the one-shot assumption explicitly and discuss limitations
- Confusing nominal vaccination rate with effective immunization rate
  (must account for vaccine efficacy < 1)
- Skipping the subsidy derivation or leaving it as "future work"
- Making the public goods structure implicit rather than explicit —
  the externality must be formally defined and quantified
- Failing to compare with Bauch & Earn 2004 — must show what is new
- Adding epidemiological complexity (SIR compartments, age structure) that
  obscures the game-theoretic contribution — keep the disease model simple,
  the game theory rigorous
- Orphan figure references — every figure must have Python/matplotlib code.
  The paper should include at minimum:
    Figure 1: Nash equilibrium p* vs R0 for different c/r values
    Figure 2: The gap (social optimum - Nash equilibrium) vs R0
    Figure 3: Required subsidy s* vs c/r ratio

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory
Create D:\EXPERIMENTS\VACCINE_GAME\ with:
  spec/, state/, outputs/, results/raw/, results/validated/, results/final/,
  devlog/, src/, papers/, papers/vaccine_game_2026/,
  papers/vaccine_game_2026/figures/, prompts/

### Step 2 — Write CLAUDE.md
  # Vaccination as a Public Goods Game — NORTH STAR

  ## What We Are Building
  A game-theoretic model proving Nash equilibrium vaccination is always below
  herd immunity, with the exact subsidy to close the gap.

  ## The Core Claim
  The Nash equilibrium vaccination rate is provably below the herd immunity
  threshold for all R0 > 1 and positive cost/risk ratios. The gap and the
  subsidy to close it are derived in closed form.

  ## Frozen Parameters (quick reference)
  | Parameter | Value | Source |
  |-----------|-------|--------|
  | R0 (measles) | 15 | Anderson & May 1991 |
  | Herd immunity | 1 - 1/R0 | Standard epidemiology |
  | Vaccine efficacy | 0.95 | WHO |
  | Game structure | Symmetric 2-strategy, N players | Bauch & Earn 2004 |

  ## Critical Enforcements
  - Game-theoretic framework throughout — not SIR dynamics
  - Nash equilibrium derived analytically, not simulated
  - Gap theorem must be a formal proof
  - Subsidy formula derived, not approximated

### Step 3 — Write spec/frozen_spec.md
Fill from FROZEN_SPEC_PARAMETERS above. Lock date today.
Locked by: James P Rice Jr.

### Step 4 — Initialize state files
state/state_vector.md — TURN: 0, MILESTONE: M1, MODE: INIT
state/innovation_log.md — header with project name and timestamp
state/dead_ends.md — header with project name

### Step 5 — Copy all prompts from SHELL
Copy from D:\EXPERIMENTS\SHELL\prompts\ into D:\EXPERIMENTS\VACCINE_GAME\prompts\:
  04_paper_orchestrator.md
  05_author.md
  06_peer_reviewer.md
  07_editor.md
  run_milestone.md
Do NOT copy 00_init.md — SHELL-level only.

Also write prompts/turn_prompts_log.md:
  # TURN PROMPTS LOG — vaccine_game_2026
  # Every exact prompt logged here. Required for reproducibility.
  [No entries yet. First entry written at Turn 1 M1.]

### Step 5b — Write run_pipeline.ps1

Write run_pipeline.ps1 in the project root (D:\EXPERIMENTS\VACCINE_GAME\) with
the slug set to "vaccine_game_2026". Use the template from
D:\EXPERIMENTS\SHELL\prompts\00_init.md Step 15, replacing [SLUG] with
vaccine_game_2026 and [SLUG] paths with VACCINE_GAME.

### Step 6 — Write STATUS.md
Phase: INIT -> PAPER PIPELINE
Turn: 0
What Is Done: Scaffolded. Spec locked.
What Is Next: Author writes M1 (formal model setup, game structure, payoff functions).

### Step 7 — Write remaining required files

Write README.md:
  # Vaccination as a Public Goods Game
  **Author:** James P Rice Jr.
  **Target:** Journal of Mathematical Biology
  **Status:** In progress
  ## What This Is
  A game-theoretic model of vaccination decisions. Nash equilibrium is always below
  herd immunity. The gap and subsidy are derived in closed form.
  ## How to Run
  claude --dangerously-skip-permissions prompts/04_paper_orchestrator.md

Write CHAIN_PROMPT.md:
  # CHAIN PROMPT — Vaccine Game Paper | THIS FILE WINS ALL CONFLICTS
  Name: Vaccination as a Public Goods Game
  Author: James P Rice Jr.
  Core claim: Nash equilibrium vaccination rate is provably below herd immunity
  threshold. The gap and subsidy to close it are derived in closed form.
  Pipeline: PAPER — Claude-only, milestone-by-milestone gating.
  Author: Claude | Peer Reviewer: Claude | Editor: Claude
  [today] | Initialized from SHELL v3

Write SACRED_FILES.md:
  # SACRED FILES | Lock date: [today] | Locked by: James P Rice Jr.
  | File | Reason | Locked |
  |------|--------|--------|
  | spec/frozen_spec.md | Oracle. Never modify after lock. | [today] |

Write BEST_PRACTICES.md:
  # BEST PRACTICES — Vaccine Game Paper | SHELL v3 standards
  - Game-theoretic framework first — not SIR epidemic dynamics.
  - Nash equilibrium derived analytically as function of R0, efficacy, c/r.
  - Gap theorem (p* < 1 - 1/R0) must be a formal proof with explicit assumptions.
  - Subsidy formula derived in closed form from gap expression.
  - Natural enemy: Bauch & Earn 2004 — must show what is new beyond their framework.
  - Sensitivity analysis required: R0 in [12-18], c/r in [0.01-0.5], efficacy in [0.9-1.0].
  - Milestone-by-milestone. No section opens until previous is Peer Reviewer ACCEPT.
  - Every figure needs Python/matplotlib code. No orphan figure references.
  - Lean-ready proofs: all hypotheses explicit, every derivation step justified.

Write devlog/DEV_LOG.md:
  # DEVELOPMENT LOG — vaccine_game_2026
  ## [today] — Session 1
  Initialized from SHELL v3. Spec locked. All files created. Git initialized.
  Pipeline: PAPER, Claude-only, milestone-by-milestone gating.
  Models: Claude (Author) -> Claude (Peer Reviewer) -> Claude (Editor).

Write outputs/options.md:
  # OPTIONS LOG — vaccine_game_2026
  [No options yet.]

Write outputs/state_vector_backup.md:
  # STATE VECTOR BACKUP — vaccine_game_2026
  [No backups yet.]

### Step 8 — Initialize git
  cd D:\EXPERIMENTS\VACCINE_GAME
  git init
  git add -A
  git commit -m "Turn 0 | Init | vaccine_game_2026"

### Step 9 — Print confirmation and hand off:
  PROJECT INITIALIZED: vaccine_game_2026
  Spec locked. All files created. Git initialized.
  Beginning paper pipeline — M1 (Formal Model Setup) first.
  Output: papers/vaccine_game_2026/paper.md
  Running. James P Rice Jr. reviews when done.

---

## HAND OFF — EXECUTE PAPER PIPELINE

DO NOT STOP HERE. The setup is complete. Now you must execute the paper pipeline.

Read prompts/04_paper_orchestrator.md NOW and follow every instruction in it.
You are the Orchestrator. Begin at the INITIALIZE section. This is not a file
to summarize — it is your operating manual. Execute it.

YOUR INPUTS:
  PROBLEM: [the full PROBLEM text from the INPUTS section above]
  DATA: No empirical data beyond frozen spec parameters. All results derived analytically from the game-theoretic model.
  SLUG: vaccine_game_2026
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS above into every Author and Reviewer prompt]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every review pass]

BEGIN NOW. Run M1. Do not ask for confirmation. Do not summarize the orchestrator.
Execute it. Write the paper.
