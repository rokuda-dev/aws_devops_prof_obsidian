---
title: Amazon EventBridge
tags: [aws, dop-c02, service]
status: consolidated-study-note
updated: 2026-09-18
read: false
---

# Amazon EventBridge

Route events to targets; Scheduler provides scheduled invocations.

## Exam mapping

Task statements: 2.3; cross-domain 5. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Event buses receive AWS/custom/partner events; rules match patterns; targets invoke actions. Pipes connect supported sources to targets with optional filtering/enrichment. Scheduler is separate from event-pattern routing.

## Architecture pattern

Config compliance/security/service event → matching rule → [[AWS Step Functions]]/[[AWS Lambda]]/SSM Automation.

## IAM and security

Use target execution roles and resource policies where required; cross-account bus permissions and target authorization are distinct.

## Failure, rollback, and lifecycle

Configure supported retries and dead-letter queues. Duplicate events are possible; targets should be idempotent. A routed event is not a completed remediation workflow.

## When to choose

> [!exam]
> Choose for reactive routing or scheduling; use Step Functions for stateful multi-step logic.

## Do not confuse with and exam traps

> [!warning]
> Do not confuse an event bus with a queue or a state machine.

## Official AWS references

- [Amazon EventBridge official reference](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 3 — scaling events

ASG lifecycle events can route to initialization/recovery handlers. Warm-pool event detail fields include case-sensitive Origin and Destination; filter the appropriate path and ASG identity.

Delivery and handler execution do not automatically complete a lifecycle hook. Build retry/idempotency, heartbeat/completion and failure handling. See [[Amazon EC2 Auto Scaling]] for a specific warm-pool event pattern.

Task 3.2.
- [Warm-pool events](https://docs.aws.amazon.com/autoscaling/ec2/userguide/warm-pools-eventbridge-events.html)

## Domain 4 — match the actual event

| Requirement | Trigger |
|---|---|
| AWS maintenance | AWS Health service event |
| Relevant API change | AWS API Call via CloudTrail with appropriate audit capture |
| Noncompliance | Config compliance change after evaluation |
| ASG membership-dependent updates | Lifecycle/state events plus live-state reconciliation |
| Security response | Relevant GuardDuty/Macie finding |
| Deployment notification | CodeDeploy instance/deployment state change |

CloudWatch Events is older naming, not numeric metric storage. Test source/detail/account/Region fields, target permissions, retry/failure handling and loop prevention.

PutEvents trace context is internal metadata; do not assume the header is a replayable payload field.

Tasks 4.1–4.3. See [[Log Subscription vs Metric Filter vs EventBridge Rule]], [[Safe Event-Driven Remediation]], [[AWS Health]].
- [API matching](https://repost.aws/knowledge-center/eventbridge-rule-monitors-s3)
- [Tracing](https://aws.amazon.com/blogs/compute/using-aws-x-ray-tracing-with-amazon-eventbridge/)

## Domain 5 — incident processing contract

Choose the exact event source/schema and scope account/Region/resource. Match Config compliance, Trusted Advisor refreshes, Health impacts, CloudTrail captured calls and native service transitions separately.

Supported rule destinations include Lambda, SNS/SQS, Kinesis, Step Functions and relevant SSM targets. A CloudWatch log group is a destination; an arbitrary alarm ARN is not a generic target. Built-in actions and alarm-produced events are different concepts.

Target invocation does not prove repair. Recheck live state, handle duplicates, monitor workflow failures in addition to delivery failures, and prevent loops.

Tasks 5.1–5.2. [[Event Sources and Response Contracts]], [[Domain 5 Architecture Patterns]].
- [Current rule targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html)
