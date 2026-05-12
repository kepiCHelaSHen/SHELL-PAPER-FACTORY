# INIT — THE SUNK COST FALLACY IS NOT ALWAYS A FALLACY (v2)
# EXECUTE IMMEDIATELY. Do not summarize, analyze, or ask questions.
# Read the INPUTS below, then execute the SETUP SEQUENCE step by step.
# Load prompts/00_init.md for the setup procedure, then run it with these inputs.
# This is not a document to review — it is a set of instructions to follow NOW.
# Incorporates all steelman review feedback from v1.

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: When Sunk Costs Carry Signals: A Bayesian Rationalization
SLUG: sunk_cost_v2_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: Theory and Decision
PIPELINE: PAPER

PROBLEM:
Proves that sunk cost behavior can be rational when sunk costs carry information
about investment quality. If initial investment was based on a private signal
about project quality, then sunk cost size correlates with posterior belief.
Derives conditions where "throwing good money after bad" is Bayesian-optimal.
Calculates the exact threshold where genuinely irrational sunk cost behavior
begins, and quantifies the decision error probability from ignoring sunk costs.

The paper is formal Bayesian decision theory. The rationality result must be
a theorem, not an illustration. The signal model must be rigorous: agent
receives noisy signal, invests proportional to posterior expectation, and sunk
cost becomes informationally equivalent to the posterior via invertibility of
the investment function. The irrationality threshold must be derived in closed
form — the exact boundary where attending to sunk costs transitions from
Bayesian-optimal to genuinely fallacious. The paper must also derive how the
information value of sunk costs decays as the agent receives additional signals
between the initial investment and the continuation decision.

The contribution is primarily a FRAMING result — the algebra is straightforward
(function inversion under monotonicity), but the insight is in the precise
identification of conditions under which sunk cost attention is rational and the
threshold separating rational from irrational attention. The paper should be
honest about this: do not oversell the technical depth and do not import
heavyweight statistical machinery to describe simple algebraic facts.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Bayesian updating
VALUE: Standard Bayesian updating — agent has prior pi(theta), receives signal
       s ~ f(s|theta), forms posterior pi(theta|s) via Bayes' theorem
UNIT: probability distribution
TOLERANCE: exact — standard Bayesian framework
SOURCE: Bayes' theorem — foundational
NOTES: The framework is standard. The novelty is in what it implies about
       sunk costs when the signal model is specified correctly.
DRIFT_RISK: LOW — standard framework

PARAMETER: Signal model
VALUE: Agent receives noisy signal s about project quality theta in [0,1].
       Signal density f(s|theta) satisfies MLRP. Prior pi(theta) has full
       support on [0,1] (required for strict monotonicity of mu(s) in s).
       E[theta|s] = mu(s) is strictly increasing in s. Agent invests
       I = g(mu(s)) where g is strictly increasing and continuous.
UNIT: signal realization
TOLERANCE: g must be strictly increasing and continuous; specific functional
           form (linear, etc.) used for closed-form results but main theorems
           hold generally. MLRP plus full-support prior required for strict
           monotonicity of mu(s) — state this regularity condition explicitly.
SOURCE: Novel formalization — Rice [this paper]
NOTES: This is the key insight: because investment I was chosen based on the
       signal, I contains information about theta. Observing I is equivalent
       to observing mu(s) because g is invertible.
DRIFT_RISK: HIGH — Author may not state the full-support regularity condition
             needed for strict monotonicity of mu(s). Author may also call this
             a "sufficient statistic" result — it is NOT Fisher sufficiency.
             It is invertibility of a monotone function. See drift risk below.

PARAMETER: Informational equivalence via invertibility
VALUE: If g is strictly increasing and continuous, then g is invertible, and
       observing I = g(mu(s)) is informationally equivalent to observing
       mu(s) = E[theta|s]. This is because mu(s) = g^{-1}(I) — the agent
       can recover the posterior expectation from the sunk cost by applying
       the inverse of the investment function.
UNIT: information equivalence
TOLERANCE: requires g strictly increasing and continuous — state explicitly.
           Also requires the agent to KNOW g (or be able to compute g^{-1}).
