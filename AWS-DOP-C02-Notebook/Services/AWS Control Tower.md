---
title: AWS Control Tower
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# AWS Control Tower

Set up and govern a multi-account landing zone and standardized account provisioning.

## Exam mapping

Task statements: 2.2. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Landing zones, registered OUs, enrolled accounts, controls, and Account Factory support governance. Account Factory for Terraform is a distinct automation option.

## Architecture pattern

[[AWS Organizations]] → Control Tower landing zone → Account Factory → governed account.

## IAM and security

Understand management/audit/log-archive responsibilities and IAM Identity Center integration. Controls can be preventive, detective, or proactive, with different enforcement mechanisms.

## Failure, rollback, and lifecycle

Existing accounts require enrollment prerequisites; registration/enrollment and drift remediation are not the same as merely moving an account into an OU.

## When to choose

> [!exam]
> Choose for standardized governed account creation and landing-zone operations.

## Do not confuse with and exam traps

> [!warning]
> Control Tower builds on Organizations; it does not replace SCP semantics or automatically govern every arbitrary existing account.

## Official AWS references

- [AWS Control Tower official reference](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)
- [[Official AWS Sources]] — source inventory and verification scope.

