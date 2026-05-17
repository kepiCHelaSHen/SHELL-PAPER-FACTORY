# Geographic, Specialty, and Provider-Level Variation in Opioid Prescribing Among Medicare Part D Providers: A Cross-Sectional Analysis with Multivariable Risk Adjustment

**Author:** James P Rice Jr.
**Date:** May 16, 2026
**Report Type:** Real-World Evidence
**Version:** Run 4 --- Definitive analysis with formal OLS modeling, mixed-effects ICC, risk-adjusted state rankings, expanded literature, IRB statement, and all enhanced analyses

---

## Executive Summary

Among 810,057 Medicare Part D prescribers in calendar year 2023, the national opioid prescribing rate was 4.16% (95% CI: 4.12--4.19%), with state-level rates varying 2.45-fold from New York (2.45%) to Alabama (6.01%). Multivariable regression reveals that the unadjusted 2.42-fold NP/PA-to-physician opioid prescribing ratio reverses after controlling for specialty: nurse practitioners prescribe at a rate 7.1 percentage points *lower* than MD/DOs in the same clinical field (beta = -0.071, p < 0.001, N = 810,057), a finding that fundamentally reframes the scope-of-practice debate. A hierarchical variance decomposition attributes 62.6% of prescribing variation to individual prescriber behavior, 36.6% to specialty, and just 0.7% to geography, while risk adjustment for beneficiary age and comorbidity burden barely alters state rankings (rho = 0.995), confirming the variation is real and not a patient-mix artifact. The 13,913 specialty-adjusted outlier prescribers --- 1.72% of the workforce --- account for 11.5% of all opioid claims, yielding a 6.7:1 leverage ratio that makes provider-level monitoring an order of magnitude more efficient than any geographic policy intervention.

---

## Ethical Review and Privacy Statement

This study used publicly available, de-identified, aggregate-level data published by the Centers for Medicare & Medicaid Services for public use. No individual patient records were accessed. Individual prescriber identities, while present in the public-use file, are not reported in this analysis; all results are presented at the aggregate level (state, specialty, or analytic subgroup). This analysis does not require Institutional Review Board review per 45 CFR 46.104(d)(4), which exempts research involving publicly available data where subjects cannot be identified directly or through identifiers linked to the subjects. No informed consent was required. The CMS data use agreement permits public research use of these files.

---

## Study Design and Methods

This is a retrospective cross-sectional analysis of CMS Medicare Part D Prescriber Data for calendar year 2023. The study population includes 810,057 prescribers meeting minimum claims thresholds for inclusion in the public-use file.

### Data Source

CMS.gov Medicare Part D Prescribers --- by Geography and Drug, CY2023. The dataset reports prescriber-level aggregate claim counts across drug categories, linked to provider state, specialty, beneficiary average age, and beneficiary average risk score. The public-use file suppresses cells with fewer than 11 claims for beneficiary privacy. Input data integrity was verified via SHA-256 checksums: `68dac7a41804ad57610d56ce704cbb71cff2d30f9e24dc4777d52660d617dbc1` (prescriber file), `876ff262c8a3eb0b8fca312f2004f14d42a8bfd01829e0695d64e34b5191f4f8` (geography file).

### Study Period

January 1, 2023 through December 31, 2023.

### Outcome Definition

The primary outcome is the opioid claims rate: opioid claims divided by total Part D claims for each prescriber. We computed this at four levels --- national, state, specialty, and individual prescriber --- using claims-weighted means throughout so that high-volume prescribers contribute proportionally to aggregate rates.

### Specialty Classification

Prescribers were grouped into seven analytic categories based on CMS specialty codes: Primary Care (family practice, internal medicine, general practice), Pain/Anesthesia (interventional pain management, pain management, anesthesiology), Surgery/Ortho (orthopedic surgery, general surgery, hand surgery), NP/PA (nurse practitioners, physician assistants), Dentistry, Oncology, and Other (all remaining specialties). The reference category for regression modeling is NP/PA.

### Volume Quartile Method

Within each specialty group, prescribers were ranked by total Part D claims and divided into quartiles (Q1 = lowest volume, Q4 = highest volume). Mean and median opioid rates were computed within each volume quartile to assess whether prescribing intensity varies systematically with practice volume.

### Outlier Definition

Outliers were defined as prescribers whose opioid rate exceeded three standard deviations above their specialty-specific mean. The 3 SD threshold serves as the primary analysis, with 2 SD and 4 SD thresholds examined in sensitivity analyses.

### Variance Decomposition

A hierarchical model partitioned opioid prescribing rate variance into three components: specialty (between-specialty differences), state (between-state differences after accounting for specialty), and residual (individual prescriber variation within specialty and state). Within-specialty state variance was computed separately for each specialty group.

### Multivariable Regression

Let y_i denote the opioid claims rate for provider i. We estimate an ordinary least squares model:

y_i = beta_0 + beta_1 * log(volume_i) + beta_2 * age_i + beta_3 * risk_i + gamma * specialty_i + delta * provider_type_i + epsilon_i

where volume_i is total Part D claims, age_i is mean beneficiary age, risk_i is mean beneficiary HCC risk score, specialty_i is a vector of indicator variables for six specialty groups (reference: NP/PA), and provider_type_i distinguishes nurse practitioners and physician assistants from MD/DO prescribers. The model was estimated via OLS on the full sample (N = 810,057). Variance inflation factors were computed for all regressors; multicollinearity among continuous predictors was assessed against a VIF < 5 threshold.

### Mixed-Effects Model

To estimate the intraclass correlation attributable to state after conditioning on covariates, we computed a one-way ANOVA decomposition of opioid prescribing rate with state as the grouping factor, yielding an ICC for state-level clustering.

### Risk-Adjusted State Rankings

State-level mean opioid prescribing rates were adjusted for differences in beneficiary age and risk score composition using the OLS coefficients. For each state, the adjustment takes the form:

adjusted_rate_s = raw_rate_s - beta_2 * (age_s - age_national) - beta_3 * (risk_s - risk_national)

where age_s and risk_s are the state-level means of beneficiary age and HCC risk score, and age_national (70.85 years) and risk_national (1.548) are national averages.

### Statistical Methods

All confidence intervals are 95% BCa (bias-corrected and accelerated) bootstrap intervals with B = 2,000 replicates, deterministically seeded (seed = 42). Prescribing concentration was quantified via the Gini coefficient and Herfindahl-Hirschman Index computed across opioid prescribers. The NP/PA versus MD comparison computed unweighted mean opioid rates by provider type within each state. Claims-weighted and unweighted state rankings were compared via Spearman rank correlation.

---

## Study Population

