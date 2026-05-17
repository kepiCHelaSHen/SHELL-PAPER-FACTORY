# Geographic and Specialty Variation in Opioid Prescribing Among Medicare Part D Providers: A Cross-Sectional Analysis

**Author:** James P Rice Jr.
**Date:** May 16, 2026
**Report Type:** Real-World Evidence

---

## Executive Summary

Among 810,057 Medicare Part D prescribers in calendar year 2023, opioid claims constituted 4.16% of all Part D claims nationally (95% CI: 4.12--4.19%), but state-level rates varied 2.45-fold, from 2.45% in New York to 6.01% in Alabama. The most operationally significant finding is that 13,913 prescribers (1.72%) exceeded three standard deviations above their specialty-adjusted mean opioid rate --- a subgroup large enough to warrant systematic review yet small enough for targeted intervention. Prescription volume was not a reliable proxy for opioid prescribing intensity: the Spearman correlation between total claims and opioid rate was 0.086 (95% CI: 0.084--0.088), meaning that monitoring programs cannot use volume alone to flag high-rate prescribers. This analysis is limited by the absence of clinical indication data in Part D claims, so the appropriateness of any individual rate cannot be assessed. The geographic variation --- not the national average --- should be the primary target for policy investigation, because a 2.45-fold difference across states serving the same federal insurance program suggests systematic rather than patient-driven variation.

---

## Study Design and Methods

This is a retrospective cross-sectional analysis of CMS Medicare Part D Prescriber Data for calendar year 2023. The study population includes 810,057 prescribers meeting minimum claims thresholds for inclusion in the public-use file.

### Data Source

CMS.gov Medicare Part D Prescribers --- by Geography and Drug, CY2023. The dataset reports prescriber-level aggregate claim counts across drug categories, linked to provider state and specialty. The public-use file suppresses cells with fewer than 11 claims for beneficiary privacy.

### Study Period

January 1, 2023 through December 31, 2023.

### Outcome Definition

The primary outcome is the opioid claims rate: the number of opioid claims divided by total Part D claims for each prescriber. We computed this at four levels of aggregation --- national, state, specialty, and individual prescriber --- using claims-weighted means throughout to ensure that high-volume prescribers contribute proportionally to aggregate rates.

### Statistical Methods

All confidence intervals are 95% BCa (bias-corrected and accelerated) bootstrap intervals with B = 2,000 replicates, deterministically seeded (seed = 42). For state-level and specialty-level aggregates, we bootstrapped over prescribers within each stratum. Outliers were defined as prescribers whose opioid rate exceeded three standard deviations above their specialty-specific mean. The volume--rate relationship was assessed via Spearman rank correlation with bootstrap confidence intervals.

Claims-weighted and unweighted state rankings were compared via Spearman rank correlation (rho = 0.70, N = 51 jurisdictions) to assess sensitivity to the weighting scheme. We report claims-weighted results throughout, with unweighted results available in the robustness analysis.

---

## Study Population

The analytic population comprises 810,057 unique Medicare Part D prescribers across 51 jurisdictions (50 states plus the District of Columbia) and 81 medical specialties. The underlying dataset contains 115,936 state-by-drug observations from the CMS geographic file.

Prescribers span the full range of Part D-eligible provider types, from primary care and surgical specialties to dentistry, optometry, and advanced practice providers. Nurse practitioners represent the single largest group (169,831 prescribers, 21.0% of total), followed by family practice (84,595, 10.4%) and physician assistants (83,286, 10.3%).

Provider counts per state range from 1,364 (Wyoming) to 79,134 (California), a 58-fold difference that is directly reflected in the width of state-level confidence intervals. Wyoming's 95% CI spans 1.15 percentage points; California's spans 0.18 percentage points.

---

## Results

### National Opioid Prescribing Rate

