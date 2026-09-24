---
title: AWS CDK
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# AWS CDK

Define infrastructure using programming languages and synthesize CloudFormation templates.

## Exam mapping

Task statements: 2.1. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Apps contain stacks and constructs; L1 reflects CloudFormation resources, L2 supplies higher-level constructs, and L3 combines architectural patterns. Synth produces templates and deployment assets.

## Architecture pattern

Reusable construct → cdk synth/diff → deployment pipeline → [[AWS CloudFormation]] stacks.

## IAM and security

Bootstrapping provides deployment roles and asset storage. Limit who may assume deployment roles and the permissions delegated to CloudFormation.

## Failure, rollback, and lifecycle

Actual infrastructure replacement and rollback follow CloudFormation behavior. A code refactor that changes logical IDs can cause resource replacement.

## When to choose

> [!exam]
> Choose for reusable infrastructure abstractions, testing, and programming-language tooling.

## Do not confuse with and exam traps

> [!warning]
> CDK is Infrastructure as Code, not host configuration management; it does not bypass CloudFormation.

## Official AWS references

- [AWS CDK official reference](https://docs.aws.amazon.com/cdk/v2/guide/home.html)
- [[Official AWS Sources]] — source inventory and verification scope.

