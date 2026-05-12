# INIT — ECHO CHAMBERS V2: POLARIZATION UNDER HETEROGENEOUS INFORMATION
# EXECUTE IMMEDIATELY. Do not summarize, analyze, or ask questions.
# Read the INPUTS below, then execute the SETUP SEQUENCE step by step.
# Load prompts/00_init.md for the setup procedure, then run it with these inputs.
# This is not a document to review — it is a set of instructions to follow NOW.

# Paper 2 of 3 in the Bayesian Epistemology Trilogy:
#   Paper 1: Conspiracy Beliefs as Bayesian Updating (conspiracy_bayes_2026) — COMPLETE
#   Paper 2: Echo Chambers under Heterogeneous Information (this paper)
#   Paper 3: Misinformation Persistence as Equilibrium (planned)
#
# V2 of echo chambers. V1 (3 runs) failed because:
#   1. The frozen spec promised a sharp phase transition that the math can't deliver
#   2. Under same-truth i.i.d. signals, even disconnected groups converge to same posterior
#   3. The linearization regime fails exactly where polarization would occur
#   4. "Unique mechanism" claims were tautological (only one lever in the model)
#
# V2 changes the core claim: polarization requires BOTH network disconnection AND
# heterogeneous information environments. The contribution is characterizing how
# topology AMPLIFIES information heterogeneity into stable polarization — not that
# topology alone causes polarization.

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Echo Chambers as Topology-Amplified Information Heterogeneity: A Bayesian Network Model
SLUG: echo_chambers_v2_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: Journal of Mathematical Sociology
PIPELINE: PAPER

PROBLEM:
Why do rational agents in the same society converge to opposing beliefs? This
paper proves that stable polarization requires two ingredients: (1) network
partition (low algebraic connectivity λ₂) AND (2) heterogeneous information
environments (different communities exposed to systematically different evidence).
Neither ingredient alone is sufficient:
- Partition without heterogeneity: disconnected groups receiving i.i.d. signals
  from the same truth converge to the same posterior asymptotically (no stable
  polarization — just transient divergence)
- Heterogeneity without partition: a connected network receiving heterogeneous
  signals converges to a weighted consensus (the network averages out the
  heterogeneity)
The paper's central result is an AMPLIFICATION THEOREM: network partition
amplifies small information heterogeneity into large belief divergence. The
steady-state belief gap between communities is proportional to the signal
heterogeneity δμ divided by the algebraic connectivity λ₂. When λ₂ → 0
(near-disconnection), even tiny δμ produces extreme polarization. When λ₂ is
large (well-connected), even large δμ is averaged out.

This extends Paper 1 (conspiracy_bayes_2026): Paper 1 proved that a single
agent in an opaque evidence environment converges to conspiracy belief. Paper 2
proves the network-level analog: communities in informationally segregated
environments converge to opposing beliefs, with the topology controlling
the amplification factor.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Network model
VALUE: Undirected graph G = (V, E) with n = |V| agents. Adjacency matrix A,
       degree matrix D, graph Laplacian L = D - A, normalized Laplacian.
       For d-regular graphs: row-stochastic weight matrix W = (1/d)A.
UNIT: graph-theoretic structure
TOLERANCE: exact — standard spectral graph theory
SOURCE: Chung 1997; Fiedler 1973; Godsil & Royle 2001
NOTES: Results derived for d-regular graphs. General graphs discussed as
       extension using normalized Laplacian. Self-loops excluded. Fixed
       network (no rewiring). Dynamic extension in Discussion only.
DRIFT_RISK: LOW — standard definitions

PARAMETER: Belief state vector
VALUE: θ(t) = (θ_1(t), ..., θ_n(t))^T where θ_i(t) is agent i's posterior
       probability at time t over binary hypothesis {H_true, H_false}.
UNIT: probability vector in [0,1]^n
TOLERANCE: exact
SOURCE: Standard Bayesian updating; extends Paper 1 notation
DRIFT_RISK: LOW

