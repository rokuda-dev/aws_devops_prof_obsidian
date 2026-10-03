---
title: AWS Secrets Manager
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# AWS Secrets Manager

Store and manage secrets, including supported managed rotation workflows.

## Exam mapping

Task statements: 1.1, 2.1; cross-domain 6. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Version stages such as AWSCURRENT/AWSPENDING support rotation. Supported rotation can use managed integration or a Lambda rotation function; multi-Region replicas distribute secrets.

Secrets may not be larger than 12KB.

## Architecture pattern

[[AWS CodeBuild]] or application IAM role → runtime secret retrieval → use credential without logging it.

## IAM and security

GetSecretValue and KMS authorization must be scoped. Cross-account access requires compatible resource/identity policies and encryption permissions; do not embed plaintext in source/buildspec.

## Failure, rollback, and lifecycle

Rotation must update the external credential and secret coherently. Consumers with cached or launch-time injected values may require refresh/redeployment.

## When to choose

> [!exam]
> Choose when credential lifecycle and rotation are primary requirements.

## Do not confuse with and exam traps

> [!warning]
> Secret replication is not database replication or universal cross-Region rotation. Infrastructure dynamic references are not automatic application hot-reload.

## Official AWS references

- [AWS Secrets Manager official reference](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 3 — regional secret dependencies

Use supported cross-Region secret replication to make required API keys/credentials available in recovery Regions. Configure regional encryption access and IAM; test that recovery code uses the intended regional secret.

Secret replication does not replicate the third-party API or guarantee the credential is valid for every regional external service. Ensure rotation and external dependency availability are included in testing. Never put plaintext secrets into notebook examples or baked images.

Task 3.2. See [[Multi-Region Application Checklist]], [[Resilience Framework and Dependency Isolation]].

## Domain 5 — response boundaries

Keep incident automation free of plaintext secret values. Secret storage/rotation does not prevent hard-coded IAM keys from leaking into repositories; prefer role credentials, preventive scanning and scoped exposed-key containment.

Tasks 5.1–5.3 where applicable. [[Domain 5 Scenario Decisions]], [[Safe Event-Driven Remediation]], [[Domain 5 Official Sources]].

## Domain 6 — machine-secret lifecycle

For Lambda-based rotation, the workflow creates a pending version, updates the backing service, tests it, and finishes the version transition. Supported managed rotation and managed external-secret rotation do not require a customer Lambda rotation function. Consumers using caches or launch-time injection still need a refresh strategy. Prefer workload roles over storing IAM access keys as secrets. See [rotation methods](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html).

Task 6.1–6.2. [[Domain 6 Security Automation and Data Protection]], [[AWS Systems Manager Parameter Store]], [[KMS vs CloudHSM vs ACM vs Secrets Manager]].
