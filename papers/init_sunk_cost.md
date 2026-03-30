# INIT — THE SUNK COST FALLACY IS NOT ALWAYS A FALLACY
# Pre-filled. Ready to run.
# claude --dangerously-skip-permissions papers/init_sunk_cost.md

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: The Sunk Cost Fallacy Is Not Always a Fallacy: A Bayesian Rationalization
SLUG: sunk_cost_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: Theory and Decision
PIPELINE: PAPER

PROBLEM:
Proves that sunk cost behavior can be rational when sunk costs carry information
about investment quality. If initial investment was based on a private signal
about project quality, then sunk cost size correlates with posterior belief.
Derives conditions where "throwing good money after bad" is Bayesian-optimal.
Calculates the exact threshold where genuinely irrational sunk cost behavior
begins.

The paper is formal Bayesian decision theory. The rationality result must be
a theorem, not an illustration. The signal model must be rigorous: agent
receives noisy signal, invests proportional to posterior expectation, and sunk
cost becomes a sufficient statistic for the posterior. The irrationality
threshold must be derived in closed form — the exact boundary where attending
to sunk costs transitions from Bayesian-optimal to genuinely fallacious.

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
       Signal is informative: E[theta|s] is increasing in s. Agent invests
       I = g(E[theta|s]) where g is increasing — higher expected quality
       leads to larger initial investment.
UNIT: signal realization
TOLERANCE: g must be increasing; specific functional form (linear, etc.)
           used for closed-form results but main theorems hold generally
SOURCE: Novel formalization — Rice [this paper]
NOTES: This is the key insight: because investment I was chosen based on the
       signal, I contains information about theta. Observing I is equivalent
       to observing a (garbled) version of the signal s.
DRIFT_RISK: HIGH — Author may not formalize the signal model rigorously,
             leaving the connection between I and theta as intuitive rather
             than proven

PARAMETER: Sunk cost as sufficient statistic
VALUE: If g is strictly monotone, then investment I is a sufficient statistic
       for E[theta|s] — knowing I tells the agent everything the signal told
       about quality that is relevant for the continuation decision
UNIT: information equivalence
TOLERANCE: requires g strictly monotone — state this assumption explicitly
SOURCE: Rice [this paper] — derived result
NOTES: This is the formal mechanism. It is why sunk costs carry information:
       they were chosen based on a signal, so they encode the signal.
       Must be stated as a proposition with proof.
DRIFT_RISK: HIGH — Author may assert this is "obvious" without proving it.
             It is not obvious — it requires the monotonicity of g and the
             informative signal structure.

PARAMETER: Irrationality threshold
VALUE: I* = threshold investment level above which continuing to invest is
       no longer Bayesian-optimal given the posterior. Below I*, attending
       to sunk costs is rational. Above I*, it is genuinely fallacious.
UNIT: investment level
TOLERANCE: must be derived in closed form as function of prior, signal
           precision, and cost structure
SOURCE: Rice [this paper] — derived result
NOTES: This is the core quantitative contribution. The behavioral economics
       literature treats ALL sunk cost attention as irrational. This paper
       shows there is a precise boundary: rational below I*, irrational above.
DRIFT_RISK: HIGH — Author may not derive I* formally; may leave it as a
             conceptual distinction without a formula

PARAMETER: Continuation decision
VALUE: After sunk I, agent invests K to complete or abandons. Continues iff
       E[theta|I] * V > K. Sunk cost I is payoff-irrelevant but enters
       posterior E[theta|I] because I encodes the signal.
SOURCE: Standard investment under uncertainty — adapted for sunk cost setting
DRIFT_RISK: MEDIUM — Author may muddle payoff relevance vs. information relevance

MILESTONES:

M1: Signal model and Bayesian framework — define the quality parameter theta,
    signal structure, investment function g, and continuation decision.
    Establish notation. State the key distinction: sunk costs are payoff-
    irrelevant but potentially information-relevant. Define what "rational
    sunk cost attention" means formally.