PARAMETER: Update rule (DeGroot-Bayesian hybrid)
VALUE: θ_i(t+1) = α · B(s_i(t+1), θ_i(t)) + (1-α) · (1/d_i) Σ_{j∈N(i)} θ_j(t)
       where B is the standard Bayesian update and α ∈ (0,1).
       Stage 1: Bayesian update on private signal. Stage 2: DeGroot averaging.
UNIT: probability
TOLERANCE: α explored parametrically. Global α (same for all agents).
SOURCE: DeGroot 1974; Jadbabaie et al. 2012; Golub & Jackson 2010
NOTES: When α = 1, reduces to Paper 1's isolated Bayesian agent.
       When α = 0, pure DeGroot (no private signals). The hybrid is essential.
DRIFT_RISK: HIGH — Author must maintain the two-stage hybrid. Pure DeGroot
             or pure Bayesian both miss the point.

PARAMETER: Heterogeneous signal model
VALUE: Agent i receives signal s_i(t) ~ N(μ_i, σ²) i.i.d. over time.
       μ_i depends on agent i's information environment:
       - Homogeneous case: μ_i = μ_true for all i (baseline, no polarization)
       - Heterogeneous case: μ_i = μ_true + δ_i where δ_i is a community-level
         bias. For a graph with two communities C_1, C_2:
         δ_i = +δμ/2 for i ∈ C_1, δ_i = -δμ/2 for i ∈ C_2
       δμ = 0 reduces to homogeneous. δμ > 0 models information heterogeneity.
UNIT: real-valued signals
TOLERANCE: σ² and δμ explored parametrically
SOURCE: Novel formalization. Empirically motivated: different communities
        ARE exposed to systematically different evidence (media ecosystems,
        geographic information access, institutional context).
NOTES: THIS IS THE KEY MODELING CHOICE THAT V1 GOT WRONG. V1 used a single
       μ_true for all agents and then couldn't prove stable polarization.
       V2 models heterogeneous information environments explicitly.
       The question becomes: how does topology interact with heterogeneity?
       IMPORTANT: δ_i is NOT a bias in the agent's likelihood model (that
       would be misspecification as in Paper 1). δ_i reflects genuine
       differences in the evidence different communities observe. A rural
       community and an urban community literally see different data about
       the same policy question. This is a feature of the information
       environment, not a failure of rationality.
DRIFT_RISK: CRITICAL — Author MUST clearly distinguish between:
  (a) homogeneous signals (μ_i = μ_true for all i) — baseline, no stable polarization
  (b) heterogeneous signals (μ_i varies by community) — stable polarization possible
  The main results must prove BOTH cases and characterize the transition.
  Do NOT assume heterogeneity and then claim polarization "emerges" — that's
  circular (different evidence in → different beliefs out). The contribution
  is the AMPLIFICATION: topology controls HOW MUCH heterogeneity translates
  to belief divergence.

PARAMETER: Steady-state belief variance V_ss
VALUE: V_ss = Σ_{k=2}^{n} v_k / (1 - ν_k²) where ν_k are eigenvalues of
       the update operator M = (1-α)W and v_k are signal-variance projections
       onto the k-th eigenvector of W.
UNIT: variance (squared posterior units)
TOLERANCE: exact derivation from spectral decomposition
SOURCE: Novel — derived in this paper via linearized analysis
NOTES: This is the paper's primary QUANTITATIVE contribution. V_ss measures
       consensus quality. Low V_ss = tight consensus. High V_ss = noisy/dispersed.
       Under homogeneous signals, V_ss → 0 as t → ∞ (consensus). Under
       heterogeneous signals, V_ss converges to a positive steady state
       proportional to δμ² / λ₂. THIS is the amplification result.
       IMPORTANT: V_ss is derived under linearization (posteriors near θ̄).
       The formula is quantitatively accurate when SNR is moderate.
       For extreme posteriors, provide Monte Carlo validation.
