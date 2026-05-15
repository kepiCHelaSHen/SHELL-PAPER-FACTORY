# STATE VECTOR
# Written at end of every turn. Read at start of every turn.
# DO NOT EDIT MANUALLY — managed by Orchestrator only.
# Format is machine-readable. One key per line. No blank lines between keys.

TURN: 0
MILESTONE: M1
MODE: INIT
FLAGS: NONE
CONSECUTIVE_BLOCKS: 0
CONSECUTIVE_PLATEAU_TURNS: 0
LAST_COMMITTED_METRICS: N/A
LAST_COMMITTED_TURN: N/A
EXPERIMENT: [EXPERIMENT NAME]
TIMESTAMP: [initialization time]

---
# FLAG LEGEND
# ANOMALY           — Unexpected spike or discontinuity in output metrics
# INSTABILITY       — Variance too high across seeds (CV > threshold)
# TREND_DEGRADATION — Metric moving wrong direction across turns
# PLATEAU           — No improvement for N consecutive turns (see orchestrator)
# NONE              — All clear

# MODE LEGEND
# INIT        — Before loop start
# VALIDATION  — Actively testing against frozen spec
# EXPLORATION — Validated; searching for improvements within spec
