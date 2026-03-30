# INIT — GRAPH-THEORETIC FRAGILITY OF SUPPLY CHAINS
# Pre-filled. Ready to run.
# claude --dangerously-skip-permissions papers/init_supply_chain.md

---

## INPUTS — ALL PRE-FILLED

PROJECT_NAME: Graph-Theoretic Fragility of Supply Chains: Percolation Thresholds and Cascading Failures
SLUG: supply_chain_2026
AUTHOR: James P Rice Jr.
TARGET_VENUE: Operations Research
PIPELINE: PAPER

PROBLEM:
Models a supply chain as a directed graph and derives the percolation threshold —
the fraction of nodes that must fail before the network loses connectivity. Proves
that just-in-time supply chains (low redundancy, high betweenness centrality) have
percolation thresholds significantly lower than random graphs of the same density.
Derives closed-form expressions for the critical failure fraction as a function of
degree distribution. Shows power-law supply networks are maximally fragile. The
central contribution is translating percolation theory from undirected to directed
graphs with empirical supply chain topology, proving that the structure corporate
supply chains have converged on (hub-and-spoke, just-in-time, power-law degree
distribution) is precisely the structure that minimizes resilience.

FROZEN_SPEC_PARAMETERS:

PARAMETER: Percolation threshold for random graphs
VALUE: p_c = 1/<k> where <k> = mean degree
UNIT: fraction of nodes
TOLERANCE: exact for Erdos-Renyi; Molloy-Reed criterion for general degree distributions
SOURCE: Erdos-Renyi 1960; Molloy & Reed 1995 | Random Structures & Algorithms 6(2-3):161-180
NOTES: The Molloy-Reed criterion states a giant component exists iff
       sum(k(k-2)*P(k)) > 0. This is the baseline for comparison. The paper must
       derive the directed-graph analog.
DRIFT_RISK: LOW — well-established result

PARAMETER: Directed graph connectivity
VALUE: Strong connectivity (every node reachable from every other) vs weak
       connectivity (connected if direction ignored)
UNIT: N/A
TOLERANCE: N/A
SOURCE: Standard graph theory (Diestel 2017, Graph Theory, 5th ed.)
NOTES: Supply chains require strong connectivity for full functionality but may
       survive on weak connectivity in degraded mode. Both thresholds must be derived.
       The gap between them is the "fragility window."
DRIFT_RISK: HIGH — Author may use undirected percolation results where directed
             results are needed. Must use directed percolation throughout.

PARAMETER: Power-law exponent for supply networks
VALUE: gamma ~ 2.1-2.5
UNIT: dimensionless
TOLERANCE: range from empirical studies
SOURCE: Brintrup et al. 2018 | International Journal of Production Research 56(13):4438-4461;
        Perera et al. 2017 | PLOS ONE 12(1):e0169816
NOTES: Power-law degree distributions with gamma < 3 have diverging second moment,
       which drives the percolation threshold to zero in the infinite network limit.
       This is the mathematical root of supply chain fragility.
DRIFT_RISK: MEDIUM — Author may use generic power-law results without citing
             supply-chain-specific topology studies

PARAMETER: Cascading failure model
VALUE: Threshold model on directed graph — node i fails if fraction of failed
       in-neighbors exceeds threshold theta_i
UNIT: N/A
TOLERANCE: theta explored parametrically (0.1 to 0.9)
SOURCE: Watts 2002 | PNAS 99(9):5766-5771
NOTES: Watts (2002) is for undirected networks. The paper must adapt the cascade
       model to directed graphs where in-degree and out-degree play different roles.
DRIFT_RISK: HIGH — Author may cite Watts without adapting to directed case

PARAMETER: Betweenness centrality
VALUE: Defined on directed graph; nodes with high betweenness are critical
UNIT: dimensionless
TOLERANCE: N/A
SOURCE: Freeman 1977; Brandes 2001
NOTES: JIT supply chains concentrate flow through few high-betweenness nodes.
       The paper must show that removing high-betweenness nodes accelerates
       cascading failure and lowers the effective percolation threshold.
DRIFT_RISK: MEDIUM — Author may mention betweenness without proving its role formally

MILESTONES:

M1: Graph model + definitions — define the supply chain as a directed graph.
    Define strong vs weak connectivity. Adapt the Molloy-Reed criterion to
    directed graphs. Define the cascading failure model on directed graphs.
    Establish notation. Show why undirected percolation theory is insufficient.

M2: Percolation threshold proofs — derive the percolation threshold for directed
    random graphs (Erdos-Renyi directed analog). Derive the threshold for directed
    power-law graphs with exponent gamma. Prove Theorem 1: for gamma < 3, the
    strong connectivity percolation threshold approaches 0 as N -> infinity.
    Prove Theorem 2: JIT networks (high betweenness concentration) have lower
    effective thresholds than random networks of the same density.

