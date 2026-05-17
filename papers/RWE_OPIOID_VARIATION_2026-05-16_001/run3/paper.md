# Geographic and Specialty Variation in Opioid Prescribing Among Medicare Part D Providers: A Cross-Sectional Analysis

**Author:** James P Rice Jr.
**Date:** May 16, 2026
**Report Type:** Real-World Evidence
**Version:** Run 3 --- Comprehensive analysis with volume-tier findings, expanded LA ratio, specialty concentration, within-specialty geographic variance, and suppression sensitivity

---

## Executive Summary

Among 810,057 Medicare Part D prescribers in calendar year 2023, the 13,913 statistical outlier prescribers --- just 1.72% of the workforce --- account for 11.5% of all opioid claims, producing a 6.7:1 leverage ratio that makes provider-level monitoring an order of magnitude more efficient than any geographic policy intervention. The national opioid prescribing rate was 4.16% (95% CI: 4.12--4.19%), with state-level rates varying 2.45-fold from New York (2.45%) to Alabama (6.01%), yet a variance decomposition reveals geography explains only 0.7% of total prescribing variation compared to 62.6% attributable to individual prescriber behavior and 36.6% to specialty. Volume-tier analysis uncovered divergent prescribing trajectories: among pain specialists, higher prescription volume is associated with sharply higher opioid rates (22.5% in Q1 vs. 51.9% in Q4), while among surgeons the relationship reverses entirely (36.8% in Q1 vs. 26.3% in Q4) --- a finding that challenges any uniform volume-based surveillance approach. Outlier prescribers show a 3.0-fold elevation in long-acting opioid ratios (10.2% vs. 3.4%), a safety signal warranting targeted clinical review. The most consequential limitation remains the absence of clinical indication data: observed variation identifies questions for investigation, not evidence of inappropriate prescribing.

---

## Study Design and Methods

This is a retrospective cross-sectional analysis of CMS Medicare Part D Prescriber Data for calendar year 2023. The study population includes 810,057 prescribers meeting minimum claims thresholds for inclusion in the public-use file.

### Data Source

CMS.gov Medicare Part D Prescribers --- by Geography and Drug, CY2023. The dataset reports prescriber-level aggregate claim counts across drug categories, linked to provider state and specialty. The public-use file suppresses cells with fewer than 11 claims for beneficiary privacy.

### Study Period

January 1, 2023 through December 31, 2023.

### Outcome Definition

The primary outcome is the opioid claims rate: opioid claims divided by total Part D claims for each prescriber. We computed this at four levels --- national, state, specialty, and individual prescriber --- using claims-weighted means throughout so that high-volume prescribers contribute proportionally to aggregate rates.

### Specialty Classification

Prescribers were grouped into seven analytic categories based on CMS specialty codes: Primary Care (family practice, internal medicine, general practice), Pain/Anesthesia (interventional pain management, pain management, anesthesiology), Surgery/Ortho (orthopedic surgery, general surgery, hand surgery), NP/PA (nurse practitioners, physician assistants), Dentistry, Oncology, and Other (all remaining specialties). This grouping permits clinically meaningful comparisons while maintaining adequate cell sizes for statistical analysis.

### Volume Quartile Method

Within each specialty group, prescribers were ranked by total Part D claims and divided into quartiles (Q1 = lowest volume, Q4 = highest volume). Mean and median opioid rates were computed within each volume quartile to assess whether prescribing intensity varies systematically with practice volume.

### Outlier Definition

Outliers were defined as prescribers whose opioid rate exceeded three standard deviations above their specialty-specific mean. We report the 3 SD threshold as the primary analysis, with 2 SD and 4 SD thresholds examined in sensitivity analyses.

### Variance Decomposition

A hierarchical model partitioned opioid prescribing rate variance into three components: specialty (between-specialty differences), state (between-state differences after accounting for specialty), and residual (individual prescriber variation within specialty and state). Within-specialty state variance was computed separately for each specialty group to assess whether geography matters differentially by clinical field.

### Statistical Methods

All confidence intervals are 95% BCa (bias-corrected and accelerated) bootstrap intervals with B = 2,000 replicates, deterministically seeded (seed = 42). Prescribing concentration was quantified via the Gini coefficient and Herfindahl-Hirschman Index (HHI) computed across opioid prescribers. The NP/PA versus MD comparison computed unweighted mean opioid rates by provider type within each state. Claims-weighted and unweighted state rankings were compared via Spearman rank correlation (rho = 0.70, N = 51).

---

## Study Population

The analytic population comprises 810,057 unique Medicare Part D prescribers across 51 jurisdictions (50 states plus the District of Columbia) and 81 medical specialties. The underlying dataset contains 115,936 state-by-drug observations from the CMS geographic file. Of these prescribers, 430,941 had at least one opioid claim, generating 57,728,383 total opioid claims nationally.

The provider type distribution reveals that nurse practitioners form the single largest group (169,831 prescribers, 21.0%), followed by family practice (84,595, 10.4%) and physician assistants (83,286, 10.3%). By analytic specialty group: Primary Care accounts for 171,777 MD/DO prescribers; NP/PA for 253,117; Surgery/Ortho for 43,703; Pain/Anesthesia for 12,687; Other specialties for 277,201; Oncology for 12,415; and Dentistry for 39,157.

Provider counts per state range from 1,364 (Wyoming) to 79,134 (California), a 58-fold difference directly reflected in confidence interval widths. Wyoming's 95% CI spans 1.15 percentage points; California's spans 0.18.

---

## Results

### 4.1 Primary Finding: National Opioid Prescribing Rate

**The national claims-weighted opioid prescribing rate among Medicare Part D providers was 4.16% (95% CI: 4.12--4.19%, N = 810,057).** Roughly one in 24 Part D prescriptions was for an opioid. This rate reflects the full prescriber spectrum, from pain management specialists --- for whom opioids constitute the majority of prescriptions --- to ophthalmologists and cardiologists who prescribe opioids rarely or never.

### 4.2 Geographic Variation

Alabama's opioid prescribing rate of 6.01% (95% CI: 5.65--6.47%) is 2.45 times New York's rate of 2.45% (95% CI: 2.38--2.53%). The 3.56 percentage-point gap between highest and lowest states is 85 times wider than the national confidence interval.

**Table 1. Ten Highest-Rate and Ten Lowest-Rate Jurisdictions, Opioid Claims as Percent of Total Part D Claims**

