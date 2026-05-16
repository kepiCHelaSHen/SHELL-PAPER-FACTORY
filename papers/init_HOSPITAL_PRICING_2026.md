# INIT — HOSPITAL PRICING OPACITY: CHARGE-TO-PAYMENT RATIOS AND THE INFORMATION ASYMMETRY PREMIUM (v3 — ASSAY-Integrated)
# EXECUTE IMMEDIATELY. Do not summarize, analyze, or ask questions.
# Read the INPUTS below, then execute the SETUP SEQUENCE step by step.
# Load prompts/00_init.md for the setup procedure, then run it with these inputs.
# This is not a document to review — it is a set of instructions to follow NOW.

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Hospital Pricing Opacity: Charge-to-Payment Ratios, Market Power, and the Information Asymmetry Premium in US Healthcare
SLUG: HOSPITAL_PRICING_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: American Economic Review (Papers and Proceedings)
PIPELINE: PAPER

PROBLEM:
Models hospital pricing as an information asymmetry game where hospitals set
charges (list prices) far above Medicare payments. The charge-to-payment ratio
(CPR) measures the markup. Derives a model where CPR depends on market
concentration (HHI), private payer share, and regulatory environment. Uses
ASSAY-computed CPR statistics from 145,879 hospital-DRG pairs across 2,906
hospitals to calibrate. The central findings: median CPR is 5.63x across all
pairs, ranging from 1.23x in Maryland (all-payer rate-setting) to 11.23x in
Nevada. Larger hospitals charge MORE, not less (Spearman rho=0.36), supporting
the market-power channel.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Median CPR (overall)
VALUE: 5.63 [95% CI: 5.61, 5.64], N=145,879 hospital-DRG pairs
UNIT: ratio (charges / Medicare payment)
SOURCE: ASSAY-CMS-HOSPITAL-PRICING-2026-05-15-001
DRIFT_RISK: LOW — ASSAY-computed

PARAMETER: 90th percentile CPR
VALUE: 11.09 [95% CI: 11.03, 11.16]
SOURCE: ASSAY-CMS-HOSPITAL-PRICING-2026-05-15-001

PARAMETER: Highest DRG markup
VALUE: Kidney transplants (DRG 652) at 12.66x [95% CI: 11.61, 13.59]
SOURCE: ASSAY-CMS-HOSPITAL-PRICING-2026-05-15-001

PARAMETER: State extremes
VALUE: Nevada 11.23x [95% CI: 10.91, 11.55] (highest),
       Maryland 1.23x [95% CI: 1.23, 1.23] (lowest, all-payer rate-setting)
SOURCE: ASSAY-CMS-HOSPITAL-PRICING-2026-05-15-001

PARAMETER: Volume-CPR correlation
VALUE: Spearman rho = 0.36 [95% CI: 0.32, 0.39]
SOURCE: ASSAY-CMS-HOSPITAL-PRICING-2026-05-15-001

PARAMETER: DRG 470 (major joint replacement)
VALUE: Charges $79,947, Medicare pays $13,074, CPR = 5.87x [95% CI: 5.69, 6.10]
SOURCE: ASSAY-CMS-HOSPITAL-PRICING-2026-05-15-001

MILESTONES:

M1: Pricing model — derive CPR as a function of market concentration, private
    payer share, and regulatory opacity. Show that CPR > 1 whenever there is
    price discrimination between payers.

M2: Empirical calibration — use ASSAY CPR data. Maryland as alpha=0 benchmark.
    Volume-CPR positive correlation as market-power evidence.

M3: DRG-level analysis — why do kidney transplants have the highest markup?
    Discuss procedure complexity, negotiation leverage, and patient lock-in.

M4: Full paper with policy discussion (price transparency, all-payer systems).

ORACLE:
The model is valid if and only if:
1. CPR is correctly derived from the pricing model
2. Maryland is used as the regulated benchmark (alpha=0)
3. The volume-CPR positive correlation is presented as market-power evidence
4. DRG-level variation is explained by the model's mechanisms
5. Policy implications are scoped to what the model supports

---

## ASSAY EVIDENCE

