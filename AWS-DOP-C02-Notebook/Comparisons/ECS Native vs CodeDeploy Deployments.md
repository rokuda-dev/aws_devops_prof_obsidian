---
tags:
  - aws
  - dop-c02
  - comparisons
updated: 2026-09-18
read: true
---

# ECS Native vs CodeDeploy Deployments

| Dimension | ECS-native traffic shifting | CodeDeploy ECS blue/green |
|---|---|---|
| Deployment controller | ECS | CODE_DEPLOY |
| Revision unit | Service revision | Task set |
| Configuration | ECS deployment configuration | Application/deployment group/AppSpec |
| Traffic strategies | Native blue/green, canary, linear | All-at-once/canary/linear subject to LB support |
| Validation | Supported ECS lifecycle hooks | AppSpec Lambda hooks |
| Alarms/rollback | Supported native integrations | CodeDeploy deployment/rollback configuration |
| Best cue | New ECS service without CodeDeploy dependency | Explicit deployment group/AppSpec/task-set scenario |

> [!important]
> Native blue/green launched July 2025; canary/linear support followed October 2025. AWS's updated guidance favors ECS-native for new deployments. CodeDeploy remains supported and important for questions that specify its architecture.

Do not mix controller-specific settings or assume all ALB/NLB combinations have identical gradual-shift support.

Official reference: [AWS comparison and current recommendation](https://aws.amazon.com/blogs/devops/choosing-between-amazon-ecs-blue-green-native-or-aws-codedeploy-in-aws-cdk/).