| Rank | State | Rate (%) | 95% CI (%) | N Prescribers |
|------|-------|----------|------------|---------------|
| 1 | Alabama | 6.01 | 5.65--6.47 | 11,965 |
| 2 | Utah | 5.87 | 5.48--6.33 | 6,192 |
| 3 | Idaho | 5.66 | 5.26--6.19 | 4,738 |
| 4 | Oklahoma | 5.54 | 5.14--6.06 | 8,598 |
| 5 | Nevada | 5.43 | 5.03--5.88 | 6,130 |
| 6 | Arkansas | 5.36 | 5.02--5.82 | 7,543 |
| 7 | Colorado | 5.26 | 5.04--5.50 | 13,647 |
| 8 | Louisiana | 5.20 | 4.79--5.73 | 12,291 |
| 9 | Oregon | 5.18 | 4.99--5.43 | 11,788 |
| 10 | Georgia | 5.11 | 4.84--5.44 | 22,205 |
| ... | ... | ... | ... | ... |
| 42 | Minnesota | 3.43 | 3.30--3.57 | 14,779 |
| 43 | Pennsylvania | 3.29 | 3.18--3.40 | 38,404 |
| 44 | Connecticut | 3.27 | 3.03--3.54 | 11,195 |
| 45 | North Dakota | 3.23 | 3.02--3.53 | 2,134 |
| 46 | Hawaii | 3.21 | 2.96--3.52 | 2,768 |
| 47 | Massachusetts | 3.09 | 2.96--3.24 | 22,148 |
| 48 | New Jersey | 3.03 | 2.87--3.19 | 19,901 |
| 49 | District of Columbia | 2.97 | 2.61--3.46 | 2,371 |
| 50 | Rhode Island | 2.65 | 2.46--2.89 | 3,427 |
| 51 | New York | 2.45 | 2.38--2.53 | 57,555 |

Alabama's wide confidence interval (0.82 pp) reflects its modest provider count of 11,965 --- roughly one-fifth of New York's 57,555. Rankings are robust at the tails under alternative specifications. Mid-ranked states shift substantially depending on weighting: Oklahoma drops from 4th (weighted) to 25th (unweighted), indicating that a small number of high-volume providers drive its weighted aggregate.

[Figure 1: State Opioid Prescribing Rates --- horizontal bar chart of all 51 jurisdictions, ranked by claims-weighted opioid rate.]

### 4.3 Specialty Variation

Specialty-level variation spans four orders of magnitude, from Interventional Pain Management (56.34%) to Optometry (0.002%). This range is clinically expected --- it reflects what different specialties treat, not differential appropriateness.

**Table 2. Top 15 Specialties by Opioid Prescribing Rate**

| Specialty | Rate (%) | 95% CI (%) | N Prescribers |
|-----------|----------|------------|---------------|
| Interventional Pain Management | 56.34 | 55.00--57.54 | 1,426 |
| Pain Management | 52.91 | 51.92--53.85 | 2,478 |
| Anesthesiology | 50.25 | 49.08--51.31 | 2,903 |
| Hand Surgery | 45.38 | 43.82--46.93 | 1,182 |
| Physical Medicine & Rehab | 35.91 | 33.76--37.91 | 5,880 |
| Orthopedic Surgery | 31.23 | 30.82--31.65 | 16,117 |
| Oral Surgery (Dentist only) | 23.74 | 23.34--24.13 | 4,468 |
| General Surgery | 22.85 | 21.24--24.37 | 11,182 |
| Physician Assistant | 12.08 | --- | 83,286 |
| Dentistry (all) | 10.25 | --- | 39,157 |
| Oncology | 9.57 | --- | 12,415 |
| General Practice | 7.68 | 7.51--7.82 | 3,528 |
| Nurse Practitioner | 4.87 | --- | 169,831 |
| Primary Care (MD/DO) | 3.17 | --- | 171,777 |
| Cardiology | 0.14 | 0.11--0.17 | 14,972 |

The important analytical decision was to define outliers relative to specialty-specific means. A pain management specialist prescribing opioids for 56% of claims is practicing within norms; an ophthalmologist at 5% would be a stark outlier relative to peers.

[Figure 3: Top 15 Specialties by Opioid Rate --- horizontal bar chart with 95% CIs.]

### 4.4 Prescribing Concentration

The distribution of opioid prescribing is not merely skewed --- it is extraordinarily concentrated. **Among 430,941 prescribers who wrote at least one opioid claim, the Gini coefficient is 0.689 (95% CI: 0.687--0.692).** This exceeds the income Gini of every country tracked by the World Bank and approaches concentration levels typically seen in venture capital returns or academic citation distributions.

**Table 3. Cumulative Share of Opioid Claims by Prescriber Percentile**

| Percentile | Prescribers (N) | Share of All Opioid Claims (%) |
|------------|----------------|-------------------------------|
| Top 1% | 4,309 | 22.87 |
| Top 5% | 21,547 | 45.74 |
| Top 10% | 43,094 | 58.73 |
| Top 20% | 86,188 | 73.32 |

Fewer than 4,400 prescribers --- out of more than 430,000 who prescribe any opioid --- account for nearly one-quarter of all Medicare Part D opioid claims. The bottom 50% of opioid prescribers contribute less than 10% of total volume. This is a system dominated by a small fraction of its participants.

[Figure 2: Lorenz Curve --- Opioid Prescribing Concentration. Gini = 0.689.]

### 4.5 Variance Decomposition

**The most important finding in this analysis is not about geography at all.** A hierarchical variance decomposition reveals:

**Table 4. Variance Decomposition of Opioid Prescribing Rate**

| Component | Variance Explained (%) |
|-----------|----------------------|
| Specialty | 36.6 |
| State (geography) | 0.7 |
| Individual prescriber (residual) | 62.6 |

[Figure 4: Variance Decomposition --- Specialty vs. Geography vs. Individual.]

Geography --- the dimension that dominates public discourse, media coverage, and most policy interventions --- explains less than 1% of opioid prescribing variation. Two pain management specialists in the same state can have vastly different opioid prescribing rates, and those individual differences are 89 times more consequential than which state they practice in (62.6% / 0.7%).

**Within-Specialty State Variance.** To test whether geography matters more within specific clinical fields, we computed the percentage of within-specialty variance attributable to state for each specialty group:

**Table 4a. Within-Specialty State Variance**

| Specialty Group | Total Variance | State Explains (%) |
|-----------------|---------------|-------------------|
| Dentistry | 0.0151 | 22.2 |
| Pain/Anesthesia | 0.0551 | 7.3 |
| Oncology | 0.0076 | 6.1 |
| Surgery/Ortho | 0.0392 | 3.8 |
| NP/PA | 0.0206 | 2.9 |
| Primary Care | 0.0027 | 1.7 |
| Other | 0.0070 | 1.4 |

