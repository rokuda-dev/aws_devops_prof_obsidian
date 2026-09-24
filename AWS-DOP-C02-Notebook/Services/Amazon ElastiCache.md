---
title: Amazon ElastiCache
tags: [aws, dop-c02, service]
status: consolidated-study-note
updated: 2026-09-18
read: false
---

# Amazon ElastiCache

Shared low-latency cache/session storage, with engine and deployment-specific resilience choices.

## Exam mapping

Task statements: 1.4; cross-domain 3. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Supported engines and deployment models differ. A shared session store lets replacement application instances serve the same users without instance-local state.

## Architecture pattern

ALB → disposable app instances → shared session store; choose TTL, access controls, and failure behavior deliberately.

## IAM and security

Use private networking, supported authentication, and encryption settings. Restrict access from application security groups.

## Failure, rollback, and lifecycle

Externalizing sessions removes host dependency but does not guarantee session durability by itself. Select engine/configuration, replication/failover, persistence, and fallback to match loss tolerance.

## When to choose

> [!exam]
> Choose for fast shared sessions/caching; [[Amazon DynamoDB]] is another session-store option when its durability/access model fits.

## Do not confuse with and exam traps

> [!warning]
> Load-balancer stickiness is not durable external state. Do not generalize one engine's persistence/failover to all ElastiCache configurations.

## Official AWS references

- [Amazon ElastiCache official reference](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html)
- [[Official AWS Sources]] — source inventory and verification scope.