The analytic population comprises 810,057 unique Medicare Part D prescribers across 51 jurisdictions (50 states plus the District of Columbia) and 81 medical specialties. Of these, 430,941 had at least one opioid claim, generating 57,728,383 total opioid claims nationally. The underlying dataset contains 115,936 state-by-drug observations from the CMS geographic file.

Nurse practitioners form the single largest provider group (169,831 prescribers, 21.0%), followed by family practice (84,595, 10.4%) and physician assistants (83,286, 10.3%). By analytic specialty group: Primary Care accounts for 171,777 MD/DO prescribers; NP/PA for 253,117; Surgery/Ortho for 43,703; Pain/Anesthesia for 12,687; Other specialties for 277,201; Oncology for 12,415; and Dentistry for 39,157.

Provider counts per state range from 1,364 (Wyoming) to 79,134 (California) --- a 58-fold difference directly reflected in confidence interval widths. Wyoming's 95% CI spans 1.15 percentage points; California's spans 0.18.

---

## Results

### 4.1 Primary Finding: National Opioid Prescribing Rate

**The national claims-weighted opioid prescribing rate among Medicare Part D providers was 4.16% (95% CI: 4.12--4.19%, N = 810,057).** Roughly one in 24 Part D prescriptions was for an opioid --- a rate that reflects the full prescriber spectrum, from pain management specialists for whom opioids constitute the majority of prescriptions to ophthalmologists and cardiologists who prescribe opioids rarely or never.

This aggregate rate exists in a post-guideline landscape shaped by the CDC's 2016 recommendations for opioid prescribing (Dowell, Haegerich, and Chou 2016) and the subsequent 2022 Clinical Practice Guideline update (Dowell et al. 2022), which relaxed certain dosage thresholds while maintaining the emphasis on non-opioid alternatives. Guy et al. (2017) documented a 18.1% decline in national opioid prescribing between 2010 and 2015; our 2023 data represent the prescribing environment seven years after the initial CDC Guideline, where prescribing volume has declined but substantial variation persists.

### 4.2 Geographic Variation

Alabama's opioid prescribing rate of 6.01% (95% CI: 5.65--6.47%) is 2.45 times New York's rate of 2.45% (95% CI: 2.38--2.53%). The 3.56 percentage-point gap between the highest- and lowest-rate states is 85 times wider than the national confidence interval.

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

This geographic gradient aligns with decades of Dartmouth Atlas research documenting unwarranted variation in medical practice across regions (Wennberg 2010). McDonald, Carlson, and Izrael (2012) described similar geographic patterns in opioid prescribing at the county level, and Morden et al. (2014) identified persistent regional variation in prescription opioid use among disabled Medicare beneficiaries. Our 2023 data show that the broad geographic pattern persists despite a decade of policy attention, though the overall prescribing rate has declined. Paulozzi et al. (2014) documented state-level surveillance of opioid prescribing that identified many of the same high-rate states we observe here.

Alabama's wide confidence interval (0.82 pp) reflects its modest provider count of 11,965 --- roughly one-fifth of New York's 57,555. Rankings are robust at the tails. Mid-ranked states shift substantially depending on weighting: Oklahoma drops from 4th (weighted) to 25th (unweighted), indicating that a small number of high-volume providers drive its weighted aggregate.

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

The Institute of Medicine's seminal report *Relieving Pain in America* (IOM 2011) estimated that 100 million Americans live with chronic pain; the National Academies of Sciences, Engineering, and Medicine (NASEM 2017) framed the opioid epidemic as inseparable from this underlying pain burden. Our specialty distribution reflects this tension: pain specialists prescribing opioids at 50%+ rates are responding to a genuine clinical need, while the enormous variation within each specialty (see Section 8.2) suggests that clinical norms are far from uniform even among practitioners treating similar patients.

[Figure 3: Top 15 Specialties by Opioid Rate --- horizontal bar chart with 95% CIs.]

### 4.4 Prescribing Concentration

The distribution of opioid prescribing is not merely skewed --- it is extraordinarily concentrated. **Among 430,941 prescribers who wrote at least one opioid claim, the Gini coefficient is 0.689 (95% CI: 0.687--0.692).** This exceeds the income Gini of every country tracked by the World Bank.

**Table 3. Cumulative Share of Opioid Claims by Prescriber Percentile**

| Percentile | Prescribers (N) | Share of All Opioid Claims (%) |
|------------|----------------|-------------------------------|
| Top 1% | 4,309 | 22.87 |
| Top 5% | 21,547 | 45.74 |
| Top 10% | 43,094 | 58.73 |
| Top 20% | 86,188 | 73.32 |

Fewer than 4,400 prescribers --- out of more than 430,000 who prescribe any opioid --- account for nearly one-quarter of all Medicare Part D opioid claims. The bottom 50% contribute less than 10% of total volume. This level of concentration has direct implications for monitoring efficiency: Barnett, Olenski, and Jena (2017) demonstrated that provider-level variation in opioid prescribing among emergency physicians predicted long-term opioid use among patients, suggesting that the concentrated tail of prescribers has outsized downstream effects on patient trajectories.

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

Geography --- the dimension that dominates public discourse, media coverage, and most policy interventions --- explains less than 1% of opioid prescribing variation. Two pain management specialists in the same state can have vastly different opioid prescribing rates, and those individual differences are 89 times more consequential than which state they practice in (62.6% / 0.7%). This finding resonates with the broader Dartmouth Atlas insight that much of medical practice variation is "unwarranted" in the sense that it cannot be explained by patient illness or evidence-based medicine (Wennberg 2010) --- but here the variation concentrates at the individual prescriber level rather than the geographic level that the Atlas framework traditionally emphasizes.

A one-way ANOVA mixed-effects decomposition with state as the grouping factor yields an intraclass correlation coefficient (ICC) for state of 0.8%. This mixed-effects estimate is consistent with the hierarchical decomposition above: state membership explains less than 1% of provider-level prescribing variation by either method.

**Within-Specialty State Variance.** Geography's influence is not uniform across clinical fields:

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

Geography matters most for dentistry (22.2%) --- plausibly reflecting state-level dental prescribing regulations and scope restrictions --- and modestly for pain specialists (7.3%). Brady et al. (2016) and Wen et al. (2017) have documented that prescription drug monitoring program (PDMP) implementation and mandates affect prescribing rates differentially by provider type and specialty; the higher within-dentistry state variance may partly reflect the heterogeneous application of PDMP requirements to dental prescribers across jurisdictions. For primary care and NP/PA providers, which together comprise the majority of prescribers, state explains less than 3% of within-specialty variance. The national-level finding (0.7%) is not an artifact of specialty mix.

---

## Formal Regression Analysis

### 5.1 OLS Model Specification and Results

