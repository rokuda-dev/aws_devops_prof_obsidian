---
title: Lambda@Edge
tags: [aws, dop-c02, service]
status: consolidated-study-note
updated: 2026-09-18
read: false
---

# Lambda@Edge

Run Lambda logic at CloudFront viewer/origin request and response events.

## Exam mapping

Task statements: 1.4. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Create the function in us-east-1, publish a numbered version, and associate it with the CloudFront event. Origin events and viewer events have different cache behavior implications.

## Architecture pattern

[[Amazon CloudFront]] event → versioned edge function → transform request/response or select supported origin behavior.

## IAM and security

Execution-role trust includes the appropriate Lambda/edge services; follow replication permissions and edge-specific limitations.

## Failure, rollback, and lifecycle

An origin-group failover can invoke an origin request/response function again for the secondary. Make the function safe for repeated execution.

## When to choose

> [!exam]
> Choose for edge logic requiring capabilities beyond lightweight viewer-event JavaScript.

## Do not confuse with and exam traps

> [!warning]
> CloudFront Functions is not Lambda@Edge; $LATEST/aliases are not the deployment target for edge associations.

## Official AWS references

- [Lambda@Edge official reference](https://docs.aws.amazon.com/lambda/latest/dg/lambda-edge.html)
- [[Official AWS Sources]] — source inventory and verification scope.

