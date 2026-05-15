# INIT — BAYESIAN MODEL OF THE REPLICATION CRISIS (v3 — ASSAY-Integrated)
# EXECUTE IMMEDIATELY. Do not summarize, analyze, or ask questions.
# Read the INPUTS below, then execute the SETUP SEQUENCE step by step.
# Load prompts/00_init.md for the setup procedure, then run it with these inputs.
# This is not a document to review — it is a set of instructions to follow NOW.

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: A Bayesian Model of the Replication Crisis: Prior Odds, Publication Bias, and the Positive Predictive Value of Science
SLUG: REPLICATION_CRISIS_2026
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
    disciplines onto the PPV surface using ASSAY-computed phi estimates and
    empirical estimates of R and power. Use ASSAY failure rates and phi MLE
    values directly — do NOT invent discipline-level parameters. Boundary
    conditions: phi -> 1 (no bias), R -> 0 (pure exploration),
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
4. The discipline mapping uses ASSAY-computed values for failure rates and phi
   estimates, supplemented by cited empirical values for R and power
5. The paper clearly distinguishes its contribution from Ioannidis (2005)

Peer Reviewer must verify: is the critical bias threshold a proven theorem,
or is it merely observed from a plot? If observed without proof, REJECT.
Peer Reviewer must also verify: does the discipline mapping use ASSAY-computed
phi values, or are they invented? If invented, REJECT.

---

## ASSAY EVIDENCE

The following ASSAY integration blocks contain pre-computed empirical values.
The Author MUST read these files and use the computed values directly.

### ASSAY Report 1: PHI_EST (Publication Bias Estimation)
PATH: C:\PROJECTS\ASSAY\reports\PHI_EST_2026-05-14_001\integration_block.yaml
REPORT_ID: ASSAY-PHI-EST-2026-05-14-001
DATA SOURCE: Open Science Collaboration (2015), Science 349(6251), aac4716
CONTAINS:
  - Overall replication failure rate: 0.6304 [95% CI: 0.528, 0.722], N=92
  - Social psychology failure rate: 0.7500 [95% CI: 0.618, 0.848], N=52
  - Cognitive psychology failure rate: 0.4750 [95% CI: 0.329, 0.625], N=40
  - phi MLE (overall): 7.39 (step-function selection model, N=92)
  - phi sensitivity at base rate 0.10: 10.0
AVAILABLE FIGURES (3):
  - figure_1_forest_plot.png — Forest plot of replication outcomes
  - figure_2_bootstrap_social.png — Bootstrap distribution for social psych
  - figure_3_sensitivity.png — Sensitivity curves across base rate assumptions

### ASSAY Report 2: PHI_CROSSFIELD (Cross-Field Comparison)
PATH: C:\PROJECTS\ASSAY\reports\PHI_CROSSFIELD_2026_2026-05-15_001\integration_block.yaml
REPORT_ID: ASSAY-PHI-CROSSFIELD-2026-05-15-001
DATA SOURCES: OSC 2015, Camerer et al. 2016 (economics), Camerer et al. 2018 (social science)
CONTAINS:
  - Overall failure rate (3 fields pooled): 0.5725 [95% CI: 0.487, 0.654], N=131
  - Psychology failure rate: 0.6304, N=92
  - Economics failure rate: 0.3889 [95% CI: 0.203, 0.614], N=18
  - Social science failure rate: 0.4762 [95% CI: 0.283, 0.676], N=21
  - phi MLE by field: psychology 7.39, economics 12.22, social science 10.48
  - phi MAP by field: psychology 27.83, economics 7.33, social science 10.82
  - Cross-field heterogeneity test: chi-squared=4.5371, permutation p=0.0993
AVAILABLE FIGURES (3):
  - figure_1_forest_plot.png — Cross-field forest plot
  - figure_2_bootstrap_distributions.png — Bootstrap distributions by field
  - figure_3_sensitivity.png — Cross-field sensitivity analysis

KEY USAGE INSTRUCTIONS FOR AUTHOR:
  - The discipline mapping (M3) MUST use the ASSAY phi estimates (MLE and MAP)
    as the empirical anchor points. Do NOT invent phi values for disciplines.
  - Report BOTH MLE and MAP estimates to show prior sensitivity.
  - The cross-field heterogeneity result (p=0.0993) is suggestive but NOT
    significant after correction. Report honestly — do not overclaim.
  - All CIs must be reported with their method (Wilson score, bootstrap BCa).
  - Cite the ASSAY report ID alongside the original data source.