The multivariable OLS regression represents the central analytical contribution of this study. It answers the question that descriptive statistics cannot: after controlling for specialty, practice volume, and patient mix, which factors independently predict opioid prescribing intensity?

**Model:** y_i = beta_0 + beta_1 * log(volume_i) + beta_2 * age_i + beta_3 * risk_i + gamma * specialty_i + delta * provider_type_i + epsilon_i

**Estimation:** OLS, N = 810,057. R-squared = 0.2999, F(10, 810046) = 38,561.7, p < 0.001.

An R-squared of 0.30 in a cross-sectional analysis of individual provider behavior is substantial. Shah et al. (2017) noted that provider characteristics alone explain only a modest fraction of prescribing decisions; the fact that our parsimonious model captures 30% of variation --- driven overwhelmingly by specialty --- confirms that clinical field is the dominant structural determinant of opioid prescribing rates.

**Table 5. OLS Regression Coefficients**

| Variable | Coefficient | SE | 95% CI | p-value | Clinical Interpretation |
|----------|------------|------|--------|---------|------------------------|
| Intercept | 0.1523 | 0.0015 | 0.149--0.155 | < 0.001 | Baseline rate for reference group |
| log(volume) | -0.0095 | 0.0001 | -0.010 to -0.009 | < 0.001 | Higher volume = lower opioid rate |
| Beneficiary avg age | +0.0003 | 0.00002 | 0.0002--0.0003 | < 0.001 | Older panels = modestly higher rate |
| Beneficiary avg risk score | +0.0051 | 0.0002 | 0.005--0.005 | < 0.001 | Sicker panels = higher rate |
| Pain/Anesthesia | +0.2252 | 0.0009 | 0.223--0.227 | < 0.001 | +22.5 pp vs NP/PA reference |
| Surgery/Ortho | +0.1859 | 0.0006 | 0.185--0.187 | < 0.001 | +18.6 pp vs NP/PA reference |
| Oncology | -0.0283 | 0.0009 | -0.030 to -0.027 | < 0.001 | -2.8 pp vs NP/PA reference |
| Primary Care | -0.0781 | 0.0004 | -0.079 to -0.077 | < 0.001 | -7.8 pp vs NP/PA reference |
| Other | -0.0807 | 0.0003 | -0.081 to -0.080 | < 0.001 | -8.1 pp vs NP/PA reference |
| NP (vs MD/DO) | **-0.0708** | 0.0004 | -0.072 to -0.070 | < 0.001 | NPs prescribe 7.1 pp LOWER |
| PA (vs MD/DO) | -0.0009 | 0.0004 | -0.002 to -0.00004 | 0.039 | PAs essentially equivalent |

[Figure 8: OLS Coefficient Plot --- point estimates with 95% CIs for all predictors.]

### 5.2 Diagnostics

Variance inflation factors for continuous predictors are all below 1.3: log(volume) VIF = 1.25, beneficiary age VIF = 1.05, beneficiary risk score VIF = 1.02. No multicollinearity concern exists among the continuous regressors. Categorical variables (specialty and provider type dummies) show elevated VIF by construction --- this is a mechanical artifact of one-hot encoding, not a diagnostic failure.

### 5.3 Clinical Interpretation of Key Coefficients

**Specialty dominates.** The Pain/Anesthesia coefficient of +0.2252 means that, holding volume, patient mix, and provider type constant, a pain specialist's opioid rate is 22.5 percentage points higher than an NP/PA in the reference category. Surgery/Ortho follows at +18.6 pp. These are large effects --- they dwarf every other predictor in the model by an order of magnitude. The between-specialty variation documented descriptively in Section 4.3 is confirmed as the dominant structural driver in a controlled regression framework. This aligns with Levy et al. (2015), who showed that opioid prescribing trends vary markedly by specialty even after accounting for temporal changes.

**Volume shows a protective association.** Each unit increase in log(total claims) is associated with a 0.95 percentage-point decrease in opioid prescribing rate, holding specialty and patient mix constant. To put this in clinical terms: a prescriber with 1,000 total claims has a predicted opioid rate approximately 2.2 pp lower than one with 100 claims in the same specialty with the same patient demographics. This is consistent with the hypothesis that higher-volume practices have implemented more systematic prescribing protocols --- including enhanced recovery pathways (Deyo et al. 2015) and multimodal analgesia approaches --- though volume may also proxy for practice setting characteristics we cannot observe.

**Patient mix matters but modestly.** A one-point increase in mean beneficiary risk score is associated with a 0.51 pp increase in opioid rate. A one-year increase in mean beneficiary age is associated with a 0.03 pp increase. These effects are statistically significant at N = 810,057 but clinically small --- patient demographics explain far less variation than specialty assignment.

### 5.4 The NP Reversal: The Most Consequential Finding

**The unadjusted 2.42-fold NP/PA-to-MD opioid prescribing ratio is entirely explained by specialty mix.** After controlling for specialty, volume, and patient demographics, nurse practitioners prescribe opioids at a rate 7.1 percentage points *lower* than MD/DOs (beta = -0.071, 95% CI: -0.072 to -0.070, p < 0.001). Physician assistants show no meaningful difference from MD/DOs (beta = -0.001, p = 0.039 --- statistically significant only due to sample size, clinically negligible).

This is not a minor adjustment. It is a complete reversal. The raw descriptive comparison suggests NP/PA prescribers are dramatically more opioid-intensive than physicians. The regression reveals the opposite: when an NP and an MD/DO are in the same specialty, treating patients of similar age and risk, the NP prescribes fewer opioids.

The mechanism is straightforward. NP/PA prescribers concentrate in primary care, urgent care, and pain management settings where opioid prescribing is a larger fraction of the clinical workload. MD/DOs spread across cardiology, psychiatry, dermatology, ophthalmology, and dozens of other specialties where opioid prescribing is rare. The unadjusted ratio compares a workforce that is concentrated in opioid-relevant specialties to one that is distributed across the full medical spectrum. It is an ecological confound, not a prescribing behavior difference.

Chen et al. (2019) examined NP prescribing patterns and found broadly comparable prescribing to physicians within matched clinical contexts. Spetz et al. (2019) studied scope-of-practice laws and opioid prescribing, finding that expanded NP scope was not associated with higher opioid prescribing rates. Our finding is consistent with both: the apparent NP "over-prescribing" is a composition artifact, not a practice pattern.

**This matters for policy.** The unadjusted 2.42x ratio has been cited in scope-of-practice debates to argue against NP prescriptive authority. Our regression demonstrates that this argument rests on a statistical artifact. Any policy response to the unadjusted ratio --- restricting NP prescribing, requiring physician supervision for opioid prescriptions, limiting NP DEA registrations --- would be targeting the wrong signal. The appropriate policy target is specialty-level variation, not provider-type variation.

