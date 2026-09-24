---
title: Amazon GuardDuty
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# Amazon GuardDuty

Managed threat detection for suspicious activity and potential compromise.

## Exam mapping

Task statements: 2.2; cross-domain 5–6. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Supported foundational data sources and optional protection plans produce security findings. Organization integration supports delegated administration and enrollment.

## Architecture pattern

Finding → [[Amazon EventBridge]]/[[AWS Security Hub]] → investigate/approve → remediation.

## IAM and security

Use delegated administrator patterns, finding access controls, and scoped response roles. GuardDuty does not require you to create ordinary CloudTrail/VPC Flow Log destinations just to analyze foundational sources.

## Failure, rollback, and lifecycle

GuardDuty detects and reports; automated containment must be separately configured and carefully scoped.

## When to choose

> [!exam]
> Choose for anomalous behavior, suspicious credentials, and threat detection.

## Do not confuse with and exam traps

> [!warning]
> [[Amazon Inspector]] finds vulnerabilities; [[Amazon Detective]] helps investigation; GuardDuty is not a patching service.

## Official AWS references

- [Amazon GuardDuty official reference](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 4 — organization detection and export

Configure required accounts/Regions, delegated administration, existing/future enrollment and protection plans. Central log storage does not enroll detectors or automatically enable all malware/runtime protections.

Use findings for scoped investigation/response. Native S3 findings export is supported with bucket/KMS permissions; EventBridge → Firehose is not always necessary merely to retain findings. Numeric CloudWatch anomalies are not equivalent threat detection.

Task 4.2. See [[Amazon Macie]], [[Safe Event-Driven Remediation]].
- [Native S3 export](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_exportfindings.html)

## Domain 6 — threat-detection boundary

GuardDuty detects suspicious activity using supported data sources and protection plans. It does not enforce least privilege, classify S3 object contents, or patch vulnerabilities. Configure organization/Region coverage and route findings to evidence-preserving, scoped response.

Task 6.3. [[Domain 6 Monitoring Auditing and Compliance]], [[Inspector vs GuardDuty vs Macie vs Access Analyzer]].
