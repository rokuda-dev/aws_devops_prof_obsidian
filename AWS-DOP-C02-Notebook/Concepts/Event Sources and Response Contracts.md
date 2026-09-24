---
title: Event Sources and Response Contracts
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# Event Sources and Response Contracts

## Choose the signal that answers the question

| Question | Event or signal |
|---|---|
| Which actor changed/accessed an S3 object? | CloudTrail with relevant S3 data-event selectors |
| Is an AWS resource configuration compliant? | Config evaluation/compliance change |
| Has a numeric workload threshold been breached? | CloudWatch alarm state change |
| Is AWS maintenance affecting this resource? | AWS Health event |
| Has ASG membership transitioned? | Relevant Auto Scaling lifecycle/state event |
| Did an object get created/deleted? | Relevant native S3 event; not a full authorization audit |
| Did an RDS operational event occur? | RDS event notification; supplement with metrics/app health |
| Did a recommendation change? | Trusted Advisor check refresh/status signal |

## Processing contract

Match exact source/detail fields, account, Region, and resource. Design for duplicate, delayed, or out-of-order events and source-specific delivery guarantees. Re-read current state before acting.

Separate routing success, accepted asynchronous invocation, handler success, and verified recovery. Configure applicable retries, dead-letter queues, monitoring, and manual escalation. Preserve correlation IDs and suppress self-triggered remediation loops.

## Target selection

Rules can route to Lambda, SNS/SQS, Kinesis, Step Functions, SSM Automation/Run Command/OpsItems, and supported other targets. A CloudWatch **log group** is a target; an arbitrary alarm ARN is not a generic rule target. “CloudWatch alarm actions” in older wording can mean built-in actions shared with alarms, not a call to evaluate an alarm.

Tasks 5.1–5.2. [[Amazon EventBridge]], [[Detection vs Enforcement vs Remediation]], [[Domain 5 Official Sources]].