---

## DOMAIN CONSTRAINTS

The Author MUST enforce these parameter ranges. Any value outside these ranges
is a model error that must be flagged, not silently used.

| Parameter | Valid Range | Justification |
|-----------|------------|---------------|
| phi | phi >= 1 | phi=1 means no bias; phi < 1 is undefined (cannot have anti-publication bias in this model) |
| R (prior odds) | R > 0 | R = P(true)/P(false); must be positive. Practical range: 0.001 (exploratory genomics) to 1.0 (pre-registered RCTs) |
| alpha | alpha in (0, 1) | False positive rate; standard values 0.005, 0.01, 0.05 |
| 1-beta (power) | (0, 1) | Power must be strictly between 0 and 1; boundary values degenerate |
| PPV | [0, 1] | Output is a probability; verify all computed PPV values are in [0,1] |
| phi* (critical threshold) | phi* = R/alpha > 0 | Derived quantity; for psychology R=0.10: phi* = 0.10/0.05 = 2.0 |

FLAG CONDITIONS:
- If any computed PPV is negative or exceeds 1: MODEL ERROR
- If phi* < 1 for any parameter combination: VERIFY — this means even phi=1 (no bias) gives PPV < 0.5
- If a discipline's empirical phi exceeds phi* by 3x or more: HIGHLIGHT as extreme case

---

## CALIBRATION INSTRUCTIONS

The Author MUST perform these specific model-data comparisons using ASSAY values:

1. PRIMARY CALIBRATION: Set phi=7.39 (ASSAY phi MLE for psychology,
   ASSAY-PHI-EST-2026-05-14-001) in the PPV formula. Compute
   phi* = R/alpha for psychology (R=0.10, alpha=0.05): phi* = 2.0.
   Show that phi=7.39 > phi*=2.0 confirms psychology operates above the
   critical threshold. Compute PPV at phi=7.39: PPV = 0.5*0.10 / (0.5*0.10 + 0.05*7.39) = 0.05/0.4195 = 0.119.
   Report: "At typical psychology parameters (R=0.10, power=0.5, alpha=0.05),
   the ASSAY-estimated phi=7.39 implies PPV = 11.9% — fewer than 1 in 8
   published positive findings are true."

2. CROSS-FIELD COMPARISON: Repeat for economics (phi MLE=12.22) and
   social science (phi MLE=10.48). Note that economics has HIGHER phi
   but LOWER failure rate (0.3889 vs 0.6304). Explain: higher R in
   economics compensates for higher phi. This is the PPV surface at work.

3. SENSITIVITY: Report phi MAP values alongside MLE (psychology: 27.83,
   economics: 7.33, social science: 10.82) to show sensitivity to priors.
   Note the MLE-MAP divergence for psychology (7.39 vs 27.83) and discuss.

4. THRESHOLD CHECK: For each field, compute phi* and compare to observed phi.
   If phi > phi* in all fields, the crisis is structural, not anomalous.

---

# === STEELMAN REVISION BRIEF (from runs 1-2) ===
# The next run MUST address every item.

KNOWN_DRIFT_RISKS:
- DO NOT use illustrative or assumed parameter values when ASSAY-computed values
  are available. Every phi estimate, failure rate, and CI in the ASSAY integration
  blocks is computed from real data. Use them.
- Every figure in the paper should use ASSAY-computed data where applicable.
  The ASSAY reports include 6 pre-rendered figures — reference or reproduce them.
- ASSAY data is REAL — computed from actual replication study data (OSC 2015,
  Camerer et al. 2016, 2018). Cite the specific ASSAY report ID and data source.
  Do not round or approximate ASSAY values.
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

# === CROSS-PAPER FINDINGS (from STEELMAN_FINDINGS.md) ===
# These are systemic Claude Author tendencies caught across multiple papers.
# Address ALL of them proactively.

