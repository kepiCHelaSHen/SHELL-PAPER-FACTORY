# INIT — TECHNOLOGY LOCK-IN AND SWITCHING COST THRESHOLDS: EV ADOPTION (v3 — ASSAY-Integrated)
# EXECUTE IMMEDIATELY. Do not summarize, analyze, or ask questions.
# Read the INPUTS below, then execute the SETUP SEQUENCE step by step.
# Load prompts/00_init.md for the setup procedure, then run it with these inputs.
# This is not a document to review — it is a set of instructions to follow NOW.

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Technology Lock-In and Switching Cost Thresholds: Evidence from the ICE-to-EV Transition
SLUG: TECH_LOCKIN_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: American Economic Journal: Economic Policy
PIPELINE: PAPER

PROBLEM:
Models technology adoption as a switching cost game where incumbent technology
(ICE vehicles) persists when switching costs exceed a critical threshold k*.
Derives k* as a function of total cost of ownership differential, charging
infrastructure density, and network effects. Uses ASSAY-computed country-level
k* estimates to classify 26 countries as locked-in or transitioning. The central
result: 42.3% of countries are above the switching threshold, and all top-5 EV
countries crossed their thresholds between 2017-2022. Norway's k*=0 (fully
transitioned) vs USA's k*=0.225 with wide CI [0.117, 1.543] illustrate the
spectrum.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Switching cost threshold k*
VALUE: Composite index from TCO differential, charging density, and network
       effects. k* in [0,1] for well-behaved cases. Normalized via min-max
       across 26 countries.
UNIT: dimensionless index [0,1]
TOLERANCE: dependent on normalization weights
SOURCE: ASSAY EV_SWITCHING_2026_2026-05-15_001
DRIFT_RISK: HIGH — Author may treat k* as a structural parameter rather than
             a normalized composite index. It is descriptive, not causal.

PARAMETER: Fraction above threshold
VALUE: 0.423 [95% CI: 0.192, 0.654], N=26
UNIT: proportion
SOURCE: ASSAY EV_SWITCHING_2026_2026-05-15_001
DRIFT_RISK: MEDIUM — wide CI; do not overstate precision

MILESTONES:

M1: Lock-in model — define switching cost function, derive threshold k*,
    prove existence of lock-in equilibrium for k > k*.

M2: Empirical calibration — use ASSAY country-level k* to classify countries.
    Confront USA CI upper > 1 explicitly. Present Norway as boundary case.

M3: Policy analysis — derive conditions for threshold crossing. Compare
    subsidy vs infrastructure investment as policy instruments.

M4: Full paper with figures from ASSAY hardened report.

ORACLE:
The model is valid if and only if:
1. k* is correctly derived from the switching cost model
2. Country classification uses ASSAY values, not invented parameters
3. USA CI upper > 1 is flagged and explained
4. Norway k*=0 is explained as boundary case (reference point)
5. Sensitivity analysis spans the weight parameter space

---

## ASSAY EVIDENCE

### ASSAY Report 1: EV_SWITCHING (Core Analysis)
PATH: C:\PROJECTS\ASSAY\reports\EV_SWITCHING_2026_2026-05-15_001\integration_block.yaml
REPORT_ID: EV_SWITCHING_2026_2026-05-15_001
DATA SOURCE: IEA Global EV Data Explorer; country-level TCO estimates
CONTAINS:
  - Fraction above threshold: 0.423 [95% CI: 0.192, 0.654], N=26
    Method: BCa Bootstrap (10,000 resamples, seed=42)
  - Median k*: 0.267 [95% CI: 0.190, 0.284], N=26
    Method: Leave-one-out range as CI proxy
  - Norway k*: 0.000 [95% CI: 0.000, 0.000]
    (Reference point — lowest switching cost after normalization)
  - China k*: 0.205 [95% CI: 0.126, 0.791]
  - USA k*: 0.225 [95% CI: 0.117, 1.543]
    NOTE: CI upper bound 1.543 EXCEEDS the valid domain [0,1]
  - Japan k*: 95.662 [95% CI: 14.891, 590.154]
    NOTE: Near-zero denominator artifact — negative TCO delta drives k* toward infinity
  - Europe fraction above: 0.625 [95% CI: 0.39, 0.82], N=16
  - Sensitivity best: 0.692, Sensitivity worst: 0.192