DRIFT_RISK: MEDIUM — Author must derive V_ss completely (all steps shown).
             V1 Run 3 had proofs absent — UNACCEPTABLE. Every step must
             be present.

PARAMETER: Amplification factor
VALUE: A(G) = δμ² / λ₂ — the steady-state belief gap between communities
       is proportional to the signal heterogeneity δμ divided by the
       algebraic connectivity λ₂.
UNIT: dimensionless ratio
TOLERANCE: exact under linearization; validated by Monte Carlo
SOURCE: Novel — this paper's central theorem
NOTES: THIS is the main result. Not a phase transition. Not a sharp threshold.
       A smooth amplification factor that quantifies how much topology
       magnifies information heterogeneity into belief divergence.
       - High λ₂ (well-connected): amplification is small, heterogeneity
         is averaged out, near-consensus
       - Low λ₂ (poorly connected): amplification is large, small δμ
         produces large belief gaps
       - λ₂ = 0 (disconnected): amplification is infinite, any δμ > 0
         produces maximum polarization
       The "effective threshold" λ₂*(ε) where A(G) > ε is a practical
       heuristic, NOT a phase boundary. Present it as such.
DRIFT_RISK: CRITICAL — Author MUST NOT frame this as a phase transition.
  It is a smooth function. The contribution is the functional form
  A(G) = δμ²/λ₂, not a sharp threshold. Do NOT overclaim.

PARAMETER: Connection to Paper 1
VALUE: When n=1 and α=1, the model reduces to Paper 1's sequential Bayesian
       updating. The heterogeneous signal δ_i for an isolated agent corresponds
       to Paper 1's "secrecy-rich environment" (μ > 0). Network partition is
       the collective analog of individual opacity.
UNIT: N/A (theoretical connection)
TOLERANCE: exact reduction — must be proven as a lemma
SOURCE: conspiracy_bayes_2026 (Paper 1)
NOTES: Keep Lemma 1 (n=1 reduction) brief — one paragraph proof, not a page.
       The conceptual connection (partition = collective opacity) is an analogy,
       not a theorem. Do not overclaim the correspondence.
DRIFT_RISK: MEDIUM — the analogy is imperfect. Paper 1's opacity drives
  convergence to a WRONG belief. Paper 2's partition amplifies DIFFERENT
  evidence into different beliefs. These are qualitatively different.
  Acknowledge the disanalogy honestly.

MILESTONES:

M1: Network model + belief dynamics — Define G, L, W, belief state vector θ(t),
    the DeGroot-Bayesian hybrid update rule, BOTH signal models (homogeneous
    and heterogeneous). Matrix form: θ(t+1) = α·B(s(t+1),θ(t)) + (1-α)·W·θ(t).
    Prove Lemma 1: n=1 reduction to Paper 1 (brief — one paragraph proof).
    Define V_ss, consensus, and polarization formally. Introduction positions
    the paper as characterizing the INTERACTION between topology and information
    heterogeneity — NOT topology alone causing polarization.

M2: Core theorems — Prove THREE results:
    Theorem 1 (Consensus under homogeneity): If G connected and signals
    homogeneous (δμ=0), all agents converge to θ* regardless of initial
    conditions. Rate exponential in λ₂. V_ss → 0.
    Theorem 2 (Amplification under heterogeneity): If signals heterogeneous
    (δμ>0), steady-state belief gap between communities proportional to
    δμ²/λ₂. Derive V_ss formula with ALL steps shown.
    Theorem 3 (Disconnection): If G disconnected (λ₂=0) with heterogeneous
    signals, communities converge to distinct posteriors. Gap = δμ·f(α,σ²).
    Corollary: The effective threshold λ₂*(ε) = δμ²/ε is a practical
    heuristic (NOT a phase boundary — state this explicitly).
    COMPLETE PROOFS REQUIRED — no tombstone-only theorems.

