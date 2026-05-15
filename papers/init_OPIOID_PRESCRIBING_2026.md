# INIT — OPIOID PRESCRIBING AND MONITORING DETERRENCE: A STRATEGIC MODEL (v3 — ASSAY-Integrated)
# EXECUTE IMMEDIATELY. Do not summarize, analyze, or ask questions.
# Read the INPUTS below, then execute the SETUP SEQUENCE step by step.
# Load prompts/00_init.md for the setup procedure, then run it with these inputs.
# This is not a document to review — it is a set of instructions to follow NOW.

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Opioid Prescribing and Monitoring Deterrence: A Strategic Model of Prescription Drug Monitoring Programs
SLUG: OPIOID_PRESCRIBING_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: Journal of Health Economics
PIPELINE: PAPER

PROBLEM:
Models opioid prescribing as a strategic interaction between prescribers and
a monitoring authority (PDMP). The prescriber chooses prescribing intensity
given a monitoring probability m and penalty F. The model predicts a deterrence
threshold m* above which prescribing drops discontinuously. Uses ASSAY-computed
state-level and specialty-level prescribing rates from CMS Medicare Part D data
(810,057 prescribers) to calibrate. The central finding: the national opioid
claims rate is 0.0416, with a 2.45x ratio between the highest state (AL: 0.0601)
and lowest (NY: 0.0245). Interventional pain management has a 0.5634 opioid
claims rate, 13.5x the national average.

FROZEN_SPEC_PARAMETERS:

PARAMETER: National opioid claims rate
VALUE: 0.0416 [95% CI: 0.0412, 0.0419], N=810,057 prescribers
UNIT: proportion (opioid claims / total claims)
SOURCE: ASSAY-CMS-OPIOID-PRESCRIBING-2026-05-15-001
DRIFT_RISK: LOW — ASSAY-computed

PARAMETER: Highest state rate (Alabama)
VALUE: 0.0601 [95% CI: 0.0565, 0.0647], N=11,965
SOURCE: ASSAY-CMS-OPIOID-PRESCRIBING-2026-05-15-001

PARAMETER: Lowest state rate (New York)
VALUE: 0.0245 [95% CI: 0.0238, 0.0253], N=57,555
SOURCE: ASSAY-CMS-OPIOID-PRESCRIBING-2026-05-15-001

PARAMETER: AL/NY ratio
VALUE: 2.45
SOURCE: ASSAY-CMS-OPIOID-PRESCRIBING-2026-05-15-001

PARAMETER: Highest specialty rate (Interventional Pain Management)
VALUE: 0.5634 [95% CI: 0.5500, 0.5754], N=1,426
SOURCE: ASSAY-CMS-OPIOID-PRESCRIBING-2026-05-15-001

PARAMETER: Outlier count (3 SD)
VALUE: 13,913 prescribers (1.72% of 809,884 scored)
SOURCE: ASSAY-CMS-OPIOID-PRESCRIBING-2026-05-15-001
NOTE: Sensitive to distributional assumptions (skewness 2-8)

PARAMETER: Volume-rate correlation
VALUE: Spearman rho = 0.0861 [95% CI: 0.0837, 0.0884], N=810,057
SOURCE: ASSAY-CMS-OPIOID-PRESCRIBING-2026-05-15-001
NOTE: Weak but statistically significant only due to N=810K. Not clinically meaningful.

PARAMETER: National LA opioid ratio
VALUE: 0.1005 (LA opioid claims / total opioid claims), N=345,583
SOURCE: ASSAY-CMS-OPIOID-PRESCRIBING-2026-05-15-001

PARAMETER: Weighted-unweighted rank correlation
VALUE: 0.7024 (Spearman, N=51 states)
SOURCE: ASSAY-CMS-OPIOID-PRESCRIBING-2026-05-15-001
NOTE: Moderate agreement — aggregation method matters

MILESTONES:

M1: Deterrence model — derive prescribing decision as function of monitoring
    probability m and penalty F. Prove existence of threshold m*.

M2: Empirical calibration — use ASSAY state-level rates to calibrate. States
    with stronger PDMP = higher m. Compare rates across m proxy values.

