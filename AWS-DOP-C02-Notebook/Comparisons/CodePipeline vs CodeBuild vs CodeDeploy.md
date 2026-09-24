---
tags: [aws, dop-c02, comparisons]
updated: 2026-09-18
read: false
---

# CodePipeline vs CodeBuild vs CodeDeploy

| Service | Responsibility | Not its primary role |
|---|---|---|
| [[AWS CodePipeline]] | Orchestrate source/build/test/approval/deploy actions | Compilation or running host scripts itself |
| [[AWS CodeBuild]] | Compile/test/scan/package, execute authorized commands | Managed platform-specific traffic shifting |
| [[AWS CodeDeploy]] | Application revision lifecycle/traffic shifts/validation hooks | General-purpose IaC |
| [[AWS CloudFormation]] | Infrastructure provisioning/update lifecycle | Language compilation |

CodeBuild can invoke AWS APIs if authorized, including publishing Lambda versions. That does not make custom build scripts the best answer when managed deployment behavior is requested.

A pipeline action can fail due to the pipeline role, assumed action role, deployment execution role, S3 access, or KMS authorization. Identify the failing layer.