SOURCE: Rice [this paper] — derived result
NOTES: THIS IS NOT A SUFFICIENT STATISTIC IN THE FISHER-NEYMAN SENSE.
       Fisher sufficiency is about probabilistic data reduction — a sufficient
       statistic T(X) preserves all information the data X contain about a
       parameter theta, in the sense that the conditional distribution of X
       given T does not depend on theta. What we prove here is simpler: a
       strictly monotone continuous function has an inverse. Do NOT use the
       term "sufficient statistic." Do NOT cite Fisher (1922) or Neyman (1935)
       as if this result is formally parallel to theirs. Call it
       "informational equivalence" or "signal recovery via invertibility."
       Must be stated as a proposition with proof.
DRIFT_RISK: CRITICAL — Author will almost certainly use the term "sufficient
             statistic" because it sounds impressive. This is the single
             biggest technical vulnerability. A referee trained in mathematical
             statistics will immediately flag that this is not Fisher sufficiency
             but function inversion. REJECT any draft that uses the term
             "sufficient statistic" without the explicit caveat that this is
             a weaker, non-probabilistic notion. Preferred: avoid the term
             entirely and use "informational equivalence."

PARAMETER: Irrationality threshold (break-even investment level)
VALUE: I* = threshold investment level at which E[theta|I] = K/V. The agent
       continues iff I > I*. For general g: I* = g(K/V). For linear
       g(mu) = alpha * mu: I* = alpha * K/V.
UNIT: investment level
TOLERANCE: must be derived in closed form as function of investment function g,
           completion cost K, and project value V. For the linear/Gaussian case,
           present as a worked EXAMPLE or COROLLARY, not a separate Theorem —
           it is a direct substitution, not a deep result.
SOURCE: Rice [this paper] — derived result
NOTES: This is the core quantitative contribution. The behavioral economics
       literature treats ALL sunk cost attention as irrational. This paper
       shows there is a precise boundary. Consider calling this the "break-even
       investment level" rather than "irrationality threshold" — the latter
       name is confusing because "threshold" connotes "above this, bad things
       happen," but here it is below I* that irrational continuation occurs.
DRIFT_RISK: HIGH — Author may present the Gaussian/linear case as a Theorem
             when it is really a worked example. Author may also overstate
             Corollary 1 by calling I < I* "genuinely irrational" without
             acknowledging that the model excludes other rational channels
             (option value, strategic commitment, learning-by-doing) that
             could justify continuation below I*.

PARAMETER: Decision error probability
VALUE: The probability that an agent who ignores sunk costs makes a DIFFERENT
       binary decision than the Bayesian agent. This is not the same as
       P(E[theta|I] != E[theta]) — it is P(the two agents choose differently),
       which requires the posterior to cross the threshold K/V relative to
       the prior mean. Must be derived as a function of signal precision,
       prior, and K/V.
UNIT: probability
TOLERANCE: must be computed, not just stated as "probability 1"
SOURCE: Rice [this paper] — derived result
NOTES: v1 of this paper claimed "the agent who ignores sunk costs makes a
       strictly suboptimal decision with probability 1." This is wrong without
       additional regularity conditions, and even when correct, overstates the
       issue — the decision is suboptimal only when E[theta|I] and mu_0 are on
       opposite sides of K/V. The decision error probability is a more
       meaningful measure of the cost of ignoring sunk costs.
DRIFT_RISK: HIGH — Author may repeat the "probability 1" claim from v1.
             REJECT any draft that claims probability 1 without computing
             the actual decision error probability.

PARAMETER: Information decay with intermediate signals
VALUE: Between the initial investment and the continuation decision, the agent
       may receive additional signals s_2, s_3, ... about theta. As more
       signals arrive, the marginal information value of I decreases because
       the agent's posterior is increasingly determined by the new signals
       rather than the original signal encoded in I. Must derive how the
       information contribution of I to the continuation decision decays
       as a function of the number and precision of intermediate signals.
