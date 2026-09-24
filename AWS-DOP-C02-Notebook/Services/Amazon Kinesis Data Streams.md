---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# Amazon Kinesis Data Streams

## Role and exam cue

Durable streaming ingestion with multiple independently consuming applications and configurable retention/replay. Use for high-volume centralized log processing when consumers need custom processing and recovery from consumer lag. This is not EventBridge event routing or automatic S3 delivery.

## Centralized-log pattern

Source CloudWatch Logs groups → cross-account logical destination → central stream → Lambda consumer → OpenSearch indexing. A separate delivery/consumer path can archive to S3. See [[Centralized Logging Architecture]].

CloudWatch subscription records contain compressed log batches. Decode the appropriate transport envelope, decompress gzip, distinguish data/control messages, and index individual log events with source identity preserved. Use event IDs/idempotency to manage duplicate processing.

## Capacity and failure

Choose appropriate stream capacity mode and partition distribution; monitor ingress throttling, consumer lag, errors, and retention headroom. CloudWatch forwarding retries are bounded, so a durable stream does not guarantee logs will arrive if upstream forwarding remains broken.

A stream consumer needs its own permissions, failure handling, checkpoint/retry design and downstream capacity. A blocked OpenSearch writer can fall behind and eventually lose replay access when retention expires.

## Cross-account security

The receiver defines a CloudWatch Logs logical destination and access policy. The sender needs authorization to create its subscription. The delivery role must authorize the actual stream action. Verify organization/account scope, Region pairing, KMS access and confused-deputy controls.

Kinesis Data Streams is no longer the only documented cross-account subscription destination; [[Amazon Data Firehose]] is another supported path.

## Sources and task mapping

Tasks 4.1–4.3. Compare [[Kinesis Data Streams vs Firehose vs EventBridge]].

- [Cross-account streaming setup](https://repost.aws/knowledge-center/streaming-cloudwatch-logs)
- [Kinesis-backed centralized OpenSearch ingestion](https://aws.amazon.com/blogs/big-data/use-amazon-kinesis-data-streams-to-deliver-real-time-data-to-amazon-opensearch-service-domains-with-amazon-opensearch-ingestion/)

## Domain 5 — response boundaries

Use retained streams for appropriate event/log analysis and custom consumers; it is not a substitute for policy enforcement or a stateful remediation workflow.

Tasks 5.1–5.3 where applicable. [[Domain 5 Scenario Decisions]], [[Safe Event-Driven Remediation]], [[Domain 5 Official Sources]].
