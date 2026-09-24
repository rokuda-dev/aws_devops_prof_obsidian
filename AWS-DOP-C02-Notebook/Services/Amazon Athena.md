---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# Amazon Athena

## Role

Serverless SQL analysis of supported data sources, commonly logs stored in S3. Suitable for audit investigation and historical analysis without provisioning a search cluster.

## S3 log-analysis pattern

Deliver CloudTrail/ALB/application logs to an authorized S3 location. Define the correct table schema/format and catalog metadata, scope time/account/Region partitions, and query the required events. Store query results in a protected location.

Partition pruning and columnar/compressed formats can reduce scanned data. Avoid assuming every gzip subscription batch or raw object is immediately a correctly modeled SQL table; parse/transform as needed.

## Dashboard use

[[Amazon QuickSight]] can visualize an Athena-backed dataset. Refresh/ingestion mode, query latency and upstream delivery determine freshness; a dashboard is not automatically real-time simply because its source is S3.

Athena is not an ingestion service or a CloudWatch alarm. Pair with delivery, retention, catalogs, encryption and access controls.

## Exam cues and sources

Tasks 4.1–4.2. Historical audit logs in S3 + SQL analysis → Athena; low-latency indexed text search → consider OpenSearch.

See [[Logs Insights vs Athena vs OpenSearch]], [[Log Lifecycle Security and Integrity]], [[Domain 4 Official Sources]].

- [S3 log analysis/schema and partition projection](https://aws.amazon.com/blogs/storage/amazon-s3-audit-logging-part-1-analyzing-server-access-logs-with-amazon-athena-for-performance-insights/)
