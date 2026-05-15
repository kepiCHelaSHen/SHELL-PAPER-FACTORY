# INIT — PHARMACEUTICAL SPENDING CONCENTRATION: PARETO TAILS AND THE LIMITS OF PARAMETRIC MODELS (v3 — ASSAY-Integrated)
# EXECUTE IMMEDIATELY. Do not summarize, analyze, or ask questions.
# Read the INPUTS below, then execute the SETUP SEQUENCE step by step.
# Load prompts/00_init.md for the setup procedure, then run it with these inputs.
# This is not a document to review — it is a set of instructions to follow NOW.

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Pharmaceutical Spending Concentration: Pareto Tails, Lorenz Calibration, and the Limits of Parametric Models in Medicare Part D
SLUG: DRUG_SPENDING_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: Journal of Health Economics
PIPELINE: PAPER

PROBLEM:
Models the distribution of pharmaceutical spending as a Pareto-family process
where a small number of blockbuster drugs capture the majority of spending.
Derives a Lorenz curve L(p) = 1-(1-p)^beta from Pareto assumptions and
calibrates against CMS Medicare Part D data (3,206 drugs, $274B total).
CRITICAL NEGATIVE RESULT: The Pareto model predicts Gini = 0.8557 but the
empirical Gini = 0.9023. The model UNDERESTIMATES concentration by 0.047.
The implied alpha parameters (alpha_q=0.69, alpha_mu=1.30) are outside the
model's domain requirement (alpha > 2 for finite variance). The calibration
FAILS structurally. This negative result constrains the model space and
points toward log-normal body + Pareto tail as a richer specification.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Empirical Gini coefficient
VALUE: 0.9023 [95% CI: 0.884, 0.917], N=3,206 drugs
UNIT: dimensionless [0,1]
SOURCE: ASSAY-CMS-DRUG-SPENDING-2026-2026-05-15-001
DRIFT_RISK: LOW — ASSAY-computed

PARAMETER: Top 10 drugs spending share
VALUE: 25.96% [95% CI: 19.74%, 37.78%]
SOURCE: ASSAY-CMS-DRUG-SPENDING-2026-2026-05-15-001
NOTE: Wide CI reflects sensitivity to individual blockbuster drugs

PARAMETER: Top 50 drugs spending share
VALUE: 51.08% [95% CI: 44.63%, 60.46%]
SOURCE: ASSAY-CMS-DRUG-SPENDING-2026-2026-05-15-001

PARAMETER: Brand spending share
VALUE: 90.95%
SOURCE: ASSAY-CMS-DRUG-SPENDING-2026-2026-05-15-001
NOTE: Classification heuristic (Brnd_Name != Gnrc_Name); no CI

PARAMETER: Lorenz exponent beta
VALUE: 0.0778 [95% CI: 0.066, 0.092]
SOURCE: ASSAY-CMS-DRUG-SPENDING-HARDENED-2026-05-15-001
NOTE: L2 minimization of L(p)=1-(1-p)^beta against empirical Lorenz

PARAMETER: Implied alpha_product
VALUE: 1.0843 [95% CI: 1.0707, 1.1018]
SOURCE: ASSAY-CMS-DRUG-SPENDING-HARDENED-2026-05-15-001
NOTE: alpha_product = alpha_mu * alpha_q = 1/(1-beta). BELOW theoretical
      requirement of alpha > 2 for finite variance.

PARAMETER: Lorenz L2 fit error
VALUE: 0.0606 [95% CI: 0.0528, 0.0705]
SOURCE: ASSAY-CMS-DRUG-SPENDING-HARDENED-2026-05-15-001
NOTE: Entire CI above 0.05 — model does NOT fit well

PARAMETER: Theoretical Gini (from Pareto)
VALUE: 0.8557
SOURCE: ASSAY-CMS-DRUG-SPENDING-HARDENED-2026-05-15-001
NOTE: Theoretical Gini = 2/(beta+1)-1. Underestimates empirical by 0.047.

PARAMETER: alpha_q (claims tail)
VALUE: 0.6909 (Pareto MLE at p90 threshold)
SOURCE: ASSAY-CMS-DRUG-SPENDING-HARDENED-2026-05-15-001
NOTE: alpha_q < 1 implies INFINITE MEAN. The standard Pareto with finite
      variance does NOT apply.