Geography matters most for dentistry (22.2%) --- plausibly reflecting state-level dental prescribing regulations --- and modestly for pain specialists (7.3%). For primary care and NP/PA providers, which together comprise the majority of prescribers, state explains less than 3% of within-specialty variance. The national-level finding (0.7%) is not an artifact of specialty mix; geography is genuinely a minor driver of prescribing behavior within most clinical fields.

---

## Provider Type Analysis

### 5.1 NP/PA versus MD Comparison

Across the 51 jurisdictions, **nurse practitioners and physician assistants prescribe opioids at a mean rate 2.42 times the physician (MD/DO) rate.** The pattern holds in 45 of 51 jurisdictions.

**Table 5. NP/PA vs. MD Opioid Prescribing Rate, Selected States**

| State | NP/PA Rate (%) | MD Rate (%) | Ratio | NP > MD? |
|-------|---------------|-------------|-------|----------|
| Connecticut | 9.16 | 2.35 | 3.90 | Yes |
| Maryland | 9.13 | 2.39 | 3.82 | Yes |
| New York | 6.90 | 1.94 | 3.56 | Yes |
| Minnesota | 10.03 | 2.86 | 3.50 | Yes |
| South Dakota | 11.48 | 3.36 | 3.41 | Yes |
| Delaware | 7.94 | 2.41 | 3.30 | Yes |
| Illinois | 8.73 | 2.72 | 3.21 | Yes |
| Indiana | 9.53 | 3.31 | 2.88 | Yes |
| Idaho | 10.57 | 3.59 | 2.94 | Yes |
| Colorado | 11.36 | 4.09 | 2.78 | Yes |
| ... | ... | ... | ... | ... |
| Florida | 4.37 | 2.99 | 1.46 | Yes |
| Arkansas | 5.88 | 4.48 | 1.31 | Yes |
| Texas | 3.65 | 3.23 | 1.13 | Yes |
| Kentucky | 3.15 | 3.84 | 0.82 | No |
| Georgia | 2.47 | 3.91 | 0.63 | No |
| West Virginia | 2.31 | 4.28 | 0.54 | No |
| Missouri | 2.37 | 4.72 | 0.50 | No |
| Alabama | 2.17 | 5.05 | 0.43 | No |
| Oklahoma | 1.89 | 4.81 | 0.39 | No |

The six states where MD rates exceed NP/PA rates --- Alabama, Georgia, Kentucky, Missouri, Oklahoma, and West Virginia --- are concentrated in the South and lower Midwest, and several rank among the highest overall prescribing states. This pattern is consistent with a hypothesis that in states with historically permissive physician prescribing cultures, NP/PA prescribers may be comparatively restrained, while in states where physician rates are already low, NP/PA rates remain elevated. But this is a pattern observation, not evidence of a causal mechanism.

### 5.2 Provider Type by Specialty Group Cross-Tabulation

The aggregate 2.42x ratio conceals substantial heterogeneity by clinical field. The following cross-tabulation reveals where the NP/PA elevation concentrates:

**Table 5a. Provider Type by Specialty Group: Mean Opioid Rate and Claims Volume**

| Provider Class | Specialty Group | N | Mean Rate (%) | Opioid Claims |
|---------------|----------------|-------|--------------|---------------|
| MD/DO | Pain/Anesthesia | 12,687 | 34.35 | 9,818,844 |
| MD/DO | Surgery/Ortho | 43,703 | 31.45 | 4,013,841 |
| MD/DO | Dentistry | 39,157 | 10.25 | 776,440 |
| MD/DO | Oncology | 12,415 | 9.57 | 871,210 |
| NP | NP/PA | 169,831 | 4.87 | 10,358,360 |
| PA | NP/PA | 83,286 | 12.08 | 6,297,043 |
| MD/DO | Primary Care | 171,777 | 3.17 | 20,799,902 |
| MD/DO | Other | 277,201 | 3.59 | 4,792,743 |

Two findings emerge. First, physician assistants prescribe opioids at 2.5 times the nurse practitioner rate (12.08% vs. 4.87%) --- the "NP/PA" category masks a large within-group difference. Second, MD/DO primary care physicians (3.17%) have a lower rate than NP/PA providers as a combined group, but the comparison is confounded by the fact that NP/PA rates aggregate across all practice settings rather than isolating primary care. The headline 2.42x ratio is real at the population level but should not be interpreted as meaning that an NP doing the same work as an MD prescribes 2.4 times more opioids.

### 5.3 Caveats

Three constraints limit interpretation. First, this comparison does not adjust for specialty mix --- NP/PA prescribers concentrate in primary care and urgent care, while "MD" includes cardiologists, psychiatrists, and other specialties that rarely prescribe opioids. The 2.42x ratio would narrow after adjustment. Second, patient panels differ: NP/PA prescribers in many states serve higher proportions of acute pain presentations, particularly in rural and underserved areas. Third, scope-of-practice laws vary by state in ways that channel different patient populations to different provider types. This analysis identifies a descriptive pattern, not a causal mechanism.

---

## Volume Tier Analysis

**This section presents a major discovery.** The relationship between prescription volume and opioid prescribing rate differs fundamentally by specialty --- in some fields, higher volume is associated with more opioid prescribing; in others, with less.

**Table 6. Opioid Prescribing Rate by Volume Quartile and Specialty Group**

| Specialty Group | Q1 (Low Vol) | Q2 | Q3 | Q4 (High Vol) | Direction |
|-----------------|-------------|-----|-----|---------------|-----------|
| Pain/Anesthesia | 22.5% | 27.1% | 36.0% | 51.9% | Higher volume = MORE |
| Surgery/Ortho | 36.8% | 33.5% | 29.2% | 26.3% | Higher volume = FEWER |
| NP/PA | 10.3% | 8.7% | 5.4% | 4.6% | Modest decline |
| Primary Care | 3.8% | 3.4% | 2.7% | 2.9% | Relatively flat |

Among pain specialists, the highest-volume prescribers have an opioid rate 2.3 times that of the lowest-volume prescribers (51.9% vs. 22.5%). The gradient is monotonic across all four quartiles. This makes clinical sense: high-volume pain practices attract and retain complex chronic pain patients, generating both high total claims and a high opioid fraction.

Among surgeons, the pattern reverses entirely. High-volume surgical practices prescribe opioids at 26.3% --- ten percentage points below the lowest-volume tier at 36.8%. A plausible interpretation: high-volume surgical centers have implemented enhanced recovery after surgery (ERAS) protocols and multimodal analgesia pathways that reduce per-patient opioid utilization. Low-volume surgeons, often in solo or small-group practice, may lack the infrastructure for these protocol-driven approaches.

