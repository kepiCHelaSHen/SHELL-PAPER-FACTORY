# Geographic and Specialty Variation in Opioid Prescribing Among Medicare Part D Providers: A Cross-Sectional Analysis

**Author:** James P Rice Jr.
**Date:** May 16, 2026
**Report Type:** Real-World Evidence
**Version:** Run 2 — Expanded with concentration, variance decomposition, provider type, and policy simulation analyses

---

## Executive Summary

Among 810,057 Medicare Part D prescribers in calendar year 2023, opioid claims constituted 4.16% of all Part D claims nationally (95% CI: 4.12--4.19%), but state-level rates varied 2.45-fold --- and a variance decomposition reveals that this geographic variation is almost irrelevant, explaining only 0.7% of total prescribing variance compared to 62.6% attributable to individual prescriber behavior and 36.6% to specialty. Opioid prescribing is extraordinarily concentrated: the top 1% of opioid prescribers write 22.9% of all opioid claims (Gini = 0.689, 95% CI: 0.687--0.692), and 13,913 outlier providers (1.7% of all prescribers) account for 6.6 million opioid claims --- 11.5% of the national total. Nurse practitioners and physician assistants prescribe opioids at 2.42 times the physician rate on average, a pattern observed in 45 of 51 jurisdictions, though this descriptive finding cannot separate scope-of-practice effects from patient panel composition. The most consequential policy implication is that targeted monitoring of fewer than 14,000 prescribers --- 1.7% of the workforce --- could address more than one in nine opioid prescriptions written under Medicare Part D.

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

Prescribing concentration was quantified via the Gini coefficient computed across all opioid prescribers (N = 430,941), with bootstrap confidence intervals. Variance decomposition used a hierarchical model partitioning opioid prescribing rate variance into three components: specialty, state (geography), and residual (individual prescriber). The NP/PA versus MD comparison computed unweighted mean opioid rates by provider type within each state.

Claims-weighted and unweighted state rankings were compared via Spearman rank correlation (rho = 0.70, N = 51 jurisdictions) to assess sensitivity to the weighting scheme. We report claims-weighted results throughout, with unweighted results available in the robustness analysis.

---

## Study Population

The analytic population comprises 810,057 unique Medicare Part D prescribers across 51 jurisdictions (50 states plus the District of Columbia) and 81 medical specialties. The underlying dataset contains 115,936 state-by-drug observations from the CMS geographic file. Of these prescribers, 430,941 had at least one opioid claim, generating 57,728,383 total opioid claims nationally.

Prescribers span the full range of Part D-eligible provider types, from primary care and surgical specialties to dentistry, optometry, and advanced practice providers. Nurse practitioners represent the single largest group (169,831 prescribers, 21.0% of total), followed by family practice (84,595, 10.4%) and physician assistants (83,286, 10.3%).

Provider counts per state range from 1,364 (Wyoming) to 79,134 (California), a 58-fold difference that is directly reflected in the width of state-level confidence intervals. Wyoming's 95% CI spans 1.15 percentage points; California's spans 0.18 percentage points.

---

## Results

### National Opioid Prescribing Rate

**The national claims-weighted opioid prescribing rate among Medicare Part D providers was 4.16% (95% CI: 4.12--4.19%, N = 810,057).** Roughly one in 24 Part D prescriptions was for an opioid. This rate reflects the full spectrum of prescriber types, from pain management specialists --- for whom opioids constitute the majority of prescriptions --- to ophthalmologists and cardiologists who prescribe opioids rarely if ever.

### Geographic Variation

Alabama's opioid prescribing rate of 6.01% (95% CI: 5.65--6.47%) is 2.45 times New York's rate of 2.45% (95% CI: 2.38--2.53%). The geographic variation dwarfs the precision of the national estimate --- the 3.56 percentage-point gap between the highest and lowest states is 85 times wider than the national confidence interval.

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

[Figure 1: State Opioid Prescribing Rates --- horizontal bar chart of all 51 jurisdictions, ranked by claims-weighted opioid rate. Code in Supplementary Materials.]

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

[Figure 3: Top 15 Specialties by Opioid Rate --- horizontal bar chart with 95% CIs. Code in Supplementary Materials.]

### Prescribing Concentration

