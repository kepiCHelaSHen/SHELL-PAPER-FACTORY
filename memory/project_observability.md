---
name: Pipeline observability is a priority
description: User needs real-time visibility into pipeline runs. File-based logs are insufficient. Database + dashboard is a product requirement, not a nice-to-have.
type: project
originSessionId: 9cd9e77b-612c-46c7-bcba-7290994a5092
---
The user cannot see what the pipeline is doing during runs. CLI shows nothing, logs are in scattered markdown files. This is unacceptable for a product.

**Why:** Running blind makes debugging impossible and erodes trust. The user needs to see agent dispatches, verdicts, token usage, and progress in real-time.

**How to apply:** When building the web interface and database tier, treat observability as a core feature, not an afterthought. The dashboard should show:
- Real-time pipeline state (which milestone, which agent, which run)
- Agent dispatch history with verdicts
- Token usage per step and per paper
- Steelman findings and dead-ends queryable
- Paper output preview
