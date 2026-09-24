---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# Amazon Data Firehose

## Name and role

Amazon Data Firehose, formerly Amazon Kinesis Data Firehose, buffers and delivers streaming data to configured supported destinations. Good cue: managed delivery of logs/metrics into S3 with optional supported transformation/format handling, rather than building every consumer.

## Domain 4 log and metric paths

| Input | Delivery pattern | Important boundary |
|---|---|---|
| CloudWatch Logs subscription | Firehose → S3 archive/analytics | Compressed log-envelope handling and optional decompression/message extraction |
| Cross-account CloudWatch Logs | Logical destination backed by Firehose | Destination policy, roles and correct Region topology |
| CloudWatch metric stream | Firehose → supported destination, such as S3 | Metric stream's Firehose must be same account and Region |
| Application streaming records | Firehose → supported destination | Record format must match destination requirements |

Delivery latency includes buffering, transformation, retries, and destination behavior; near-real-time is not instantaneous.

## OpenSearch caveat

Firehose supports OpenSearch for suitable records, but current documentation says **CloudWatch Logs delivery to the Firehose OpenSearch destination is not supported**: CloudWatch combines multiple events into one record, while OpenSearch expects individual documents.

Do not infer that the S3 decompression option makes this direct path supported. Use CloudWatch's OpenSearch subscription integration or a suitable Kinesis → Lambda/OpenSearch Ingestion processing path.

## Operations and security

Scope delivery-role access to the destination, encryption keys and configured error/backup locations. Monitor failed delivery, transformation errors, freshness/lag and backup/error records. S3 retention/lifecycle and query permissions are separate from delivery configuration.

## Sources

Tasks 4.1–4.3. See [[CloudWatch Metric Streams]], [[CloudWatch Log Subscriptions and Cross-Account Destinations]].

- [CloudWatch Logs input and OpenSearch limitation](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-cloudwatch-logs.html)
- [Cross-account account-level Firehose subscriptions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CrossAccountSubscriptions-Firehose-Account.html)
- [Decompression/message extraction](https://aws.amazon.com/about-aws/whats-new/2024/02/amazon-data-firehose-message-extraction-cloudwatch-logs/)