- [F-005] POLICY LANGUAGE OVERSHOOTS MODEL SCOPE — Author writes policy claims
  stronger than the math supports. For this paper: "pre-registration fixes the
  crisis" must be scoped to "pre-registration reduces phi" with explicit bounds.
  Do not claim the model proves more than it does. The model says high phi kills
  PPV — it does not say which interventions reduce phi by how much.

- [F-002] "ILLUSTRATIVE" COMPONENT THAT IS LOAD-BEARING — Author tends to
  downplay the novel contribution as "one of several extensions." The phi
  parameter and critical threshold phi* ARE the contribution. Do not present
  phi as optional or illustrative. It is the theorem.

- [F-036/F-024] FIGURES CODE-ONLY — Author generates matplotlib code but does
  not render or embed figures. All 3 figures must appear as rendered output in
  the paper, not just code blocks. Code goes in appendix or supplementary.

- [F-015] MISSING DATA/CODE AVAILABILITY STATEMENT — PNAS requires a data
  availability statement. Include: "Replication data from Open Science
  Collaboration (2015), Camerer et al. (2016, 2018). ASSAY-computed statistics
  available at [ASSAY report IDs]. Figure code available at [repository]."

- [F-006] NOTATION OVERLOAD — Author reuses symbols across different meanings.
  In this paper: alpha is the false positive rate ONLY. Do not reuse alpha for
  anything else. Keep R, phi, alpha, beta strictly single-meaning throughout.

- [F-037] RELATED WORK SECTION TOO LONG — Author writes 1,800+ word Related
  Work sections. PNAS Perspective format is short. Related Work should be
  ~500 words max, integrated into Introduction, not a standalone section.

- [F-014] EM DASH IN TITLE — Journal submission systems mangle em dashes.
  Use a colon or subtitle format for the title.

- [DE-015/058/065/080] SCOPE DISGUISE — Author presents limitations as "future
  work" or "open problems." State limitations as limitations. Examples for this
  paper: "the model assumes study independence" is a limitation, not an open
  problem. "We do not model p-hacking" is a scope choice, not future work.

- [DE-038] PLACEHOLDER VALUES IN TABLES — Author writes "[from code execution]"
  instead of actual numbers. The discipline mapping table (M3) MUST have real
  values from ASSAY integration blocks and cited sources. No placeholders.

- [F-034] DO NOT CLAIM LEAN-READINESS — Author tends to claim proofs are
  "structured for Lean formalization" when they are not formalized. This is a
  PNAS Perspective, not a proof theory paper. Do not mention Lean.

# === LESSONS FROM PRIOR RUNS (v1/v2 Steelman feedback, distilled) ===

- PHI DEFINITION MUST BE CONSISTENT — Define phi as the effective false
  positive inflation factor (alpha_eff = alpha * phi) from the start. Do NOT
  define phi as a publication probability ratio that then gets redefined. If
  you show that a naive publication filter cancels (Proposition 0), make clear
  that phi captures within-study inflation (selective reporting, multiple
  testing, analytic flexibility), not the between-study file drawer. One
  coherent definition throughout.

- THEOREM FRAMING — phi* = R/alpha is elementary algebra. Do not frame it as
  a "deep theorem." Frame it as a "closed-form critical boundary" whose value
  is in the interpretation and the discipline mapping, not in the proof
  difficulty. The contribution is making the implicit explicit and actionable,
  not proving something hard.

- SCOPE PHI HONESTLY — phi conflates multiple mechanisms (file drawer,
  selective reporting, p-hacking). Acknowledge this explicitly as a modeling
  choice. State that phi captures the net effect and that decomposing it
  requires empirical data the model does not provide.

- CONDITION THE DISCIPLINE MAPPING — The ASSAY-computed phi estimates are
  MODEL-DEPENDENT (selection model MLE). Report them as such: "Under the
  step-function selection model, the MLE phi for psychology is 7.39
  (ASSAY-PHI-EST-2026-05-14-001)." Do not present model estimates as
  established facts. Report BOTH MLE and MAP estimates.

