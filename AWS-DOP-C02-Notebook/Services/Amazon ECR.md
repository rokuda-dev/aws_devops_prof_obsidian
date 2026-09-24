---
title: Amazon ECR
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# Amazon ECR

Managed registry for container images and OCI artifacts.

## Exam mapping

Task statements: 1.3, 1.4. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Repositories store image manifests/layers. Use immutable release tags or image digests, image scanning, lifecycle-policy previews, and supported replication.

## Architecture pattern

[[AWS CodeBuild]] builds/tests image → push digest → [[Amazon ECS]] deploys that digest.

## IAM and security

Cross-account pulls need caller IAM and repository permissions; GetAuthorizationToken is registry-level. Image-pulling permissions generally belong to the ECS execution role.

## Failure, rollback, and lifecycle

Retain rollback image digests. Lifecycle expiration can remove artifacts still needed by old task definitions; preview rules and retain release history.

## When to choose

> [!exam]
> Choose for container/OCI artifacts, not language dependencies or AMI creation.

## Do not confuse with and exam traps

> [!warning]
> ECR stores images; [[EC2 Image Builder]] or CodeBuild creates them. Replication is not the same as granting a target account pull access.

## Official AWS references

- [Amazon ECR official reference](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 3 — regional image readiness

Configure supported cross-Region/cross-account replication so images are available near each regional deployment. Destination permissions matter for cross-account replication.

Images pushed/restored after replication is configured can replicate; preexisting images are not automatically backfilled. Verify the recovery image digest exists before an outage. Local pulls use the regional replica; pulling does not itself define the replication configuration.

Task 3.2. See [[Multi-Region Application Checklist]], [[Amazon EKS]].
- [ECR replication behavior](https://docs.aws.amazon.com/AmazonECR/latest/userguide/replication.html)