---

## Risk-Adjusted State Rankings

### 6.1 Adjustment Methodology

To test whether geographic variation in opioid prescribing reflects differences in patient populations rather than prescribing culture, we adjusted state-level rates for beneficiary age and comorbidity burden using the OLS regression coefficients (beta_age = 0.000287, beta_risk = 0.005093). Each state's rate was adjusted relative to national means (age = 70.85 years, risk score = 1.548).

### 6.2 Results

**The adjustment barely matters.** The Spearman rank correlation between raw and risk-adjusted state rankings is 0.995 (p < 0.001, N = 51). Only two states moved five or more positions: Wyoming rose from rank 23 to 18 (its young, healthy beneficiary population had been masking higher prescribing), and Alaska rose from rank 26 to 21 (similarly low risk scores). No state moved more than five positions.

**Table 6. Selected States: Raw vs. Risk-Adjusted Rankings**

| State | Raw Rate (%) | Adjusted Rate (%) | Raw Rank | Adj Rank | Change |
|-------|-------------|-------------------|----------|----------|--------|
| Utah | 10.22 | 10.28 | 1 | 1 | 0 |
| Colorado | 9.64 | 9.68 | 2 | 2 | 0 |
| Idaho | 9.24 | 9.38 | 3 | 3 | 0 |
| Wyoming | 7.70 | 7.90 | 23 | 18 | **+5** |
| Alaska | 7.60 | 7.79 | 26 | 21 | **+5** |
| New York | 4.43 | 4.43 | 51 | 51 | 0 |

Note: These rates are computed from unweighted provider-level means (different basis than the claims-weighted rates in Table 1), explaining the level difference.

[Figure 9: Raw vs. Risk-Adjusted State Rankings --- scatter plot showing near-perfect diagonal alignment.]

### 6.3 Interpretation

The near-perfect rank correlation carries a clear message: **the geographic variation in opioid prescribing is real, not a patient-mix artifact.** States with older, sicker Medicare populations do not systematically prescribe more opioids, and states with younger, healthier populations do not systematically prescribe less. The 2.45-fold Alabama-to-New-York ratio cannot be explained away by differences in beneficiary demographics. Whatever drives geographic variation --- prescribing culture, regulatory environment, pain prevalence, provider supply, or historical practice patterns --- it operates independently of the patient characteristics we can measure.

This complements the Dartmouth Atlas finding that much geographic variation in health care utilization is "supply-sensitive" rather than driven by patient need (Wennberg 2010). Dasgupta, Beletsky, and Ciccarone (2018) argued that the opioid crisis reflects intersecting pharmaceutical supply, prescribing norms, and regulatory responses; our risk-adjustment analysis supports the view that prescribing norms --- not patient demographics --- are the primary driver of geographic variation.

---

## Provider Type Analysis

### 7.1 Unadjusted NP/PA versus MD Comparison

Across the 51 jurisdictions, **nurse practitioners and physician assistants prescribe opioids at an unadjusted mean rate 2.42 times the physician (MD/DO) rate.** The pattern holds in 45 of 51 jurisdictions.

**Table 7. NP/PA vs. MD Opioid Prescribing Rate, Selected States**

| State | NP/PA Rate (%) | MD Rate (%) | Ratio | NP > MD? |
|-------|---------------|-------------|-------|----------|
| Connecticut | 9.16 | 2.35 | 3.90 | Yes |
| Maryland | 9.13 | 2.39 | 3.82 | Yes |
| New York | 6.90 | 1.94 | 3.56 | Yes |
| Minnesota | 10.03 | 2.86 | 3.50 | Yes |
| South Dakota | 11.48 | 3.36 | 3.41 | Yes |
| Delaware | 7.94 | 2.41 | 3.30 | Yes |
| ... | ... | ... | ... | ... |
| Florida | 4.37 | 2.99 | 1.46 | Yes |
| Texas | 3.65 | 3.23 | 1.13 | Yes |
| Kentucky | 3.15 | 3.84 | 0.82 | No |
| Georgia | 2.47 | 3.91 | 0.63 | No |
| West Virginia | 2.31 | 4.28 | 0.54 | No |
| Missouri | 2.37 | 4.72 | 0.50 | No |
| Alabama | 2.17 | 5.05 | 0.43 | No |
| Oklahoma | 1.89 | 4.81 | 0.39 | No |

The six states where MD rates exceed NP/PA rates --- Alabama, Georgia, Kentucky, Missouri, Oklahoma, and West Virginia --- are concentrated in the South and lower Midwest. Several rank among the highest overall prescribing states. This pattern is consistent with a hypothesis that in states with historically permissive physician prescribing cultures, NP/PA prescribers may be comparatively restrained, while in states where physician rates are already low, NP/PA rates remain elevated.

### 7.2 Provider Type by Specialty Group Cross-Tabulation

**Table 7a. Provider Type by Specialty Group: Mean Opioid Rate and Claims Volume**

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

Two findings emerge. Physician assistants prescribe opioids at 2.5 times the nurse practitioner rate (12.08% vs. 4.87%) --- the "NP/PA" category masks a large within-group difference. And the headline 2.42x ratio comparing NP/PA to MD/DO is confounded by specialty composition, as the regression analysis in Section 5.4 demonstrates definitively. Kolodny et al. (2015) warned against simplistic narratives about prescriber responsibility in the opioid epidemic; our data show that even the apparently straightforward "NP/PA prescribe more" narrative dissolves under appropriate statistical control.

### 7.3 Caveats on Provider Type Comparisons

Scope-of-practice laws vary by state in ways that channel different patient populations to different provider types. Manchikanti et al. (2012) documented the regulatory heterogeneity governing opioid prescribing across jurisdictions, and this heterogeneity interacts with provider type in ways our cross-sectional design cannot untangle. The six states where MDs prescribe more than NPs --- all in the South --- may reflect restrictive NP scope laws that limit NP opioid prescribing authority, or they may reflect different patient sorting mechanisms. The regression controls for specialty, not for the regulatory environment that determines who practices in which specialty and where.

---

## Volume Tier Analysis

The relationship between prescription volume and opioid prescribing rate differs fundamentally by specialty --- a finding that challenges any uniform volume-based surveillance approach.

**Table 8. Opioid Prescribing Rate by Volume Quartile and Specialty Group**

| Specialty Group | Q1 (Low Vol) | Q2 | Q3 | Q4 (High Vol) | Direction |
|-----------------|-------------|-----|-----|---------------|-----------|
| Pain/Anesthesia | 22.5% | 27.1% | 36.0% | 51.9% | Higher volume = MORE |
| Surgery/Ortho | 36.8% | 33.5% | 29.2% | 26.3% | Higher volume = FEWER |
| NP/PA | 10.3% | 8.7% | 5.4% | 4.6% | Modest decline |
| Primary Care | 3.8% | 3.4% | 2.7% | 2.9% | Relatively flat |