M2: Rationality theorem and threshold derivation — prove that when I is a
    sufficient statistic for E[theta|s], attending to sunk costs is Bayesian-
    optimal. Derive the irrationality threshold I* in closed form. Prove
    that below I*, sunk cost attention is rational, and above I*, it is
    genuinely fallacious. State conditions on g, signal structure, and prior
    required for the results.

M3: Applications and boundary conditions — apply the framework to three
    domains: venture capital (follow-on investment), corporate R&D (project
    continuation), and military (escalation of commitment). For each, specify
    the signal model and derive whether observed sunk cost behavior is above
    or below I*. Sensitivity analysis on signal precision and prior.
    Boundary conditions: what happens as signal precision goes to zero
    (pure noise) or infinity (perfect information)?

M4: Full paper — Introduction (the sunk cost fallacy and its exceptions),
    Related work (Thaler 1980, Arkes & Blumer 1985, Staw 1976, McAfee et al.
    2010, Baliga & Ely 2011), Discussion (implications for behavioral
    economics, when heuristics are rational, limitations), Conclusion.
    Self-contained Abstract.

ORACLE:
The model is valid if and only if:
1. The signal model is formally specified with explicit assumptions
2. The sufficient statistic result is proven as a proposition
3. The rationality conditions are stated as a theorem with explicit conditions
4. The irrationality threshold I* is derived in closed form
5. Applications (VC, R&D, military) use the formal framework, not anecdotes

Peer Reviewer must verify: are the rationality conditions and irrationality
threshold proven theorems, or are they illustrated with examples? If the
latter, REJECT.

KNOWN_DRIFT_RISKS:
- Not formalizing the signal model rigorously — the whole contribution depends
  on the signal model being explicit; without it, "sunk costs carry
  information" is just a verbal argument anyone could make
- Conflating information value with commitment bias — the paper shows sunk
  costs carry information about quality; commitment escalation (Staw 1976)
  is a separate psychological phenomenon; must distinguish formally
- Not proving the threshold theorem — the irrationality threshold I* is the
  quantitative contribution; without a closed-form expression, the paper
  is a conceptual note, not a theory paper
- Citing Thaler 1980 without engaging formally — Thaler defined the sunk
  cost fallacy; this paper partially overturns it; must state precisely
  what is overturned (the universality of the fallacy) and what is preserved
  (sunk costs above I* are still irrational)
- Making applications too informal — VC, R&D, military must specify signal
  model parameters, not just tell stories
- Moralizing about behavioral economics — paper refines the fallacy, does
  not reject it; keep tone constructive
- Missing McAfee et al. 2010 connection — they use option value, this paper
  uses information; must distinguish the two mechanisms
- Conflating sufficient statistic result with triviality — requires specific
  conditions on signal model and investment function g
- PROOF STRATEGY: The signal model must use a formal Bayesian setup — prior
  pi(theta), signal s = theta + epsilon (Gaussian noise), investment function
  g(E[theta|s]). Prove that I = g(E[theta|s]) is a sufficient statistic for
  E[theta|s] under specific conditions on g (monotonicity, invertibility).
  This is the technical core — do NOT skip to the threshold without it.
- PROOF STRATEGY: The irrationality threshold I* must be derived from the
  value of continuing vs abandoning — set up the decision problem formally
  as V_continue(I) vs V_abandon, derive I* where they cross, prove it is
  unique under stated conditions on the cost/benefit structure.
- FORMALIZATION: The three applications (VC, R&D, military) must each
  specify the signal distribution, the investment function, and compute I*
  with numbers — not just narratively claim "sunk costs carry information
  in VC." Show the signal-to-noise ratio for each domain.
