---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# Logs Insights vs Athena vs OpenSearch

| Choice | Data location/model | Best cue | Main preparation |
|---|---|---|---|
| CloudWatch Logs Insights | Log groups already in CloudWatch | Interactive operational log analysis | Select groups/time window; discovered fields/parse |
| Athena | Supported sources, commonly S3 log archive | SQL historical audit/data-lake analysis | Correct schema/catalog/partitions and query-result permissions |
| OpenSearch | Indexed documents | Low-latency indexed search and analytics | Ingestion, mappings, index lifecycle, cluster/collection security |

No option automatically collects all accounts' logs. Select collection/storage first, then search. Retention, encryption, access, freshness and cost depend on the full pipeline; “OpenSearch always costs more” is not a universal rule.

Tasks 4.1–4.2. See [[CloudWatch Logs Insights and Filter Patterns]], [[Amazon Athena]], [[Amazon OpenSearch Service]], [[Centralized Logging Architecture]].
