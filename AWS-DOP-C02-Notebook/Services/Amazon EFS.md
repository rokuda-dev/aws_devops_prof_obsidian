---
title: Amazon EFS
tags: [aws, dop-c02, service]
status: consolidated-study-note
updated: 2026-09-18
read: false
---

# Amazon EFS

Managed shared NFS/POSIX filesystem for supported Linux workloads.

## Exam mapping

Task statements: 1.4; cross-domain 3. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Regional and One Zone filesystem options have different resilience. Mount targets provide VPC connectivity; access points help isolate application paths/identities.

## Architecture pattern

Replacement Linux app instances → mount shared EFS filesystem → retained files independent of host lifecycle.

## IAM and security

Use security groups, supported IAM authorization, access points, encryption at rest/in transit, and appropriate file permissions.

## Failure, rollback, and lifecycle

Shared files survive instance replacement, but backup/recovery and filesystem availability still require a design. One Zone does not have the same AZ resilience as Regional.

## When to choose

> [!exam]
> Choose when multiple Linux clients require shared filesystem semantics.

## Do not confuse with and exam traps

> [!warning]
> EFS is neither object storage nor ordinary EC2-attached block storage; externalizing sessions and sharing files are distinct application decisions.

## Official AWS references

- [Amazon EFS official reference](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)
- [[Official AWS Sources]] — source inventory and verification scope.

