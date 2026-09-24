---
title: AWS Organizations
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# AWS Organizations

Manage AWS accounts, OUs, and organization-wide governance boundaries.

## Exam mapping

Task statements: 2.2; cross-domain 6. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

A hierarchy contains root, OUs, and accounts. SCPs cap permissions for affected member-account principals; applicable policies inherit down the hierarchy. Delegated administration separates service management from the management account.

## Architecture pattern

OU governance → SCP boundary + scoped account roles → organization-integrated services.

## IAM and security

SCPs grant nothing, do not restrict management-account principals, and do not restrict service-linked roles. Identity/resource policy evaluation still matters.

## Failure, rollback, and lifecycle

A poorly scoped deny can block operations across member accounts. Test governance changes in a limited OU and understand inheritance before broad rollout.

## When to choose

> [!exam]
> Choose for account grouping, central policy boundaries, and organization integration.

## Do not confuse with and exam traps

> [!warning]
> An OU is an account governance group, not a resource-level IAM group. [[AWS Control Tower]] adds landing-zone/account-vending governance.

## Official AWS references

- [AWS Organizations official reference](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 6 — organizational access boundaries

SCPs limit available permissions in affected member accounts but grant nothing. They do not restrict principals in the management account or service-linked roles. Test denies in a limited OU and protect governance changes with separate administrative controls.

Task 6.1. [[SCP vs Permissions Boundary vs Session Policy vs Resource Policy]], [[AWS Control Tower]], [[Domain 6 Scenario Decisions]].
