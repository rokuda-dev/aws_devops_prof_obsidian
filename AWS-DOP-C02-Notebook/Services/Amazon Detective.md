---
title: Amazon Detective
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# Amazon Detective

Investigate security findings and relationships to help determine root cause.

## Exam mapping

Task statements: 2.2; cross-domain 5–6. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Behavior graphs correlate supported security/activity data for investigation. Use findings with related entities, activity, and relationships.

## Architecture pattern

[[Amazon GuardDuty]] finding → Detective investigation → evidence → scoped response.

## IAM and security

Control graph membership and investigation access; use organization administration where supported.

## Failure, rollback, and lifecycle

An investigation service does not automatically contain a threat or patch a vulnerable package.

## When to choose

> [!exam]
> Choose for root-cause investigation and contextual analysis of suspicious activity.

## Do not confuse with and exam traps

> [!warning]
> GuardDuty detects threats; Inspector finds vulnerabilities; Security Hub centralizes findings/workflows.

## Official AWS references

- [Amazon Detective official reference](https://aws.amazon.com/detective/faqs/)
- [[Official AWS Sources]] — source inventory and verification scope.

