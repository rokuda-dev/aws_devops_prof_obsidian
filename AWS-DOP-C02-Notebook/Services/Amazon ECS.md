---
title: Amazon ECS
tags: [aws, dop-c02, service]
status: consolidated-study-note
updated: 2026-09-18
read: false
---

# Amazon ECS

Container orchestration with rolling and native or CodeDeploy-controlled traffic-shifting deployments.

## Exam mapping

Task statements: 1.4; cross-domain resilience. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Clusters provide capacity; task definitions specify containers; tasks run revisions; services maintain desired count. Fargate avoids host management; EC2 provides host-level control.

## Architecture pattern

[[AWS CodeBuild]] builds image → [[Amazon ECR]] → service revision → rolling or native blue/green/canary/linear deployment.

## IAM and security

Execution role: image pulls, logs, launch-time secret retrieval. Task role: application AWS API calls. Fargate uses awsvpc; private tasks need required endpoints or NAT.

## Failure, rollback, and lifecycle

Rolling deployment circuit breaker/alarms can detect failure and roll back when enabled. Native ECS traffic-shifting supports alarms/hooks; CodeDeploy ECS uses task sets and two target groups.

## When to choose

> [!exam]
> Choose ECS-native traffic shifting for new ECS releases; keep CodeDeploy when the question explicitly describes its controller, AppSpec, task sets, or deployment groups.

## Do not confuse with and exam traps

> [!warning]
> Native ECS traffic shifting exists. Do not assume all blue/green deployments require CodeDeploy. Launch-time injected secrets do not hot-reload.

## Official AWS references

- [Amazon ECS official reference](https://aws.amazon.com/blogs/devops/choosing-between-amazon-ecs-blue-green-native-or-aws-codedeploy-in-aws-cdk/)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 3 — scalable and recoverable containers

[[AWS Application Auto Scaling]] changes ECS service desired task count. EC2 capacity-provider/ASG scaling changes available hosts; [[AWS Fargate]] supplies task compute without EC2 host administration. These are distinct capacity layers.

Choose policies, replica bounds, health checks, placement/AZ distribution, startup time, quotas, and deployment headroom. Protect downstream database connections from an uncontrolled task surge.

For regional DR, deploy compatible services, networking, IAM, secrets and data access in each Region. Ensure [[Amazon ECR]] images exist locally. Scaling task count does not replicate application state.

Task 3.2. See [[Multi-Region Application Checklist]], [[Scaling Metrics and Troubleshooting]].

## Domain 4 — logs and capacity layers

awslogs task configuration sends stdout/stderr to CloudWatch Logs; a host CloudWatch agent is not required for this driver alone. Fargate uses execution-role log delivery; FireLens destination calls use the task role. Verify EC2 ECS agent/driver/role behavior separately.

Explicitly choose blocking/non-blocking behavior. Current default is non-blocking unless overridden; full buffers can drop logs, while blocking can stall application writes.

Logs subscription → Firehose → S3 archives application logs. ALB logs require separate setup. Capacity-provider infrastructure strategy and service desired-count scaling remain distinct.

Tasks 4.1–4.3. See [[CloudWatch Agent and Container Log Collection]], [[Domain 4 Scenario Decisions]], [[AWS Application Auto Scaling]].
- [Current driver default](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html)

## Domain 5 — service and process failures

Check service events, deployment status, stopped-task/container reasons, placement/capacity, image/execution-role access, network path, startup/target health and configured logs. Exit 137 indicates SIGKILL; confirm OOM versus termination timeout/other causes.

Fargate uses configured task logging and authorized container-level tooling, not SSH/Docker access to a host. Local docker logs on EC2 only applies where supported and retained by the driver.

Task 5.3. [[ECS and EKS Failure Triage]], [[CloudWatch Container Insights]], [[CI-CD Failure Triage and Parallel Actions]].