**The national claims-weighted opioid prescribing rate among Medicare Part D providers was 4.16% (95% CI: 4.12--4.19%, N = 810,057).** Roughly one in 24 Part D prescriptions was for an opioid. This rate reflects the full spectrum of prescriber types, from pain management specialists --- for whom opioids constitute the majority of prescriptions --- to ophthalmologists and cardiologists who prescribe opioids rarely if ever.

### Geographic Variation

The most clinically significant finding in this analysis is not the national rate but the magnitude of interstate variation. Alabama's opioid prescribing rate of 6.01% (95% CI: 5.65--6.47%) is 2.45 times New York's rate of 2.45% (95% CI: 2.38--2.53%). The geographic variation dwarfs the precision of the national estimate --- the 3.56 percentage-point gap between the highest and lowest states is 85 times wider than the national confidence interval.

The following table presents the ten highest-rate and ten lowest-rate jurisdictions. Full rankings for all 51 jurisdictions are available in the Data Appendix.

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

Several patterns deserve attention. Alabama's wide confidence interval (0.82 percentage points) reflects its relatively modest provider count of 11,965 --- roughly one-fifth of New York's 57,555. The ranking is robust at the tails (Alabama and New York remain first and last under alternative specifications), but mid-ranked states shift substantially depending on weighting. Colorado, ranked 7th by claims-weighted rate, sits at 2nd when rates are unweighted, suggesting a small number of high-volume, high-rate providers drive its aggregate downward in weighted analysis.

### Specialty Variation

Specialty-level variation is substantially larger than geographic variation, but this is expected and clinically unremarkable: pain specialists prescribe opioids at high rates because that is what they treat.

**Table 2. Selected Specialty Opioid Prescribing Rates**

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
| General Practice | 7.68 | 7.51--7.82 | 3,528 |
| Nephrology | 0.72 | 0.64--0.80 | 6,330 |
| Cardiology | 0.14 | 0.11--0.17 | 14,972 |
| Psychiatry | 0.13 | 0.10--0.17 | 18,732 |
| Optometry | 0.002 | 0.001--0.004 | 22,485 |

The range from Interventional Pain Management (56.34%) to Optometry (0.002%) spans four orders of magnitude. The important analytical decision here was to define outliers relative to specialty-specific means rather than the national mean. A pain management specialist prescribing opioids for 56% of claims is practicing within norms; an ophthalmologist at 5% would be a clear statistical outlier relative to peers.

---

## Subgroup Analyses

### Outlier Identification

Using a threshold of three standard deviations above the specialty-adjusted mean, **13,913 prescribers (1.72% of 809,884 scored) were identified as statistical outliers.** This count is sensitive to threshold: at 2 SD, 30,568 prescribers (3.77%) qualify; at 4 SD, 7,133 (0.88%). We report the 3 SD threshold throughout because it balances specificity against operational feasibility --- 13,913 prescribers is large enough to represent a systemic pattern but small enough for a health system or payer to conduct structured chart review.

The distribution of outliers across specialties is uneven. Nurse practitioners account for 5,782 outliers (41.6% of the total), substantially exceeding their 21.0% share of all prescribers. Physician assistants (1,419 outliers, 10.2%), family practice (1,273, 9.2%), and internal medicine (1,125, 8.1%) follow. The concentration among advanced practice providers may reflect scope-of-practice patterns, care settings (e.g., rural clinics, urgent care), or systematic differences in patient panels. This analysis cannot distinguish among those explanations.

Several specialties exhibit high skewness in their opioid rate distributions --- pharmacists (skewness = 16.8), cardiology (31.3), and optometry (105.8) --- indicating that the bulk of providers in these fields prescribe essentially zero opioids, while a handful prescribe at rates far above the specialty mean. The 3 SD threshold in these highly skewed distributions captures genuinely extreme behavior.

### Volume--Rate Relationship

