---
title: AWS CloudFormation StackSets
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# AWS CloudFormation StackSets

Deploy a common stack definition across multiple accounts and Regions.

## Exam mapping

Task statements: 2.1, 2.2. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

A StackSet contains the template; stack instances represent account/Region targets. Self-managed permissions use administrator/execution roles; service-managed permissions integrate with Organizations.

## Architecture pattern

[[AWS Organizations]] OU → service-managed StackSet → auto-deploy to eligible new accounts → track stack instances.

## IAM and security

Service-managed deployment requires trusted access; use delegated administration appropriately. Self-managed execution-role trust must match the administrator account.

## Failure, rollback, and lifecycle

Set concurrency, failure tolerance, and Region order. Partial failure can leave some targets updated and others unchanged; inspect operations and remediate.

## When to choose

> [!exam]
> Choose for centrally deploying common infrastructure and baseline resources across accounts/Regions.

## Do not confuse with and exam traps

> [!warning]
> StackSets create resources in targets; [[AWS RAM]] shares an existing resource. It is not a distributed atomic transaction.

## Official AWS references

- [AWS CloudFormation StackSets official reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)
- [[Official AWS Sources]] — source inventory and verification scope.

