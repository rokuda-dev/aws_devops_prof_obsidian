---
title: AWS SAM
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# AWS SAM

Serverless-focused Infrastructure as Code built on CloudFormation.

## Exam mapping

Task statements: 1.4, 2.1. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

The AWS::Serverless-2016-10-31 transform expands SAM resources into CloudFormation resources. Functions, APIs, and event sources can coexist with ordinary CloudFormation resources.

## Architecture pattern

Build/package application → deploy stack → AutoPublishAlias + DeploymentPreference → [[AWS CodeDeploy]] Lambda rollout.

## IAM and security

Use scoped function execution roles and deployment roles; never embed secret values in a SAM template.

## Failure, rollback, and lifecycle

Alias-based CodeDeploy traffic shifting can roll back on validation failure or alarms. Infrastructure changes still follow CloudFormation update/rollback semantics.

## When to choose

> [!exam]
> Choose for concise Lambda/API/event-source templates and integrated serverless deployment tooling.

## Do not confuse with and exam traps

> [!warning]
> SAM is not a separate infrastructure provisioning engine; aliases and published versions are required for controlled version traffic.

## Official AWS references

- [AWS SAM official reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 3 — build containers are not deployment package type

SAM CLI containerized builds can supply a Lambda-compatible build environment for dependencies/native compilation. This is separate from choosing a Lambda container-image deployment package versus ZIP.

CI/CD systems can run SAM CLI using a suitable host or build container. Choose compatible build images, runtimes, dependency tools and permissions. Templates still require regional data/configuration and recovery design.

Task 3.2. See [[AWS Lambda]], [[Amazon API Gateway]], [[Domain 3 Transcript Corrections]].
- [SAM containerized build example](https://aws.amazon.com/blogs/dotnet/building-serverless-net-applications-with-aws-lambda-and-the-sam-cli/)
