# Common Knowledge in One Step: A Deterministic Mechanism for Coordination via Constrained Information Architecture

**James P. Rice Jr.**

## Abstract

The infinite regress of nested beliefs required by common knowledge -- every agent knows, every agent knows every agent knows, ad infinitum -- has been treated as an inherent obstacle to coordination in multi-agent systems. Halpern and Moses (1990) proved that common knowledge is unattainable in any system with unreliable message-passing channels, and Rubinstein (1989) demonstrated that arbitrarily many rounds of message confirmation fail to produce common knowledge when each message has a positive probability of loss. These impossibility results, however, are channel-specific: they apply to sequential message-passing architectures, not to all information architectures. This paper introduces a **Sacred File** -- a shared, immutable, simultaneously accessible information structure satisfying a Partition Collapse property -- and a **State Vector** -- an append-only audit trail recording agents' access. Within Aumann's (1976) partition model, we prove that the Partition Collapse property forces the meet of agents' information partitions to equal the partition induced by the Sacred File (Lemma 1), that any event encoded in the Sacred File is common knowledge at every state in which it holds (Theorem 1, Part A), and that the coordination event for the Stag Hunt is common knowledge at step 1 -- the first moment both agents access the Sacred File (Theorem 1, Part B). Under a payoff-dominant equilibrium selection principle, common knowledge of the coordination event yields the action profile (Stag, Stag) with payoff (2, 2), eliminating the risk-dominant equilibrium without repeated play, pre-play communication, or costly signaling (Theorem 2). The result transforms common knowledge from an epistemic primitive that must be assumed into a design property that can be constructed.

---

## Definitions Block

All notation introduced here is fixed for the remainder of the paper.

**Definition 1 (State Space).** Let $\Omega$ be a finite, non-empty set of states of the world. Each $\omega \in \Omega$ encodes a complete description of the environment: the payoff-relevant parameters, each agent's action choice, and all information that has been disclosed or withheld. We call $\Omega$ the **state space**.

**Definition 2 (Agent Set).** Let $N = \{1, 2\}$ be the set of agents. Both agents are rational in the decision-theoretic sense: given beliefs, each agent selects the action that maximizes expected utility.

**Definition 3 (Information Partition).** For each agent $i \in N$, let $\mathcal{P}_i$ be a partition of $\Omega$. The cell $\mathcal{P}_i(\omega)$ containing state $\omega$ is the set of states agent $i$ considers possible when the true state is $\omega$. We call $\mathcal{P}_i$ agent $i$'s **information partition** (Aumann 1976).

**Definition 4 (Knowledge Operator).** For agent $i \in N$ and event $E \subseteq \Omega$, define the **knowledge operator**:

$$K_i(E) = \{\omega \in \Omega : \mathcal{P}_i(\omega) \subseteq E\}$$

Agent $i$ **knows** $E$ at state $\omega$ if and only if $\omega \in K_i(E)$. That is, $i$ knows $E$ when every state $i$ considers possible is a member of $E$.

**Definition 5 (Mutual Knowledge).** For event $E \subseteq \Omega$, the **first-order mutual knowledge** of $E$ is:

$$M^1(E) = K_1(E) \cap K_2(E)$$

The $k$-th order mutual knowledge is defined recursively:

$$M^k(E) = M^1(M^{k-1}(E))$$

for $k \geq 2$, with $M^0(E) = E$. At depth $k$, every agent knows that every agent knows ... ($k$ times) ... that $E$ holds. Mutual knowledge at any finite depth $k$ does **not** entail mutual knowledge at depth $k+1$.

**Definition 6 (Common Knowledge).** Event $E$ is **common knowledge** at state $\omega$ if and only if:

$$\omega \in C(E) = \bigcap_{k=1}^{\infty} M^k(E)$$

Equivalently, following Aumann (1976), let $\mathcal{P}^* = \mathcal{P}_1 \wedge \mathcal{P}_2$ be the **meet** (finest common coarsening) of the agents' information partitions. Then $E$ is common knowledge at $\omega$ if and only if $\mathcal{P}^*(\omega) \subseteq E$. The infinite regress in the first characterization and the partition-meet in the second are logically equivalent, but the partition-meet formulation is the one we exploit.

**Definition 7 (Sacred File).** A **Sacred File** $S$ is a public information partition element defined as follows. Let $\mathcal{F} \subseteq 2^\Omega$ be a sub-$\sigma$-algebra of events. The Sacred File is a function $S : \Omega \to \mathcal{F}$ satisfying:

(i) **Publicity.** For all $\omega \in \Omega$ and all $i \in N$: $\mathcal{P}_i(\omega) \subseteq S(\omega)$. That is, every state agent $i$ considers possible is consistent with the content of $S$.

(ii) **Immutability.** $S$ is determined at $\omega$ prior to agents' action choices and cannot be altered by either agent. Formally, $S$ is $\mathcal{F}_0$-measurable, where $\mathcal{F}_0$ is the sub-$\sigma$-algebra of pre-play events.

(iii) **Partition Collapse.** For all $\omega \in \Omega$: $\mathcal{P}_1(\omega) = \mathcal{P}_2(\omega) = S(\omega)$. Both agents' information partitions coincide with the partition induced by $S$.

The Partition Collapse property is the decisive condition. It forces the meet $\mathcal{P}^* = \mathcal{P}_1 \wedge \mathcal{P}_2$ to equal the partition induced by $S$ itself, because when $\mathcal{P}_1 = \mathcal{P}_2$, the finest common coarsening of a partition with itself is that same partition. Any event $E$ that is a union of cells of $S$ is therefore common knowledge by Definition 6.

**Definition 8 (State Vector).** A **State Vector** $V$ is a function $V : \Omega \times T \to \mathcal{R}$, where $T = \{0, 1, 2, \ldots\}$ is a discrete time index and $\mathcal{R}$ is a record space, satisfying:

(i) **Completeness.** $V(\omega, t)$ encodes, for each agent $i \in N$, agent $i$'s action at time $t$ (if any), agent $i$'s declared partition cell at time $t$, and a timestamp.