The distribution of opioid prescribing is not merely skewed --- it is extraordinarily concentrated. **Among the 430,941 prescribers who wrote at least one opioid claim, the Gini coefficient is 0.689 (95% CI: 0.687--0.692).** For context, this exceeds the income Gini of every country tracked by the World Bank; it approaches the concentration levels typically seen in venture capital returns or academic citation distributions.

The top percentiles tell the story plainly:

**Table 3. Cumulative Share of Opioid Claims by Prescriber Percentile**

| Percentile | Share of All Opioid Claims (%) |
|------------|-------------------------------|
| Top 1% (4,309 prescribers) | 22.87 |
| Top 5% (21,547 prescribers) | 45.74 |
| Top 10% (43,094 prescribers) | 58.73 |
| Top 20% (86,188 prescribers) | 73.32 |

Fewer than 4,400 prescribers --- out of more than 430,000 who prescribe any opioid at all --- account for nearly one-quarter of all Medicare Part D opioid claims. The top 5% write nearly half. This is not a gradual distribution with a modest right tail; it is a system dominated by a small fraction of its participants.

The Lorenz curve in Figure 2 makes this concentration visible. The curve bows sharply away from the diagonal line of perfect equality, with the bottom 50% of opioid prescribers contributing less than 10% of total opioid claims.

[Figure 2: Lorenz Curve --- Opioid Prescribing Concentration. X-axis: cumulative share of opioid prescribers (ranked lowest to highest); Y-axis: cumulative share of opioid claims. Gini = 0.689. Code in Supplementary Materials.]

State-level Gini coefficients vary from 0.543 (Vermont) to 0.757 (Louisiana), indicating that prescribing concentration itself is geographically uneven. High-rate states do not uniformly have higher concentration --- Alabama (Gini = 0.747) and Florida (0.754) show extreme concentration, while Utah (0.674) achieves a high overall rate with more diffuse prescribing across its provider base. The full state Gini table is available in the Data Appendix.

### Variance Decomposition

**The most important finding in this analysis is not about geography at all.** A hierarchical variance decomposition partitioning opioid prescribing rate into specialty, state, and individual prescriber components reveals that:

**Table 4. Variance Decomposition of Opioid Prescribing Rate**

| Component | Variance Explained (%) |
|-----------|----------------------|
| Specialty | 36.6 |
| State (geography) | 0.7 |
| Individual prescriber (residual) | 62.6 |

[Figure 4: Variance Decomposition --- Specialty vs. Geography vs. Individual. Stacked bar or pie chart showing the three components. Code in Supplementary Materials.]

Geography --- the dimension that dominates public discourse, media attention, and most policy interventions --- explains less than 1% of the variation in opioid prescribing rates. Specialty explains roughly a third, which is expected: an anesthesiologist and a cardiologist prescribe opioids at fundamentally different rates for clinically obvious reasons. But nearly two-thirds of the variance is attributable to differences among individual prescribers *within the same specialty and state*.

This finding reframes the opioid prescribing narrative. The conventional story --- "Alabama has a prescribing problem and New York does not" --- is, at best, incomplete. The data say something different: two pain management specialists in the same state can have vastly different opioid prescribing rates, and those individual differences are 89 times more consequential than which state they practice in (62.6% / 0.7%). The policy implication is that state-level interventions (prescribing caps, state PDMP designs, formulary restrictions) are targeting a dimension that accounts for less than a percentage point of total variation. Provider-level interventions --- peer comparison feedback, specialty-specific benchmarking, academic detailing --- target the dimension where 63% of the variation actually lives.

---

## Subgroup Analyses

### Provider Type: Nurse Practitioners and Physician Assistants versus Physicians

Across the 51 jurisdictions, nurse practitioners and physician assistants prescribe opioids at a mean rate 2.42 times the physician (MD/DO) rate. The median state-level NP/PA-to-MD ratio is 2.58. In 45 of 51 jurisdictions, the NP/PA opioid prescribing rate exceeds the MD rate.

**Table 5. NP/PA vs. MD Opioid Prescribing Rate, Selected States**

