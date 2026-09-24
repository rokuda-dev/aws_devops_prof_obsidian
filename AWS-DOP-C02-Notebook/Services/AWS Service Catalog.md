---
title: AWS Service Catalog
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# AWS Service Catalog

Governed self-service provisioning of approved infrastructure products.

## Exam mapping

Task statements: 2.1, 2.2. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Products contain provisionable versions; portfolios group products and access; constraints define launch/governance behavior; a provisioned product is a launched instance.

## Architecture pattern

Approved [[AWS CloudFormation]] template → product → portfolio/access + launch constraint → user provisioning.

## IAM and security

A launch-role constraint provides approved provisioning permissions without granting broad direct resource permissions to end users.

## Failure, rollback, and lifecycle

Update provisioned products to approved versions; maintain safe lifecycle and resource-retention choices in templates.

## When to choose

> [!exam]
> Choose when developers must self-provision only standardized, approved architectures.

## Do not confuse with and exam traps

> [!warning]
> Service Catalog vends approved definitions; [[AWS RAM]] shares existing resources; [[AWS CloudFormation StackSets]] deploys centrally across targets.

## Official AWS references

- [AWS Service Catalog official reference](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 6 — governed provisioning

Products and constraints provide approved self-service infrastructure. A template constraint validates allowed launch-time parameter combinations; it is not a universal IAM boundary or continuous drift detector. Pair catalog governance with IAM, Config and audit evidence.

Tasks 6.2–6.3. [[AWS Control Tower]], [[AWS Config]], [[Domain 6 Monitoring Auditing and Compliance]].
