# INIT — CONSPIRACY BELIEFS AS BAYESIAN UPDATING
# Pre-filled. Ready to run.
# claude --dangerously-skip-permissions papers/init_conspiracy_bayes.md

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Conspiracy Beliefs as Bayesian Updating on a Hidden Variable: A Formal Epistemological Model
SLUG: conspiracy_bayes_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: Episteme
PIPELINE: PAPER

PROBLEM:
Models conspiracy belief formation as Bayesian updating on a hidden variable
(conspiracy existence) given observable evidence. Shows that even a small prior
on the conspiracy hypothesis, combined with ambiguous evidence (government secrecy,
conflicting accounts), leads rational Bayesian agents to converging conspiracy
belief. Derives conditions for convergence and proves public transparency is the
only robust prevention mechanism. The central contribution is formalizing what
epistemologists discuss informally: conspiracy belief is not irrational — it is
the output of rational Bayesian updating under specific likelihood structures.
The pathology is in the evidence environment, not the reasoner. Transparency
changes the likelihood structure and is the only mechanism that provably prevents
convergence.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Bayes' theorem
VALUE: P(H|E) = P(E|H)*P(H) / P(E)
UNIT: probability
TOLERANCE: exact — this is the foundational equation
SOURCE: Standard probability theory
NOTES: Applied sequentially: P(H|E_1,...,E_n) via iterated updating.
       The model must use sequential updating, not single-shot.
DRIFT_RISK: LOW — standard, but Author may simplify to single update

PARAMETER: Hidden variable model
VALUE: H_c (conspiracy exists) vs H_n (no conspiracy, standard explanation).
       Binary hypothesis space. Prior: P(H_c) = pi_0, P(H_n) = 1 - pi_0.
UNIT: probability
TOLERANCE: pi_0 explored parametrically (0.01 to 0.5)
SOURCE: Novel formalization — this paper's framework
NOTES: The binary hypothesis space is a simplification. The paper should
       acknowledge multi-hypothesis extensions in Discussion but derive the
       core results for the binary case. pi_0 is the initial conspiracy prior —
       even small values (0.01) can lead to convergence.
DRIFT_RISK: MEDIUM — Author may make the model too complex (multiple conspiracy
             hypotheses) or too simple (single update, not sequential)

PARAMETER: Likelihood ratio for ambiguous evidence
VALUE: Lambda_k = P(E_k|H_c) / P(E_k|H_n) > 1 for secrecy-type evidence;
       Lambda_k < 1 for transparency-type evidence
UNIT: dimensionless ratio
TOLERANCE: explored parametrically
SOURCE: Derived from evidence type classification (novel)
NOTES: The key insight: secrecy (government classification, NDAs, redacted documents)
       generates evidence with Lambda > 1 because such evidence is more expected under
       H_c than H_n. Transparency generates Lambda < 1 because full disclosure is more
       expected under H_n. This asymmetry drives convergence.
DRIFT_RISK: HIGH — Author may assert Lambda > 1 for secrecy without deriving why.
             Must formally justify the likelihood asymmetry from the evidence structure.

PARAMETER: Convergence criterion
VALUE: Posterior P(H_c|E_1,...,E_n) -> 1 as n -> infinity, under the condition
       that sum(log(Lambda_k)) -> +infinity
UNIT: probability (limit)
TOLERANCE: exact — this is a standard Bayesian convergence result
SOURCE: Standard Bayesian convergence (Doob 1949; Blackwell & Dubins 1962)
NOTES: The convergence theorem must state: if the agent receives a sequence of
       evidence items with average log-likelihood ratio > 0 (i.e., evidence is
       on average more consistent with H_c than H_n), then P(H_c) -> 1 regardless
       of the prior pi_0 > 0. This is the formal trap: in a secrecy-rich environment,
       convergence is guaranteed for any non-zero conspiracy prior.
DRIFT_RISK: HIGH — Author may not prove convergence formally, or may simulate it
             instead of deriving the conditions analytically

PARAMETER: Transparency mechanism
VALUE: If evidence environment shifts to Lambda_k < 1 on average (transparency
       regime), convergence reverses: P(H_c) -> 0
