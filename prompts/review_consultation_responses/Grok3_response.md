**CURRENT DIMENSIONS: KEEP / MODIFY / DROP**

1. **Originality** — KEEP. Core gate. Make it stricter: distinguish incremental vs. substantive novelty.
2. **Mathematical Rigor** — KEEP. Non-negotiable for any paper with formal content. Split scoring into correctness and presentation.
3. **Literature Awareness** — MODIFY → “Positioning & Citation Integrity”. Current version too soft; must explicitly check for missing seminal works and citation accuracy.
4. **Intellectual Honesty** — KEEP. Merge minor overlap with limitations discussion into this single dimension.
5. **Clarity of Writing** — MODIFY → “Precision & Economy of Language”. Current label too vague; penalize hedging, filler, and AI-typical syntactic patterns.
6. **Policy Relevance** — DROP. Not universally applicable. Replace with domain-specific relevance when appropriate rather than a universal score.
7. **Conceptual Compression** — KEEP but rename “Problem Formalization Quality”. Valuable but currently too subjective.
8. **Empirical Grounding** — MODIFY → “Justification of Assumptions & Parameters”. Covers both empirical and theoretical papers.
9. **Publishability** — DROP. This is an output variable, not an input dimension. It should be derived from the other scores.
10. **Overall Coherence** — MODIFY → “Logical Consistency Across Sections”. Narrow to detecting internal contradictions.

**PROPOSED NEW SCORED DIMENSIONS**

1. **Methodological Soundness** — Evaluates whether the chosen approach is appropriate for the stated research question and whether alternative methods were considered.
2. **Reproducibility & Transparency** — Assesses availability of data, code, hyperparameters, and step-by-step procedures sufficient for independent replication.
3. **Statistical & Inferential Validity** — Checks for correct application of statistical methods, multiple-testing correction, effect-size reporting, and avoidance of p-hacking signals.
4. **Argumentative Structure** — Measures logical flow, premise-to-conclusion validity, and absence of non-sequiturs or circular reasoning.
5. **Citation Integrity** — Verifies that citations are accurate, relevant, and not fabricated or misrepresented.

**PROPOSED BOOLEAN CHECKS**

1. **AI_WRITTEN_DETECTION** — Pass if the paper exhibits natural human variation in sentence length, sparse hedging, domain-specific idioms, and non-templated citation integration. Fail on repetitive syntactic patterns or “academese” filler.
2. **EFFORT_ESTIMATION** — Provide estimated person-months, minimum expertise level (PhD/postdoc/faculty), and research calendar time. Fail if estimate is unrealistically low for claimed contribution.
3. **Citation Fabrication** — Fail if any reference is unverifiable, malformed, or attributed to a paper that does not contain the claimed statement.
4. **Logical Fallacy** — Fail on detectable instances of equivocation, false dichotomy, appeal to authority, or post-hoc reasoning in core arguments.
5. **Scope Creep** — Fail if the paper claims results beyond what the stated methodology and evidence can support.
6. **Data/Result Fabrication Signals** — Fail on impossible precision, missing variance, or effect sizes that violate domain constraints without justification.
7. **Assumption Sensitivity** — Fail if the paper does not test robustness to key assumptions or if conclusions collapse under reasonable perturbations.
8. **Formatting & Compliance** — Fail if the manuscript violates target journal formatting or ethical statement requirements.

**QUALITATIVE SECTION IMPROVEMENTS**

- Add “Desk-Rejection Simulation”: Would an editor at the target venue send this for review or reject outright?
- Replace free-form “hostile reviewer” with structured attack vectors: (a) theoretical flaw, (b) empirical weakness, (c) missing literature, (d) over-claiming.
- Add “Minimum Revision Threshold”: List the smallest set of changes that would make the paper acceptable rather than open-ended criticism.
- Require explicit statement of “fatal flaw” if any dimension ≤ 3.

**SCORING METHODOLOGY RECOMMENDATIONS**

- Weighting: Originality (15%), Mathematical/Methodological Rigor (20%), Citation Integrity (15%), Logical Consistency (15%), Reproducibility (10%), remaining dimensions 5% each.
- Automatic fail if any of the following occur: AI_WRITTEN_DETECTION = fail, Citation Fabrication = fail, any core dimension (Originality, Rigor, Integrity) ≤ 3, composite < 7.0.
- No sub-scores inside dimensions; force reviewers to pick one integer 1–10.
- Composite = weighted average rounded to one decimal. Require ≥ 8.0 for “pass” across at least three independent reviewers.

**REVIEWER PERSONA & FRAMING RECOMMENDATIONS**

Frame the reviewer as: “You are a senior associate editor at a top-tier journal (e.g., Econometrica, QJE, Nature Methods, IEEE TPAMI) with 15+ years of reviewing experience. Your default stance is skeptical. You look for reasons to reject first. You have been burned by fabricated citations and overstated claims before. You will not give the benefit of the doubt. You will flag even small inconsistencies.”

Explicit bias guards: (1) do not reward length, (2) do not reward complexity for its own sake, (3) ignore institutional prestige signals (none present), (4) penalize performative rigor that does not advance the claim.

**WILD CARDS — THINGS YOU THINK WE’RE MISSING**

- “Reference Echo Chamber” check: does the paper only cite recent, highly similar work while ignoring foundational or contradictory literature?
- “Result Cherry-Picking” check: are only favorable specifications or datasets reported?
- “Contribution Inflation” check: does the abstract or introduction claim more than the actual technical increment justifies?
- Cross-model consistency requirement: any dimension differing by >3 points across reviewers triggers mandatory re-review with explicit discrepancy resolution.
- Mandatory “adversarial example” test for empirical papers: reviewer must propose one concrete change to data or specification that would overturn the main result.
