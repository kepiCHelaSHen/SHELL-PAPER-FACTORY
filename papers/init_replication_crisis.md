# INIT — BAYESIAN MODEL OF THE REPLICATION CRISIS
# Pre-filled. Ready to run.
# claude --dangerously-skip-permissions papers/init_replication_crisis.md

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: A Bayesian Model of the Replication Crisis: Prior Odds, Publication Bias, and the Positive Predictive Value of Science
SLUG: replication_crisis_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: Proceedings of the National Academy of Sciences (Perspective)
PIPELINE: PAPER

PROBLEM:
Extends Ioannidis (2005) by building a full Bayesian model where the positive
predictive value (PPV) of a published finding depends on three parameters: prior
odds that a tested hypothesis is true, statistical power, and publication bias
factor. Derives PPV as a closed-form function and proves there exists a critical
publication bias factor above which PPV < 50% regardless of statistical power.
Maps multiple disciplines onto this surface. The central contribution is the
critical bias threshold theorem: there is a formal boundary in parameter space
beyond which most published findings are false, and no amount of statistical
power can fix it. This is not a rehash of Ioannidis — it is the theorem he
described informally, now proven.

FROZEN_SPEC_PARAMETERS:

PARAMETER: PPV formula (extended)
VALUE: PPV = (1-beta)*R / ((1-beta)*R + alpha*phi)
UNIT: probability
TOLERANCE: exact — this is the defining equation of the model
SOURCE: Ioannidis 2005 extended with publication bias factor phi
NOTES: R = prior odds, beta = Type II error rate (1-beta = power), alpha = Type I
       error rate, phi = publication bias factor. When phi=1, reduces to Ioannidis.
       The extension is the phi parameter and the critical threshold theorem.
DRIFT_RISK: HIGH — Author may reproduce Ioannidis without the phi extension.
             The phi term is the entire contribution. Enforce it.

PARAMETER: Alpha (false positive rate)
VALUE: 0.05
UNIT: probability
TOLERANCE: exact (conventional threshold)
SOURCE: Fisher/Neyman-Pearson convention
NOTES: Alpha = 0.05 is the standard. Sensitivity analysis should also explore
       alpha = 0.01 and alpha = 0.005 (Benjamin et al. 2018 proposal).
DRIFT_RISK: LOW — standard parameter

PARAMETER: Publication bias factor phi
VALUE: Ratio of probability of publishing a positive result to probability of
       publishing a negative result. phi >= 1 (phi=1 means no bias).
UNIT: dimensionless ratio
TOLERANCE: explored parametrically (phi from 1 to 50)
SOURCE: Novel parameter — this paper's contribution
NOTES: This is the key innovation. phi captures the file drawer effect as a single
       parameter. The critical threshold theorem gives the phi* above which
       PPV < 0.5 regardless of power. Must be derived, not estimated.
DRIFT_RISK: HIGH — Author may treat phi as empirical rather than deriving
             the critical threshold formally

PARAMETER: Prior odds R
VALUE: Varies by field — psychology ~0.1, clinical trials ~0.5, exploratory
       genomics ~0.001, pre-registered RCTs ~1.0
UNIT: dimensionless ratio (R = P(true)/P(false))
TOLERANCE: order of magnitude by field
SOURCE: Ioannidis 2005 Table 4; Dreber et al. 2015
NOTES: The discipline mapping (M3) must place at least 5 fields on the
       PPV surface as a function of R and phi. This is the applied payoff.
DRIFT_RISK: MEDIUM — Author may pick convenient R values instead of citing sources

PARAMETER: Statistical power (1-beta)
VALUE: Varies — median in psychology ~0.5, clinical trials ~0.8
UNIT: probability
TOLERANCE: explored parametrically (0.1 to 0.99)
SOURCE: Cohen 1962; Button et al. 2013 | Nature Reviews Neuroscience 14:365-376
NOTES: The critical bias threshold theorem must show that for any power level,
       there exists a phi* that makes PPV < 0.5. Power alone cannot save you.
DRIFT_RISK: MEDIUM — Author may overstate the role of power as a fix

MILESTONES:

M1: Bayesian framework + definitions — define PPV, prior odds R, power,
    publication bias factor phi. Derive the extended PPV formula with phi.
    Show Ioannidis (2005) as a special case (phi=1). Establish notation.
    Clearly state what is new vs. what is Ioannidis.

M2: PPV derivation + critical threshold theorem — derive PPV as a function of
    R, power, and phi. Prove Theorem 1: for any statistical power (1-beta) < 1,
    there exists a critical phi* such that PPV < 0.5 for all phi > phi*.
    Derive phi* in closed form. Show phi* is independent of sample size.

