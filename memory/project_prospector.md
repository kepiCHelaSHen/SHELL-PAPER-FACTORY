---
name: Prospector in-memory exploration
description: User has a Prospector project that loads data in memory without DB abstraction. 50GB capacity on this box. Key advantage over SQL for discovery.
type: project
originSessionId: ae1dbf40-8281-45da-943b-24a3a18f16da
---
Prospector loads data into pandas DataFrames in memory for frictionless exploration. The box can comfortably hold 50GB, which means 100M+ rows with categorical optimization.

**Why:** The volume-tier finding (pain specialists prescribe MORE opioids at higher volume, surgeons do opposite) was discovered because the data was in memory and the analysis was a 3-line groupby. Nobody would have written that SQL query. Database = answering known questions. In-memory = discovering unknown patterns.

**How to apply:** The architecture is Prospector discovers → ASSAY formalizes → SHELL publishes. When the user asks about data analysis approaches, favor in-memory exploration over database queries for exploratory/discovery work. Reserve databases for storage, retrieval, and standardized repeating queries.
