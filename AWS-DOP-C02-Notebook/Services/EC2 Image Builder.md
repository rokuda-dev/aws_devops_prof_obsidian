---
title: EC2 Image Builder
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# EC2 Image Builder

Automate creation, testing, and distribution of AMIs and container images.

## Exam mapping

Task statements: 1.3, 2.1. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Recipes combine a source image and build/test components. Infrastructure configuration defines build resources; distribution configuration defines image destinations.

## Architecture pattern

Source/recipe + components → build → tests → distribute AMI or publish to [[Amazon ECR]].

## IAM and security

Scope build-instance and service permissions; control access to components, source images, distribution targets, and KMS keys.

## Failure, rollback, and lifecycle

Failed validation should block image promotion. Publishing an AMI or updating an SSM parameter does not replace running instances: update the launch template and refresh the fleet.

## When to choose

> [!exam]
> Choose for repeatable golden images, patch rebuilds, and validated multi-account/Region distribution.

## Do not confuse with and exam traps

> [!warning]
> Image Builder builds the image; Auto Scaling/CloudFormation rollout mechanics replace the hosts.

## Official AWS references

- [EC2 Image Builder official reference](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 3 — fast, repeatable scale-out

Bake tested application libraries/web components into an AMI instead of downloading every dependency during each launch. Systems Manager Automation can also build/customize images.

Distribute the AMI to required Regions, update the ASG launch-template version, and roll out through a deliberate instance refresh/deployment process. An image existing in a catalog does not update running instances. Keep secrets appropriately dynamic, not baked into the image.

Task 3.2. See [[Amazon EC2 Auto Scaling]], [[AWS Systems Manager]], [[Resilience Framework and Dependency Isolation]].