M3: Specialty analysis — interventional pain management as the high-baseline
    specialty. Outlier identification.

M4: Full paper with policy discussion on PDMP design.

ORACLE:
The model is valid if and only if:
1. The deterrence threshold m* is correctly derived
2. State-level variation is consistent with different m values
3. Specialty variation is explained by baseline clinical need
4. Outlier analysis uses the ASSAY 3-SD threshold (13,913 prescribers)
5. The weak volume-rate correlation is not overinterpreted

---

## ASSAY EVIDENCE

### ASSAY Report: CMS_OPIOID_PRESCRIBING
PATH: C:\PROJECTS\ASSAY\reports\CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001\integration_block.yaml
REPORT_ID: ASSAY-CMS-OPIOID-PRESCRIBING-2026-05-15-001
DATA SOURCE: CMS Medicare Part D Prescriber Data, CY2023
CONTAINS:
  - National opioid claims rate: 0.0416 [95% CI: 0.0412, 0.0419], N=810,057
    Method: Claims-weighted aggregate with BCa bootstrap (B=2000, seed=42)
  - Highest state (AL): 0.0601 [95% CI: 0.0565, 0.0647], N=11,965
  - Lowest state (NY): 0.0245 [95% CI: 0.0238, 0.0253], N=57,555
  - AL/NY ratio: 2.45 (ratio of point estimates; no CI for ratio)
  - Highest specialty (Interventional Pain Mgmt): 0.5634 [95% CI: 0.5500, 0.5754], N=1,426
    Method: Claims-weighted with percentile bootstrap
  - Outlier count (3 SD above specialty mean): 13,913 (1.72% of 809,884 scored)
    NOTE: Threshold-based; sensitive to skewness (2-8 across specialties)
  - Volume-rate Spearman rho: 0.0861 [95% CI: 0.0837, 0.0884], N=810,057
    NOTE: Statistically significant only due to massive N; weak effect
  - National LA opioid ratio: 0.1005, N=345,583
  - Weighted vs unweighted rank correlation: 0.7024 (moderate agreement)
AVAILABLE FIGURES (6):
  - State-level prescribing rate map/chart
  - Specialty-level rate comparison
  - Outlier distribution
  - Volume vs rate scatter
  - LA opioid ratio by state
  - Forest plot of state rates

---

## DOMAIN CONSTRAINTS

| Parameter | Valid Range | Justification |
|-----------|------------|---------------|
| Prescribing rate | [0, 1] | Proportion of opioid claims out of total claims. Rate of 0.5634 for interventional pain is valid — over half their claims are opioid-related. |
| Monitoring intensity m | [0, 1] | Model parameter. m=0 means no monitoring, m=1 means every prescription is reviewed. |
| Penalty F | F > 0 | Penalty for detected inappropriate prescribing. Must be positive for deterrence to work. |
| Deterrence threshold m* | m* in (0, 1) | The monitoring level above which prescribing drops. If m* >= 1, deterrence is impossible (penalty too low). If m* = 0, any monitoring deters (penalty infinitely high). |

FLAG CONDITIONS:
- Volume-rate rho = 0.0861 is WEAK. Statistical significance at N=810K is
  meaningless for practical purposes. Do NOT claim "higher-volume prescribers
  prescribe more opioids" as a substantive finding. The effect size is negligible.
  Report it but flag: "The correlation is statistically significant (p<0.001)
  but trivially small (rho=0.0861), reflecting the massive sample size rather
  than a clinically meaningful relationship."
- The 3-SD outlier threshold assumes approximate normality within specialties.
  With skewness 2-8, this threshold is CONSERVATIVE (captures fewer outliers
  than a symmetric distribution would suggest). Flag this assumption.
- The weighted-unweighted rank correlation (0.7024) means state rankings change
  depending on aggregation method. Present both weighted and unweighted results.
- AL/NY ratio of 2.45x has no CI. Propagate uncertainty from individual state
  CIs or acknowledge the gap.

---

## CALIBRATION INSTRUCTIONS

The Author MUST perform these specific model-data comparisons using ASSAY values:

