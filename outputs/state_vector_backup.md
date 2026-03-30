# STATE VECTOR BACKUP
# Written by Orchestrator before any high-risk operation (reversion, mode switch, milestone transition).
# If state_vector.md is ever corrupted or lost, restore from here.
# Format mirrors state/state_vector.md exactly.

=== BACKUP TAKEN: [TIMESTAMP] ===
=== REASON: [e.g., "Pre-reversion to Turn 4 commit" / "Mode switch VALIDATION → EXPLORATION"] ===

TURN: [N]
MILESTONE: [M1 / M2 / M3 / M4]
MODE: [VALIDATION / EXPLORATION]
FLAGS: [NONE / flag list]
CONSECUTIVE_BLOCKS: [N]
CONSECUTIVE_PLATEAU_TURNS: [N]
LAST_COMMITTED_METRICS: [metric: value, metric: value]
LAST_COMMITTED_TURN: [N]
EXPERIMENT: [EXPERIMENT NAME]
TIMESTAMP: [time of state being backed up]

---

[No backups yet.]