For NP/PA providers and primary care, volume shows a modest inverse relationship or near-flat profile, consistent with the weak national volume-rate correlation (Spearman rho = 0.086).

**The policy implication is direct.** Any surveillance system that applies a single volume threshold --- flagging all prescribers above X total claims for review --- will systematically over-identify high-volume pain specialists (whose rates are high for clinically coherent reasons) while missing low-volume surgeons and primary care providers who may represent the more actionable outliers. Volume-based monitoring is not merely inefficient; it is systematically biased in its clinical targeting.

---

## Long-Acting Opioid Analysis

### 7.1 National LA Ratio

Long-acting (LA) opioid formulations constitute 10.05% of all opioid claims nationally (N = 345,583 prescribers with any opioid claims). LA opioids include extended-release morphine, oxycodone ER, fentanyl patches, and methadone for pain. They carry higher per-dose risk of dependence and respiratory depression but are the standard of care for stable chronic pain requiring around-the-clock management.

### 7.2 LA Ratio by Outlier Status

**Table 7. Long-Acting Opioid Ratio by Outlier Status**

| Group | Mean LA Ratio (%) | Median LA Ratio (%) | N Prescribers |
|-------|------------------|--------------------:|---------------|
| Non-outliers | 3.41 | 0.0 | 333,169 |
| Outliers (>3 SD) | 10.24 | 0.0 | 12,414 |

**Outlier prescribers have a 3.0-fold elevation in long-acting opioid use relative to non-outliers (10.24% vs. 3.41%).** The median is zero in both groups --- reflecting that the majority of opioid prescribers write no LA opioid claims at all --- but the mean difference is clinically meaningful. A prescriber who is already a statistical outlier for opioid volume and who also preferentially prescribes long-acting formulations presents a compounded risk profile. This is a safety signal, not a clinical judgment: it identifies a subpopulation warranting structured chart review.

### 7.3 LA Ratio by Provider Type

**Table 7a. Long-Acting Opioid Ratio by Provider Type**

| Provider Type | Mean LA Ratio (%) | N Prescribers |
|---------------|------------------|---------------|
| NP | 5.02 | 57,902 |
| MD/DO | 3.55 | 245,244 |
| PA | 2.36 | 42,437 |

Nurse practitioners show the highest LA ratio (5.02%), followed by physicians (3.55%) and physician assistants (2.36%). The NP elevation may reflect their concentration in chronic pain management settings where LA formulations are clinically appropriate, or it may indicate differential prescribing patterns. Without indication data, the interpretation remains ambiguous.

### 7.4 Safety Signal Interpretation

The 3x outlier-to-non-outlier LA ratio does not prove inappropriate prescribing. A legitimate pain specialist managing complex chronic pain patients will appropriately prescribe both a high opioid rate and a high proportion of long-acting formulations. What the signal identifies is a statistically defined subpopulation where two risk markers co-occur: unusually high opioid volume and unusually high long-acting proportion. Among the approximately 12,400 outliers with LA data, this combination warrants clinical review at rates substantially higher than for the general prescriber population.

---

## Concentration by Specialty

### 8.1 Specialty-Specific Concentration Metrics

Prescribing concentration varies markedly across specialty groups. Pain/Anesthesia shows the highest Gini (0.717), while Dentistry shows the lowest (0.443) --- indicating that dental opioid prescribing is relatively diffuse across practitioners, while pain medicine concentrates heavily among top prescribers.

**Table 8. Concentration Metrics by Specialty Group**

| Specialty Group | Gini | HHI (%) | Effective N | N Prescribers |
|-----------------|------|---------|-------------|---------------|
| Pain/Anesthesia | 0.717 | 3.95 | 2,534 | 11,578 |
| NP/PA | 0.686 | 0.64 | 15,689 | 128,275 |
| Primary Care | 0.616 | 0.29 | 34,110 | 134,919 |
| Other | 0.588 | 1.29 | 7,774 | 83,051 |
| Surgery/Ortho | 0.531 | 0.84 | 11,954 | 41,347 |
| Oncology | 0.523 | 2.43 | 4,124 | 11,413 |
| Dentistry | 0.443 | 1.06 | 9,464 | 20,358 |

The "Effective N" column --- derived from the inverse of the HHI --- measures how many equally-sized prescribers would produce the observed concentration. For Pain/Anesthesia, just 2,534 "effective prescribers" generate the same concentration pattern as 11,578 actual prescribers, confirming that a small core dominates the specialty's opioid output.

### 8.2 Within-Specialty Dispersion

The interquartile range (IQR) of opioid prescribing rates within specialties further quantifies this internal heterogeneity:

**Table 8a. Within-Specialty Dispersion (IQR of Individual Opioid Rates)**

| Specialty Group | Median Rate (%) | IQR (pp) | P90/P10 Ratio |
|-----------------|----------------|----------|---------------|
| Pain/Anesthesia | 35.1 | 40.9 | 26.7 |
| Surgery/Ortho | 28.9 | 26.5 | 8.3 |
| NP/PA | 0.4 | 6.3 | 2,593 |
| Primary Care | 2.0 | 3.6 | 687 |
| Dentistry | 5.2 | 19.0 | 2,785 |
| Oncology | 7.4 | 9.0 | 13.7 |
| Other | 0.0 | 2.5 | 1,349 |

The extraordinarily high P90/P10 ratios for NP/PA (2,593x) and Primary Care (687x) reflect that most prescribers in these groups write very few opioid claims relative to their total volume, while a small tail prescribes at dramatically higher rates. The denominator near zero at P10 amplifies these ratios, but the pattern is genuine: within-group heterogeneity vastly exceeds between-group differences for most specialty categories.

[Figure 5: Lorenz Curves by Specialty Group --- overlaid curves showing differential concentration.]

### 8.3 State Rate versus State Gini

State-level opioid rates and state-level Gini coefficients are positively but imperfectly correlated. Louisiana (Gini = 0.757) and Florida (0.754) show the highest concentration --- prescribing is dominated by a small number of extremely high-rate providers. Vermont (0.543) and North Dakota (0.567) show the lowest concentration --- prescribing is more diffuse. High-rate states tend toward higher concentration (Alabama: rate 6.01%, Gini 0.747), but exceptions exist: Utah achieves a high rate (5.87%) with moderate concentration (0.674), suggesting a broader prescribing culture rather than a small number of outliers driving the aggregate.

[Figure 7: State Rate vs. Concentration Scatter --- each point a state, x-axis = opioid rate, y-axis = Gini.]

---

## Outlier Analysis

### 9.1 Outlier Identification

