# The Fermi Paradox as a Survival Function: What the Silence Implies About Civilizational Hazard Rates

**James P Rice Jr.**

---

## Abstract

The Fermi paradox — the contradiction between the expected prevalence of extraterrestrial civilizations and the absence of evidence for them — has resisted resolution for over sixty years, in part because the dominant analytical framework, the Drake equation, cannot formally incorporate the observation of silence. This paper replaces the Drake equation with a survival function framework in which the silence is treated as a right-censored observation in the sense of classical survival analysis. We define the communicative lifetime of a civilization as a random variable governed by a hazard function, model civilization emergence as a Poisson process, and construct the exact likelihood for zero detections over sixty years of SETI observation. Under the exponential hazard model, we prove that the maximum likelihood estimate of the hazard rate is λ̂ = +∞, corresponding to a mean communicative lifetime of τ̂ = 0, for any positive emergence rate η > 0. This result is invariant to the value of η, to the choice of parametric hazard model (we verify it for both exponential and Weibull families), and to order-of-magnitude perturbations in the SETI detection radius and galactic emergence rate. The maximum likelihood explanation for the silence is a late-stage filter — a persistent hazard acting on civilizations after they enter the communicating state — not a deficit in civilizational emergence. We derive this conclusion as a theorem, formally reject or subsume five competing models (including the Drake equation, the Rare Earth hypothesis, and the Great Filter framework), and identify the boundary conditions under which the result holds or fails. The Weibull shape parameter k, which discriminates between increasing and decreasing hazard, is shown to be non-identifiable from zero detections alone; we characterize the data that would resolve it. The survival function framework transforms the Fermi paradox from a problem of missing parameters into a censored-data inference problem with a sharp, formally derived answer.

---

## 1. Definitions

**Definition 1 (State Space).** Let Ω = {communicating, silent, extinct} be the state space for a civilization at any time t ≥ 0. A civilization occupies exactly one state at each t. The state "communicating" means the civilization emits detectable electromagnetic signatures at Kardashev Type I or above within a radius r₀ ≈ 100 ly. The state "silent" means the civilization exists but does not emit detectable signatures. The state "extinct" is absorbing: once entered, it cannot be left.

**Definition 2 (Population).** Let N★ ≈ 10¹¹ denote the number of stars in the Milky Way capable of hosting communicating civilizations (Bland-Hawthorn & Gerhard 2016). The population of interest is the set of civilizations that have, at any point in the galaxy's history, entered the "communicating" state. We do not require an estimate of how many civilizations have emerged; the survival function conditions on the existence of at least one communicating civilization and asks how long it persists.

**Definition 3 (Communicative Lifetime).** Let T_c be a non-negative random variable representing the duration a civilization spends in the "communicating" state before transitioning to "silent" or "extinct." The survival function S(t), hazard function h(t), and cumulative hazard function H(t) are all defined with respect to T_c.

**Definition 4 (Survival Function).** The survival function S : [0, ∞) → [0, 1] is defined as

S(t) = P(T_c > t)

the probability that a civilization remains in the communicating state for longer than time t. S(0) = 1 and S(t) → 0 as t → ∞. S(t) is non-increasing and right-continuous.

**Definition 5 (Hazard Function).** The hazard function h : [0, ∞) → [0, ∞) is defined as

h(t) = lim_{Δt→0} P(t ≤ T_c < t + Δt | T_c ≥ t) / Δt

This is the instantaneous rate of transition out of the communicating state, conditional on having survived to time t. The hazard function fully determines the survival function via the relationship S(t) = exp(−H(t)), where H(t) is the cumulative hazard.

**Definition 6 (Cumulative Hazard Function).** The cumulative hazard function H : [0, ∞) → [0, ∞) is defined as

H(t) = ∫₀ᵗ h(u) du

The survival function is recovered as S(t) = exp(−H(t)).

**Definition 7 (Exponential Hazard Model).** Under the exponential hazard model, h(t) = λ for all t ≥ 0, where λ > 0 is a constant hazard rate. This yields:

S(t) = exp(−λt)

The mean communicative lifetime under this model is τ = 1/λ. The exponential model encodes the memoryless property: a civilization that has survived for t years is no more or less likely to cease communicating in the next instant than a newly communicating civilization.

**Definition 8 (Weibull Hazard Model).** Under the Weibull hazard model, h(t) = (k/λ_w)(t/λ_w)^{k−1} for t ≥ 0, where λ_w > 0 is the scale parameter and k > 0 is the shape parameter. This yields:

S(t) = exp(−(t/λ_w)^k)

The shape parameter k encodes the age-dependence of the hazard:
- k = 1: reduces to the exponential model (constant hazard, memoryless)
- k > 1: hazard increases with age — civilizations that have survived longer face higher risk of cessation (late filter)
- k < 1: hazard decreases with age — civilizations that have survived longer face lower risk (early filter, or survivorship selection)

**Definition 9 (Observational Baseline).** Let T_obs = 60 years denote the duration of systematic SETI observation (Tarter 2001). Let n = 0 denote the number of confirmed detections of communicating civilizations during this period. The pair (T_obs, n = 0) constitutes a right-censored observation: we know that no civilization was detected during [0, T_obs], but we cannot observe beyond T_obs.

**Definition 10 (Censored Observation).** The observation n = 0 over the interval [0, T_obs] is a Type I right-censored datum. It provides information about the survival function through the likelihood contribution L = S(T_obs), not through a point estimate P(detection) = 0. The distinction is fundamental: P = 0 implies impossibility; S(T_obs) near 1 implies that the expected number of detectable civilizations at any given time is small, which constrains the hazard rate.

**Definition 11 (Galaxy Age Horizon).** Let T_gal = 13.6 × 10⁹ years denote the age of the Milky Way (Planck Collaboration 2020). T_gal sets the upper bound on the time domain over which civilizations could have emerged and entered the communicating state. The survival function is evaluated over [0, T_gal], though the observational constraint applies only to the recent window [T_gal − T_obs, T_gal].

**Definition 12 (Detection Radius).** Let r₀ ≈ 100 ly denote the radius within which current SETI instrumentation could detect a Kardashev Type I transmitter (Tarter 2001; Enriquez et al. 2017). The volume surveyed is V₀ = (4/3)π r₀³. The fraction of the galactic disk surveyed is f_sky = V₀ / V_gal, where V_gal is the volume of the Milky Way's stellar disk.

**Definition 13 (Likelihood Function).** Given the censored observation (T_obs, n = 0) and a hazard model parameterized by θ, the likelihood function is

L(θ) = P(n = 0 | θ) = [S(T_obs; θ)]^{N_eff}

where N_eff is the effective number of independently observable civilizations within the surveyed volume during T_obs. The maximum likelihood estimate θ̂ maximizes L(θ), or equivalently minimizes −log L(θ).

**Definition 14 (Effective Observable Population).** Let N_eff denote the expected number of civilizations that could, in principle, have been detected within the surveyed volume V₀ during the observational window T_obs. N_eff depends on the emergence rate, the spatial density of civilizations, and the fraction of the galaxy surveyed. In the exponential model, N_eff = ρ · V₀ · T_obs, where ρ is the spatial density of civilizations entering the communicating state per unit volume per unit time. The constraint n = 0 bounds N_eff · (1 − S(T_obs)) from above.

**Symbol Table**

| Symbol | Definition | Introduced |
|--------|-----------|------------|
| Ω | State space {communicating, silent, extinct} | Def. 1 |
| t | Time variable (years) | Def. 1 |
| N★ | Milky Way stellar count, ≈ 10¹¹ | Def. 2 |
| T_c | Communicative lifetime (random variable) | Def. 3 |
| S(t) | Survival function, P(T_c > t) | Def. 4 |
| h(t) | Hazard function | Def. 5 |
| H(t) | Cumulative hazard function | Def. 6 |
| λ | Constant hazard rate (exponential model) | Def. 7 |
| τ | Mean communicative lifetime, 1/λ | Def. 7 |
| k | Weibull shape parameter | Def. 8 |
| λ_w | Weibull scale parameter | Def. 8 |
| T_obs | Observational baseline, 60 years | Def. 9 |
| n | Number of confirmed detections, = 0 | Def. 9 |
| T_gal | Galaxy age, 13.6 Gyr | Def. 11 |
| r₀ | SETI detection radius, ≈ 100 ly | Def. 12 |
| V₀ | Surveyed volume, (4/3)πr₀³ | Def. 12 |
| f_sky | Fraction of galaxy surveyed, V₀/V_gal | Def. 12 |
| V_gal | Volume of the Milky Way's stellar disk | Def. 12 |
| L(θ) | Likelihood function | Def. 13 |
| θ | Hazard model parameter vector | Def. 13 |
| θ̂ | Maximum likelihood estimate of θ | Def. 13 |
| λ̂ | Maximum likelihood estimate of λ (= θ̂ when θ = λ) | Def. 13 |
| N_eff | Effective observable population | Def. 14 |
| ρ | Spatial density of emerging civilizations | Def. 14 |

---

## 2. Introduction

The Fermi paradox — the apparent contradiction between the high prior probability of extraterrestrial civilizations and the absence of evidence for them — has generated six decades of proposed resolutions. Most of these resolutions share a common mathematical framework: the Drake equation (Drake 1961). This paper argues that the Drake equation is the wrong framework, and that replacing it with survival analysis transforms the paradox from a puzzle of missing probabilities into a formal inference problem with a sharp, derivable answer.

### 2.1 The Drake Equation and Its Failure

Drake (1961) proposed estimating the number of detectable civilizations as a product of independent factors: star formation rate, fraction of stars with planets, fraction of those with life, and so on. The equation treats civilizational emergence as a chain of independent probabilities and outputs a point estimate N.

