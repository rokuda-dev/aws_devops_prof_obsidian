---
title: Amazon Inspector
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# Amazon Inspector

Vulnerability management for supported workloads such as EC2, ECR images, and Lambda.

## Exam mapping

Task statements: 2.2; cross-domain 6. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Supported scan modes/integrations assess packages and other enabled vulnerability categories. EC2 scan requirements differ between agent-based/agentless options; ECR enhanced scanning integrates Inspector.

## Architecture pattern

Supported workload/image/function → scan → finding → prioritize → patch/rebuild/redeploy.

## IAM and security

Use delegated administration and scoped finding access. Understand required Systems Manager integration for applicable EC2 scan modes.

## Failure, rollback, and lifecycle

Findings identify remediation work; they do not patch workloads automatically. Rebuild images and redeploy after dependency fixes.

## When to choose

> [!exam]
> Choose for package/CVE exposure and supported vulnerability assessment.

## Do not confuse with and exam traps

> [!warning]
> Do not install or memorize the legacy standalone Inspector Agent model. [[Amazon GuardDuty]] detects threats, not merely vulnerable package versions.

## Official AWS references

- [Amazon Inspector official reference](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 4 — legacy blueprint terminology

Current Inspector is a supported continuous vulnerability/exposure service, not GuardDuty threat detection.

Assessment-template wording in the exam guide is legacy Classic terminology. **Inspector Classic ended support May 20, 2026**; do not use its assessment-template/agent recipe as a current deployment instruction.

Task 4.2. See [[Domain 4 Transcript Corrections]].
- [Classic retirement and current-service distinction](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html)

## Domain 6 — vulnerability evidence

Modern Inspector continuously scans supported EC2, ECR, Lambda and related coverage according to enabled scan types. Findings do not approve an AMI or patch a workload. Combine approved-image controls with vulnerability findings and controlled rebuild/redeployment.

Task 6.3. [[Domain 6 Monitoring Auditing and Compliance]], [[Inspector vs GuardDuty vs Macie vs Access Analyzer]].
