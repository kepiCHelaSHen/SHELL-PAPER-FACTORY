# INIT FILE — RWE Evidence Report: Opioid Prescribing Variation (VALIDATED)
# TYPE: Real-World Evidence Report — FULL PIPELINE VALIDATION
# PURPOSE: Compare pipeline-validated output against single-pass Author output.
# The single-pass version (RWE_OPIOID_VARIATION) scored Gemini ACCEPT with six 10s.
# This version runs through Peer Reviewer, Steelman, and Editor to test whether
# the adversarial pipeline maintains or degrades quality.

## Experiment Identity
Name: Geographic and Specialty Variation in Opioid Prescribing Among Medicare Part D Providers: A Cross-Sectional Analysis
Slug: RWE_OPIOID_VARIATION_VALIDATED
Author: James P Rice Jr.
Target: Health Affairs / Internal evidence report
Status: INIT
Report Type: REAL_WORLD_EVIDENCE

## PIPELINE CONFIGURATION
# These override the default academic prompts:
AUTHOR_PROMPT: prompts/05_author_rwe.md
PEER_REVIEWER_PROMPT: prompts/06_peer_reviewer_rwe.md
STEELMAN_PROMPT: prompts/08_steelman_rwe.md
EDITOR_PROMPT: prompts/07_editor.md
REVIEW_MODE: SINGLE_DOCUMENT
# Single-document mode: Author writes entire report, then Peer Reviewer reviews
# the whole thing, then Steelman attacks the whole thing. No M1/M2/M3/M4 milestones.

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
Pipeline: RWE REPORT — single-document with full adversarial validation
Author: Claude (Agent dispatch, prompts/05_author_rwe.md)
Peer Reviewer: Claude (Agent dispatch, prompts/06_peer_reviewer_rwe.md)
Steelman: Claude (Agent dispatch, prompts/08_steelman_rwe.md)
Editor: Claude (Agent dispatch, prompts/07_editor.md)
Review format: Markdown
ASSAY DATA: CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001

## ASSAY EVIDENCE
### ASSAY Report: CMS_OPIOID_PRESCRIBING
PATH: C:\PROJECTS\ASSAY\reports\CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001\integration_block.yaml
DATA_APPENDIX: C:\PROJECTS\ASSAY\reports\CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001\data_appendix_fragment.md

### ENHANCED ANALYSES (all pre-computed, pass to Author)
CONCENTRATION: C:\PROJECTS\ASSAY\reports\CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001\run1\outputs\concentration_metrics.json
POLICY_SIM: C:\PROJECTS\ASSAY\reports\CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001\run1\outputs\policy_simulation.json
VARIANCE_DECOMP: C:\PROJECTS\ASSAY\reports\CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001\run1\outputs\variance_decomposition.json
CROSSTAB: C:\PROJECTS\ASSAY\reports\CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001\run1\outputs\enhanced\crosstab_provider_specialty.csv
WITHIN_SPEC_IQR: C:\PROJECTS\ASSAY\reports\CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001\run1\outputs\enhanced\within_specialty_iqr.csv
VOLUME_TIERS: C:\PROJECTS\ASSAY\reports\CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001\run1\outputs\enhanced\volume_tier_analysis.csv
SPEC_GINI: C:\PROJECTS\ASSAY\reports\CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001\run1\outputs\enhanced\specialty_gini_hhi.csv
LA_OUTLIER: C:\PROJECTS\ASSAY\reports\CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001\run1\outputs\enhanced\la_ratio_by_outlier.csv
LA_PROVIDER: C:\PROJECTS\ASSAY\reports\CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001\run1\outputs\enhanced\la_ratio_by_provider.csv
SUPPRESSION: C:\PROJECTS\ASSAY\reports\CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001\run1\outputs\enhanced\suppression_sensitivity.json
WITHIN_SPEC_STATE: C:\PROJECTS\ASSAY\reports\CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001\run1\outputs\enhanced\within_specialty_state_variance.csv
OUTLIER_STATES: C:\PROJECTS\ASSAY\reports\CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001\run1\outputs\enhanced\outlier_by_state_detailed.csv
NP_VS_MD: C:\PROJECTS\ASSAY\reports\CMS_OPIOID_PRESCRIBING_2026_2026-05-15_001\run1\outputs\np_vs_md_by_state.csv

KEY COMPUTED VALUES:
  - National opioid claims rate: 4.16% [95% CI: 4.12-4.19%], N=810,057
  - State max/min ratio: 2.45x (Alabama 6.01% vs New York 2.45%)
  - Gini coefficient: 0.6892 [0.687, 0.692]
  - Top 1% of prescribers: 22.87% of all opioid claims
  - Top 5%: 45.74%, Top 10%: 58.73%
  - Variance decomposition: Specialty 36.6%, State 0.7%, Individual 62.6%
  - NP/PA vs MD ratio: 2.42x, NP higher in 45/51 states
  - Outlier providers (>3 SD): 13,913 (1.72%) → 11.5% of all opioid claims
  - Outlier LA ratio: 10.24% vs non-outlier 3.41% (3x elevation)
  - Volume-rate by specialty: Pain ↑ (22.5→51.9%), Surgery ↓ (36.8→26.3%)
  - Policy sim: 50% convergence → 1.48M fewer claims (2.6%)
  - Suppression sensitivity: 200K imputed → rate shifts 0.25pp (robust)