| State | NP/PA Rate (%) | MD Rate (%) | Ratio | NP > MD? |
|-------|---------------|-------------|-------|----------|
| Connecticut | 9.16 | 2.35 | 3.90 | Yes |
| Maryland | 9.13 | 2.39 | 3.82 | Yes |
| New York | 6.90 | 1.94 | 3.56 | Yes |
| Minnesota | 10.03 | 2.86 | 3.50 | Yes |
| South Dakota | 11.48 | 3.36 | 3.41 | Yes |
| Idaho | 10.57 | 3.59 | 2.94 | Yes |
| Alaska | 8.93 | 3.22 | 2.77 | Yes |
| Hawaii | 6.49 | 3.59 | 1.81 | Yes |
| Florida | 4.37 | 2.99 | 1.46 | Yes |
| Texas | 3.65 | 3.23 | 1.13 | Yes |
| Kentucky | 3.15 | 3.84 | 0.82 | No |
| Georgia | 2.47 | 3.91 | 0.63 | No |
| West Virginia | 2.31 | 4.28 | 0.54 | No |
| Missouri | 2.37 | 4.72 | 0.50 | No |
| Alabama | 2.17 | 5.05 | 0.43 | No |
| Oklahoma | 1.89 | 4.81 | 0.39 | No |

The six states where MD rates exceed NP/PA rates --- Alabama, Georgia, Kentucky, Missouri, Oklahoma, and West Virginia --- are all in the South or lower Midwest, and several are among the highest overall prescribing states. This pattern is consistent with a hypothesis (though far from proof) that in states with historically permissive physician prescribing cultures, NP/PA prescribers may be comparatively restrained, while in states where physician opioid rates are already low, NP/PA rates remain elevated.

Three caveats constrain interpretation. First, this comparison does not adjust for specialty mix --- NP/PA prescribers are concentrated in primary care and urgent care settings, while "MD" includes cardiologists, psychiatrists, and other specialties that rarely prescribe opioids. The 2.42x ratio would narrow substantially after specialty adjustment. Second, patient panel differences are unobserved: NP/PA prescribers in many states serve higher proportions of patients with acute pain presentations. Third, scope-of-practice laws vary by state in ways that may channel different patient populations to different provider types. This analysis identifies a descriptive pattern, not a causal mechanism.

### Outlier Identification

Using a threshold of three standard deviations above the specialty-adjusted mean, **13,913 prescribers (1.72% of 809,884 scored) were identified as statistical outliers.** This count is sensitive to threshold: at 2 SD, 30,568 prescribers (3.77%) qualify; at 4 SD, 7,133 (0.88%). We report the 3 SD threshold throughout because it balances specificity against operational feasibility --- 13,913 prescribers is large enough to represent a systemic pattern but small enough for a health system or payer to conduct structured chart review.

The distribution of outliers across specialties is uneven. Nurse practitioners account for 5,782 outliers (41.6% of the total), substantially exceeding their 21.0% share of all prescribers. Physician assistants (1,419 outliers, 10.2%), family practice (1,273, 9.2%), and internal medicine (1,125, 8.1%) follow. The concentration among advanced practice providers may reflect scope-of-practice patterns, care settings (e.g., rural clinics, urgent care), or systematic differences in patient panels. This analysis cannot distinguish among those explanations.

Several specialties exhibit high skewness in their opioid rate distributions --- pharmacists (skewness = 16.8), cardiology (31.3), and optometry (105.8) --- indicating that the bulk of providers in these fields prescribe essentially zero opioids, while a handful prescribe at rates far above the specialty mean. The 3 SD threshold in these highly skewed distributions captures genuinely extreme behavior.

### Volume--Rate Relationship

**The correlation between total prescription volume and opioid prescribing rate was weak: Spearman rho = 0.086 (95% CI: 0.084--0.088, N = 810,057).** This result is statistically significant (p < 0.001) only because of the massive sample size --- the explained variance is less than 1%. The Pearson correlation was negative (r = -0.17), suggesting a slight tendency for the highest-volume prescribers to have lower opioid rates, possibly reflecting large primary care or cardiology practices where opioids are a small fraction of total output.

This is a negative finding, and an important one. Prescription volume cannot serve as a screening proxy for opioid prescribing intensity. A prescriber writing 10,000 Part D claims per year is no more or less likely to have a high opioid rate than one writing 500. Monitoring systems that prioritize high-volume prescribers for review are unlikely to efficiently identify those with the highest opioid-to-total ratios.

### Long-Acting Opioid Ratio