### ASSAY Report 2: EV_SWITCHING_HARDENED (Figures)
PATH: C:\PROJECTS\ASSAY\reports\EV_SWITCHING_HARDENED_2026-05-15_001\integration_block.yaml
REPORT_ID: EV_SWITCHING_HARDENED_2026-05-15_001
CONTAINS:
  - figure_1_kstar_bar_chart.png — Country-level k* with CIs, colored by classification
  - figure_2_phase_diagram.png — Switching cost vs network effect phase diagram
  - figure_3_sensitivity_tornado.png — Sensitivity tornado (switching cost weight most influential)
  - figure_4_ev_trajectory.png — EV adoption trajectories with threshold crossings
KEY FINDINGS FROM FIGURES:
  - Switching cost weight is the most influential parameter (tornado range 0.269-0.615)
  - All top-5 EV countries crossed thresholds between 2017-2022
  - Locked-in countries cluster in low-switching-cost, high-infrastructure quadrant

---

## DOMAIN CONSTRAINTS

The Author MUST enforce these parameter ranges. Any value outside these ranges
is a model error that must be flagged, not silently used.

| Parameter | Valid Range | Justification |
|-----------|------------|---------------|
| k* | [0, 1] | Normalized composite index. k*=0 means zero switching cost (Norway). k*=1 means maximum switching cost in sample. Values OUTSIDE [0,1] reflect normalization artifacts. |
| Fraction above threshold | [0, 1] | Proportion of countries. The 0.423 value has wide CI [0.192, 0.654] — report this uncertainty prominently. |
| TCO differential | Can be negative | Negative TCO means EVs already cheaper. Japan has negative TCO delta, causing k* to blow up — this is a model artifact, not a real switching cost of 95.662. |
| Weight parameters | Each in [0, 2], sum unconstrained | Sensitivity analysis must span weight space. Default weights are 1.0 each. |

FLAG CONDITIONS:
- USA k* CI upper is 1.543 — this EXCEEDS the valid domain [0,1]. The paper
  MUST flag this: "The USA's BCa bootstrap CI upper bound of 1.543 exceeds
  the normalized domain. This reflects parameter uncertainty from heterogeneous
  state-level conditions (US averages mask enormous state-level variation in
  charging density), not a model prediction that switching costs exceed the
  maximum. The wide CI indicates the USA's lock-in status is genuinely uncertain."
- Japan k* = 95.662 is an artifact of near-zero denominator in the TCO ratio.
  Flag: "Japan's extreme k* reflects a negative TCO differential (EVs are not
  yet cost-competitive in Japan), causing division by a near-zero quantity.
  Interpret Japan as 'deeply locked in' without taking the numeric value literally."
- Norway k* = 0.000 is the reference point by construction (min-max normalization).
  Flag: "Norway's k*=0 is a normalization artifact — it is the country with the
  lowest composite switching cost, not a country with literally zero barriers."

---

## CALIBRATION INSTRUCTIONS

The Author MUST perform these specific model-data comparisons using ASSAY values:

1. PRIMARY CALIBRATION: Compute k* from the model for each of the 26 countries
   using ASSAY switching cost and network parameters. Compare model k* to
   ASSAY-observed EV adoption share. Do countries above the threshold (k* > median)
   show lower EV adoption? Present the phase diagram (ASSAY figure_2) as evidence.

2. THRESHOLD CROSSING TIMING: The ASSAY hardened report shows all top-5 EV
   countries crossed their k* thresholds between 2017-2022. Use figure_4 to
   illustrate. Discuss whether the crossing is a cause or correlate of adoption.

