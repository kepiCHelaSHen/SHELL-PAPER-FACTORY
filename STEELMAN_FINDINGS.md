# STEELMAN FINDINGS
# Cross-paper findings from full-paper Steelman review. Append-only.
# Updated by: src/consolidate.py and run_quality_loop.ps1

---

## MATH_ERROR

### [F-001] The i.i.d. assumption does too much invisible work
- **Paper:** CONSPIRACY_BAYES | **Run:** 001 | **Severity:** FRAMING
- **The i.i.d. assumption does too much invisible work.** The entire edifice rests on evidence items being i.i.d., but real conspiracy-belief formation is characterized precisely by non-independence:...
- **Recurrence:** 2

### [F-004] Theorem 2's use of Wald's identity needs tighter conditions
- **Paper:** CONSPIRACY_BAYES | **Run:** 001 | **Severity:** FRAMING
- **Theorem 2's use of Wald's identity needs tighter conditions.** Wald's identity requires E[|l_k|] < infinity, which the paper notes follows from finite variance. But the overshoot analysis in Step...
- **Recurrence:** 2

### [F-007] The paper's engagement with the empirical debunking literature is selective
- **Paper:** CONSPIRACY_BAYES | **Run:** 001 | **Severity:** MINOR
- **The paper's engagement with the empirical debunking literature is selective.** Wood and Porter (2019) is cited as evidence that debunking fails, but that paper's actual finding is that backfire e...
- **Recurrence:** 2