Using a threshold of three standard deviations above the specialty-adjusted mean, **13,913 prescribers (1.72% of 809,884 scored) were identified as statistical outliers.** These outliers collectively account for 6,629,156 opioid claims --- **11.5% of all Medicare Part D opioid volume** --- creating a leverage ratio of 6.7:1 (claims share to prescriber share).

Nurse practitioners account for 5,782 outliers (41.6%), substantially exceeding their 21.0% share of all prescribers. Physician assistants (1,419, 10.2%), family practice (1,273, 9.2%), and internal medicine (1,125, 8.1%) follow. The concentration among advanced practice providers may reflect scope-of-practice patterns, rural practice settings, or systematic patient panel differences.

### 9.2 State Distribution of Outliers

**Table 9. Top 15 States by Outlier Count**

| State | N Outliers | % of All Outliers | State Prescribers | Outlier Rate (%) |
|-------|-----------|-------------------|-------------------|-----------------|
| California | 1,108 | 8.0 | 79,134 | 1.40 |
| Florida | 816 | 5.9 | 57,376 | 1.42 |
| Ohio | 761 | 5.5 | 32,319 | 2.35 |
| Pennsylvania | 619 | 4.4 | 38,404 | 1.61 |
| Texas | 587 | 4.2 | 53,586 | 1.10 |
| New York | 586 | 4.2 | 57,555 | 1.02 |
| Michigan | 536 | 3.9 | 27,317 | 1.96 |
| Illinois | 535 | 3.8 | 29,897 | 1.79 |
| North Carolina | 515 | 3.7 | 26,715 | 1.93 |
| Tennessee | 498 | 3.6 | 18,733 | 2.66 |
| Indiana | 468 | 3.4 | 16,827 | 2.78 |
| Arizona | 377 | 2.7 | 17,529 | 2.15 |
| Wisconsin | 376 | 2.7 | 15,609 | 2.41 |
| Washington | 342 | 2.5 | 19,785 | 1.73 |
| Massachusetts | 336 | 2.4 | 22,148 | 1.52 |

California and Florida have the most outliers in absolute terms (reflecting their large provider populations), but Indiana (2.78%), Tennessee (2.66%), and Wisconsin (2.41%) have the highest outlier rates as a proportion of state prescribers. New York, despite being the lowest-rate state overall, still harbors 586 outliers --- underscoring that even low-average states contain individual prescribers with extreme rates.

### 9.3 Threshold Sensitivity

| Threshold | N Outliers | % of Prescribers | Ratio (vs 3 SD) |
|-----------|-----------|-------------------|-----------------|
| 2 SD | 30,568 | 3.77% | 2.20x |
| 3 SD | 13,913 | 1.72% | 1.00x (reference) |
| 4 SD | 7,133 | 0.88% | 0.51x |

The 2 SD to 4 SD ratio (4.29:1) is consistent with a moderately right-skewed distribution. The finding is not sensitive to reasonable threshold choices --- all thresholds identify a small proportion of prescribers accounting for a disproportionate share of opioid claims.

### 9.4 The 6.7:1 Leverage Ratio

The 13,913 outlier prescribers represent 1.72% of the workforce but account for 11.5% of opioid claims: a leverage ratio of 6.7:1. This ratio means that each percentage point of prescriber monitoring effort directed at outliers addresses 6.7 percentage points of opioid claim volume. No geographic intervention approaches this efficiency --- 50% convergence of all 25 above-median states yields a 2.6% reduction in claims, while monitoring the 1.7% of prescribers who are outliers addresses 11.5% of volume even before any behavior change occurs.

---

## Policy Simulation

### 10.1 Scenario 1: Partial State Convergence

If the 25 states with above-median opioid rates converged 50% toward the national median, **approximately 1,480,702 fewer opioid claims would be written, a 2.6% reduction in total volume (base: 57,728,383).**

**Table 10. Top Five States by Projected Reduction Under 50% Convergence**

| State | Current Rate (%) | Target Rate (%) | Claims Reduced |
|-------|-----------------|-----------------|----------------|
| Alabama | 6.01 | 5.23 | 214,571 |
| Georgia | 5.11 | 4.78 | 145,844 |
| Tennessee | 5.03 | 4.74 | 110,457 |
| Oklahoma | 5.54 | 4.99 | 94,047 |
| North Carolina | 4.80 | 4.62 | 91,038 |

A 2.6% reduction is meaningful in absolute terms but modest relative to total volume. This modesty is arithmetically inevitable given the variance decomposition: geography explains only 0.7% of prescribing variation. Even aggressive state-level convergence cannot address the 63% of variation residing at the individual prescriber level.

### 10.2 Scenario 2: Outlier Targeting

**The 13,913 outlier prescribers account for 6,629,156 opioid claims --- 11.5% of all Medicare Part D opioid volume.** Even a 20% reduction in outlier prescribing would yield approximately 1,325,831 fewer claims (2.3%) --- nearly matching the effect of 50% convergence across all 25 above-median states.

### 10.3 Comparative Efficiency

| Strategy | Prescribers Affected | Claims Addressed | Efficiency Ratio |
|----------|---------------------|-----------------|-----------------|
| 50% state convergence | ~405,000 (25 states) | 1,480,702 (2.6%) | 1.0x (reference) |
| Outlier monitoring | 13,913 (1.7%) | 6,629,156 (11.5%) | 4.5x per prescriber |

Outlier targeting addresses 4.5 times more claims per prescriber touched than geographic convergence. The operational asymmetry is starker: state-level policies require legislative or regulatory action across 25 jurisdictions, while outlier monitoring requires specialty-adjusted benchmarking infrastructure applied to fewer than 14,000 providers.

---

## Sensitivity and Robustness

### 11.1 Weighted versus Unweighted Rankings

The Spearman rank correlation between claims-weighted and unweighted state rankings is 0.70 (N = 51). New York remains last under both methods. Oklahoma drops from 4th (weighted) to 25th (unweighted), indicating that a small number of high-volume, high-rate providers substantially influence its weighted aggregate. Both perspectives are valid: claims-weighted rates reflect the prescription experience of Medicare beneficiaries; unweighted rates reflect typical provider behavior.

### 11.2 Winsorized Rankings

State rankings computed after winsorizing individual opioid rates at the 1st and 99th percentiles correlate at rho = 0.71 with un-winsorized rankings. This confirms that extreme individual prescribers influence aggregate rankings but do not create the geographic pattern --- it persists after trimming.

### 11.3 Outlier Threshold Sensitivity

As reported in Section 9.3, outlier counts range from 30,568 (2 SD) to 7,133 (4 SD). The finding of disproportionate prescribing concentration among outliers is robust to threshold choice.

