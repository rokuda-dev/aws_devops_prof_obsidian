---
title: AWS CodeCommit
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# AWS CodeCommit

Managed Git repositories with IAM-integrated authorization.

## Exam mapping

Task statements: 1.1. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Repositories, branches, commits, pull requests, and repository events support source-driven workflows. AWS reopened the service to new customers on November 25, 2025.

## Architecture pattern

Commit/PR → repository event/source action → [[AWS CodeBuild]] tests → [[AWS CodePipeline]] release.

## IAM and security

Restrict repository/branch actions with IAM. Use supported Git authentication and encryption controls; avoid hardcoded long-lived keys.

## Failure, rollback, and lifecycle

A source repository does not deploy changes by itself. Version history supports restoring a revision; deployment rollback belongs to deployment tooling.

## When to choose

> [!exam]
> Choose when a scenario calls for AWS-managed Git source control and IAM integration.

## Do not confuse with and exam traps

> [!warning]
> The temporary 2024 new-customer restriction is not current. [[AWS CodeConnections]] connects external repositories; it is not Git storage.

## Official AWS references

- [AWS CodeCommit official reference](https://docs.aws.amazon.com/codecommit/latest/userguide/history.html)
- [[Official AWS Sources]] — source inventory and verification scope.
