# INIT — MISINFORMATION PERSISTENCE AS EQUILIBRIUM
# EXECUTE IMMEDIATELY. Do not summarize, analyze, or ask questions.
# Read the INPUTS below, then execute the SETUP SEQUENCE step by step.
# Load prompts/00_init.md for the setup procedure, then run it with these inputs.
# This is not a document to review — it is a set of instructions to follow NOW.
#
# Paper 3 of 3 in the Bayesian Epistemology Trilogy:
#   Paper 1: Conspiracy Beliefs as Bayesian Updating (hidden variable model)
#   Paper 2: Echo Chambers as Bayesian Network Partitioning (network fragmentation)
#   Paper 3: Misinformation Persistence as Equilibrium (this paper)
#
# This paper unifies Papers 1 and 2: agents who update rationally (Paper 1)
# in possibly partitioned networks (Paper 2) face a costly correction game.
# Even when every agent is perfectly Bayesian, misinformation persists as a
# Nash equilibrium because correction is a public good with private costs.
#
# Pre-filled. Ready to run.
# claude --dangerously-skip-permissions papers/init_misinformation.md

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Misinformation Persistence as Equilibrium: Costly Correction in Bayesian Networks
SLUG: misinformation_equilibrium_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: Games and Economic Behavior
PIPELINE: PAPER

PROBLEM:
Why does misinformation persist even among rational agents who could, in principle,
correct it? This paper proves that misinformation persistence is a Nash equilibrium
when correction is costly. We integrate the Bayesian updating framework from Paper 1
(agents with posteriors theta_i over a hidden variable) with the network topology
from Paper 2 (graph G, possibly partitioned into echo chambers). Each agent can pay
a cost c > 0 to broadcast a correction signal that shifts neighbors' posteriors toward
the truth. We prove the existence of a critical correction cost threshold c* above
which the "misinformed equilibrium" — all agents abstain from correcting — is the
unique stable Bayesian Nash Equilibrium. Below c*, correction cascades can occur.
The central contribution is showing that misinformation persistence is not a failure
of rationality (Paper 1 showed beliefs are rational) or a failure of network structure
alone (Paper 2 showed clustering is structural) — it is the rational outcome of a
costly public goods game played on a Bayesian network. Paper 1 explains WHY people
believe misinformation (rational updating on hidden variables). Paper 2 explains
WHY it clusters (network partitioning). This paper explains WHY nobody fixes it
(costly correction with free-riding). Pure formal theory — no empirical data needed.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Agent belief model (from Paper 1)
VALUE: Each agent i holds posterior theta_i = P(H_c | E_i^1, ..., E_i^n) via
       sequential Bayesian updating on hidden variable H_c vs H_n.
       Prior: pi_0 > 0. Likelihood ratios Lambda_k as defined in Paper 1.
UNIT: probability
TOLERANCE: exact — inherits Paper 1 framework without modification
SOURCE: Paper 1 (Conspiracy Beliefs as Bayesian Updating), Theorem 1
NOTES: Agents are heterogeneous in their posteriors theta_i because they have
       observed different evidence sequences. An agent is "misinformed" if
       theta_i > 0.5 when the true state is H_n (no conspiracy). The posterior
       theta_i is the agent's type in the game-theoretic model.
DRIFT_RISK: LOW — standard import from Paper 1, but must be explicitly connected

PARAMETER: Network topology (from Paper 2)
VALUE: Undirected graph G = (V, E) where V = {1, ..., N} agents and E = edges.
       G may be partitioned: G = G_1 union G_2 union ... union G_K with
       limited cross-partition edges. Adjacency matrix A. Degree d_i for agent i.
       Critical connectivity threshold tau from Paper 2.
UNIT: graph structure
TOLERANCE: exact — inherits Paper 2 framework
SOURCE: Paper 2 (Echo Chambers as Bayesian Network Partitioning)
NOTES: The network determines who receives a correction signal. If G is
       partitioned below the critical threshold tau (Paper 2), correction
       signals cannot propagate across partitions regardless of cost.
       This creates interaction between Paper 2's structural result and
       Paper 3's strategic result.