- IOANNIDIS u* HAS A CLOSED FORM — DO NOT CLAIM OTHERWISE. Setting
  PPV_Ioannidis = 0.5 and solving for u yields:
  u* = ((1-beta)*R - alpha) / ((1-beta) - beta*R)
  This is closed-form. The paper MUST NOT claim phi "enables" a threshold
  that was "previously impossible." Derive u* explicitly in the paper,
  compare it to phi* = R/alpha, and argue for phi on the correct grounds:
  phi* is simpler, more interpretable, isolates the actionable parameter
  (false-positive inflation), and decomposes into policy levers. The
  contribution is interpretability and applied value, not mathematical
  novelty over Ioannidis.

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory (auto-versioned)
Resolve the project directory using auto-versioning:
1. List all existing directories matching C:\PROJECTS\SHELL\papers\REPLICATION_CRISIS_2026_*
2. If none exist: use REPLICATION_CRISIS_2026_[TODAY]_001
3. If some exist: find the highest sequence number, increment by 1,
   use REPLICATION_CRISIS_2026_[TODAY]_[NEXT_SEQ]
Store as RESOLVED_DIR. Use RESOLVED_DIR for ALL paths below.

Create RESOLVED_DIR with subdirectories:
  figures/, outputs/, results/raw/, results/final/,
  devlog/, prompts/

### Step 2 — Write CLAUDE.md
  # Bayesian Model of the Replication Crisis — NORTH STAR

  ## What We Are Building
  A Bayesian model extending Ioannidis (2005) with a publication bias parameter,
  proving a critical threshold beyond which most published findings are false.

  ## The Core Claim
  There exists a critical publication bias factor phi* above which PPV < 50%
  regardless of statistical power. This is derived as a theorem, not observed.

  ## ASSAY Data Available
  Two ASSAY reports provide real phi estimates and failure rates:
  - PHI_EST_2026-05-14_001: phi MLE = 7.39, failure rates by subfield
  - PHI_CROSSFIELD_2026_2026-05-15_001: phi by field (psych, econ, social sci)
  USE THESE VALUES. Do not invent discipline-level parameters.

  ## Frozen Parameters (quick reference)
  | Parameter | Value | Source |
  |-----------|-------|--------|
  | Alpha | 0.05 | Fisher/Neyman-Pearson |
  | PPV formula | (1-beta)*R / ((1-beta)*R + alpha*phi) | Ioannidis extended |
  | Prior odds R | 0.001-1.0 by field | Ioannidis 2005 Table 4 |
  | Bias factor phi | 1-50 (parametric); MLE 7.39 (ASSAY) | Novel + ASSAY |

  ## Critical Enforcements
  - phi parameter is the contribution — not a rehash of Ioannidis
  - Critical threshold theorem must be formally proven
  - Discipline mapping must use ASSAY-computed phi values + cited empirical R
  - PPV is not a p-value — keep the distinction sharp

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
  # TURN PROMPTS LOG — REPLICATION_CRISIS_2026
  # Every exact prompt logged here. Required for reproducibility.
  [No entries yet. First entry written at Turn 1 M1.]

### Step 5b — Write run_pipeline.ps1

Write run_pipeline.ps1 in the project root (RESOLVED_DIR) with
the slug set to "REPLICATION_CRISIS_2026". Use the template from
C:\PROJECTS\SHELL\prompts\00_init.md Step 15, replacing [SLUG] with
REPLICATION_CRISIS_2026 and [SLUG] paths with REPLICATION_CRISIS_2026.

### Step 6 — Write STATUS.md
Phase: INIT -> PAPER PIPELINE
Turn: 0
What Is Done: Scaffolded. Spec locked. ASSAY integration blocks linked.
What Is Next: Author writes M1 (Bayesian framework, PPV definition, phi parameter).

### Step 7 — Write remaining required files

Write README.md:
  # A Bayesian Model of the Replication Crisis
  **Author:** James P Rice Jr.
  **Target:** PNAS (Perspective)
  **Status:** In progress
  **ASSAY Data:** PHI_EST + PHI_CROSSFIELD reports (real replication data)
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
  ASSAY: PHI_EST + PHI_CROSSFIELD integration blocks provide real phi estimates.
  Pipeline: PAPER — Claude-only, milestone-by-milestone gating.
  Author: Claude | Peer Reviewer: Claude | Editor: Claude
  [today] | Initialized from SHELL v6.2 (ASSAY-integrated)

Write SACRED_FILES.md:
  # SACRED FILES | Lock date: [today] | Locked by: James P Rice Jr.
  | File | Reason | Locked |
  |------|--------|--------|
  | frozen_spec.md | Oracle. Never modify after lock. | [today] |

