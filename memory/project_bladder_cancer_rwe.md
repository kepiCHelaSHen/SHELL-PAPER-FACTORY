---
name: Bladder cancer RWE project
description: Planning to generate RWE reports from Norstella NLP bladder cancer data (25M rows, 8 tables) using SHELL + pharmaverse. Work will happen on work machine with Redshift MCP.
type: project
originSessionId: 8f39d8f9-8379-45ef-bc28-07f2f484bfc7
---
## Bladder Cancer RWE — Project Plan

**Data source:** Norstella production Redshift (`rwd_production.nlp_bladder_cancer`), 8 master tables, 25.4M total rows. NLP-extracted from clinical notes. 94%+ extraction accuracy validated by data science team.

**Why:** Demonstrate end-to-end autonomous RWE generation from Norstella's own data. CEO/CTO demo. Commercial value: pharma companies pay $200-500K per RWE study.

**How to apply:** When the user works from their work machine with Redshift MCP connected, this context applies. The full analysis plan and pharmaverse mapping are in the conversation where this was planned.

### Key Tables
- diagnosis_master (6.5M) — conditions, recurrence status, severity
- medication_master (4M) — drugs, response, AEs, intent, discontinuation reason, name_curated
- surgery_master (5.5M) — procedures, outcomes
- tumor_properties_master (1.4M) — staging (TNM curated), grade, margins, invasion, metastasis
- tumor_properties_supplemental_master (1.4M) — BCG refractory, CIS, risk level, focality
- tumor_events_master (2M) — progression, recurrence events
- risk_factors_master (3.8M) — clinical risk factors from notes
- radiation_master (627K) — radiation tx, concurrent chemo flag

### Priority Reports (in order)
1. BCG-unresponsive outcomes (is_bcg_refractory field exists, FDA regulatory pathway, highest commercial value)
2. Real-world AE profiles by regimen (medication.adverse_event fields)
3. Treatment sequencing by stage
4. Immunotherapy adoption and real-world response
5. Recurrence patterns and surveillance
6. Metastatic treatment and outcomes

### Pharmaverse Integration
- R layer sits between ASSAY and SHELL
- admiral + admiralonco for SDTM→ADaM derivation
- tern for statistical analysis, rtables for regulatory tables
- NLP tables map to SDTM domains: medication→CM/EX, tumor_properties→TR, medication.adverse_event→AE, surgery→PR

### Key Schema Notes
- No demographics in the 8 NLP tables (age, sex, race) — needs enrichment from other Norstella RWD via norstella_patient_id join
- medication_master has name_curated (normalized drug names), response, adverse_event, intent, reason_for_discontinuation — these are the gold fields
- _origin and _evidence fields provide NLP provenance chain
- All tables link via norstella_patient_id → clinicalnoteid → encounterid

### Before First Analysis
- Profile date ranges (MIN/MAX notedatetime) to determine temporal span
- Profile null rates on key fields (response, adverse_event, intent)
- Profile value distributions on staging, grading, medication names
- Need 18+ months for time-to-event analyses, 6 months sufficient for descriptive/AE studies

### Init File Requirements
- Frozen spec must encode bladder cancer treatment paradigms (BCG induction/maintenance, cisplatin eligibility, NCCN guidelines)
- Drift risks must include observational study biases (immortal time bias, confounding by indication, informative censoring)
- ASSAY integration blocks built from live Redshift queries
- 94% NLP accuracy figure goes in as known limitation with sensitivity analysis requirement
