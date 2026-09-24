---
title: AWS Lambda
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# AWS Lambda

Managed event-driven function execution; published versions and aliases enable controlled releases.

## Exam mapping

Task statements: 1.4, 2.3; cross-domain response. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Published versions are immutable snapshots. An alias targets a version and may weight traffic to a second version. Event-source mappings poll streams/queues; invocation and retry behavior depend on the source.

## Architecture pattern

Publish version → [[AWS CodeDeploy]] shifts alias → validation hooks + [[Amazon CloudWatch]] alarms → complete or rollback.

## IAM and security

Function execution role governs application API access; resource-based policies govern supported invocations. Avoid static credentials in code.

## Failure, rollback, and lifecycle

CodeDeploy rollback moves alias traffic back; it does not undo database or external side effects. Stream consumers must handle duplicates and poison records.

## When to choose

> [!exam]
> Choose for custom event-driven automation; use [[AWS Step Functions]] when multiple steps, waits, or explicit workflow state are needed.

## Do not confuse with and exam traps

> [!warning]
> $LATEST is mutable, not an immutable release. [[Amazon API Gateway]] canary settings operate at a different layer from alias weights.

## Official AWS references

- [AWS Lambda official reference](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 3 — serverless scaling and recovery automation

Reserved concurrency limits/reserves function concurrency; provisioned concurrency keeps execution environments initialized and has cost even while unused. Neither eliminates downstream capacity/connection limits.

Treat recovery handlers as idempotent workflows with bounded retries, safe permissions, independent failure confirmation and explicit data readiness. A single RDS notification should not immediately trigger destructive writer changes.

Separate Lambda alias canaries from API Gateway canary deployments and regional disaster recovery. See [[Amazon SNS]], [[AWS Step Functions]], [[Amazon Application Recovery Controller]], [[AWS Fargate]].

Tasks 3.1–3.3. See [[Domain 3 Transcript Corrections]].

## Domain 4 — processors and response handlers

Log subscription processors handle compressed batches/control messages; stream consumers and event-bus targets have different payload/retry behavior. Preserve source/event identity and index individual documents correctly.

Scope roles, use idempotent actions and monitor backlog/failure. Prefer direct native delivery/SSM/SNS targets where custom code is unnecessary.

Tasks 4.1–4.3. See [[CloudWatch Log Subscriptions and Cross-Account Destinations]], [[Safe Event-Driven Remediation]], [[AWS X-Ray]].

## Domain 5 — response handlers and deployment tests

Event handlers must validate affected resource identity, limit permissions, handle duplicate delivery and record sanitized outcomes. Multi-step incident orchestration may belong in Step Functions or SSM Automation.

For CodeDeploy Lambda releases, validate the target published version using platform-specific hooks and report callback status. Candidate-version tests, alarm-stop behavior and post-traffic validation are separate controls.

Tasks 5.1–5.3. [[Exposed Credential Response]], [[Lambda Deployment Validation Hooks]], [[Safe Event-Driven Remediation]].
