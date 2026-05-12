# INIT — ECHO CHAMBERS V3: VALIDATED AMPLIFICATION MODEL
# EXECUTE IMMEDIATELY. Do not summarize, analyze, or ask questions.
# Read the INPUTS below, then execute the SETUP SEQUENCE step by step.
# Load prompts/00_init.md for the setup procedure, then run it with these inputs.
# This is not a document to review — it is a set of instructions to follow NOW.

# Paper 2 of 3 in the Bayesian Epistemology Trilogy.
#   Paper 1: Conspiracy Beliefs as Bayesian Updating (conspiracy_bayes_2026) — COMPLETE
#   Paper 2: Echo Chambers — Validated Amplification Model (this paper)
#   Paper 3: Misinformation Persistence as Equilibrium (planned)
#
# V3. Prior versions failed because:
#   V1 (3 runs): Promised phase transition math can't deliver. Same-truth signals
#     can't produce stable polarization. Proofs absent in Run 3.
#   V2 (3 runs): Validation table EMPTY every run. Monte Carlo used mean-field
#     proxy instead of actual graph adjacency. Proof gap in gap formula derivation.
#     Novelty overclaimed vs control theory. Trilogy framing premature.
#
# V3 changes:
#   1. M3 MUST execute simulation code and write actual numbers into the paper
#   2. Monte Carlo MUST use explicit adjacency matrix — ban mean-field proxy
#   3. Fiedler-to-community mapping MUST be a proved lemma, not a hand-wave
#   4. Friedkin-Johnsen connection developed (not dismissed in one sentence)
#   5. Trilogy framing reduced to a remark
#   6. "Not a phase transition" stated twice max, not six times
#   7. Simulation code in appendix, not body

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Echo Chambers as Topology-Amplified Information Heterogeneity
SLUG: echo_chambers_v3_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: Journal of Mathematical Sociology
PIPELINE: PAPER

PROBLEM:
Why do communities of agents — each updating rationally on private evidence —
converge to opposing beliefs? This paper proves that stable polarization requires
two ingredients: network partition (low algebraic connectivity) AND heterogeneous
information environments (different communities exposed to different evidence).
The central result is an amplification factor A_V proportional to delta_mu^2 /
(1-nu_2)^2, quantifying how topology magnifies information heterogeneity into
belief divergence. This is a smooth function — not a phase transition.

The mathematical structure (forcing/spectral-gap) is known from multi-agent
control theory (Olfati-Saber et al. 2007; Ren & Beard 2005). This paper
contributes: (a) a DeGroot-Bayesian hybrid model connecting the spectral
mechanism to the social learning and echo chamber literatures, (b) three
theorems characterizing the consensus-polarization continuum, (c) the explicit
connection to Friedkin-Johnsen (1990) stubbornness models showing the Bayesian
micro-foundation as the contribution, and (d) Monte Carlo validation on
explicit graph structures demonstrating where the linearized formulas hold
and where they break down.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Network model
VALUE: Undirected d-regular graph G = (V, E), n = |V| agents. Weight matrix
       W = (1/d)A. Graph Laplacian L = D - A. Results for d-regular; general
       graphs discussed via normalized Laplacian.
UNIT: graph-theoretic structure
TOLERANCE: exact
SOURCE: Chung 1997; Fiedler 1973
DRIFT_RISK: LOW

PARAMETER: Update rule (DeGroot-Bayesian hybrid)
VALUE: theta_i(t+1) = alpha * B(s_i(t+1), theta_i(t)) + (1-alpha) * (1/d) * sum_{j in N(i)} theta_j(t)
       Stage 1: Bayesian update on private signal. Stage 2: DeGroot averaging.
       alpha in (0,1). Global alpha for all agents.
UNIT: probability
SOURCE: DeGroot 1974; Jadbabaie et al. 2012 (non-Bayesian social learning)
NOTES: This is a heuristic approximation to full Bayesian network inference.
       Agents are Bayesian w.r.t. private signals, use DeGroot averaging for
       network information. NOT "rational agents" — describe precisely.