## Frozen Parameters

| Parameter | Value | CI | Source |
|-----------|-------|----|--------|
| National opioid rate | 4.16% | [4.12, 4.19] | CMS Part D 2023 |
| Alabama rate | 6.01% | [5.65, 6.47] | CMS Part D 2023 |
| New York rate | 2.45% | [2.38, 2.53] | CMS Part D 2023 |
| State ratio | 2.45x | — | Computed |
| Gini coefficient | 0.6892 | [0.687, 0.692] | Bootstrap, B=2000 |
| Top 1% share | 22.87% | — | Computed |
| Top 5% share | 45.74% | — | Computed |
| Specialty variance | 36.6% | — | Variance decomposition |
| State variance | 0.7% | — | Variance decomposition |
| Individual variance | 62.6% | — | Variance decomposition |
| NP/PA vs MD ratio | 2.42x | — | 45/51 states |
| Outlier count | 13,913 | — | >3 SD above specialty mean |
| Outlier claims share | 11.5% | — | 6.6M of 57.7M claims |
| Outlier LA ratio | 10.24% | — | vs 3.41% non-outlier |
| Volume-rate rho | 0.0861 | [0.0793, 0.0929] | Spearman, N=810,057 |
| Pain Q1→Q4 | 22.5%→51.9% | — | Volume quartile |
| Surgery Q1→Q4 | 36.8%→26.3% | — | Volume quartile |
| Total prescribers | 810,057 | — | CMS Part D 2023 |
| Total opioid claims | 57,728,383 | — | CMS Part D 2023 |

## Drift Risks
- Do NOT use causal language. This is observational.
- Do NOT identify individual prescribers as inappropriate.
- Do NOT claim high-rate states are "over-prescribing."
- The volume-rate correlation (0.0861) is WEAK. Do not overinterpret.
- The NP/PA finding cannot distinguish scope-of-practice from patient panel effects.
- The variance decomposition is a simple decomposition, not a causal model.
  State and specialty effects may confound (pain specialists cluster geographically).
  Acknowledge this limitation explicitly.
- Outlier LA ratio (3x) is a SIGNAL, not proof of inappropriate prescribing.

## Oracle
- The 2.45x state variation and 62.6% individual variance are the headlines.
- The volume-tier finding (pain ↑, surgery ↓) is the most surprising result.
- The 6.7:1 leverage ratio (outlier targeting) is the most actionable finding.
- The weak volume-rate correlation is a NEGATIVE finding — report honestly.
- Suppression sensitivity confirms robustness (0.25pp shift under worst case).

## PIPELINE INSTRUCTIONS

### For the Orchestrator:
1. Scaffold directory: papers/RWE_OPIOID_VARIATION_VALIDATED_[DATE]_001/
2. Copy frozen parameters to frozen_spec.md
3. Read ALL ASSAY data files listed above BEFORE dispatching Author
4. Use SINGLE_DOCUMENT mode — Author writes entire report in one pass
5. Peer Reviewer (06_peer_reviewer_rwe.md) reviews entire document (R1-R15)
6. If Peer Reviewer REJECTs: pass numbered list back to Author. Max 3 rounds.
7. Steelman (08_steelman_rwe.md) attacks entire document (A1-A12)
8. If Steelman finds FATAL flaw: Author revises. Max 2 Steelman rounds.
9. Editor (07_editor.md) reviews for prose and AI detection (E1-E24)
10. External review via run_reviews.py after pipeline completes

### What to pass to Author:
- The full RWE Author prompt (05_author_rwe.md)
- ALL frozen parameters above
- ALL ASSAY data file contents (read each file and include the data)
- Drift risks
- The report structure should match the run3 version we already produced:
  Executive Summary, Study Design, Population, Results (geographic + specialty +
  concentration + variance decomposition), Provider Type Analysis, Volume Tier
  Analysis, LA Opioid Analysis, Concentration by Specialty, Outlier Analysis,
  Policy Simulation, Sensitivity, Limitations, Clinical Implications, Data Appendix
- 7 figures (reference only, no code in body)

### What to pass to Peer Reviewer:
- The full RWE Peer Reviewer prompt (06_peer_reviewer_rwe.md)
- The Author's draft
- The frozen spec
- The ASSAY computed values (so Peer Reviewer can verify numbers match)

### What to pass to Steelman:
- The full RWE Steelman prompt (08_steelman_rwe.md)
- The Peer-Reviewer-approved draft
- The frozen spec
- Mode: FULL_REPORT

### What to pass to Editor:
- The full Editor prompt (07_editor.md)
- The Steelman-survived draft
- Steelman critique for context

## SETUP SEQUENCE
1. Create directory: papers/RWE_OPIOID_VARIATION_VALIDATED_[DATE]_001/
2. Copy frozen parameters to frozen_spec.md
3. Initialize state_vector.md
4. Run pipeline: prompts/04_paper_orchestrator.md
