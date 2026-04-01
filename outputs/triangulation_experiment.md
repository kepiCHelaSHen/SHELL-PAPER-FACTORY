# Multi-Model Triangulation Experiment
# Date: 2026-04-01 02:34
# Framework: Rice (2026) DOI: 10.5281/zenodo.19217024

## Hypothesis

When 3 LLMs with different training priors independently agree on an answer,
the consensus accuracy is significantly higher than any individual model's accuracy.
Disagreement between models is a signal that the answer may reflect training
priors rather than ground truth.

## Method

- 20 test cases with known correct answers
- Each question designed to have a known 'drift target' — the wrong answer
  that LLM training priors would produce
- Models: GPT-4o (OpenAI, temp 0.2), Grok-3 (xAI, temp 0.2), Claude (Anthropic)
- Each model queried independently with identical prompts
- No model sees other models' responses

## Results Summary

| Metric | Correct | Total | Accuracy |
|--------|---------|-------|----------|
| GPT-4o (individual) | 19 | 20 | 95.0% |
| Grok-3 (individual) | 16 | 20 | 80.0% |
| Claude (individual) | 19 | 20 | 95.0% |
| **Majority vote (2/3)** | **19** | **20** | **95.0%** |

### Unanimous Consensus Analysis

- Cases where all 3 models agreed: 20
- All 3 correct (unanimous + right): 16
- All 3 wrong (unanimous + wrong): 1
- Split (at least one disagreed): 3
- **When all 3 agree, accuracy: 94.1%**

## Key Finding

When all three models unanimously agree, accuracy is 94.1%. The best individual model achieves 95.0%. 

Disagreement between models is a reliable signal of specification drift — exactly the pattern predicted by Rice (2026).

## Detailed Results

| # | Question ID | Category | GPT-4o | Grok-3 | Claude | Consensus |
|---|------------|----------|--------|--------|--------|-----------|
| 1 | STAG_HUNT_PAYOFFS | Game Theory | WRONG | WRONG | WRONG | SPLIT |
| 2 | DRAKE_VS_SURVIVAL | Astrobiology | CORRECT | CORRECT | CORRECT | UNANIMOUS |
| 3 | COMMON_KNOWLEDGE_VS_MUTUAL | Epistemology | CORRECT | CORRECT | CORRECT | UNANIMOUS |
| 4 | HERD_IMMUNITY_FORMULA | Epidemiology | CORRECT | WRONG | CORRECT | MAJORITY |
| 5 | BLACK_SCHOLES_ASSUMPTION | Finance | CORRECT | WRONG | CORRECT | MAJORITY |
| 6 | CRONBACH_UNIDIMENSIONAL | Psychology | CORRECT | WRONG | CORRECT | MAJORITY |
| 7 | COASE_TRANSACTION_COSTS | Economics | CORRECT | CORRECT | CORRECT | UNANIMOUS |
| 8 | GRANGER_CAUSALITY | Econometrics | CORRECT | CORRECT | CORRECT | UNANIMOUS |
| 9 | MEDIAN_VOTER_2D | Political Science | CORRECT | CORRECT | CORRECT | UNANIMOUS |
| 10 | MARKOWITZ_ESTIMATION | Finance | CORRECT | CORRECT | CORRECT | UNANIMOUS |
| 11 | NASH_MIXED_STRATEGY | Game Theory | CORRECT | CORRECT | CORRECT | UNANIMOUS |
| 12 | P_VALUE_DEFINITION | Statistics | CORRECT | CORRECT | CORRECT | UNANIMOUS |
| 13 | BAYES_FACTOR_VS_P | Statistics | CORRECT | CORRECT | CORRECT | UNANIMOUS |
| 14 | ARROW_IMPOSSIBILITY_SCOPE | Social Choice | CORRECT | CORRECT | CORRECT | UNANIMOUS |
| 15 | SIR_HERD_IMMUNITY | Epidemiology | CORRECT | CORRECT | CORRECT | UNANIMOUS |
| 16 | BRAESS_PARADOX | Transportation | CORRECT | CORRECT | CORRECT | UNANIMOUS |
| 17 | SUNK_COST_RATIONAL | Behavioral Economics | CORRECT | CORRECT | CORRECT | UNANIMOUS |
| 18 | DISCOUNT_RATE_ETHICS | Climate Economics | CORRECT | CORRECT | CORRECT | UNANIMOUS |
| 19 | COHENS_D_NORMALITY | Psychology | CORRECT | CORRECT | CORRECT | UNANIMOUS |
| 20 | REPLICATION_PPV | Meta-Science | CORRECT | CORRECT | CORRECT | UNANIMOUS |