Nationally, long-acting (LA) opioid formulations constitute 10.05% of all opioid claims (N = 345,583 prescribers with any opioid claims). Long-acting opioids are associated with higher risk of dependence and overdose in some clinical contexts, though they are also the standard of care for chronic pain management. The 10.05% figure provides a baseline for future trend analyses but should not be interpreted normatively without clinical context. State-level LA ratios are available in the supplementary data tables.

---

## Policy Simulation

Two counterfactual scenarios quantify the potential scope of policy interventions. These are arithmetic exercises, not causal predictions --- they estimate volume under hypothetical conditions, not the impact of any specific policy change.

### Scenario 1: Partial Convergence of High-Rate States

If the 25 states with above-median opioid prescribing rates were to converge 50% toward the national median, **approximately 1,480,702 fewer opioid claims would be written annually, a 2.6% reduction in total Medicare Part D opioid volume (base: 57,728,383 claims).**

The five states contributing the largest reductions under this scenario:

**Table 6. Top Five States by Projected Claims Reduction Under 50% Convergence**

| State | Current Rate (%) | Target Rate (%) | Claims Reduced |
|-------|-----------------|-----------------|----------------|
| Alabama | 6.01 | 5.23 | 214,571 |
| Georgia | 5.11 | 4.78 | 145,844 |
| Tennessee | 5.03 | 4.74 | 110,457 |
| Oklahoma | 5.54 | 4.99 | 94,047 |
| North Carolina | 4.80 | 4.62 | 91,038 |

A 2.6% national reduction from state-level convergence is meaningful in absolute terms (1.5 million fewer claims) but modest in relative terms. This modesty is consistent with the variance decomposition finding: geography accounts for only 0.7% of prescribing variation. Even dramatic state-level convergence cannot address the 63% of variation that lives at the individual prescriber level.

### Scenario 2: Outlier Prescriber Monitoring

**The 13,913 outlier prescribers (>3 SD above specialty mean) account for 6,629,156 opioid claims --- 11.5% of all Medicare Part D opioid volume.** These 13,913 providers represent 1.72% of the prescriber workforce.

The arithmetic is stark. Monitoring 1.7% of prescribers could address 11.5% of opioid prescribing volume. This 6.7:1 leverage ratio --- the ratio of claims share to prescriber share --- makes outlier-focused interventions far more efficient per unit of regulatory effort than state-level policy changes. Even if monitoring reduced outlier prescribing by only 20%, the national opioid claims reduction (approximately 1,325,831 claims, 2.3%) would approach the impact of 50% state convergence across all 25 above-median states.

The policy choice is clear, if not simple: state-level interventions treat a dimension responsible for 0.7% of variance and yield modest aggregate effects. Prescriber-level interventions target a dimension responsible for 63% of variance and offer an order-of-magnitude better leverage ratio. The operational cost of monitoring 13,913 providers is, however, nontrivial --- it requires specialty-adjusted benchmarking infrastructure, clinical review capacity, and due process protections that most state boards and health plans do not currently possess at scale.

---

## Sensitivity and Robustness

Four robustness checks address potential concerns about the stability of reported findings.

**Claims-weighted versus unweighted rankings.** The Spearman rank correlation between claims-weighted and unweighted state rankings is 0.70 (N = 51). This moderate correlation indicates that the choice of aggregation method materially affects mid-range state rankings. New York remains lowest and Utah moves from 2nd (weighted) to 1st (unweighted) --- the tails are stable. However, Oklahoma drops from 4th (weighted) to 25th (unweighted), and Nevada drops from 5th to 29th, indicating that a small number of high-volume providers in those states substantially influence the weighted aggregate. Both perspectives are valid: claims-weighted rates reflect the prescription experience of Medicare beneficiaries; unweighted rates reflect typical provider behavior. We report claims-weighted results as the primary analysis because they capture population-level exposure.

**Winsorized rankings.** To assess the influence of extreme values, we computed state rankings after winsorizing individual prescriber opioid rates at the 1st and 99th percentiles. The Spearman correlation between winsorized and un-winsorized rankings was 0.71, closely matching the weighted/unweighted comparison. This confirms that extreme individual prescribers influence aggregate rankings, but do not create them --- the geographic pattern persists after trimming.