M3: Power-law fragility + resilience index + boundary conditions — define a
    resilience index combining percolation threshold and cascade speed. Show
    power-law supply networks minimize this index. Derive conditions under which
    adding redundancy (increasing minimum degree) raises the threshold above a
    target. Boundary conditions: gamma -> 2 (maximally fragile), gamma -> infinity
    (approaches Poisson), theta -> 0 (maximally sensitive cascades).
    Sensitivity analysis table.

M4: Full paper — Introduction (supply chain fragility as a graph theory problem),
    Related work (Albert et al. 2000, Watts 2002, Brintrup et al. 2018),
    Discussion (policy implications — redundancy requirements, diversification,
    stress testing), Conclusion. Self-contained Abstract.

ORACLE:
The model is valid if and only if:
1. The supply chain is modeled as a directed graph with explicit degree distributions
2. Percolation thresholds are derived for directed graphs, not cited from undirected theory
3. The power-law fragility result (gamma < 3 -> threshold -> 0) is proven as a theorem
4. The cascading failure model is adapted to directed graphs (in-degree/out-degree)
5. Strong vs weak connectivity thresholds are both derived

Peer Reviewer must verify: are the percolation thresholds derived for directed graphs,
or are undirected results cited without adaptation? If the latter, REJECT.

KNOWN_DRIFT_RISKS:
- Using undirected graph theory where directed is needed — supply chains are
  inherently directed (supplier -> manufacturer -> distributor)
- Citing Erdos-Renyi or Molloy-Reed percolation thresholds without deriving the
  directed-graph analogs
- Not distinguishing strong from weak connectivity — both matter for supply chains
  and the gap between them is the fragility window
- Using Watts (2002) cascade model without adapting to directed graphs where
  in-degree and out-degree play asymmetric roles
- Citing power-law exponents without supply-chain-specific sources
- Making the model too abstract — must connect to actual supply chain topology
  (JIT, hub-and-spoke, tier structure)
- Adding unnecessary simulation when analytical results are available —
  keep it analytical, use simulation only for validation
- Skipping the resilience index derivation or leaving it informal
- Failing to address targeted attacks (high-betweenness removal) vs random failures
  — both must be analyzed and compared
- Orphan figure references — every figure must have Python/matplotlib code.
  The paper should include at minimum:
    Figure 1: Percolation threshold vs gamma for directed power-law graphs
    Figure 2: Cascade size vs initial failure fraction (random vs targeted)
    Figure 3: Resilience index as a function of redundancy (minimum degree)

---

## SETUP SEQUENCE — EXECUTE NOW

### Step 1 — Create project directory
Create D:\EXPERIMENTS\SUPPLY_CHAIN\ with:
  spec/, state/, outputs/, results/raw/, results/validated/, results/final/,
  devlog/, src/, papers/, papers/supply_chain_2026/,
  papers/supply_chain_2026/figures/, prompts/

### Step 2 — Write CLAUDE.md
  # Graph-Theoretic Fragility of Supply Chains — NORTH STAR

  ## What We Are Building
  A directed-graph percolation model proving power-law supply chains are
  maximally fragile, with closed-form percolation thresholds.

  ## The Core Claim
  For power-law supply networks with gamma < 3, the strong connectivity
  percolation threshold approaches zero as network size grows. JIT supply
  chains have converged on the most fragile possible topology.

  ## Frozen Parameters (quick reference)
  | Parameter | Value | Source |
  |-----------|-------|--------|
  | Random graph p_c | 1/<k> | Erdos-Renyi / Molloy-Reed |
  | Connectivity | Strong vs weak (directed) | Standard graph theory |
  | Power-law gamma | 2.1-2.5 | Brintrup et al. 2018 |
  | Cascade model | Threshold on directed graph | Watts 2002 adapted |

  ## Critical Enforcements
  - Directed graph throughout — not undirected
  - Percolation thresholds derived, not cited from undirected theory
  - Strong vs weak connectivity both analyzed
  - Power-law fragility is a theorem, not an observation

### Step 3 — Write spec/frozen_spec.md
Fill from FROZEN_SPEC_PARAMETERS above. Lock date today.
Locked by: James P Rice Jr.

### Step 4 — Initialize state files
state/state_vector.md — TURN: 0, MILESTONE: M1, MODE: INIT
state/innovation_log.md — header with project name and timestamp
state/dead_ends.md — header with project name

### Step 5 — Copy all prompts from SHELL
Copy from D:\EXPERIMENTS\SHELL\prompts\ into D:\EXPERIMENTS\SUPPLY_CHAIN\prompts\:
  04_paper_orchestrator.md
  05_author.md
  06_peer_reviewer.md
  07_editor.md
  run_milestone.md
Do NOT copy 00_init.md — SHELL-level only.

Also write prompts/turn_prompts_log.md:
  # TURN PROMPTS LOG — supply_chain_2026
  # Every exact prompt logged here. Required for reproducibility.
  [No entries yet. First entry written at Turn 1 M1.]