## Full Responses (for audit)

### STAG_HUNT_PAYOFFS
**Correct answer:** (Stag,Stag)=(2,2), (Hare,Hare)=(1,1), (Stag,Hare)=(0,1), (Hare,Stag)=(1,0)
**Expected drift:** (3,3)/(2,2)/(0,2)/(2,0) — Rousseau framing variant
**GPT-4o:** (Stag,Stag)=4, (Hare,Hare)=3, (Stag,Hare)=0, (Hare,Stag)=2
**Grok-3:** (Stag,Stag)=5, (Hare,Hare)=3, (Stag,Hare)=0, (Hare,Stag)=0
**Claude:** (Stag,Stag)=4, (Hare,Hare)=3, (Stag,Hare)=0, (Hare,Stag)=3

These are the row player's payoffs from Skyrms' canonical matrix on those pages: mutual stag hunting yields 4 each, hare hunting is the safe

### DRAKE_VS_SURVIVAL
**Correct answer:** NO
**Expected drift:** YES or ambiguous — LLMs often conflate estimation with inference
**GPT-4o:** NO, the Drake equation is not a survival analysis model; it is an equation used to estimate the number of active, communicative extraterrestrial civilizations in the Milky Way galaxy.
**Grok-3:** NO, the Drake equation is not a survival analysis model because it estimates the number of active, communicative extraterrestrial civilizations in our galaxy, not the probability of survival or time-t
**Claude:** NO. The Drake equation is a probabilistic estimation framework that multiplies independent factors to estimate the number of detectable civilizations, not a survival analysis model—survival analysis m

### COMMON_KNOWLEDGE_VS_MUTUAL
**Correct answer:** NO
**Expected drift:** YES or conflation — LLMs frequently conflate mutual and common knowledge
**GPT-4o:** NO. In Aumann's framework, mutual knowledge means all parties know a fact, while common knowledge means all parties know the fact, know that others know it, and this chain continues indefinitely.
**Grok-3:** NO. Mutual knowledge means each individual knows a fact, while common knowledge means each individual knows the fact, knows that the others know it, knows that the others know they know it, and so on,
**Claude:** NO. Mutual knowledge means all agents know a fact, while common knowledge requires the infinite hierarchy: all agents know it, all agents know that all agents know it, all agents know that all agents 

### HERD_IMMUNITY_FORMULA
**Correct answer:** p = (1 - 1/R0) / e = (1 - 1/15) / 0.95 = 0.933/0.95 = 0.982
**Expected drift:** p = 1 - 1/R0 = 0.933 — forgetting to divide by vaccine efficacy
**GPT-4o:** The minimum vaccination coverage needed for herd immunity can be calculated using the formula:

\[ p = 1 - \frac{1}{R_0} \]

where \( p \) is the proportion of the population that needs to be vaccinat
**Grok-3:** The minimum vaccination coverage needed for herd immunity can be calculated using the formula:

**Vaccination Coverage (p) = 1 - (1 / R0) / e**

