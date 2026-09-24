---
title: AWS CodeConnections
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# AWS CodeConnections

Managed authorization between AWS developer tools and supported external Git providers.

## Exam mapping

Task statements: 1.1. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Connections link providers such as GitHub, GitLab, and Bitbucket. CLI/IaC-created connections start PENDING until provider authorization is completed in the console.

## Architecture pattern

Provider commit/PR → authorized connection → [[AWS CodePipeline]] source → [[AWS CodeBuild]].

## IAM and security

Scope UseConnection to the connection and supported repository/action conditions. New and older resources can have codeconnections or codestar-connections ARN prefixes.

## Failure, rollback, and lifecycle

A pending/revoked connection prevents source access. Confirm authorization, provider installation access, event filters, and service-role permissions.

## When to choose

> [!exam]
> Choose for external source integration without embedding personal tokens in build configuration.

## Do not confuse with and exam traps

> [!warning]
> CodeConnections authenticates access; it does not host repositories or orchestrate releases.

## Official AWS references

- [AWS CodeConnections official reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections.html)
- [[Official AWS Sources]] — source inventory and verification scope.