DRIFT_RISK: MEDIUM — must use Paper 2's specific partition model, not a
             generic network; the critical connectivity threshold tau must
             appear explicitly

PARAMETER: Action space
VALUE: Each agent i chooses a_i in {correct, abstain}.
       If a_i = correct: agent pays cost c and broadcasts signal s to all
       neighbors j in N(i) = {j : (i,j) in E}.
       If a_i = abstain: agent pays nothing and broadcasts nothing.
UNIT: binary action
TOLERANCE: exact
SOURCE: Novel formalization — this paper's framework
NOTES: The action space is intentionally simple (binary). Extensions to
       continuous effort or targeted correction are discussed in Discussion
       but not modeled in the core results. The binary choice isolates the
       free-riding incentive cleanly.
DRIFT_RISK: LOW — temptation to add continuous effort levels; resist until
             binary case is fully solved

PARAMETER: Correction cost
VALUE: c > 0, constant per broadcast. Agent i who corrects pays c regardless
       of the number of neighbors reached. Cost represents: time, social risk,
       cognitive effort, reputation cost of contradicting group consensus.
UNIT: utility (normalized)
TOLERANCE: c explored parametrically; key threshold c* derived analytically
SOURCE: Novel — this paper's framework
NOTES: The constant-cost assumption is a simplification. The key insight is
       that any positive cost creates a free-riding incentive. Variable cost
       c_i (heterogeneous) is an extension but does not change the qualitative
       result: a threshold still exists.
DRIFT_RISK: MEDIUM — must not assume c = 0 or c -> infinity; the interesting
             regime is intermediate c near c*

PARAMETER: Correction signal
VALUE: Public signal s that, when received by agent j, causes Bayesian update:
       theta_j' = theta_j * Lambda_s / (theta_j * Lambda_s + (1-theta_j))
       where Lambda_s = P(s|H_n) / P(s|H_c) < 1 (signal favors truth H_n).
       Signal strength: |log(Lambda_s)| > 0.
UNIT: likelihood ratio (dimensionless)
TOLERANCE: Lambda_s explored parametrically; must satisfy Lambda_s < 1
SOURCE: Derived from Paper 1's likelihood ratio framework
NOTES: The correction signal is transparency-type evidence (Paper 1, Theorem 3).
       It shifts posteriors toward truth. The key constraint: one signal shifts
       one agent's posterior by a bounded amount. Correcting a highly misinformed
       agent (theta_i close to 1) requires multiple signals or very strong Lambda_s.
       Signal strength is finite — correction is not instantaneous persuasion.
DRIFT_RISK: HIGH — must not model correction as "instantly setting theta = 0";
             correction works through the Bayesian update mechanism from Paper 1

PARAMETER: Equilibrium concept
VALUE: Bayesian Nash Equilibrium (BNE). Agent i's strategy sigma_i: [0,1] -> {correct, abstain}
       maps type theta_i to action. Strategy profile sigma* is BNE if for all i:
       E[u_i(sigma_i*, sigma_{-i}*) | theta_i] >= E[u_i(a_i, sigma_{-i}*) | theta_i]
       for all a_i in {correct, abstain}.
UNIT: N/A (solution concept)
TOLERANCE: exact — standard game theory
SOURCE: Harsanyi 1967-68 (Bayesian games)
NOTES: Types are the posteriors theta_i. The BNE concept is essential because
       agents have private information (their evidence histories and posteriors).
       Must not simplify to complete information Nash equilibrium — the Bayesian
       structure from Paper 1 is the whole point.
DRIFT_RISK: HIGH — must use BNE, not plain Nash equilibrium; the incomplete
             information (private posteriors) is what connects to Paper 1

PARAMETER: Critical correction cost threshold c*
VALUE: c* = f(G, Lambda_s, {theta_i}) — derived analytically.
       When c > c*, the misinformed equilibrium (all abstain) is the unique
       stable BNE. When c < c*, correction equilibria exist.
       c* depends on: network structure G (degree distribution, partition structure),
       signal strength |log(Lambda_s)|, distribution of posteriors {theta_i}.
