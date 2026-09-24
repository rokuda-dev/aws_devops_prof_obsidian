---
title: CI-CD Failure Triage and Parallel Actions
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# CI-CD Failure Triage and Parallel Actions

## Find the failed layer

| Layer | Evidence and checks |
|---|---|
| CodePipeline | Failed stage/action, execution details, revision/artifacts, action role, approval state |
| CodeBuild | Phase context/build logs, buildspec/tests, dependency/artifact access, VPC connectivity |
| CodeDeploy | Deployment and per-target status, hook result, health constraint, alarm history, platform-specific logs |
| CloudFormation | Stack events, failing logical resource/status reason, permissions, change/replacement dependencies |
| Runtime | Application/container logs, metrics/traces, synthetic checks, network and dependency behavior |

An approval rejection is a workflow decision, not necessarily a build failure. Preserve the reason and authorized approver/audit evidence rather than auto-bypassing the gate.

## Safe parallelization

Independent actions within the **same stage** run in parallel when configured with the same runOrder. Different values order actions. This does not automatically parallelize the bodies of Lambda functions or bypass dependencies between stages.

Separate artifacts/outputs and verify downstream quotas, contention, correctness, and rollback scope. Faster execution is not a root-cause fix for broken tests or deployment permissions.

## CodeDeploy host threshold

For EC2/on-premises custom deployment configurations, MinimumHealthyHosts uses HOST_COUNT or FLEET_PERCENT to express an availability constraint. These are configuration types, not two metrics that measure current host health. Inspect actual deployment/per-host and application health; overall success may have documented host exceptions.

Task 5.3. [[AWS CodePipeline]], [[AWS CodeBuild]], [[AWS CodeDeploy]], [[AWS CloudFormation]], [[Lambda vs ECS vs EC2 CodeDeploy Hooks]], [[Domain 5 Official Sources]].