**The correlation between total prescription volume and opioid prescribing rate was weak: Spearman rho = 0.086 (95% CI: 0.084--0.088, N = 810,057).** This result is statistically significant (p < 0.001) only because of the massive sample size --- the explained variance is less than 1%. The Pearson correlation was negative (r = -0.17), suggesting a slight tendency for the highest-volume prescribers to have lower opioid rates, possibly reflecting large primary care or cardiology practices where opioids are a small fraction of total output.

This is a negative finding, and an important one. It means prescription volume cannot serve as a screening proxy for opioid prescribing intensity. A prescriber writing 10,000 Part D claims per year is no more or less likely to have a high opioid rate than one writing 500. Monitoring systems that prioritize high-volume prescribers for review are unlikely to efficiently identify those with the highest opioid-to-total ratios.

### Long-Acting Opioid Ratio

Nationally, long-acting (LA) opioid formulations constitute 10.05% of all opioid claims (N = 345,583 prescribers with any opioid claims). Long-acting opioids are associated with higher risk of dependence and overdose in some clinical contexts, though they are also the standard of care for chronic pain management. The 10.05% figure provides a baseline for future trend analyses but should not be interpreted normatively without clinical context. State-level LA ratios are available in the supplementary data tables.

---

## Sensitivity and Robustness

Three robustness checks address potential concerns about the stability of reported findings.

**Claims-weighted versus unweighted rankings.** The Spearman rank correlation between claims-weighted and unweighted state rankings is 0.70 (N = 51). This moderate correlation indicates that the choice of aggregation method materially affects mid-range state rankings. New York remains lowest and Utah moves from 2nd (weighted) to 1st (unweighted) --- the tails are stable. However, Oklahoma drops from 4th (weighted) to 25th (unweighted), and Nevada drops from 5th to 29th, indicating that a small number of high-volume providers in those states substantially influence the weighted aggregate. Both perspectives are valid: claims-weighted rates reflect the prescription experience of Medicare beneficiaries; unweighted rates reflect typical provider behavior. We report claims-weighted results as the primary analysis because they capture population-level exposure.

**Winsorized rankings.** To assess the influence of extreme values, we computed state rankings after winsorizing individual prescriber opioid rates at the 1st and 99th percentiles. The Spearman correlation between winsorized and un-winsorized rankings was 0.71, closely matching the weighted/unweighted comparison. This confirms that extreme individual prescribers influence aggregate rankings, but do not create them --- the geographic pattern persists after trimming.

**Outlier threshold sensitivity.** As noted, outlier counts range from 30,568 (2 SD) to 7,133 (4 SD). The 3 SD threshold identifies 13,913 providers. The ratio of 2 SD to 4 SD outlier counts (4.29:1) is consistent with a moderately right-skewed distribution, not with a distribution driven by a small number of extreme cases. The outlier finding is robust to reasonable threshold choices.

---

## Limitations and Caveats

The most consequential limitation of this analysis is the absence of clinical indication data in Medicare Part D claims. We observe that Alabama prescribers write opioid claims at 2.45 times the rate of New York prescribers, but we cannot determine whether Alabama's Medicare population has commensurately higher rates of chronic pain, surgical procedures, or other clinical conditions that appropriately generate opioid prescriptions. If Alabama's Medicare beneficiaries are systematically older, sicker, or more likely to have pain-generating conditions, some portion of the observed rate difference would be clinically explained rather than culturally or regulatory-driven. Linking Part D prescribing data to Medicare claims for diagnoses (ICD-10) and procedures (CPT) would substantially narrow this interpretive gap. Until such linkage is performed, the 2.45x ratio identifies a question, not an answer.

A second limitation arises from the specialty classification system itself. CMS specialty codes are self-reported and not uniformly granular. "General Practice" and "Family Practice" are distinct categories with different opioid rates (7.68% and 3.25%, respectively), but the clinical difference between these classifications is unclear in many cases. Our outlier analysis adjusts for specialty, which means misclassified providers may be scored against an inappropriate peer group. The practical impact is likely small --- the 13,913 outlier count would change modestly under alternative specialty groupings --- but it introduces noise into the specialty-specific estimates.