1. PRIMARY CALIBRATION: The model predicts a deterrence threshold m* above which
   prescribing drops discontinuously. ASSAY provides the empirical prescribing
   distribution across 51 states. Use state-level rates to calibrate: states
   with stronger PDMP enforcement (proxy for higher m) should have lower
   prescribing rates. The AL/NY ratio of 2.45x should be consistent with
   different m values. Specifically:
   - Alabama (0.0601): Historically weaker PDMP enforcement (proxy m_AL)
   - New York (0.0245): Historically stronger PDMP with mandatory use (proxy m_NY)
   - If m_NY > m* > m_AL, the model predicts NY rate << AL rate. The 2.45x ratio
     is consistent with AL being below threshold and NY above.

2. SPECIALTY CALIBRATION: Interventional pain management (0.5634) has a
   naturally high opioid baseline due to clinical function. The model must
   distinguish between high baseline (clinically appropriate) and high excess
   (monitoring-deterrable). Present specialty rates as a BASELINE ADJUSTMENT,
   not as evidence of inappropriate prescribing.

3. OUTLIER ANALYSIS: 13,913 prescribers (1.72%) exceed 3 SD above their
   specialty mean. These are the prescribers the PDMP is designed to detect.
   Compute: at current detection rates, what monitoring probability m would
   be needed to deter these outliers? Is m feasible?

4. LA OPIOID RATIO: Long-acting opioids represent 10.05% of opioid claims
   nationally. LA prescribing patterns may differ across states. Present as
   supplementary analysis.

5. AGGREGATION SENSITIVITY: The weighted-unweighted rank correlation is 0.7024.
   Present both aggregations and discuss which is more relevant for the model
   (claims-weighted captures patient exposure; unweighted captures prescriber
   behavior).

---

# === STEELMAN REVISION BRIEF ===

KNOWN_DRIFT_RISKS:
- Do NOT claim high prescribing rates are evidence of inappropriate prescribing.
  The data shows RATES, not appropriateness. Some specialties (pain management)
  have legitimately high opioid prescribing rates.
- Do NOT use the volume-rate correlation (rho=0.0861) as evidence of anything
  substantive. It is trivially small despite statistical significance.
- Do NOT identify individual prescribers as outliers in the paper. The 13,913
  count is a population statistic, not a naming exercise.
- The deterrence model is THEORETICAL. The ASSAY data provides cross-sectional
  variation, not causal estimates of PDMP effects. Do not claim PDMP effectiveness
  from cross-state comparisons.

# === CROSS-PAPER FINDINGS ===

- [F-005] POLICY OVERSHOOTS — PDMP design recommendations must be scoped to model.
- [F-002] ILLUSTRATIVE — The 2.45x AL/NY ratio and specialty variation ARE the findings.
- [F-036/F-024] FIGURES — Render all 6 ASSAY figures.
- [DE-038] PLACEHOLDERS — All rates, CIs, counts from ASSAY. No filler.

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory (auto-versioned)
Resolve: C:\PROJECTS\SHELL\papers\OPIOID_PRESCRIBING_2026_[TODAY]_[SEQ]

### Steps 2-9 — Follow identical structure, substituting OPIOID_PRESCRIBING_2026.

---

## HAND OFF — EXECUTE PAPER PIPELINE

YOUR INPUTS:
  PROBLEM: [the full PROBLEM text from INPUTS above]
  DATA: ASSAY integration block at:
    - C:\PROJECTS\ASSAY\reports\CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001\integration_block.yaml
    Key values:
      National rate: 0.0416 [0.0412, 0.0419], N=810,057
      AL: 0.0601 [0.0565, 0.0647], NY: 0.0245 [0.0238, 0.0253]
      AL/NY ratio: 2.45x
      Interventional Pain: 0.5634 [0.5500, 0.5754]
      Outliers (3 SD): 13,913 (1.72%)
      Volume-rate rho: 0.0861 [0.0837, 0.0884] (WEAK)
      LA ratio: 0.1005
      6 figures available
  SLUG: OPIOID_PRESCRIBING_2026

BEGIN NOW. Run M1. Execute it. Write the paper.