UNIT: information value (mutual information or posterior variance reduction)
TOLERANCE: must be a formal proposition, not a verbal remark
SOURCE: Rice [this paper] — derived result
NOTES: v1 completely omitted this. It is the most obvious practical objection
       to the model: a VC who invested in Series A has observed two years of
       startup performance before the Series B decision. The original signal s
       encoded in I is just one input; the VC now has direct performance data.
       The paper must show formally when I is and is not valuable.
DRIFT_RISK: CRITICAL — Author may omit this entirely (as in v1) or treat it
             as a verbal remark in the Discussion. It must be a PROPOSITION
             in M2 with a proof showing the decay rate.

PARAMETER: Continuation decision
VALUE: After sunk I, agent invests K to complete or abandons. Continues iff
       E[theta|I] * V > K. Sunk cost I is payoff-irrelevant but enters
       posterior E[theta|I] because I encodes the signal via invertibility.
SOURCE: Standard investment under uncertainty — adapted for sunk cost setting
DRIFT_RISK: MEDIUM — Author may muddle payoff relevance vs. information relevance

PARAMETER: Knowledge of g
VALUE: The agent must KNOW the investment function g (or be able to compute
       g^{-1}) at the continuation stage. This is a scope limitation of the
       model, NOT an open problem. If g is unknown, the mechanism fails
       completely — not partially.
UNIT: assumption
TOLERANCE: must be stated as an explicit assumption and discussed as a
           scope limitation in Boundary Conditions
SOURCE: Rice [this paper] — assumption
NOTES: The strongest defense for this assumption is INSTITUTIONAL: dollar
       amounts are recorded in accounting systems, contracts, and ledgers,
       while private posterior assessments are not. Investment functions
       within organizations are often formalized (budget rules, commitment
       thresholds, approval tiers). This institutional defense should be
       PRIMARY, not a throwaway remark.
DRIFT_RISK: HIGH — Author may bury this as an "open problem" (as in v1)
             rather than acknowledging it as a scope limitation that bounds
             the model's applicability.

MILESTONES:

M1: Signal model and Bayesian framework — define the quality parameter theta,
    signal structure (with full-support regularity condition), investment
    function g, and continuation decision. Establish notation. State the key
    distinction: sunk costs are payoff-irrelevant but potentially information-
    relevant. Define "informational equivalence via invertibility" — NOT
    "sufficient statistic." State the knowledge-of-g assumption explicitly.
    Introduction must EXTEND/REFINE the behavioral literature, not attack it.
    Use the literature gap formula but frame as "building on X, we show Y"
    not "X fails because Y." Minimum 8 prior works cited in Introduction.

M2: Rationality theorem, informational equivalence proof, break-even
    investment level derivation, decision error probability, and information
    decay proposition.
    Required deliverables:
    (a) Proposition: informational equivalence of I and mu(s) via invertibility
        of g. Do NOT call this a sufficient statistic. Proof must state the
        full-support regularity condition.
    (b) Theorem: attending to sunk costs is Bayesian-optimal; ignoring them
        causes decision errors with probability P_err (derived, not asserted).
    (c) Corollary or Example (NOT Theorem): break-even investment level
        I* = alpha*K/V under Gaussian/linear model. This is a substitution,
        not a deep result.
    (d) Proposition: information decay — as the agent receives n additional
        signals of precision tau_2 between stages, the marginal information
        contribution of I to the continuation decision decreases. Derive the
        decay rate formally. Show that as n*tau_2 -> infinity, the value of
        I goes to zero (the new signals swamp the old one).
    (e) Remark on Corollary 1 scope: when stating that continuation below I*
        is not rationalizable by information extraction, acknowledge that
        the model excludes other rational channels (option value, strategic
        commitment, learning-by-doing) that could justify continuation.

