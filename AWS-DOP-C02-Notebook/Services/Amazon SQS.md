---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# Amazon SQS

## Role

Queue decoupling between producers and consumers. Included here because the Domain 4 transcript incorrectly attributes worker-health checks to SQS.

**Correction:** SQS does not perform an ALB-style application-health check before a worker receives more messages. Consumers or event-source integrations control polling/concurrency and must handle unhealthy processing behavior.

## Monitoring and processing

Monitor visible/in-flight backlog, age of oldest messages and processing failures. Use backlog per worker/task for suitable scaling decisions; raw queue depth alone does not account for current capacity.

Visibility timeout temporarily hides a received message; successful processing must lead to deletion. Handle retry/duplicate delivery and poison messages using an appropriate dead-letter policy. Configure visibility/concurrency to match processing time and downstream capacity.

## Health boundaries

Load balancer target checks and Route 53 checks are distinct mechanisms. For workers, application readiness, polling, concurrency, heartbeat/processing metrics and alarms need explicit design.

Tasks 4.2–4.3. See [[AWS Fargate]], [[Scaling Metrics and Troubleshooting]], [[Safe Event-Driven Remediation]].

- [SQS/Lambda polling and visibility explanation](https://aws.amazon.com/blogs/apn/understanding-amazon-sqs-and-aws-lambda-event-source-mapping-for-efficient-message-processing/)

## Domain 5 — response boundaries

Use queues to decouple response consumers and buffer work. Configure visibility/retry/dead-letter handling and idempotency; queue receipt does not prove incident resolution.

Tasks 5.1–5.3 where applicable. [[Domain 5 Scenario Decisions]], [[Safe Event-Driven Remediation]], [[Domain 5 Official Sources]].