UNIT: N/A (mechanism)
TOLERANCE: N/A
SOURCE: Derived — follows from the convergence theorem applied to Lambda < 1
NOTES: This is the policy punchline. Transparency is not just good governance —
       it is the only mechanism that changes the likelihood structure enough to
       prevent conspiracy belief convergence. Must be proven, not merely argued.
DRIFT_RISK: MEDIUM — Author may moralize about transparency instead of proving it
             as the unique convergence-breaking mechanism

MILESTONES:

M1: Bayesian model + definitions — define the hidden variable model (H_c vs H_n),
    prior pi_0, evidence sequence {E_k}, likelihood ratios Lambda_k. Classify
    evidence types (secrecy-type: Lambda > 1; transparency-type: Lambda < 1;
    neutral: Lambda = 1). Show the sequential updating formula. Establish notation.
    Clearly state what makes this a formal epistemological model, not just Bayes.

M2: Convergence theorem + conditions — Prove Theorem 1: if pi_0 > 0 and the
    average log-likelihood ratio E[log(Lambda_k)] > 0, then P(H_c|E_1,...,E_n) -> 1
    as n -> infinity. Prove Theorem 2: the rate of convergence depends on
    E[log(Lambda_k)] and Var[log(Lambda_k)]. Derive the expected number of evidence
    items to reach a given posterior threshold (e.g., P(H_c) > 0.9).

M3: Transparency mechanism + boundary conditions — Prove Theorem 3: public
    transparency (shifting E[log(Lambda_k)] < 0) is the only mechanism that
    reverses convergence in the binary model. Show that increasing pi_0 skepticism
    (reducing prior) only delays convergence, does not prevent it. Show that
    "debunking" (single strong Lambda < 1 evidence) is insufficient if the
    background remains Lambda > 1. Boundary conditions: pi_0 -> 0 (maximum
    skepticism), Lambda_k -> 1 for all k (uninformative evidence), all Lambda > 1
    (pure secrecy environment). Sensitivity analysis table.

M4: Full paper — Introduction (conspiracy belief as a formal epistemological problem),
    Related work (Sunstein & Vermeule 2009, Dentith 2014, Keeley 1999, Bayesian
    epistemology literature), Discussion (implications for information policy,
    limitations of binary model, relationship to echo chambers and filter bubbles),
    Conclusion. Self-contained Abstract.

ORACLE:
The model is valid if and only if:
1. The hidden variable model is formally defined with explicit hypotheses and priors
2. The likelihood ratio structure is derived from evidence types, not assumed
3. The convergence theorem is proven with explicit conditions, not simulated
4. The transparency mechanism is proven as the unique convergence-breaker
5. The rate of convergence is derived, not just the limiting behavior

Peer Reviewer must verify: is the convergence to conspiracy belief a proven theorem
with explicit conditions, or is it merely demonstrated via simulation or example?
If the latter, REJECT.

KNOWN_DRIFT_RISKS:
- Making the model too simple — single Bayesian update instead of sequential
  updating with convergence analysis
- Not proving convergence formally — simulating it or showing examples is
  insufficient; the conditions and rate must be derived analytically
- Moralizing about conspiracy theories instead of doing math — the paper takes
  no position on whether conspiracy beliefs are true or false; it derives when
  rational agents converge to them
- Confusing the model's implications — the result is that conspiracy belief is
  RATIONAL given the evidence structure, not that it is irrational; the pathology
  is in the evidence environment (secrecy), not the reasoner
- Asserting Lambda > 1 for secrecy evidence without deriving it from the
  information structure — must formally justify why classified documents,
  redactions, and official denials increase the likelihood ratio
- Making the transparency result a platitude instead of a theorem — must prove
  that only a shift in the average likelihood ratio (not individual debunking
  events) prevents convergence
- Adding multi-hypothesis complexity before the binary case is fully solved —
  binary first, extensions in Discussion
- PROOF STRATEGY: The convergence proof MUST use martingale theory (posterior
  is a bounded martingale under the true measure) — not just examples or
  simulation showing the posterior increases. The strong law of large numbers
  on log-likelihood ratios drives convergence. State and prove this formally.