M3: Discipline mapping + boundary conditions — map at least 5 scientific
    disciplines onto the PPV surface using empirical estimates of R, power,
    and phi. Identify which fields are above vs. below the critical threshold.
    Boundary conditions: phi -> 1 (no bias), R -> 0 (pure exploration),
    power -> 1 (perfect power). Sensitivity analysis table.

M4: Full paper — Introduction (the replication crisis as a parameter estimation
    problem), Related work (Ioannidis 2005, Benjamin et al. 2018, Open Science
    Collaboration 2015), Discussion (policy implications — pre-registration,
    registered reports, replication incentives), Conclusion.
    Self-contained Abstract.

ORACLE:
The model is valid if and only if:
1. The PPV formula with phi is correctly derived from Bayes' theorem
2. The critical publication bias threshold phi* is proven as a formal theorem
3. phi* is given in closed form as a function of R, alpha, and power
4. The discipline mapping uses cited empirical values, not invented ones
5. The paper clearly distinguishes its contribution from Ioannidis (2005)

Peer Reviewer must verify: is the critical bias threshold a proven theorem,
or is it merely observed from a plot? If observed without proof, REJECT.

KNOWN_DRIFT_RISKS:
- Reproducing Ioannidis (2005) without extending it — the phi parameter and
  critical threshold theorem are the entire contribution
- Confusing PPV with p-value — PPV is a property of the published literature,
  not of any individual study
- Not deriving the critical bias threshold as a formal theorem — must be proven,
  not just plotted
- Using made-up prior odds R for different fields — must cite sources
  (Ioannidis 2005 Table 4, Dreber et al. 2015, Open Science Collaboration 2015)
- Overstating statistical power as a solution — the critical threshold theorem
  shows phi can overwhelm any power level
