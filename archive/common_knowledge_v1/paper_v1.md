# ARCHIVED — Common Knowledge Paper v1
# Run date: 2026-03-30
# Status: First run, single-turn pipeline, pre-shell-upgrade
# Notes: Good proof structure, real citations, Peer Reviewer caught ω ∈ E error.
#        Missing: adversarial stress-test, formalism-first, literature gap formula,
#        Lean-ready proof structure, milestone-by-milestone gating.
#        Archived for before/after comparison with v2.

# A Deterministic Solution to the Infinite Regress of Common Knowledge

**James P. Rice Jr.**

---

## Abstract

Common knowledge — the condition in which all agents know a proposition, all agents know that all agents know it, and so on ad infinitum — is foundational to game-theoretic analyses of coordination but practically unattainable under standard information structures because the epistemic regress is infinite. This paper introduces a constrained information architecture consisting of two components: a **Sacred File** (a shared, immutable public document) and a **State Vector** (an append-only audit log confirming each agent's access). We prove, using the partitional information model of Aumann (1976), that when two rational agents read the same Sacred File and the State Vector confirms mutual access, the information partition collapses to a single element, achieving common knowledge in exactly one step. We apply this result to the Stag Hunt coordination game, showing that under this architecture rational agents deterministically select the payoff-dominant equilibrium (Stag, Stag), eliminating coordination failure without requiring repeated interaction, costly signaling, or external enforcement. The result provides a constructive mechanism for achieving common knowledge in multi-agent systems, with implications for mechanism design, artificial intelligence, and organizational theory.

---

## 1. Introduction

The concept of common knowledge occupies a peculiar position in game theory: it is simultaneously indispensable and practically impossible. Since Aumann's (1976) foundational formalization, common knowledge has been recognized as a necessary condition for many equilibrium concepts, including the selection among multiple Nash equilibria in coordination games. Yet the definition itself — an infinite regress of mutual knowledge — presents an immediate operational problem. How can finite agents, operating in finite time, ever establish that an infinite tower of epistemic conditions holds?

The standard answer has been to treat common knowledge as an idealization. In the epistemic logic tradition (Fagin, Halpern, Moses, & Vardi, 1995), the common knowledge operator C is defined as the infinite conjunction of iterated knowledge operators: Cp = Ep ∧ EEp ∧ EEEp ∧ ..., where E denotes "everyone knows." This definition is analytically precise but operationally vacuous — no finite procedure can verify infinitely many conditions.

The practical consequence is coordination failure. Consider the **Stag Hunt** (Luce & Raiffa, 1957; Skyrms, 2004), a canonical two-player coordination game with the following payoff matrix:

|  | **Stag** | **Hare** |
|---|---|---|
| **Stag** | (2, 2) | (0, 1) |
| **Hare** | (1, 0) | (1, 1) |

This game has two Nash equilibria in pure strategies: (Stag, Stag) with payoff (2, 2) and (Hare, Hare) with payoff (1, 1). The first is payoff-dominant; the second is risk-dominant. Rational agents who lack common knowledge of each other's rationality face a coordination problem: choosing Stag is optimal only if the other agent also chooses Stag, but believing the other will choose Stag requires knowing that the other knows you will choose Stag, which requires knowing that the other knows you know, and so on. The infinite regress of common knowledge directly maps onto the infinite regress of strategic confidence required for coordination on (Stag, Stag).

This paper resolves the infinite regress by construction. We introduce an **information architecture** — a specific arrangement of information access and audit — under which common knowledge is achieved in a single, finite step. The architecture consists of two formal objects:

1. **The Sacred File** — a shared document that is publicly readable by all agents and whose content is identical for every reader. It is not a communication channel; it is a shared epistemic state.

2. **The State Vector** — an append-only log that records which agents have read the Sacred File and when. It provides the second-order confirmation: not only does each agent know the content of the Sacred File, but each agent knows that every other agent also knows it.

We prove that under Aumann's (1976) partitional information model, the combination of these two objects collapses the information partition to a single element after a single shared read, thereby achieving common knowledge at step 1. We then apply this result to the Stag Hunt, showing that the architecture deterministically selects the payoff-dominant equilibrium.

The contribution is threefold. First, we provide a constructive proof that common knowledge can be achieved in finite (indeed, unit) time under a well-defined information architecture, resolving a gap between the theoretical requirement and practical impossibility identified by Halpern and Moses (1990). Second, we demonstrate that the architecture eliminates coordination failure in the Stag Hunt without repeated interaction (Kandori, Mailath, & Rob, 1993), costly signaling (Spence, 1973), or external enforcement. Third, we offer a formal framework applicable to multi-agent AI systems, organizational design, and mechanism design wherever coordination on a payoff-dominant equilibrium is desired but common knowledge has been assumed rather than constructed.

---

## 2. Formal Model

### 2.1 Agents and States

Let N = {1, 2} be the set of agents. Let Ω be a finite set of states of the world. Each state ω ∈ Ω specifies the full description of the environment relevant to the agents' decisions, including the game being played, the payoff structure, and each agent's rationality.

### 2.2 Information Partitions

Following Aumann (1976), each agent i ∈ N is endowed with an **information partition** P_i of Ω. For any state ω ∈ Ω, let P_i(ω) denote the element of P_i containing ω — the set of states that agent i cannot distinguish from ω. Agent i **knows** an event E ⊆ Ω at state ω if and only if P_i(ω) ⊆ E.

Define the **knowledge operator** for agent i:

K_i(E) = {ω ∈ Ω : P_i(ω) ⊆ E}

The **mutual knowledge operator** is:

E(E) = K_1(E) ∩ K_2(E)

That is, an event is mutually known at ω if both agents know it at ω.

**Common knowledge** is the infinite intersection:

C(E) = E(E) ∩ E(E(E)) ∩ E(E(E(E))) ∩ ...

Equivalently, in Aumann's formulation: an event E is common knowledge at ω if and only if the element of the **meet** of the partitions P_1 and P_2 containing ω is a subset of E. The meet, denoted P_1 ∧ P_2, is the finest partition that is coarser than both P_1 and P_2.

**Definition 1 (Common Knowledge).** An event E ⊆ Ω is common knowledge at state ω if and only if (P_1 ∧ P_2)(ω) ⊆ E.

### 2.3 The Standard Problem

Under a generic information structure, P_1 and P_2 may be arbitrarily fine, meaning the meet P_1 ∧ P_2 may have many elements. In such cases, even if both agents know an event E (mutual knowledge), the meet element containing the true state may not be a subset of E, and common knowledge fails.

### 2.4 The Sacred File

**Definition 2 (Sacred File).** A **Sacred File** is a function S: Ω → X, where X is a message space, satisfying:

(i) **Publicity:** For all ω ∈ Ω and all i ∈ N, S(ω) is observable to agent i.
(ii) **Determinism:** S is measurable with respect to the meet P_1 ∧ P_2.
(iii) **Completeness:** S encodes all payoff-relevant information.

### 2.5 The State Vector

**Definition 3 (State Vector).** A **State Vector** is an append-only function V: Ω × N → {0, 1}, where V(ω, i) = 1 indicates that agent i has read the Sacred File at state ω. The State Vector is itself publicly observable.

### 2.6 The Combined Architecture

**Definition 4 (Sacred File Architecture).** The **Sacred File Architecture** is the information structure (Ω, N, {P_i^*}, S, V), where P_i^*(ω) = {ω' ∈ Ω : S(ω') = S(ω) and V(ω', j) = V(ω, j) for all j ∈ N}.

---

## 3. Proof: Common Knowledge at Step 1

**Lemma 1.** Under the Sacred File Architecture, if V(ω, i) = 1 for all i ∈ N, then P_1^*(ω) = P_2^*(ω).

**Lemma 2.** If P_1^*(ω) = P_2^*(ω), then the meet (P_1^* ∧ P_2^*)(ω) = P_1^*(ω) = P_2^*(ω).

**Theorem 1 (Common Knowledge at Step 1).** Under the Sacred File Architecture, once all agents have read the Sacred File, any event E = S^{-1}(X_E) is common knowledge at every state ω ∈ E.

**Corollary 1.** The common knowledge regress terminates at step 1.

---

## 4. Application: Stag Hunt Coordination

**Theorem 2 (Stag Hunt Resolution).** Under the Sacred File Architecture, rational agents select (Stag, Stag).

---

## 5. Discussion

### 5.1 Relationship to Prior Work
Halpern-Moses impossibility, Rubinstein Electronic Mail Game, Monderer-Samet common p-belief.

### 5.2–5.4 Implications
Multi-agent AI systems, mechanism design, organizational theory.

### 5.5 Limitations
Two agents, static game, rationality assumption, State Vector honesty.

---

## 6. Conclusion

The Sacred File Architecture achieves common knowledge in exactly one step, eliminating coordination failure in the Stag Hunt.

---

## References

Aumann (1976), Fagin et al. (1995), Halpern & Moses (1990), Kandori et al. (1993),
Luce & Raiffa (1957), Monderer & Samet (1989), Rubinstein (1989), Schelling (1960),
Skyrms (2004), Spence (1973).