- PROOF STRATEGY: The transparency theorem must show that shifting the
  AVERAGE log-likelihood ratio below zero (not just adding counter-evidence)
  is necessary and sufficient. Prove this as a biconditional theorem.
- FORMALIZATION: The evidence types must be formally defined as a partition
  of the evidence space with distinct likelihood ratios for each type —
  not just "some evidence favors H_c." The model needs structure.
- Failing to connect to formal epistemology literature — Bayesian epistemology
  (Howson & Urbach, Earman) must be cited and positioned against
- Ignoring the network/social dimension — state as a limitation (individual
  model, not social) but do not attempt to solve it in this paper
- Orphan figure references — every figure must have Python/matplotlib code.
  The paper should include at minimum:
    Figure 1: Posterior P(H_c) trajectory under secrecy-rich evidence (Lambda > 1)
    Figure 2: Convergence rate vs average log-likelihood ratio
    Figure 3: Effect of transparency intervention on posterior trajectory

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory
Create D:\EXPERIMENTS\CONSPIRACY_BAYES\ with:
  spec/, state/, outputs/, results/raw/, results/validated/, results/final/,
  devlog/, src/, papers/, papers/conspiracy_bayes_2026/,
  papers/conspiracy_bayes_2026/figures/, prompts/

### Step 2 — Write CLAUDE.md
  # Conspiracy Beliefs as Bayesian Updating — NORTH STAR

  ## What We Are Building
  A formal Bayesian model proving rational agents converge to conspiracy belief
  under secrecy-rich evidence, with transparency as the only fix.

  ## The Core Claim
  Any non-zero conspiracy prior, combined with evidence whose average likelihood
  ratio favors the conspiracy hypothesis (secrecy-type evidence), guarantees
  convergence to conspiracy belief. Transparency is the only mechanism that
  reverses this. Both are proven as theorems.

  ## Frozen Parameters (quick reference)
  | Parameter | Value | Source |
  |-----------|-------|--------|
  | Bayes' theorem | P(H|E) = P(E|H)P(H)/P(E) | Standard |
  | Hypotheses | H_c vs H_n (binary) | Novel formalization |
  | Convergence | P(H_c) -> 1 if E[log Lambda] > 0 | Bayesian convergence |
  | Transparency | Shifts E[log Lambda] < 0 | Derived |

  ## Critical Enforcements
  - Sequential Bayesian updating, not single-shot
  - Convergence theorem formally proven with explicit conditions
  - Transparency proven as unique convergence-breaker, not argued
  - No moralizing — the model is neutral on truth of conspiracy hypotheses

### Step 3 — Write spec/frozen_spec.md
Fill from FROZEN_SPEC_PARAMETERS above. Lock date today.
Locked by: James P Rice Jr.

### Step 4 — Initialize state files
state/state_vector.md — TURN: 0, MILESTONE: M1, MODE: INIT
state/innovation_log.md — header with project name and timestamp
state/dead_ends.md — header with project name

### Step 5 — Copy all prompts from SHELL
Copy from D:\EXPERIMENTS\SHELL\prompts\ into D:\EXPERIMENTS\CONSPIRACY_BAYES\prompts\:
  04_paper_orchestrator.md
  05_author.md
  06_peer_reviewer.md
  07_editor.md
  run_milestone.md
Do NOT copy 00_init.md — SHELL-level only.

Also write prompts/turn_prompts_log.md:
  # TURN PROMPTS LOG — conspiracy_bayes_2026
  # Every exact prompt logged here. Required for reproducibility.
  [No entries yet. First entry written at Turn 1 M1.]

### Step 5b — Write run_pipeline.ps1

Write run_pipeline.ps1 in the project root (D:\EXPERIMENTS\CONSPIRACY_BAYES\) with
the slug set to "conspiracy_bayes_2026". Use the template from
D:\EXPERIMENTS\SHELL\prompts\00_init.md Step 15, replacing [SLUG] with
conspiracy_bayes_2026 and [SLUG] paths with CONSPIRACY_BAYES.

### Step 6 — Write STATUS.md
Phase: INIT -> PAPER PIPELINE
Turn: 0
What Is Done: Scaffolded. Spec locked.
What Is Next: Author writes M1 (Bayesian model, hidden variable, evidence classification).