DRIFT_RISK: HIGH — must maintain two-stage hybrid. Must NOT call agents
  "rational" without qualification.

PARAMETER: Heterogeneous signal model
VALUE: s_i(t) ~ N(mu_true + delta_i, sigma^2) i.i.d. over time.
       delta_i = +delta_mu/2 for i in C_1, delta_i = -delta_mu/2 for i in C_2.
       Homogeneous case: delta_mu = 0. Heterogeneous: delta_mu > 0.
UNIT: real-valued signals
SOURCE: Novel formalization of community-specific information environments.
NOTES: Each agent's likelihood correctly specified for their own channel.
       This is a modeling assumption — state explicitly.
DRIFT_RISK: CRITICAL — do NOT claim polarization "emerges" from topology
  alone. Both topology AND heterogeneity required.

PARAMETER: Linearized dynamics
VALUE: x(t+1) = (1-alpha)*W*x(t) + alpha*gamma*epsilon(t+1) + alpha*gamma*delta
       gamma = (mu_true - mu_false)/sigma^2 (common base gain)
       Assumption: delta_mu << |mu_true - mu_false| (heterogeneity small
       relative to signal-hypothesis separation). State as formal assumption.
UNIT: deviation from theta_bar
SOURCE: Standard linearization of Bayesian update
NOTES: Linearization valid when beliefs moderate (near theta_bar ~ 0.5).
       Invalid for extreme beliefs — must validate with Monte Carlo.
DRIFT_RISK: HIGH — must state validity condition as formal assumption,
  not bury it in a definition.

PARAMETER: Steady-state belief variance
VALUE: V_ss = (1/n) * sum_{k=2}^{n} E[a_k^2]
       V_ss^{hom} = (1/n) * sum_{k=2}^{n} alpha^2*gamma^2*sigma^2 / (1-nu_k^2)
       V_ss^{excess} = (1/n) * sum_{k=2}^{n} alpha^2*gamma^2*delta_k^2 / (1-nu_k)^2
       NOTE: denominator is (1-nu_k)^2 for excess (squared bias),
             (1-nu_k^2) for noise. These are different.
UNIT: variance
SOURCE: Derived via spectral decomposition
NOTES: Sum starts at k=2 (k=1 is mean component, not disagreement).
       1/n factor required per definition (average over agents).
DRIFT_RISK: CRITICAL — V1 and V2 both had denominator errors.
  (1-nu_k)^2 for excess, (1-nu_k^2) for noise. Get this right.

PARAMETER: Amplification factor
VALUE: A_V(G) = V_ss^{excess} / (alpha^2 * gamma^2 * sigma^2)
       For aligned partition: A_V = delta_mu^2 / [4*sigma^2*(1-nu_2)^2]
       Well-connected regime: A_V ~ delta_mu^2 * d^2 / [4*sigma^2*(1-alpha)^2*lambda_2^2]
       SCALING IS lambda_2^{-2} for variance, lambda_2^{-1} for gap.
UNIT: dimensionless ratio
SOURCE: Derived in this paper
NOTES: One consistent definition throughout. Do NOT redefine mid-paper.
DRIFT_RISK: CRITICAL — V2 Run 1 caught inconsistent definition between
  Definition and Theorem. Use ONE definition. The denominator is the
  per-agent signal innovation variance, not the Fiedler noise component.

PARAMETER: Friedkin-Johnsen connection
VALUE: The DeGroot-Bayesian hybrid steady state is mathematically isomorphic
       to the Friedkin-Johnsen (1990) model with stubbornness. In F-J, agents
       anchor to an exogenous "prejudice" while averaging with neighbors.
       The Bayesian micro-foundation gives the prejudice an informational
       interpretation (it comes from private signals, not psychological
       stubbornness). THIS is the contribution over F-J.