- Treating publication bias as binary (publish/don't publish) when phi is a
  continuous ratio — keep the continuous formulation
- Adding unnecessary complexity (multiple testing, p-hacking, HARKing) that
  obscures the clean three-parameter model — keep it tight
- Failing to state policy implications — pre-registration, registered reports,
  and replication incentives must be discussed as mechanisms to reduce phi
- Orphan figure references — every figure must have Python/matplotlib code.
  The paper should include at minimum:
    Figure 1: PPV surface as a function of R and phi (fixed power = 0.8)
    Figure 2: Critical threshold phi* as a function of R for different alpha
    Figure 3: Discipline map — 5+ fields plotted on the PPV surface

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory
Create D:\EXPERIMENTS\REPLICATION_CRISIS\ with:
  spec/, state/, outputs/, results/raw/, results/validated/, results/final/,
  devlog/, src/, papers/, papers/replication_crisis_2026/,
  papers/replication_crisis_2026/figures/, prompts/

### Step 2 — Write CLAUDE.md
  # Bayesian Model of the Replication Crisis — NORTH STAR

  ## What We Are Building
  A Bayesian model extending Ioannidis (2005) with a publication bias parameter,
  proving a critical threshold beyond which most published findings are false.

  ## The Core Claim
  There exists a critical publication bias factor phi* above which PPV < 50%
  regardless of statistical power. This is derived as a theorem, not observed.

  ## Frozen Parameters (quick reference)
  | Parameter | Value | Source |
  |-----------|-------|--------|
  | Alpha | 0.05 | Fisher/Neyman-Pearson |
  | PPV formula | (1-beta)*R / ((1-beta)*R + alpha*phi) | Ioannidis extended |
  | Prior odds R | 0.001-1.0 by field | Ioannidis 2005 Table 4 |
  | Bias factor phi | 1-50 (parametric) | Novel parameter |

  ## Critical Enforcements
  - phi parameter is the contribution — not a rehash of Ioannidis
  - Critical threshold theorem must be formally proven
  - Discipline mapping must use cited empirical values
  - PPV is not a p-value — keep the distinction sharp

### Step 3 — Write spec/frozen_spec.md
Fill from FROZEN_SPEC_PARAMETERS above. Lock date today.
Locked by: James P Rice Jr.

### Step 4 — Initialize state files
state/state_vector.md — TURN: 0, MILESTONE: M1, MODE: INIT
state/innovation_log.md — header with project name and timestamp
state/dead_ends.md — header with project name

### Step 5 — Copy all prompts from SHELL
Copy from D:\EXPERIMENTS\SHELL\prompts\ into D:\EXPERIMENTS\REPLICATION_CRISIS\prompts\:
  04_paper_orchestrator.md
  05_author.md
  06_peer_reviewer.md
  07_editor.md
  run_milestone.md
Do NOT copy 00_init.md — SHELL-level only.

Also write prompts/turn_prompts_log.md:
  # TURN PROMPTS LOG — replication_crisis_2026
  # Every exact prompt logged here. Required for reproducibility.
  [No entries yet. First entry written at Turn 1 M1.]

### Step 5b — Write run_pipeline.ps1

Write run_pipeline.ps1 in the project root (D:\EXPERIMENTS\REPLICATION_CRISIS\) with
the slug set to "replication_crisis_2026". Use the template from
D:\EXPERIMENTS\SHELL\prompts\00_init.md Step 15, replacing [SLUG] with
replication_crisis_2026 and [SLUG] paths with REPLICATION_CRISIS.

### Step 6 — Write STATUS.md
Phase: INIT -> PAPER PIPELINE
Turn: 0
What Is Done: Scaffolded. Spec locked.
What Is Next: Author writes M1 (Bayesian framework, PPV definition, phi parameter).

### Step 7 — Write remaining required files

Write README.md:
  # A Bayesian Model of the Replication Crisis
  **Author:** James P Rice Jr.
  **Target:** PNAS (Perspective)
  **Status:** In progress
  ## What This Is
  A Bayesian model proving a critical publication bias threshold beyond which
  most published findings are false, regardless of statistical power.
  ## How to Run
  claude --dangerously-skip-permissions prompts/04_paper_orchestrator.md

Write CHAIN_PROMPT.md:
  # CHAIN PROMPT — Replication Crisis Paper | THIS FILE WINS ALL CONFLICTS
  Name: A Bayesian Model of the Replication Crisis
  Author: James P Rice Jr.
  Core claim: Critical publication bias threshold phi* exists above which
  PPV < 50% regardless of power. Formally proven.
  Pipeline: PAPER — Claude-only, milestone-by-milestone gating.
  Author: Claude | Peer Reviewer: Claude | Editor: Claude
  [today] | Initialized from SHELL v3

Write SACRED_FILES.md:
  # SACRED FILES | Lock date: [today] | Locked by: James P Rice Jr.
  | File | Reason | Locked |
  |------|--------|--------|
  | spec/frozen_spec.md | Oracle. Never modify after lock. | [today] |

Write BEST_PRACTICES.md:
  # BEST PRACTICES — Replication Crisis Paper | SHELL v3 standards
  - PPV formula with phi is the contribution — not a rehash of Ioannidis.
  - Critical bias threshold must be a formal theorem with closed-form phi*.
  - Discipline mapping uses cited empirical values for R, power, phi.
  - PPV is not a p-value. Maintain the distinction throughout.
  - Natural enemy: Ioannidis 2005 — must show what is new beyond that paper.
  - Sensitivity analysis required: alpha in {0.005, 0.01, 0.05}, R in [0.001-1.0].
  - Milestone-by-milestone. No section opens until previous is Peer Reviewer ACCEPT.
  - Every figure needs Python/matplotlib code. No orphan figure references.
  - Lean-ready proofs: all hypotheses explicit, every derivation step justified.

Write devlog/DEV_LOG.md:
  # DEVELOPMENT LOG — replication_crisis_2026
  ## [today] — Session 1
  Initialized from SHELL v3. Spec locked. All files created. Git initialized.
  Pipeline: PAPER, Claude-only, milestone-by-milestone gating.
  Models: Claude (Author) -> Claude (Peer Reviewer) -> Claude (Editor).

Write outputs/options.md:
  # OPTIONS LOG — replication_crisis_2026
  [No options yet.]

Write outputs/state_vector_backup.md:
  # STATE VECTOR BACKUP — replication_crisis_2026
  [No backups yet.]

### Step 8 — Initialize git
  cd D:\EXPERIMENTS\REPLICATION_CRISIS
  git init
  git add -A
  git commit -m "Turn 0 | Init | replication_crisis_2026"

### Step 9 — Print confirmation and hand off:
  PROJECT INITIALIZED: replication_crisis_2026
  Spec locked. All files created. Git initialized.
  Beginning paper pipeline — M1 (Bayesian Framework + Definitions) first.
  Output: papers/replication_crisis_2026/paper.md
  Running. James P Rice Jr. reviews when done.

---

## HAND OFF — EXECUTE PAPER PIPELINE

Load prompts/04_paper_orchestrator.md.

Pass:
  PROBLEM: [full PROBLEM text above]
  DATA: No empirical data beyond cited field-level estimates in frozen spec.
        All results derived analytically from the Bayesian model.
  SLUG: replication_crisis_2026
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS into every Author and Reviewer prompt]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every pass]

Run the full milestone pipeline: M1 -> M2 -> M3 -> M4.
Do not skip milestones. Do not open M2 until M1 is Peer Reviewer ACCEPT.
Halt only on HALT CONDITIONS.
When done write papers/replication_crisis_2026/paper.md and halt.
James P Rice Jr. reviews it.
