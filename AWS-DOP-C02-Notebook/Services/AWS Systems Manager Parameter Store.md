---
title: AWS Systems Manager Parameter Store
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# AWS Systems Manager Parameter Store

Hierarchical storage for parameters and KMS-encrypted SecureString values.

## Exam mapping

Task statements: 1.1, 2.1. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Parameters include String, StringList, and SecureString, with versioning and tier-dependent policies/sharing. Hierarchical paths organize environments and applications.

## Architecture pattern

[[AWS CodeBuild]]/application/[[AWS CloudFormation]] retrieves parameter through its IAM role.

## IAM and security

SecureString access needs relevant SSM permissions and KMS authorization. Scope paths carefully; encryption is not a substitute for access policy.

## Failure, rollback, and lifecycle

Updating an AMI parameter does not refresh an Auto Scaling fleet. CloudFormation must consume the new value in an update and trigger the appropriate host replacement.

## When to choose

> [!exam]
> Choose for general hierarchical configuration and encrypted parameters.

## Do not confuse with and exam traps

> [!warning]
> Secrets Manager is the stronger default when managed secret rotation/lifecycle is central; parameter versioning is not rotation of an external credential.

## Official AWS references

- [AWS Systems Manager Parameter Store official reference](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 6 — secure configuration

SecureString values use KMS; ordinary String values are not encrypted by Parameter Store. Secrets Manager references use the `/aws/reference/secretsmanager/<secret>` prefix and support GetParameter/GetParameters, not GetParametersByPath. Cross-account parameter sharing requires advanced-tier parameters and AWS RAM/resource-policy configuration.

Task 6.2. [[Domain 6 Security Automation and Data Protection]], [[AWS Secrets Manager]], [[KMS vs CloudHSM vs ACM vs Secrets Manager]].