(ii) **Append-Only Integrity.** For all $t' < t$: the component of $V(\omega, t)$ corresponding to time $t'$ equals $V(\omega, t')$. History cannot be revised.

(iii) **Mutual Accessibility.** For all $\omega \in \Omega$, $t \in T$, and $i \in N$: $V(\omega, t)$ is $\mathcal{P}_i$-measurable. Both agents observe the full State Vector at every time step.

The State Vector is the dynamic audit trail that tracks agents' interactions with $S$. Where $S$ encodes what is commonly known, $V$ records the sequence by which agents came to know it.

**Definition 9 (Stag Hunt Game).** The **Stag Hunt** is a two-player symmetric coordination game $G = (N, A, u)$ where $A = \{Stag, Hare\}$ is the common action set and the payoff function $u : A \times A \to \mathbb{R}^2$ is given by:

|  | Stag | Hare |
|---|---|---|
| **Stag** | (2, 2) | (0, 1) |
| **Hare** | (1, 0) | (1, 1) |

The game has two pure-strategy Nash equilibria: $(Stag, Stag)$ with payoff $(2, 2)$ and $(Hare, Hare)$ with payoff $(1, 1)$. The $(Stag, Stag)$ equilibrium is **payoff-dominant** (it Pareto-dominates all other outcomes). The $(Hare, Hare)$ equilibrium is **risk-dominant** (each agent's worst-case payoff from $Hare$ exceeds the worst-case payoff from $Stag$: $\min(1,1) = 1 > \min(2,0) = 0$). The equilibrium selection problem is: absent common knowledge of mutual rationality and the payoff structure, rational agents may settle on the risk-dominant equilibrium, forgoing the payoff-dominant one.

**Definition 10 (Rationality Event).** Define the event $R \subseteq \Omega$ as the set of states at which both agents are rational:

$$R = \{\omega \in \Omega : \text{for all } i \in N, \text{ agent } i \text{ maximizes expected utility given } \mathcal{P}_i(\omega)\}$$

**Definition 11 (Coordination Event).** Define the **coordination event** $E^* \subseteq \Omega$:

$$E^* = R \cap \{\omega \in \Omega : u \text{ is as specified in Definition 9}\}$$

$E^*$ is the event that both agents are rational and that the payoff structure is the Stag Hunt defined above. When $C(E^*)$ obtains -- that is, when $E^*$ is common knowledge -- we will show that, under the payoff-dominant equilibrium selection principle (Def 14), the selected equilibrium is $(Stag, Stag)$.

**Definition 12 (Sacred File Induced Partition).** Let $\mathcal{P}_S$ denote the partition of $\Omega$ induced by $S$, i.e., the partition whose cells are $\{S(\omega) : \omega \in \Omega\}$. By Partition Collapse (Def 7.iii), $\mathcal{P}_S = \mathcal{P}_1 = \mathcal{P}_2$.

**Definition 13 (Sacred File Encoding).** An event $E \subseteq \Omega$ is **$S$-encoded** if $E$ is a union of cells of $\mathcal{P}_S$. The Sacred File architecture requires that both the rationality event $R$ (Def 10) and the payoff structure event $\{\omega : u \text{ is as in Def 9}\}$ are $S$-encoded. This is a design requirement on the content of $S$: the Sacred File must encode enough information to distinguish rational from irrational states and to distinguish the game being played.

**Definition 14 (Payoff-Dominant Equilibrium Selection).** The **payoff-dominant equilibrium selection principle** states: in a coordination game $G$ with a unique Pareto-dominant Nash equilibrium $(a^*, a^*)$, if it is common knowledge that (i) both agents are rational, (ii) both agents have identical information (the same partition cell), and (iii) the payoff structure is as specified, then both agents select $a^*$. This is an equilibrium selection criterion -- not a theorem of standard rationalizability, but an axiom reflecting the principle that rational agents with identical information and common knowledge thereof have no basis for coordinating on a Pareto-inferior equilibrium.

---

## 1. Introduction

The concept of common knowledge -- every agent knows, every agent knows that every agent knows, every agent knows that every agent knows that every agent knows, and so on without end -- is among the most fundamental and most problematic primitives in the theory of multi-agent interaction. Aumann (1976) proved that if two agents share a common prior and their posteriors for any event are common knowledge, those posteriors must agree. This celebrated impossibility-of-agreeing-to-disagree result established common knowledge as the epistemic bedrock of rational coordination. Yet the very definition of common knowledge demands an infinite regress of nested beliefs, and this infinity is the source of persistent difficulties: how can finite agents, operating in finite time, ever *verify* that common knowledge obtains?

The problem is not merely philosophical. In game theory, equilibrium selection depends critically on the epistemic state of the players. Consider the Stag Hunt (Luce and Raiffa 1957; Skyrms 2004), the canonical coordination game. Two hunters independently choose to pursue a stag (which requires cooperation) or a hare (which does not). If both hunt stag, both receive the highest payoff; if one defects to hare while the other hunts stag, the defector receives a moderate payoff and the cooperator receives nothing. The game has two Nash equilibria: the payoff-dominant $(Stag, Stag)$ and the risk-dominant $(Hare, Hare)$. Which equilibrium rational agents select depends entirely on what they know about each other's knowledge of rationality and payoffs. Mutual knowledge at any finite depth is insufficient: a rational agent who knows the other is rational, and knows the other knows she is rational, but is uncertain whether this nesting continues, may still rationally defect to $Hare$ as a hedge against coordination failure. Only common knowledge of the event "both agents are rational and both face the Stag Hunt payoffs," combined with a payoff-dominant equilibrium selection principle, guarantees that $Stag$ is selected.

The literature has circled this problem from several directions, without resolving it.

Aumann (1976) proposed the partitional information model to formalize common knowledge as a static property of information structures, establishing that common knowledge of an event $E$ holds at state $\omega$ if and only if the meet of agents' information partitions at $\omega$ is contained in $E$. But the partition model is descriptive, not constructive: it characterizes *what* common knowledge is, but provides no mechanism by which agents with initially distinct information can *achieve* it. The model assumes a fixed partition structure exogenously given; it does not address how partitions can be designed or constrained to guarantee common knowledge of a target event.

Halpern and Moses (1990) proposed a temporal-epistemic logic to analyze common knowledge in distributed systems, establishing the fundamental result that common knowledge *cannot be attained* in any system where communication is not guaranteed -- specifically, in any system where messages may be lost. But their impossibility result depends on unreliable channels: the infinite regress persists precisely because each message introduces a new layer of uncertainty about receipt. This leaves open the question of what happens in architectures where the communication channel is not a sequence of messages at all, but a shared, simultaneously accessible, immutable structure.

Rubinstein (1989) proposed the Electronic Mail Game to demonstrate the fragility of almost-common-knowledge, showing that arbitrarily many rounds of message confirmation still fail to produce common knowledge when each message has an independent (however small) probability of loss. But Rubinstein's result is a consequence of the sequential, lossy channel: each confirmation introduces a new state in which one agent's partition cell differs from the other's, preventing partition collapse. The result does not apply to architectures in which both agents observe the same object simultaneously, because in such architectures no confirmation messages are needed and no loss events exist.

Monderer and Samet (1989) proposed common $p$-belief as a relaxation of common knowledge, showing that for $p$ sufficiently close to 1, common $p$-belief of rationality suffices for approximate equilibrium play. But common $p$-belief is an approximation, not a replacement: it yields $\epsilon$-equilibria, not exact Nash equilibria, and the bound on $\epsilon$ degrades as the game's payoff structure becomes more sensitive to higher-order beliefs. For the Stag Hunt specifically, no amount of common $p$-belief (for $p < 1$) eliminates the risk-dominant equilibrium from the set of rationalizable strategies; only full common knowledge ($p = 1$) does.

The gap in the literature is therefore architectural. The impossibility results of Halpern-Moses and Rubinstein are channel-dependent: they prove that sequential message-passing cannot produce common knowledge, but they do not prove that *no* information architecture can produce it. The approximation results of Monderer-Samet show that relaxing the common knowledge requirement weakens the conclusion. And Aumann's original framework, while providing the right formalism, provides no constructive mechanism. What is missing is a *specific, implementable information architecture* that collapses agents' information partitions by construction, yielding common knowledge of a target event in a finite and verifiable number of steps.

This paper fills that gap. We introduce an information architecture consisting of two formal objects -- a **Sacred File** and a **State Vector** -- and prove that this architecture produces common knowledge of the coordination event $E^*$ (both agents are rational and both face the Stag Hunt payoffs) at the first time step at which both agents access the Sacred File. The Sacred File is not a metaphor; it is a formally defined element of the partition model (Definition 7) whose Partition Collapse property forces both agents' information partitions to coincide. The State Vector (Definition 8) provides the verifiable audit trail that records agents' access, ensuring that the epistemic claims are grounded in observable events rather than introspective self-reports.

The paper makes three contributions:

1. **A formal information architecture for common knowledge.** We define the Sacred File and State Vector within Aumann's (1976) partition model and prove that the Partition Collapse property (Definition 7, condition iii) forces the meet of agents' information partitions to equal the partition induced by $S$. Any event that is a union of cells of $S$ is therefore common knowledge by the Aumann characterization. This transforms common knowledge from an infinitely nested epistemic condition into a *design property* of the information structure.

2. **A one-step common knowledge theorem for coordination games.** We will show that when both agents access the Sacred File encoding the Stag Hunt payoffs and the rationality event $R$, the coordination event $E^*$ becomes common knowledge at step 1 -- not asymptotically, not approximately, but exactly and immediately. The infinite regress that plagues message-passing architectures does not arise because there are no messages to confirm: both agents observe the same partition-collapsing object simultaneously.

3. **A deterministic equilibrium selection result for the Stag Hunt.** We will show that common knowledge of $E^*$, combined with a payoff-dominant equilibrium selection principle (Definition 14), yields $(Stag, Stag)$ as the selected equilibrium, eliminating the risk-dominant $(Hare, Hare)$ equilibrium without repeated play, pre-play communication, costly signaling, or evolutionary dynamics. The mechanism is purely epistemic: the architecture changes what agents know, and what agents know determines what they do.

The remainder of the paper is structured as follows. Section 2 presents the main theorem and its proof. Section 3 discusses the application to the Stag Hunt and boundary conditions. Section 4 places this work in the context of the broader literature. Section 5 discusses implications and future directions. Section 6 concludes.

---

## 2. Main Results

This section contains three results. Lemma 1 establishes that the Partition Collapse property forces the meet of the agents' information partitions to equal the Sacred File induced partition $\mathcal{P}_S$ (Def 12). Theorem 1 uses this to prove that any $S$-encoded event (Def 13) is common knowledge, and that the coordination event $E^*$ is common knowledge at step 1. Theorem 2 proves that under common knowledge of $E^*$ and the payoff-dominant equilibrium selection principle (Def 14), both agents select $Stag$, yielding the action profile $(Stag, Stag)$.

---

**Lemma 1 (Partition Collapse implies Meet Equals Sacred File Partition).**

*Hypotheses.*

(H1) $\Omega$ is a finite non-empty state space (Def 1).

(H2) $N = \{1, 2\}$ (Def 2).

(H3) $\mathcal{P}_1$ and $\mathcal{P}_2$ are information partitions of $\Omega$ (Def 3).

(H4) $S : \Omega \to \mathcal{F}$ is a Sacred File satisfying properties (i)--(iii) of Def 7. In particular, Partition Collapse (Def 7.iii) holds: for all $\omega \in \Omega$, $\mathcal{P}_1(\omega) = \mathcal{P}_2(\omega) = S(\omega)$.

(H5) $\mathcal{P}^* = \mathcal{P}_1 \wedge \mathcal{P}_2$ is the meet of the information partitions (Def 6).

*Claim.* $\mathcal{P}^* = \mathcal{P}_S$, where $\mathcal{P}_S$ is the Sacred File induced partition (Def 12).

*Proof.*

(1) By Def 7.iii (Partition Collapse), for all $\omega \in \Omega$: $\mathcal{P}_1(\omega) = S(\omega)$ and $\mathcal{P}_2(\omega) = S(\omega)$. Therefore $\mathcal{P}_1 = \mathcal{P}_2 = \mathcal{P}_S$ as partitions of $\Omega$.

(2) The meet $\mathcal{P}^* = \mathcal{P}_1 \wedge \mathcal{P}_2$ is, by definition, the finest partition of $\Omega$ that is coarser than both $\mathcal{P}_1$ and $\mathcal{P}_2$. A partition $\mathcal{Q}$ is coarser than $\mathcal{P}_i$ if and only if every cell of $\mathcal{P}_i$ is a subset of some cell of $\mathcal{Q}$; equivalently, for all $\omega \in \Omega$, $\mathcal{P}_i(\omega) \subseteq \mathcal{Q}(\omega)$.

(3) Since $\mathcal{P}_1 = \mathcal{P}_2 = \mathcal{P}_S$ (from step 1), any partition $\mathcal{Q}$ that is coarser than both $\mathcal{P}_1$ and $\mathcal{P}_2$ is equivalently any partition that is coarser than $\mathcal{P}_S$.

(4) The finest partition that is coarser than $\mathcal{P}_S$ is $\mathcal{P}_S$ itself, because every partition is coarser than or equal to itself: for all $\omega$, $\mathcal{P}_S(\omega) \subseteq \mathcal{P}_S(\omega)$.

(5) Therefore $\mathcal{P}^* = \mathcal{P}_S$. $\blacksquare$

---

**Theorem 1 (One-Step Common Knowledge).**

*Hypotheses.*

(H1) $\Omega$ is a finite non-empty state space (Def 1).

(H2) $N = \{1, 2\}$ (Def 2).

(H3) $\mathcal{P}_1$ and $\mathcal{P}_2$ are information partitions of $\Omega$ (Def 3).

(H4) $S : \Omega \to \mathcal{F}$ is a Sacred File satisfying Publicity, Immutability, and Partition Collapse (Def 7).

(H5) $V : \Omega \times T \to \mathcal{R}$ is a State Vector satisfying Completeness, Append-Only Integrity, and Mutual Accessibility (Def 8).

(H6) $G = (N, A, u)$ is the Stag Hunt (Def 9) with $A = \{Stag, Hare\}$ and payoffs $(2,2), (0,1), (1,0), (1,1)$.

(H7) $R \subseteq \Omega$ is the rationality event (Def 10).

(H8) $E^* = R \cap \{\omega \in \Omega : u \text{ is as specified in Def 9}\}$ is the coordination event (Def 11).

(H9') Both $R$ and $\{\omega \in \Omega : u \text{ is as specified in Def 9}\}$ are $S$-encoded (Def 13). That is, each is a union of cells of $\mathcal{P}_S$ (Def 12). This is a consequence of the Sacred File Encoding requirement (Def 13): the Sacred File must encode enough information to distinguish rational from irrational states and to distinguish the game being played.

(H10) At time $t = 1$, both agents access $S$. Formally, $V(\omega, 1)$ records that both agents have observed $S(\omega)$ at $t = 1$.

(H10') At $t = 1$, the information available to each agent $i$ is exactly $\mathcal{P}_i(\omega) = S(\omega)$; no additional private information refines this partition beyond $\mathcal{P}_S$. That is, agents possess no side-channel information that would split any cell of $\mathcal{P}_S$ into finer sub-cells.

*Claim (Part A).* For any event $E \subseteq \Omega$ that is a union of cells of $\mathcal{P}_S$, $E$ is common knowledge at every $\omega \in E$. That is, $E \subseteq C(E)$.

*Claim (Part B).* $E^*$ is common knowledge at every $\omega \in E^*$ at step $t = 1$. That is, $E^* \subseteq C(E^*)$ at $t = 1$.

*Proof of Part A.*

(1) Suppose $E \subseteq \Omega$ is a union of cells of $\mathcal{P}_S$. That is, there exists an index set $J$ and cells $\{C_j\}_{j \in J}$ of $\mathcal{P}_S$ such that $E = \bigcup_{j \in J} C_j$. (Here $J$ and $\{C_j\}_{j \in J}$ are locally bound proof variables: $J$ indexes the cells of $\mathcal{P}_S$ that compose $E$, and each $C_j$ is the corresponding cell.)

(2) By Lemma 1, $\mathcal{P}^* = \mathcal{P}_S$. Therefore $E$ is a union of cells of $\mathcal{P}^*$.

(3) Let $\omega \in E$. Since $E$ is a union of cells of $\mathcal{P}^*$ and $\omega \in E$, the cell $\mathcal{P}^*(\omega)$ is one of the cells whose union is $E$. Therefore $\mathcal{P}^*(\omega) \subseteq E$.

(4) By the Aumann partition-meet characterization (Def 6): $E$ is common knowledge at $\omega$ if and only if $\mathcal{P}^*(\omega) \subseteq E$.

(5) From steps (3) and (4): $\omega \in C(E)$.

(6) Since $\omega$ was an arbitrary element of $E$, we have $E \subseteq C(E)$.

We now verify that this is consistent with the infinite-regress characterization. By Def 6, $C(E) = \bigcap_{k=1}^{\infty} M^k(E)$, so we must have $E \subseteq M^k(E)$ for all $k \geq 1$. We confirm this independently:

(7) Let $\omega \in E$ and $i \in N$. By Lemma 1, $\mathcal{P}^* = \mathcal{P}_S$. By Def 7.iii, $\mathcal{P}_i(\omega) = S(\omega) = \mathcal{P}^*(\omega)$. From step (3), $\mathcal{P}^*(\omega) \subseteq E$. Therefore $\mathcal{P}_i(\omega) \subseteq E$, which by Def 4 means $\omega \in K_i(E)$.

(8) Since step (7) holds for both $i = 1$ and $i = 2$, and for all $\omega \in E$: $E \subseteq K_1(E) \cap K_2(E) = M^1(E)$ (by Def 5).

(9) We prove by induction that $E \subseteq M^k(E)$ for all $k \geq 1$.

- *Base case ($k = 1$):* Established in step (8).
- *Inductive step:* Assume $E \subseteq M^{k-1}(E)$ for some $k \geq 2$. We must show $E \subseteq M^k(E) = M^1(M^{k-1}(E))$.

(10) Since $E \subseteq M^{k-1}(E)$ (inductive hypothesis) and $E$ is a union of cells of $\mathcal{P}_S$, we first show that $M^{k-1}(E)$ is also a union of cells of $\mathcal{P}_S$.

(11) For any event $F \subseteq \Omega$ and agent $i$, $K_i(F) = \{\omega : \mathcal{P}_i(\omega) \subseteq F\}$. By Def 7.iii, $\mathcal{P}_i(\omega) = S(\omega)$. So $K_i(F) = \{\omega : S(\omega) \subseteq F\}$. This is a union of cells of $\mathcal{P}_S$: either the entire cell $S(\omega)$ is in $F$ (and then every $\omega'$ with $S(\omega') = S(\omega)$ is in $K_i(F)$), or it is not (and then no such $\omega'$ is in $K_i(F)$).

(12) Therefore $M^1(F) = K_1(F) \cap K_2(F)$ is an intersection of two unions of cells of $\mathcal{P}_S$, which is itself a union of cells of $\mathcal{P}_S$ (since the intersection of unions of partition cells is a union of partition cells).

(13) By induction on the recursive definition $M^k(E) = M^1(M^{k-1}(E))$, applying step (12) at each stage: $M^{k-1}(E)$ is a union of cells of $\mathcal{P}_S$ for all $k \geq 1$.

(14) Now, let $\omega \in E$ and $i \in N$. We have $\mathcal{P}_i(\omega) = S(\omega) = \mathcal{P}^*(\omega) \subseteq E$ (from step 3). Since $E \subseteq M^{k-1}(E)$ (inductive hypothesis), $\mathcal{P}_i(\omega) \subseteq E \subseteq M^{k-1}(E)$. By Def 4, $\omega \in K_i(M^{k-1}(E))$.

(15) Since step (14) holds for both $i = 1$ and $i = 2$: $\omega \in K_1(M^{k-1}(E)) \cap K_2(M^{k-1}(E)) = M^1(M^{k-1}(E)) = M^k(E)$.

(16) Since $\omega$ was arbitrary in $E$: $E \subseteq M^k(E)$.

(17) By induction, $E \subseteq M^k(E)$ for all $k \geq 1$. Therefore $E \subseteq \bigcap_{k=1}^{\infty} M^k(E) = C(E)$.

Therefore, for any event $E$ that is a union of cells of $\mathcal{P}_S$, $E \subseteq C(E)$. $\blacksquare$

*Proof of Part B.*

We must show that $E^*$ satisfies the hypotheses of Part A and that common knowledge obtains at $t = 1$.

(1) By (H9'), $R$ is $S$-encoded (Def 13), i.e., $R$ is a union of cells of $\mathcal{P}_S$. That is, the Sacred File determines whether the agents are rational: for any cell $C$ of $\mathcal{P}_S$, either $C \subseteq R$ or $C \cap R = \emptyset$.

(2) By (H9'), $\{\omega \in \Omega : u \text{ is as specified in Def 9}\}$ is $S$-encoded (Def 13), i.e., it is a union of cells of $\mathcal{P}_S$. That is, the Sacred File determines the payoff structure: for any cell $C$ of $\mathcal{P}_S$, either $C$ is entirely contained in the set of states where the payoff matrix is the Stag Hunt, or $C$ is disjoint from it.

(3) $E^* = R \cap \{\omega : u \text{ is as in Def 9}\}$ (by Def 11). The intersection of two $S$-encoded events is $S$-encoded. *Justification:* Let $E = \bigcup_{j \in J} C_j$ and $F = \bigcup_{l \in L} C_l$ where each $C_j, C_l$ is a cell of $\mathcal{P}_S$. (Here $J$, $L$, $C_j$, and $C_l$ are locally bound proof variables.) Since $\mathcal{P}_S$ is a partition, its cells are pairwise disjoint. Therefore $E \cap F = \bigcup_{m \in J \cap L} C_m$, which is a union of cells of $\mathcal{P}_S$.

(4) Since $E^*$ is $S$-encoded (a union of cells of $\mathcal{P}_S$), Part A applies: $E^* \subseteq C(E^*)$.

(5) It remains to show that common knowledge obtains at step $t = 1$ specifically. The Partition Collapse property (Def 7.iii) holds as a structural property of $S$: the equation $\mathcal{P}_i(\omega) = S(\omega)$ holds for all $\omega$ and all $i$, from the moment both agents have access to $S$.

(6) By (H10), at time $t = 1$, both agents access $S$, and $V(\omega, 1)$ records this access. By (H10'), at $t = 1$, the information available to each agent $i$ is exactly $\mathcal{P}_i(\omega) = S(\omega)$, with no additional private information refining the partition beyond $\mathcal{P}_S$. No prior time step is needed: the Partition Collapse is a property of the architecture, not a result of iterated communication.

(7) By Mutual Accessibility of $V$ (Def 8.iii), both agents observe $V(\omega, 1)$ at $t = 1$, which records that both agents have accessed $S$. This observation is itself $S$-encoded (since $V(\omega, 1)$ is $\mathcal{P}_i$-measurable by Def 8.iii and $\mathcal{P}_i = \mathcal{P}_S$ by Def 7.iii and Def 12).

(8) Combining steps (4) and (6): at $t = 1$, for all $\omega \in E^*$, $\omega \in C(E^*)$. Common knowledge of $E^*$ obtains at the first step.

(9) The step count is 1 because no iterative confirmation is required. In message-passing architectures (Halpern and Moses 1990; Rubinstein 1989), each round of communication establishes one additional level of mutual knowledge ($M^k \to M^{k+1}$), and common knowledge requires $k \to \infty$, which is never reached in finite time. In the Sacred File architecture, the Partition Collapse property yields $\mathcal{P}_1 = \mathcal{P}_2 = \mathcal{P}_S$ directly (step 1 of Lemma 1), which by steps (7)--(17) of Part A simultaneously satisfies $E^* \subseteq M^k(E^*)$ for *all* $k$ at once. The infinite regress is not traversed iteratively; it is bypassed by architectural fiat. One access to $S$ produces all levels of mutual knowledge simultaneously.

Therefore $E^*$ is common knowledge at every $\omega \in E^*$ at step $t = 1$. $\blacksquare$

---

**Theorem 2 (Equilibrium Selection under Common Knowledge).**

*Hypotheses.*

(H1)--(H10), (H9'), (H10') as in Theorem 1.

(H11) $\omega \in E^*$, so that $E^*$ is common knowledge at $\omega$ (by Theorem 1).

(H12) The payoff-dominant equilibrium selection principle (Def 14) is in force.

*Claim.* Under $C(E^*)$ and the payoff-dominant equilibrium selection principle (Def 14), both agents select $Stag$, yielding the action profile $(Stag, Stag)$.

*Proof.*

(1) By (H11) and Theorem 1, at state $\omega$: $C(E^*)$ obtains. Unpacking Def 11 and Def 6, this means it is common knowledge that both agents are rational (Def 10) and that the payoff matrix is the Stag Hunt (Def 9).

(2) Since $E^*$ is common knowledge, each agent knows the payoff matrix is the Stag Hunt (Def 9):

|  | Stag | Hare |
|---|---|---|
| **Stag** | (2, 2) | (0, 1) |
| **Hare** | (1, 0) | (1, 1) |

and this knowledge is itself common knowledge.

(3) We first verify the strategic structure of the game. A strategy $a_i$ is strictly dominated for agent $i$ if there exists $a_i'$ such that $u_i(a_i', a_{-i}) > u_i(a_i, a_{-i})$ for all $a_{-i} \in A$.

(4) **Strict dominance check.** Check whether either strategy is strictly dominated without any assumption about the opponent's play:
- For agent $i$: $u_i(Stag, Stag) = 2 > u_i(Hare, Stag) = 1$, but $u_i(Stag, Hare) = 0 < u_i(Hare, Hare) = 1$. So $Stag$ is not strictly dominated by $Hare$.
- For agent $i$: $u_i(Hare, Stag) = 1 < u_i(Stag, Stag) = 2$, but $u_i(Hare, Hare) = 1 > u_i(Stag, Hare) = 0$. So $Hare$ is not strictly dominated by $Stag$.
- Neither strategy is strictly dominated. Standard iterated elimination of strictly dominated strategies does not eliminate any strategy.

(5) **Best responses.** From the payoff matrix:
- If agent $-i$ plays $Stag$: $u_i(Stag, Stag) = 2 > u_i(Hare, Stag) = 1$. Best response is $Stag$.
- If agent $-i$ plays $Hare$: $u_i(Hare, Hare) = 1 > u_i(Stag, Hare) = 0$. Best response is $Hare$.

Each agent's best response matches the opponent's action: the best response to $Stag$ is $Stag$, and the best response to $Hare$ is $Hare$. Both $(Stag, Stag)$ and $(Hare, Hare)$ are Nash equilibria, since each is a mutual best response.

(6) **Payoff dominance.** The payoff at $(Stag, Stag)$ is $(2, 2)$ and at $(Hare, Hare)$ is $(1, 1)$. The equilibrium $(Stag, Stag)$ **Pareto-dominates** $(Hare, Hare)$: $u_i(Stag, Stag) = 2 > 1 = u_i(Hare, Hare)$ for both $i \in N$. Moreover, $(Stag, Stag)$ is the *unique* Pareto-dominant Nash equilibrium: no other Nash equilibrium yields payoffs at least as high for both agents.

(7) **Application of the Payoff-Dominant Equilibrium Selection Principle (Def 14).** We verify that the three conditions of Def 14 are satisfied:

(8) *Condition (i): Common knowledge of rationality.* By step (1), $C(E^*)$ obtains at $\omega$, i.e., $\mathcal{P}^*(\omega) \subseteq E^*$. Since $E^* \subseteq R$ (by Def 11), we have $\mathcal{P}^*(\omega) \subseteq E^* \subseteq R$. By the Aumann characterization (Def 6), $\omega \in C(R)$. (This is an instance of the monotonicity of the common knowledge operator: for any events $E \subseteq F$, $C(E) \subseteq C(F)$, which follows directly from the partition-meet characterization since $\mathcal{P}^*(\omega) \subseteq E \subseteq F$ implies $\mathcal{P}^*(\omega) \subseteq F$.) Therefore it is common knowledge that both agents are rational.

(9) *Condition (ii): Common knowledge of identical information.* By Partition Collapse (Def 7.iii) and Def 12, $\mathcal{P}_1(\omega) = \mathcal{P}_2(\omega) = S(\omega) = \mathcal{P}_S(\omega)$ for all $\omega \in \Omega$. Both agents have the same partition cell at every state. The event $I = \{\omega \in \Omega : \mathcal{P}_1(\omega) = \mathcal{P}_2(\omega)\}$ equals $\Omega$ itself, so $I$ is trivially a union of cells of $\mathcal{P}_S$ (it is $\Omega$, the union of all cells). By Part A of Theorem 1, $I \subseteq C(I)$, i.e., $C(I) = \Omega$. It is common knowledge at every state that both agents have identical information.

(10) *Condition (iii): Common knowledge of the payoff structure.* By step (1), $C(E^*)$ obtains. Since $E^* \subseteq \{\omega : u \text{ is as in Def 9}\}$ (by Def 11), and $\mathcal{P}^*(\omega) \subseteq E^* \subseteq \{\omega : u \text{ is as in Def 9}\}$, we have $\omega \in C(\{\omega : u \text{ is as in Def 9}\})$ by Def 6. It is common knowledge that the payoff structure is the Stag Hunt.

(11) **Conclusion by Def 14.** All three conditions of the payoff-dominant equilibrium selection principle (Def 14) are satisfied: (i) common knowledge of rationality (step 8), (ii) common knowledge of identical information (step 9), and (iii) common knowledge of the payoff structure (step 10). The Stag Hunt has a unique Pareto-dominant Nash equilibrium, $(Stag, Stag)$ (step 6). By Def 14, both agents select $Stag$.

(12) The resulting action profile is $(Stag, Stag)$, with payoff $(2, 2)$.

(13) **Acknowledgment on the role of Def 14.** We emphasize that this result depends on the payoff-dominant equilibrium selection principle (Def 14), which is an axiom of the model, not a theorem of standard rationalizability. Under standard rationalizability alone, both $(Stag, Stag)$ and $(Hare, Hare)$ survive as Nash equilibria. Neither strategy is eliminated by iterated elimination of never-best-responses, because $Stag$ is a best response to $Stag$ and $Hare$ is a best response to $Hare$ (step 5). The contribution of the Sacred File architecture is that it creates the epistemic conditions -- specifically, common knowledge of identical information -- under which the payoff-dominant selection principle applies. Without the Sacred File, agents may lack common knowledge that they share the same information, and the conditions of Def 14 are not met; with it, all three conditions are satisfied, and the axiom yields selection of the Pareto-dominant equilibrium.

Therefore, under $C(E^*)$ and the payoff-dominant equilibrium selection principle (Def 14), both agents select $Stag$, yielding the action profile $(Stag, Stag)$. $\blacksquare$

---

**Remark 1 (Why step 1 and not step 0).** At $t = 0$, the State Vector $V(\omega, 0)$ records initial conditions but does not yet record that both agents have accessed $S$. The Partition Collapse property (Def 7.iii) is a structural property of $S$, but its epistemic consequences require that both agents have *observed* $S$. At $t = 1$, $V(\omega, 1)$ records both agents' access (H10 of Theorem 1), and Mutual Accessibility of $V$ (Def 8.iii) ensures both agents observe this record. The common knowledge claim is therefore grounded at $t = 1$: the first moment at which observation is verified.

**Remark 2 (Contrast with message-passing architectures).** In Rubinstein's (1989) Electronic Mail Game, each confirmation message establishes one additional level of mutual knowledge. After $k$ messages, $M^k(E)$ holds but $M^{k+1}(E)$ does not, because the last sender is uncertain whether the last message arrived. The partition cells of the two agents differ at every finite stage, so $\mathcal{P}_1(\omega) \neq \mathcal{P}_2(\omega)$ at every relevant state, and $\mathcal{P}^*(\omega)$ extends beyond $E$. The Sacred File bypasses this entirely: Partition Collapse forces $\mathcal{P}_1(\omega) = \mathcal{P}_2(\omega)$ without any messages, so no confirmation layer is needed and the infinite regress is resolved at step 1.

**Remark 3 (The Sacred File as a sufficient condition).** Theorem 1 establishes a sufficient condition for common knowledge, not a necessary one. Other architectures may also produce common knowledge (e.g., Aumann's original model assumes common knowledge of the prior as given). The contribution of the Sacred File architecture is that it provides a *constructive, implementable* mechanism: one can design $S$ to encode specific target events and verify via $V$ that both agents have accessed it.

---

## 3. Application and Boundary Conditions

### 3.1 The Sacred File as a Common Knowledge Machine

By Theorem 1 (Part A), any $S$-encoded event $E$ satisfies $E \subseteq C(E)$: common knowledge is not negotiated, inferred, or iteratively confirmed, but manufactured by the architecture itself. The mechanism is the Partition Collapse property (Def 7.iii), which by Lemma 1 forces $\mathcal{P}^* = \mathcal{P}_S$. Every event expressible as a union of cells of the Sacred File partition is automatically common knowledge at every state in which it holds.

This yields a design methodology: to make a target event $E$ common knowledge, encode it into $S$ such that $E$ is $S$-encoded (Def 13). By Theorem 1 (Part A), the infinite regress resolves at the moment of encoding, not at the moment of observation. The State Vector $V$ (Def 8) then provides the audit trail confirming that both agents have accessed $S$, grounding the epistemic claim in observable fact.

### 3.2 One-Step Coordination in the Stag Hunt

The canonical application is the Stag Hunt (Def 9). The equilibrium selection problem in the Stag Hunt is well understood: rational agents face two Nash equilibria, $(Stag, Stag)$ at payoff $(2,2)$ and $(Hare, Hare)$ at payoff $(1,1)$. Without common knowledge of the coordination event $E^*$, a rational agent cannot rule out the possibility that the other agent lacks sufficient confidence in mutual rationality, and may therefore hedge toward $Hare$. The risk-dominant equilibrium persists not because agents are irrational, but because the epistemic conditions for payoff-dominant selection are unsatisfied.

By Theorem 1 (Part B), when both agents access a Sacred File encoding rationality and the Stag Hunt payoff structure, the coordination event $E^*$ is common knowledge at step $t = 1$. By Theorem 2, under the payoff-dominant equilibrium selection principle (Def 14), both agents select $Stag$, yielding $(Stag, Stag)$ with payoff $(2, 2)$. The risk-dominant equilibrium is not selected -- not because it ceases to be a Nash equilibrium (it remains one), but because the epistemic conditions produced by the Sacred File architecture, combined with Def 14, lead both agents to the payoff-dominant equilibrium instead. No evolutionary dynamics, repeated play, cheap talk, or costly signaling is required: a single architectural intervention resolves the epistemic deficit.

The step count is exactly 1. Not "finitely many." Not "asymptotically." One access to $S$, recorded in $V$, and the coordination problem is solved.

### 3.3 Generalization Beyond the Stag Hunt

Theorem 1 is not specific to the Stag Hunt. Part A establishes that *any* $S$-encoded event is common knowledge. The Stag Hunt application (Theorem 2) uses the payoff-dominant equilibrium selection principle (Def 14) to convert common knowledge into a specific action profile, but the common knowledge result itself is game-independent.

We conjecture that for any finite coordination game $G = (N, A, u)$ with a unique Pareto-dominant Nash equilibrium $(a^*, a^*)$, if the payoff structure event and the rationality event $R$ are $S$-encoded, then by Theorem 1 (Part A) the coordination event is common knowledge at step 1, and the payoff-dominant equilibrium is selected under an appropriately generalized version of Def 14. The common knowledge result (Theorem 1 Part A) holds immediately for any such game, since it is game-independent. The equilibrium selection step requires verifying that the generalized Def 14 conditions are met for the specific game in question. This paper proves the result for the Stag Hunt (Theorem 2); the general case is stated as a conjecture, not a theorem.

The scope of the result is bounded by the scope of Def 14: the equilibrium selection principle applies to games with a unique Pareto-dominant Nash equilibrium. Games with multiple Pareto-incomparable equilibria, games with no pure-strategy Nash equilibrium, or games in which the Pareto-dominant outcome is not a Nash equilibrium fall outside the mechanism. These boundaries are made precise in Section 3.5.

### 3.4 The Architecture as an Impossibility Bypass

The impossibility results of Halpern and Moses (1990) and the fragility results of Rubinstein (1989) have been widely interpreted as establishing that common knowledge is unattainable in practice. The Sacred File architecture demonstrates that this interpretation conflates a channel-specific impossibility with a general one.

By Theorem 1 (Part B), common knowledge of $E^*$ obtains at step 1 in the Sacred File architecture. This does not contradict Halpern-Moses or Rubinstein, because the Sacred File is not a message-passing channel. The impossibility results apply to systems in which agents must confirm receipt of messages, each confirmation introducing a new layer of epistemic uncertainty. The Sacred File eliminates the confirmation layer entirely: Partition Collapse (Def 7.iii) ensures $\mathcal{P}_1 = \mathcal{P}_2 = \mathcal{P}_S$ by construction, not by communication. No message is sent, so no message can be lost, and the infinite regress that Halpern-Moses proved to be unresolvable in message-passing systems does not arise.

The precise relationship: Halpern-Moses proved that in systems satisfying their communication axioms (which include the possibility of message loss), common knowledge is unattainable. The Sacred File architecture does not satisfy those axioms -- it is not a communication system in their sense -- and therefore their impossibility result does not apply. The Sacred File is a shared, simultaneously accessible, immutable object. By Definition 7, the Sacred File satisfies none of the Halpern-Moses communication axioms: it is not a channel, no messages are sent, and no runs exist in which one agent's observation differs from another's (since Partition Collapse, Def 7.iii, eliminates all such states). The architecture is closer in spirit to Aumann's (1976) common prior than to a communication channel, but unlike a common prior, it is constructive and verifiable via $V$.

### 3.5 Boundary Conditions

This section subjects the results of Sections 2--3 to adversarial stress-testing. The goal is not to qualify or hedge, but to identify the exact boundaries at which the results hold, degrade, or fail.

#### 3.5.1 Natural Enemy: Halpern and Moses (1990)

**The result.** Halpern and Moses (1990) proved that in any system where communication is not guaranteed -- formally, in any interpreted system where at every point there exists a run in which a sent message is not received -- common knowledge of any non-trivial event cannot be attained in finite time. Their proof shows that each round of message exchange increases the depth of mutual knowledge by exactly one level ($M^k \to M^{k+1}$), and since common knowledge requires $M^k$ for all $k$, no finite number of rounds suffices.

**Why it seems to contradict this paper.** Theorem 1 (Part B) claims that common knowledge of $E^*$ obtains at step $t = 1$. If Halpern-Moses proved that common knowledge is unattainable in finite time, and this paper claims attainment at $t = 1$, the results appear contradictory.

**Why it does not.** The Halpern-Moses impossibility is conditional on the system being a *message-passing system with unreliable channels*. Their formal framework is the "interpreted systems" model, in which agents communicate by sending messages along channels, and the possibility space includes runs in which any given message fails to arrive. The key structural feature is that each agent's local state depends on the *sequence of messages received*, and since each message may or may not arrive, the agents' local states (and hence their information partitions) can diverge.

The Sacred File architecture is not a message-passing system. No agent sends a message to any other agent. Both agents observe the same object $S$ simultaneously, and their information partitions are constrained to coincide by Partition Collapse (Def 7.iii). The divergence mechanism that drives the Halpern-Moses impossibility -- the possibility that agent 1 received a message that agent 2 did not -- has no analogue in the Sacred File architecture, because there are no messages.

Formally: the Halpern-Moses impossibility applies to systems in which there exist two runs $r, r'$ that are indistinguishable to agent $i$ at some time $t$ but distinguishable to agent $j$, because a message arrived in $r$ but not in $r'$. In the Sacred File architecture, Partition Collapse ensures that for all $\omega$, $\mathcal{P}_1(\omega) = \mathcal{P}_2(\omega)$. No such pair of distinguishable-to-one-but-not-the-other states exists. The architecture eliminates the precondition of the impossibility result.

**The boundary.** If the Sacred File's Publicity or Partition Collapse properties are weakened -- for instance, if agent 1 observes a slightly different version of $S$ than agent 2, or if access to $S$ is mediated by a lossy channel -- the architecture degenerates into a message-passing system, and the Halpern-Moses impossibility reasserts itself. The result of this paper holds *exactly* at the boundary where Partition Collapse is satisfied and fails *immediately* when it is violated. There is no graceful degradation: see Section 3.5.3.

#### 3.5.2 Rubinstein's Electronic Mail Game (1989)

**The challenge.** Rubinstein (1989) showed that in a coordination game where agents exchange confirmation messages with independent loss probability $\epsilon > 0$, the unique rationalizable strategy is the risk-dominant equilibrium -- even after arbitrarily many rounds of confirmation. This is often cited as evidence that "almost common knowledge" is strategically worthless for equilibrium selection.

**Relationship to this paper.** Rubinstein's result depends on the sequential, lossy channel: each message creates a new state in which the sender knows the message was sent but the receiver may not have received it. The agents' partition cells differ at every state, so $\mathcal{P}_1(\omega) \neq \mathcal{P}_2(\omega)$ for all relevant $\omega$, and the meet $\mathcal{P}^*$ is strictly coarser than either individual partition.

The Sacred File architecture prevents this divergence by construction: Partition Collapse forces $\mathcal{P}_1 = \mathcal{P}_2 = \mathcal{P}_S$, and by Lemma 1, $\mathcal{P}^* = \mathcal{P}_S$. No confirmation messages are needed because there are no messages to confirm. Rubinstein's construction of divergent partition cells has no analogue in the Sacred File architecture.

**The boundary.** If access to $S$ requires a confirmation step -- for instance, if agent 1 must verify that agent 2 has accessed $S$, and this verification can fail -- the system reintroduces the Rubinstein structure. The State Vector $V$ is designed to avoid this: by Mutual Accessibility (Def 8.iii), both agents observe $V$ directly, and $V$ records both agents' access. The verification is not a message from agent 2 to agent 1; it is a shared observation of a common object. If Mutual Accessibility of $V$ is violated, the Rubinstein fragility returns.

#### 3.5.3 Assumption Violations

**Partition Collapse (Def 7.iii).** This is the load-bearing assumption. Two cases must be distinguished depending on how it is weakened.

*Case (a): Publicity holds, Collapse fails.* If the condition is weakened to $\mathcal{P}_i(\omega) \subseteq S(\omega)$ for all $i$ (Publicity alone, without Collapse), then both agents' partitions are refinements of $\mathcal{P}_S$, and $\mathcal{P}_1 \neq \mathcal{P}_2$ in general. However, the meet $\mathcal{P}^* = \mathcal{P}_1 \wedge \mathcal{P}_2$ cannot be strictly coarser than $\mathcal{P}_S$, because $\mathcal{P}_S$ is a common coarsening of $\mathcal{P}_1$ and $\mathcal{P}_2$ (both refine it), and the meet is by definition the *finest* common coarsening, so $\mathcal{P}^*$ is finer than or equal to $\mathcal{P}_S$. Consequently, any $S$-encoded event (a union of cells of $\mathcal{P}_S$) is also a union of cells of $\mathcal{P}^*$, and $E \subseteq C(E)$ still holds for $S$-encoded events by the Aumann characterization. **Theorem 1 Part A survives Publicity alone for $S$-encoded events.** What Partition Collapse adds beyond Publicity is the elimination of private information: without Collapse, agents may possess information finer than $\mathcal{P}_S$ (their partitions are strict refinements), creating asymmetric knowledge about non-$S$-encoded events. This asymmetric private information does not threaten common knowledge of $S$-encoded events, but it does mean that the agents are not in identical epistemic states -- they share common knowledge of $E^*$ but may disagree on finer-grained questions not encoded in $S$. The impact on the paper's two main results differs. **Theorem 1 Part A** (any $S$-encoded event is common knowledge) survives Publicity alone, since the meet $\mathcal{P}^*$ refines $\mathcal{P}_S$ and the Aumann characterization still applies. **Theorem 2** (equilibrium selection) does not survive Publicity alone, because Def 14 condition (ii) requires common knowledge that both agents have *identical information* -- specifically, that $\mathcal{P}_1(\omega) = \mathcal{P}_2(\omega)$ for all $\omega$ -- and this fails when agents' partitions are strict refinements of $\mathcal{P}_S$ that differ from each other. Under Publicity without Collapse, agents achieve common knowledge of $E^*$ but lack the epistemic symmetry that Def 14 requires for equilibrium selection.

*Case (b): Publicity itself fails.* If agents observe different content -- for instance, if access to $S$ is mediated by a lossy or corrupted channel, so that agent $i$'s effective partition is not constrained to refine $\mathcal{P}_S$ -- then cells of $\mathcal{P}_1$ may cross the boundaries of cells of $\mathcal{P}_S$, and likewise for $\mathcal{P}_2$. In this case, the meet $\mathcal{P}^*$ can be strictly coarser than $\mathcal{P}_S$, up to and including the trivial partition $\{\Omega\}$. $S$-encoded events may fail to be common knowledge, because $\mathcal{P}^*(\omega)$ may extend beyond $E$ even when $\omega \in E$. Quantitatively: let $|\mathcal{P}_S| = n$. If Publicity is violated, the meet $\mathcal{P}^*$ can have as few as 1 cell (the trivial partition), meaning only $\Omega$ is guaranteed to be common knowledge -- a total collapse of the mechanism. The result degrades from "all $S$-encoded events are common knowledge" to "only $\Omega$ is guaranteed to be common knowledge." This is the catastrophic case: the architecture degenerates into one where agents effectively share no common information structure, and the Halpern-Moses impossibility reasserts itself.

The upshot is that Partition Collapse is not the sole load-bearing condition for $S$-encoded events (Publicity alone suffices for those), but it is load-bearing for the guarantee that agents have *no* epistemic asymmetry -- the condition that makes the Sacred File a complete common knowledge machine rather than a partial one. The catastrophic degradation occurs when Publicity itself fails, not merely when Collapse fails.

**Immutability (Def 7.ii).** If $S$ can be altered after initial observation, agents face a dynamic game in which the content of $S$ at time $t$ may differ from its content at time $t' > t$. The partition $\mathcal{P}_S$ becomes time-dependent: $\mathcal{P}_S^t \neq \mathcal{P}_S^{t'}$. An event $E$ that is $S$-encoded at $t$ may not be $S$-encoded at $t'$. Common knowledge of $E$ established at $t$ via Theorem 1 may be invalidated at $t'$. The State Vector's Append-Only Integrity (Def 8.ii) records the history, but the epistemic claim $E \subseteq C(E)$ is time-indexed and holds only for the partition in force at the time of access. If either agent can modify $S$, the architecture degenerates into a signaling game, and common knowledge of the modification event requires a separate mechanism -- reintroducing the regress.

**Mutual Accessibility of $V$ (Def 8.iii).** If agent $i$ cannot observe $V(\omega, t)$ at time $t$, then the verification that both agents have accessed $S$ breaks down. Specifically, the proof of Theorem 1 Part B, step (7), relies on both agents observing $V(\omega, 1)$ to confirm mutual access. Without Mutual Accessibility, agent 1 may know she has accessed $S$, but not know that agent 2 has accessed $S$. This reduces common knowledge to first-order knowledge ($K_1(E^*)$ but not $M^2(E^*)$), which is insufficient for the application of Theorem 2.

**$S$-encoding of $E^*$ (H9').** If the rationality event $R$ or the payoff structure event is not $S$-encoded -- that is, if some cell of $\mathcal{P}_S$ contains both rational and irrational states, or both Stag Hunt and non-Stag-Hunt payoff states -- then $E^*$ is not a union of cells of $\mathcal{P}_S$, and Theorem 1 Part A does not apply. The Sacred File is too coarse to distinguish the relevant events, and the common knowledge claim fails. This is not a limitation of the theorem but a design constraint on $S$: the Sacred File must be constructed to encode the target events at sufficient granularity.

**Finite state space (Def 1).** The assumption that $\Omega$ is finite is used throughout: partitions of finite sets are well-defined, the meet is unique, and the intersection $\bigcap_{k=1}^{\infty} M^k(E)$ is computed over a nested sequence of subsets of a finite set. If $\Omega$ is infinite (countable or uncountable), the partition model requires measure-theoretic machinery (common knowledge is defined via the meet of sub-$\sigma$-algebras), and the Partition Collapse property must be reformulated as agreement of $\sigma$-algebras. The core argument extends naturally to the countable case. The uncountable case requires care with regularity conditions on $S$ but does not introduce fundamental obstacles, since the Aumann characterization of common knowledge via the meet of partitions generalizes to $\sigma$-algebras (Aumann 1976, Section 3).

**Rationality assumption (Def 10).** The model assumes that rationality is a binary, verifiable property: either $\omega \in R$ or $\omega \notin R$. In practice, rationality is not binary. Bounded rationality, trembling-hand errors, or mistaken beliefs can cause an agent to be "in $R$" according to the Sacred File but to act irrationally in practice. The model's response: what is $S$-encoded is the event *that the Sacred File declares both agents rational*, not the metaphysical fact of rationality. If the Sacred File's declaration is incorrect at some state $\omega$ (the Sacred File says "rational" but the agent is not), then $\omega \notin E^*$ by definition, and the theorem does not apply at $\omega$. The model is honest about what it assumes: it requires that $R$ be correctly encoded, and the burden of verification falls on the design of $S$.

#### 3.5.4 Edge Cases

**Degenerate Sacred File: $|\mathcal{P}_S| = 1$.** If $S$ induces the trivial partition $\{\Omega\}$, then every event is either $\Omega$ or $\emptyset$, both of which are trivially common knowledge. The mechanism works but is vacuous: the Sacred File distinguishes nothing. $E^*$ is common knowledge only if $E^* = \Omega$ (all states are coordination states) or $E^* = \emptyset$ (no states are). This is the edge case in which the Sacred File provides no information beyond "a state space exists."

**Degenerate Sacred File: $|\mathcal{P}_S| = |\Omega|$.** If $S$ induces the finest possible partition (each cell is a singleton $\{\omega\}$), then every event is $S$-encoded, and every event is common knowledge at the unique state in which it holds. The mechanism works maximally: the Sacred File distinguishes everything. This is the case of perfect common information.

**Single agent: $|N| = 1$.** The model assumes $|N| = 2$. With a single agent, the meet $\mathcal{P}^*$ is just $\mathcal{P}_1$, and common knowledge reduces to individual knowledge. The results hold trivially but the coordination problem does not arise.

**More than two agents: $|N| > 2$.** The model is defined for $N = \{1, 2\}$. For $|N| > 2$, Theorem 1 requires $\mathcal{P}_i(\omega) = S(\omega)$ for all $i \in N$ (Partition Collapse generalized to $n$ agents). The meet $\mathcal{P}^* = \bigwedge_{i \in N} \mathcal{P}_i$ equals $\mathcal{P}_S$ if and only if $\mathcal{P}_i = \mathcal{P}_S$ for all $i$. The formal extension of Theorem 1 is straightforward under this condition, but this paper does not prove it. The potential failure point: a single agent $i$ for whom $\mathcal{P}_i \neq \mathcal{P}_S$ can cause the meet to be strictly coarser than $\mathcal{P}_S$, and the common knowledge claim fails for events that are $S$-encoded but not $\mathcal{P}^*$-encoded. Theorem 2 additionally requires that Def 14 be restated for $n$-player coordination games, which may require additional equilibrium selection axioms for asymmetric games.

**Payoffs at the boundary: $(Stag, Stag) = (1,1)$.** If the Stag Hunt payoffs are modified so that $(Stag, Stag) = (Hare, Hare) = (1,1)$, the game has no unique Pareto-dominant equilibrium, and Def 14 does not apply. The common knowledge result (Theorem 1) still holds, but the equilibrium selection result (Theorem 2) fails. The mechanism produces common knowledge but cannot resolve equilibrium selection without payoff dominance.

**Payoffs inverted: risk-dominant = payoff-dominant.** If $(Hare, Hare)$ yields $(2,2)$ and $(Stag, Stag)$ yields $(1,1)$, the payoff-dominant equilibrium is $(Hare, Hare)$, and Def 14 selects it. The mechanism is indifferent to the labels; it selects whichever equilibrium is Pareto-dominant. The result is unchanged in structure.

#### 3.5.5 Sensitivity Summary

| Assumption | Baseline | Weakening | CK of $S$-encoded events | Equilibrium Selection (Thm 2) |
|---|---|---|---|---|
| Partition Collapse (Def 7.iii) | $\mathcal{P}_i = \mathcal{P}_S$ for all $i$ | Publicity holds, $\mathcal{P}_i$ strictly refines $\mathcal{P}_S$ | **Preserved** (meet refines $\mathcal{P}_S$) | **Fails** (Def 14 condition (ii) requires identical partitions) |
| Publicity (Def 7.i) | $\mathcal{P}_i(\omega) \subseteq S(\omega)$ | Agent $i$'s partition crosses $S$-cell boundaries | **Fails** (meet can coarsen to $\{\Omega\}$) | **Fails** |
| Immutability (Def 7.ii) | $S$ fixed for all $t$ | $S$ modified with probability $\delta$ per period | CK holds at $t$, invalid at $t'$ with probability $\delta$ | Degrades (time-indexed CK only) |
| Mutual Accessibility (Def 8.iii) | Both agents observe $V$ | Agent observes $V$ with probability $1-p$ | Degrades to $M^1(E^*)$ (first-order mutual knowledge) | **Fails** (requires $C(E^*)$) |
| $S$-encoding (H9') | $R$, payoff event are unions of cells of $\mathcal{P}_S$ | Some cell of $\mathcal{P}_S$ straddles $R$-boundary | **Fails** (Theorem 1A does not apply) | **Fails** |
| Rationality (Def 10) | $R$ correctly encoded in $S$ | $S$ declares rational but agent acts irrationally | $\omega \notin E^*$; theorem does not apply at $\omega$ | N/A at $\omega$ |

The critical boundary is Publicity (Def 7.i): its violation causes catastrophic failure. Partition Collapse strengthens Publicity by eliminating private information, but for $S$-encoded events, Publicity alone suffices. The precise degradation rate under partial Publicity violation -- relating the fraction of states where Publicity holds to a common $p$-belief bound (Monderer and Samet 1989) -- is an open problem (Section 3.5.7, item 2).

#### 3.5.6 The Contentious Status of Definition 14

The payoff-dominant equilibrium selection principle (Def 14) is an axiom, not a theorem. This is stated explicitly in Def 14 and acknowledged in Theorem 2, step (13). The result of Theorem 2 is conditional on this axiom.

The axiom is contentious. Harsanyi and Selten (1988) proposed payoff dominance as a primary selection criterion, but their own theory ultimately selected risk dominance for the Stag Hunt under certain tracing procedure conditions. Carlsson and van Damme (1993) showed that in global games with strategic uncertainty, the risk-dominant equilibrium is uniquely selected as noise vanishes. The experimental literature is mixed: some experiments find payoff-dominant play (e.g., Rankin, Van Huyck, and Battalio 2000, with sufficient coordination history), while others find risk-dominant play (e.g., Battalio, Samuelson, and Van Huyck 2001, with strategic uncertainty).

The response of this paper is structural, not empirical. The claim is not that Def 14 describes how agents *do* behave, but that it describes how agents *should* behave given the epistemic conditions produced by the Sacred File. Specifically: under Partition Collapse, both agents have identical information (Theorem 2, step 9), both know they have identical information, and this is common knowledge. Under these conditions, the standard arguments for risk dominance -- which depend on strategic uncertainty about the opponent's information or beliefs -- do not apply. There is no uncertainty about the opponent's information: it is the same information, and this fact is common knowledge. The agent who selects $Hare$ in these conditions must believe that the other agent, *with the same information and the same common knowledge*, will also select $Hare$ -- but by symmetric reasoning, if one selects $Hare$, both do, yielding $(1,1)$ when $(2,2)$ was available. Def 14 axiomatizes the principle that symmetric rational agents with common knowledge of identical information and a unique Pareto-dominant equilibrium select it.

If one rejects Def 14, Theorem 1 still holds. Common knowledge of $E^*$ still obtains at step 1. What fails is only the equilibrium selection conclusion of Theorem 2. The contribution of the Sacred File architecture to the common knowledge problem is independent of whether one accepts Def 14.

#### 3.5.7 Open Problems

1. **Multi-agent extension.** This paper proves the result for $|N| = 2$. The extension to $|N| > 2$ agents with Partition Collapse ($\mathcal{P}_i = \mathcal{P}_S$ for all $i$) is conjectured to hold by the same argument, but the proof has not been carried out for the general case, and equilibrium selection in $n$-player coordination games introduces additional complications (multiple Pareto-incomparable equilibria, coalitional deviations) not addressed by Def 14.

2. **Relaxation of Partition Collapse to approximate partition alignment.** What happens when $\mathcal{P}_1 \approx \mathcal{P}_2$ in some metric sense (e.g., when the partitions agree on all but an $\epsilon$-measure set of states)? Section 3.5.3 shows that the exact result fails, but it does not characterize the rate of degradation. A quantitative version -- "if $\mathcal{P}_1$ and $\mathcal{P}_2$ agree on a $(1-\epsilon)$ fraction of states, then common $p$-belief of $E^*$ holds for $p = f(\epsilon)$" -- would connect this framework to the Monderer-Samet (1989) common $p$-belief literature. This paper does not prove such a result.

3. **Dynamic Sacred Files.** The Immutability condition (Def 7.ii) requires that $S$ is fixed. In practice, coordination environments change over time. Can the model be extended to a sequence of Sacred Files $S_0, S_1, S_2, \ldots$, each immutable within its epoch, with common knowledge re-established at each transition? The State Vector's append-only structure (Def 8.ii) suggests a natural framework, but the inter-epoch epistemic dynamics have not been analyzed.

4. **Equilibrium selection without Def 14.** Can the payoff-dominant equilibrium selection principle be replaced by a weaker condition? For instance: if common knowledge of $E^*$ holds and agents are permitted to use pre-play communication (cheap talk), does the combination suffice for payoff-dominant selection without axiomatizing it? Aumann (1990) showed that cheap talk alone does not resolve equilibrium selection in the Stag Hunt, but cheap talk combined with common knowledge of identical information may have different properties. This paper does not address this question.

5. **Computational verification.** The State Vector $V$ provides a formal audit trail, but the paper does not address the computational cost of verifying that $S$ satisfies Partition Collapse in practice. For large state spaces $\Omega$, verifying that $\mathcal{P}_1(\omega) = S(\omega)$ for all $\omega$ may be infeasible. A complexity-theoretic analysis of the verification problem is an open question.

#### 3.5.8 Is Partition Collapse Too Strong?

The most natural objection to the entire framework is that Partition Collapse (Def 7.iii) is too strong an assumption -- that it "assumes the conclusion" by forcing agents' partitions to coincide, thereby trivializing the common knowledge problem.

The objection has force but misidentifies the contribution. The common knowledge problem, as posed by Halpern-Moses and Rubinstein, is: *can common knowledge be achieved by finite agents in finite time?* Their answer is no, given message-passing channels. This paper's answer is yes, given a different architecture. The Partition Collapse property is not a free assumption: it is a *design specification* for an information structure. The contribution is the identification that such a design specification exists, is formally coherent within the Aumann partition model, and yields common knowledge at step 1.

The analogy: when Aumann (1976) assumes a common prior, one might object that the common prior "assumes the conclusion" of agreement. But the common prior is a modeling choice that identifies conditions under which agreement obtains, and its value lies in making those conditions explicit. Similarly, Partition Collapse identifies conditions under which common knowledge obtains, and its value lies in making those conditions constructive and verifiable (via the State Vector $V$). We note, however, an important disanalogy: unlike the common prior, which permits agents to have distinct information partitions over $\Omega$, Partition Collapse forces partition identity. The assumption is therefore strictly stronger than the common prior, but the payoff -- constructive common knowledge at step 1, not merely consistency of beliefs -- is correspondingly stronger.

The quantitative question -- how difficult is it to instantiate Partition Collapse in practice? -- is a question of mechanism design, not of the theorem's validity. Section 3.5.3 establishes that any violation of Partition Collapse can destroy the result entirely, which is precisely what makes it a sharp, falsifiable condition rather than a vague sufficiency claim.

---

## 4. Related Work

The Sacred File architecture engages directly with four strands of the common knowledge literature. For each, we state what the prior work achieved, where it falls short, and how this paper advances beyond it.

### 4.1 Aumann (1976): The Partition Model

Aumann (1976) proposed the partitional information model to formalize common knowledge, establishing that common knowledge of an event $E$ holds at state $\omega$ if and only if $\mathcal{P}^*(\omega) \subseteq E$, where $\mathcal{P}^*$ is the meet of agents' information partitions. But Aumann's framework is descriptive, not constructive: it characterizes the conditions under which common knowledge obtains without providing a mechanism by which agents can bring those conditions about. The partition structure is assumed exogenously given; the model does not address how partitions can be designed or constrained. This paper introduces the Sacred File (Def 7) as a constructive mechanism within Aumann's own framework. The Partition Collapse property (Def 7.iii) is a design specification that, when satisfied, forces $\mathcal{P}^* = \mathcal{P}_S$ (Lemma 1), yielding common knowledge of any $S$-encoded event (Theorem 1, Part A). Where Aumann characterized common knowledge as a property that either holds or does not, this paper shows it can be *manufactured* by architectural design.

### 4.2 Halpern and Moses (1990): Impossibility in Distributed Systems

Halpern and Moses (1990) proposed a temporal-epistemic logic for distributed systems, establishing that common knowledge cannot be attained in any system where messages may be lost. But their impossibility result is conditional on the system being a message-passing architecture with unreliable channels: the infinite regress of mutual knowledge persists because each message introduces a new layer of uncertainty about receipt. This paper introduces the Sacred File, which is not a message-passing channel and does not satisfy the Halpern-Moses communication axioms. No messages are sent, no messages can be lost, and Partition Collapse (Def 7.iii) eliminates the partition divergence that drives their impossibility. Theorem 1 (Part B) achieves what Halpern-Moses proved impossible for message-passing systems -- common knowledge in finite time -- by operating in an architectural class to which their impossibility does not apply.

### 4.3 Rubinstein (1989): The Electronic Mail Game

Rubinstein (1989) proposed the Electronic Mail Game to demonstrate that almost-common-knowledge is strategically insufficient, showing that arbitrarily many rounds of message confirmation fail to produce common knowledge when each message has a positive probability of loss, and that the unique rationalizable strategy is the risk-dominant equilibrium. But Rubinstein's result depends on the sequential, lossy channel structure: each confirmation creates a new state in which one agent's partition cell differs from the other's, preventing partition collapse. This paper introduces a shared, simultaneously accessible object (the Sacred File) that bypasses the confirmation structure entirely. Partition Collapse (Def 7.iii) ensures $\mathcal{P}_1 = \mathcal{P}_2 = \mathcal{P}_S$ without any messages, so Rubinstein's construction of divergent partition cells has no analogue. Where Rubinstein showed that message-based confirmation cannot close the epistemic gap, the Sacred File architecture closes it by architectural fiat at step 1.

### 4.4 Monderer and Samet (1989): Common $p$-Belief

Monderer and Samet (1989) proposed common $p$-belief as a relaxation of common knowledge, showing that for $p$ sufficiently close to 1, common $p$-belief of payoffs and rationality suffices for approximate ($\epsilon$-) equilibrium play. But common $p$-belief yields approximations, not exact results: the bound on $\epsilon$ degrades as the game becomes more sensitive to higher-order beliefs. For the Stag Hunt specifically, no amount of common $p$-belief for $p < 1$ eliminates the risk-dominant equilibrium from the set of rationalizable strategies; only full common knowledge ($p = 1$) does. This paper achieves $p = 1$ -- exact common knowledge -- via the Sacred File architecture, making the Monderer-Samet approximation unnecessary for games covered by Theorem 1. The approximation framework remains relevant for settings where Partition Collapse cannot be fully satisfied (Section 3.5.7, item 2).

### 4.5 Harsanyi and Selten (1988): Equilibrium Selection

Harsanyi and Selten (1988) proposed a general theory of equilibrium selection using payoff dominance and risk dominance as competing criteria, with a tracing procedure to adjudicate between them. For the Stag Hunt, their tracing procedure can select the risk-dominant equilibrium under certain prior conditions, even when payoff dominance points to $(Stag, Stag)$. This paper does not challenge the Harsanyi-Selten framework in general but provides a specific epistemic environment -- common knowledge of identical information under Partition Collapse -- in which the standard arguments for risk dominance do not apply. Under these conditions, the payoff-dominant equilibrium selection principle (Def 14) is invoked as an axiom. The contribution is the construction of the epistemic conditions, not the resolution of the payoff-dominance-versus-risk-dominance debate in general.

### 4.6 Carlsson and van Damme (1993): Global Games

Carlsson and van Damme (1993) showed that in global games -- coordination games with perturbed payoffs and noisy private signals -- the risk-dominant equilibrium is uniquely selected as noise vanishes. Their result depends on strategic uncertainty introduced by private signals: agents observe slightly different signals, creating higher-order uncertainty about the opponent's beliefs. The Sacred File architecture eliminates this channel of uncertainty entirely: Partition Collapse ensures both agents observe the same partition cell with no private signal noise. The global games selection result does not apply to the Sacred File setting because the mechanism that drives risk-dominant selection -- private signal variation -- is absent by construction.

---

## 5. Discussion

### 5.1 Common Knowledge as a Design Property

The central implication of this paper is methodological: common knowledge need not be treated as an exogenous epistemic primitive that either obtains or does not. It can be *designed into* an information architecture. The Sacred File is a blueprint: define a shared, immutable, simultaneously accessible information structure satisfying Partition Collapse (Def 7.iii), implement a State Vector satisfying Mutual Accessibility (Def 8.iii), and common knowledge of any $S$-encoded event is guaranteed at the first access step.

This reframes the common knowledge problem from an impossibility ("agents cannot achieve common knowledge in finite time") to a design problem ("under what architectural constraints does common knowledge obtain?"). The impossibility results of Halpern and Moses (1990) and Rubinstein (1989) remain valid within their scope -- message-passing systems with unreliable channels -- but the scope is narrower than previously appreciated.

### 5.2 Practical Implications

The formal objects in this paper -- the Sacred File and State Vector -- have natural analogues in real-world coordination systems. A public blockchain ledger satisfies versions of Publicity, Immutability, and Mutual Accessibility (though Partition Collapse requires that agents derive no private information beyond the ledger's content). A legally binding public contract, posted on a government registry accessible to all parties, approximates the Sacred File's structural properties. A transparent order book on an exchange allows all participants to observe the same state.

The gap between the formal model and implementation is the gap between Partition Collapse as a mathematical condition and its satisfaction in physical systems. Real systems face challenges: network latency can delay observation (threatening Mutual Accessibility), corrupted reads can violate Publicity, and side-channel information can introduce private refinements that violate Partition Collapse even when agents access the same file. These are engineering constraints, not theoretical ones, and they do not invalidate the theorem -- they identify the conditions that implementations must satisfy.

### 5.3 Implications for Multi-Agent AI Systems

Multi-agent AI systems face coordination problems structurally identical to the Stag Hunt: two agents must choose between a cooperative strategy (high payoff if both cooperate, low payoff if one defects) and a safe strategy (moderate payoff regardless). The Sacred File architecture provides a formal mechanism by which AI agents can be designed to achieve common knowledge of shared objectives and constraints, enabling coordination on payoff-dominant outcomes without the need for iterated negotiation or message-passing protocols.

The State Vector additionally provides an audit trail: if agents' actions diverge from the expected equilibrium, the State Vector records the full history of information access, enabling post-hoc analysis of coordination failures.

---

## 6. Conclusion

This paper has established three results.

First, we defined the Sacred File (Def 7) and State Vector (Def 8) as formal objects within Aumann's (1976) partition model. The Partition Collapse property of the Sacred File forces the meet of agents' information partitions to equal the partition induced by $S$ (Lemma 1), transforming common knowledge from an epistemic primitive into a design property of the information architecture.

Second, we proved that any event encoded in the Sacred File is common knowledge at every state in which it holds (Theorem 1, Part A), and that the coordination event $E^*$ -- the event that both agents are rational and face the Stag Hunt payoffs -- is common knowledge at step 1, the first moment both agents access the Sacred File (Theorem 1, Part B). The step count is 1, not "finitely many": one access to $S$ produces all levels of mutual knowledge simultaneously, bypassing the infinite regress that plagues message-passing architectures.

Third, we proved that under common knowledge of $E^*$ and the payoff-dominant equilibrium selection principle (Def 14), both agents select $Stag$, yielding the action profile $(Stag, Stag)$ with payoff $(2, 2)$ (Theorem 2). The risk-dominant equilibrium $(Hare, Hare)$ is not selected because the epistemic conditions produced by the Sacred File satisfy all three conditions of Def 14: common knowledge of rationality, common knowledge of identical information, and common knowledge of the payoff structure.

These results do not contradict the impossibility results of Halpern and Moses (1990) or Rubinstein (1989). Those results apply to message-passing systems with unreliable channels. The Sacred File is not a message-passing channel; it is a shared, immutable, simultaneously accessible information structure. The impossibility results are channel-specific, not architecture-general, and the Sacred File operates outside their scope.

The result depends on two key assumptions: Partition Collapse (Def 7.iii), which forces agents' information partitions to coincide, and the payoff-dominant equilibrium selection principle (Def 14), which converts common knowledge into a specific action profile. If Partition Collapse is weakened to Publicity alone, Theorem 1 (Part A) survives for $S$-encoded events, but Theorem 2 fails (Section 3.5.3). If Def 14 is rejected, Theorem 1 still holds -- common knowledge of $E^*$ at step 1 -- but equilibrium selection is undetermined.

The open problems are clear: extension to $|N| > 2$ agents, quantitative analysis of degradation under approximate partition alignment, dynamic Sacred Files, and alternative equilibrium selection principles. The contribution of this paper is the identification that the common knowledge problem admits a constructive, one-step solution under the right architectural constraints -- and the precise specification of what those constraints are.

---

## References

Aumann, R.J. (1976). Agreeing to disagree. *Annals of Statistics*, 4(6), 1236--1239.

Aumann, R.J. (1990). Nash equilibria are not self-enforcing. In J.J. Gabszewicz, J.-F. Richard, and L.A. Wolsey (Eds.), *Economic Decision-Making: Games, Econometrics and Optimisation*, pp. 201--206. Elsevier.

Battalio, R., Samuelson, L., and Van Huyck, J. (2001). Optimization incentives and coordination failure in laboratory stag hunt games. *Econometrica*, 69(3), 749--764.

Carlsson, H. and van Damme, E. (1993). Global games and equilibrium selection. *Econometrica*, 61(5), 989--1018.

Halpern, J.Y. and Moses, Y. (1990). Knowledge and common knowledge in a distributed environment. *Journal of the ACM*, 37(3), 549--587.

Harsanyi, J.C. and Selten, R. (1988). *A General Theory of Equilibrium Selection in Games*. MIT Press.

Luce, R.D. and Raiffa, H. (1957). *Games and Decisions: Introduction and Critical Survey*. Wiley.

Monderer, D. and Samet, D. (1989). Approximating common knowledge with common beliefs. *Games and Economic Behavior*, 1(2), 170--190.

Rankin, F.W., Van Huyck, J.B., and Battalio, R.C. (2000). Strategic similarity and emergent conventions: Evidence from similar stag hunt games. *Games and Economic Behavior*, 32(2), 315--337.

Rubinstein, A. (1989). The Electronic Mail Game: Strategic behavior under "almost common knowledge." *American Economic Review*, 79(3), 385--391.

Skyrms, B. (2004). *The Stag Hunt and the Evolution of Social Structure*. Cambridge University Press.