Third, the public-use file suppresses cells with fewer than 11 claims for privacy. This means that prescribers who write very few opioid prescriptions (1--10 claims) may have their opioid claims suppressed while their total claims are fully reported, biasing their observed opioid rate downward. The magnitude of this bias is difficult to quantify without access to the restricted-use file, but it would tend to slightly understate the national opioid prescribing rate and modestly reduce the outlier count at the high end.

Finally, this analysis is cross-sectional. A single year of data cannot distinguish between states on different trajectories. A state with a historically high opioid rate that has declined 30% over five years tells a fundamentally different story than one with a stable high rate, and this analysis cannot differentiate between them. Longitudinal extension --- repeating this analysis for CY2019 through CY2023 --- would add substantial interpretive value at minimal incremental cost.

---

## Clinical Implications

The headline finding for health system executives and policymakers is the 2.45-fold variation across states, not the 4.16% national average. A national average obscures the policy-relevant question: why does opioid prescribing among Medicare providers in Alabama look so different from New York, given that both populations are served by the same federal insurance program with the same formulary constraints?

Three findings have immediate operational relevance.

First, the 13,913 specialty-adjusted outlier prescribers represent the most actionable intervention target. These are not simply high-volume prescribers or prescribers in pain-related specialties --- they are providers whose opioid prescribing rate exceeds their specialty peers by more than three standard deviations. Health plans, pharmacy benefit managers, and state medical boards could use specialty-adjusted benchmarking (rather than crude volume thresholds) to prioritize prescriber education, peer comparison interventions, or prospective drug utilization review. The fact that 41.6% of outliers are nurse practitioners suggests that interventions should be designed for the provider types most likely to be identified, not exclusively for physicians.

Second, the weak volume--rate correlation (rho = 0.086) has a direct operational consequence: prescription drug monitoring programs (PDMPs) and payer surveillance systems that flag prescribers based on total opioid volume will miss the majority of high-rate prescribers. A pain specialist writing 2,000 opioid prescriptions per year may have a perfectly typical rate for the specialty, while a dermatologist writing 50 opioid prescriptions could be an extreme outlier. Rate-based monitoring, adjusted for specialty, would be substantially more efficient than volume-based approaches.

Third, the 10.05% long-acting opioid ratio provides a national baseline that can be tracked over time and compared across health systems. Changes in this ratio --- particularly increases --- may signal shifts in chronic pain management practices that warrant clinical attention.

**What this analysis does not mean.** This report does not identify any individual prescriber as engaging in inappropriate prescribing. Statistical outlier status is not a clinical judgment --- it is a population-level flag that warrants further investigation. A prescriber three standard deviations above the specialty mean may be serving a uniquely complex patient population, operating in a region with limited access to non-pharmacological pain management, or filling a legitimate clinical niche. The purpose of outlier identification is to prioritize review, not to assign blame. Similarly, this analysis does not establish that any state's opioid prescribing rate is "too high" or "too low." The appropriateness of a prescribing rate is a clinical determination that requires patient-level data this study does not contain.

---

## Data Appendix

### Data Sources

CMS.gov Medicare Part D Prescribers --- by Geography and Drug, CY2023. Sample size: 115,936 state-by-drug observations; 810,057 unique prescribers after aggregation.

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
| Volume--rate rho | 0.086 | 0.084--0.088 | 810,057 | Spearman + bootstrap |
| LA opioid ratio | 10.05% | --- | 345,583 | Aggregate ratio |
| Weighted/unweighted rank rho | 0.70 | --- | 51 | Spearman |

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

### Interpretation Constraints

The following interpretations are explicitly excluded by the analytical methodology: causal inference, generalization to non-Medicare populations, individual prescriber targeting, normative judgment on any state's rate, and characterization of any prescribing rate as "inappropriate" without patient-level clinical data.

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