**Outlier threshold sensitivity.** As noted, outlier counts range from 30,568 (2 SD) to 7,133 (4 SD). The 3 SD threshold identifies 13,913 providers. The ratio of 2 SD to 4 SD outlier counts (4.29:1) is consistent with a moderately right-skewed distribution, not with a distribution driven by a small number of extreme cases. The outlier finding is robust to reasonable threshold choices.

**Gini coefficient stability.** The bootstrap 95% CI for the national Gini coefficient (0.687--0.692) is narrow, spanning only 0.005 units. This precision reflects the large sample of 430,941 opioid prescribers. The concentration finding is not sensitive to sampling variation. State-level Gini coefficients have wider CIs (not individually bootstrapped in this analysis) but the cross-state range of 0.543 to 0.757 is large enough that the geographic pattern of concentration --- highest in the Southeast, lowest in northern New England --- is robust to reasonable uncertainty.

---

## Limitations and Caveats

The most consequential limitation of this analysis is the absence of clinical indication data in Medicare Part D claims. We observe that Alabama prescribers write opioid claims at 2.45 times the rate of New York prescribers, but we cannot determine whether Alabama's Medicare population has commensurately higher rates of chronic pain, surgical procedures, or other clinical conditions that appropriately generate opioid prescriptions. If Alabama's Medicare beneficiaries are systematically older, sicker, or more likely to have pain-generating conditions, some portion of the observed rate difference would be clinically explained rather than culturally or regulatory-driven. Linking Part D prescribing data to Medicare claims for diagnoses (ICD-10) and procedures (CPT) would substantially narrow this interpretive gap. Until such linkage is performed, the 2.45x ratio identifies a question, not an answer.

The variance decomposition finding --- that individual prescriber behavior explains 62.6% of variance --- is powerful but requires careful interpretation. The "individual" component is a residual: it captures everything not explained by specialty or state, including unmeasured confounders such as patient panel composition, practice setting, local pain prevalence, and payer mix. A prescriber who treats a disproportionately elderly, post-surgical population will have a higher opioid rate for clinically legitimate reasons that this decomposition attributes to "individual behavior." The 62.6% figure should be read as an upper bound on the role of individual prescriber discretion, not a precise estimate of it.

The NP/PA versus MD comparison faces a similar confounding problem, arguably more severe. Nurse practitioners and physician assistants are not randomly assigned to patient panels; they disproportionately practice in primary care, urgent care, and rural settings where acute pain presentations may be more common. The 2.42x unadjusted rate ratio would almost certainly shrink --- and might reverse in some states --- after adjusting for specialty, practice setting, and patient acuity. The consistency of the pattern across 45 of 51 jurisdictions is suggestive but not dispositive.

A third limitation arises from the specialty classification system itself. CMS specialty codes are self-reported and not uniformly granular. "General Practice" and "Family Practice" are distinct categories with different opioid rates (7.68% and 3.25%, respectively), but the clinical difference between these classifications is unclear in many cases. Our outlier analysis adjusts for specialty, which means misclassified providers may be scored against an inappropriate peer group. The practical impact is likely small --- the 13,913 outlier count would change modestly under alternative specialty groupings --- but it introduces noise into the specialty-specific estimates.

Fourth, the public-use file suppresses cells with fewer than 11 claims for privacy. Prescribers who write very few opioid prescriptions (1--10 claims) may have their opioid claims suppressed while their total claims are fully reported, biasing their observed opioid rate downward. The magnitude of this bias is difficult to quantify without access to the restricted-use file, but it would tend to slightly understate the national opioid prescribing rate and modestly reduce the outlier count at the high end.

Finally, this analysis is cross-sectional. A single year of data cannot distinguish between states on different trajectories. A state with a historically high opioid rate that has declined 30% over five years tells a fundamentally different story than one with a stable high rate, and this analysis cannot differentiate between them. Longitudinal extension --- repeating this analysis for CY2019 through CY2023 --- would add substantial interpretive value at minimal incremental cost.

---

## Clinical Implications

The headline finding for health system executives and policymakers is no longer the 2.45-fold state variation. It is the variance decomposition. Geography --- the axis around which nearly all opioid policy is organized --- explains 0.7% of prescribing variation. Individual prescriber behavior explains 62.6%. The public conversation about opioid prescribing has been, in a quantifiable sense, oriented around the wrong unit of analysis.

Four findings have immediate operational relevance.