UNIT: N/A (theoretical connection)
SOURCE: Friedkin & Johnsen 1990; Ghaderi & Srikant 2014
NOTES: Do NOT dismiss F-J in one sentence. Develop the connection.
       Show the mathematical correspondence, then articulate what the
       Bayesian micro-foundation adds.
DRIFT_RISK: HIGH — V2 Run 3 Steelman flagged underdeveloped F-J connection.
  Must be a full subsection in Related Work.

PARAMETER: Monte Carlo validation requirements
VALUE: Must use EXPLICIT adjacency matrix. Construct the graph. Use actual
       neighbor sets in the update rule. NO mean-field community-average proxy.
       Report: Monte Carlo mean, standard error, analytical prediction,
       relative error for each (b, delta_mu) combination.
       MUST include a d-regular validation (random d-regular graph with
       planted partition) to isolate linearization error from regularity error.
UNIT: N/A (methodology)
SOURCE: N/A
NOTES: V2 ALL THREE RUNS had empty validation tables with placeholder
       values "[from code execution]". THIS IS THE MOST CRITICAL V3 FIX.
       The Author MUST write the simulation code, EXECUTE IT within the
       Claude session, capture the output, and WRITE THE ACTUAL NUMBERS
       into the validation table. If the code cannot be executed in the
       session, provide a complete self-contained script AND manually
       compute at least 3 representative data points using basic arithmetic
       to populate the table.
DRIFT_RISK: CRITICAL — if the validation table has placeholders, the
  Peer Reviewer MUST REJECT. No exceptions.

MILESTONES:

M1: Definitions + Introduction. Define graph, update rule, signal model,
    linearized dynamics, V_ss (with correct denominators), A_V (one
    definition). Introduction: honest about control-theory precedent
    (paragraph 2, not buried). State contribution: modeling framework +
    three theorems + F-J connection + validation. Lemma 1 (Paper 1
    reduction) as a brief remark, not a full lemma. "Not a phase
    transition" — state once in introduction, once in Theorem 2 discussion.
    No more. Linearization validity as formal Assumption 1.

M2: Core proofs. Theorem 1 (consensus under homogeneity), Theorem 2
    (amplification under heterogeneity — with complete proof including
    Fiedler-to-community-average mapping as an explicit Lemma 2, not
    hand-waved), Theorem 3 (disconnection). Corollary 1 as Remark
    (practical heuristic, not a formal corollary). COMPLETE PROOFS
    REQUIRED — no tombstone-only theorems, no stream-of-consciousness,
    no "Wait — let me recompute."

M3: Application + Boundary Conditions. CRITICAL: The Author MUST:
    (a) Write Python simulation code using EXPLICIT adjacency matrix
    (b) EXECUTE the code or compute representative values manually
    (c) POPULATE the validation table with ACTUAL NUMBERS
    (d) Include a d-regular validation (planted partition graph)
    If the validation table has "[from code execution]" or any placeholder,
    the Peer Reviewer MUST REJECT IMMEDIATELY.
    Also: natural enemy (Golub-Jackson), sensitivity analysis, competing
    models (including Friedkin-Johnsen with explicit comparison), boundary
    conditions, open problems.

M4: Full paper assembly. Abstract (~150 words, no heavy notation).
    Related Work: develop F-J connection as full subsection. Discussion:
    fold "what model doesn't say" into prose naturally — no defensive
    numbered list. Conclusion: no policy recommendations that Discussion
    already disclaimed. Simulation code in appendix section, not in body.
    Trilogy framing: one remark about Paper 1 connection, no "Paper 3
    planned" references.

ORACLE:
1. Complete proofs for all theorems (no tombstones without proof bodies)
2. Fiedler-to-community mapping proved as explicit Lemma 2
3. V_ss denominators correct: (1-nu_k)^2 for excess, (1-nu_k^2) for noise
4. A_V defined ONCE and used consistently
5. Validation table populated with ACTUAL NUMBERS (not placeholders)
6. Monte Carlo uses explicit adjacency matrix (not mean-field proxy)
7. d-regular validation included alongside barbell validation
8. Linearization validity stated as formal Assumption 1
9. Friedkin-Johnsen connection developed as full subsection
10. "Not a phase transition" stated maximum 2 times
11. No "rational agents" — describe the update rule precisely
12. Trilogy framing minimal (remark only)

