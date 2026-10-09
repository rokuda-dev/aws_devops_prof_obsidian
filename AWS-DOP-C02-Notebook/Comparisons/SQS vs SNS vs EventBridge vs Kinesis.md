---
title: SQS vs SNS vs EventBridge vs Kinesis
tags:
  - aws
  - dop-c02
  - comparisons
  - messaging
verified: 2026-10-07
read: false
---

# SQS vs SNS vs EventBridge vs Kinesis

## Fast decision

| Requirement | Best first thought | Decisive boundary |
|---|---|---|
| Buffer work for competing consumers | [[Amazon SQS]] Standard | At-least-once delivery; duplicates and occasional reordering are possible |
| Preserve order for related commands | [[Amazon SQS]] FIFO | Ordering is within a message group; deduplication does not remove the need for idempotent side effects |
| Push one publication to several subscribers | [[Amazon SNS]] | Fan-out/pub-sub; add one SQS queue per consumer when each needs durable buffering |
| Route AWS, custom, or partner events by content | [[Amazon EventBridge]] | Event pattern and target routing; not a competing-consumer work queue |
| Retain a high-volume record stream for replay and independent readers | [[Amazon Kinesis Data Streams]] | Records persist for the retention window; ordering is per shard/partition-key path, not global |

## Delivery and consumption model

| Service | Consumer model | Order | Replay/history | Filtering |
|---|---|---|---|---|
| SQS Standard | Competing pollers; successful work deletes the message | Best effort | No normal replay after deletion; DLQ redrive is failure recovery | Producers choose the queue; consumers receive queued messages |
| SQS FIFO | Competing pollers with ordered message groups | Strict within a group | No normal replay after deletion | Producers choose the queue and group |
| SNS | Push copy to every matching subscription | Topic/type dependent; do not assume Standard ordering | No retained stream replay | Subscription filter policies |
| EventBridge | Rules route matching events to targets | Do not assume global ordering | Archive/replay only when that capability is configured | Rich event-pattern matching and optional transformation |
| Kinesis Data Streams | Independent applications read positions in a retained stream | Per shard; partition key determines placement | Native within configured retention | Consumers process the stream; routing is application logic |

## Composition patterns

```text
Publisher -> SNS topic -> SQS queue per consumer -> independent retry/backpressure

AWS/custom event -> EventBridge rule -> Step Functions/Lambda/SSM target

High-volume records -> Kinesis Data Streams -> several independent consumers
```

An accepted publish, enqueue, or target invocation is not proof that the business operation completed. Configure the applicable permissions, retries, dead-letter handling, monitoring, idempotency, and outcome verification.

## Exam traps

- Standard SQS is not exactly once and not strictly ordered.
- FIFO ordering is not global across all message groups.
- SNS fan-out does not provide queue-style buffering to an email, HTTP, or Lambda subscriber; SNS-to-SQS adds that buffer.
- EventBridge is not numeric metric storage, a log-query engine, or a workflow state machine.
- Kinesis retention/replay does not make every downstream side effect exactly once.

Tasks 4.3 and 5.1. See [[Event Sources and Response Contracts]], [[Kinesis Data Streams vs Firehose vs EventBridge]], and [[Safe Event-Driven Remediation]].

## Official AWS references

- [SQS Standard queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.html)
- [SQS FIFO queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fifo-queues.html)
- [SNS fan-out and subscriber model](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)
- [EventBridge concepts](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
- [Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)

