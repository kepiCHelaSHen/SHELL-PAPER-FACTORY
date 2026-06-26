# SHELL v6.5 — Current Status
# Updated: 2026-06-26

Phase:   MAINTENANCE — Engine fixes, documentation sync, preparing for v7
Mode:    POST-PUBLICATION CLEANUP

## What Is Done

### Engine (SHELL v6.5)
- Author v5 prompt: anti-AI-detection writing discipline + ASSAY citation reform
- Orchestrator v5 wiring: passes ASSAY data to all Author dispatches
- Editor v3 with E21-E24 AI-detection editorial checks
- External review v2: 15 dimensions, 12 boolean forensic checks, weighted scoring
- Review panel: Gemini 2.5 Pro (primary) + Grok-3 ×2 (adversarial, double-run)
- Auto-parse: scripts/parse_reviews.py extracts scores and flags disagreements
- Feedback loop: scripts/revise_from_review.py builds targeted revision briefs
- Regression canary: Prisoner's Dilemma NE paper, baseline established

### ASSAY (Analytics Engine)
- 19 completed analysis reports across 8 domains
- v1.1 integration blocks: data_appendix_fragment, data_availability_statement,
  forbidden_interpretations_prose, data_sources provenance
- generate_appendix_fragment.py produces Data Appendix prose from any report
- .gitignore excludes raw data files (only code/config/YAML committed)

### Papers (6 published to Zenodo with DOIs)

| Paper | Gemini | Grok | B1 (AI) | B3 (Citations) |
|-------|--------|------|---------|----------------|
| REPLICATION_CRISIS | ACCEPT (9.06) | MINOR (8.10) | PASS | PASS |
| DRUG_SPENDING | MINOR (9.18) | MINOR (8.09) | PASS | PASS |
| TECH_LOCKIN | MINOR (8.88) | MAJOR (8.10) | Grok flag | PASS |
| OPIOID_PRESCRIBING | MINOR (8.58) | MINOR (7.79) | PASS | PASS |
| VACCINE_GAME | MINOR (8.52) | MINOR (7.91) | PASS | PASS |
| HOSPITAL_PRICING | MINOR (~8.5) | MINOR (7.89) | PASS | PASS |

All 6 pass citation integrity (B3=PASS) across all reviewers.
5/6 pass AI detection on both models. Only TECH_LOCKIN flagged by Grok.

### Additional Papers
- RWE_OPIOID_VARIATION: 4 runs, Gemini ACCEPT (seven 10s, min 9)
- RWE_OPIOID_VARIATION_VALIDATED: Pipeline-validated A/B test variant
- CANARY_REGRESSION: Baseline established for regression testing

### Engine Fixes Applied (2026-06-26)
- CR-1: Fixed ASSAY citation contradiction (Peer Reviewer U8e vs Author Rule 5F)
- Renumbered duplicate RULE 6 in Author prompt (now RULE 6 figures, RULE 7 claims)
- Fixed LEARNINGS.md example to use public-source citation format
- Fixed CHAIN_PROMPT template to reflect Claude-only v5 pipeline (was Grok/GPT-4o)
- Fixed Steelman RWE verdict rubric ordering (was before A13/A14, now after)
- Updated prompts/README.md init file references (removed nonexistent, added actual)
- Added .obsidian/ to .gitignore

## What Is Next
- [x] Publish all 6 papers to Zenodo — DONE (DOIs assigned)
- [x] Fix pipeline-breaking ASSAY citation contradiction — DONE
- [x] Fix engine prompt inconsistencies — DONE
- [ ] Rotate API keys before next canary run
- [ ] Run canary as regression test to validate engine fixes
- [ ] Consider TECH_LOCKIN editing pass to eliminate final Grok AI flag (optional)
- [ ] v7 Phase 2: quality improvements (formalism budget, hedging budget, dedup agent)
- [ ] v7 Phase 3: PROSPECT → ASSAY → SHELL closed loop (no manual handoffs)
- [ ] Build observability dashboard (web tier)
- [ ] Migrate from CLI to API when ready for production runs
