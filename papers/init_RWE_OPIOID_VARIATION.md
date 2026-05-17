# INIT FILE — RWE Evidence Report: Opioid Prescribing Variation
# TYPE: Real-World Evidence Report (NOT academic paper)
# AUTHOR_PROMPT: prompts/05_author_rwe.md

## Experiment Identity
Name: Geographic and Specialty Variation in Opioid Prescribing Among Medicare Part D Providers: A Cross-Sectional Analysis
Slug: RWE_OPIOID_VARIATION
Author: James P Rice Jr.
Target: Internal evidence report / Health Affairs (for publication)
Status: INIT
Report Type: REAL_WORLD_EVIDENCE

## Study Question (PICO Format)
- **Population**: All Medicare Part D prescribers (N=810,057) in CY2023
- **Intervention/Exposure**: Geographic location (state) and medical specialty
- **Comparator**: National average opioid prescribing rate; lowest-rate state (New York)
- **Outcome**: Opioid claims as a percentage of total Part D claims

## Plain Language Question
"How much does opioid prescribing vary across states and specialties among
Medicare providers, and which subgroups have statistically elevated rates?"

## Confirmed Design Decisions
Spec locked: frozen_spec.md
Pipeline: RWE REPORT — milestone-by-milestone gating
Author prompt: prompts/05_author_rwe.md (RWE variant)
Peer Reviewer: prompts/06_peer_reviewer.md (standard — works for RWE)
Editor: prompts/07_editor.md (standard)
Review format: Markdown

## ASSAY EVIDENCE
### ASSAY Report: CMS_OPIOID_PRESCRIBING
PATH: C:\PROJECTS\ASSAY\reports\CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001\integration_block.yaml
DATA_APPENDIX: C:\PROJECTS\ASSAY\reports\CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001\data_appendix_fragment.md

KEY COMPUTED VALUES (from integration block):
  - National opioid claims rate: 4.16% [95% CI: 4.12-4.19%], N=810,057
  - Highest state (Alabama): 6.01% [5.65-6.47%]
  - Lowest state (New York): 2.45% [2.38-2.53%]
  - State max/min ratio: 2.45x
  - Interventional Pain Medicine: 56.34% [55.00-57.54%]
  - General Practice: 7.68% [7.51-7.82%]
  - Outlier providers (>3 SD): 13,913 (1.72%)
  - Volume-rate correlation: Spearman rho = 0.0861 [0.0793-0.0929] (weak)
  - Long-acting opioid ratio: 10.05%

## Milestones
M1: Study Design + Study Population. Define inclusion/exclusion criteria,
    data source, statistical methods. Present the study population table.
M2: Results. Primary finding (national rate + CI), geographic variation table
    (all 51 states ranked), specialty variation table (13 specialties ranked).
    Identify the 2.45x state ratio as the headline finding.
M3: Subgroup Analyses + Sensitivity + Limitations. Outlier analysis (13,913
    providers), volume-rate relationship (rho=0.0861, weak), long-acting ratio.
    Sensitivity: robustness to outlier exclusion, specialty-adjusted rates.
    Limitations as argumentative prose (not numbered list).
M4: Executive Summary (written LAST) + Clinical Implications + Data Appendix.
    Include data_appendix_fragment from ASSAY.

## Frozen Parameters

| Parameter | Value | CI | Source |
|-----------|-------|----|--------|
| National opioid rate | 4.16% | [4.12, 4.19] | CMS Part D 2023 |
| Alabama rate | 6.01% | [5.65, 6.47] | CMS Part D 2023 |
| New York rate | 2.45% | [2.38, 2.53] | CMS Part D 2023 |
| State ratio | 2.45x | — | Computed |
| Interventional Pain rate | 56.34% | [55.00, 57.54] | CMS Part D 2023 |
| General Practice rate | 7.68% | [7.51, 7.82] | CMS Part D 2023 |
| Outlier count | 13,913 | — | >3 SD above specialty mean |
| Volume-rate rho | 0.0861 | [0.0793, 0.0929] | Spearman, N=810,057 |
| LA opioid ratio | 10.05% | — | CMS Part D 2023 |
| Total prescribers | 810,057 | — | CMS Part D 2023 |

## Drift Risks
- Do NOT use causal language. This is observational. "Associated with" not "causes."
- Do NOT identify individual prescribers as inappropriate. The analysis identifies
  population-level patterns, not individual misconduct.
- Do NOT claim that high-rate states are "over-prescribing." State that variation
  exists and warrants investigation — the clinical appropriateness of any rate
  depends on patient population characteristics not captured in claims data.
- The volume-rate correlation (0.0861) is WEAK. Do not overinterpret. It means
  high-volume prescribers are NOT systematically more likely to prescribe opioids.
- Alabama's rate (6.01%) has a WIDER CI than New York's (2.45%) because of
  different provider counts. Note this when comparing.

## Oracle
- The 2.45x state variation ratio is the headline finding.
- The specialty analysis shows Interventional Pain at 56.34% is expected and
  should not be framed as concerning — these are pain specialists.
- The outlier analysis (13,913 at >3 SD) is the most operationally actionable finding.
- The weak volume-rate correlation is a NEGATIVE finding — report it honestly.
  It means PDMP monitoring cannot use prescription volume as a proxy for
  opioid prescribing intensity.

## SETUP SEQUENCE
1. Create directory: papers/RWE_OPIOID_VARIATION_[DATE]_001/
2. Copy frozen parameters to frozen_spec.md
3. Initialize state_vector.md
4. Run pipeline with AUTHOR_PROMPT: prompts/05_author_rwe.md
