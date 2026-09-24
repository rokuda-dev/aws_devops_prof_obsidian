---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# Kinesis Data Streams vs Firehose vs EventBridge

| Choice | Primary responsibility | Good cue | Not automatic |
|---|---|---|---|
| Kinesis Data Streams | Retained record stream and consumer ecosystem | Replay/custom processing/multiple consumers | S3 archive or search indexing |
| Data Firehose | Buffered managed delivery to supported destinations | Log/metric delivery into S3 | Arbitrary stream replay or every source/destination combination |
| EventBridge | Event matching/routing to targets | Service events, API-change response, lifecycle notifications | Numeric metric storage or indexed log archive |

EventBridge can have a stream/delivery service as a target, but that does not make event patterns interchangeable with CloudWatch subscription patterns. Match throughput, retry/retention, record format and downstream readiness.

Tasks 4.1–4.3. See [[Amazon Kinesis Data Streams]], [[Amazon Data Firehose]], [[Amazon EventBridge]], [[CloudWatch Log Subscriptions and Cross-Account Destinations]].