Write BEST_PRACTICES.md:
  # BEST PRACTICES — Replication Crisis Paper | SHELL v6.2 + ASSAY
  - PPV formula with phi is the contribution — not a rehash of Ioannidis.
  - Critical bias threshold must be a formal theorem with closed-form phi*.
  - Discipline mapping uses ASSAY-computed phi values (MLE + MAP) and cited R.
  - PPV is not a p-value. Maintain the distinction throughout.
  - Natural enemy: Ioannidis 2005 — must show what is new beyond that paper.
  - ASSAY values are authoritative — do not round, approximate, or replace with
    illustrative estimates.
  - Sensitivity analysis required: alpha in {0.005, 0.01, 0.05}, R in [0.001-1.0].
  - Milestone-by-milestone. No section opens until previous is Peer Reviewer ACCEPT.
  - Every figure needs Python/matplotlib code. No orphan figure references.

Write devlog/DEV_LOG.md:
  # DEVELOPMENT LOG — REPLICATION_CRISIS_2026
  ## [today] — Session 1
  Initialized from SHELL v6.2 (ASSAY-integrated). Spec locked. All files created.
  ASSAY reports linked: PHI_EST_2026-05-14_001, PHI_CROSSFIELD_2026_2026-05-15_001.
  Pipeline: PAPER, Claude-only, milestone-by-milestone gating.
  Models: Claude (Author) -> Claude (Peer Reviewer) -> Claude (Editor).

Write outputs/options.md:
  # OPTIONS LOG — REPLICATION_CRISIS_2026
  [No options yet.]

Write outputs/state_vector_backup.md:
  # STATE VECTOR BACKUP — REPLICATION_CRISIS_2026
  [No backups yet.]

### Step 8 — Initialize git
  cd RESOLVED_DIR
  git init
  git add -A
  git commit -m "Turn 0 | Init | REPLICATION_CRISIS_2026 (ASSAY-integrated v3)"

### Step 9 — Print confirmation and hand off:
  PROJECT INITIALIZED: REPLICATION_CRISIS_2026
  Spec locked. All files created. Git initialized.
  ASSAY integration blocks linked: PHI_EST + PHI_CROSSFIELD.
  Beginning paper pipeline — M1 (Bayesian Framework + Definitions) first.
  Output: papers/REPLICATION_CRISIS_2026/paper.md
  Running. James P Rice Jr. reviews when done.

---

## HAND OFF — EXECUTE PAPER PIPELINE

DO NOT STOP HERE. The setup is complete. Now you must execute the paper pipeline.

Read prompts/04_paper_orchestrator.md NOW and follow every instruction in it.
You are the Orchestrator. Begin at the INITIALIZE section. This is not a file
to summarize — it is your operating manual. Execute it.

YOUR INPUTS:
  PROBLEM: [the full PROBLEM text from the INPUTS section above]
  DATA: ASSAY integration blocks at:
    - C:\PROJECTS\ASSAY\reports\PHI_EST_2026-05-14_001\integration_block.yaml
    - C:\PROJECTS\ASSAY\reports\PHI_CROSSFIELD_2026_2026-05-15_001\integration_block.yaml
    Read these files and use the computed values. Do not use illustrative estimates
    for any quantity that ASSAY has computed. Key values:
      Overall failure rate: 0.6304 [0.528, 0.722], N=92
      Social psych failure: 0.7500 [0.618, 0.848], N=52
      Cognitive failure: 0.4750 [0.329, 0.625], N=40
      Cross-field pooled: 0.5725 [0.487, 0.654], N=131
      Psychology failure: 0.6304, Economics: 0.3889, Social science: 0.4762
      phi MLE: psychology 7.39, economics 12.22, social science 10.48
      phi MAP: psychology 27.83, economics 7.33, social science 10.82
      Cross-field heterogeneity: chi-squared=4.5371, permutation p=0.0993
      6 pre-rendered figures available in the ASSAY report directories.
  SLUG: REPLICATION_CRISIS_2026
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS above into every Author and Reviewer prompt]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every review pass]

BEGIN NOW. Run M1. Do not ask for confirmation. Do not summarize the orchestrator.
Execute it. Write the paper.