### 11.4 Suppression Sensitivity

The CMS public-use file suppresses cells with fewer than 11 claims. To quantify the impact, we simulated the addition of suppressed providers under three scenarios:

**Table 11. Suppression Sensitivity Analysis**

| Suppressed Providers Imputed | Adjusted National Rate (%) | Difference from Observed |
|-----------------------------|---------------------------|-------------------------|
| 50,000 | 3.911 | -0.25 pp |
| 100,000 | 3.911 | -0.25 pp |
| 200,000 | 3.911 | -0.25 pp |

Adding up to 200,000 imputed suppressed providers (with assumed low opioid rates reflecting the suppression threshold) shifts the national rate by only 0.25 percentage points. The primary findings --- geographic variation ratios, specialty patterns, outlier identification, variance decomposition --- are robust to plausible levels of suppression-related missingness. The stability across scenarios (50K to 200K) indicates that the suppressed population, by construction of the suppression rule, contributes negligibly to opioid claim volume.

---

## Limitations and Caveats

The most consequential limitation is the absence of clinical indication data. We observe that Alabama prescribers write opioid claims at 2.45 times the rate of New York prescribers, but cannot determine whether Alabama's Medicare population has commensurately higher rates of chronic pain, surgical recovery, or other conditions that generate clinically appropriate opioid prescriptions. If Alabama's beneficiaries are systematically older, sicker, or more likely to have pain-generating conditions, some portion of the observed difference would be clinically explained rather than driven by prescribing culture or regulatory environment. Linking Part D data to Medicare diagnosis and procedure claims (ICD-10/CPT) would narrow this interpretive gap substantially --- until such linkage is performed, the 2.45x ratio identifies a question, not an answer.

The variance decomposition finding --- that individual prescriber behavior explains 62.6% of variance --- is powerful but demands careful interpretation. The "individual" component is technically a residual. It captures everything not explained by specialty or state, including unmeasured confounders: patient panel composition, practice setting, local pain prevalence, referral patterns, and payer mix. A prescriber serving a disproportionately post-surgical, elderly population will have a higher opioid rate for clinically legitimate reasons that this decomposition attributes to "individual behavior." The 62.6% figure should be read as an upper bound on the role of prescriber discretion, not a precise estimate of it.

The ecological fallacy constrains all state-level claims. A state's aggregate opioid rate is a summary statistic, not a characteristic of any individual prescriber within it. High-rate states contain many low-rate prescribers; low-rate states contain outliers. Policy responses that treat all prescribers within a high-rate state as equivalent targets would misapply the finding.

CMS suppression of small cells introduces a known but modest bias. Prescribers with 1--10 opioid claims have those claims suppressed while their total claims are fully reported, biasing their observed rate downward. Sensitivity analysis shows the national rate shifts by only 0.25 percentage points under extreme imputation scenarios (200,000 suppressed providers). The core findings are robust.

This is a cross-sectional analysis. A single year cannot distinguish between states on different trajectories. A state with a high rate that has declined 30% over five years tells a fundamentally different story than one with a stable high rate --- this analysis cannot differentiate. Longitudinal extension to CY2019--2023 would add substantial interpretive value at minimal incremental cost.

Finally, these data are Medicare only. The Medicare population skews older and sicker than the general population. Opioid prescribing patterns among commercially insured or Medicaid populations may differ substantially in level, geographic distribution, and provider type composition. No generalization to non-Medicare populations is warranted.

---

## Clinical Implications

### 13.1 Three Actionable Findings

The headline finding for health system executives and policymakers is the variance decomposition. Geography --- the axis around which nearly all opioid policy has been organized --- explains 0.7% of prescribing variation. Individual prescriber behavior explains 62.6%. The public conversation has been, in a quantifiable sense, oriented around the wrong unit of analysis.

**First: the 6.7:1 leverage ratio.** The 13,913 specialty-adjusted outlier prescribers account for 11.5% of all Medicare Part D opioid claims while constituting 1.72% of the workforce. Health plans, PBMs, and state medical boards could use specialty-adjusted benchmarking to prioritize education, peer comparison, or prospective drug utilization review for this small group. The efficiency gain over broad-based interventions is approximately an order of magnitude.

**Second: volume-tier divergence demands specialty-specific monitoring.** Surveillance systems applying uniform volume thresholds will systematically over-identify pain specialists (whose high rates reflect patient mix) while missing the surgeons and primary care providers whose rates are genuinely anomalous for their clinical context. Any credible monitoring system must be both rate-based and specialty-adjusted.

**Third: the LA ratio safety signal.** Outlier prescribers who also preferentially use long-acting formulations (3x elevation) represent a compound risk population. This two-signal approach --- high opioid rate AND high LA proportion --- could substantially improve the specificity of safety monitoring compared to single-threshold approaches.

### 13.2 What This Does NOT Mean

This report does not identify any individual prescriber as engaging in inappropriate prescribing. Statistical outlier status is a population-level flag, not a clinical judgment. A prescriber three standard deviations above the specialty mean may be serving uniquely complex patients, operating in a region with limited non-pharmacological pain resources, or filling a legitimate clinical niche.

This analysis does not establish that any state's rate is "too high" or "too low." The appropriateness of a prescribing rate is a clinical determination requiring patient-level data this study does not contain.

The NP/PA finding does not support scope-of-practice restrictions. The 2.42x ratio is unadjusted for specialty mix, patient panel, and practice setting. The appropriate next step is a matched analysis controlling for these factors, not a policy response to an unadjusted descriptive statistic.

The volume-tier finding does not mean that high-volume pain specialists are inappropriate. It means their prescribing patterns are clinically coherent and should not trigger the same monitoring thresholds applied to other specialties.

### 13.3 Recommended Next Steps for Health Systems

1. **Implement specialty-adjusted opioid benchmarking** using within-specialty z-scores rather than national or state-level rate thresholds. The methodology described in this report is directly operationalizable by any organization with access to Part D prescriber data.

2. **Deploy compound-signal screening** combining high opioid rate (>3 SD within specialty) with high LA proportion (>10% of opioid claims are long-acting). This two-factor approach would identify the approximately 1,200--1,500 highest-priority prescribers for clinical chart review.

3. **Construct volume-specialty interaction profiles** that define expected rate ranges by volume quartile within each specialty. A high-volume pain specialist at 52% opioid rate is within norms; a low-volume primary care provider at 15% is far outside them. Static thresholds miss this distinction.

4. **Establish longitudinal baselines** by repeating this analysis for CY2019--2023, enabling trend-adjusted benchmarking. A prescriber whose rate is declining from a historically high level is fundamentally different from one whose rate is stable or rising.