PARAMETER: alpha_mu (markup tail)
VALUE: 1.3017 (Pareto MLE at p90 threshold)
SOURCE: ASSAY-CMS-DRUG-SPENDING-HARDENED-2026-05-15-001
NOTE: alpha_mu > 1 only at extreme tail (p90+); at p70 it is 0.60

PARAMETER: Calibration status
VALUE: FAILED
SOURCE: ASSAY-CMS-DRUG-SPENDING-HARDENED-2026-05-15-001
NOTE: Neither L2 < 0.05 NOR individual alpha > 1 met. Structural failure.

MILESTONES:

M1: Pareto model — derive L(p) = 1-(1-p)^beta from Pareto assumptions.
    Show Gini = 2/(beta+1)-1. Establish domain requirements: alpha > 2
    for finite variance, alpha > 1 for finite mean.

M2: Calibration — fit beta to Medicare Part D data. Report L2=0.0606.
    Report implied alpha_product=1.0843 (below requirement).
    CONFRONT THE FAILURE. Show Lorenz overlay (empirical vs theoretical).

M3: Diagnosis — why does the model fail? The real distribution has heavier
    tails than Pareto. Decompose: within-brand variation dominates (76.3%
    of Gini). Brand/generic split explains only 8.9%. Suggest log-normal
    body + Pareto tail.

M4: Full paper — frame as "what can the Pareto model tell us about drug
    spending, and where does it break down?"

ORACLE:
The model is valid if and only if:
1. The Lorenz curve derivation is correct
2. The calibration failure is reported PROMINENTLY (abstract, introduction)
3. alpha_q = 0.69 (infinite mean) is acknowledged explicitly
4. The paper proposes a richer specification (log-normal + Pareto) without
   implementing it (scope boundary)
5. The negative result is framed as INFORMATIVE, not as a failure

Peer Reviewer: If the paper claims the Pareto model fits well, REJECT.
L2=0.0606 > 0.05 and alpha_product=1.0843 < 2. The calibration fails.
If the paper hides the Gini gap (0.9023 vs 0.8557), REJECT.

---

## ASSAY EVIDENCE

### ASSAY Report 1: CMS_DRUG_SPENDING (Core Analysis)
PATH: C:\PROJECTS\ASSAY\reports\CMS_DRUG_SPENDING_2026_2026-05-15_001\integration_block.yaml
REPORT_ID: ASSAY-CMS-DRUG-SPENDING-2026-2026-05-15-001
DATA SOURCE: CMS Medicare Part D Spending by Drug, 2024
CONTAINS:
  - Gini coefficient: 0.9023 [95% CI: 0.8880, 0.9212], N=3,206
    Method: Trapezoidal Lorenz integration; BCa bootstrap (B=10,000, seed=42)
  - Top 10 spending share: 25.96% [95% CI: 19.74%, 37.78%]
    Method: BCa bootstrap
    NOTE: Wide CI — individual blockbuster drugs enter/leave top-10 in resamples
  - Top 50 spending share: 51.08% [95% CI: 44.63%, 60.46%]
  - Brand spending share: 90.95% (heuristic classification; no CI)
  - HHI (manufacturer, 10K scale): 295.95 [95% CI: 267.25, 623.38]
    NOTE: Entire CI below DOJ unconcentrated threshold of 1500
  - Eliquis share: 6.67% ($18.27B / $274.10B total)
  - Spending accelerators (CAGR > 20%, 2019-2023): 298 drugs

### ASSAY Report 2: CMS_DRUG_SPENDING_HARDENED (Calibration)
PATH: C:\PROJECTS\ASSAY\reports\CMS_DRUG_SPENDING_HARDENED_2026-05-15_001\integration_block.yaml
REPORT_ID: ASSAY-CMS-DRUG-SPENDING-HARDENED-2026-05-15-001
CONTAINS:
  - Lorenz exponent beta: 0.0778 [95% CI: 0.066, 0.092]
    Method: L2 minimization; percentile bootstrap (B=2000, seed=42)
  - Implied alpha_product: 1.0843 [95% CI: 1.0707, 1.1018]
    Derived: alpha_mu * alpha_q = 1/(1-beta)
  - Lorenz L2 fit error: 0.0606 [95% CI: 0.0528, 0.0705]
    NOTE: Entire CI above 0.05 — model consistently underestimates tail
  - Gini (empirical): 0.9023 [95% CI: 0.8837, 0.9174]
  - Gini (theoretical Pareto): 0.8557
    GAP: 0.047 (theoretical underestimates by 5.2%)
  - alpha_q (claims tail, p90): 0.6909
    NOTE: alpha < 1 implies INFINITE MEAN
  - alpha_mu (markup tail, p90): 1.3017
    NOTE: alpha < 2 means infinite variance
  - Calibration status: FAILED
    Criteria: L2 < 0.05 AND alpha > 1. Neither met.
  - Gini between brand/generic: 0.0804 (8.9% of total Gini)
    Within-brand dominates: 76.3%
  - Spending accelerators: 298 drugs with CAGR > 20%
