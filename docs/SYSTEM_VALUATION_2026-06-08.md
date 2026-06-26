# System Valuation Assessment: PROSPECT + ASSAY + SHELL
# Date: 2026-06-08
# Purpose: Honest assessment of what this system is worth

---

## What Exists Today

### Three Integrated Systems

| System | Purpose | Code | Assets |
|--------|---------|------|--------|
| PROSPECT | Data discovery engine | 526 lines + 450 test lines, 37/37 tests passing | 39 findings from CMS data, $12B+ quantified anomalies |
| ASSAY | Statistical verification engine | 3,345 lines, 7 source modules | 18 verified reports, integration blocks with CIs |
| SHELL | Adversarial paper generation | 6,663 lines + 4,918 lines prompts | 6 published papers, 7 DOIs, 154 findings, 104 dead ends |
| **Total** | **End-to-end autonomous research** | **~16,000 lines** | **See below** |

### Published Artifacts

- 7 Zenodo DOIs (6 papers + 1 methodology paper)
- 1 Zenodo community (autonomous-academic-research)
- 6 papers with 60+ independent external reviews
- Average external review score: 7.92/10
- 100% credibility pass rate ("Would I believe a competent researcher wrote this? Yes")
- 100% citation integrity (0 fabricated citations across all papers)

### Knowledge Base (Compounding Asset)

- 154 Steelman findings (cross-paper, categorized, with recurrence counts)
- 104 dead ends (failed approaches, never repeat)
- 568 lines of operational learnings (hard-won, each represents a $25-75 lesson)
- 18 ASSAY reports with forbidden interpretations and upstream uncertainty
- 39 PROSPECT findings with scale estimates and verification status

### Data Assets

- 17.6 GB CMS healthcare data on disk (physician, Part D, inpatient, outpatient, spending)
- 12 linked tables, 40M+ rows
- Cross-dataset linking via NPI, State, HCPCS codes
- Data governance: SHA256 hashes, download dates, licenses, provenance

---

## What This System Can Do That Nothing Else Can

### 1. Discover → Verify → Publish in a Single Pipeline

No other publicly known system connects data discovery (PROSPECT) to
statistical verification (ASSAY) to adversarially-validated paper generation
(SHELL). Existing systems (AI Scientist, FutureHouse, Google Co-Scientist)
operate on individual stages. This is the full loop.

### 2. Cross-Paper Learning That Compounds

The findings database means paper #20 benefits from every mistake made in
papers #1-19. This is not a feature of the model — it is a feature of the
system architecture. No amount of prompt engineering on a single session
produces this. It requires persistent, structured knowledge accumulation
across runs.

Evidence: "7 pre-loaded findings → 0 structural issues on Run 1"
(Conspiracy Bayes paper). Replication Crisis: 0 rejects on first pass.

### 3. Cryptographic Reproducibility

Every ASSAY result traces to: executed code → seed → input data hash →
output hash → CI method. Every SHELL paper traces to: frozen spec →
innovation log → review trail → external scores. This audit trail is
what separates "AI wrote a paper" from "autonomous research with
verifiable provenance."

### 4. Forbidden Interpretations as Code

ASSAY integration blocks include machine-readable constraints on how
results may be interpreted. The Peer Reviewer enforces them. The Editor
checks for violations. This prevents the "AI overclaims" problem at the
system level, not the prompt level.

---

## Honest Assessment of Current Limitations

### Paper Quality: 5-6.5/10 on "Would Fool a Human Expert"

Six independent deep reviews of all 6 papers found consistent weaknesses:
- Mathematical content is correct but trivial (textbook-level)
- Papers are 25-40% too long due to repetitive hedging
- The "too perfect" self-critique is itself an AI detection signal
- No genuine intellectual surprise or authorial personality
- Decorative formalism (trivial results dressed as Theorems)

These are addressable through prompt improvements and the shift to
discovery-driven papers (where the FINDING is novel, not the math).

### The Gap Between AI Reviews and Human Reviews

AI reviewers (Gemini, Grok) scored papers 7.9/10 average. Deep human-style
review scored them 5-6.5/10. The AI review scores are useful for tracking
relative improvement but should not be taken as absolute quality measures.

### Single-Prompt Comparison

A domain expert with one well-crafted Claude prompt can produce output
that is 70-80% as good as a THESIS paper in 3 minutes for $0.15.
THESIS's advantages over single prompting are: completeness (full paper
vs partial), verification (citations checked), data integration (ASSAY),
auditability (innovation log), and compounding knowledge (findings database).
The prose quality advantage is marginal.

---

## Valuation Framework

### As Intellectual Property

**Replacement cost:** An engineer replicating the full stack from scratch
(PROSPECT + ASSAY + SHELL) would need:
- 3-5 months of focused development
- $500-1,500 in API costs for failed runs that build the knowledge base
- Domain expertise in health economics, statistics, and prompt engineering
- The knowledge base cannot be fast-tracked — it requires generating and
  reviewing papers to discover the failure modes