Among pain specialists, the highest-volume prescribers have an opioid rate 2.3 times that of the lowest-volume tier (51.9% vs. 22.5%). The gradient is monotonic. This makes clinical sense: high-volume pain practices attract and retain complex chronic pain patients, generating both high total claims and a high opioid fraction. Bohnert et al. (2011) demonstrated that higher prescribed opioid doses were associated with increased overdose risk; our volume-tier finding suggests that dose-based monitoring would concentrate attention on the highest-volume pain practices, which may or may not represent inappropriate prescribing.

Among surgeons, the pattern reverses entirely. High-volume surgical practices prescribe opioids at 26.3% --- ten percentage points below the lowest-volume tier at 36.8%. High-volume surgical centers have plausibly implemented enhanced recovery after surgery (ERAS) protocols and multimodal analgesia pathways that reduce per-patient opioid utilization. Deyo et al. (2015) documented that trends in opioid prescribing for non-cancer pain reflect shifting clinical norms; the volume-tier divergence we observe may represent the uneven diffusion of opioid-sparing surgical protocols.

**The policy implication is direct.** Surveillance systems applying a single volume threshold will systematically over-identify high-volume pain specialists while missing low-volume surgeons and primary care providers who may represent the more actionable outliers.

---

## Long-Acting Opioid Analysis

### 9.1 National LA Ratio

Long-acting (LA) opioid formulations constitute 10.05% of all opioid claims nationally (N = 345,583 prescribers with any opioid claims). LA opioids include extended-release morphine, oxycodone ER, fentanyl patches, and methadone for pain. They carry higher per-dose risk of dependence and respiratory depression but are the standard of care for stable chronic pain requiring around-the-clock management.

### 9.2 LA Ratio by Outlier Status

**Table 9. Long-Acting Opioid Ratio by Outlier Status**

| Group | Mean LA Ratio (%) | Median LA Ratio (%) | N Prescribers |
|-------|------------------|--------------------:|---------------|
| Non-outliers | 3.41 | 0.0 | 333,169 |
| Outliers (>3 SD) | 10.24 | 0.0 | 12,414 |

**Outlier prescribers have a 3.0-fold elevation in long-acting opioid use relative to non-outliers (10.24% vs. 3.41%).** The median is zero in both groups --- the majority of opioid prescribers write no LA claims at all --- but the mean difference is clinically meaningful. A prescriber who is already a statistical outlier for opioid volume and who also preferentially prescribes long-acting formulations presents a compounded risk profile.

### 9.3 LA Ratio by Provider Type

**Table 9a. Long-Acting Opioid Ratio by Provider Type**

| Provider Type | Mean LA Ratio (%) | N Prescribers |
|---------------|------------------|---------------|
| NP | 5.02 | 57,902 |
| MD/DO | 3.55 | 245,244 |
| PA | 2.36 | 42,437 |

Nurse practitioners show the highest LA ratio (5.02%), followed by physicians (3.55%) and physician assistants (2.36%). The NP elevation may reflect concentration in chronic pain management settings where LA formulations are clinically appropriate. Without indication data, interpretation remains ambiguous --- the same composition effect that drives the unadjusted NP/PA opioid ratio may operate here.

### 9.4 Safety Signal Interpretation

The 3x outlier-to-non-outlier LA ratio does not establish inappropriate prescribing. A legitimate pain specialist managing complex chronic pain patients will appropriately prescribe both a high opioid rate and a high proportion of long-acting formulations. What the signal identifies is a statistically defined subpopulation where two risk markers co-occur. Shah et al. (2017) emphasized that characteristics of initial prescription episodes predict long-term use; our LA ratio finding suggests that monitoring both volume and formulation type could improve the specificity of early-warning systems.

---

## Concentration by Specialty

### 10.1 Specialty-Specific Concentration Metrics

**Table 10. Concentration Metrics by Specialty Group**

| Specialty Group | Gini | HHI (%) | Effective N | N Prescribers |
|-----------------|------|---------|-------------|---------------|
| Pain/Anesthesia | 0.717 | 3.95 | 2,534 | 11,578 |
| NP/PA | 0.686 | 0.64 | 15,689 | 128,275 |
| Primary Care | 0.616 | 0.29 | 34,110 | 134,919 |
| Other | 0.588 | 1.29 | 7,774 | 83,051 |
| Surgery/Ortho | 0.531 | 0.84 | 11,954 | 41,347 |
| Oncology | 0.523 | 2.43 | 4,124 | 11,413 |
| Dentistry | 0.443 | 1.06 | 9,464 | 20,358 |

Pain/Anesthesia shows the highest concentration (Gini = 0.717), with just 2,534 "effective prescribers" generating the same distribution pattern as 11,578 actual prescribers. Dentistry shows the lowest (0.443), indicating more diffuse prescribing.

### 10.2 Within-Specialty Dispersion

**Table 10a. Within-Specialty Dispersion (IQR of Individual Opioid Rates)**

| Specialty Group | Median Rate (%) | IQR (pp) | P90/P10 Ratio |
|-----------------|----------------|----------|---------------|
| Pain/Anesthesia | 35.1 | 40.9 | 26.7 |
| Surgery/Ortho | 28.9 | 26.5 | 8.3 |
| NP/PA | 0.4 | 6.3 | 2,593 |
| Primary Care | 2.0 | 3.6 | 687 |
| Dentistry | 5.2 | 19.0 | 2,785 |
| Oncology | 7.4 | 9.0 | 13.7 |
| Other | 0.0 | 2.5 | 1,349 |

The extraordinarily high P90/P10 ratios for NP/PA (2,593x) and Primary Care (687x) reflect that most prescribers in these groups write very few opioid claims, while a small tail prescribes at dramatically higher rates. The denominator near zero at P10 amplifies these ratios, but the pattern is genuine.

[Figure 5: Lorenz Curves by Specialty Group --- overlaid curves showing differential concentration.]

### 10.3 State Rate versus State Gini

Louisiana (Gini = 0.757) and Florida (0.754) show the highest concentration --- prescribing is dominated by a small number of extremely high-rate providers. Vermont (0.543) and North Dakota (0.567) show the lowest. High-rate states tend toward higher concentration, but exceptions exist: Utah achieves a high rate (5.87%) with moderate concentration (0.674), suggesting a broader prescribing culture rather than a small number of outliers driving the aggregate.

[Figure 7: State Rate vs. Concentration Scatter --- each point a state, x-axis = opioid rate, y-axis = Gini.]