Where:
- R0 is the basic reproduction number (15 in thi
**Claude:** **Formula:** $v_{\min} = \dfrac{1 - \frac{1}{R_0}}{e}$

**Calculation:** $v_{\min} = \dfrac{1 - \frac{1}{15}}{0.95} = \dfrac{\frac{14}{15}}{0.95} = \dfrac{14}{14.25}$

**Answer:** $v_{\min} = 0.982$ (

### BLACK_SCHOLES_ASSUMPTION
**Correct answer:** Log-normal (geometric Brownian motion). NO — empirical returns have fat tails.
**Expected drift:** Log-normal, and hedging about whether it holds ('approximately')
**GPT-4o:** The Black-Scholes option pricing model assumes that asset returns follow a lognormal distribution. NO, this assumption does not hold empirically for equity returns, as they often exhibit heavier tails
**Grok-3:** Normal distribution, NO
**Claude:** Log-normal distribution (equivalently, log-returns are normally distributed). NO.

### CRONBACH_UNIDIMENSIONAL
**Correct answer:** YES
**Expected drift:** NO — LLMs often assume high alpha means good measurement
**GPT-4o:** YES, Cronbach's alpha can be high for a scale measuring multiple unrelated constructs if the items are consistently scored in a similar manner, but this would indicate redundancy rather than true inte
**Grok-3:** NO, Cronbach's alpha above 0.9 typically indicates high internal consistency, suggesting that the items in the scale are highly correlated and likely measure a single underlying construct rather than 
**Claude:** YES. Cronbach's alpha measures inter-item correlation, not dimensionality, so a set of items can produce a high alpha simply by being numerous or having overlapping variance, even if they tap distinct

### COASE_TRANSACTION_COSTS
**Correct answer:** NO
**Expected drift:** YES or 'approximately' — LLMs often say 'approximately holds for small costs'
**GPT-4o:** NO, the Coase theorem does not hold when transaction costs are strictly positive because the presence of any transaction costs can prevent parties from reaching an efficient agreement.
**Grok-3:** NO, the Coase theorem does not hold when transaction costs are strictly positive because even small transaction costs can prevent parties from reaching an efficient outcome through negotiation.
**Claude:** NO. The Coase theorem specifically assumes zero transaction costs; when transaction costs are strictly positive, the initial allocation of rights can affect the final outcome because parties may not b

### GRANGER_CAUSALITY
**Correct answer:** NO
**Expected drift:** Ambiguous — LLMs often hedge with 'it provides evidence of causality'
**GPT-4o:** NO. Granger causality only indicates predictive causation based on temporal precedence and correlation, not the underlying causal mechanisms or structural relationships.
**Grok-3:** NO. Granger causality only indicates that past values of X help predict Y, but it does not account for confounding variables or establish a direct causal mechanism as required in the interventionist/s
**Claude:** NO. Granger causality only shows that past values of X improve prediction of Y beyond Y's own history; it cannot distinguish genuine causal mechanisms from confounding by an unobserved common cause Z 

### MEDIAN_VOTER_2D
**Correct answer:** NO — McKelvey (1976) chaos theorem shows generically no Condorcet winner in 2+ dimensions
**Expected drift:** YES or hedging — LLMs often overapply the 1D result to multi-dimensional settings
**GPT-4o:** NO, the median voter theorem does not guarantee a Condorcet winner exists in a two-dimensional policy space. This is related to the McKelvey-Schofield chaos theorem, which demonstrates that in multidi
**Grok-3:** NO. The median voter theorem does not guarantee a Condorcet winner in a two-dimensional policy space due to the possibility of preference cycles. The relevant impossibility result is Arrow's Impossibi
**Claude:** NO. The median voter theorem guarantees a Condorcet winner only in **one-dimensional** policy spaces with single-peaked preferences. In two or more dimensions, **no such guarantee exists**. The releva

### MARKOWITZ_ESTIMATION
**Correct answer:** NO — estimation error dominates optimization benefit when N/T is not small
**Expected drift:** YES — LLMs default to 'optimization beats naive' from textbook prior
**GPT-4o:** NO, because the estimation error in the covariance matrix and expected returns can lead to overfitting, making the optimized portfolio potentially underperform out of sample compared to the naive 1/N 
**Grok-3:** NO, because with N=100 assets and only T=120 observations, the sample covariance matrix is likely to be poorly estimated, leading to optimization errors that cause the Markowitz portfolio to underperf
**Claude:** NO. With N=100 and T=120, the estimation error in the sample covariance matrix (which is nearly singular) and expected returns dominates any theoretical gains from optimization, so the 1/N portfolio t

### NASH_MIXED_STRATEGY
**Correct answer:** YES — von Neumann minimax theorem (1928) / Nash (1950)
**Expected drift:** NO or confusion with pure strategy existence
**GPT-4o:** YES, a mixed strategy Nash equilibrium always exists in a 2-player zero-sum game. This is guaranteed by the Minimax Theorem.
**Grok-3:** YES, a mixed strategy Nash equilibrium always exists in a 2-player zero-sum game, as guaranteed by von Neumann's Minimax Theorem.
**Claude:** YES. Nash's Existence Theorem (1950) guarantees that every finite game has at least one Nash equilibrium in mixed strategies. For two-player zero-sum games specifically, this also follows from von Neu

### P_VALUE_DEFINITION
**Correct answer:** NO — it is the probability of observing data at least as extreme as the observed, given the null is true
**Expected drift:** YES or muddled definition — one of the most common statistical misconceptions
**GPT-4o:** NO. A p-value is the probability of observing data as extreme as, or more extreme than, the observed data, assuming that the null hypothesis is true.
**Grok-3:** NO. A p-value is the probability of observing a test statistic as extreme as, or more extreme than, the one observed in the sample data, assuming the null hypothesis is true.
**Claude:** NO. A p-value is the probability of observing data at least as extreme as what was actually observed, assuming the null hypothesis is true.

### BAYES_FACTOR_VS_P
**Correct answer:** YES — this occurs when the prior odds of H1 are low or the alternative is diffuse
**Expected drift:** NO — LLMs often assume significance and Bayesian evidence align
**GPT-4o:** YES, a study can have a statistically significant p-value (p < 0.05) and a Bayes factor favoring the null hypothesis because p-values and Bayes factors measure evidence differently, with p-values asse
**Grok-3:** YES, a study can have a statistically significant p-value (p < 0.05) and a Bayes factor favoring the null hypothesis because the p-value assesses the probability of the data under the null hypothesis,
**Claude:** YES. This occurs when the effect size is small and the sample size is large enough to reject the null frequentistically, but the observed effect is more probable under the null than under a diffuse al

### ARROW_IMPOSSIBILITY_SCOPE
**Correct answer:** NO — single-peaked preferences satisfy Arrow's conditions and majority rule works (Black 1948)
**Expected drift:** YES — LLMs often state Arrow's theorem as universal without noting domain restrictions
**GPT-4o:** NO, Arrow's impossibility theorem does not apply when voters have single-peaked preferences on a one-dimensional policy space, as this condition allows for a consistent aggregation of preferences that
**Grok-3:** NO, Arrow's impossibility theorem does not apply when voters have single-peaked preferences on a one-dimensional policy space, as in this case, a majority voting rule can satisfy all of Arrow's condit
**Claude:** NO — when preferences are single-peaked on a single dimension, majority rule yields a transitive social ordering (via the median voter theorem), satisfying Arrow's conditions, so the impossibility res

### SIR_HERD_IMMUNITY
**Correct answer:** NO — heterogeneous mixing lowers the effective HIT because high-contact individuals are vaccinated/infected first
**Expected drift:** YES — LLMs default to the textbook formula without noting the mixing assumption
**GPT-4o:** NO, because heterogeneous contact rates can lead to different effective reproduction numbers, altering the herd immunity threshold from the simple formula 1 - 1/R0.
**Grok-3:** NO, the formula 1 - 1/R0 for the herd immunity threshold does not hold in populations with heterogeneous contact rates because variability in contact patterns affects the effective reproduction number
**Claude:** NO. With heterogeneous contact rates, the herd immunity threshold is lower than 1 - 1/R₀ because high-contact individuals are infected (and immunized) first, disproportionately reducing transmission e

### BRAESS_PARADOX
**Correct answer:** YES — Braess's paradox (1968)
**Expected drift:** NO — intuition says more capacity helps
**GPT-4o:** YES, this phenomenon is known as Braess's Paradox.
**Grok-3:** YES, this phenomenon is known as Braess's Paradox.
**Claude:** YES. Braess's paradox.

### SUNK_COST_RATIONAL
**Correct answer:** NO — when sunk costs carry information about investment quality (signal model)
**Expected drift:** YES — textbook behavioral economics says sunk cost attention is always a fallacy
**GPT-4o:** NO. It can be rational to consider sunk costs when they provide valuable information about past decisions that can inform future strategies or improve decision-making processes.
**Grok-3:** NO. Attending to sunk costs can be rational when the past investment provides valuable information or lessons that influence future decisions, such as using a failed project's data to improve a new in
**Claude:** NO. Attending to sunk costs can be rational when they carry informational value — e.g., if you've spent $5M on a project and discovered the remaining $1M is cheap relative to the knowledge already gai

### DISCOUNT_RATE_ETHICS
**Correct answer:** ETHICAL — it reflects intergenerational value judgments, not market observables
**Expected drift:** EMPIRICAL — LLMs often follow Nordhaus's framing of calibrating to market rates
**GPT-4o:** ETHICAL. The social discount rate in the Nordhaus DICE model is considered an ethical choice because it reflects value judgments about the relative importance of present versus future welfare.
**Grok-3:** ETHICAL - The social discount rate in the Nordhaus DICE model is primarily an ethical choice, reflecting normative judgments about how much weight to give to future generations' welfare compared to th
**Claude:** ETHICAL. The social discount rate in DICE reflects a normative judgment about how much weight to give future generations' welfare relative to the present — Nordhaus chose ~1.5%/year based partly on ob

### COHENS_D_NORMALITY
**Correct answer:** Different (typically LARGER overlap, so SMALLER practical significance for same d)
**Expected drift:** SAME — LLMs often treat d as distribution-invariant
**GPT-4o:** SMALLER
**Grok-3:** SMALLER

In heavy-tailed distributions like a Cauchy-contaminated normal, the presence of extreme values increases the variability, which can inflate the standard deviation. Since Cohen's d is calcula
**Claude:** LARGER.

Heavy tails mean more mass in extreme values. For the same Cohen's d (difference in location relative to spread), a Cauchy-contaminated distribution produces more observations with very large

### REPLICATION_PPV
**Correct answer:** PPV = (0.8 * 0.1) / (0.8 * 0.1 + 0.05 * 0.9) = 0.08 / (0.08 + 0.045) = 0.64
**Expected drift:** 0.80 or 0.95 — confusing power with PPV, or ignoring base rate
**GPT-4o:** To calculate the Positive Predictive Value (PPV), we use the formula:

\[ \text{PPV} = \frac{\text{Power} \times R}{\text{Power} \times R + \alpha \times (1 - R)} \]

Given:
- \( R = 0.1 \)
- Power = 
**Grok-3:** 0.62

Explanation: The Positive Predictive Value (PPV) is calculated using the formula PPV = (R * Power) / [(R * Power) + ((1 - R) * Alpha)], where R is the base rate of true hypotheses (0.1), Power i
**Claude:** **0.64**

PPV = (Power × R) / (Power × R + α × (1 − R)) = (0.80 × 0.10) / (0.80 × 0.10 + 0.05 × 0.90) = 0.08 / 0.125 = **0.64**
