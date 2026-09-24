---
title: Amazon EBS
tags: [aws, dop-c02, service]
status: consolidated-study-note
updated: 2026-09-18
read: false
---

# Amazon EBS

Block storage attached to EC2, with volume/snapshot lifecycle independent of application deployment.

## Exam mapping

Task statements: 1.4; cross-domain 3. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Volumes are Availability Zone-scoped; snapshots support recovery and creation of volumes. Supported Multi-Attach exceptions have strict volume/instance/application requirements.

## Architecture pattern

EC2 + volume → snapshots/backup → restore volume in target AZ as needed.

## IAM and security

Use encryption/KMS permissions and scoped snapshot-sharing controls.

## Failure, rollback, and lifecycle

Deleting/replacing an instance can delete attached volumes according to DeleteOnTermination settings. Protect important data and validate restoration.

## When to choose

> [!exam]
> Choose for EC2 block-device semantics and AZ-local volume workloads.

## Do not confuse with and exam traps

> [!warning]
> Do not treat ordinary EBS as a shared cross-AZ POSIX filesystem. Application-level consistency still matters for snapshots.

## Official AWS references

- [Amazon EBS official reference](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html)
- [[Official AWS Sources]] — source inventory and verification scope.