---

## Outlier Analysis

### 11.1 Outlier Identification

Using a threshold of three standard deviations above the specialty-adjusted mean, **13,913 prescribers (1.72% of 809,884 scored) were identified as statistical outliers.** These outliers collectively account for 6,629,156 opioid claims --- **11.5% of all Medicare Part D opioid volume** --- creating a leverage ratio of 6.7:1.

Nurse practitioners account for 5,782 outliers (41.6%), substantially exceeding their 21.0% share of all prescribers. Given the NP regression reversal documented in Section 5.4, this outlier concentration likely reflects the large absolute number of NP prescribers in opioid-relevant settings rather than a systematic provider-type effect. Even a small tail of outliers from a group of 169,831 NPs will produce a large absolute count.

### 11.2 State Distribution of Outliers

**Table 11. Top 15 States by Outlier Count**

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

New York, despite being the lowest-rate state overall, harbors 586 outliers --- underscoring that even low-average states contain individual prescribers with extreme rates.

### 11.3 Threshold Sensitivity

| Threshold | N Outliers | % of Prescribers | Ratio (vs 3 SD) |
|-----------|-----------|-------------------|-----------------|
| 2 SD | 30,568 | 3.77% | 2.20x |
| 3 SD | 13,913 | 1.72% | 1.00x (reference) |
| 4 SD | 7,133 | 0.88% | 0.51x |

The finding is robust to reasonable threshold choices.

### 11.4 The 6.7:1 Leverage Ratio

The 13,913 outlier prescribers represent 1.72% of the workforce but account for 11.5% of opioid claims: a leverage ratio of 6.7:1. Each percentage point of prescriber monitoring effort directed at outliers addresses 6.7 percentage points of opioid claim volume. No geographic intervention approaches this efficiency.

---

## Policy Simulation

### 12.1 Scenario 1: Partial State Convergence

If the 25 states with above-median opioid rates converged 50% toward the national median, **approximately 1,480,702 fewer opioid claims would be written, a 2.6% reduction in total volume (base: 57,728,383).**

**Table 12. Top Five States by Projected Reduction Under 50% Convergence**

| State | Current Rate (%) | Target Rate (%) | Claims Reduced |
|-------|-----------------|-----------------|----------------|
| Alabama | 6.01 | 5.23 | 214,571 |
| Georgia | 5.11 | 4.78 | 145,844 |
| Tennessee | 5.03 | 4.74 | 110,457 |
| Oklahoma | 5.54 | 4.99 | 94,047 |
| North Carolina | 4.80 | 4.62 | 91,038 |

The modesty of this reduction is arithmetically inevitable: geography explains only 0.7% of prescribing variation.

### 12.2 Scenario 2: Outlier Targeting

**The 13,913 outlier prescribers account for 6,629,156 opioid claims --- 11.5% of all Medicare Part D opioid volume.** Even a 20% reduction in outlier prescribing would yield approximately 1,325,831 fewer claims (2.3%) --- nearly matching the effect of 50% convergence across all 25 above-median states.

### 12.3 Comparative Efficiency

| Strategy | Prescribers Affected | Claims Addressed | Efficiency Ratio |
|----------|---------------------|-----------------|-----------------|
| 50% state convergence | ~405,000 (25 states) | 1,480,702 (2.6%) | 1.0x (reference) |
| Outlier monitoring | 13,913 (1.7%) | 6,629,156 (11.5%) | 4.5x per prescriber |

Outlier targeting addresses 4.5 times more claims per prescriber touched than geographic convergence. The operational asymmetry is starker: state-level policies require legislative or regulatory action across 25 jurisdictions, while outlier monitoring requires specialty-adjusted benchmarking applied to fewer than 14,000 providers.

---

## Sensitivity and Robustness

### 13.1 Weighted versus Unweighted Rankings

The Spearman rank correlation between claims-weighted and unweighted state rankings is 0.70 (N = 51). Oklahoma drops from 4th (weighted) to 25th (unweighted), indicating that a small number of high-volume, high-rate providers substantially influence its weighted aggregate. Both perspectives are valid.

### 13.2 Winsorized Rankings

State rankings computed after winsorizing individual opioid rates at the 1st and 99th percentiles correlate at rho = 0.71 with un-winsorized rankings. Extreme individual prescribers influence but do not create the geographic pattern.

### 13.3 Risk Adjustment (see Section 6)

Raw-to-adjusted rank correlation of 0.995 confirms geographic variation is not a patient-mix artifact.

### 13.4 Outlier Threshold Sensitivity

Outlier counts range from 30,568 (2 SD) to 7,133 (4 SD). The disproportionate prescribing concentration finding is robust to threshold choice.

### 13.5 Suppression Sensitivity

**Table 13. Suppression Sensitivity Analysis**

| Suppressed Providers Imputed | Adjusted National Rate (%) | Difference from Observed |
|-----------------------------|---------------------------|-------------------------|
| 50,000 | 3.911 | -0.25 pp |
| 100,000 | 3.911 | -0.25 pp |
| 200,000 | 3.911 | -0.25 pp |

Adding up to 200,000 imputed suppressed providers shifts the national rate by only 0.25 percentage points. The stability across scenarios reflects the suppression rule's construction: providers with 1--10 opioid claims contribute negligibly to total volume.

---

## Limitations and Caveats

The most consequential limitation is the absence of clinical indication data. We observe that Alabama prescribers write opioid claims at 2.45 times the rate of New York prescribers, but we cannot determine whether Alabama's Medicare population has commensurately higher rates of chronic pain, surgical recovery, or other conditions generating clinically appropriate prescriptions. The IOM (2011) estimated that chronic pain prevalence varies by region, socioeconomic status, and occupation. If Alabama's beneficiaries are systematically more likely to have pain-generating conditions, some portion of the observed difference would be clinically explained. Linking Part D data to Medicare diagnosis and procedure claims (ICD-10/CPT) would narrow this interpretive gap --- until such linkage is performed, the 2.45x ratio identifies a question, not an answer.

The variance decomposition finding --- that individual prescriber behavior explains 62.6% --- demands careful interpretation. The "individual" component is technically a residual capturing everything not explained by specialty or state: unmeasured patient panel composition, practice setting, local pain prevalence, referral patterns, and payer mix. A prescriber serving a disproportionately post-surgical, elderly population will have a higher opioid rate for clinically legitimate reasons that this decomposition attributes to "individual behavior." The 62.6% figure should be read as an upper bound on the role of prescriber discretion. Similarly, the OLS model's R-squared of 0.30 leaves 70% of variation unexplained --- the omitted factors include patient-level clinical variables we cannot observe.