M3: Applications and boundary conditions — apply the framework to three
    domains: venture capital (follow-on investment), corporate R&D (project
    continuation), and military (escalation of commitment). For each, specify
    the signal model and derive whether observed sunk cost behavior is above
    or below I*.
    IMPORTANT: Call parameters "illustrative," not "calibrated." They are
    round numbers without empirical sources.
    Required:
    - Natural enemy (sunk cost irrelevance principle)
    - Knowledge-of-g as SCOPE LIMITATION (not open problem)
    - Nonlinear/discrete g as practical limitation (VC investment tiers,
      minimum sizes, capacity constraints — flat regions may dominate)
    - Prior misspecification discussion
    - Sensitivity analysis with epsilon-perturbation table
    - Competing models (prospect theory, self-justification, option value,
      regret theory) — when rejecting option value and learning-by-doing,
      acknowledge they are complementary rational channels, not irrational
    - Open problems (heterogeneous g, sequential signals, strategic interaction,
      empirical calibration)
    - THREE FIGURES with Python/matplotlib code:
        Figure 1: Signal model — relationship between theta, s, and I
        Figure 2: Rational vs. irrational regions with break-even level I*,
                  including decision error probability shading
        Figure 3: Application comparison — VC, R&D, military relative to I*,
                  showing information decay with intermediate signals

M4: Full paper — Introduction (extending the behavioral literature, not
    attacking it), Related Work (minimum 25 references — engage Eyster 2002,
    philosophical literature on sunk cost rationality, experimental work on
    informative vs. uninformative sunk costs), Discussion (memory device
    interpretation as primary, not secondary; information decay implications;
    scope limitations), Conclusion. Self-contained Abstract.
    CRITICAL: Verify every citation. The v1 Baliga & Ely (2011) citation was
    almost certainly wrong — the paper described as "good wars and bad wars"
    about strategic signaling may be a DIFFERENT Baliga-Ely paper from the
    one titled "Mnemonomics: The Sunk Cost Fallacy as a Memory Kludge."
    If the latter exists, it formalizes sunk costs as memory proxies —
    EXACTLY this paper's thesis. Must engage with it seriously and explain
    what this paper adds beyond their treatment. If the citation is wrong,
    fix it. Do NOT fabricate or guess — verify against known publications.

ORACLE:
The model is valid if and only if:
1. The signal model is formally specified with explicit assumptions including
   full-support regularity condition
2. The informational equivalence result is proven as a proposition — NOT
   called a "sufficient statistic" and NOT citing Fisher/Neyman as if
   formally parallel
3. The rationality conditions are stated as a theorem with explicit conditions
4. The break-even investment level I* is derived in closed form
5. The decision error probability is computed (not just asserted as "probability 1")
6. The information decay proposition is proven with a formal decay rate
7. Applications use illustrative (not "calibrated") parameters with the
   formal framework
8. Knowledge of g is stated as a scope limitation, not an open problem
9. Three figures with executable Python code are present
10. At least 25 references, with Baliga & Ely citation verified

Peer Reviewer must verify: (a) Is the term "sufficient statistic" used? If so,
REJECT. (b) Is the Gaussian/linear case presented as a Theorem? If so, REJECT —
it should be a Corollary or Example. (c) Does the Introduction attack or extend
the behavioral literature? If attack, REJECT. (d) Is the information decay
proposition present with a formal proof? If absent, REJECT. (e) Are application
parameters called "calibrated"? If so, REJECT — must be "illustrative."

KNOWN_DRIFT_RISKS:

- CRITICAL: Using "sufficient statistic" terminology — the v1 paper used this
  term throughout and cited Fisher (1922) and Neyman (1935). This is technically
  wrong. The result is function inversion under monotonicity, not Fisher
  sufficiency. Any referee trained in mathematical statistics will reject on
  this basis alone. Use "informational equivalence via invertibility" instead.
  REJECT any draft containing the phrase "sufficient statistic."

- CRITICAL: Omitting the information decay proposition — v1 had no discussion
  of what happens when the agent receives new signals between stages. This is
  the most obvious practical objection. Must be a formal proposition in M2
  showing the decay rate. REJECT any draft that treats this as a verbal remark.

