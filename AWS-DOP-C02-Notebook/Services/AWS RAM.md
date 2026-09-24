---
title: AWS RAM
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# AWS Resource Access Manager

Share supported existing AWS resources across accounts and organizational boundaries.

## Exam mapping

Task statements: 2.2. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Resource shares include supported resources, principals, and managed permissions. Organization integration can avoid invitation workflows for eligible organization sharing.

## Architecture pattern

Owning account's supported resource → resource share → approved consumer account/OU.

## IAM and security

The owner retains ownership. Check service-specific sharing support, permissions, organization trust, and invitation requirements.

## Failure, rollback, and lifecycle

Removing a share revokes sharing access but is not the same as deleting the owning resource. Consumers still depend on the resource's lifecycle.

## When to choose

> [!exam]
> Choose to avoid duplicating a shareable existing resource such as supported network infrastructure.

## Do not confuse with and exam traps

> [!warning]
> RAM is not arbitrary resource sharing and does not provision a separate copy in every consumer account.

## Official AWS references

- [AWS RAM official reference](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html)
- [[Official AWS Sources]] — source inventory and verification scope.

