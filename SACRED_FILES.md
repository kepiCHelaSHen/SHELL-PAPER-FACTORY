# SACRED FILES
# Files that must never be modified after the lock date.
# The Critic checks this list at the start of every turn.
# If a sacred file is touched, the experiment is invalidated.

Lock date: [DATE]

## Sacred Files

| File | Reason | Locked |
|------|--------|--------|
| spec/frozen_spec.md | The oracle. Modifying it changes what we are validating. | [DATE] |
| [file] | [reason] | [DATE] |

## Rule

If you are unsure whether a file is safe to touch — do not touch it.
If a sacred file must change, halt the loop, document why, create a new
versioned spec, and restart from Turn 0. Log the restart in DEV_LOG.md.
