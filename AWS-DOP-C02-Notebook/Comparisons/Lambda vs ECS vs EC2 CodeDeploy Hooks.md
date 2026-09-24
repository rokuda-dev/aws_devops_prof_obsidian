---
title: Lambda vs ECS vs EC2 CodeDeploy Hooks
tags: [aws, dop-c02, domain-5]
verified: 2026-09-20
read: false
---

# Lambda vs ECS vs EC2 CodeDeploy Hooks

| Platform | Deployable unit | User-scriptable validation hooks | Important distinction |
|---|---|---|---|
| Lambda | Published function versions and alias | BeforeAllowTraffic, AfterAllowTraffic | Explicit candidate-version validation; no AfterAllowTestTraffic |
| ECS with CodeDeploy | Replacement task set with load-balancer traffic | BeforeInstall, AfterInstall, AfterAllowTestTraffic, BeforeAllowTraffic, AfterAllowTraffic | Test listener enables test-traffic validation |
| EC2/on-premises | Revision installed by agent on target instances | ApplicationStop, BeforeInstall, AfterInstall, ApplicationStart, ValidateService, BeforeBlockTraffic, AfterBlockTraffic, BeforeAllowTraffic, AfterAllowTraffic | Scripts run on hosts; prior revision supplies ApplicationStop; traffic-hook availability depends on the deployment/rollback lifecycle |

Lambda/ECS validation functions must report hook execution status through the callback API. For EC2/on-premises, `DownloadBundle`, `Install`, `BlockTraffic`, and `AllowTraffic` are reserved agent events, not user-scriptable AppSpec hooks.

MinimumHealthyHosts HOST_COUNT/FLEET_PERCENT is an EC2/on-premises configuration concern, not a Lambda traffic-shift metric. ECS-native deployment hooks are a separate controller; do not transplant CodeDeploy names blindly.

Task 5.2–5.3. [[AWS CodeDeploy]], [[Lambda Deployment Validation Hooks]], [[ECS Native vs CodeDeploy Deployments]].

- [Official platform hook definitions](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html)