### ASSAY Report: CMS_HOSPITAL_PRICING
PATH: C:\PROJECTS\ASSAY\reports\CMS_HOSPITAL_PRICING_2026_2026-05-15_001\integration_block.yaml
REPORT_ID: ASSAY-CMS-HOSPITAL-PRICING-2026-05-15-001
DATA SOURCE: CMS Medicare Inpatient Hospitals by Provider and Service, FY2024
CONTAINS:
  - Overall median CPR: 5.63 [95% CI: 5.61, 5.64], N=145,879 hospital-DRG pairs
    Method: Bootstrap BCa (10,000 resamples, seed=42)
  - 90th percentile CPR: 11.09 [95% CI: 11.03, 11.16]
    Method: Bootstrap BCa
  - Highest DRG markup: Kidney transplants (DRG 652) at 12.66x [95% CI: 11.61, 13.59]
    Method: Bootstrap BCa
  - Highest state median CPR: Nevada at 11.23x [95% CI: 10.91, 11.55]
    Method: Bootstrap percentile
  - Lowest state median CPR: Maryland at 1.23x [95% CI: 1.23, 1.23]
    Method: Bootstrap percentile (nearly degenerate — rate-setting)
  - Volume-CPR correlation: Spearman rho = 0.36 [95% CI: 0.32, 0.39]
    Method: Bootstrap BCa (10,000 resamples, seed=42)
    Interpretation: Larger hospitals charge MORE relative to Medicare payments
  - DRG 470 (major joint replacement): CPR = 5.87x [95% CI: 5.69, 6.10]
    Median charges: $79,947; Medicare payment: $13,074
  - Robustness: Winsorization changes median by 0.00%, mean by -0.59%
DATA PROVENANCE:
  - 145,879 hospital-DRG pairs, 2,906 hospitals, 540 DRGs, 51 states
  - SHA256 of input: 2ab6da15be4cd47c4ecc05e0f54545e4493ee4eea58df626d1aa2e6b19b65e0d
AVAILABLE FIGURES (4):
  - CPR distribution (histogram)
  - State heatmap
  - DRG 470 deep dive
  - CPR vs volume scatter

---

## DOMAIN CONSTRAINTS

| Parameter | Valid Range | Justification |
|-----------|------------|---------------|
| CPR | CPR >= 1 | By construction: charges >= Medicare payments. If any CPR < 1, it means charges are below Medicare — this can happen for loss-leader DRGs but should be flagged. |
| HHI | [0, 10000] | Standard HHI scale. 0 = perfect competition, 10000 = monopoly. |
| Private payer share | [0, 1] | Fraction of hospital revenue from private payers. Higher share = more pricing flexibility. |
| Opacity parameter alpha | [0, 1] | Model parameter. alpha=0 means full transparency (Maryland). alpha=1 means full opacity. |

FLAG CONDITIONS:
- Maryland CPR = 1.23x with degenerate CI [1.23, 1.23]. This is the regulated
  benchmark. All-payer rate-setting collapses CPR near 1. This is not an outlier
  to exclude — it is the alpha=0 case that validates the model.
- Nevada CPR = 11.23x is 9.1x higher than Maryland. The model must explain this
  9x range through opacity/market-power differences.
- Volume-CPR rho=0.36 is POSITIVE. This CONTRADICTS the naive competition
  story (more volume = more competition = lower prices). It SUPPORTS the
  market-power story (larger hospitals have more negotiating leverage).
  Present this as a key finding.

OVERIDENTIFICATION TEST (REQUIRED — addresses D5 non-falsifiability):
  The model is exactly identified by construction (opacity parameter alpha
  maps 1:1 to observed CPR). To make it FALSIFIABLE, use the volume-CPR
  correlation as an OVERIDENTIFYING RESTRICTION:
  
  PREDICTION: If opacity enables markups, then hospitals with higher volume
  (which proxies for market power) should have higher CPR, because market
  power both enables opacity and prevents price discipline.
  
  TEST: The model predicts rho(volume, CPR) > 0. The ASSAY-computed value
  is rho = 0.36 [0.32, 0.39]. If rho were <= 0, the opacity-market-power
  channel would be falsified — high CPR would not correlate with market
  power, contradicting the model's mechanism.
  
  SECOND TEST: DRG complexity as a predictor. The model predicts that
  higher-complexity DRGs (where information asymmetry is greater) should
  have higher CPR. Compare DRG 652 (kidney transplant, CPR=12.66) vs
  DRG 470 (joint replacement, CPR=5.87) — the model predicts this ordering
  because transplants have greater opacity (fewer providers, emergency nature,
  higher complexity). If low-complexity DRGs had HIGHER CPR, the model's
  opacity mechanism would be contradicted.
  
  The Author MUST present these tests explicitly and report whether the
  predictions survive. If they fail, confront the failure honestly.

