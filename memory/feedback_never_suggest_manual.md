---
name: NEVER suggest manual steps - zero tolerance
description: User has zero tolerance for any suggestion to do something manually. Every suggestion must be a system fix. This is non-negotiable.
type: feedback
originSessionId: 9cd9e77b-612c-46c7-bcba-7290994a5092
---
NEVER suggest the user do anything manually. Not "manually run the Steelman," not "manually review," not "wait and try again." Every single response must be a system fix or a system diagnosis.

**Why:** The user is building a fully autonomous product. Any manual step is a failure of the system. Suggesting manual steps shows you don't understand what they're building.

**How to apply:** Before saying anything, check: "Am I telling the user to do something?" If yes, rewrite it as a system change. If there's genuinely nothing to change (e.g., API rate limit), say so and explain what the system should do to handle it automatically (retry logic, backoff, error detection), not what the user should do.