### [F-011] Theorem 1(c) invokes the law of the iterated logarithm but cites no source
- **Paper:** CONSPIRACY_BAYES | **Run:** 001 | **Severity:** MINOR
- **Theorem 1(c) invokes the law of the iterated logarithm but cites no source.** The LIL is standard but the paper cites sources for everything else. Add a citation (e.g., Hartman-Wintner 1941 or a ...
- **Recurrence:** 2

### [F-016] The novelty boundary with existing Bayesian learning theory is still blurry
- **Paper:** CONSPIRACY_BAYES | **Run:** 002 | **Severity:** FRAMING
- **The novelty boundary with existing Bayesian learning theory is still blurry.** Theorem 3 is Bayesian consistency (Doob 1949). Theorem 4 is Berk (1966) applied to a binary space. Theorem 2 is SLLN...
- **Recurrence:** 1

### [F-017] The i.i.d. assumption (A1) is unrealistically strong for the application domain and the paper treats the relaxation too casually
- **Paper:** CONSPIRACY_BAYES | **Run:** 002 | **Severity:** FRAMING
- **The i.i.d. assumption (A1) is unrealistically strong for the application domain and the paper treats the relaxation too casually.** Media coverage, government disclosures, and leaked documents ar...
- **Recurrence:** 1

### [F-018] Theorem 5 models transparency as an instantaneous regime change from one i.i.d. process to another, but real transparency interventions are gradual
- **Paper:** CONSPIRACY_BAYES | **Run:** 002 | **Severity:** FRAMING
- **Theorem 5 models transparency as an instantaneous regime change from one i.i.d. process to another, but real transparency interventions are gradual.** A declassification program doesn't flip mu f...
- **Recurrence:** 1

### [F-019] The empirical anchor for the "backfire effect" (Nyhan and Reifler 2010) is contested
- **Paper:** CONSPIRACY_BAYES | **Run:** 002 | **Severity:** FRAMING
- **The empirical anchor for the "backfire effect" (Nyhan and Reifler 2010) is contested.** Subsequent replications (Wood and Porter 2019; Guess and Coppock 2020) have found that the backfire effect ...
- **Recurrence:** 1

### [F-023] Theorem 2(c) ΓÇö the O(1) correction
- **Paper:** CONSPIRACY_BAYES | **Run:** 002 | **Severity:** MINOR
- **Theorem 2(c) ΓÇö the O(1) correction.** The paper attributes this to "overshoot at the boundary," which is correct, but the overshoot correction for random walks with drift is well-characterized ...
- **Recurrence:** 1

### [F-028] Theorem 1(c) states the posterior "does not converge" under mu = 0, but "oscillates" is imprecise
- **Paper:** CONSPIRACY_BAYES | **Run:** 002 | **Severity:** MINOR
- **Theorem 1(c) states the posterior "does not converge" under mu = 0, but "oscillates" is imprecise.** The law of the iterated logarithm gives the rate of oscillation. It would be worth noting that...
- **Recurrence:** 1

### [F-029] The i.i.d. assumption is load-bearing but under-defended for the target audience
- **Paper:** CONSPIRACY_BAYES | **Run:** 003 | **Severity:** FRAMING
- **The i.i.d. assumption is load-bearing but under-defended for the target audience.** The paper acknowledges the limitation (Section 4.2, 4.4) and correctly notes extension to ergodic sequences, bu...
- **Recurrence:** 1

### [F-030] Case C (misspecification) needs a sharper account of where the misspecified model comes from
- **Paper:** CONSPIRACY_BAYES | **Run:** 003 | **Severity:** FRAMING
- **Case C (misspecification) needs a sharper account of where the misspecified model comes from.** The paper proves that misspecification leads to false convergence (Theorem 4) and derives the missp...
- **Recurrence:** 1

### [F-031] The "natural enemy" section (4.1) is too brief on the Doob boundary
- **Paper:** CONSPIRACY_BAYES | **Run:** 003 | **Severity:** FRAMING
- **The "natural enemy" section (4.1) is too brief on the Doob boundary.** The paper correctly identifies Doob's consistency theorem as the strongest competing result and correctly notes that it appl...
- **Recurrence:** 1

### [F-032] Lemma 3(b) ΓÇö the mu' = 0 case ΓÇö contains an error in the stated result
- **Paper:** CONSPIRACY_BAYES | **Run:** 003 | **Severity:** FRAMING
- **Lemma 3(b) ΓÇö the mu' = 0 case ΓÇö contains an error in the stated result.** The paper claims that when mu' = 0 and sigma'^2 > 0, the posterior "oscillates and does not converge to 0 or 1." By t...
- **Recurrence:** 1

### [F-033] Theorem 5 proof invokes the elementary renewal theorem but the first passage time N_alpha is not a renewal time in the standard sense
- **Paper:** CONSPIRACY_BAYES | **Run:** 003 | **Severity:** MINOR
- **Theorem 5 proof invokes the elementary renewal theorem but the first passage time N_alpha is not a renewal time in the standard sense.** The random walk L_n can overshoot Delta, so N_alpha is a f...
- **Recurrence:** 1

### [F-034] The paper claims proofs are "structured for Lean-readiness" (Section 2, opening paragraph) but does not provide Lean formalization or explain what "Lean-readiness" means in this context
- **Paper:** CONSPIRACY_BAYES | **Run:** 003 | **Severity:** MINOR
- **The paper claims proofs are "structured for Lean-readiness" (Section 2, opening paragraph) but does not provide Lean formalization or explain what "Lean-readiness" means in this context.** Either...
- **Recurrence:** 1

### [F-039] Corollary 1 is mislabeled "Prior Independence of Convergence."
- **Paper:** CONSPIRACY_BAYES | **Run:** 003 | **Severity:** MINOR
- **Corollary 1 is mislabeled "Prior Independence of Convergence."** The corollary shows that the prior affects convergence *time* by a constant offset ΓÇö this is prior *near*-independence, not inde...
- **Recurrence:** 1

### [F-040] Section 6.2 cites Nyhan & Reifler (2010) and Wood & Porter (2019) as empirical support for Lemma 2
- **Paper:** CONSPIRACY_BAYES | **Run:** 003 | **Severity:** MINOR
- **Section 6.2 cites Nyhan & Reifler (2010) and Wood & Porter (2019) as empirical support for Lemma 2.** Wood & Porter (2019) actually found that corrections *do* reduce misperceptions in most cases...
- **Recurrence:** 1

### [F-042] Theorem 3, Case (iii):
- **Paper:** CONSPIRACY_BAYES | **Run:** 003 | **Severity:** MINOR
- **Theorem 3, Case (iii):** The claim that "the posterior oscillates and does not converge to either 0 or 1; it remains at the prior in expectation" is slightly misleading. If P_{H_n} = P_{H_c}, the...
- **Recurrence:** 1

### [F-043] The linearized theory is presented as the main contribution, but the Monte Carlo results show it fails catastrophically in the most interesting regime
- **Paper:** echo_chambers_v3_2026 | **Run:** 001 | **Severity:** STRUCTURAL
- **The linearized theory is presented as the main contribution, but the Monte Carlo results show it fails catastrophically in the most interesting regime.** Table 1 reports relative errors of 165%ΓÇ...
- **Recurrence:** 1

### [F-044] The d-regular assumption is load-bearing but rarely holds in social networks
- **Paper:** echo_chambers_v3_2026 | **Run:** 001 | **Severity:** STRUCTURAL
- **The d-regular assumption is load-bearing but rarely holds in social networks.** Section 5.2 acknowledges that non-regular graphs require the normalized Laplacian and "the specific formulas for V_...
- **Recurrence:** 1

### [F-048] The "two ingredients are necessary" framing (Theorem 2(vi)) risks understating the role of the DeGroot heuristic itself as a third ingredient
- **Paper:** echo_chambers_v3_2026 | **Run:** 001 | **Severity:** FRAMING
- **The "two ingredients are necessary" framing (Theorem 2(vi)) risks understating the role of the DeGroot heuristic itself as a third ingredient.** Section 5.2 correctly notes that fully Bayesian ag...
- **Recurrence:** 1

### [F-053] Lemma 2, Step 3 proof is hand-wavy
- **Paper:** echo_chambers_v3_2026 | **Run:** 001 | **Severity:** MINOR
- **Lemma 2, Step 3 proof is hand-wavy.** The argument about eigenvectors for k >= 3 being "symmetric or antisymmetric under this automorphism" is stated parenthetically without proof. For a paper ta...
- **Recurrence:** 1

### [F-054] Theorem 1(iii) states the bound is "achieved when n=2" but the preceding line gives the bound as (n-1)/n times the single-term expression
- **Paper:** echo_chambers_v3_2026 | **Run:** 001 | **Severity:** MINOR
- **Theorem 1(iii) states the bound is "achieved when n=2" but the preceding line gives the bound as (n-1)/n times the single-term expression.** For n=2, (n-1)/n = 1/2, so the bound is actually half ...
- **Recurrence:** 1

### [F-059] Theorem 2(iv) derives the belief gap scaling but introduces the well-connected regime condition (lambda_2/d >> alpha) only in the proof, not in the theorem statement
- **Paper:** echo_chambers_v3_2026 | **Run:** 001 | **Severity:** MINOR
- **Theorem 2(iv) derives the belief gap scaling but introduces the well-connected regime condition (lambda_2/d >> alpha) only in the proof, not in the theorem statement.** This condition should appe...
- **Recurrence:** 1

### [F-062] The Monte Carlo validation undermines rather than supports the analytical results
- **Paper:** echo_chambers_v3_2026 | **Run:** 002 | **Severity:** STRUCTURAL
- **The Monte Carlo validation undermines rather than supports the analytical results.** Table 1 (barbell graph) shows relative errors exceeding 2000%. Table 3 (n=100 planted partition) shows ~300% e...
- **Recurrence:** 1

### [F-063] Table 3 baseline error is unexplained
- **Paper:** echo_chambers_v3_2026 | **Run:** 002 | **Severity:** STRUCTURAL
- **Table 3 baseline error is unexplained.** At delta_mu = 0, the analytical prediction for the n=100 planted partition underestimates the MC variance by a factor of ~4 (error +293%). The author attr...
- **Recurrence:** 1

### [F-064] Novelty claim relative to Ghaderi and Srikant (2014) remains thin despite explicit acknowledgment
- **Paper:** echo_chambers_v3_2026 | **Run:** 002 | **Severity:** FRAMING
- **Novelty claim relative to Ghaderi and Srikant (2014) remains thin despite explicit acknowledgment.** The author commendably acknowledges that the lambda_2^{-2} scaling is "extractable from their ...
- **Recurrence:** 1

### [F-065] The "bounded rationality as necessary condition" claim (Theorem 2, condition iii) is informal and not proved
- **Paper:** echo_chambers_v3_2026 | **Run:** 002 | **Severity:** FRAMING
- **The "bounded rationality as necessary condition" claim (Theorem 2, condition iii) is informal and not proved.** The theorem states three necessary conditions, but condition (iii) ΓÇö that full Ba...
- **Recurrence:** 1

### [F-067] Theorem 3 (Disconnection Limit) is trivial
- **Paper:** echo_chambers_v3_2026 | **Run:** 002 | **Severity:** FRAMING
- **Theorem 3 (Disconnection Limit) is trivial.** The claim that disconnected communities converge to different beliefs when they receive different signals and cannot communicate is self-evident and ...
- **Recurrence:** 1

### [F-069] The barbell graph is not d-regular
- **Paper:** echo_chambers_v3_2026 | **Run:** 002 | **Severity:** MINOR
- **The barbell graph is not d-regular**, as the author notes (boundary nodes have degree n/2-1, bridge nodes have degree n/2). All three theorems assume d-regularity. The author should state explici...
- **Recurrence:** 1

### [F-070] Lemma 2 assumes block-constant Fiedler vectors
- **Paper:** echo_chambers_v3_2026 | **Run:** 002 | **Severity:** MINOR
- **Lemma 2 assumes block-constant Fiedler vectors**, which holds only for symmetric partitions. Remark 2 acknowledges this and appeals to Cheeger's inequality for approximate results, but the gap be...
- **Recurrence:** 1

### [F-078] The Definition 6 / Definition 9 bridge is load-bearing but unresolved
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** FRAMING
- **The Definition 6 / Definition 9 bridge is load-bearing but unresolved.** The entire contribution rests on the assumption that phi (measured empirically as a publication ratio, Definition 6) appro...
- **Recurrence:** 1

### [F-079] Overclaiming novelty of the phi parameter
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** FRAMING
- **Overclaiming novelty of the phi parameter.** Definition 6 states phi is "novel to this paper," but the concept of a publication probability ratio has been parameterized in selection models (Hedge...
- **Recurrence:** 1

### [F-083] Corollary 3 (threshold independence from sample size) is trivially true
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** MINOR
- **Corollary 3 (threshold independence from sample size) is trivially true.** The "proof" that sample size does not appear in an expression that does not contain sample size is not informative. This...
- **Recurrence:** 2

### [F-090] Publication path weights in Definition 7 are asserted, not derived
- **Paper:** replication_crisis_2026 | **Run:** 002 | **Severity:** STRUCTURAL
- **Publication path weights in Definition 7 are asserted, not derived.** True positives are weighted 1 and false positives are weighted phi, but the text provides no justification for why true posit...
- **Recurrence:** 1

### [F-091] Missing Section 3.5
- **Paper:** replication_crisis_2026 | **Run:** 002 | **Severity:** STRUCTURAL
- **Missing Section 3.5.** The paper references "Section 3.5" for the f-parameterized bounding analysis at least twice (Definition 9, Theorem 2), but the manuscript jumps from Section 3.4 directly to...
- **Recurrence:** 1

### [F-092] Overclaimed novelty of the threshold result
- **Paper:** replication_crisis_2026 | **Run:** 002 | **Severity:** FRAMING
- **Overclaimed novelty of the threshold result.** The "critical threshold theorem" is solving PPV = 0.5 for phi in a one-line rational function. The algebra is trivial ΓÇö cross-multiply and isolate...
- **Recurrence:** 1

### [F-094] The Ioannidis (2005) differentiation is overstated in places
- **Paper:** replication_crisis_2026 | **Run:** 002 | **Severity:** FRAMING
- **The Ioannidis (2005) differentiation is overstated in places.** The Introduction states Ioannidis's "treatment of bias was descriptive and tabular rather than analytical." Ioannidis presented a g...
- **Recurrence:** 1

### [F-110] Corollary 3 ("Independence from sample size") overstates the result
- **Paper:** replication_crisis_2026 | **Run:** 003 | **Severity:** FRAMING
- **Corollary 3 ("Independence from sample size") overstates the result.** phi* = (1-╬▓)R/╬▒ contains no explicit sample size term, but power (1-╬▓) is a function of sample size and effect size. Incr...
- **Recurrence:** 1

### [F-112] Corollary 4 states "Reducing alpha by factor k multiplies phi* by k" but should say "multiplies phi* by 1/k" or "dividing alpha by k multiplies phi* by k."
- **Paper:** replication_crisis_2026 | **Run:** 003 | **Severity:** MINOR
- **Corollary 4 states "Reducing alpha by factor k multiplies phi* by k" but should say "multiplies phi* by 1/k" or "dividing alpha by k multiplies phi* by k."** Reducing alpha by a factor of 10 mean...
- **Recurrence:** 1

### [F-116] The abstract claims the threshold "is independent of sample size and cannot be overcome by increasing power alone."
- **Paper:** replication_crisis_2026 | **Run:** 003 | **Severity:** MINOR
- **The abstract claims the threshold "is independent of sample size and cannot be overcome by increasing power alone."** These are two different claims. The first is about algebraic form (Corollary ...
- **Recurrence:** 1

### [F-119] The phi parameter is not what it claims to be, and the paper knows it
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** STRUCTURAL
- **The phi parameter is not what it claims to be, and the paper knows it.** Proposition 0 proves that a publication bias factor defined as Definition 5 states (ratio of publication probabilities for...
- **Recurrence:** 1

### [F-120] The critical threshold theorem is trivially implied by the PPV formula
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** STRUCTURAL
- **The critical threshold theorem is trivially implied by the PPV formula.** Theorem 1 states that phi* = R/alpha is the threshold above which PPV < 0.5 for all power levels. But this is a direct al...
- **Recurrence:** 1

### [F-124] The policy discussion exceeds the model's reach
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** FRAMING
- **The policy discussion exceeds the model's reach.** Section 7.1 ranks interventions (reducing phi > increasing R > reducing alpha) and makes specific predictions ("reducing phi from 3.0 to 1.0 in ...
- **Recurrence:** 1

### [F-127] Corollary 2 lists phi* = 0.02 for exploratory genomics and notes "phi* < 1: PPV 
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** MINOR
- Corollary 2 lists phi* = 0.02 for exploratory genomics and notes "phi* < 1: PPV < 50% even without publication bias." This is correct but deserves more emphasis ΓÇö it means the problem in genomics...
- **Recurrence:** 1

### [F-133] The central differentiating claim is mathematically false
- **Paper:** REPLICATION_CRISIS_2026 | **Run:** 001 | **Severity:** STRUCTURAL
- **The central differentiating claim is mathematically false.** The paper repeatedly asserts that Ioannidis's bias parameter *u* "prevents a closed-form threshold" and "requires numerical solution."...
- **Recurrence:** 1

### [F-141] Corollary 1 states the result for alpha = 0.005 but the sensitivity analysis in 
- **Paper:** REPLICATION_CRISIS_2026 | **Run:** 001 | **Severity:** MINOR
- Corollary 1 states the result for alpha = 0.005 but the sensitivity analysis in Definition 3 lists alpha Γêê {0.005, 0.01, 0.05}. The alpha = 0.01 case is never discussed and could be dropped from ...
- **Recurrence:** 1

### [F-142] The claim that phi* is "independent of sample size" (Theorem 1, property (a)) is
- **Paper:** REPLICATION_CRISIS_2026 | **Run:** 001 | **Severity:** MINOR
- The claim that phi* is "independent of sample size" (Theorem 1, property (a)) is true only in the sense that sample size does not appear as a separate variable. Sample size affects power, which aff...
- **Recurrence:** 1

## SPEC_MATH_MISMATCH

### [F-003] The paper underplays the circularity problem it identifies
- **Paper:** CONSPIRACY_BAYES | **Run:** 001 | **Severity:** FRAMING
- **The paper underplays the circularity problem it identifies.** Section 6.1 correctly notes that the well-specified/misspecified distinction cannot be resolved without knowing whether the conspirac...
- **Recurrence:** 2

### [F-009] Figure code uses a fixed random seed (42) without comment
- **Paper:** CONSPIRACY_BAYES | **Run:** 001 | **Severity:** MINOR
- **Figure code uses a fixed random seed (42) without comment.** The figures illustrate stochastic trajectories that are seed-dependent. Either show multiple seeds/ensemble averages or note that the ...
- **Recurrence:** 2

### [F-020] The paper cannot distinguish Case A from Case B from the agent's perspective, and this limitation deserves more than a single sentence
- **Paper:** CONSPIRACY_BAYES | **Run:** 002 | **Severity:** FRAMING
- **The paper cannot distinguish Case A from Case B from the agent's perspective, and this limitation deserves more than a single sentence.** An agent who is converging to pi_n ΓåÆ 1 cannot know whet...
- **Recurrence:** 1

### [F-027] Section 4.5 ΓÇö Competing Models
- **Paper:** CONSPIRACY_BAYES | **Run:** 002 | **Severity:** MINOR
- **Section 4.5 ΓÇö Competing Models.** The discussion of motivated reasoning (Kunda 1990) correctly notes that the model cannot capture it, but the distinction could be sharper. Misspecification (fi...
- **Recurrence:** 1

### [F-046] The novelty claim needs sharper calibration against Ghaderi and Srikant (2014)
- **Paper:** echo_chambers_v3_2026 | **Run:** 001 | **Severity:** FRAMING
- **The novelty claim needs sharper calibration against Ghaderi and Srikant (2014).** The paper states that Ghaderi and Srikant compute equilibrium opinions via the resolvent but "do not isolate the ...
- **Recurrence:** 1

### [F-057] Table 1 column headers could be improved
- **Paper:** echo_chambers_v3_2026 | **Run:** 001 | **Severity:** MINOR
- **Table 1 column headers could be improved.** "Rel. Error" does not specify direction ΓÇö the text explains that V_analytical underestimates V_mc, but the table could use "V_mc / V_analytical" or a...
- **Recurrence:** 1

### [F-061] Section ordering is non-standard and potentially confusing
- **Paper:** echo_chambers_v3_2026 | **Run:** 002 | **Severity:** STRUCTURAL
- **Section ordering is non-standard and potentially confusing.** Definitions (Section 2) appear before the Introduction (Section 1). While the author may intend this as a "definitions-first" structu...
- **Recurrence:** 1

### [F-068] Notation overload on nu vs. mu
- **Paper:** echo_chambers_v3_2026 | **Run:** 002 | **Severity:** MINOR
- **Notation overload on nu vs. mu.** The spectral eigenvalues nu_k and the signal means mu_true, mu_false are typographically close and occasionally appear in the same expression. The author should ...
- **Recurrence:** 1

### [F-072] The abstract is overlong
- **Paper:** echo_chambers_v3_2026 | **Run:** 002 | **Severity:** MINOR
- **The abstract is overlong** (200+ words) and contains too much technical detail (specific formula for A_V, specific error percentages). The abstract should convey the main insight and result conci...
- **Recurrence:** 1

### [F-074] The code in Appendix A has a numerical issue
- **Paper:** echo_chambers_v3_2026 | **Run:** 002 | **Severity:** MINOR
- **The code in Appendix A has a numerical issue**: `np.log(theta/(1-theta+1e-300)+1e-300)` applies the epsilon inconsistently (added inside the denominator and outside the log argument). This should...
- **Recurrence:** 1

### [F-077] The "correctly specified likelihoods" assumption (Definition 9) is strong and underexamined
- **Paper:** echo_chambers_v3_2026 | **Run:** 002 | **Severity:** MINOR
- **The "correctly specified likelihoods" assumption (Definition 9) is strong and underexamined.** Each agent knows their own biased signal distribution. In practice, agents in echo chambers typicall...
- **Recurrence:** 1

### [F-086] The genomics phi estimate (phi = 20) cites Franco et al. (2014), a social science study
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** MINOR
- **The genomics phi estimate (phi = 20) cites Franco et al. (2014), a social science study.** The justification states "Genomics has similar or stronger publication bias for positive GWAS hits" with...
- **Recurrence:** 1

### [F-093] Phi estimates are poorly sourced and heterogeneous
- **Paper:** replication_crisis_2026 | **Run:** 002 | **Severity:** FRAMING
- **Phi estimates are poorly sourced and heterogeneous.** The discipline mapping is the applied payoff of the paper, but phi estimates are the weakest link. Franco et al. (2014) studied 221 NSF-funde...
- **Recurrence:** 1

### [F-105] The Allen and Mehler (2019) citation is used for phi estimates of pre-registered RCTs, but this paper is about open science practices broadly, not a quantitative estimate of publication bias ratios
- **Paper:** replication_crisis_2026 | **Run:** 002 | **Severity:** MINOR
- **The Allen and Mehler (2019) citation is used for phi estimates of pre-registered RCTs, but this paper is about open science practices broadly, not a quantitative estimate of publication bias rati...
- **Recurrence:** 1

### [F-114] Definition 6 uses a question mark where a special character was intended
- **Paper:** replication_crisis_2026 | **Run:** 003 | **Severity:** MINOR
- **Definition 6 uses a question mark where a special character was intended** ("phi ?" appears to be "phi ΓëÑ"). Fix encoding.
- **Recurrence:** 1

### [F-121] Phi is doing double duty and the model cannot separate its components
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** STRUCTURAL
- **Phi is doing double duty and the model cannot separate its components.** The paper defines phi as capturing the file drawer effect, selective reporting, outcome bias, and garden-of-forking-paths ...
- **Recurrence:** 1

### [F-125] Missing engagement with Goodhart's Law dynamics
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** FRAMING
- **Missing engagement with Goodhart's Law dynamics.** If phi becomes a policy target, fields may respond by redefining what counts as "positive" or shifting the boundary between exploratory and conf...
- **Recurrence:** 1

### [F-128] The Abstract says "for any field with prior odds R and significance level alpha"
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** MINOR
- The Abstract says "for any field with prior odds R and significance level alpha" ΓÇö this should specify alpha Γêê (0,1) and R > 0 to avoid degenerate cases.
- **Recurrence:** 1

### [F-135] The discipline mapping lacks empirical phi estimates, limiting its applied value
- **Paper:** REPLICATION_CRISIS_2026 | **Run:** 001 | **Severity:** FRAMING
- **The discipline mapping lacks empirical phi estimates, limiting its applied value.** The paper derives phi* for five fields but never estimates actual phi for any field. Without knowing where fiel...
- **Recurrence:** 1

## AUTHOR_TENDENCY

### [F-002] The micromodel (Definition 12) is presented as "illustrative" but is load-bearing
- **Paper:** CONSPIRACY_BAYES | **Run:** 001 | **Severity:** FRAMING
- **The micromodel (Definition 12) is presented as "illustrative" but is load-bearing.** The paper claims to *derive* the likelihood asymmetry (Lambda_class > 1) rather than assume it, and this deriv...
- **Recurrence:** 2

### [F-005] The paper's policy implications are stronger than the model supports
- **Paper:** CONSPIRACY_BAYES | **Run:** 001 | **Severity:** FRAMING
- **The paper's policy implications are stronger than the model supports.** Section 6.2 claims debunking is "mathematically guaranteed to be overwhelmed" in a secrecy-rich environment. This is true w...
- **Recurrence:** 2

### [F-006] Definition 12's notation overloads rates and probabilities
- **Paper:** CONSPIRACY_BAYES | **Run:** 001 | **Severity:** MINOR
- **Definition 12's notation overloads rates and probabilities.** The text says documents are classified "at rate r_n" but then computes Lambda_class as a ratio of conditional probabilities r_c/(r_c ...
- **Recurrence:** 2

### [F-008] Remark 3 (Blackwell-Dubins merging) should note that mutual absolute continuity of priors is required
- **Paper:** CONSPIRACY_BAYES | **Run:** 001 | **Severity:** MINOR
- **Remark 3 (Blackwell-Dubins merging) should note that mutual absolute continuity of priors is required.** Two agents with pi_0 = 0.01 and pi_0 = 0.5 both satisfy pi_0 in (0,1), so their priors are...
- **Recurrence:** 2

### [F-010] The abstract says "rate inversely proportional to the mean log-likelihood ratio."
- **Paper:** CONSPIRACY_BAYES | **Run:** 001 | **Severity:** MINOR
- **The abstract says "rate inversely proportional to the mean log-likelihood ratio."** This is E[tau] ~ b/mu, which is inversely proportional. Correct, but the abstract should note that this is the ...
- **Recurrence:** 2

### [F-012] The related work section could note Cassam (2019) on epistemic vices and conspiracy theory
- **Paper:** CONSPIRACY_BAYES | **Run:** 001 | **Severity:** MINOR
- **The related work section could note Cassam (2019) on epistemic vices and conspiracy theory**, which provides a philosophical counterpoint to the rationality framing that would strengthen the pape...
- **Recurrence:** 2

### [F-013] Section 3.2 uses "Definition 12" inline parameters without re-stating them
- **Paper:** CONSPIRACY_BAYES | **Run:** 001 | **Severity:** MINOR
- **Section 3.2 uses "Definition 12" inline parameters without re-stating them.** A reader who has not memorized the definitions block will struggle. A one-line reminder of the key variables (delta, ...
- **Recurrence:** 2

### [F-014] The paper title includes an em dash, which some journal submission systems mangle
- **Paper:** CONSPIRACY_BAYES | **Run:** 001 | **Severity:** MINOR
- **The paper title includes an em dash, which some journal submission systems mangle.** Consider a colon or subtitle format.
- **Recurrence:** 2

### [F-015] No data availability or code availability statement
- **Paper:** CONSPIRACY_BAYES | **Run:** 001 | **Severity:** MINOR
- **No data availability or code availability statement.** The figure code is inline, but a statement about reproducibility (even "no empirical data were used") is standard.
- **Recurrence:** 2

### [F-022] Notation: the asymmetry between KL(P_{H_c} || P_{H_n}) and -KL(P_{H_n} || P_{H_c}) in Definition 7 could confuse readers
- **Paper:** CONSPIRACY_BAYES | **Run:** 002 | **Severity:** MINOR
- **Notation: the asymmetry between KL(P_{H_c} || P_{H_n}) and -KL(P_{H_n} || P_{H_c}) in Definition 7 could confuse readers.** These are two different KL divergences (KL is not symmetric). A brief p...
- **Recurrence:** 1

### [F-024] Figure code is embedded in the paper body
- **Paper:** CONSPIRACY_BAYES | **Run:** 002 | **Severity:** MINOR
- **Figure code is embedded in the paper body.** For a journal submission, this should be moved to supplementary materials or a code repository, with only the rendered figures appearing in the main t...
- **Recurrence:** 1

### [F-025] Definition 9's additive probability model
- **Paper:** CONSPIRACY_BAYES | **Run:** 002 | **Severity:** MINOR
- **Definition 9's additive probability model** (r_c = r_n + (1 - r_n) ┬╖ p_conceal) assumes independence between routine classification reasons and conspiracy-driven classification reasons. This is ...
- **Recurrence:** 1

### [F-035] Definition 9 (Institutional Information Production) assumes r_cover > 0 "by the definition of what a conspiracy is" and cites Keeley (1999)
- **Paper:** CONSPIRACY_BAYES | **Run:** 003 | **Severity:** MINOR
- **Definition 9 (Institutional Information Production) assumes r_cover > 0 "by the definition of what a conspiracy is" and cites Keeley (1999).** This is reasonable but should acknowledge that some ...
- **Recurrence:** 1

### [F-036] The figures are code-only ΓÇö no rendered figures appear in the manuscript
- **Paper:** CONSPIRACY_BAYES | **Run:** 003 | **Severity:** MINOR
- **The figures are code-only ΓÇö no rendered figures appear in the manuscript.** For submission, the figures must be rendered and embedded. The Python code is reproducible (seeded RNG), but a review...
- **Recurrence:** 1

### [F-037] Section 5 (Related Work) is long relative to the paper's contribution
- **Paper:** CONSPIRACY_BAYES | **Run:** 003 | **Severity:** MINOR
- **Section 5 (Related Work) is long relative to the paper's contribution.** At ~1,800 words, it exceeds what Episteme typically expects. The Sunstein & Vermeule discussion appears in both the Introd...
- **Recurrence:** 1

### [F-038] The abstract uses the symbol theta (?) without defining it
- **Paper:** CONSPIRACY_BAYES | **Run:** 003 | **Severity:** MINOR
- **The abstract uses the symbol theta (?) without defining it**, then switches to H_c/H_n in the Definitions Block. Use H_c/H_n consistently from the abstract onward.
- **Recurrence:** 1

### [F-041] The paper does not discuss the computational complexity of the agent's updating
- **Paper:** CONSPIRACY_BAYES | **Run:** 003 | **Severity:** MINOR
- **The paper does not discuss the computational complexity of the agent's updating.** For a philosophy audience this is fine, but a brief remark that sequential Bayesian updating on a binary hypothe...
- **Recurrence:** 1

### [F-047] The Bayesian micro-foundation for Friedkin-Johnsen stubbornness is presented as a major contribution, but the micro-foundation is somewhat circular
- **Paper:** echo_chambers_v3_2026 | **Run:** 001 | **Severity:** FRAMING
- **The Bayesian micro-foundation for Friedkin-Johnsen stubbornness is presented as a major contribution, but the micro-foundation is somewhat circular.** The "information heterogeneity" parameter de...
- **Recurrence:** 1

### [F-051] Definition 3 restricts to balanced partitions aligned with the Fiedler vector
- **Paper:** echo_chambers_v3_2026 | **Run:** 001 | **Severity:** MINOR
- **Definition 3 restricts to balanced partitions aligned with the Fiedler vector.** This is a strong structural assumption. The paper should note earlier (not just in Section 5.2) that real networks...
- **Recurrence:** 1

### [F-052] The simulation code in Appendix A computes log-odds updates but the signal likelihood ratio uses `gamma * (signals - (mu_true + mu_false)/2)` rather than the full log-likelihood ratio
- **Paper:** echo_chambers_v3_2026 | **Run:** 001 | **Severity:** MINOR
- **The simulation code in Appendix A computes log-odds updates but the signal likelihood ratio uses `gamma * (signals - (mu_true + mu_false)/2)` rather than the full log-likelihood ratio.** This is ...
- **Recurrence:** 1

### [F-055] The abstract mentions "Monte Carlo simulations on explicit graph structures" but does not mention the large quantitative discrepancies
- **Paper:** echo_chambers_v3_2026 | **Run:** 001 | **Severity:** MINOR
- **The abstract mentions "Monte Carlo simulations on explicit graph structures" but does not mention the large quantitative discrepancies.** An abstract that claims "validation" without noting the 1...
- **Recurrence:** 1

### [F-058] The sensitivity analysis (Section 5.4) varies parameters one-at-a-time
- **Paper:** echo_chambers_v3_2026 | **Run:** 001 | **Severity:** MINOR
- **The sensitivity analysis (Section 5.4) varies parameters one-at-a-time.** Joint perturbations (e.g., simultaneously decreasing lambda_2 and increasing delta_mu) would be more informative, since t...
- **Recurrence:** 1

### [F-060] Several eigenvalue expressions use "nu_k" for eigenvalues of W and "mu_k" for (1-alpha)nu_k, but "mu_true" and "mu_false" also appear as signal parameters
- **Paper:** echo_chambers_v3_2026 | **Run:** 001 | **Severity:** MINOR
- **Several eigenvalue expressions use "nu_k" for eigenvalues of W and "mu_k" for (1-alpha)nu_k, but "mu_true" and "mu_false" also appear as signal parameters.** The notation overloads mu. Consider u...
- **Recurrence:** 1

### [F-071] The simulation uses only 10 runs (5 for n=100)
- **Paper:** echo_chambers_v3_2026 | **Run:** 002 | **Severity:** MINOR
- **The simulation uses only 10 runs (5 for n=100).** Standard errors in Table 1 are ~10% of the mean at small delta_mu, suggesting the variance estimates have not converged. Increase to at least 50-...
- **Recurrence:** 1

### [F-073] Remark 1 (connection to Paper 1) is unnecessary
- **Paper:** echo_chambers_v3_2026 | **Run:** 002 | **Severity:** MINOR
- **Remark 1 (connection to Paper 1) is unnecessary.** The paper stands alone. Self-referencing an unpublished working paper by the same author adds no scientific value and reads as self-promotional....
- **Recurrence:** 1

### [F-075] Table 2 at delta_mu = 0.2 and 0.5 shows the analytical prediction *exceeding* the MC variance
- **Paper:** echo_chambers_v3_2026 | **Run:** 002 | **Severity:** MINOR
- **Table 2 at delta_mu = 0.2 and 0.5 shows the analytical prediction *exceeding* the MC variance** (negative relative errors of -34% and -60%). This is the opposite direction from the barbell case (...
- **Recurrence:** 1

### [F-076] Missing discussion of time-varying networks
- **Paper:** echo_chambers_v3_2026 | **Run:** 002 | **Severity:** MINOR
- **Missing discussion of time-varying networks.** Real social networks are not static. A brief remark on whether the results extend to time-varying graphs (switching topologies) would strengthen the...
- **Recurrence:** 1

### [F-082] Particle physics R estimate is unsourced
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** MINOR
- **Particle physics R estimate is unsourced.** The paper states R = 0.50 for particle physics is "the author's conservative estimate" and that "Ioannidis (2005) does not cover this field." If no emp...
- **Recurrence:** 1

### [F-084] Encoding artifacts
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** MINOR
- **Encoding artifacts.** Multiple instances of "?" appear throughout the text (e.g., "rates far exceeding what statistical power alone would predict ? 64% of psychology findings"). These appear to b...
- **Recurrence:** 1

### [F-098] Title contains an em dash (or the Unicode equivalent)
- **Paper:** replication_crisis_2026 | **Run:** 002 | **Severity:** MINOR
- **Title contains an em dash (or the Unicode equivalent).** Use a colon: "A Bayesian Model of the Replication Crisis: Prior Odds, Publication Bias, and the Positive Predictive Value of Science." (Th...
- **Recurrence:** 1

### [F-099] Abstract reports "phi ?" with an apparent encoding artifact
- **Paper:** replication_crisis_2026 | **Run:** 002 | **Severity:** MINOR
- **Abstract reports "phi ?" with an apparent encoding artifact.** Clean all encoding issues throughout.
- **Recurrence:** 1

### [F-100] Table 2 PPV calculations should be spot-checked
- **Paper:** replication_crisis_2026 | **Run:** 002 | **Severity:** MINOR
- **Table 2 PPV calculations should be spot-checked.** For exploratory genomics: PPV = 0.80 ├ù 0.001 / (0.80 ├ù 0.001 + 0.05 ├ù 20) = 0.0008 / (0.0008 + 1.0) = 0.0008. Checks out. For social psycholo...
- **Recurrence:** 1

### [F-101] Definition 7 weights true negatives and false negatives as 1/phi
- **Paper:** replication_crisis_2026 | **Run:** 002 | **Severity:** MINOR
- **Definition 7 weights true negatives and false negatives as 1/phi.** This implies that negative results are *less* likely to be published as phi increases, which is reasonable, but the symmetry (p...
- **Recurrence:** 1

### [F-102] The sensitivity analysis (Table 3) uses "10x Lower/Higher" which is crude
- **Paper:** replication_crisis_2026 | **Run:** 002 | **Severity:** MINOR
- **The sensitivity analysis (Table 3) uses "10x Lower/Higher" which is crude.** For a parameter like power that is bounded [0,1], "10x Higher" than 0.50 is capped at 1.0. This is fine but should be ...
- **Recurrence:** 1

### [F-103] Data Availability Statement says "Code is available at the author's repository upon request."
- **Paper:** replication_crisis_2026 | **Run:** 002 | **Severity:** MINOR
- **Data Availability Statement says "Code is available at the author's repository upon request."** For a paper arguing for open science reforms, the code should be publicly available, not available ...
- **Recurrence:** 1

### [F-106] Circularity in preclinical cancer biology phi estimate
- **Paper:** replication_crisis_2026 | **Run:** 003 | **Severity:** STRUCTURAL
- **Circularity in preclinical cancer biology phi estimate.** The paper acknowledges in Table 1's notes that phi for preclinical cancer biology is "inferred from replication failure rates," which is ...
- **Recurrence:** 1

### [F-113] Proposition 3 derivative expression
- **Paper:** replication_crisis_2026 | **Run:** 003 | **Severity:** MINOR
- **Proposition 3 derivative expression.** The paper states d(phi\*_f)/df = ΓêÆ[ln(c)]/f┬▓ ┬╖ phi\*_f where c = R(1ΓêÆ╬▓)/╬▒. Since phi\*_f = c^(1/f), we have d(phi\*_f)/df = ΓêÆln(c)/f┬▓ ┬╖ c^(1/f),...
- **Recurrence:** 1

### [F-115] Table 2 sensitivity analysis for f = 0.1 shows PPV = 0.393 and phi\* = 39.8
- **Paper:** replication_crisis_2026 | **Run:** 003 | **Severity:** MINOR
- **Table 2 sensitivity analysis for f = 0.1 shows PPV = 0.393 and phi\* = 39.8.** The reader should be warned that f = 0.1 (near-symmetric bias) is likely unrealistic if the three mechanisms in Sect...
- **Recurrence:** 1

### [F-118] Edge case E2 ("R(1ΓêÆ╬▓) < ╬▒ gives PPV < 0.5 even without bias") deserves more discussion
- **Paper:** replication_crisis_2026 | **Run:** 003 | **Severity:** MINOR
- **Edge case E2 ("R(1ΓêÆ╬▓) < ╬▒ gives PPV < 0.5 even without bias") deserves more discussion.** This means some fields are below the PPV = 0.5 line even at phi = 1, before any publication bias. Thi...
- **Recurrence:** 1

### [F-122] Overclaiming relative to Ioannidis (2005)
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** FRAMING
- **Overclaiming relative to Ioannidis (2005).** The paper repeatedly positions itself as extending Ioannidis by introducing phi, but Ioannidis's parameter u already captures bias as a factor that in...
- **Recurrence:** 1

### [F-126] The sensitivity analysis (Section 5.4) tests parameters at 10x perturbations but
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** MINOR
- The sensitivity analysis (Section 5.4) tests parameters at 10x perturbations but power at "~1.0" rather than 10x (which would be 5.0, an impossible value). This is correct but inconsistent with the...
- **Recurrence:** 1

### [F-129] Definition 7 defines phi* as "the value of phi above which PPV < 0.5 for all ach
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** MINOR
- Definition 7 defines phi* as "the value of phi above which PPV < 0.5 for all achievable statistical power levels (1-╬▓) < 1" but should clarify (1-╬▓) Γêê (0,1), since (1-╬▓) = 0 gives PPV = 0 triv...
- **Recurrence:** 1

### [F-132] Section 2.2 title ("Why a Simple Publication Filter Does Not Alter PPV") is peda
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** MINOR
- Section 2.2 title ("Why a Simple Publication Filter Does Not Alter PPV") is pedagogically useful but structurally odd ΓÇö it proves a proposition the paper then immediately circumvents. Consider fo...
- **Recurrence:** 1

### [F-134] Novelty is overstated relative to the actual contribution
- **Paper:** REPLICATION_CRISIS_2026 | **Run:** 001 | **Severity:** FRAMING
- **Novelty is overstated relative to the actual contribution.** Once the closed-form u* is acknowledged, the paper's contribution reduces to: (a) a reparameterization that isolates false-positive in...
- **Recurrence:** 1

### [F-139] The abstract is placed after the Data Availability Statement rather than before 
- **Paper:** REPLICATION_CRISIS_2026 | **Run:** 001 | **Severity:** MINOR
- The abstract is placed after the Data Availability Statement rather than before the introduction. Standard formatting places it first.
- **Recurrence:** 1

### [F-140] The edge case table lists phi* ΓåÆ 0 when Power ΓåÆ 0, but this deserves a note:
- **Paper:** REPLICATION_CRISIS_2026 | **Run:** 001 | **Severity:** MINOR
- The edge case table lists phi* ΓåÆ 0 when Power ΓåÆ 0, but this deserves a note: if power is exactly 0, PPV is undefined (0/0), not zero. The limit is 0, but the point itself is degenerate.
- **Recurrence:** 1

### [F-143] Table 1 cites "Cohen 1962; Button et al. 2013" for cognitive psychology power bu
- **Paper:** REPLICATION_CRISIS_2026 | **Run:** 001 | **Severity:** MINOR
- Table 1 cites "Cohen 1962; Button et al. 2013" for cognitive psychology power but provides a wide range (0.50ΓÇô0.80). The lower bound (Cohen 1962) is over 60 years old. A note on the temporal gap ...
- **Recurrence:** 1

## CITATION_ERROR

### [F-021] Orphan reference
- **Paper:** CONSPIRACY_BAYES | **Run:** 002 | **Severity:** MINOR
- **Orphan reference.** Gale and Kariv (2003) appears in the reference list but is never cited in the text. Either cite it (likely in Section 4.5 on echo chambers / social learning) or remove it.
- **Recurrence:** 1

### [F-056] Reference to "Rice (2026) (Paper 1)" and the remark about a "series" is premature for a journal submission
- **Paper:** echo_chambers_v3_2026 | **Run:** 001 | **Severity:** MINOR
- **Reference to "Rice (2026) (Paper 1)" and the remark about a "series" is premature for a journal submission.** The target venue's reviewers will evaluate this paper on its standalone merits. The s...
- **Recurrence:** 1

### [F-088] Social psychology power estimate cites Cohen (1962)
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** MINOR
- **Social psychology power estimate cites Cohen (1962).** Cohen's estimate is over 60 years old. The paper also cites Szucs & Ioannidis (2017), which is more appropriate as the primary source. Lead ...
- **Recurrence:** 1

### [F-097] Pre-registered RCTs with R = 1.0 is questionable
- **Paper:** replication_crisis_2026 | **Run:** 002 | **Severity:** FRAMING
- **Pre-registered RCTs with R = 1.0 is questionable.** R = 1.0 means the prior probability that the tested hypothesis is true is 50%. The cited source (Nosek et al. 2018) discusses pre-registration ...
- **Recurrence:** 1

### [F-104] Reference: Iyengar and Greenhouse (1988) appears in the reference list but is not cited in the text
- **Paper:** replication_crisis_2026 | **Run:** 002 | **Severity:** MINOR
- **Reference: Iyengar and Greenhouse (1988) appears in the reference list but is not cited in the text.** Remove or cite.
- **Recurrence:** 1

### [F-108] R ~ 1.0 for pre-registered studies is weakly sourced
- **Paper:** replication_crisis_2026 | **Run:** 003 | **Severity:** FRAMING
- **R ~ 1.0 for pre-registered studies is weakly sourced.** The table cites this as an "illustrative upper bound" with no empirical source. Pre-registration constrains hypothesis quality, but R = 1.0...
- **Recurrence:** 1

### [F-117] Reference formatting
- **Paper:** replication_crisis_2026 | **Run:** 003 | **Severity:** MINOR
- **Reference formatting.** Several references use inconsistent date-author formatting (e.g., "Ioannidis et al. 2011" in Table 1 source column but full citation not in References). Add all cited work...
- **Recurrence:** 1

### [F-130] The reference list omits Smaldino and McElreath (2016), "The natural selection o
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** MINOR
- The reference list omits Smaldino and McElreath (2016), "The natural selection of bad science," which models the evolutionary dynamics of publication bias and is directly relevant.
- **Recurrence:** 1

### [F-131] Figure references cannot be verified (figures are external images). The paper sh
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** MINOR
- Figure references cannot be verified (figures are external images). The paper should include figure descriptions sufficient for a referee to assess them from the text alone ΓÇö the captions provide...
- **Recurrence:** 1

### [F-136] The sensitivity analysis is vacuous
- **Paper:** REPLICATION_CRISIS_2026 | **Run:** 001 | **Severity:** FRAMING
- **The sensitivity analysis is vacuous.** The table confirms that an algebraic identity holds under parameter perturbation, which is tautological. A meaningful sensitivity analysis would examine how...
- **Recurrence:** 1

### [F-144] The Benjamini & Hochberg (1995) reference appears in the reference list but is n
- **Paper:** REPLICATION_CRISIS_2026 | **Run:** 001 | **Severity:** MINOR
- The Benjamini & Hochberg (1995) reference appears in the reference list but is never cited in the text.
- **Recurrence:** 1

### [F-145] Figure references cannot be evaluated because figures are external images. The r
- **Paper:** REPLICATION_CRISIS_2026 | **Run:** 001 | **Severity:** MINOR
- Figure references cannot be evaluated because figures are external images. The referee cannot verify Figures 1ΓÇô3.
- **Recurrence:** 1

## ASSEMBLY_ERROR

### [F-045] Sections 1 and 2 appear twice in the manuscript
- **Paper:** echo_chambers_v3_2026 | **Run:** 001 | **Severity:** STRUCTURAL
- **Sections 1 and 2 appear twice in the manuscript.** The paper contains a duplicate header block ΓÇö the full title, author line, and Sections 1ΓÇô2 appear to restart after the initial abstract. Th...
- **Recurrence:** 1

### [F-085] The Related Work section (Section 5) substantially duplicates the Introduction and Section 4.5 (Competing Models)
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** MINOR
- **The Related Work section (Section 5) substantially duplicates the Introduction and Section 4.5 (Competing Models).** Gelman & Carlin, p-curve, selection models, and replication markets are discus...
- **Recurrence:** 1

### [F-087] Figure code is included but figures are not rendered in the manuscript
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** MINOR
- **Figure code is included but figures are not rendered in the manuscript.** The paper includes Python code for three figures but references them as "[Figure 1: ...]" placeholders. For review, the f...
- **Recurrence:** 1

### [F-089] Figures are code blocks, not rendered figures
- **Paper:** replication_crisis_2026 | **Run:** 002 | **Severity:** STRUCTURAL
- **Figures are code blocks, not rendered figures.** Figures 1-3 are presented as Python source code with placeholder text ("[Figure 1: ...]"). A submitted manuscript must contain rendered figures. N...
- **Recurrence:** 2

## PROOF_STRATEGY_DRIFT

## FRAMING_OVERCLAIM

### [F-026] The paper's title uses "formal epistemological model" but the paper is closer to applied probability theory than to formal epistemology as practiced in philosophy
- **Paper:** CONSPIRACY_BAYES | **Run:** 002 | **Severity:** MINOR
- **The paper's title uses "formal epistemological model" but the paper is closer to applied probability theory than to formal epistemology as practiced in philosophy.** Consider whether the target a...
- **Recurrence:** 1

### [F-049] The Monte Carlo validation uses n=20 exclusively
- **Paper:** echo_chambers_v3_2026 | **Run:** 001 | **Severity:** FRAMING
- **The Monte Carlo validation uses n=20 exclusively.** While the analytical results are independent of n for aligned partitions, the validation should include at least one larger network (n=100 or n...
- **Recurrence:** 1

### [F-050] The planted-partition graph in Section 4.2 has "average degree 9.5" after symmetrization, which departs from d-regularity
- **Paper:** echo_chambers_v3_2026 | **Run:** 001 | **Severity:** FRAMING
- **The planted-partition graph in Section 4.2 has "average degree 9.5" after symmetrization, which departs from d-regularity.** The paper's entire theory assumes d-regular graphs, yet the planted-pa...
- **Recurrence:** 1

### [F-066] The connection to empirical echo chamber phenomena is asserted but never developed
- **Paper:** echo_chambers_v3_2026 | **Run:** 002 | **Severity:** FRAMING
- **The connection to empirical echo chamber phenomena is asserted but never developed.** The introduction cites Sunstein (2001), Pariser (2011), and Bail et al. (2018), but the paper never maps its ...
- **Recurrence:** 1

### [F-080] The discipline mapping presents point estimates without uncertainty
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** FRAMING
- **The discipline mapping presents point estimates without uncertainty.** Table 1 assigns single values of R, power, and phi to each field, yielding PPV values reported to three decimal places (e.g....
- **Recurrence:** 1

### [F-081] Section 4.1 ("Natural Enemy") understates Ioannidis's treatment of bias
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** FRAMING
- **Section 4.1 ("Natural Enemy") understates Ioannidis's treatment of bias.** The paper claims Ioannidis (2005) "treats publication as a binary filter" and did not isolate bias as a parameter. Ioann...
- **Recurrence:** 1

### [F-095] Policy claims exceed model scope
- **Paper:** replication_crisis_2026 | **Run:** 002 | **Severity:** FRAMING
- **Policy claims exceed model scope.** Section 7.1 states that reducing phi from 15 to 1.5 in social psychology "would raise PPV from 0.063 to 0.400." This is a conditional prediction from the model...
- **Recurrence:** 1

### [F-096] Related Work is redundant with Section 5
- **Paper:** replication_crisis_2026 | **Run:** 002 | **Severity:** FRAMING
- **Related Work is redundant with Section 5.** The Boundary Conditions section (5.1, 5.5) and Related Work section (6) cover substantially the same territory ΓÇö Ioannidis, selection models, Benjami...
- **Recurrence:** 1

### [F-107] The asymmetric weighting assumption (Definition 7) needs stronger justification
- **Paper:** replication_crisis_2026 | **Run:** 003 | **Severity:** FRAMING
- **The asymmetric weighting assumption (Definition 7) needs stronger justification.** The paper assigns weight 1 to true positives and weight phi to false positives, with the rationale that novelty ...
- **Recurrence:** 1

### [F-109] GWAS classification as "above threshold" is misleading given the field's actual practice
- **Paper:** replication_crisis_2026 | **Run:** 003 | **Severity:** FRAMING
- **GWAS classification as "above threshold" is misleading given the field's actual practice.** The paper notes in Section 4.2 that GWAS uses genome-wide significance (alpha ~ 5├ù10Γü╗Γü╕), which inc...
- **Recurrence:** 1

### [F-111] Section 7.3's back-calculation is presented as model validation but is not
- **Paper:** replication_crisis_2026 | **Run:** 003 | **Severity:** FRAMING
- **Section 7.3's back-calculation is presented as model validation but is not.** The calculation showing that PPV = 0.36, replication power = 0.92, and alpha = 0.05 yield a replication rate of 0.363...
- **Recurrence:** 1

### [F-123] The discipline mapping uses illustrative estimates but draws strong conclusions
- **Paper:** replication_crisis_2026 | **Run:** 001 | **Severity:** FRAMING
- **The discipline mapping uses illustrative estimates but draws strong conclusions.** The paper states phi estimates are "order-of-magnitude approximations" and "the least certain parameters in the ...
- **Recurrence:** 1

### [F-137] Proposition 0 does important but under-motivated work
- **Paper:** REPLICATION_CRISIS_2026 | **Run:** 001 | **Severity:** FRAMING
- **Proposition 0 does important but under-motivated work.** The proposition shows that a naive between-study publication filter cancels in PPV. This is a critical modeling assumption ΓÇö it justifie...
- **Recurrence:** 1

### [F-138] The paper does not engage with the fact that its model and Ioannidis's model make *different predictions*
- **Paper:** REPLICATION_CRISIS_2026 | **Run:** 001 | **Severity:** FRAMING
- **The paper does not engage with the fact that its model and Ioannidis's model make *different predictions*.** Because phi inflates only false positives while u inflates both pathways, the two mode...
- **Recurrence:** 1