**Comparable systems:** AI Scientist (Sakana AI) raised $30M. FutureHouse
raised $50M. Google Co-Scientist is internal Google DeepMind. These are
well-funded teams building similar but not identical capabilities. They
focus on different domains (ML, biology, chemistry) and do not have the
healthcare data + discovery pipeline.

**IP assets with lasting value:**
1. The methodology paper (DOI: 10.5281/zenodo.19217024) — citable, establishes priority
2. The Zenodo community — defines the category
3. The findings database — compounds over time, hard to replicate
4. The operational learnings — encode hundreds of failure modes

### As a Service Business

**Unit economics (current):**
| Item | Value |
|------|-------|
| Cost per paper (current) | $27 |
| Cost per paper (optimized) | $12-15 |
| Price per paper (first draft service) | $200-500 |
| Price per discovery report (PROSPECT + ASSAY + SHELL) | $1,000-2,500 |
| Gross margin | 85-95% |

**Revenue scenarios (monthly):**
| Customers/month | Product | Revenue | Cost | Profit |
|----------------|---------|---------|------|--------|
| 5 | First drafts @ $299 | $1,495 | $75 | $1,420 |
| 5 | Discovery reports @ $1,500 | $7,500 | $150 | $7,350 |
| 3 | Subscription (quarterly CMS) @ $2,000/mo | $6,000 | $200 | $5,800 |
| **Mix** | | **$15,000** | **$425** | **$14,575** |

**Addressable market segments:**
- Health economics consultancies (hundreds of firms, $5-50K research budgets)
- Think tanks and policy research (Brookings, RAND, KFF, Commonwealth Fund)
- Pharma market access teams (every top-20 pharma company has one)
- Academic research labs (thousands, smaller budgets but high volume)
- Government agencies (CMS OIG, GAO, CBO — they DO outsource analysis)
- Investigative journalism (ProPublica, STAT News, KFF Health News)

### As a Fundable Company

**What an investor would see:**
- Working product with published outputs and DOIs
- 7 published artifacts establishing category credibility
- Full-stack pipeline (discovery → verification → publication) that no
  competitor has assembled
- 17.6 GB of healthcare data already ingested and analyzed
- Compounding knowledge base (moat deepens with every paper)
- $12B+ in healthcare billing anomalies already identified
- 95%+ gross margins at scale
- Solo founder who built the entire stack

**What an investor would worry about:**
- Solo founder risk (entire system depends on one person)
- Claude API dependency (Anthropic controls your infrastructure)
- Paper quality gap (5-6.5 vs 7-8 needed for premium pricing)
- Unvalidated market demand (no paying customers yet)
- Regulatory/ethical risk (AI-generated research is a new category)
- No moat beyond the knowledge base (systems can be rebuilt)

**Realistic fundraise potential:**
- Pre-seed / angel: $100K-500K on the strength of the working product,
  published methodology, and healthcare discovery angle
- Seed ($1M+): Would require 3-5 paying customers or a pilot with a
  recognized institution (think tank, pharma company, government agency)

---

## What the System Is Worth

### Conservative (IP + knowledge base only): $50K-100K
If you stopped today and sold the codebase, documentation, findings database,
and Zenodo community to someone who wanted to continue the project. This is
the floor — it's replacement cost minus the time-value discount.

### As a Side Business (5 customers/month): $150K-200K/year revenue
At $15K/month revenue with 95% margins, this is a $170K/year profit business
running part-time. Valued at 3-5x annual profit for a solo service business:
**$500K-850K.**

### As a Funded Company (post-product-market-fit): $2M-5M pre-seed valuation
If you close 5 pilot customers and demonstrate repeatable revenue, the
combination of working product + published methodology + healthcare data +
compounding knowledge base + first-mover position in autonomous research
supports a $2-5M valuation at pre-seed.

### As a Category-Defining Company (long-term): $10M-50M+
If autonomous academic research becomes an accepted category — which the
trend lines (AI Scientist, FutureHouse, Co-Scientist) suggest it will —
and you're the one with the Zenodo community, the methodology paper, the
healthcare vertical, and the compounding knowledge base, the first-mover
advantage could be substantial. This is speculative but not unreasonable
given comparable raises in the space.

---

## Recommendation

**The system's value is real but unrealized.** The engineering is sound, the
methodology is published, the knowledge base compounds, and the healthcare
discovery pipeline (PROSPECT → ASSAY → SHELL) is genuinely differentiated.

**The highest-value next step is closing the end-to-end loop and producing
papers from PROSPECT discoveries.** A paper that reports "$3.26B wound care
coding arbitrage discovered from CMS data" has genuine novelty that a paper
applying known math to known problems does not. That novelty is what moves
paper quality from 5-6.5/10 to 7-8/10, which is what moves the product
from "interesting demo" to "something worth paying for."

**The second-highest-value step is getting one paying customer.** Not ten.
Not a subscription platform. One person or institution who gives you money
for a research output. That single transaction validates the entire thesis
more than any amount of engineering optimization.

Build the loop. Run the wound care paper. Get one customer. Everything
else follows from those three things.