M3: Application + boundary conditions — Worked numerical example comparing
    V_ss formula to Monte Carlo simulation across range of SNR and θ̄ values
    (validates linearization). Natural enemy: Golub & Jackson 2010 (consensus
    without private signals — different model, different result, explain why).
    Sensitivity analysis table. Competing models (pure DeGroot, pure Bayesian,
    bounded confidence). Limitations: fixed network, linearization regime,
    exogenous signals. Open problems: dynamic networks, endogenous signal
    selection, strategic agents.

M4: Full paper — Abstract (last), Introduction, Related Work (consolidated —
    NO duplication between Intro and Related Work), Core Results, Application,
    Boundary Conditions, Discussion (implications for understanding echo
    chambers — NOT platform design recommendations, which the model doesn't
    support), Conclusion, References. Figures with Python code.
    FIGURES MUST MATCH THE MODEL — if showing polarization, use heterogeneous
    signals. Do not show different μ_true per component unless the model
    specifies it.

ORACLE:
The model is valid if and only if:
1. Network model formally defined with spectral properties
2. DeGroot-Bayesian hybrid update precisely specified as two-stage process
3. BOTH homogeneous and heterogeneous signal models defined and distinguished
4. Consensus under homogeneity proven with convergence rate (Theorem 1)
5. Amplification factor A(G) = δμ²/λ₂ derived with complete proof (Theorem 2)
6. V_ss formula derived with ALL steps shown (no proof-free theorems)
7. Disconnection result proven with explicit gap formula (Theorem 3)
8. Monte Carlo validation of V_ss formula beyond linearization regime
9. Reduction to Paper 1 proven as brief lemma
10. NO phase transition language — amplification, not threshold
11. Figures consistent with stated signal model

Peer Reviewer must verify: Are complete proofs present for all theorems?
If any theorem has a tombstone with no proof body, REJECT.
Does the paper claim a phase transition or sharp threshold? If yes, REJECT.
Is the amplification factor derived or merely asserted? If asserted, REJECT.