AVAILABLE FIGURES (4):
  - figure1_lorenz_overlay.png — Empirical vs theoretical Lorenz
  - figure2_top20_spending.png — Top 20 drugs bar chart
  - figure3_accelerators.png — Spending accelerator trends
  - figure4_brand_generic_lorenz.png — Brand vs generic Lorenz curves

---

## DOMAIN CONSTRAINTS

| Parameter | Valid Range | Justification |
|-----------|------------|---------------|
| Gini | [0, 1] | Standard Gini index. The 0.9023 value is extremely high — only 7 of 100 theoretical concentration points separate this from perfect concentration. |
| alpha (Pareto tail) | alpha > 0 | For finite mean: alpha > 1. For finite variance: alpha > 2. The ASSAY data gives alpha_q = 0.69 (infinite mean) and alpha_mu = 1.30 (infinite variance). BOTH violate the theoretical requirements. |
| alpha_product | alpha_product > 0 | Composite parameter. At 1.0843, it is barely above 1, meaning the distribution is at the boundary of the Pareto family. |
| beta (Lorenz exponent) | beta in (0, 1) | beta=0 means perfect concentration (Gini=1). beta=1 means perfect equality (Gini=0). The 0.0778 value means extreme concentration. |
| Spending | >= 0 | Drug spending cannot be negative. |
| L2 fit error | >= 0 | Lower is better. L2 < 0.05 was the success criterion. ASSAY reports 0.0606 — the model fails. |

FLAG CONDITIONS:
- alpha_q = 0.69 implies INFINITE MEAN for the claims distribution. This means
  the standard Pareto model with finite moments does NOT apply. The paper MUST
  acknowledge this explicitly: "The estimated claims-tail exponent alpha_q=0.69
  falls below 1, implying the Pareto distribution has infinite mean at this
  threshold. This is a fundamental violation of the model's assumptions, not
  a calibration imprecision."
- The Gini gap (0.9023 empirical vs 0.8557 theoretical) of 0.047 means the model
  underestimates concentration. The real distribution has HEAVIER tails than Pareto.
- Calibration status is FAILED. This is not a borderline result — both criteria
  (L2 < 0.05 AND alpha > 1) are violated.
- Brand spending share (90.95%) but between-brand/generic Gini contribution is
  only 8.9%. This means the brand/generic split does NOT explain concentration.
  Within-brand variation (a few blockbusters dominating all brand drugs) is the
  driver.

---

## CALIBRATION INSTRUCTIONS

CRITICAL NEGATIVE RESULT — The Pareto model predicts Gini = 0.8557 but empirical
Gini = 0.9023. The model UNDERESTIMATES concentration.

1. PRIMARY CALIBRATION: Fit beta=0.0778 via L2 minimization of L(p)=1-(1-p)^beta
   against the empirical Lorenz curve. Report L2=0.0606 [0.0528, 0.0705].
   The entire CI is above the 0.05 success threshold. The fit FAILS.
   Show the Lorenz overlay figure (figure1_lorenz_overlay from ASSAY hardened).

2. ALPHA DIAGNOSIS: Report alpha_product=1.0843 and decompose:
   alpha_q=0.6909 (claims tail), alpha_mu=1.3017 (markup tail).
   State explicitly: "alpha_q=0.69 implies the claims distribution has infinite
   mean under the Pareto model. alpha_mu=1.30 implies infinite variance for the
   markup distribution. The requirement alpha > 2 for finite variance (and thus
   for the theoretical Lorenz formula to hold) is violated by a factor of ~3x
   for alpha_q and ~1.5x for alpha_mu."

3. GINI GAP: Report: "The Pareto model predicts Gini = 0.8557 but the empirical
   Gini = 0.9023, a gap of 0.047. The model captures the direction of concentration
   (Gini >> 0.5) but underestimates its magnitude by 5.2%. The implied alpha
   parameters (alpha_q=0.69, alpha_mu=1.30) are outside the model's domain
   requirement (alpha > 2), confirming the Pareto specification is inadequate."