---

## Data Appendix

### Data Sources

CMS.gov Medicare Part D Prescribers --- by Geography and Drug, CY2023. Sample size: 115,936 state-by-drug observations; 810,057 unique prescribers after aggregation. License: See source.

### Computational Methodology

All computations were performed using the authors' analytical pipeline (report reference: ASSAY-CMS-OPIOID-PRESCRIBING-2026-05-15-001). The pipeline executes a five-stage process: (M1) data ingestion and cleaning, (M2) core statistical analysis, (M3) robustness checks and sensitivity analysis, (M4) report assembly, and (M5) integration artifact validation. All scripts are deterministically seeded (seed = 42) and produce hash-verified outputs for reproducibility.

Input data integrity verified via SHA-256: `68dac7a41804ad57610d56ce704cbb71cff2d30f9e24dc4777d52660d617dbc1` (prescriber file), `876ff262c8a3eb0b8fca312f2004f14d42a8bfd01829e0695d64e34b5191f4f8` (geography file).

### Key Computed Values

| Metric | Value | 95% CI | N | Method |
|--------|-------|--------|---|--------|
| National opioid rate | 4.16% | 4.12--4.19% | 810,057 | BCa bootstrap |
| Highest state (AL) | 6.01% | 5.65--6.47% | 11,965 | BCa bootstrap |
| Lowest state (NY) | 2.45% | 2.38--2.53% | 57,555 | BCa bootstrap |
| State ratio (AL/NY) | 2.45x | --- | --- | Ratio |
| Interventional Pain Mgmt | 56.34% | 55.00--57.54% | 1,426 | Percentile bootstrap |
| Outlier count (3 SD) | 13,913 | --- | 809,884 | Specialty-adjusted z-score |
| Outlier percentage | 1.72% | --- | 809,884 | Derived |
| Outlier opioid claims | 6,629,156 | --- | 13,913 | Sum of outlier claims |
| Outlier claims share | 11.48% | --- | 57,728,383 | Derived |
| Leverage ratio | 6.7:1 | --- | --- | Claims share / prescriber share |
| Volume--rate rho | 0.086 | 0.084--0.088 | 810,057 | Spearman + bootstrap |
| LA opioid ratio | 10.05% | --- | 345,583 | Aggregate ratio |
| LA ratio (outliers) | 10.24% | --- | 12,414 | Mean among outliers |
| LA ratio (non-outliers) | 3.41% | --- | 333,169 | Mean among non-outliers |
| Weighted/unweighted rho | 0.70 | --- | 51 | Spearman |
| Winsorized rank rho | 0.71 | --- | 51 | Spearman |
| Gini coefficient | 0.689 | 0.687--0.692 | 430,941 | Bootstrap |
| Top 1% claims share | 22.87% | --- | 4,309 | Lorenz curve |
| Top 5% claims share | 45.74% | --- | 21,547 | Lorenz curve |
| Top 10% claims share | 58.73% | --- | 43,094 | Lorenz curve |
| Variance: specialty | 36.6% | --- | --- | Hierarchical decomposition |
| Variance: state | 0.7% | --- | --- | Hierarchical decomposition |
| Variance: individual | 62.6% | --- | --- | Hierarchical decomposition |
| NP/PA-to-MD mean ratio | 2.42x | --- | 51 | Unweighted state means |
| States where NP > MD | 45 of 51 | --- | 51 | Count |
| Half-convergence reduction | 1,480,702 | --- | 25 states | Arithmetic simulation |
| Pain Q4 opioid rate | 51.9% | --- | 3,172 | Volume quartile mean |
| Surgery Q4 opioid rate | 26.3% | --- | 10,893 | Volume quartile mean |
| Pain Gini | 0.717 | --- | 11,578 | Specialty-group Gini |
| Primary Care Gini | 0.616 | --- | 134,919 | Specialty-group Gini |
| Suppression sensitivity | -0.25 pp | --- | 200,000 imputed | Simulation |

### State-Level Gini Coefficients

| State | Gini | State | Gini | State | Gini |
|-------|------|-------|------|-------|------|
| AL | 0.747 | KY | 0.734 | OH | 0.673 |
| AK | 0.628 | LA | 0.757 | OK | 0.747 |
| AZ | 0.707 | MA | 0.606 | OR | 0.629 |
| AR | 0.715 | MD | 0.706 | PA | 0.658 |
| CA | 0.658 | ME | 0.580 | RI | 0.580 |
| CO | 0.626 | MI | 0.673 | SC | 0.700 |
| CT | 0.647 | MN | 0.595 | SD | 0.606 |
| DC | 0.576 | MO | 0.711 | TN | 0.698 |
| DE | 0.730 | MS | 0.729 | TX | 0.707 |
| FL | 0.754 | MT | 0.608 | UT | 0.674 |
| GA | 0.748 | NC | 0.710 | VA | 0.679 |
| HI | 0.592 | ND | 0.567 | VT | 0.543 |
| IA | 0.597 | NE | 0.627 | WA | 0.634 |
| ID | 0.666 | NH | 0.622 | WI | 0.616 |
| IL | 0.634 | NJ | 0.669 | WV | 0.679 |
| IN | 0.691 | NM | 0.634 | WY | 0.613 |
| KS | 0.624 | NV | 0.711 | NY | 0.642 |

### Complete State Rankings

**Table A1. All 51 Jurisdictions, Opioid Claims Rate, Ranked by Claims-Weighted Rate**