# === STEELMAN REVISION BRIEF (from run 1) ===
# The next run MUST address every item.
# STRUCTURAL ISSUES:
1. **Theorem 2 proof has a dimensional inconsistency in the amplification factor.** The paper claims the amplification factor is A(G) = ╬┤_╬╝┬▓ / ╬╗Γéé, but the proof in Step 6 shows the belief *gap* scales as ╬ö_ss ~ ╬┤_╬╝ / (╬▒ + (1-╬▒)╬╗Γéé/d), which is linear in ╬┤_╬╝, not quadratic. The *variance* scales as ╬┤_╬╝┬▓ / ╬╗Γéé, but A(G) is described interchangeably as governing both the gap and the variance throughout the paper (Abstract: "steady-state belief gap between communities is governed by the amplification factor"; Theorem 2(iii): "dominant Fiedler contribution gives ╬ö_ss ~ ╬┤_╬╝ / ╬╗Γéé ... and the amplification factor is A(G) = ╬┤_╬╝┬▓ / ╬╗Γéé"). The gap is proportional to ╬┤_╬╝ / ╬╗Γéé; the variance is proportional to ╬┤_╬╝┬▓ / ╬╗Γéé. Pick one quantity for A(G) and use it consistently, or define two distinct measures.
2. **The linearized update equation in Section 2.2 conflates signal mean and hypothesis likelihood.** Definition 7 sets up the Bayesian update with ╧å(s|H_true) = N(s; ╬╝_i, ╧â┬▓), making the true-hypothesis likelihood *community-dependent*. This means agent i's likelihood function is correctly specified only if H_true implies the agent's local signal mean ╬╝_i. But under the binary hypothesis {H_true, H_false}, H_true is a single state of the world ΓÇö it cannot simultaneously imply different signal means for different agents unless you explicitly model the hypothesis space as including community-specific parameters. The paper never addresses this. As written, heterogeneous agents are not updating on the same hypothesis, which undermines the "rational agents disagreeing" framing. This needs either a reformulation (e.g., H_true implies a world-state, and community membership determines the observation channel) or explicit acknowledgment that agents have correctly-specified but community-specific likelihood functions.
3. **Monte Carlo validation is insufficiently reported.** The paper claims "linearized formula matches Monte Carlo within 10% for moderate ╬┤_╬╝" but provides no formal error metric, no confidence intervals, no table of numerical values. The validation is described in prose and delegated to a figure. For a paper whose central contribution is a formula, the validation must include a table with point estimates, standard errors, and percentage deviations across the parameter grid. The code is provided, which is commendable, but the results are not reported with the rigor expected at JMS.
# REVISION INSTRUCTIONS:
1. **Resolve the gap vs. variance inconsistency (Structural Issue 1).** Define A(G) as governing exactly one quantity ΓÇö either the belief gap (linear in ╬┤_╬╝) or the variance (quadratic in ╬┤_╬╝). Update the abstract, introduction, theorems, summary table, and corollary to use the chosen definition consistently. If you define A(G) for variance, introduce a separate symbol for the gap scaling.
2. **Fix the likelihood specification for heterogeneous agents (Structural Issue 2).** Explicitly model the observation channel: state that H_true implies a world-state, each agent's community membership determines a known observation function, and each agent's likelihood is correctly specified for their own channel. This preserves the "rational agents" claim. Alternatively, reframe as agents with community-specific models who are each internally consistent.
3. **Add a numerical validation table (Structural Issue 3).** For each (╬┤_╬╝, ╬╗Γéé) pair in the simulation, report: Monte Carlo mean ┬▒ standard error, analytical prediction, absolute error, and relative error. This table should appear in the main text, not a supplement.
4. **Foreground the control-theory relationship (Framing Issue 1).** In the introduction, after stating the amplification factor, add a paragraph acknowledging that the spectral structure (bias ~ forcing/spectral-gap) is known in multi-agent control theory, and clearly state what this paper adds: the Bayesian-DeGroot hybrid, the information-heterogeneity interpretation, and the connection to the echo chamber literature.
5. **Reframe agent rationality (Framing Issue 2).** Replace "rational agents" with "agents who are Bayesian with respect to private signals and use DeGroot averaging for network information." In Section 4.2, acknowledge that the hybrid rule is a heuristic approximation to full network Bayesian inference, and note that fully Bayesian network learning would require agents to infer the entire signal history of the network.
6. **Address the d-regular restriction (Framing Issue 3).** Either (a) prove the main results for general graphs using the normalized Laplacian, or (b) verify numerically that the barbell graph simulation (which is not d-regular) matches the d-regular theoretical predictions and explain why the approximation works. Acknowledge the gap explicitly.
7. **Discuss Fiedler-community misalignment (Framing Issue 4).** Add a paragraph or subsection analyzing what happens when the community partition is not perfectly aligned with the Fiedler vector. Derive or bound the reduction in amplification as a function of the angle between the bias vector ╬┤ and the Fiedler vector ╧åΓéé.
8. **Fix minor issues 1ΓÇô10** as listed above. In particular: remove the magic constant 0.002, clarify what ╬╡ measures in Corollary 1, fix seed collisions in the simulation code, and verify the Barber├í citation.

KNOWN_DRIFT_RISKS:
- CRITICAL: Framing amplification as a phase transition. The Steelman
  caught this THREE TIMES in V1. There is no sharp threshold. The
  amplification A(G) = δμ²/λ₂ is a smooth function. The "effective
  threshold" λ₂*(ε) is a modeling convention, not a phase boundary.
  ANY language about "critical threshold below which consensus fails"
  is WRONG and must be REJECTED.
- CRITICAL: Proving polarization under homogeneous signals. V1 Run 2's
  Steelman proved this is IMPOSSIBLE — under i.i.d. same-truth signals,
  even disconnected groups converge to the same posterior asymptotically.
  Stable polarization requires heterogeneous information. Do NOT claim
  topology alone causes polarization.