- CRITICAL: Baliga & Ely citation — v1 cited "Baliga and Ely (2011). Mnemonic:
  the sunk cost fallacy as a memory kludge. AEJ:Micro 3(4):35-67" but
  characterized it as a strategic signaling model about "good wars and bad
  wars." This may be conflating two different papers. If B&E 2011 actually
  formalizes sunk costs as memory kludges (which the title suggests), their
  model is a DIRECT PREDECESSOR and must be engaged seriously — the present
  paper must explain precisely what it adds. Do NOT dismiss it as "game-
  theoretic" without reading it. If the citation details are wrong, fix them.
  Do NOT fabricate journal/volume/page numbers — if uncertain, cite as
  "Baliga and Ely (2011)" without journal details and flag for verification.

- HIGH: Presenting Gaussian/linear case as a Theorem — v1 had "Theorem 2"
  for I* = alpha*K/V, which is a direct substitution. Present as a Corollary,
  Example, or Worked Example. Reserve "Theorem" for results with non-trivial
  proof content.

- HIGH: Claiming decision error "with probability 1" — v1 Theorem 1(v) made
  this claim. It is wrong without regularity conditions (continuous signal
  distribution, non-degenerate prior). And even when technically correct, the
  relevant quantity is not P(posteriors differ) but P(different binary decision).
  Must compute the decision error probability as a function of signal precision,
  prior, and K/V.

- HIGH: Attacking the behavioral literature in the Introduction — v1 used
  the literature gap formula 5 times with the structure "X proposed Y, but Y
  fails." This reads as attacking Thaler, Arkes/Blumer, and Staw. Reframe as
  extending/refining: "Thaler (1980) established the sunk cost fallacy under
  conditions where sunk costs are uninformative. We show that when sunk costs
  are informative, the rational prediction changes." The message is the same;
  the framing is collaborative rather than adversarial.

- HIGH: Calling I < I* "genuinely irrational" without caveat — v1 Corollary 1
  said continuation below I* "requires a non-Bayesian explanation." But the
  model excludes option value (McAfee et al. 2010), strategic commitment
  (Baliga and Ely 2011), and learning-by-doing — all rational channels that
  could justify continuation below I*. Must acknowledge these exclusions when
  stating Corollary 1.

- HIGH: Knowledge of g buried as "open problem" — v1 listed heterogeneous g
  under Open Problems. But if g is unknown, the ENTIRE mechanism fails (not
  partially). This is a scope limitation, not an open problem. The institutional
  defense (dollar amounts in accounting systems) must be the PRIMARY
  justification for the assumption.

- MEDIUM: Missing regularity condition for strict monotonicity of mu(s) —
  MLRP alone does not guarantee mu(s) is strictly increasing in s. Need
  full-support prior on [0,1]. State this explicitly in the signal model
  definition and in the proposition proof.

- MEDIUM: Calling application parameters "calibrated" — v1 used round numbers
  ($10M, $5M, etc.) without empirical sources. Call them "illustrative."

- MEDIUM: Thin reference list — v1 had 15 references for a paper engaging
  with a 50-year literature. Target 25-30 minimum. Missing at minimum:
  Eyster (2002) on rationalizing past decisions, philosophical literature
  on sunk costs and rational agency (Kelly 2004, Steele 1996), experimental
  work distinguishing informative from uninformative sunk costs.

- MEDIUM: No figures — the frozen spec called for 3 figures. v1 had none.
  Figures showing the rational/irrational regions and application comparison
  substantially improve readability and are expected for a theory paper
  in this venue.

- MEDIUM: Prior misspecification not discussed — the Bayesian framework
  assumes the prior is correct. If the prior is wrong, E[theta|I] is wrong
  and I* is wrong. Needs at least a paragraph in Boundary Conditions.

- MEDIUM: Nonlinear/discrete g in practice — VC investment amounts cluster
  at discrete levels ($1M, $2M, $5M, $10M). Minimum investment sizes and
  capacity constraints create flat regions in g. The epsilon-perturbation
  sensitivity analysis from v1 obscures the practical severity — the flat
  regions may dominate the domain. Discuss this honestly.