3. SENSITIVITY: The ASSAY tornado chart shows switching cost weight is the most
   influential parameter (range 0.269-0.615 for fraction above threshold).
   Present the full sensitivity range: best case 0.692, worst case 0.192.
   The paper must acknowledge: "The fraction of countries above threshold ranges
   from 19.2% to 69.2% depending on weight specification."

4. COUNTRY DEEP DIVES:
   - Norway (k*=0.000): Explain as boundary reference. Discuss policies
     (tax exemptions, toll waivers, charging density) that drove switching costs
     to minimum.
   - China (k*=0.205 [0.126, 0.791]): Second-lowest point estimate. Discuss
     industrial policy, subsidy programs, domestic manufacturing.
   - USA (k*=0.225 [0.117, 1.543]): Similar point estimate to China but MUCH
     wider CI. Discuss state-level heterogeneity.
   - Japan (k*=95.662): Explain as artifact. Japan is locked in due to negative
     TCO delta (hybrid-focused industrial policy).

5. EUROPE vs REST: Europe fraction above threshold: 0.625 [0.39, 0.82].
   Compare to global 0.423. Is Europe systematically different?

---

# === STEELMAN REVISION BRIEF ===

KNOWN_DRIFT_RISKS:
- k* is a NORMALIZED COMPOSITE INDEX, not a structural causal parameter.
  Do NOT interpret k*=0.225 for the USA as "22.5% of maximum switching cost"
  in any meaningful economic sense. It is a rank-ordering tool.
- The model does not identify CAUSAL effects of policies on switching costs.
  It classifies countries by observed switching cost proxies. Policy discussion
  must be clearly speculative/suggestive.
- Japan's k*=95.662 is a normalization artifact. Do NOT use it in regression
  or statistical analysis without transformation or exclusion.
- N=26 is small. Do not overfit. Do not run regressions with > 3 predictors.

# === CROSS-PAPER FINDINGS ===

- [F-005] POLICY OVERSHOOTS — Do not claim the model identifies optimal subsidies.
- [F-002] ILLUSTRATIVE COMPONENT — The threshold classification IS the result.
- [F-036/F-024] FIGURES — Use all 4 ASSAY hardened figures. Render, don't just cite code.
- [DE-038] PLACEHOLDERS — Every k*, CI, and fraction must be from ASSAY.

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory (auto-versioned)
Resolve using auto-versioning: C:\PROJECTS\SHELL\papers\TECH_LOCKIN_2026_[TODAY]_[SEQ]

Create RESOLVED_DIR with subdirectories:
  figures/, outputs/, results/raw/, results/final/, devlog/, prompts/

### Steps 2-9 — Follow identical structure to REPLICATION_CRISIS_2026 init,
substituting TECH_LOCKIN_2026 for the slug throughout.

---

## HAND OFF — EXECUTE PAPER PIPELINE

DO NOT STOP HERE. Execute the paper pipeline.

YOUR INPUTS:
  PROBLEM: [the full PROBLEM text from INPUTS above]
  DATA: ASSAY integration blocks at:
    - C:\PROJECTS\ASSAY\reports\EV_SWITCHING_2026_2026-05-15_001\integration_block.yaml
    - C:\PROJECTS\ASSAY\reports\EV_SWITCHING_HARDENED_2026-05-15_001\integration_block.yaml
    Key values:
      Fraction above threshold: 0.423 [0.192, 0.654], N=26
      Median k*: 0.267 [0.190, 0.284]
      Norway k*: 0.000, China k*: 0.205 [0.126, 0.791]
      USA k*: 0.225 [0.117, 1.543] (CI upper > 1 — FLAG)
      Japan k*: 95.662 (artifact — FLAG)
      Europe fraction above: 0.625 [0.39, 0.82]
      4 publication-quality figures available
  SLUG: TECH_LOCKIN_2026
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS above]

BEGIN NOW. Run M1. Execute it. Write the paper.
