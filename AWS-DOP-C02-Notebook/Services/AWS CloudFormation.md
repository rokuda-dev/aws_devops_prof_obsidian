---
title: AWS CloudFormation
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# AWS CloudFormation

Declarative provisioning and lifecycle management of AWS infrastructure.

## Exam mapping

Task statements: 1.4, 2.1. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Templates define stacks; parameters customize deployments; outputs expose values. Nested stacks reuse templates; change sets preview creates, updates, and replacements. Drift detection covers supported resources and properties, not every possible out-of-band change.

## Architecture pattern

Source-controlled template → [[AWS CodePipeline]] creates change set → review/approval → execute → monitor stack events.

## IAM and security

Separate pipeline/action roles from the CloudFormation execution role; scope iam:PassRole. A stack policy restricts updates through CloudFormation, not direct API changes.

## Failure, rollback, and lifecycle

Creation/update failures normally trigger rollback, subject to configured options. DeletionPolicy controls stack deletion/removal; UpdateReplacePolicy controls the old resource after replacement. Retain/Snapshot do not prevent every replacement.

## When to choose

> [!exam]
> Choose for repeatable, versioned infrastructure and dependency-aware updates.

## Do not confuse with and exam traps

> [!warning]
> A change set predicts operations, not successful execution. Parameter changes alone do not refresh running fleets.

## Official AWS references

- [AWS CloudFormation official reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 3 — repeatable recovery infrastructure

Deploy a compatible regional application stack from templates, with explicit regional images, keys, secrets, networking and data endpoints. Desired ASG capacity must fit quotas and tested recovery timing.

Updating RDS EngineVersion is an infrastructure operation, not a guarantee of short downtime. Review [[Amazon RDS]] engine/topology upgrade behavior and [[RDS Blue Green vs EngineVersion Update vs Read Replica Promotion]].

Use supported stack drift detection, but it does not inspect every runtime setting or prove data freshness/recovery. Tasks 3.1 and 3.3. See [[Disaster Recovery Testing and Failback]].

## Domain 5 — failed deployments and repair

Start with stack events and the failing logical resource/status reason; correlate recent changes, IAM, quotas/capacity and downstream dependencies. An automated retry or rollback can fail for the same underlying condition.

Document whether a proposed response changes, replaces or deletes resources, and preserve persistent data. Supported drift checks evaluate infrastructure state, not the entire application incident.

Task 5.3. [[CI-CD Failure Triage and Parallel Actions]], [[Incident Response Workflow and Evidence Preservation]].

## Domain 6 — security and drift

Use templates to encode reviewed security controls and drift detection to compare supported stack resources with expected configuration. Drift is not a vulnerability scan or complete application audit. Protect deployment roles, review change sets, and avoid plaintext secrets in templates/parameters.

Tasks 6.2–6.3. [[Domain 6 Monitoring Auditing and Compliance]], [[AWS Config]], [[AWS Service Catalog]].