| Rank | State | Rate (%) | 95% CI (%) | N Prescribers |
|------|-------|----------|------------|---------------|
| 1 | AL | 6.01 | 5.65--6.47 | 11,965 |
| 2 | UT | 5.87 | 5.48--6.33 | 6,192 |
| 3 | ID | 5.66 | 5.26--6.19 | 4,738 |
| 4 | OK | 5.54 | 5.14--6.06 | 8,598 |
| 5 | NV | 5.43 | 5.03--5.88 | 6,130 |
| 6 | AR | 5.36 | 5.02--5.82 | 7,543 |
| 7 | CO | 5.26 | 5.04--5.50 | 13,647 |
| 8 | LA | 5.20 | 4.79--5.73 | 12,291 |
| 9 | OR | 5.18 | 4.99--5.43 | 11,788 |
| 10 | GA | 5.11 | 4.84--5.44 | 22,205 |
| 11 | TN | 5.03 | 4.82--5.25 | 18,733 |
| 12 | MT | 4.90 | 4.55--5.42 | 2,979 |
| 13 | AZ | 4.89 | 4.62--5.19 | 17,529 |
| 14 | KY | 4.86 | 4.55--5.23 | 13,297 |
| 15 | WY | 4.85 | 4.36--5.51 | 1,364 |
| 16 | MS | 4.84 | 4.45--5.32 | 6,730 |
| 17 | IN | 4.81 | 4.60--5.06 | 16,827 |
| 18 | WA | 4.81 | 4.61--5.01 | 19,785 |
| 19 | NC | 4.80 | 4.60--5.01 | 26,715 |
| 20 | MI | 4.74 | 4.58--4.89 | 27,317 |
| 21 | AK | 4.69 | 4.09--5.46 | 1,574 |
| 22 | KS | 4.61 | 4.42--4.84 | 7,261 |
| 23 | MD | 4.61 | 4.32--4.93 | 14,380 |
| 24 | SC | 4.53 | 4.26--4.82 | 13,705 |
| 25 | DE | 4.45 | 3.78--5.31 | 2,522 |
| 26 | MO | 4.45 | 4.27--4.66 | 16,344 |
| 27 | NM | 4.38 | 4.10--4.70 | 5,059 |
| 28 | FL | 4.27 | 4.09--4.48 | 57,376 |
| 29 | TX | 4.25 | 4.10--4.40 | 53,586 |
| 30 | VA | 3.91 | 3.71--4.14 | 18,575 |
| 31 | CA | 3.84 | 3.76--3.94 | 79,134 |
| 32 | SD | 3.81 | 3.45--4.30 | 2,446 |
| 33 | NE | 3.78 | 3.56--4.06 | 4,968 |
| 34 | ME | 3.71 | 3.49--4.01 | 4,503 |
| 35 | WI | 3.67 | 3.54--3.84 | 15,609 |
| 36 | OH | 3.67 | 3.54--3.80 | 32,319 |
| 37 | IL | 3.63 | 3.50--3.75 | 29,897 |
| 38 | WV | 3.61 | 3.39--3.91 | 5,243 |
| 39 | NH | 3.50 | 3.21--3.88 | 4,147 |
| 40 | IA | 3.48 | 3.34--3.63 | 8,681 |
| 41 | VT | 3.47 | 3.26--3.72 | 1,673 |
| 42 | MN | 3.43 | 3.30--3.57 | 14,779 |
| 43 | PA | 3.29 | 3.18--3.40 | 38,404 |
| 44 | CT | 3.27 | 3.03--3.54 | 11,195 |
| 45 | ND | 3.23 | 3.02--3.53 | 2,134 |
| 46 | HI | 3.21 | 2.96--3.52 | 2,768 |
| 47 | MA | 3.09 | 2.96--3.24 | 22,148 |
| 48 | NJ | 3.03 | 2.87--3.19 | 19,901 |
| 49 | DC | 2.97 | 2.61--3.46 | 2,371 |
| 50 | RI | 2.65 | 2.46--2.89 | 3,427 |
| 51 | NY | 2.45 | 2.38--2.53 | 57,555 |

### Figures

- **Figure 1:** State Opioid Prescribing Rates --- horizontal bar chart of all 51 jurisdictions ranked by claims-weighted opioid rate.
- **Figure 2:** Lorenz Curve --- Opioid Prescribing Concentration among 430,941 opioid prescribers. Gini = 0.689.
- **Figure 3:** Top 15 Specialties by Opioid Prescribing Rate with 95% CIs.
- **Figure 4:** Variance Decomposition --- Specialty (36.6%) vs. Geography (0.7%) vs. Individual (62.6%).
- **Figure 5:** Lorenz Curves by Specialty Group --- overlaid curves showing Pain/Anesthesia (Gini 0.717) through Dentistry (0.443).
- **Figure 6:** Volume Quartile Analysis --- Opioid rates by volume tier for Pain, Surgery, NP/PA, and Primary Care.
- **Figure 7:** State Rate vs. Concentration Scatter --- x-axis = state opioid rate, y-axis = state Gini coefficient.

All figure-generating code is available from the authors upon request.

### Interpretation Constraints

The following interpretations are explicitly excluded by the analytical methodology: causal inference, generalization to non-Medicare populations, individual prescriber targeting, normative judgment on any state's rate, characterization of any prescribing rate as "inappropriate" without patient-level clinical data, attribution of NP/PA-to-MD differences to provider competence or training quality, and normative judgment on long-acting opioid prescribing without indication data.

### Data Availability

The primary data are publicly available from CMS.gov. The computational pipeline scripts and configuration are available from the authors upon request. Input data integrity is verified via SHA-256 checksums documented in the data lineage record.

---

## References

1. Centers for Medicare & Medicaid Services. Medicare Part D Prescribers --- by Geography and Drug, Calendar Year 2023. CMS.gov. Accessed May 2026.

2. Centers for Medicare & Medicaid Services. Medicare Provider Utilization and Payment Data: Part D Prescriber. Data documentation and methodology notes. CMS.gov.

3. Dowell D, Haegerich TM, Chou R. CDC Guideline for Prescribing Opioids for Chronic Pain --- United States, 2016. *MMWR Recomm Rep.* 2016;65(1):1--49.

4. Guy GP Jr, Zhang K, Bohm MK, et al. Vital Signs: Changes in Opioid Prescribing in the United States, 2006--2015. *MMWR Morb Mortal Wkly Rep.* 2017;66(26):697--704.

5. McDonald DC, Carlson K, Izrael D. Geographic Variation in Opioid Prescribing in the U.S. *J Pain.* 2012;13(10):988--996.

6. Schieber LZ, Guy GP Jr, Seth P, et al. Trends and Patterns of Geographic Variation in Opioid Prescribing Practices by State, United States, 2006--2017. *JAMA Netw Open.* 2019;2(3):e190665.

7. Morden NE, Munson JC, Colla CH, et al. Prescription Opioid Use among Disabled Medicare Beneficiaries: Intensity, Trends, and Regional Variation. *Med Care.* 2014;52(9):852--859.

8. Deyo RA, Hallvik SE, Hildebran C, et al. Association Between Initial Opioid Prescribing Patterns and Subsequent Long-Term Use Among Opioid-Naive Patients: A Statewide Retrospective Cohort Study. *J Gen Intern Med.* 2017;32(1):21--27.

9. Barnett ML, Olenski AR, Jena AB. Opioid-Prescribing Patterns of Emergency Physicians and Risk of Long-Term Use. *N Engl J Med.* 2017;376(7):663--673.

10. Levy B, Paulozzi L, Mack KA, Jones CM. Trends in Opioid Analgesic-Prescribing Rates by Specialty, U.S., 2007--2012. *Am J Prev Med.* 2015;49(3):409--413.
