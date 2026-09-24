---
title: AWS Security Hub
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# AWS Security Hub

Centralize security findings and posture workflows across supported services/accounts/Regions.

## Exam mapping

Task statements: 2.2; cross-domain 6. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Security findings and CSPM checks integrate with supported services and organization administration. Current product naming distinguishes Security Hub and Security Hub CSPM capabilities; read current feature documentation.

## Architecture pattern

[[Amazon GuardDuty]]/[[Amazon Inspector]]/posture findings → central view → prioritized investigation and response.

## IAM and security

Configure delegated administration, organization coverage, and Region aggregation appropriately; access to findings is not authority to remediate every resource.

## Failure, rollback, and lifecycle

Aggregation is visibility/workflow, not automatic correction. Standards checks, integrations, and remediation require their own setup.

## When to choose

> [!exam]
> Choose for centralized security findings/posture, not a replacement for each detector.

## Do not confuse with and exam traps

> [!warning]
> [[AWS Config]] aggregator centralizes Config data; Security Hub centralizes security workflows. [[Amazon Detective]] specializes in investigation.

## Official AWS references

- [AWS Security Hub and Security Hub CSPM official distinction](https://docs.aws.amazon.com/securityhub/latest/userguide/what-are-securityhub-services.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 3 — security findings across Regions

Configure supported cross-Region aggregation and participating Regions/accounts explicitly. Do not assume every regional finding is aggregated without setup.

Central findings support posture/investigation; they do not provide application data replication or health-based failover. Task 3.2. See [[Multi-Region Application Checklist]].

## Domain 4 — findings distinctions

GuardDuty threats, Macie sensitive-data/S3 risks and Inspector vulnerabilities remain distinct detector outputs. Central visibility does not make one service perform another's analysis. Validate/authorize response separately.

Task 4.2. See [[Amazon GuardDuty]], [[Amazon Macie]], [[Amazon Inspector]], [[Safe Event-Driven Remediation]].

## Domain 6 — centralized findings

Security Hub CSPM sends findings and state changes to EventBridge. Custom actions represent explicitly selected findings/insights; they are not the same as routing every finding. Centralization does not authorize remediation—validate scope and use a dedicated least-privilege response role.

Task 6.2. [[Domain 6 Architecture Patterns]], [[Inspector vs GuardDuty vs Macie vs Access Analyzer]].