Drake proposed the multiplicative probability chain N = R★ · f_p · n_e · f_l · f_i · f_c · L to estimate the number of detectable civilizations, but this framework fails under three conditions that the Fermi paradox specifically presents. First, the Drake equation cannot incorporate censored observations: the observation n = 0 is not informative within the Drake framework because the equation outputs an expected count N, and N = 0 is achieved only when one or more factors is exactly zero — which is a statement about impossibility, not about the duration or timing of civilizational communication. Second, the Drake equation treats civilizational lifetime L as a free parameter to be estimated independently, when in fact it is the quantity most directly constrained by the silence. Third, the equation assumes independence among its factors, precluding any formal treatment of how the hazard of civilizational cessation depends on age or stage of development. This paper introduces a survival function framework (Definitions 1–14) in which the silence is a censored observation that directly constrains the hazard rate, resolving all three failures.

### 2.2 From Point Estimates to Survival Analysis

The core methodological shift is this: instead of asking "how many civilizations exist?" (a point estimate), we ask "given that none have been detected, what does the survival function imply about the rate at which civilizations cease to communicate?" This reframing has three consequences.

First, the observation n = 0 over T_obs = 60 years is no longer a puzzle to be explained away — it is a censored datum to be analyzed. In survival analysis (Cox 1972), right-censored observations are the norm, not the exception. Medical trials, engineering reliability studies, and actuarial science all build inference from censored data. The Fermi paradox is, mathematically, no different.

Second, the hazard function h(t) replaces Drake's free parameter L with a formal object that can be estimated from data. Under the exponential model (Definition 7), the maximum likelihood hazard rate λ̂ given n = 0 constrains the mean communicative lifetime τ = 1/λ̂ directly. Under the Weibull model (Definition 8), the shape parameter k reveals whether the hazard increases or decreases with civilizational age — that is, whether the dominant filter is early or late.

Third, the survival framework provides a natural formalism for competing hypotheses about filter timing. Hart (1975) proposed the "Fact A" argument — that the absence of extraterrestrial visitors implies an early filter preventing civilizations from arising in the first place — but Hart's argument assumes the filter location rather than deriving it from data. In the survival framework, the filter location is not assumed; it is estimated from the shape parameter k of the Weibull hazard model, with k > 1 indicating a late filter and k < 1 indicating an early filter. This paper introduces a formal derivation (presented in Section 3) that replaces Hart's assumption with an inference.

### 2.3 Positioning Against Prior Work

Hanson (1998) introduced the "Great Filter" concept, arguing that at least one step in the chain from inert matter to galaxy-spanning civilization must be extremely improbable. Hanson proposed the Great Filter as a conceptual framework for understanding why the galaxy appears empty, but the Great Filter framework fails to distinguish between early and late filter locations using formal inference — Hanson's analysis identifies the existence of a filter but treats its location as a matter for prior belief rather than posterior estimation. This paper introduces a survival function formalism in which the filter location is derived from the maximum likelihood hazard rate under the Weibull model, succeeding where Hanson's framework required assumption.

Ćirković (2018) provided a comprehensive taxonomy of Fermi paradox solutions, organizing them by mechanism type. Ćirković catalogued the solution space exhaustively, but the taxonomy does not provide a formal criterion for discriminating among solutions — the categories are descriptive, not inferential. This paper introduces a likelihood-based framework that formally discriminates among filter hypotheses by their consistency with the censored observation, providing the inferential criterion that Ćirković's taxonomy lacks.

### 2.4 What This Paper Will Show

The remainder of this paper proceeds as follows. Section 3 derives the maximum likelihood hazard rate λ̂ under the exponential model given n = 0 detections over T_obs years, and extends the analysis to the Weibull model to formally distinguish early from late filter hypotheses. Section 4 applies these results to the observed SETI silence, presents a sensitivity analysis varying all primary parameters, formally rejects competing models, and identifies the boundary conditions under which the result holds or fails. Section 5 places the contribution in the context of prior work and states the paper's limitations and open problems.

The central claim of this paper — that under exponential hazard, the maximum likelihood estimate of the hazard rate implies a mean communicative lifetime consistent only with a dominant post-technological filter — will be derived as a theorem in Section 3. It is stated here as a preview, not as a result. The derivation, not this statement, is the contribution.

No figures are required in this section.

---

## 3. Core Derivation

This section derives the maximum likelihood hazard rate consistent with zero detections, first under the exponential model and then under the Weibull extension. The filter location result is stated and proved as a theorem.

### 3.1 Likelihood Construction for the Censored Observation

We construct the exact likelihood for the observation n = 0 detections over T_obs years, refining the schematic form given in Definition 13.

**Proposition 1 (Steady-State Population Model).** Let civilizations emerge in the detectable volume V₀ as a homogeneous Poisson process with rate η > 0 (civilizations per year). Each civilization, upon emergence, communicates for a random duration T_c with survival function S(t; θ), where θ is the parameter vector of the hazard model. By the M/G/∞ queueing result (Takács 1962), the steady-state number of concurrently communicating civilizations N follows a Poisson distribution with mean

  μ(θ) = η · E[T_c | θ] = η · ∫₀^∞ S(t; θ) dt

*Proof.* The M/G/∞ queue models an infinite-server system with Poisson arrivals at rate η and general service time distribution with survival function S(t; θ). In steady state, the number of busy servers (here, communicating civilizations) follows Poisson(η · E[service time]) (Takács 1962, Theorem 1). The stationarity condition requires T_gal >> E[T_c | θ]. We assume this holds and verify consistency post hoc: the MLE derived in §3.2 gives E[T_c] → 0, so T_gal >> E[T_c] is satisfied everywhere in the parameter space except the degenerate limit λ → 0 (infinite lifetime), which is excluded by λ > 0. For any finite λ > 0, E[T_c] = 1/λ < ∞ << T_gal = 13.6 Gyr. □

**Remark on Definition 13.** Definition 13 expressed the likelihood as L(θ) = [S(T_obs; θ)]^{N_eff}. This captures the correct intuition — the likelihood depends on the survival function and the effective population — but conflates the per-civilization survival probability with the population-level detection probability. The Poisson construction above is the exact form: L depends on μ = η · E[T_c], not on S(T_obs) directly. The two formulations converge qualitatively (both constrain the hazard rate upward), but the Poisson form is the correct basis for maximum likelihood estimation.

**Proposition 2 (Censored Likelihood).** Given n = 0 detections, the likelihood function for the hazard model parameter θ is:

  L(θ | n = 0) = P(N = 0 | θ) = exp(−μ(θ))

and the log-likelihood is:

  ℓ(θ | n = 0) = −μ(θ) = −η · ∫₀^∞ S(t; θ) dt

*Proof.* Direct from the Poisson probability mass function: P(N = k) = μ^k · exp(−μ) / k!, evaluated at k = 0. □

**Remark.** This likelihood treats the zero-detection observation as informative data, not as an absence of data. The censored observation constrains the expected number of concurrent communicators μ from above: large μ makes n = 0 improbable. This is the fundamental advantage of the survival framework over the Drake equation: the silence is evidence that can be analyzed, not a puzzle to be explained away.

### 3.2 Maximum Likelihood Estimation Under Exponential Hazard

Under the exponential hazard model (Definition 7), S(t; λ) = exp(−λt) and E[T_c] = 1/λ. The steady-state expected count is:

  μ(λ) = η/λ

and the log-likelihood is:

  ℓ(λ) = −η/λ

**Lemma 1 (Monotonicity of Log-Likelihood).** The function ℓ(λ) = −η/λ is strictly increasing on (0, ∞) for all η > 0.

*Proof.* dℓ/dλ = η/λ² > 0 for all λ > 0 and η > 0. □

**Theorem 1 (Boundary MLE Under Exponential Hazard).** Under the exponential hazard model with emergence rate η > 0, the maximum likelihood estimate of the hazard rate given n = 0 detections is:

  λ̂_ML = sup{λ > 0 : ℓ(λ) is defined} = +∞

Equivalently, the maximum likelihood estimate of the mean communicative lifetime is:

  τ̂_ML = 1/λ̂_ML = 0

*Proof.* By Lemma 1, ℓ(λ) is strictly increasing on (0, ∞). The supremum of ℓ is lim_{λ→∞} (−η/λ) = 0, which is not attained at any finite λ. Therefore the MLE lies at the boundary of the parameter space: λ̂ = +∞, τ̂ = 0. □

**Remark.** The boundary MLE is not a defect of the model — it is the result. The data maximally favor infinite hazard rate. This is the mathematical encoding of the observation that zero detections are most consistent with civilizations that cease communicating immediately upon emergence. No finite hazard rate is more consistent with the data than a larger one.

**Proposition 3 (Confidence Bound on Mean Communicative Lifetime).** For significance level α ∈ (0, 1), the (1 − α) upper confidence bound on the mean communicative lifetime τ under the exponential model is:

  τ_α = −ln(α) / η

*Proof.* We require P(N = 0 | τ) ≥ α, i.e., the observed outcome must not fall in the rejection region:

  exp(−η · τ) ≥ α
  −η · τ ≥ ln(α)
  τ ≤ −ln(α) / η

The bound τ_α = −ln(α)/η is the largest value of τ consistent with the observation n = 0 at confidence level (1 − α). □

**Numerical Illustration.** At the 95% confidence level (α = 0.05), τ₀.₀₅ ≈ 3.0/η. The emergence rate η in the detectable volume depends on the galactic emergence rate η_gal and the fraction of the galaxy surveyed f_sky = V₀/V_gal (Definition 12):

  η = η_gal · f_sky

Representative values, using f_sky ≈ 2.7 × 10⁻⁷ (for r₀ = 100 ly):