4. WHAT EXPLAINS THE FAILURE: "The real pharmaceutical spending distribution
   has heavier tails than any single Pareto can capture. A richer specification —
   such as a log-normal body with Pareto tail (double Pareto-lognormal) —
   would accommodate both the moderate-spending drugs and the extreme blockbusters.
   This is a SCOPE BOUNDARY for this paper: we identify the failure and constrain
   the model space, but fitting a mixture model is left for future work."

5. BRAND/GENERIC DECOMPOSITION: Between brand/generic Gini = 0.0804 (8.9% of
   total). Within-brand variation dominates at 76.3%. Present this as: "The
   brand/generic split is NOT the primary driver of concentration. Within the
   brand category, a few blockbusters (Eliquis alone = 6.67% of total spending)
   dominate. The concentration problem is about WHICH brand drugs, not about
   brand vs generic."

6. WHAT THE PAPER IS: A NEGATIVE RESULT paper. The Pareto model fails
   quantitatively but succeeds qualitatively (direction is right). The negative
   result is a FEATURE: it constrains the model space and identifies that real
   drug spending has heavier tails than Pareto. Frame as scientific progress,
   not as a failed project.

---

# === STEELMAN REVISION BRIEF ===

KNOWN_DRIFT_RISKS:
- MOST CRITICAL: The Author will try to present the Pareto model as approximately
  correct. It is NOT. L2=0.0606 > 0.05, alpha_q=0.69 < 1, calibration FAILED.
  Do not downplay the failure.
- Do NOT claim "the Pareto model captures most of the variation." It misses the
  tail — and the tail IS the policy-relevant part (blockbuster drugs).
- Do NOT present alpha_q=0.69 without noting it implies infinite mean.
- The negative result should be in the ABSTRACT: "We find the Pareto model
  underestimates pharmaceutical spending concentration (theoretical Gini 0.8557
  vs empirical 0.9023), with implied tail exponents outside the model's domain."
- 298 spending accelerators (CAGR > 20%) is a supplementary finding, not the
  main result. Present in discussion, not as a headline.

# === CROSS-PAPER FINDINGS ===

- [F-005] POLICY OVERSHOOTS — The model fails. Do not derive policy from a
  failed calibration. Discuss what the failure IMPLIES for policy (simple
  parametric models are insufficient).
- [F-002] ILLUSTRATIVE — The FAILURE is the finding. Lead with it.
- [F-036/F-024] FIGURES — Use all 4 ASSAY hardened figures. The Lorenz overlay
  showing the gap is the hero figure.
- [DE-038] PLACEHOLDERS — All Gini, beta, alpha, L2 from ASSAY. No filler.

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory (auto-versioned)
Resolve: C:\PROJECTS\SHELL\papers\DRUG_SPENDING_2026_[TODAY]_[SEQ]

### Steps 2-9 — Follow identical structure, substituting DRUG_SPENDING_2026.

---

## HAND OFF — EXECUTE PAPER PIPELINE

YOUR INPUTS:
  PROBLEM: [the full PROBLEM text from INPUTS above]
  DATA: ASSAY integration blocks at:
    - C:\PROJECTS\ASSAY\reports\CMS_DRUG_SPENDING_2026_2026-05-15_001\integration_block.yaml
    - C:\PROJECTS\ASSAY\reports\CMS_DRUG_SPENDING_HARDENED_2026-05-15_001\integration_block.yaml
    Key values:
      Gini: 0.9023 [0.884, 0.917], N=3,206
      Top 10: 25.96% [19.74%, 37.78%], Top 50: 51.08% [44.63%, 60.46%]
      Brand share: 90.95%
      beta: 0.0778 [0.066, 0.092]
      alpha_product: 1.0843 [1.0707, 1.1018] (BELOW requirement of alpha > 2)
      L2 fit error: 0.0606 [0.0528, 0.0705] (FAILS threshold of 0.05)
      Theoretical Gini: 0.8557 vs Empirical: 0.9023 (GAP = 0.047)
      alpha_q: 0.6909 (INFINITE MEAN), alpha_mu: 1.3017
      Calibration: FAILED
      4 figures available (Lorenz overlay, top-20, accelerators, brand/generic)
  SLUG: DRUG_SPENDING_2026

BEGIN NOW. Run M1. Confront the negative result honestly. Write the paper.