---

## CALIBRATION INSTRUCTIONS

The Author MUST perform these specific model-data comparisons using ASSAY values:

1. MARYLAND BENCHMARK: Use Maryland (CPR=1.23x) as the alpha=0 case. Under
   full regulation, CPR approaches 1 (charges ≈ payments). Maryland's 1.23x
   represents the residual markup even under rate-setting (possibly administrative
   costs or stale charge-master entries). Derive the implied opacity premium
   for other states: e.g., Nevada's opacity premium = 11.23/1.23 = 9.13x
   above the regulated baseline.

2. MARKET POWER CHANNEL: The volume-CPR positive correlation (Spearman rho=0.36
   [0.32, 0.39]; ASSAY-CMS-HOSPITAL-PRICING-2026-05-15-001) supports the
   market-power channel. Present this as: "Larger hospitals (by total discharges)
   have HIGHER charge-to-payment ratios (rho=0.36, p<0.001), consistent with
   the hypothesis that market concentration enables higher markups. This
   contradicts the competitive model where higher volume should reduce per-unit
   markups through economies of scale."

3. DRG VARIATION: Kidney transplants (DRG 652) at 12.66x vs DRG 470 (joint
   replacement) at 5.87x. Discuss why: transplants have fewer competing providers,
   emergency nature limits patient shopping, high complexity reduces price
   transparency. Present the DRG-level variation as evidence that opacity varies
   by procedure type.

4. STATE VARIATION: The 9.1x range from Maryland (1.23x) to Nevada (11.23x)
   is the key cross-sectional variation. Map states to model parameters.
   Which state characteristics predict higher CPR? (Market concentration,
   regulatory environment, private payer mix.)

5. ROBUSTNESS: Winsorization changes median by 0.00% and mean by -0.59%.
   CPR results are not driven by outliers.

---

# === STEELMAN REVISION BRIEF ===

KNOWN_DRIFT_RISKS:
- CPR is charges divided by Medicare payments. Charges are list prices that
  NO ONE pays (except the uninsured). Do not conflate CPR with actual prices
  paid by private insurers. CPR measures the OPACITY GAP, not the actual
  price discrimination.
- The model does not identify CAUSAL effects of market concentration on CPR.
  The volume-CPR correlation is descriptive, not causal.
- Maryland is the benchmark by POLICY DESIGN (all-payer rate-setting), not by
  random assignment. Do not claim the Maryland comparison is quasi-experimental.
- Do NOT claim hospitals are "gouging" patients. The model says opacity enables
  higher markups, which is different from normative judgment.

# === CROSS-PAPER FINDINGS ===

- [F-005] POLICY OVERSHOOTS — Do not claim price transparency "will fix" pricing.
  The model shows opacity enables high CPR; it does not predict what transparency
  would do to actual negotiated prices.
- [F-002] ILLUSTRATIVE — The 9.1x Maryland-Nevada range IS the finding.
- [F-036/F-024] FIGURES — Render all 4 ASSAY figures.
- [DE-038] PLACEHOLDERS — All CPR values, CIs, and correlations from ASSAY.

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory (auto-versioned)
Resolve: C:\PROJECTS\SHELL\papers\HOSPITAL_PRICING_2026_[TODAY]_[SEQ]

### Steps 2-9 — Follow identical structure, substituting HOSPITAL_PRICING_2026.

---

## HAND OFF — EXECUTE PAPER PIPELINE

YOUR INPUTS:
  PROBLEM: [the full PROBLEM text from INPUTS above]
  DATA: ASSAY integration block at:
    - C:\PROJECTS\ASSAY\reports\CMS_HOSPITAL_PRICING_2026_2026-05-15_001\integration_block.yaml
    Key values:
      Median CPR: 5.63 [5.61, 5.64], N=145,879
      90th pctile CPR: 11.09 [11.03, 11.16]
      Top DRG: kidney transplants 12.66x [11.61, 13.59]
      Nevada: 11.23x [10.91, 11.55], Maryland: 1.23x [1.23, 1.23]
      Volume-CPR rho: 0.36 [0.32, 0.39]
      DRG 470: 5.87x [5.69, 6.10], charges $79,947 / payment $13,074
  SLUG: HOSPITAL_PRICING_2026

BEGIN NOW. Run M1. Execute it. Write the paper.