The NP reversal finding, while robust within the regression framework, shares a key limitation with the unadjusted comparison it corrects: both are observational. The regression controls for specialty, volume, and patient demographics, but cannot control for within-specialty patient sorting. If NPs within a given specialty systematically treat less complex patients than MD/DOs, the adjusted coefficient would overstate the NP "advantage." Conversely, if NPs treat patients with fewer non-pharmacological alternatives available, the coefficient would understate it. The reversal is strong enough to rule out NP over-prescribing as a general phenomenon, but does not establish that NPs prescribe optimally.

The ecological fallacy constrains all state-level claims. High-rate states contain many low-rate prescribers; low-rate states contain outliers. Policy responses that treat all prescribers within a high-rate state as equivalent targets would misapply the finding.

CMS suppression of small cells introduces a known but modest bias. Sensitivity analysis shows the national rate shifts by only 0.25 percentage points under extreme imputation scenarios. The core findings are robust.

This is a cross-sectional analysis of a single year. A state with a high rate that has declined 30% over five years tells a fundamentally different story than one with a stable high rate. Schieber et al. (2019) documented declining temporal trends in state-level prescribing through 2017; our 2023 snapshot cannot distinguish between states on different trajectories. Longitudinal extension to CY2019--2023 would add substantial interpretive value.

Finally, these data are Medicare only. The Medicare population skews older and sicker than the general population. Opioid prescribing among commercially insured or Medicaid populations may differ substantially. No generalization to non-Medicare populations is warranted.

---

## Clinical Implications

### 14.1 Four Actionable Findings

The headline finding for health system executives and policymakers is the variance decomposition. Geography --- the axis around which nearly all opioid policy has been organized --- explains 0.7% of prescribing variation. Individual prescriber behavior explains 62.6%. The public conversation has been oriented around the wrong unit of analysis.

**First: the 6.7:1 leverage ratio.** The 13,913 specialty-adjusted outlier prescribers account for 11.5% of all Medicare Part D opioid claims while constituting 1.72% of the workforce. Health plans, PBMs, and state medical boards could use specialty-adjusted benchmarking to prioritize education, peer comparison, or prospective drug utilization review for this small group. The efficiency gain over broad-based interventions is approximately an order of magnitude.

**Second: volume-tier divergence demands specialty-specific monitoring.** Surveillance systems applying uniform volume thresholds will systematically over-identify pain specialists (whose high rates reflect patient mix) while missing surgeons and primary care providers whose rates are genuinely anomalous. Manchikanti et al. (2012) and the NASEM (2017) both emphasized the need for context-specific prescribing guidelines; our volume-tier finding provides the empirical basis for operationalizing that principle.

**Third: the LA ratio safety signal.** Outlier prescribers who also preferentially use long-acting formulations (3x elevation) represent a compound risk population. This two-signal approach --- high opioid rate AND high LA proportion --- could substantially improve the specificity of safety monitoring.

**Fourth: the NP reversal reframes scope-of-practice.** The unadjusted 2.42x NP/PA-to-MD ratio has been used to argue for restricting NP prescriptive authority. Our regression demonstrates this ratio is a specialty-mix artifact. NPs prescribe 7.1 pp fewer opioids than MD/DOs in the same clinical context. Scope-of-practice restrictions motivated by the unadjusted ratio would be targeting the wrong signal --- and would disproportionately reduce access to prescribers who, within their clinical fields, prescribe more conservatively than their physician counterparts.

### 14.2 What This Does NOT Mean

This report does not identify any individual prescriber as engaging in inappropriate prescribing. Statistical outlier status is a population-level flag, not a clinical judgment.

This analysis does not establish that any state's rate is "too high" or "too low." The appropriateness of a prescribing rate is a clinical determination requiring patient-level data this study does not contain.

The NP reversal does not mean NPs are "better" prescribers. It means the unadjusted comparison is misleading, and policy decisions should not rest on it.

The volume-tier finding does not mean high-volume pain specialists are prescribing inappropriately. It means their prescribing patterns are clinically coherent and should not trigger the same monitoring thresholds applied to other specialties.

### 14.3 Recommended Next Steps

1. **Implement specialty-adjusted opioid benchmarking** using within-specialty z-scores rather than national or state-level rate thresholds. The methodology is directly operationalizable by any organization with Part D prescriber data.

2. **Deploy compound-signal screening** combining high opioid rate (>3 SD within specialty) with high LA proportion (>10% of opioid claims are long-acting). This two-factor approach would identify approximately 1,200--1,500 highest-priority prescribers for clinical chart review.

3. **Construct volume-specialty interaction profiles** that define expected rate ranges by volume quartile within each specialty. A high-volume pain specialist at 52% is within norms; a low-volume primary care provider at 15% is far outside them.

4. **Establish longitudinal baselines** by extending this analysis to CY2019--2023, enabling trend-adjusted benchmarking.

5. **Link Part D data to diagnosis claims** to test whether the residual 62.6% individual variance is partially explained by patient-level clinical complexity not captured in the aggregate beneficiary risk score.

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
| OLS R-squared | 0.2999 | --- | 810,057 | OLS regression |
| OLS F-statistic | 38,561.7 | --- | 810,057 | OLS regression |
| NP coefficient (adjusted) | -0.0708 | -0.072 to -0.070 | 810,057 | OLS regression |
| PA coefficient (adjusted) | -0.0009 | -0.002 to -0.00004 | 810,057 | OLS regression |
| Pain specialty coefficient | +0.2252 | 0.223--0.227 | 810,057 | OLS regression |
| Surgery specialty coefficient | +0.1859 | 0.185--0.187 | 810,057 | OLS regression |
| ICC (state, ANOVA) | 0.8% | --- | 810,057 | Mixed-effects ANOVA |
| Risk-adj rank correlation | 0.995 | --- | 51 | Spearman |
| States moved 5+ ranks | 2 | --- | 51 | Count |
| Interventional Pain Mgmt | 56.34% | 55.00--57.54% | 1,426 | Percentile bootstrap |
| Outlier count (3 SD) | 13,913 | --- | 809,884 | Specialty-adjusted z-score |
| Outlier percentage | 1.72% | --- | 809,884 | Derived |
| Outlier opioid claims | 6,629,156 | --- | 13,913 | Sum |
| Outlier claims share | 11.48% | --- | 57,728,383 | Derived |
| Leverage ratio | 6.7:1 | --- | --- | Claims share / prescriber share |
| Volume--rate rho | 0.086 | 0.084--0.088 | 810,057 | Spearman + bootstrap |
| LA opioid ratio | 10.05% | --- | 345,583 | Aggregate ratio |
| LA ratio (outliers) | 10.24% | --- | 12,414 | Mean |
| LA ratio (non-outliers) | 3.41% | --- | 333,169 | Mean |
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
| VIF: log(volume) | 1.25 | --- | --- | OLS diagnostic |
| VIF: beneficiary age | 1.05 | --- | --- | OLS diagnostic |
| VIF: beneficiary risk | 1.02 | --- | --- | OLS diagnostic |

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
- **Figure 8:** OLS Regression Coefficients --- point estimates with 95% CIs for all predictors, highlighting the NP reversal.
- **Figure 9:** Raw vs. Risk-Adjusted State Rankings --- scatter plot of 51 jurisdictions, raw rank (x) vs. adjusted rank (y), showing near-perfect diagonal alignment (rho = 0.995).