- CRITICAL: Absent proofs. V1 Run 3 had theorems with tombstones but no
  proof bodies. EVERY theorem must have a complete proof with all steps.
  If the Author writes "Proof. ∎" with nothing in between, the Peer
  Reviewer MUST REJECT.
- HIGH: Circular polarization argument. If polarization requires
  heterogeneous signals as an assumption, the Author cannot claim
  polarization "emerges" from the model. The contribution is the
  AMPLIFICATION FACTOR — how much topology magnifies heterogeneity —
  not the existence of polarization itself.
- HIGH: Linearization regime. V_ss formula valid only near θ̄ ≈ 0.5.
  Must provide explicit validity bounds AND Monte Carlo validation
  showing error across full posterior range. Do not hand-wave about
  ergodic or contraction arguments without proving them.
- HIGH: "Unique mechanism" claims. The model has one structural lever
  (edge set). Claiming reconnection is the "unique" mechanism for
  reducing polarization is tautological. Either define a class of
  interventions and prove uniqueness relative to that class, or drop
  the claim.
- MEDIUM: Overclaiming policy implications. The model has fixed networks,
  exogenous signals, rational agents. Real platforms have none of these.
  Platform design implications are conjectures, not theorems. Label them
  as such.
- MEDIUM: Overstating the Paper 1 analogy. Paper 1's opacity drives
  convergence to a WRONG belief. Paper 2's partition amplifies DIFFERENT
  evidence. These are qualitatively different phenomena. The analogy
  (partition = collective opacity) is suggestive, not exact.
- MEDIUM: Notation consistency. Use θ_true throughout (not μ_true).
  Use global α (not agent-specific α_i) unless proving agent-specific results.
- LOW: Redundant literature review. Consolidate positioning in Related
  Work section. Introduction states contributions, Related Work does
  detailed comparison. No duplication.
- PROOF STRATEGY: V_ss derivation must use spectral decomposition of
  the update operator M = (1-α)W. Express deviation θ(t) - θ̄ in
  eigenbasis of W. Each component evolves as AR(1) with coefficient ν_k.
  V_ss = Σ v_k/(1-ν_k²). Under heterogeneity, the mean signal vector
  has non-zero projection onto the Fiedler vector, creating a persistent
  bias term proportional to δμ/λ₂.
- PROOF STRATEGY: Amplification theorem uses the Fiedler vector to
  decompose the heterogeneity. The community-level signal bias δ_i
  projects onto the Fiedler vector (by construction — the Fiedler vector
  identifies the partition). The λ₂ eigenvalue controls how quickly this
  component is averaged out. Low λ₂ = slow averaging = large steady-state
  gap. This is the mathematical mechanism.

---

## SETUP SEQUENCE — EXECUTE NOW

Load prompts/00_init.md and execute the setup procedure with the INPUTS above.
Use SLUG echo_chambers_v2_2026 for all directory names and references.

## HAND OFF — EXECUTE PAPER PIPELINE

DO NOT STOP AFTER SCAFFOLDING. DO NOT ASK FOR PERMISSION. DO NOT ASK IF THE
USER WANTS TO PROCEED. DO NOT SUMMARIZE WHAT YOU DID.

After scaffolding is complete, IMMEDIATELY:
1. Read prompts/04_paper_orchestrator.md in the new project directory
2. Begin M1 — Author mode, write the Definitions Block and Introduction
3. Continue through M2, M3, M4 until paper.md is written
4. This is a single continuous execution — scaffold then write the paper

YOUR INPUTS FOR THE PIPELINE:
  PROBLEM: [the full PROBLEM text from the INPUTS section above]
  DATA: No empirical data. All results derived analytically.
  SLUG: echo_chambers_v2_2026
  DRIFT_RISKS: [paste from KNOWN_DRIFT_RISKS above]
  FROZEN_SPEC: [full contents of frozen_spec.md in the project directory]

YOU ARE THE ORCHESTRATOR. EXECUTE THE PIPELINE NOW.