UNIT: utility (normalized)
TOLERANCE: exact derivation of c* as a function of model primitives
SOURCE: Novel — this paper's central result
NOTES: The main theorem. c* must be expressed in closed form (or characterized
       by conditions) as a function of the network topology, signal strength,
       and belief distribution. The dependence on G connects to Paper 2: more
       partitioned networks have higher c* (correction is less effective when
       the network is fragmented). The dependence on {theta_i} connects to
       Paper 1: more entrenched beliefs (higher theta_i) require stronger
       correction, raising c*.
DRIFT_RISK: HIGH — this is the central result; must be a theorem with proof,
             not a simulation result or conjecture

PARAMETER: Free-riding condition
VALUE: Correction is a public good: if agent i corrects, all neighbors j in N(i)
       benefit (posteriors shift toward truth) but only i pays cost c.
       Marginal private benefit of correcting: b_i = sum_{j in N(i)} v(Delta theta_j)
       where Delta theta_j is the posterior shift and v() is the value function.
       Free-riding: if b_i < c, agent i strictly prefers to abstain and let
       others correct.
UNIT: utility comparison
TOLERANCE: exact
SOURCE: Public goods theory (Samuelson 1954; Olson 1965)
NOTES: The public goods structure is what makes this a game theory paper, not
       just applied Bayesian epistemology. The free-riding condition must be
       derived from the payoff structure, not assumed. Must show: even agents
       who KNOW the truth (theta_i near 0) may rationally abstain from correcting
       because the private cost exceeds their private benefit from others being
       informed.
DRIFT_RISK: HIGH — must not reduce to a generic public goods game; the Bayesian
             structure (theta_i determines both who needs correction and who
             values it) is what distinguishes this from standard models

PARAMETER: Stability condition
VALUE: The misinformed equilibrium (all abstain) is stable when c > c* in the
       sense that no unilateral deviation (single agent switching to correct)
       is profitable, AND no coalition of size k < k*(G) can profitably deviate.
       k*(G) is the minimum coalition size for profitable group correction.
       k*(G) depends on network structure from Paper 2.
UNIT: N/A (equilibrium property)
TOLERANCE: exact — must prove both unilateral and coalitional stability
SOURCE: Novel — extends standard Nash stability to coalition-proofness
NOTES: Unilateral stability (no single agent deviates) is necessary but not
       sufficient. Must also characterize k*(G): the minimum group size that
       can profitably coordinate correction. In highly partitioned networks
       (Paper 2), k*(G) is large because correction must reach across partitions.
       This connects the game-theoretic result to the network structure result.
DRIFT_RISK: MEDIUM — may prove only unilateral stability and miss coalitional
             analysis; both are needed for the "persistence" claim

MILESTONES:

M1: Game-theoretic model + definitions — Define the correction game formally.
    Import agent model from Paper 1 (posteriors theta_i, Bayesian updating,
    likelihood ratios). Import network model from Paper 2 (graph G, partitions,
    critical connectivity threshold tau). Define action space {correct, abstain},
    cost c, correction signal s with likelihood ratio Lambda_s, and payoff
    function u_i. Define the Bayesian Nash Equilibrium concept for this game.
    State the connection to public goods theory. Establish notation consistent
    with Papers 1 and 2. Clearly state what is imported vs. novel.