### Step 5b — Write run_pipeline.ps1

Write run_pipeline.ps1 in the project root (D:\EXPERIMENTS\SUPPLY_CHAIN\) with
the slug set to "supply_chain_2026". Use the template from
D:\EXPERIMENTS\SHELL\prompts\00_init.md Step 15, replacing [SLUG] with
supply_chain_2026 and [SLUG] paths with SUPPLY_CHAIN.

### Step 6 — Write STATUS.md
Phase: INIT -> PAPER PIPELINE
Turn: 0
What Is Done: Scaffolded. Spec locked.
What Is Next: Author writes M1 (directed graph model, connectivity definitions, cascade model).

### Step 7 — Write remaining required files

Write README.md:
  # Graph-Theoretic Fragility of Supply Chains
  **Author:** James P Rice Jr.
  **Target:** Operations Research
  **Status:** In progress
  ## What This Is
  A directed-graph percolation model of supply chain fragility. Power-law networks
  are maximally fragile. Percolation thresholds derived in closed form.
  ## How to Run
  claude --dangerously-skip-permissions prompts/04_paper_orchestrator.md

Write CHAIN_PROMPT.md:
  # CHAIN PROMPT — Supply Chain Fragility Paper | THIS FILE WINS ALL CONFLICTS
  Name: Graph-Theoretic Fragility of Supply Chains
  Author: James P Rice Jr.
  Core claim: Power-law supply networks with gamma < 3 have percolation thresholds
  approaching zero. JIT supply chains are maximally fragile by construction.
  Pipeline: PAPER — Claude-only, milestone-by-milestone gating.
  Author: Claude | Peer Reviewer: Claude | Editor: Claude
  [today] | Initialized from SHELL v3

Write SACRED_FILES.md:
  # SACRED FILES | Lock date: [today] | Locked by: James P Rice Jr.
  | File | Reason | Locked |
  |------|--------|--------|
  | spec/frozen_spec.md | Oracle. Never modify after lock. | [today] |

Write BEST_PRACTICES.md:
  # BEST PRACTICES — Supply Chain Fragility Paper | SHELL v3 standards
  - Directed graph formalism throughout — never undirected.
  - Percolation thresholds derived for directed graphs, not cited from undirected.
  - Strong vs weak connectivity both analyzed; gap = fragility window.
  - Cascading failure model adapted to directed graphs (in-degree/out-degree asymmetry).
  - Natural enemy: Albert et al. 2000 — must distinguish from their undirected results.
  - Sensitivity analysis: gamma in [2.0-3.5], theta in [0.1-0.9], targeted vs random.
  - Milestone-by-milestone. No section opens until previous is Peer Reviewer ACCEPT.
  - Every figure needs Python/matplotlib code. No orphan figure references.
  - Lean-ready proofs: all hypotheses explicit, every derivation step justified.

Write devlog/DEV_LOG.md:
  # DEVELOPMENT LOG — supply_chain_2026
  ## [today] — Session 1
  Initialized from SHELL v3. Spec locked. All files created. Git initialized.
  Pipeline: PAPER, Claude-only, milestone-by-milestone gating.
  Models: Claude (Author) -> Claude (Peer Reviewer) -> Claude (Editor).

Write outputs/options.md:
  # OPTIONS LOG — supply_chain_2026
  [No options yet.]

Write outputs/state_vector_backup.md:
  # STATE VECTOR BACKUP — supply_chain_2026
  [No backups yet.]

### Step 8 — Initialize git
  cd D:\EXPERIMENTS\SUPPLY_CHAIN
  git init
  git add -A
  git commit -m "Turn 0 | Init | supply_chain_2026"

### Step 9 — Print confirmation and hand off:
  PROJECT INITIALIZED: supply_chain_2026
  Spec locked. All files created. Git initialized.
  Beginning paper pipeline — M1 (Graph Model + Definitions) first.
  Output: papers/supply_chain_2026/paper.md
  Running. James P Rice Jr. reviews when done.

---

## HAND OFF — EXECUTE PAPER PIPELINE

DO NOT STOP HERE. The setup is complete. Now you must execute the paper pipeline.

Read prompts/04_paper_orchestrator.md NOW and follow every instruction in it.
You are the Orchestrator. Begin at the INITIALIZE section. This is not a file
to summarize — it is your operating manual. Execute it.

YOUR INPUTS:
  PROBLEM: [the full PROBLEM text from the INPUTS section above]
  DATA: No empirical data beyond cited topology parameters in frozen spec. All results derived analytically from directed graph percolation theory.
  SLUG: supply_chain_2026
  DRIFT_RISKS: [paste KNOWN_DRIFT_RISKS above into every Author and Reviewer prompt]
  FROZEN_SPEC: [pass full frozen_spec.md to Peer Reviewer on every review pass]

BEGIN NOW. Run M1. Do not ask for confirmation. Do not summarize the orchestrator.
Execute it. Write the paper.