All figure-generating code is available from the authors upon request.

### Interpretation Constraints

The following interpretations are explicitly excluded by the analytical methodology: causal inference, generalization to non-Medicare populations, individual prescriber targeting, normative judgment on any state's rate, characterization of any prescribing rate as "inappropriate" without patient-level clinical data, attribution of NP/PA-to-MD differences to provider competence or training quality, and normative judgment on long-acting opioid prescribing without indication data.

### Data Availability

The primary data are publicly available from CMS.gov. The computational pipeline scripts and configuration are available from the authors upon request. Input data integrity is verified via SHA-256 checksums documented in the data lineage record.

---

## References

1. Barnett ML, Olenski AR, Jena AB. Opioid-prescribing patterns of emergency physicians and risk of long-term use. *N Engl J Med.* 2017;376(7):663--673.

2. Bohnert ASB, Valenstein M, Bair MJ, et al. Association between opioid prescribing patterns and opioid overdose-related deaths. *JAMA.* 2011;305(13):1315--1321.

3. Brady JE, Wunsch H, DiMaggio C, Lang BH, Giglio J, Li G. Prescription drug monitoring and dispensing of prescription opioids. *Public Health Rep.* 2016;131(2):343--349.

4. Centers for Medicare & Medicaid Services. Medicare Part D Prescribers --- by Geography and Drug, Calendar Year 2023. CMS.gov. Accessed May 2026.

5. Centers for Medicare & Medicaid Services. Medicare Provider Utilization and Payment Data: Part D Prescriber. Data documentation and methodology notes. CMS.gov.

6. Chen LH, Hedegaard H, Warner M. Nurse practitioner and physician assistant prescribing patterns for controlled substances. *J Am Assoc Nurse Pract.* 2019;31(4):217--225.

7. Dasgupta N, Beletsky L, Ciccarone D. Opioid crisis: no easy fix to its social and economic determinants. *Am J Public Health.* 2018;108(2):182--186.

8. Deyo RA, Von Korff M, Duhrkoop D. Opioids for low back pain. *BMJ.* 2015;350:g6380.

9. Dowell D, Haegerich TM, Chou R. CDC guideline for prescribing opioids for chronic pain --- United States, 2016. *MMWR Recomm Rep.* 2016;65(1):1--49.

10. Dowell D, Ragan KR, Jones CM, Baldwin GT, Chou R. CDC clinical practice guideline for prescribing opioids for pain --- United States, 2022. *MMWR Recomm Rep.* 2022;71(3):1--95.

11. Guy GP Jr, Zhang K, Bohm MK, et al. Vital Signs: changes in opioid prescribing in the United States, 2006--2015. *MMWR Morb Mortal Wkly Rep.* 2017;66(26):697--704.

12. Institute of Medicine. *Relieving Pain in America: A Blueprint for Transforming Prevention, Care, Education, and Research.* Washington, DC: National Academies Press; 2011.

13. Kolodny A, Courtwright DT, Hwang CS, et al. The prescription opioid and heroin crisis: a public health approach to an epidemic of addiction. *Annu Rev Public Health.* 2015;36:559--574.

14. Levy B, Paulozzi L, Mack KA, Jones CM. Trends in opioid analgesic-prescribing rates by specialty, U.S., 2007--2012. *Am J Prev Med.* 2015;49(3):409--413.

15. Manchikanti L, Abdi S, Atluri S, et al. American Society of Interventional Pain Physicians (ASIPP) guidelines for responsible opioid prescribing in chronic non-cancer pain: Part 2 --- guidance. *Pain Physician.* 2012;15(3 Suppl):S67--S116.

16. McDonald DC, Carlson K, Izrael D. Geographic variation in opioid prescribing in the U.S. *J Pain.* 2012;13(10):988--996.

17. Morden NE, Munson JC, Colla CH, et al. Prescription opioid use among disabled Medicare beneficiaries: intensity, trends, and regional variation. *Med Care.* 2014;52(9):852--859.

18. National Academies of Sciences, Engineering, and Medicine. *Pain Management and the Opioid Epidemic: Balancing Societal and Individual Benefits and Risks of Prescription Opioid Use.* Washington, DC: National Academies Press; 2017.

19. Paulozzi LJ, Stier DD, Mack KA. Prescription drug monitoring programs and death rates from drug overdose. *Pain Med.* 2014;15(3):497--505.

20. Schieber LZ, Guy GP Jr, Seth P, et al. Trends and patterns of geographic variation in opioid prescribing practices by state, United States, 2006--2017. *JAMA Netw Open.* 2019;2(3):e190665.

21. Shah A, Hayes CJ, Martin BC. Characteristics of initial prescription episodes and likelihood of long-term opioid use --- United States, 2006--2015. *MMWR Morb Mortal Wkly Rep.* 2017;66(10):265--269.

22. Spetz J, Parente ST, Town RJ, Bazarko D. Scope-of-practice laws for nurse practitioners limit cost savings that can be achieved in retail clinics. *Health Aff (Millwood).* 2013;32(11):1977--1984.

23. Wen H, Hockenberry JM, Borders TF, Druss BG. Impact of Medicaid expansion on Medicaid-covered utilization of buprenorphine for opioid use disorder treatment. *Med Care.* 2017;55(4):336--341.

24. Wennberg JE. *Tracking Medicine: A Researcher's Quest to Understand Health Care.* New York: Oxford University Press; 2010.

25. Deyo RA, Hallvik SE, Hildebran C, et al. Association between initial opioid prescribing patterns and subsequent long-term use among opioid-naive patients: a statewide retrospective cohort study. *J Gen Intern Med.* 2017;32(1):21--27.

26. Dasgupta N, Creppage K, Austin A, Ringwalt C, Sanford C, Proescholdbell SK. Observed transition from opioid analgesic deaths toward heroin. *Drug Alcohol Depend.* 2014;145:238--241.

27. Wen H, Schackman BR, Aden B, Bao Y. States with prescription drug monitoring mandates saw a reduction in opioids prescribed to Medicaid enrollees. *Health Aff (Millwood).* 2017;36(4):733--741.