| η_gal (yr⁻¹) | Interpretation | η (yr⁻¹) | τ₀.₀₅ (years) | τ₀.₀₅ / T_gal |
|--------------|----------------|-----------|---------------|---------------|
| 10⁻⁴ | One per 10⁴ yr (optimistic) | 2.7 × 10⁻¹¹ | 1.1 × 10¹¹ | ~8 |
| 10⁻⁶ | One per Myr | 2.7 × 10⁻¹³ | 1.1 × 10¹³ | ~800 |
| 10⁻⁹ | One per Gyr (conservative) | 2.7 × 10⁻¹⁶ | 1.1 × 10¹⁶ | ~10⁶ |

**Remark.** The confidence bound τ₀.₀₅ exceeds T_gal for all tabulated η values when the detectable volume is restricted to r₀ = 100 ly. This reflects the small fraction of the galaxy surveyed (f_sky ≈ 10⁻⁷), not a weakness of the model. The bound tightens linearly with f_sky and with η_gal. For the constraint to imply τ₀.₀₅ < T_gal, we require η > −ln(0.05)/T_gal ≈ 2.2 × 10⁻¹⁰ yr⁻¹ in the detectable volume. The sensitivity of the confidence bound to these parameters is analyzed in Section 4.

The critical result is not the confidence bound (which depends on η), but the MLE itself: **the maximum likelihood estimate λ̂ = +∞ is independent of η** (Theorem 1). For any emergence rate, the data most favor a late filter. The confidence bound tells us how strongly, but the direction is invariant.

### 3.3 Filter Location

**Definition 15 (Filter Classification).** A *late-stage filter* (or *late filter*) is any persistent hazard that acts on civilizations after they enter the communicating state. Formally, a late filter corresponds to a hazard function h(t) > 0 for t > 0: the instantaneous risk of cessation per unit time for civilizations that are currently communicating. An *early filter* corresponds to a reduction in the emergence rate η: civilizations rarely arise, but those that do may persist. The survival model separates these two mechanisms into independent parameters: η governs pre-emergence filtering and h(t) (parameterized by λ or (k, λ_w)) governs post-emergence filtering.

**Remark.** This classification is exhaustive within the model. The expected number of concurrent communicators μ = η · E[T_c] can be made small either by reducing η (early filter) or by reducing E[T_c] (late filter). The survival framework does not assume which mechanism dominates — it estimates them separately.

**Theorem 2 (Late Filter Derivation).** Under the survival function framework with exponential hazard and emergence rate η > 0, the observation n = 0 detections over T_obs years implies that the maximum likelihood explanation for the silence is a late-stage filter acting on communicating civilizations. Specifically: for any η > 0, the MLE of the post-emergence hazard rate is λ̂ = +∞, meaning the data favor the strongest possible late filter. This result is silent on whether an early filter (small η) also operates.

*Proof.* The proof proceeds in three steps.

*Step 1 (Parameter separation).* The expected number of concurrent communicators is μ = η · τ = η/λ (Proposition 1, exponential case). The parameter η captures all pre-emergence factors: star formation, planet habitability, abiogenesis probability, evolutionary contingency, and any other condition required for a civilization to enter the communicating state. The parameter λ = 1/τ captures all post-emergence factors: technology-driven existential risk, resource depletion, voluntary cessation of communication, or any other mechanism that causes a communicating civilization to stop. The survival model assigns η and λ independent roles: η sets the arrival rate; λ sets the departure rate. The observation n = 0 constrains their product η/λ = η · τ to be small. The log-likelihood ℓ(λ) = −η/λ depends on both η and λ jointly, but the critical property is this: for any fixed η > 0, the MLE of λ is at +∞ (Theorem 1). The MLE direction is independent of the particular value of η.

*Step 2 (MLE of the hazard rate).* By Theorem 1, the maximum likelihood estimate of the hazard rate is λ̂ = +∞ for any η > 0. The log-likelihood ℓ(λ) = −η/λ is strictly increasing for any positive emergence rate (Lemma 1). No finite value of λ is a better explanation of the data than a larger one. Crucially, this result holds for all η > 0: whether civilizations emerge once per millennium or once per eon, the MLE of the post-emergence hazard rate is the same.

*Step 3 (Identification of the late filter).* The parameter λ is, by construction (Definitions 5 and 7), the instantaneous rate at which civilizations transition out of the communicating state. A large λ implies a strong force driving civilizations from communication to silence or extinction after they have emerged. By Definition 15, this is a late-stage filter. The MLE λ̂ = +∞ implies that, among all possible hazard rates, the data are maximally consistent with the strongest possible post-emergence hazard. The late filter is therefore the maximum likelihood explanation for the silence.

The argument is independent of η. It does not assert that η is large (many civilizations emerge) or small (few emerge). It asserts only that whatever the emergence rate, the data favor the highest possible post-emergence cessation rate. The silence is explained by what happens after civilizations arise, not by whether they arise at all. □

**Corollary 1 (Resolution of Drake's Conflation).** The Drake equation N = R★ · f_p · n_e · f_l · f_i · f_c · L treats the civilizational lifetime L as one factor among many. The observation N = 0 constrains the product of all factors but provides no basis for identifying which factor is responsible. The survival framework decomposes the same observation into two orthogonal components: the emergence rate η (analogous to the product R★ · f_p · n_e · f_l · f_i · f_c) and the hazard rate λ = 1/L. Theorem 1 shows that the MLE of λ is at +∞ regardless of η, identifying the post-emergence hazard (i.e., the factor L in Drake's notation) as the dominant constraint. The survival framework succeeds where the Drake equation is silent because it separates what the Drake equation conflates.

### 3.4 Weibull Extension: Age-Dependent Hazard

Under the Weibull hazard model (Definition 8), the mean communicative lifetime is:

  E[T_c] = λ_w · Γ(1 + 1/k)

where Γ denotes the gamma function. The steady-state expected count is:

  μ(k, λ_w) = η · λ_w · Γ(1 + 1/k)

and the log-likelihood is:

  ℓ(k, λ_w) = −η · λ_w · Γ(1 + 1/k)

**Theorem 3 (Weibull Boundary MLE).** Under the Weibull hazard model with emergence rate η > 0 and n = 0 detections, the maximum likelihood estimate of the scale parameter satisfies λ̂_w → 0⁺ for every k > 0. The corresponding MLE of the mean communicative lifetime is τ̂ = λ̂_w · Γ(1 + 1/k) → 0. The joint MLE over (k, λ_w) is the set {(k, 0⁺) : k > 0}, and all points in this set achieve the same supremum likelihood (lim → 1).

*Proof.* For any fixed k > 0, Γ(1 + 1/k) is a positive constant. The log-likelihood ℓ(k, λ_w) = −η · λ_w · Γ(1 + 1/k) is strictly increasing as λ_w → 0⁺ (since ℓ approaches 0 from below, and −η · λ_w · Γ(1 + 1/k) < 0 for all λ_w > 0). The supremum over λ_w > 0 is not attained, and the MLE is at the boundary λ̂_w = 0⁺. Since this holds for every k > 0, and the supremum likelihood lim_{λ_w→0⁺} exp(−η · λ_w · Γ(1 + 1/k)) = 1 is the same for all k, the joint MLE is not a single point but the boundary set {(k, 0⁺) : k > 0}. This confirms that k is not identified (see Proposition 4) while τ̂ → 0 is universal. □

**Proposition 4 (Shape Parameter Non-Identifiability).** Under the Weibull hazard model with n = 0 detections, the shape parameter k is not identifiable from the likelihood alone. For any k₁, k₂ > 0 and any target likelihood value L₀ ∈ (0, 1), there exist scale parameters λ_w^{(1)}, λ_w^{(2)} > 0 such that L(k₁, λ_w^{(1)}) = L(k₂, λ_w^{(2)}) = L₀.

*Proof.* The likelihood depends on (k, λ_w) only through μ = η · λ_w · Γ(1 + 1/k). For any target μ₀ = −ln(L₀) > 0 and any k > 0, set λ_w = μ₀ / (η · Γ(1 + 1/k)) > 0 to achieve L = exp(−μ₀) = L₀. Therefore every point on the likelihood surface with the same μ value gives the same likelihood, and k is not identifiable from n = 0 alone. □

**Remark.** The non-identifiability of k is a scope boundary, not a limitation. The Weibull shape parameter encodes the *nature* of the post-emergence hazard:

| k value | Hazard trend | Physical interpretation |
|---------|-------------|----------------------|
| k < 1 | h(t) decreasing | Early-life risk dominates; survivors become resilient |
| k = 1 | h(t) constant | Memoryless hazard; reduces to exponential model |
| k > 1 | h(t) increasing | Risk grows with civilizational age; late-acting destruction |

Distinguishing among these requires additional data beyond n = 0 — for example, a detection with an estimated civilizational age, or a temporal pattern of detections. The present paper's result does not require k to be identified: the late-filter conclusion (Theorem 2) rests on the MLE of τ → 0, which holds for all k > 0 (Theorem 3). The Weibull extension is stated here to establish the formal framework for future observations that could discriminate among late-filter mechanisms.

### 3.5 Robustness

**Proposition 5 (Invariance to Hazard Model).** The late-filter conclusion (Theorem 2) holds under any parametric hazard model with parameter θ for which E[T_c | θ] → 0 as θ is taken to its boundary MLE.

*Proof.* The likelihood under any hazard model is L(θ) = exp(−η · E[T_c | θ]) (Proposition 2). The MLE maximizes L, which requires minimizing E[T_c | θ] over the parameter space. If the infimum of E[T_c | θ] is 0 and is not attained at any interior point, then the MLE sends E[T_c] → 0, and the data favor the shortest possible communicative lifetime. By Definition 15, this corresponds to maximal post-emergence hazard — a late filter. The result is verified for both models analyzed in this paper: exponential (θ = λ, E[T_c] = 1/λ → 0 as λ → ∞) and Weibull (θ = (k, λ_w), E[T_c] = λ_w · Γ(1 + 1/k) → 0 as λ_w → 0⁺). The proposition extends to any parametric family satisfying the stated condition. □

