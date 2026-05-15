# FROZEN SPECIFICATION
# Experiment: [EXPERIMENT NAME]
# Locked: [DATE]
# Author: James P Rice Jr.
# Status: LOCKED — DO NOT MODIFY AFTER LOOP START

---

## LOCK CONFIRMATION

This specification was locked before the build loop began. Any modification after
this date invalidates the experiment. If the spec needs to change, halt the loop,
document why, create a new versioned spec file, and restart from Turn 0.

Locked by: James P Rice Jr.
Lock date: [DATE]
Loop start turn: 1

---

## PARAMETERS

Replace each block below with the real parameter. One block per parameter.
Delete unused blocks. Add more as needed — same format.

---

PARAMETER: [name]
VALUE: [exact value]
UNIT: [unit of measurement or "dimensionless"]
TOLERANCE: [exact match / ± X%]
SOURCE: [Author Year] | [Table X / Page Y / Line Z / Equation N]
NOTES: [calibration history, why this value, what goes wrong if it drifts]

---

PARAMETER: [name]
VALUE: [exact value]
UNIT: [unit]
TOLERANCE: [exact match / ± X%]
SOURCE: [Author Year] | [Table X / Page Y / Line Z]
NOTES: [notes]

---

## ORACLE

The oracle for validating simulation or calculation outputs against this specification:

[Describe how outputs will be validated — e.g., "Compare against published table values
from [source]" or "Run calculation and compare to known analytic solution" or
"Cross-reference against benchmark dataset at [location]"]

---

## KNOWN PRIOR DRIFT RISK

For each parameter, note what the LLM prior is likely to propose based on domain
knowledge — this is the expected drift target. If unknown, write "unknown."

PARAMETER: [name]
EXPECTED DRIFT DIRECTION: [above / below / unknown]
EXPECTED DRIFT VALUE: [if known — e.g., "LLM prior likely ≈ 0.30, correct value is 0.10"]
DRIFT RISK: [HIGH / MEDIUM / LOW]

---

## MILESTONE MAP

The build loop will validate parameters in the following order:

| Milestone | Parameters Checked         | Oracle                  |
|-----------|----------------------------|-------------------------|
| M1        | [list]                     | [validation method]     |
| M2        | [list]                     | [validation method]     |
| M3        | [list]                     | [validation method]     |
| M4        | [integration / full check] | [full validation]       |

---

## STATISTICAL VALIDATION REQUIREMENTS

Sigma gate threshold (CV): < 15% (default) or [experiment-specific value]
Minimum seeds / runs: 10 for development, 30 for convergence validation
Effect persistence requirement: Any effect observed at n=k must replicate at n > k before acceptance
False positive protocol: Effects that vanish at larger n are logged as dead ends immediately
