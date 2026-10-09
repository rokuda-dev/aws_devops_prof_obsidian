---
tags:
  - aws
  - dop-c02
  - domain-4
verified: 2026-10-07
read: false
---

# Amazon SQS

## Role

Queue decoupling between producers and consumers. Included here because the Domain 4 transcript incorrectly attributes worker-health checks to SQS.

**Correction:** SQS does not perform an ALB-style application-health check before a worker receives more messages. Consumers or event-source integrations control polling/concurrency and must handle unhealthy processing behavior.

## Monitoring and processing

Monitor visible/in-flight backlog, age of oldest messages and processing failures. Use backlog per worker/task for suitable scaling decisions; raw queue depth alone does not account for current capacity.

Visibility timeout temporarily hides a received message; successful processing must lead to deletion. Handle retry/duplicate delivery and poison messages using an appropriate dead-letter policy. Configure visibility/concurrency to match processing time and downstream capacity.

## Standard versus FIFO

| Queue type | Delivery and order | Best fit | Exam safeguard |
|---|---|---|---|
| Standard | At-least-once delivery; duplicates and occasional reordering are possible | Maximum-throughput work distribution where consumers are idempotent | Do not infer one processing attempt or strict order |
| FIFO | Ordering within a message group plus send deduplication/exactly-once queue processing semantics | Commands where related operations must remain ordered | Choose message-group IDs deliberately; consumer side effects still need idempotency and failure handling |

SQS is a competing-consumer buffer: a message is normally processed by one consumer path and deleted after success. For independent copies delivered to several consumers, use an SNS fan-out design with a separate queue per consumer when buffering and retries are required. EventBridge is the stronger first thought for content-based event routing; Kinesis Data Streams is for retained, replayable streaming records.

## Health boundaries

Load balancer target checks and Route 53 checks are distinct mechanisms. For workers, application readiness, polling, concurrency, heartbeat/processing metrics and alarms need explicit design.

Tasks 4.2–4.3. See [[AWS Fargate]], [[Scaling Metrics and Troubleshooting]], [[Safe Event-Driven Remediation]].

- [SQS/Lambda polling and visibility explanation](https://aws.amazon.com/blogs/apn/understanding-amazon-sqs-and-aws-lambda-event-source-mapping-for-efficient-message-processing/)
- [Standard queue delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.html)
- [FIFO queue behavior](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fifo-queues.html)
- [[SQS vs SNS vs EventBridge vs Kinesis]]

## Domain 5 — response boundaries

Use queues to decouple response consumers and buffer work. Configure visibility/retry/dead-letter handling and idempotency; queue receipt does not prove incident resolution.

Tasks 5.1–5.3 where applicable. [[Domain 5 Scenario Decisions]], [[Safe Event-Driven Remediation]], [[Domain 5 Official Sources]].