**Proposition 6 (Dependence on the Existence Assumption).** The late-filter conclusion requires the assumption η > 0: at least one civilization has emerged in the detectable volume over galactic history. If η = 0, the model is degenerate — μ = 0 regardless of λ — and the silence is trivially explained without any filter.

*Proof.* If η = 0, then ℓ(λ) = 0 for all λ, and the likelihood provides no information about λ. The MLE is undefined, and no filter conclusion (early or late) can be drawn. The assumption η > 0 is equivalent to the assumption that the Fermi paradox is a genuine puzzle — that at least one civilization could, in principle, have been detected. Without this assumption, there is no paradox and no need for a filter. □

**Remark.** The assumption η > 0 is minimal. It does not require a specific value of η, nor does it require that η be large. It requires only that the emergence of communicating civilizations is not impossible. Under this assumption, and under any hazard model for which E[T_c] can be driven to zero, the silence is best explained by a late filter. The quantitative strength of the conclusion (the tightness of the bound on τ) depends on η, but the qualitative direction (late filter, not early) does not.

### Symbol Table (additions to Section 1)

| Symbol | Definition | Introduced |
|--------|-----------|------------|
| μ(θ) | Expected number of concurrent communicators, η · E[T_c] | Prop. 1 |
| η | Emergence rate in detectable volume (civ/yr) | Prop. 1 |
| η_gal | Galactic emergence rate (civ/yr) | §3.2 |
| τ_α | (1−α) confidence upper bound on τ | Prop. 3 |
| λ̂_ML | MLE of hazard rate (= +∞ under exponential) | Thm. 1 |
| τ̂_ML | MLE of mean communicative lifetime (= 0) | Thm. 1 |

---

## 4. Application and Boundary Conditions

This section applies the survival framework derived in Section 3 to the observed SETI silence. We present a sensitivity analysis varying all primary parameters, formally reject competing models, and identify the boundary conditions under which the late-filter result holds or fails. All three figures are specified with Python/matplotlib code.

### 4.1 Sensitivity Analysis

The late-filter conclusion (Theorem 2) rests on the MLE λ̂ = +∞, which is invariant to parameter choices (Proposition 5). The *quantitative strength* of the conclusion — specifically, the upper confidence bound τ_α on the mean communicative lifetime — depends on three parameters: the emergence rate η, the SETI detection radius r₀, and the galaxy age T_gal. We vary each by orders of magnitude to determine whether the qualitative conclusion survives.

**Setup.** From Proposition 3, the (1 − α) upper confidence bound on τ under the exponential model is:

  τ_α = −ln(α) / η

where η = η_gal · f_sky and f_sky = V₀ / V_gal. The surveyed volume is V₀ = (4/3)πr₀³ and the galactic disk volume is V_gal ≈ 8.0 × 10¹² ly³ (assuming a disk of radius 50,000 ly and thickness 1,000 ly). Thus:

  f_sky(r₀) = (4/3)πr₀³ / V_gal

**Table 1. Sensitivity of the 95% confidence bound τ₀.₀₅ to parameter variation.**

| η_gal (yr⁻¹) | r₀ (ly) | f_sky | η (yr⁻¹) | τ₀.₀₅ (yr) | τ₀.₀₅ / T_gal | Late filter? |
|--------------|---------|-------|-----------|------------|---------------|-------------|
| 10⁻⁴ | 100 | 5.2 × 10⁻⁷ | 5.2 × 10⁻¹¹ | 5.7 × 10¹⁰ | 4.2 | Indeterminate |
| 10⁻⁴ | 1,000 | 5.2 × 10⁻⁴ | 5.2 × 10⁻⁸ | 5.7 × 10⁷ | 4.2 × 10⁻³ | **Yes** |
| 10⁻⁴ | 10,000 | 0.52 | 5.2 × 10⁻⁵ | 5.7 × 10⁴ | 4.2 × 10⁻⁶ | **Yes** |
| 10⁻⁶ | 100 | 5.2 × 10⁻⁷ | 5.2 × 10⁻¹³ | 5.7 × 10¹² | 4.2 × 10² | Indeterminate |
| 10⁻⁶ | 1,000 | 5.2 × 10⁻⁴ | 5.2 × 10⁻¹⁰ | 5.7 × 10⁹ | 0.42 | **Yes** |
| 10⁻⁶ | 10,000 | 0.52 | 5.2 × 10⁻⁷ | 5.7 × 10⁶ | 4.2 × 10⁻⁴ | **Yes** |
| 10⁻⁹ | 100 | 5.2 × 10⁻⁷ | 5.2 × 10⁻¹⁶ | 5.7 × 10¹⁵ | 4.2 × 10⁵ | Indeterminate |
| 10⁻⁹ | 1,000 | 5.2 × 10⁻⁴ | 5.2 × 10⁻¹³ | 5.7 × 10¹² | 4.2 × 10² | Indeterminate |
| 10⁻⁹ | 10,000 | 0.52 | 5.2 × 10⁻¹⁰ | 5.7 × 10⁹ | 0.42 | **Yes** |

**Reading the table.** "Late filter?" is marked **Yes** when τ₀.₀₅ < T_gal (the 95% upper bound on communicative lifetime is shorter than the age of the galaxy, meaning civilizations are constrained to be short-lived) and "Indeterminate" when τ₀.₀₅ ≥ T_gal (the confidence bound is too loose to rule out long-lived civilizations at the 95% level).

**Interpretation.** Three regimes emerge:

1. *Strong constraint* (τ₀.₀₅ << T_gal): When the detectable volume is large (r₀ ≥ 1,000 ly) and the emergence rate is moderate to high (η_gal ≥ 10⁻⁶ yr⁻¹), the confidence bound constrains τ to a small fraction of galactic history. The late-filter conclusion is quantitatively strong.

2. *Marginal constraint* (τ₀.₀₅ ≈ T_gal): At the boundary — for instance, η_gal = 10⁻⁶ yr⁻¹ with r₀ = 1,000 ly, or η_gal = 10⁻⁹ yr⁻¹ with r₀ = 10,000 ly — the bound is approximately one galactic age. The late-filter conclusion holds but not strongly.

3. *Weak constraint* (τ₀.₀₅ >> T_gal): When both the detectable volume is small (r₀ = 100 ly) and the emergence rate is low (η_gal ≤ 10⁻⁶ yr⁻¹), the observation n = 0 is consistent with long-lived civilizations existing beyond the surveyed volume. The late-filter conclusion is not supported at the 95% level.

**Critical observation.** In all nine parameter combinations, the MLE remains λ̂ = +∞ (Theorem 1). The qualitative direction of the result — late filter, not early — is invariant to all parameter choices. Only the quantitative strength varies. The sensitivity table demonstrates that the conclusion is robust in direction but parameter-dependent in magnitude.

**Table 2. Sensitivity to galaxy age T_gal.**

| T_gal (Gyr) | η_gal (yr⁻¹) | r₀ (ly) | τ₀.₀₅ / T_gal | Conclusion change? |
|-------------|--------------|---------|---------------|-------------------|
| 10.0 | 10⁻⁶ | 1,000 | 0.57 | No (still < 1) |
| 13.6 | 10⁻⁶ | 1,000 | 0.42 | Baseline |
| 15.0 | 10⁻⁶ | 1,000 | 0.38 | No (still < 1) |

The confidence bound τ₀.₀₅ is independent of T_gal (it depends only on η). The ratio τ₀.₀₅/T_gal changes, but since our primary comparison is τ₀.₀₅ versus T_gal, the conclusion is insensitive to galaxy age within the range permitted by observational uncertainty (13.6 ± 0.1 Gyr) and even under order-of-magnitude perturbation.

### 4.2 Formal Rejection of Competing Models

We now formally compare the survival function framework against five competing models. For each, we state the model's core claim, identify the specific formal property it lacks, and show why it is either subsumed by or inconsistent with the survival framework.

**Model 1: The Drake Equation (Drake 1961)**

*Core claim.* The number of detectable civilizations is N = R★ · f_p · n_e · f_l · f_i · f_c · L.

*Formal rejection.* The Drake equation fails on three counts, each of which is resolved by the survival framework:

(a) *Cannot incorporate censored observations.* The observation n = 0 within the Drake equation implies that at least one multiplicative factor is zero, which is a statement of impossibility. In the survival framework, n = 0 is a censored datum that constrains the hazard rate (Definition 10, Proposition 2). The Drake equation treats the silence as a deficiency of input parameters; the survival framework treats it as data.

(b) *Lifetime L is a free parameter, not an estimand.* Drake's L must be guessed or estimated from non-SETI data. In the survival framework, L = 1/λ is the quantity directly constrained by the silence (Theorem 1). The framework transforms L from an input into an output.

(c) *Independence assumption prevents filter discrimination.* The multiplicative structure of the Drake equation assumes that the factors are independent. The survival framework separates the emergence rate η (pre-communication factors) from the hazard rate λ (post-communication factors) and shows that the MLE of λ is at +∞ independently of η (Theorem 2, Step 1). This separation is not available within the Drake framework.

*Status:* **Subsumed.** The survival framework recovers the Drake equation's population estimate as a special case (μ = η/λ corresponds to N when η encodes all Drake pre-factors and 1/λ = L), but provides inferential structure that the Drake equation lacks.

**Model 2: Rare Earth / Fact A (Hart 1975)**

*Core claim.* The absence of extraterrestrial visitors implies that the emergence of intelligence is rare — i.e., that a strong early filter prevents civilizations from arising.

*Formal rejection.* Hart's argument assumes that the filter is early (small η) without deriving this from data. In the survival framework, the filter location is not assumed but estimated. Theorem 2 demonstrates that for any η > 0, the MLE of the post-emergence hazard rate λ is at +∞. The data favor a late filter regardless of the emergence rate. Hart's early-filter hypothesis is not rejected as impossible, but it is shown to be the non-maximum-likelihood explanation: given any non-zero emergence rate, the data are better explained by high post-emergence hazard than by low emergence rate.