- LOW: Title — "The Sunk Cost Fallacy Is Not Always a Fallacy" is provocative
  and risks being read as "the sunk cost fallacy is wrong." Consider "When
  Sunk Costs Carry Signals: A Bayesian Rationalization" — more precise, less
  defensive trigger for behavioral economists.

- LOW: "Irrationality threshold" naming — "threshold" connotes "above this,
  bad things happen" but here it is BELOW I* that irrational continuation
  occurs. Consider "break-even investment level" or "signal-inferred
  break-even."

- PROOF STRATEGY: The informational equivalence result must use invertibility
  of strictly monotone continuous functions — NOT Fisher-Neyman sufficiency.
  Proof: g strictly increasing + continuous on [0,1] => g injective =>
  g^{-1} exists on [g(0), g(1)] => mu(s) = g^{-1}(I). State the full-support
  condition for mu(s) strict monotonicity. This is the technical core but
  acknowledge its algebraic simplicity — do not dress it up.

- PROOF STRATEGY: The information decay proposition should use the Gaussian
  updating framework. After initial signal s_1 with precision tau_1 and
  n additional signals s_2,...,s_{n+1} each with precision tau_2, the
  posterior is E[theta|s_1,...,s_{n+1}] = (tau_0*mu_0 + tau_1*s_1 +
  n*tau_2*s_bar) / (tau_0 + tau_1 + n*tau_2). The weight on s_1 (and
  therefore the information content of I) is tau_1 / (tau_0 + tau_1 + n*tau_2),
  which goes to 0 as n -> infinity. Derive the marginal information
  contribution of I as a function of n and tau_2.

- PROOF STRATEGY: Decision error probability. Under the Gaussian model, the
  sunk-cost-ignoring agent continues iff mu_0 > K/V, while the Bayesian agent
  continues iff g^{-1}(I) > K/V. The decision error probability is
  P(mu_0 and g^{-1}(I) on opposite sides of K/V) = P(mu(s) crosses K/V
  relative to mu_0). Under the Gaussian model this can be computed in
  closed form using the normal CDF.

- FORMALIZATION: The three applications (VC, R&D, military) must each
  specify the signal distribution, the investment function, and compute I*
  with numbers. Parameters are ILLUSTRATIVE, not calibrated. Show the
  signal-to-noise ratio for each domain. Add information decay analysis:
  how many intermediate signals does each domain typically have, and how
  much does this reduce the value of I?

- FIGURE GUIDANCE:
    Figure 1: Signal model diagram — show theta generating s, s generating
              mu(s), mu(s) generating I via g, and g^{-1} recovering mu(s)
              from I. Annotate with the invertibility relationship.
    Figure 2: Rational vs. irrational regions — I on x-axis, E[theta|I] on
              y-axis, horizontal line at K/V, vertical line at I*. Shade the
              decision error region where mu_0 and E[theta|I] disagree.
    Figure 3: Application comparison — three panels (VC, R&D, military)
              showing I* relative to typical investment distributions, with
              information decay curves showing how I's value decreases with
              intermediate signals.

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 0 — Resolve project directory (auto-versioning)

The base slug is SUNK_COST. Resolve the project directory using this pattern:
  C:\PROJECTS\SHELL\papers\SUNK_COST_[YYYY-MM-DD]_[SEQ]\

To resolve:
1. List all existing directories matching C:\PROJECTS\SHELL\papers\SUNK_COST_*
2. If none exist: use SUNK_COST_[TODAY]_001
3. If some exist: find the highest sequence number across ALL matching
   directories (regardless of date), increment by 1, use SUNK_COST_[TODAY]_[NEXT_SEQ]

Store: RESOLVED_DIR and RESOLVED_SLUG. Use these for ALL paths below.

### Step 1 — Create project directory
Create RESOLVED_DIR with:
  spec/, state/, outputs/, results/raw/, results/validated/, results/final/,
  devlog/, src/, papers/sunk_cost_v2_2026/,
  papers/sunk_cost_v2_2026/figures/, prompts/, figures/

