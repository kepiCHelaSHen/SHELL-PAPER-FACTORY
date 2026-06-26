# SACRED FILES
# Files that must never be modified after the lock date.
# The Critic checks this list at the start of every turn.
# If a sacred file is touched, the experiment is invalidated.

Lock date: 2026-05-16

## Sacred Files

| File | Reason | Locked |
|------|--------|--------|
| `papers/*/frozen_spec.md` | The oracle. Modifying it changes what we are validating. | Per-paper at init |
| `STEELMAN_FINDINGS.md` | Append-only. Existing entries are permanent record. Never edit, only append. | 2026-05-16 |
| `DEAD_ENDS.md` | Append-only. Failed approaches are permanent. Never delete entries. | 2026-05-16 |
| `papers/init_REPLICATION_CRISIS_2026.md` | Published paper init. Modifying invalidates provenance. | 2026-05-15 |
| `papers/init_DRUG_SPENDING_2026.md` | Published paper init. Modifying invalidates provenance. | 2026-05-15 |
| `papers/init_TECH_LOCKIN_2026.md` | Published paper init. Modifying invalidates provenance. | 2026-05-15 |
| `papers/init_OPIOID_PRESCRIBING_2026.md` | Published paper init. Modifying invalidates provenance. | 2026-05-15 |
| `papers/init_VACCINE_GAME_2026.md` | Published paper init. Modifying invalidates provenance. | 2026-05-15 |
| `papers/init_HOSPITAL_PRICING_2026.md` | Published paper init. Modifying invalidates provenance. | 2026-05-15 |
| `papers/init_CANARY_REGRESSION.md` | Regression baseline. Modifying invalidates all future comparisons. | 2026-05-16 |
| `published_manifest.json` | Zenodo DOI record. Append-only after publication. | 2026-05-16 |

## Rules

1. If unsure whether a file is safe to touch — do not touch it.
2. If a sacred file must change, halt the loop, document why, create a new
   versioned spec, and restart from Turn 0. Log the restart in DEV_LOG.md.
3. Append-only files (STEELMAN_FINDINGS, DEAD_ENDS) may have new entries added
   but existing entries must never be modified or deleted.
4. Published paper inits are locked because their DOIs point to papers generated
   from these exact specifications.