Peer Reviewer: If validation table has ANY placeholder text, REJECT.
If proofs end with tombstone and no body, REJECT.
If A_V is defined differently in two places, REJECT.

KNOWN_DRIFT_RISKS:
- CRITICAL: Empty validation tables. V2 Runs 1, 2, and 3 ALL had
  placeholder values. The Author generates code but doesn't run it.
  If the Author writes "[from code execution]" or similar, REJECT.
  The Author must either execute the code or manually compute values.
- CRITICAL: Mean-field Monte Carlo. V2 Run 1 Steelman caught that the
  simulation used community-average proxy instead of actual graph
  adjacency. Must construct explicit adjacency matrix and use actual
  neighbor sets in the update.
- CRITICAL: Denominator confusion. (1-nu_k)^2 for excess variance
  (squared bias from forcing). (1-nu_k^2) for noise variance (AR(1)
  variance). These are mathematically different. V2 Run 1 got this wrong.
- CRITICAL: A_V redefinition. V2 Run 1 defined A_V as one ratio in
  Definition 15 and a different ratio in Theorem 2. ONE definition.
- HIGH: Proof gap in gap formula. V2 Run 2 Steelman caught that
  Theorem 2(vi) hand-waves the Fiedler-to-community mapping. Prove
  it as Lemma 2 with explicit computation.
- HIGH: Friedkin-Johnsen dismissal. V2 Run 3 Steelman flagged one-sentence
  dismissal. Must develop the mathematical correspondence and articulate
  what Bayesian micro-foundation adds.
- HIGH: "Not a phase transition" overstatement. V2 Run 3 counted six
  instances. Maximum two.
- HIGH: Overclaimed novelty. The spectral mechanism is known from
  control theory. State this upfront. Contribution is the modeling
  framework and its connection to echo chamber literature.
- MEDIUM: Trilogy framing. V2 Run 3 Steelman called it "premature and
  self-promotional." Reduce to a remark about Paper 1 connection.
- MEDIUM: "Rational agents" label. Agents use a heuristic (DeGroot
  averaging), not full Bayesian network inference. Describe precisely.
- MEDIUM: Simulation code in paper body. Move to appendix section.
- LOW: Corollary 1 labeled as corollary but described as heuristic.
  Make it a Remark instead.
- PROOF STRATEGY: V_ss via spectral decomposition of M = (1-alpha)W.
  Each component is AR(1). Noise variance = alpha^2*gamma^2*sigma^2/(1-nu_k^2).
  Bias from forcing = alpha^2*gamma^2*delta_k^2/(1-nu_k)^2.
  The Fiedler component dominates because (1-nu_2) is smallest.
- PROOF STRATEGY: Lemma 2 (Fiedler-community mapping) — for balanced
  partition {C_1,C_2} with |C_1|=|C_2|=n/2, Fiedler vector phi_2 has
  [phi_2]_i = +1/sqrt(n) for i in C_1, -1/sqrt(n) for i in C_2.
  Community average of phi_2 over C_1 = 1/sqrt(n). Bias projection
  delta_2 = sqrt(n)*delta_mu/2. PROVE THIS EXPLICITLY.

---

## SETUP SEQUENCE — EXECUTE NOW

Load prompts/00_init.md and execute the setup procedure with the INPUTS above.
Use SLUG echo_chambers_v3_2026 for all directory names and references.

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
  DATA: No empirical data. All results derived analytically + Monte Carlo validation.
  SLUG: echo_chambers_v3_2026
  DRIFT_RISKS: [paste from KNOWN_DRIFT_RISKS above]
  FROZEN_SPEC: [full contents of frozen_spec.md in the project directory]

YOU ARE THE ORCHESTRATOR. EXECUTE THE PIPELINE NOW.