### Step 2 — Write CLAUDE.md
North star: Bayesian model proving sunk cost attention is rational when
sunk costs encode signals via invertibility of the investment function.
I* is the break-even investment level. Key change from v1: NO "sufficient
statistic" language, information decay proposition required, decision error
probability computed, Baliga & Ely citation verified, Introduction extends
(not attacks) behavioral literature, parameters illustrative not calibrated,
three figures required.

### Step 3 — Write frozen_spec.md
Fill from FROZEN_SPEC_PARAMETERS above. Lock date today.
Locked by: James P Rice Jr.

### Step 4 — Initialize state files
state_vector.md — TURN: 0, MILESTONE: M1, MODE: INIT
innovation_log.md — header with project name and timestamp
dead_ends.md — header with project name. Include: "v1 used 'sufficient
statistic' terminology throughout — this was the primary technical
vulnerability. Do not repeat."

### Step 5 — Copy all prompts from SHELL
Copy from C:\PROJECTS\SHELL\prompts\ into RESOLVED_DIR\prompts\:
  04_paper_orchestrator.md
  05_author.md
  06_peer_reviewer.md
  07_editor.md
  08_steelman.md
  run_milestone.md
Do NOT copy 00_init.md — SHELL-level only.

Also write prompts/turn_prompts_log.md:
  # TURN PROMPTS LOG — sunk_cost_v2_2026
  # Every exact prompt logged here. Required for reproducibility.
  [No entries yet. First entry written at Turn 1 M1.]

### Step 5b — Write run_pipeline.ps1

Write run_pipeline.ps1 in RESOLVED_DIR with the slug set to RESOLVED_SLUG.
Use the template from C:\PROJECTS\SHELL\prompts\00_init.md Step 15,
replacing [SLUG] references with RESOLVED_SLUG and paths with RESOLVED_DIR.

### Step 6 — Write STATUS.md
Phase: INIT -> PAPER PIPELINE
Turn: 0
What Is Done: Scaffolded. Spec locked. v1 steelman feedback incorporated.
What Is Next: Author writes M1 (Signal model + Bayesian framework + definitions).

### Step 7 — Write remaining required files
Write README.md, CHAIN_PROMPT.md, SACRED_FILES.md, BEST_PRACTICES.md,
devlog/DEV_LOG.md, outputs/options.md, outputs/state_vector_backup.md.
CHAIN_PROMPT.md must include:
  Pipeline: PAPER — Claude-only, milestone-by-milestone gating
  Author: Claude | Peer Reviewer: Claude | Editor: Claude
  v2 changes: No "sufficient statistic," information decay proposition,
  decision error probability, verified citations, collaborative framing,
  illustrative parameters, three figures, 25+ references.

### Step 8 — Initialize git
  cd RESOLVED_DIR
  git init
  git add -A
  git commit -m "Turn 0 | Init | sunk_cost_v2_2026 | RESOLVED_SLUG — steelman feedback incorporated"

### Step 9 — Print confirmation and hand off:
  PROJECT INITIALIZED: sunk_cost_v2_2026 (RESOLVED_SLUG)
  Spec locked. All files created. Git initialized.
  v1 steelman feedback fully incorporated into drift risks.
  Beginning paper pipeline — M1 (Signal Model + Bayesian Framework) first.
  Output: RESOLVED_DIR\paper.md
  Running. James P Rice Jr. reviews when done.

---

## HAND OFF — EXECUTE PAPER PIPELINE

DO NOT STOP HERE. The setup is complete. Now you must execute the paper pipeline.

Read prompts/04_paper_orchestrator.md NOW and follow every instruction in it.
You are the Orchestrator. Begin at the INITIALIZE section. This is not a file
to summarize — it is your operating manual. Execute it.

YOUR INPUTS:
  PROBLEM: [the full PROBLEM text from the INPUTS section above]
  DATA: No empirical data. All results derived analytically from the Bayesian model.
  SLUG: RESOLVED_SLUG
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS above into every Author and Reviewer prompt]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every review pass]

BEGIN NOW. Run M1. Do not ask for confirmation. Do not summarize the orchestrator.
Execute it. Write the paper.