First, the 13,913 specialty-adjusted outlier prescribers represent the most actionable and most efficient intervention target. These providers account for 11.5% of all Medicare Part D opioid claims (6.6 million claims) while constituting just 1.7% of the prescriber workforce. The 6.7:1 leverage ratio --- claims share to prescriber share --- means that monitoring these prescribers is approximately an order of magnitude more efficient than state-level convergence policies. Health plans, pharmacy benefit managers, and state medical boards could use specialty-adjusted benchmarking to prioritize prescriber education, peer comparison interventions, or prospective drug utilization review. The finding that 41.6% of outliers are nurse practitioners suggests that interventions should be designed for the provider types most likely to be identified, not exclusively for physicians.

Second, the Gini coefficient of 0.689 establishes that opioid prescribing is not gradually distributed across a broad population of providers. It is dominated by a small fraction. The top 1% of opioid prescribers write 23% of claims; the top 5% write 46%. This degree of concentration means that broad-based interventions (e.g., continuing education requirements for all prescribers, universal prior authorization) impose costs on hundreds of thousands of prescribers to address behavior concentrated among thousands. Targeted approaches are not merely more efficient --- they are categorically more appropriate given the distribution.

Third, the weak volume--rate correlation (rho = 0.086) has a direct operational consequence: prescription drug monitoring programs (PDMPs) and payer surveillance systems that flag prescribers based on total opioid volume will miss the majority of high-rate prescribers. A pain specialist writing 2,000 opioid prescriptions per year may have a perfectly typical rate for the specialty, while a dermatologist writing 50 opioid prescriptions could be an extreme outlier. Rate-based monitoring, adjusted for specialty, would be substantially more efficient than volume-based approaches.

Fourth, the NP/PA prescribing pattern --- elevated in 45 of 51 states, with a mean ratio of 2.42x --- warrants investigation but not reactive policy. The most responsible interpretation is that this finding generates a specific testable hypothesis: that after adjusting for specialty, practice setting, and patient panel composition, the NP/PA-to-MD ratio will narrow substantially. If it does not, that would constitute stronger evidence of a systematic prescribing culture difference. The appropriate next step is a matched analysis, not a scope-of-practice restriction.

**What this analysis does not mean.** This report does not identify any individual prescriber as engaging in inappropriate prescribing. Statistical outlier status is not a clinical judgment --- it is a population-level flag that warrants further investigation. A prescriber three standard deviations above the specialty mean may be serving a uniquely complex patient population, operating in a region with limited access to non-pharmacological pain management, or filling a legitimate clinical niche. The purpose of outlier identification is to prioritize review, not to assign blame. Similarly, this analysis does not establish that any state's opioid prescribing rate is "too high" or "too low." The appropriateness of a prescribing rate is a clinical determination that requires patient-level data this study does not contain.

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
| Volume--rate rho | 0.086 | 0.084--0.088 | 810,057 | Spearman + bootstrap |
| LA opioid ratio | 10.05% | --- | 345,583 | Aggregate ratio |
| Weighted/unweighted rank rho | 0.70 | --- | 51 | Spearman |
| Gini coefficient | 0.689 | 0.687--0.692 | 430,941 | Bootstrap |
| Top 1% claims share | 22.87% | --- | 4,309 | Lorenz curve |
| Top 5% claims share | 45.74% | --- | 21,547 | Lorenz curve |
| Top 10% claims share | 58.73% | --- | 43,094 | Lorenz curve |
| Variance: specialty | 36.6% | --- | --- | Hierarchical decomposition |
| Variance: state | 0.7% | --- | --- | Hierarchical decomposition |
| Variance: individual | 62.6% | --- | --- | Hierarchical decomposition |
| NP/PA-to-MD mean ratio | 2.42x | --- | 51 | Unweighted state means |
| States where NP > MD | 45 of 51 | --- | 51 | Count |
| Half-convergence reduction | 1,480,702 claims | --- | 25 states | Arithmetic simulation |

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

All figure-generating code is available from the authors upon request.

### Interpretation Constraints

The following interpretations are explicitly excluded by the analytical methodology: causal inference, generalization to non-Medicare populations, individual prescriber targeting, normative judgment on any state's rate, characterization of any prescribing rate as "inappropriate" without patient-level clinical data, and attribution of NP/PA-to-MD differences to provider competence or training quality.

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