M2: Main theorems — Prove Theorem 1 (Existence of c*): there exists a critical
    cost threshold c* such that for c > c*, the all-abstain profile is the unique
    stable BNE. Derive c* in closed form as a function of G, Lambda_s, and {theta_i}.
    Prove Theorem 2 (Network dependence): c* is increasing in network fragmentation
    (more partitioned networks from Paper 2 have higher c*, making correction
    harder). Formally: c*(G) > c*(G') if G is more partitioned than G' in the
    sense of Paper 2. Prove Theorem 3 (Belief dependence): c* is increasing in
    belief entrenchment (higher average theta_i raises c*, connecting to Paper 1's
    convergence result). Prove Theorem 4 (Coalition threshold): derive k*(G),
    the minimum coalition size for profitable group correction.

M3: Interaction effects + comparative statics — Prove Theorem 5 (Trilogy
    interaction): combine Paper 1's convergence (theta_i -> 1 under secrecy),
    Paper 2's partitioning (G fragments below tau), and this paper's costly
    correction (c > c*) to show a "misinformation trap": secrecy drives beliefs
    up (Paper 1), network fragments (Paper 2), and correction becomes unprofitable
    (Paper 3), creating a self-reinforcing cycle. Derive comparative statics:
    dc*/d(Lambda_s), dc*/d(connectivity), dc*/d(mean theta). Characterize the
    parameter regions where correction equilibria exist. Boundary conditions:
    c -> 0 (costless correction — always corrected), c -> infinity (no correction),
    fully connected G (easiest correction), fully partitioned G (impossible correction),
    all theta_i = 0 (no misinformation to correct). Sensitivity analysis table.

M4: Full paper — Introduction (why misinformation persists among rational agents),
    Related work (public goods and information: Bergemann & Valimaki 2002,
    Acemoglu et al. 2010, Banerjee et al. 2013; misinformation models:
    Vosoughi et al. 2018, Pennycook & Rand 2019; game theory of communication:
    Crawford & Sobel 1982, Kartik 2009). Discussion (policy implications: reducing
    correction cost is more effective than "debunking"; platform design;
    limitations of binary action model; relationship to mechanism design).
    Explicit trilogy summary: how Papers 1+2+3 form a complete theory.
    Conclusion. Self-contained Abstract.

ORACLE:
The model is valid if and only if:
1. The correction game is formally defined with explicit payoffs, types, and strategies
2. The agent model imports Paper 1's Bayesian updating framework — agents hold posteriors
   theta_i that update via likelihood ratios, not abstract "beliefs"
3. The network imports Paper 2's partition structure — graph G with critical
   connectivity threshold tau, not a generic network
4. The critical cost threshold c* is derived analytically as a function of
   model primitives (G, Lambda_s, {theta_i}), not simulated or conjectured
5. The free-riding result emerges from the Bayesian public goods structure,
   not from a generic public goods game with relabeled variables
6. The stability result covers both unilateral and coalitional deviations
7. The interaction between all three papers is proven as a theorem (the
   misinformation trap), not merely discussed narratively

Peer Reviewer must verify: is the critical cost threshold c* a proven theorem
with an explicit formula or characterization in terms of model primitives?
Does the free-riding result depend essentially on the Bayesian structure from
Paper 1 and the network structure from Paper 2, or could it have been derived
from a generic public goods model? If the latter, REJECT — the paper must
demonstrate that the Bayesian-network structure creates phenomena that a
standard public goods model cannot capture.

KNOWN_DRIFT_RISKS:
- Reducing to a generic public goods game — the MOST DANGEROUS drift risk.
  This paper is NOT just "public goods on a network." The Bayesian structure
  from Paper 1 (agents have private posteriors that update via likelihood ratios)
  and the partition structure from Paper 2 (network fragments at threshold tau)
  must be ESSENTIAL to the results. If you can derive the same c* without
  Bayesian updating or without network partitions, the paper has drifted into
  a standard public goods model and lost its contribution.
- Disconnecting from Paper 1 — must use Paper 1's specific framework: hidden
  variable H_c vs H_n, sequential Bayesian updating, likelihood ratios Lambda_k,
  convergence theorem. Agents' types ARE their posteriors theta_i from Paper 1.
  Do not introduce a new belief model.
- Disconnecting from Paper 2 — must use Paper 2's specific framework: graph G
  with partitions, critical connectivity threshold tau. The network is not just
  "who talks to whom" — it has the specific fragmentation structure from Paper 2.
  c* must depend on tau explicitly.
- Using complete information Nash equilibrium instead of BNE — agents have private
  posteriors (their evidence histories from Paper 1 are private). This is an
  incomplete information game. BNE is the correct solution concept. Using plain
  Nash equilibrium discards the connection to Paper 1.
- Modeling correction as instant persuasion — correction works through the Bayesian
  update mechanism from Paper 1. A correction signal has likelihood ratio Lambda_s
  and shifts posteriors by a bounded amount. It does not "set beliefs to truth."
  Multiple corrections may be needed for entrenched beliefs.
- Proving only unilateral stability — must also characterize coalitional stability
  (minimum coalition size k*(G) for profitable group correction). The persistence
  claim requires showing that even small groups cannot profitably deviate.
- Making the "misinformation trap" theorem narrative instead of formal — the
  interaction of Papers 1+2+3 (secrecy -> belief entrenchment -> network fragmentation
  -> costly correction -> persistence) must be a proven theorem with explicit conditions,
  not a verbal argument in the Discussion section.
- PROOF STRATEGY: The c* derivation should use the marginal benefit of correction.
  Agent i's benefit from correcting = sum over neighbors j of the value of shifting
  theta_j. This depends on: (a) the network (how many neighbors, from Paper 2),
  (b) the signal strength (Lambda_s, from Paper 1's framework), and (c) the current
  beliefs (theta_j, from Paper 1). The threshold c* is where marginal benefit =
  marginal cost for the pivotal agent. Derive this explicitly.
- PROOF STRATEGY: The coalition threshold k*(G) should be derived from the structure
  of G. In a complete graph, k* = 1 (one corrector reaches everyone). In a partitioned
  graph, k* >= K (need at least one corrector per partition). Derive the general
  formula.
- FORMALIZATION: Payoffs must be explicitly specified. Suggested structure:
  u_i(correct) = -c + beta * sum_{j in N(i)} [theta_j - theta_j'] (benefit from
  shifting neighbors toward truth)
  u_i(abstain) = beta * sum_{j in N(i)} [theta_j - theta_j''] (benefit from others'
  corrections, which agent i free-rides on)
  where beta is the altruism/externality weight and theta_j' < theta_j is the
  post-correction posterior. Make this concrete.
- Ignoring the role of the truth-knowing agents — some agents may have theta_i near 0
  (they know the truth from Paper 1). These are the potential correctors. Must analyze
  their incentives specifically, not treat all agents symmetrically.
- Orphan figure references — every figure must have Python/matplotlib code.
  The paper should include at minimum:
    Figure 1: Phase diagram in (c, connectivity) space showing correction vs.
              misinformed equilibrium regions
    Figure 2: c* as a function of network fragmentation (connecting to Paper 2)
    Figure 3: c* as a function of average belief entrenchment (connecting to Paper 1)
    Figure 4: The misinformation trap — trajectory through (belief, fragmentation,
              correction cost) space showing self-reinforcing cycle

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory
Create C:\PROJECTS\SHELL\papers\MISINFORMATION_EQUILIBRIUM\ with:
  spec/, state/, outputs/, results/raw/, results/validated/, results/final/,
  devlog/, src/, papers/, papers/misinformation_equilibrium_2026/,
  papers/misinformation_equilibrium_2026/figures/, prompts/

### Step 2 — Write CLAUDE.md
  # Misinformation Persistence as Equilibrium — NORTH STAR

  ## What We Are Building
  A game-theoretic proof that misinformation persists as a Nash equilibrium
  when correction is costly, integrating Bayesian updating (Paper 1) with
  network partitioning (Paper 2) into a costly correction game.

  ## The Core Claim
  There exists a critical correction cost threshold c* such that for c > c*,
  the all-abstain (misinformed) equilibrium is the unique stable Bayesian Nash
  Equilibrium. c* depends on network structure (Paper 2) and belief entrenchment
  (Paper 1), creating a "misinformation trap" when secrecy, fragmentation, and
  costly correction reinforce each other.

  ## Trilogy Position
  Paper 1: WHY people believe it (rational Bayesian updating on hidden variables)
  Paper 2: WHY it clusters (network partitioning at critical threshold)
  Paper 3: WHY nobody fixes it (costly correction game — THIS PAPER)

  ## Frozen Parameters (quick reference)
  | Parameter | Value | Source |
  |-----------|-------|--------|
  | Agent model | theta_i = P(H_c given E_i) via Bayes | Paper 1 |
  | Network | G = (V,E), partitions, threshold tau | Paper 2 |
  | Actions | {correct, abstain} | Novel |
  | Cost | c > 0 per broadcast | Novel |
  | Signal | Lambda_s < 1 (truth-favoring) | Paper 1 framework |
  | Equilibrium | Bayesian Nash Equilibrium | Harsanyi |
  | Key result | c* = critical cost threshold | Novel |

  ## Critical Enforcements
  - BNE with private types (posteriors from Paper 1), NOT complete-information Nash
  - Correction works through Bayesian updating (Paper 1), not instant persuasion
  - Network is Paper 2's partition model with threshold tau, not generic graph
  - Free-riding emerges from Bayesian public goods structure, not relabeled standard model
  - c* derived analytically in closed form, not simulated
  - Misinformation trap theorem proven formally across all three papers

  ## References to Prior Papers
  Paper 1: C:\PROJECTS\SHELL\papers\CONSPIRACY_BAYES\
  Paper 2: (Echo Chambers as Bayesian Network Partitioning — when available)

### Step 3 — Write frozen_spec.md
Fill from FROZEN_SPEC_PARAMETERS above. Lock date today.
Locked by: James P Rice Jr.

### Step 4 — Initialize state files
state_vector.md — TURN: 0, MILESTONE: M1, MODE: INIT
innovation_log.md — header with project name and timestamp
dead_ends.md — header with project name

### Step 5 — Copy all prompts from SHELL
Copy from C:\PROJECTS\SHELL\prompts\ into C:\PROJECTS\SHELL\papers\MISINFORMATION_EQUILIBRIUM\prompts\:
  04_paper_orchestrator.md
  05_author.md
  06_peer_reviewer.md
  07_editor.md
  run_milestone.md
Do NOT copy 00_init.md — SHELL-level only.

Also write prompts/turn_prompts_log.md:
  # TURN PROMPTS LOG — misinformation_equilibrium_2026
  # Every exact prompt logged here. Required for reproducibility.
  [No entries yet. First entry written at Turn 1 M1.]

### Step 5b — Write run_pipeline.ps1

Write run_pipeline.ps1 in the project root (C:\PROJECTS\SHELL\papers\MISINFORMATION_EQUILIBRIUM\) with
the slug set to "misinformation_equilibrium_2026". Use the template from
C:\PROJECTS\SHELL\prompts\00_init.md Step 15, replacing [SLUG] with
misinformation_equilibrium_2026 and [SLUG] paths with MISINFORMATION_EQUILIBRIUM.

### Step 6 — Write STATUS.md
Phase: INIT -> PAPER PIPELINE
Turn: 0
What Is Done: Scaffolded. Spec locked.
What Is Next: Author writes M1 (Game-theoretic model, import Paper 1 agents, import Paper 2 network, define correction game).

### Step 7 — Write remaining required files

Write README.md:
  # Misinformation Persistence as Equilibrium: Costly Correction in Bayesian Networks
  **Author:** James P Rice Jr.
  **Target:** Games and Economic Behavior
  **Status:** In progress
  **Trilogy:** Paper 3 of 3 (Bayesian Epistemology Trilogy)
  ## What This Is
  A game-theoretic proof that misinformation persists as a Nash equilibrium when
  correction is costly. Integrates Bayesian updating (Paper 1) with network
  partitioning (Paper 2). Pure formal theory.
  ## How to Run
  claude --dangerously-skip-permissions prompts/04_paper_orchestrator.md

Write CHAIN_PROMPT.md:
  # CHAIN PROMPT — Misinformation Equilibrium Paper | THIS FILE WINS ALL CONFLICTS
  Name: Misinformation Persistence as Equilibrium: Costly Correction in Bayesian Networks
  Author: James P Rice Jr.
  Trilogy: Paper 3 of 3 (Bayesian Epistemology Trilogy)
  Core claim: Misinformation persists as a Bayesian Nash Equilibrium when correction
  cost c exceeds threshold c*. c* depends on network structure (Paper 2) and belief
  entrenchment (Paper 1). The "misinformation trap" is a self-reinforcing cycle
  across all three papers.
  Pipeline: PAPER — Claude-only, milestone-by-milestone gating.
  Author: Claude | Peer Reviewer: Claude | Editor: Claude
  [today] | Initialized from SHELL v3

Write SACRED_FILES.md:
  # SACRED FILES | Lock date: [today] | Locked by: James P Rice Jr.
  | File | Reason | Locked |
  |------|--------|--------|
  | frozen_spec.md | Oracle. Never modify after lock. | [today] |

Write BEST_PRACTICES.md:
  # BEST PRACTICES — Misinformation Equilibrium Paper | SHELL v3 standards
  - BNE with private types, not complete-information Nash. Types = posteriors from Paper 1.
  - Correction via Bayesian updating (Paper 1 signals), not instant persuasion.
  - Network is Paper 2's partition model with threshold tau, not a generic graph.
  - c* derived analytically in closed form as function of model primitives.
  - Free-riding emerges from Bayesian structure, not relabeled standard public goods.
  - Misinformation trap theorem proven formally, not discussed narratively.
  - Must cite and position against Acemoglu et al. 2010 and Banerjee et al. 2013.
  - Milestone-by-milestone. No section opens until previous is Peer Reviewer ACCEPT.
  - Every figure needs Python/matplotlib code. No orphan figure references.
  - Lean-ready proofs: all hypotheses explicit, every derivation step justified.
  - Explicit references to Paper 1 and Paper 2 results throughout.

Write devlog/DEV_LOG.md:
  # DEVELOPMENT LOG — misinformation_equilibrium_2026
  ## [today] — Session 1
  Initialized from SHELL v3. Spec locked. All files created. Git initialized.
  Pipeline: PAPER, Claude-only, milestone-by-milestone gating.
  Models: Claude (Author) -> Claude (Peer Reviewer) -> Claude (Editor).
  Trilogy position: Paper 3 of 3. Builds on Paper 1 (conspiracy_bayes_2026)
  and Paper 2 (echo_chambers — forthcoming).

Write outputs/options.md:
  # OPTIONS LOG — misinformation_equilibrium_2026
  [No options yet.]

Write outputs/state_vector_backup.md:
  # STATE VECTOR BACKUP — misinformation_equilibrium_2026
  [No backups yet.]

### Step 8 — Initialize git
  cd C:\PROJECTS\SHELL\papers\MISINFORMATION_EQUILIBRIUM
  git init
  git add -A
  git commit -m "Turn 0 | Init | misinformation_equilibrium_2026"

### Step 9 — Print confirmation and hand off:
  PROJECT INITIALIZED: misinformation_equilibrium_2026
  Spec locked. All files created. Git initialized.
  Trilogy position: Paper 3 of 3 (Bayesian Epistemology Trilogy).
  Paper 1 (conspiracy_bayes_2026): agents believe misinformation rationally.
  Paper 2 (echo_chambers): misinformation clusters via network partitioning.
  Paper 3 (this paper): nobody corrects because correction is costly.
  Beginning paper pipeline — M1 (Game-Theoretic Model + Definitions) first.
  Output: papers/misinformation_equilibrium_2026/paper.md
  Running. James P Rice Jr. reviews when done.

---

## HAND OFF — EXECUTE PAPER PIPELINE

DO NOT STOP HERE. The setup is complete. Now you must execute the paper pipeline.

Read prompts/04_paper_orchestrator.md NOW and follow every instruction in it.
You are the Orchestrator. Begin at the INITIALIZE section. This is not a file
to summarize — it is your operating manual. Execute it.

YOUR INPUTS:
  PROBLEM: [the full PROBLEM text from the INPUTS section above]
  DATA: No empirical data. All results derived analytically from the game-theoretic model
        with Bayesian agents (Paper 1) on networks (Paper 2).
  SLUG: misinformation_equilibrium_2026
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS above into every Author and Reviewer prompt]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every review pass]

  PAPER 1 REFERENCE: C:\PROJECTS\SHELL\papers\CONSPIRACY_BAYES\
    Key imports: Hidden variable model (H_c vs H_n), sequential Bayesian updating,
    likelihood ratios Lambda_k, convergence theorem (Theorem 1), transparency mechanism
    (Theorem 3). Agents' types theta_i are posteriors from this framework.

  PAPER 2 REFERENCE: Echo Chambers as Bayesian Network Partitioning
    Key imports: Graph G = (V,E), partition structure, critical connectivity threshold tau,
    network fragmentation conditions. The network topology for the correction game.

BEGIN NOW. Run M1. Do not ask for confirmation. Do not summarize the orchestrator.
Execute it. Write the paper.
