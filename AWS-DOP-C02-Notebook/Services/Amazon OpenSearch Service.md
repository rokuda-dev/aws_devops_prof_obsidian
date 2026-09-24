---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# Amazon OpenSearch Service

## Role and exam cue

Managed search/indexing and analytics for workloads that need searchable log documents and interactive indexed analysis. Domains are managed clusters; serverless collections are a distinct deployment option.

Choose for centralized indexed logs when search requirements justify index/storage/ingestion overhead. [[Amazon Athena]] can query appropriately formatted S3 archives without maintaining a search cluster; [[CloudWatch Logs Insights and Filter Patterns]] queries logs already held in CloudWatch.

## Ingestion choices

| Input | Suitable pattern |
|---|---|
| CloudWatch Logs | Supported subscription integration, or stream + explicit processor |
| Central Kinesis stream | Lambda consumer or supported OpenSearch Ingestion pipeline |
| S3 log objects | Event-driven processor or suitable ingestion pipeline |
| DynamoDB changes | Supported change-data processing/integration; not ordinary CloudWatch metric ingestion |

Preserve account, Region, service, log group, event time and event ID. Decode batch envelopes and write individual documents. Validate schema/mappings, index naming, duplicate handling, ingestion backpressure and retries.

The transcript's general list of data sources is not a guarantee that every source works through every delivery service. In particular, direct CloudWatch Logs → Firehose → OpenSearch has a documented limitation.

## Security and lifecycle

Use authorized network access, scoped IAM/resource policies and appropriate fine-grained permissions. Configure encryption, retention/index lifecycle, backups and resilient capacity. Do not expose compliance logs publicly or store unnecessary credentials/PII.

Indexing makes data searchable; it does not itself make the archive immutable or prove completeness.

## Sources

Tasks 4.1–4.3. See [[Logs Insights vs Athena vs OpenSearch]], [[Centralized Logging Architecture]].

- [Overview — official resource](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html)
- [Kinesis and OpenSearch Ingestion](https://aws.amazon.com/blogs/big-data/use-amazon-kinesis-data-streams-to-deliver-real-time-data-to-amazon-opensearch-service-domains-with-amazon-opensearch-ingestion/)
- [Firehose CloudWatch input limitation](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-cloudwatch-logs.html)