- Orphan figure references — every figure must have clear formal content:
    Figure 1: Signal model — relationship between theta, s, and I
    Figure 2: Rational vs. irrational sunk cost regions with threshold I*
    Figure 3: Application comparison — VC, R&D, military relative to I*

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory
Create D:\EXPERIMENTS\SUNK_COST\ with:
  spec/, state/, outputs/, results/raw/, results/validated/, results/final/,
  devlog/, src/, papers/, papers/sunk_cost_2026/,
  papers/sunk_cost_2026/figures/, prompts/

### Step 2 — Write CLAUDE.md
North star: Bayesian model proving sunk cost attention is rational when
sunk costs encode signals. I* is the irrationality threshold. Frozen
params: Standard Bayes, noisy informative signal, sunk cost as sufficient
statistic (g monotone), threshold I*. Enforcements: rigorous signal model,
proven sufficient statistic, closed-form I*, information vs. commitment.

### Step 3 — Write spec/frozen_spec.md
Fill from FROZEN_SPEC_PARAMETERS above. Lock date today.
Locked by: James P Rice Jr.

### Step 4 — Initialize state files
state/state_vector.md — TURN: 0, MILESTONE: M1, MODE: INIT
state/innovation_log.md — header with project name and timestamp
state/dead_ends.md — header with project name

### Step 5 — Copy all prompts from SHELL
Copy from D:\EXPERIMENTS\SHELL\prompts\ into D:\EXPERIMENTS\SUNK_COST\prompts\:
  04_paper_orchestrator.md
  05_author.md
  06_peer_reviewer.md
  07_editor.md
  run_milestone.md
Do NOT copy 00_init.md — SHELL-level only.

Also write prompts/turn_prompts_log.md:
  # TURN PROMPTS LOG — sunk_cost_2026
  # Every exact prompt logged here. Required for reproducibility.
  [No entries yet. First entry written at Turn 1 M1.]

### Step 5b — Write run_pipeline.ps1

Write run_pipeline.ps1 in the project root (D:\EXPERIMENTS\SUNK_COST\) with
the slug set to "sunk_cost_2026". Use the template from
D:\EXPERIMENTS\SHELL\prompts\00_init.md Step 15, replacing [SLUG] with
sunk_cost_2026 and [SLUG] paths with SUNK_COST.

### Step 6 — Write STATUS.md
Phase: INIT -> PAPER PIPELINE
Turn: 0
What Is Done: Scaffolded. Spec locked.
What Is Next: Author writes M1 (Signal model + Bayesian framework + definitions).

### Step 7 — Write remaining required files
Write README.md, CHAIN_PROMPT.md, SACRED_FILES.md, BEST_PRACTICES.md,
devlog/DEV_LOG.md, outputs/options.md, outputs/state_vector_backup.md.
CHAIN_PROMPT.md must include:
  Pipeline: PAPER — Claude-only, milestone-by-milestone gating
  Author: Claude | Peer Reviewer: Claude | Editor: Claude

### Step 8 — Initialize git
  cd D:\EXPERIMENTS\SUNK_COST
  git init
  git add -A
  git commit -m "Turn 0 | Init | sunk_cost_2026"

### Step 9 — Print confirmation and hand off:
  PROJECT INITIALIZED: sunk_cost_2026
  Spec locked. All files created. Git initialized.
  Beginning paper pipeline — M1 (Signal Model + Bayesian Framework) first.
  Output: papers/sunk_cost_2026/paper.md
  Running. James P Rice Jr. reviews when done.

---

## HAND OFF — EXECUTE PAPER PIPELINE

Load prompts/04_paper_orchestrator.md.

Pass:
  PROBLEM: [full PROBLEM text above]
  DATA: No empirical data. All results derived analytically from the Bayesian model.
  SLUG: sunk_cost_2026
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS into every Author and Reviewer prompt]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every pass]

Run the full milestone pipeline: M1 -> M2 -> M3 -> M4.
Do not skip milestones. Do not open M2 until M1 is Peer Reviewer ACCEPT.
Halt only on HALT CONDITIONS.
When done write papers/sunk_cost_2026/paper.md and halt.
James P Rice Jr. reviews it.