More precisely: the observation n = 0 constrains μ = η/λ to be small. This can be achieved by small η (Hart's early filter), large λ (late filter), or both. The survival framework shows that for any fixed η > 0, the likelihood is maximized at λ → ∞ (Lemma 1). Hart's explanation requires λ to be moderate or small and η to be vanishingly small — a parameter configuration that, while possible, achieves a lower likelihood than λ → ∞ for the same η.

*Status:* **Inconsistent with the MLE.** Hart's early filter is not ruled out but is shown to be the non-ML explanation.

**Model 3: The Great Filter (Hanson 1998)**

*Core claim.* At least one evolutionary step between inert matter and galaxy-spanning civilization has extremely low probability (the "Great Filter"), explaining the apparent emptiness of the galaxy.

*Formal rejection.* Hanson's framework identifies the existence of a filter but does not derive its location from data. Hanson explicitly frames the question as: "is the filter behind us or ahead of us?" and treats the answer as a matter for prior belief and auxiliary evidence (fossil record, future risk assessment), not as a quantity that can be estimated from the SETI observation itself.

The survival framework resolves this. Theorem 2 derives the filter location from the observation n = 0: the MLE of the post-emergence hazard rate is λ̂ = +∞, which by Definition 15 corresponds to a late filter. Where Hanson assumes the filter's existence and debates its location, the survival framework derives both: the filter's existence follows from the non-degenerate likelihood (Proposition 2), and its location follows from the MLE (Theorem 2).

The distinction is methodological: Hanson's Great Filter is a conceptual contribution (naming the problem); the survival function framework is an inferential contribution (solving it). The two are complementary, not contradictory — but the survival framework provides the formal derivation that Hanson's framework lacks.

*Status:* **Subsumed.** The survival framework derives what the Great Filter framework assumes.

**Model 4: Non-Poisson Emergence**

*Core claim.* Civilization emergence may not follow a homogeneous Poisson process. If emergence is clustered (e.g., following galactic habitability windows) or self-exciting (e.g., panspermia creating correlated emergence events), the M/G/∞ queueing model (Proposition 1) may be misspecified.

*Formal assessment.* This is a legitimate model extension, not a competing model. The Poisson assumption enters through Proposition 1, which yields the steady-state mean μ = η · E[T_c]. Under non-Poisson emergence:

(a) If emergence is a renewal process (independent but non-exponentially distributed inter-arrival times), the M/G/∞ result still holds in steady state as long as the arrival process is stationary (Takács 1962). The late-filter conclusion is unaffected.

(b) If emergence is non-stationary (time-varying rate η(t)), the steady-state assumption breaks down. The expected count at the observation time becomes μ(t) = ∫₀ᵗ η(s) · S(t − s; θ) ds, which depends on the emergence history. However, the MLE of the hazard parameter still minimizes μ(t), and for any non-degenerate η(·), this still requires minimizing E[T_c] — i.e., maximizing the hazard rate. The direction of the MLE is preserved.

(c) If emergence is self-exciting (the emergence of one civilization increases the probability of nearby emergence — e.g., via panspermia), the civilizations are no longer independent, and the Poisson model for the concurrent count N is misspecified. This is a genuine scope boundary: the present model assumes independent civilizations. Extension to correlated emergence is deferred to future work.

*Status:* **Partially within scope.** Cases (a) and (b) are handled; case (c) is a stated scope boundary.

**Model 5: Non-Uniform Emergence Rate Over Galactic Time**

*Core claim.* The emergence rate η may vary systematically with galactic age — for example, increasing as metallicity rises, or decreasing as stellar formation rates decline. A constant η may be a poor approximation.

*Formal assessment.* This concern is addressed by the analysis of case (b) under Model 4 above. Additionally:

The confidence bound τ_α = −ln(α)/η depends on the *local* emergence rate η in the detectable volume during the observational window. If η has varied over galactic time, the relevant quantity is the rate during the recent epoch (the last ~10⁴ years, given r₀ = 100 ly and light-travel-time considerations), not the time-averaged rate. The sensitivity table (Table 1) already varies η_gal over five orders of magnitude, which subsumes any plausible variation in the recent-epoch emergence rate.

The MLE result (Theorem 1) is invariant to η entirely: λ̂ = +∞ for any η > 0. Whether η was higher in the past (more civilizations emerged) or lower (fewer emerged), the observation n = 0 still favors the highest possible post-emergence hazard rate. The late-filter conclusion is robust to temporal variation in emergence rate.

*Status:* **Within scope.** The MLE is invariant to η; the confidence bound is addressed by the sensitivity table.

### 4.3 Boundary Conditions

The late-filter conclusion holds under specific assumptions. We state the conditions under which it holds, and the conditions under which it fails.

**Conditions for the result to hold:**

(B1) *At least one civilization has emerged* (η > 0). This is the existence assumption (Proposition 6). If η = 0 identically, there is no paradox and no filter to locate. The result requires only that emergence is not impossible — it does not require a specific value of η.

(B2) *Civilizations are independently observable.* The Poisson model for the concurrent count N assumes that the emergence and cessation of each civilization is independent of others. If civilizations are causally linked (e.g., one civilization's expansion prevents another's emergence, or a galactic-scale catastrophe destroys all civilizations simultaneously), the independence assumption fails. Correlated cessation events would make n = 0 more probable than the Poisson model predicts, weakening the constraint on λ.

(B3) *The observation n = 0 is accurate.* The model conditions on zero confirmed detections. If a detection has occurred but has not been confirmed (e.g., a signal of ambiguous origin), the censored observation changes. Even a single confirmed detection (n = 1) with an estimated civilizational age would transform the inference: the shape parameter k of the Weibull model becomes identifiable (resolving the non-identifiability stated in Proposition 4), and the MLE is no longer at the boundary.

(B4) *SETI instrumentation has non-zero detection probability within the surveyed volume.* The model assumes that a Kardashev Type I civilization within r₀ would be detected. If the actual detection probability is significantly less than 1 (due to beaming fraction, frequency mismatch, or intermittent transmission), the effective surveyed volume is smaller than V₀, and η is correspondingly reduced. The MLE direction is preserved (Theorem 1 is invariant to η), but the confidence bound loosens.

(B5) *The communicating state is well-defined.* The model assumes a binary distinction between "communicating" (detectable) and "not communicating" (silent or extinct). If civilizations transition gradually (e.g., reducing detectable emissions as technology advances beyond electromagnetic communication), the hazard function describes the rate of transition below the detection threshold, not the rate of extinction. The late-filter conclusion then refers to a filter against *continued detectability*, which may include technological transcendence as well as destruction. This is a feature of the model, not a limitation: the survival function constrains what is observable, and the silence constrains the hazard rate of the observable-to-unobservable transition regardless of its cause.

**Conditions under which the result fails:**

(F1) *η = 0.* No civilizations have ever emerged. The paradox dissolves and no filter is needed (Proposition 6).

(F2) *Civilizations are undetectable by design.* If communicating civilizations deliberately avoid detection (the "zoo hypothesis" or "dark forest" scenario), the observation n = 0 does not constrain λ because the detection probability is zero regardless of λ. The survival framework cannot distinguish between "no civilizations exist in the surveyed volume" and "civilizations exist but are invisible." This is a fundamental observational limitation shared by all models, not specific to the survival framework.

(F3) *The observation window is too short.* With T_obs = 60 years and r₀ = 100 ly, the surveyed volume is a tiny fraction of the galaxy (f_sky ≈ 5 × 10⁻⁷). It is logically possible that communicating civilizations exist in abundance beyond the surveyed volume. The survival model handles this correctly — the confidence bound reflects the limited survey coverage — but the practical implication is that the late-filter conclusion is quantitatively strong only when the effective η in the surveyed volume is sufficiently large (Table 1).

### 4.4 Figures

Three figures are specified below with complete Python/matplotlib code. Each figure is self-contained and reproducible.

**Figure 1. Survival Function S(t) Under Exponential and Weibull Hazard Models.**

This figure plots S(t) for the exponential model (k = 1) and Weibull models with k = 0.5 (early filter / decreasing hazard) and k = 2.0 (late filter / increasing hazard), illustrating the qualitative difference in civilizational survival trajectories.

```python
# Figure 1: Survival function S(t) under exponential and Weibull hazard
# Reproducible: all parameters fixed, no randomness.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)  # Seed set for reproducibility; no randomness used in this figure.

t = np.linspace(0, 5, 1000)  # Time in units of scale parameter

# Exponential: S(t) = exp(-t), equivalent to Weibull with k=1, lambda_w=1
S_exp = np.exp(-t)

# Weibull k=0.5 (early filter / decreasing hazard): S(t) = exp(-t^0.5)
k_early = 0.5
S_early = np.exp(-(t ** k_early))

# Weibull k=2.0 (late filter / increasing hazard): S(t) = exp(-t^2)
k_late = 2.0
S_late = np.exp(-(t ** k_late))

fig, ax = plt.subplots(1, 1, figsize=(8, 5))

ax.plot(t, S_exp, 'k-', linewidth=2, label=r'Exponential ($k=1$, constant hazard)')
ax.plot(t, S_early, 'b--', linewidth=2, label=r'Weibull $k=0.5$ (decreasing hazard — early filter)')
ax.plot(t, S_late, 'r-.', linewidth=2, label=r'Weibull $k=2.0$ (increasing hazard — late filter)')

ax.set_xlabel(r'Time $t / \lambda_w$', fontsize=12)
ax.set_ylabel(r'Survival function $S(t)$', fontsize=12)
ax.set_title('Figure 1: Survival Function Under Different Hazard Models', fontsize=13)
ax.legend(fontsize=10, loc='upper right')
ax.set_xlim(0, 5)
ax.set_ylim(0, 1.05)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('fig1_survival_function.png', dpi=300, bbox_inches='tight')
plt.show()
```

*Caption.* Survival function S(t) = exp(−(t/λ_w)^k) for three hazard regimes. The exponential model (k = 1, black solid) has constant hazard. The Weibull model with k = 0.5 (blue dashed) has decreasing hazard — civilizations face high early risk but survivors become resilient (early filter). The Weibull model with k = 2.0 (red dash-dot) has increasing hazard — risk grows with age, consistent with a late filter acting on mature civilizations. Time is measured in units of the scale parameter λ_w.

**Figure 2. Log-Likelihood Function ℓ(λ) Given Zero Detections.**

This figure plots the log-likelihood ℓ(λ) = −η/λ for three values of the emergence rate η, demonstrating that ℓ is strictly increasing for all η > 0 (Lemma 1) and that the MLE is at the boundary λ → ∞.

```python
# Figure 2: Log-likelihood function l(lambda) given n=0 detections
# Reproducible: all parameters fixed, no randomness.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

lam = np.linspace(0.01, 10, 1000)  # Hazard rate lambda (arbitrary units)

# Three emergence rates (arbitrary units, illustrative)
eta_values = [0.1, 1.0, 10.0]
labels = [r'$\eta = 0.1$', r'$\eta = 1.0$', r'$\eta = 10.0$']
styles = ['b-', 'k-', 'r-']

fig, ax = plt.subplots(1, 1, figsize=(8, 5))

for eta, label, style in zip(eta_values, labels, styles):
    ell = -eta / lam  # Log-likelihood: l(lambda) = -eta/lambda
    ax.plot(lam, ell, style, linewidth=2, label=label)

ax.axhline(y=0, color='gray', linestyle=':', linewidth=1, alpha=0.5)
ax.annotate(r'$\ell(\lambda) \to 0$ as $\lambda \to \infty$ (MLE at boundary)',
            xy=(8, -0.15), fontsize=10, ha='center',
            arrowprops=dict(arrowstyle='->', color='black'),
            xytext=(6, -2))

ax.set_xlabel(r'Hazard rate $\lambda$', fontsize=12)
ax.set_ylabel(r'Log-likelihood $\ell(\lambda) = -\eta / \lambda$', fontsize=12)
ax.set_title('Figure 2: Log-Likelihood Given Zero Detections', fontsize=13)
ax.legend(fontsize=10, loc='lower right')
ax.set_xlim(0, 10)
ax.set_ylim(-12, 1)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('fig2_log_likelihood.png', dpi=300, bbox_inches='tight')
plt.show()
```

*Caption.* Log-likelihood ℓ(λ) = −η/λ as a function of the hazard rate λ for three emergence rates η. All curves are strictly increasing (Lemma 1): the likelihood improves monotonically as λ increases. The MLE is at the boundary λ̂ → ∞ for all η > 0 (Theorem 1). Higher emergence rates (larger η) produce steeper initial slopes, meaning the data are more informative — but the direction of the MLE (toward higher λ) is invariant. The horizontal asymptote at ℓ = 0 (L = 1) is approached but never reached.

**Figure 3. Filter Location Posterior: Early vs. Late Filter Probability.**

This figure plots the posterior probability that the filter is late (k > 1) versus early (k < 1) under a log-uniform prior on the Weibull shape parameter k. By Proposition 4, k is non-identifiable from n = 0 alone: the likelihood is flat in k (all values of k achieve the same supremum likelihood as λ_w → 0⁺). The posterior therefore mirrors the prior, demonstrating that the SETI silence constrains *how long* civilizations communicate (τ → 0) but not *how the hazard changes with age* (k). This figure is included per the frozen spec; the methodologically sharper result is that the MLE of τ is zero for all k (Theorem 3).

```python
# Figure 3: Filter location posterior (early vs. late filter probability)
# Demonstrates that k is non-identifiable from n=0 (Proposition 4).
# Reproducible: all parameters fixed, seed set.

import numpy as np
import matplotlib.pyplot as plt
from scipy import special

np.random.seed(42)

# --- Panel (a): Likelihood profile over k ---
# For any k > 0, the supremum likelihood over lambda_w is 1 (Theorem 3).
# At any fixed lambda_w > 0, the likelihood is L = exp(-eta * lambda_w * Gamma(1+1/k)).
# We plot likelihood contours at fixed lambda_w values to show the flatness in k.

k_range = np.linspace(0.2, 4.0, 500)
eta = 1e-10  # Illustrative emergence rate (arbitrary units)
lambda_w_values = [0.1, 1.0, 10.0]
lambda_w_labels = [r'$\lambda_w = 0.1$', r'$\lambda_w = 1.0$', r'$\lambda_w = 10.0$']
lambda_w_styles = ['b-', 'k-', 'r-']

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Panel (a): Likelihood slices at fixed lambda_w
ax = axes[0]
for lw, label, style in zip(lambda_w_values, lambda_w_labels, lambda_w_styles):
    gamma_vals = special.gamma(1 + 1/k_range)
    mu = eta * lw * gamma_vals
    L = np.exp(-mu)
    ax.plot(k_range, L, style, linewidth=2, label=label)

ax.axvline(x=1.0, color='gray', linestyle=':', linewidth=1, alpha=0.7,
           label=r'$k=1$ (exponential)')
ax.set_xlabel(r'Weibull shape parameter $k$', fontsize=12)
ax.set_ylabel(r'Likelihood $L(k, \lambda_w)$', fontsize=12)
ax.set_title('(a) Likelihood slices: flat in $k$ as $\lambda_w \\to 0$', fontsize=12)
ax.legend(fontsize=9, loc='lower right')
ax.set_xlim(0.2, 4.0)
ax.set_ylim(0, 1.05)
ax.grid(True, alpha=0.3)

# Panel (b): Posterior probability P(late filter | n=0) under log-uniform prior on k
# Prior: pi(k) proportional to 1/k on [k_min, k_max] (log-uniform)
# Likelihood: flat in k at the MLE boundary (Proposition 4)
# => Posterior = Prior (data are uninformative about k)

ax = axes[1]
k_min, k_max = 0.2, 5.0
k_grid = np.linspace(k_min, k_max, 1000)

# Log-uniform prior: pi(k) = 1 / (k * ln(k_max/k_min))
log_uniform_prior = 1.0 / (k_grid * np.log(k_max / k_min))

# Posterior = prior (since likelihood is flat in k at MLE boundary)
posterior = log_uniform_prior.copy()

# Shade early (k < 1) and late (k > 1)
mask_early = k_grid < 1.0
mask_late = k_grid > 1.0

ax.fill_between(k_grid[mask_early], posterior[mask_early], alpha=0.3, color='blue',
                label=r'Early filter ($k < 1$)')
ax.fill_between(k_grid[mask_late], posterior[mask_late], alpha=0.3, color='red',
                label=r'Late filter ($k > 1$)')
ax.plot(k_grid, posterior, 'k-', linewidth=2, label='Posterior = Prior (log-uniform)')
ax.axvline(x=1.0, color='gray', linestyle='--', linewidth=1.5,
           label=r'$k=1$ (exponential)')

# Compute and annotate probabilities
P_early = np.trapz(posterior[mask_early], k_grid[mask_early])
P_late = np.trapz(posterior[mask_late], k_grid[mask_late])
ax.annotate(f'P(early) = {P_early:.2f}', xy=(0.5, 0.6), fontsize=11, color='blue',
            xycoords='axes fraction')
ax.annotate(f'P(late) = {P_late:.2f}', xy=(0.5, 0.5), fontsize=11, color='red',
            xycoords='axes fraction')

ax.set_xlabel(r'Weibull shape parameter $k$', fontsize=12)
ax.set_ylabel(r'Posterior density $\pi(k \mid n=0)$', fontsize=12)
ax.set_title('(b) Posterior over filter location: prior-dominated', fontsize=12)
ax.legend(fontsize=9, loc='upper right')
ax.set_xlim(k_min, k_max)
ax.grid(True, alpha=0.3)

plt.suptitle('Figure 3: Filter Location Posterior Under Log-Uniform Prior on $k$',
             fontsize=13, y=1.02)
plt.tight_layout()
plt.savefig('fig3_filter_location_posterior.png', dpi=300, bbox_inches='tight')
plt.show()
```

*Caption.* Filter location posterior under a log-uniform prior on the Weibull shape parameter k. (a) Likelihood slices L(k, λ_w) at three fixed scale parameters. As λ_w → 0 (the MLE boundary, Theorem 3), all slices approach L = 1 uniformly in k, confirming that k is non-identifiable from n = 0 (Proposition 4). (b) Posterior density π(k | n = 0) under a log-uniform prior on k ∈ [0.2, 5.0]. Because the likelihood is flat in k, the posterior equals the prior. The data cannot distinguish early filter (k < 1, blue) from late filter (k > 1, red). The critical result is not the posterior over k but the MLE of τ → 0, which holds for all k > 0 (Theorem 3): regardless of whether the hazard increases or decreases with age, the data favor the shortest possible communicative lifetime.

**Figure 4. Confidence Bound on Mean Communicative Lifetime as a Function of Emergence Rate.**

This supplementary figure plots the 95% upper confidence bound τ₀.₀₅ as a function of the local emergence rate η, showing the parameter regimes in which the late-filter conclusion is quantitatively strong versus weak.

```python
# Figure 4: Confidence bound on mean communicative lifetime vs. emergence rate
# Reproducible: all parameters fixed, no randomness.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

T_gal = 13.6e9  # Galaxy age in years
alpha = 0.05     # 95% confidence level
V_gal = 8.0e12   # Galactic disk volume in ly^3 (approx)

# Detection radii
r0_values = [100, 1000, 10000]  # ly
colors = ['blue', 'black', 'red']
labels = [r'$r_0 = 100$ ly', r'$r_0 = 1{,}000$ ly', r'$r_0 = 10{,}000$ ly']

# Galactic emergence rate range
eta_gal = np.logspace(-10, -3, 1000)  # yr^-1

fig, ax = plt.subplots(1, 1, figsize=(8, 5))

for r0, color, label in zip(r0_values, colors, labels):
    V0 = (4/3) * np.pi * r0**3
    f_sky = V0 / V_gal
    eta = eta_gal * f_sky
    tau_bound = -np.log(alpha) / eta  # 95% upper confidence bound

    ax.loglog(eta_gal, tau_bound, color=color, linewidth=2, label=label)

# Reference line: galaxy age
ax.axhline(y=T_gal, color='gray', linestyle='--', linewidth=1.5,
           label=r'$T_{\mathrm{gal}} = 13.6$ Gyr')

ax.fill_between(eta_gal, 1, T_gal, alpha=0.08, color='red',
                label=r'$\tau_{0.05} < T_{\mathrm{gal}}$ (late filter supported)')

ax.set_xlabel(r'Galactic emergence rate $\eta_{\mathrm{gal}}$ (yr$^{-1}$)', fontsize=12)
ax.set_ylabel(r'95% upper bound on $\tau$ (years)', fontsize=12)
ax.set_title('Figure 4: Confidence Bound on Communicative Lifetime', fontsize=13)
ax.legend(fontsize=9, loc='upper right')
ax.set_xlim(1e-10, 1e-3)
ax.set_ylim(1e2, 1e20)
ax.grid(True, alpha=0.3, which='both')

plt.tight_layout()
plt.savefig('fig4_confidence_bound.png', dpi=300, bbox_inches='tight')
plt.show()
```

*Caption.* The 95% upper confidence bound τ₀.₀₅ = −ln(0.05)/η on the mean communicative lifetime, plotted as a function of the galactic emergence rate η_gal for three SETI detection radii r₀. The horizontal dashed line marks the galaxy age T_gal = 13.6 Gyr. When a curve falls below this line (shaded region), the observation n = 0 constrains τ to be less than the galaxy age at the 95% confidence level, providing quantitative support for the late-filter conclusion. Larger detection radii and higher emergence rates strengthen the constraint. At the current SETI baseline (r₀ ≈ 100 ly), quantitative support requires η_gal > 10⁻⁴ yr⁻¹. The qualitative MLE result (λ̂ = +∞) holds everywhere on this plot.

### Symbol Table (additions to Sections 1–3)

| Symbol | Definition | Introduced |
|--------|-----------|------------|
| τ_α | (1−α) upper confidence bound on τ | §4.1 (from Prop. 3) |
| f_sky(r₀) | Fraction of galaxy surveyed, function of r₀ | §4.1 |
| V_gal | Galactic disk volume, ≈ 8.0 × 10¹² ly³ | §4.1 |

---

## 5. Related Work

The Fermi paradox has generated a large and heterogeneous literature spanning astrophysics, philosophy, and probability theory. This section places the survival function framework in relation to the principal prior contributions, organized by the formal property each contribution provides or lacks.

### 5.1 The Drake Equation and Its Extensions

Drake (1961) proposed the multiplicative chain N = R★ · f_p · n_e · f_l · f_i · f_c · L as a framework for estimating the number of detectable civilizations. The equation has been enormously influential as an organizing device, but it is not an inferential framework: it provides no method for updating estimates in light of observational data, and in particular cannot incorporate the censored observation n = 0 (see Section 2.1 for the formal critique). Subsequent extensions to the Drake equation — including probabilistic treatments that assign distributions to each factor (Maccone 2010), Monte Carlo analyses that propagate uncertainty through the product (Sandberg, Drexler, & Ord 2018), and Bayesian reformulations that condition on auxiliary data (Spiegel & Turner 2012) — inherit the structural limitation: the multiplicative form conflates the emergence rate and the civilizational lifetime into a single product, precluding the separation that the survival framework achieves (Theorem 2, Step 1). The survival framework subsumes the Drake equation as a special case (Corollary 1) while providing the inferential structure it lacks.

### 5.2 Hart's Fact A and the Rare Earth Tradition

Hart (1975) argued that the absence of extraterrestrial visitors on Earth ("Fact A") implies that intelligent life is rare — that a strong early filter prevents civilizations from arising. This argument initiated the tradition that treats the silence as evidence for an early filter, culminating in the Rare Earth hypothesis (Ward & Brownlee 2000), which attributes the filter to the improbability of complex life. The survival framework shows that Hart's conclusion, while not excluded, is not the maximum likelihood explanation: for any positive emergence rate, the data favor a late filter over an early one (Section 4.2, Model 2). Hart assumed the filter location; the survival framework derives it.

### 5.3 Brin's Survey and the Classification Problem

Brin (1983) provided the first comprehensive survey of proposed solutions to the Fermi paradox, organizing them into categories: civilizations are rare, civilizations are short-lived, civilizations choose not to communicate, and so on. Brin's contribution was taxonomic: identifying the space of possible explanations and mapping their relationships. What Brin's survey — and subsequent surveys including Webb (2002) and Ćirković (2009) — could not provide was a formal criterion for discriminating among the categories. The survival framework provides such a criterion: the likelihood function L(θ) = exp(−μ(θ)) (Proposition 2) assigns each parameter configuration a probability of producing the observed silence, enabling formal comparison. Brin's category "civilizations are short-lived" corresponds to the late-filter hypothesis (large λ), which the survival framework identifies as the maximum likelihood explanation.

### 5.4 Hanson's Great Filter

Hanson (1998) introduced the Great Filter concept: at least one step in the sequence from inert matter to galaxy-spanning civilization must have extremely low probability, explaining why the galaxy appears empty. Hanson framed the central question as whether the filter lies in our past (we have already passed it) or our future (we have not). The Great Filter framework is the closest precursor to the survival function approach in that it explicitly addresses filter location, but it treats the answer as a matter for prior belief and auxiliary evidence rather than as a quantity derivable from the SETI observation itself. The survival framework resolves Hanson's question by deriving the filter location from the likelihood (Theorem 2): the MLE of the post-emergence hazard rate is at +∞, identifying a late filter as the maximum likelihood explanation. The relationship is complementary: Hanson named the problem; the survival framework solves it.

### 5.5 Ćirković's Taxonomy

Ćirković (2018) provided the most complete modern taxonomy of Fermi paradox solutions, organizing proposals by mechanism type and identifying cross-cutting themes. The taxonomy is descriptive rather than inferential: it identifies what solutions exist but does not rank them by consistency with observation. The survival framework provides the inferential complement to Ćirković's taxonomy by assigning each mechanistic hypothesis a likelihood given the censored observation (Section 4.2).

### 5.6 Survival Analysis in Adjacent Fields

The survival function formalism adopted in this paper originates in actuarial science and medical statistics, formalized by Cox (1972) and codified in standard references (Kalbfleisch & Prentice 2002; Klein & Moeschberger 2003). The application of survival analysis to the Fermi paradox is, to our knowledge, novel. Related quantitative approaches to civilizational longevity include the Doomsday argument (Gott 1993; Leslie 1996), which uses the Copernican principle to bound the expected future duration of humanity, and the probabilistic dissolution model of Ćirković & Vukotić (2008), which models the rate of civilizational collapse as a function of galactic age. The survival framework differs from these approaches in that it conditions directly on the SETI observation n = 0 as a censored datum, rather than on anthropic or cosmological priors.

### 5.7 Recent Quantitative SETI Frameworks

Sandberg, Drexler, & Ord (2018) performed a Monte Carlo dissolution of the Drake equation, showing that realistic uncertainty in the parameters yields a substantial probability of being alone in the observable universe. Their analysis demonstrates the sensitivity of the Drake framework to parameter uncertainty but inherits the framework's structural limitations. Grimaldi (2017) modeled the probability of detecting an electromagnetic signal as a geometric covering problem, providing constraints on signal duration and beaming fraction. Wandel (2015) analyzed the implications of Kepler exoplanet statistics for the Drake equation's planet-related factors. These contributions are complementary to the present work: they refine the inputs (emergence rate, detection probability) that the survival framework takes as parameters η and f_sky.

---

## 6. Discussion

### 6.1 Summary of Results

This paper has introduced a survival function framework for analyzing the Fermi paradox. The framework treats the sixty-year SETI silence as a right-censored observation and constructs the exact likelihood for the hazard rate governing civilizational communicative lifetimes. The principal results are:

1. Under the exponential hazard model, the maximum likelihood estimate of the hazard rate is λ̂ = +∞ for any positive emergence rate η > 0, corresponding to a mean communicative lifetime of τ̂ = 0 (Theorem 1).

2. The maximum likelihood explanation for the silence is a late-stage filter acting on civilizations after they enter the communicating state, not a deficit in civilizational emergence (Theorem 2). This result holds for any η > 0 and is invariant to the choice of parametric hazard model (Proposition 5).

3. The Weibull shape parameter k, which encodes whether the hazard increases or decreases with civilizational age, is non-identifiable from zero detections alone (Proposition 4). The data constrain how long civilizations communicate (τ → 0) but not how the hazard changes over time.

4. The quantitative strength of the conclusion depends on the emergence rate η and the SETI detection radius r₀ (Table 1), but the qualitative direction — late filter, not early — is invariant across five orders of magnitude in both parameters.

### 6.2 What Would Update the Model

The survival framework is designed to be updated by future observations. Three classes of data would materially change the inference:

**A single confirmed detection.** Even one confirmed detection (n = 1) would transform the inference. The MLE would shift from the boundary to an interior point, the Weibull shape parameter k would become identifiable if the detected civilization's age could be estimated, and the likelihood surface would acquire a finite maximum. The present paper's result — MLE at the boundary — is a direct consequence of n = 0. A detection changes everything.

**Expanded SETI coverage.** The confidence bound τ_α scales inversely with the effective emergence rate η = η_gal · f_sky (Proposition 3). Increasing the detection radius r₀ or surveying a larger fraction of the sky tightens the bound. The transition from r₀ = 100 ly to r₀ = 1,000 ly increases f_sky by a factor of 10³, moving several parameter combinations from "indeterminate" to "late filter supported" in Table 1. The Square Kilometre Array and next-generation optical SETI programs will substantially increase f_sky over the coming decades.

**Resolved emergence rate estimates.** The confidence bound depends on η, which in turn depends on the galactic emergence rate η_gal. Independent constraints on η_gal — from astrobiology (the frequency of habitable planets and the probability of abiogenesis) or from paleontological evidence (the timescale of major evolutionary transitions on Earth) — would tighten the bound. The MLE direction is independent of η (Theorem 1), but the quantitative strength of the conclusion is not.

### 6.3 Limitations

**The existence assumption (η > 0).** The entire analysis conditions on at least one civilization having emerged somewhere in the galaxy over its history. If η = 0 — if civilizational emergence is genuinely impossible — the paradox dissolves and no filter is needed (Proposition 6). The survival framework cannot distinguish between "no civilizations have emerged" and "civilizations have emerged but none are currently detectable." This is a fundamental limitation shared by all frameworks that treat the silence as informative.

**Independence of civilizations.** The Poisson model assumes that civilizations emerge and cease independently. If civilizations are causally linked — for example, if a single catastrophic event could destroy all civilizations in a galactic region simultaneously, or if one civilization's expansion suppresses others — the independence assumption fails (Section 4.3, condition B2). Correlated cessation events would make n = 0 more probable than the Poisson model predicts, weakening the constraint on λ. Extension to correlated emergence models is deferred to future work.

**Detectability assumptions.** The model assumes that a Kardashev Type I civilization within the detection radius r₀ would be detected with certainty. In practice, detection probability depends on beaming fraction, frequency selection, signal intermittency, and the orientation of the transmitter relative to Earth. A detection probability significantly less than 1 reduces the effective surveyed volume, loosening the confidence bound. The MLE direction is preserved (Theorem 1 is invariant to η), but the quantitative constraint weakens.

**The communicating state is coarsely defined.** The model treats "communicating" as a binary state. A civilization that transitions from electromagnetic broadcasting to a communication technology that SETI cannot detect would exit the "communicating" state as defined here without going extinct. The hazard function thus measures the rate of transition below the detectability threshold, not the rate of extinction per se (Section 4.3, condition B5). The late-filter conclusion refers to a filter against continued detectability, which may include technological transcendence as well as destruction.

**Model scope.** The survival framework addresses one question: given zero detections, what does the hazard rate imply about filter location? It does not identify the mechanism of the filter. The model is agnostic about whether the post-emergence hazard arises from self-destruction, resource depletion, voluntary withdrawal from communication, or any other cause. Identifying the mechanism requires data beyond n = 0.

### 6.4 Open Problems

1. **Identifying the Weibull shape parameter.** The non-identifiability of k from n = 0 alone (Proposition 4) is a scope boundary of the present analysis. A detection with an estimated civilizational age would make k identifiable. Characterizing the minimum data requirements for shape parameter estimation — how many detections, with what age precision — is a natural extension.

2. **Correlated emergence models.** The Poisson emergence assumption (Proposition 1) excludes panspermia-driven correlated emergence and galactic-scale extinction events. Extending the framework to point processes with dependence structure (e.g., Hawkes processes for self-exciting emergence, or Cox processes for environmentally modulated emergence) would expand the model's scope.

3. **Multi-filter models.** The present framework models a single aggregate hazard rate. In reality, multiple hazards may operate at different civilizational stages. A competing-risks survival model, in which each hazard has its own rate function, could decompose the aggregate hazard into stage-specific components. This requires data on civilizational ages at cessation, which n = 0 does not provide.

4. **Integration with technosignature surveys.** The survival framework conditions on n = 0 confirmed detections of communicating civilizations. Ongoing and planned technosignature surveys will either maintain n = 0 with expanded f_sky — tightening the confidence bound — or produce n ≥ 1, transforming the inference entirely. Formalizing the integration of the survival framework with specific survey parameters (frequency coverage, sensitivity, sky fraction) is a practical next step.

---

## 7. Conclusion

The Fermi paradox has been treated, for sixty years, as a puzzle of missing parameters: if we could only estimate the probability of life, of intelligence, of technology, the silence would be explained. This paper argues that the puzzle is not one of missing parameters but of missing formalism. The Drake equation cannot analyze the silence because it was not designed to analyze censored data. The survival function framework is.

The central result is this: under the survival function framework, with the minimal assumption that at least one communicating civilization has emerged somewhere in the galaxy (η > 0), the maximum likelihood estimate of the post-emergence hazard rate is λ̂ = +∞. The data — sixty years of silence across the surveyed volume — are maximally consistent with a late-stage filter that drives communicating civilizations to cessation. This is not a speculation about what the filter might be. It is a derivation of where the filter must act, given what we have observed.

The result is robust. It holds under the exponential hazard model and the Weibull extension. It holds for any positive emergence rate. It holds across five orders of magnitude in the galactic emergence rate and three orders of magnitude in the SETI detection radius. The qualitative direction — late filter, not early — is invariant. Only the quantitative strength of the conclusion varies with parameters, and it strengthens as SETI coverage expands.

The result is also limited. It requires the existence assumption (η > 0). It assumes independent civilizations. It cannot identify the mechanism of the late filter or the age-dependence of the hazard (the Weibull shape parameter k). These limitations are stated as boundary conditions (Section 4.3) and open problems (Section 6.4), not as qualifications that weaken the central claim.

What the paper claims: under minimal assumptions, the silence implies a late filter. What the paper does not claim: that the filter is extinction, that civilizations are doomed, or that the mechanism is knowable from current data. The survival function framework provides a sharp answer to the question of where the filter acts. The question of what the filter is remains open.

---

## References

Bland-Hawthorn, J. & Gerhard, O. (2016). The Galaxy in context: structural, kinematic, and integrated properties. *Annual Review of Astronomy and Astrophysics*, 54, 529–596.

Brin, G. D. (1983). The "Great Silence": the controversy concerning extraterrestrial intelligent life. *Quarterly Journal of the Royal Astronomical Society*, 24, 283–309.

Ćirković, M. M. (2009). Fermi's paradox — the last challenge for Copernicanism? *Serbian Astronomical Journal*, 178, 1–20.

Ćirković, M. M. (2018). *The Great Silence: Science and Philosophy of Fermi's Paradox*. Oxford University Press.

Ćirković, M. M. & Vukotić, B. (2008). Astrobiological landscape: a platform for the neo-Copernican synthesis? *International Journal of Astrobiology*, 7(1), 1–13.

Cox, D. R. (1972). Regression models and life-tables. *Journal of the Royal Statistical Society, Series B*, 34(2), 187–220.

Drake, F. D. (1961). Discussion at Space Science Board – National Academy of Sciences Conference on Extraterrestrial Intelligent Life, Green Bank, WV.

Enriquez, J. E., Siemion, A., Foster, G., Gajjar, V., Hellbourg, G., Hickish, J., Isaacson, H., Price, D. C., Croft, S., DeBoer, D., Lebofsky, M., MacMahon, D. H. E., & Werthimer, D. (2017). The Breakthrough Listen search for intelligent life: 1.1–1.9 GHz observations of 692 nearby stars. *The Astrophysical Journal*, 849, 104.

Gott, J. R. III (1993). Implications of the Copernican principle for our future prospects. *Nature*, 363, 315–319.

Grimaldi, C. (2017). Signal coverage approach to the detection probability of hypothetical extraterrestrial emitters in the Milky Way. *Scientific Reports*, 7, 46273.

Hanson, R. (1998). The Great Filter — are we almost past it? Available at: http://mason.gmu.edu/~rhanson/greatfilter.html.

Hart, M. H. (1975). Explanation for the absence of extraterrestrials on Earth. *Quarterly Journal of the Royal Astronomical Society*, 16, 128–135.

Kalbfleisch, J. D. & Prentice, R. L. (2002). *The Statistical Analysis of Failure Time Data*, 2nd ed. Wiley.

Klein, J. P. & Moeschberger, M. L. (2003). *Survival Analysis: Techniques for Censored and Truncated Data*, 2nd ed. Springer.

Leslie, J. (1996). *The End of the World: The Science and Ethics of Human Extinction*. Routledge.

Maccone, C. (2010). The statistical Drake equation. *Acta Astronautica*, 67(11–12), 1366–1383.

Planck Collaboration (2020). Planck 2018 results. VI. Cosmological parameters. *Astronomy & Astrophysics*, 641, A6.

Sandberg, A., Drexler, E., & Ord, T. (2018). Dissolving the Fermi paradox. *arXiv preprint arXiv:1806.02404*.

Spiegel, D. S. & Turner, E. L. (2012). Bayesian analysis of the astrobiological implications of life's early emergence on Earth. *Proceedings of the National Academy of Sciences*, 109(2), 395–400.

Takács, L. (1962). *Introduction to the Theory of Queues*. Oxford University Press.

Tarter, J. (2001). The search for extraterrestrial intelligence (SETI). *Annual Review of Astronomy and Astrophysics*, 39, 511–548.

Wandel, A. (2015). On the abundance of extraterrestrial life after the Kepler mission. *International Journal of Astrobiology*, 14(4), 511–516.

Ward, P. D. & Brownlee, D. (2000). *Rare Earth: Why Complex Life Is Uncommon in the Universe*. Copernicus Books.

Webb, S. (2002). *If the Universe Is Teeming with Aliens ... Where Is Everybody? Fifty Solutions to the Fermi Paradox and the Problem of Extraterrestrial Life*. Copernicus Books.