### Step 7 — Write remaining required files

Write README.md:
  # Conspiracy Beliefs as Bayesian Updating on a Hidden Variable
  **Author:** James P Rice Jr.
  **Target:** Episteme
  **Status:** In progress
  ## What This Is
  A formal Bayesian model of conspiracy belief formation. Rational agents converge
  to conspiracy belief under secrecy. Transparency is the proven fix.
  ## How to Run
  claude --dangerously-skip-permissions prompts/04_paper_orchestrator.md

Write CHAIN_PROMPT.md:
  # CHAIN PROMPT — Conspiracy Bayes Paper | THIS FILE WINS ALL CONFLICTS
  Name: Conspiracy Beliefs as Bayesian Updating on a Hidden Variable
  Author: James P Rice Jr.
  Core claim: Rational Bayesian agents converge to conspiracy belief under
  secrecy-rich evidence. Transparency is the only convergence-breaking mechanism.
  Both proven as theorems.
  Pipeline: PAPER — Claude-only, milestone-by-milestone gating.
  Author: Claude | Peer Reviewer: Claude | Editor: Claude
  [today] | Initialized from SHELL v3

Write SACRED_FILES.md:
  # SACRED FILES | Lock date: [today] | Locked by: James P Rice Jr.
  | File | Reason | Locked |
  |------|--------|--------|
  | spec/frozen_spec.md | Oracle. Never modify after lock. | [today] |

Write BEST_PRACTICES.md:
  # BEST PRACTICES — Conspiracy Bayes Paper | SHELL v3 standards
  - Sequential Bayesian updating throughout, not single-shot.
  - Convergence theorem formally proven with explicit conditions and rate.
  - Transparency proven as unique convergence-breaker — theorem, not argument.
  - No moralizing. The model is neutral on truth. Pathology is in evidence environment.
  - Natural enemy: Sunstein & Vermeule 2009 — must show formal contribution beyond.
  - Likelihood ratios derived from evidence structure, not assumed.
  - Milestone-by-milestone. No section opens until previous is Peer Reviewer ACCEPT.
  - Every figure needs Python/matplotlib code. No orphan figure references.
  - Lean-ready proofs: all hypotheses explicit, every derivation step justified.

Write devlog/DEV_LOG.md:
  # DEVELOPMENT LOG — conspiracy_bayes_2026
  ## [today] — Session 1
  Initialized from SHELL v3. Spec locked. All files created. Git initialized.
  Pipeline: PAPER, Claude-only, milestone-by-milestone gating.
  Models: Claude (Author) -> Claude (Peer Reviewer) -> Claude (Editor).

Write outputs/options.md:
  # OPTIONS LOG — conspiracy_bayes_2026
  [No options yet.]

Write outputs/state_vector_backup.md:
  # STATE VECTOR BACKUP — conspiracy_bayes_2026
  [No backups yet.]

### Step 8 — Initialize git
  cd D:\EXPERIMENTS\CONSPIRACY_BAYES
  git init
  git add -A
  git commit -m "Turn 0 | Init | conspiracy_bayes_2026"

### Step 9 — Print confirmation and hand off:
  PROJECT INITIALIZED: conspiracy_bayes_2026
  Spec locked. All files created. Git initialized.
  Beginning paper pipeline — M1 (Bayesian Model + Evidence Classification) first.
  Output: papers/conspiracy_bayes_2026/paper.md
  Running. James P Rice Jr. reviews when done.

---

## HAND OFF — EXECUTE PAPER PIPELINE

Load prompts/04_paper_orchestrator.md.

Pass:
  PROBLEM: [full PROBLEM text above]
  DATA: No empirical data. All results derived analytically from the Bayesian model.
  SLUG: conspiracy_bayes_2026
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS into every Author and Reviewer prompt]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every pass]

Run the full milestone pipeline: M1 -> M2 -> M3 -> M4.
Do not skip milestones. Do not open M2 until M1 is Peer Reviewer ACCEPT.
Halt only on HALT CONDITIONS.
When done write papers/conspiracy_bayes_2026/paper.md and halt.
James P Rice Jr. reviews it.
