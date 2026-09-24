---
title: AWS Step Functions
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# AWS Step Functions

Stateful orchestration of multi-step workflows with branching, retries, waits, and service integrations.

## Exam mapping

Task statements: 2.3; cross-domain 5. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

States model tasks, choices, parallel work, waits, retries, and catches. Standard and Express workflows differ in duration, execution guarantees, and integration support.

## Architecture pattern

[[Amazon EventBridge]] → state machine → AWS SDK integration/[[AWS Lambda]]/approval → handle errors and compensation.

## IAM and security

Execution roles authorize service integrations; scope PassRole and invoked-resource permissions. Protect execution history from sensitive payloads.

## Failure, rollback, and lifecycle

Retries can repeat side effects: build idempotent tasks. Catch paths provide recovery/compensation; automatic workflow rollback of arbitrary external changes does not exist.

## When to choose

> [!exam]
> Choose when explicit workflow state, long waits, callbacks, or coordinated error handling are needed.

## Do not confuse with and exam traps

> [!warning]
> EventBridge routes events; Lambda runs custom code; [[AWS Systems Manager]] Automation is an operational runbook alternative.

## Official AWS references

- [AWS Step Functions official reference](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 3 — recovery orchestration gates

Coordinate detection confirmation, approval/fencing, data promotion/restore, capacity changes, validation and traffic shift. Retry only actions that are safe/idempotent; fail clearly rather than allowing writes against an unready replica.

Compare with Systems Manager operational runbooks and current ARC Region switch supported recovery blocks. A state machine does not itself replicate data.

Task 3.3. See [[Disaster Recovery Strategies]], [[Amazon Application Recovery Controller]], [[Domain 3 Architecture Patterns]].

## Domain 4 — bounded response workflows

Coordinate validation, evidence preservation, approval, repair and verification where multiple steps are required. Use timeouts, safe retries and explicit failure notification.

Task 4.3. See [[Safe Event-Driven Remediation]], [[Domain 4 Architecture Patterns]].

## Domain 5 — operational orchestration

Health/EventBridge can start a state machine for exposed-key containment, audit review and sanitized notification. Scope exact keys/identities, give containment failures an escalation path, and make effects duplicate-safe.

Config custom rules do not use a state machine as their direct evaluator. Config-related response can still use EventBridge → Step Functions or SSM Automation's aws:executeStateMachine action; do not infer an absolute integration prohibition.

Tasks 5.1–5.2. [[Exposed Credential Response]], [[Config Compliance vs CloudTrail Actor Attribution]], [[Safe Event-Driven Remediation]].
- [SSM state-machine action](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-executeStateMachine.html)
