---
tags:
  - aws
  - dop-c02
  - domain-1
  - elastic-beanstalk
verified: 2026-09-18
read: true
---

# AWS Elastic Beanstalk

Elastic Beanstalk deploys applications while provisioning and operating underlying AWS resources such as compute, load balancing, scaling, and health monitoring.

## Current service model

AWS documentation now describes:

- **Standard** — applications run directly on EC2; includes Windows support and familiar Beanstalk platform branches.
- **Cluster** — applications run on EKS, with container images or source built into images, faster deployments/scaling, and managed OpenTelemetry integration.

## Standard deployment policies

- All at once
- Rolling
- Rolling with additional batch
- Immutable
- Traffic splitting
- Blue/green by creating a separate environment and swapping environment URLs/CNAMEs

## Exam cues

- Managed web application platform with access to underlying resources → Elastic Beanstalk.
- Lowest-risk production change → immutable or blue/green, accepting temporary extra capacity.
- Avoid mixing Beanstalk deployment-policy names with CodeDeploy deployment configurations.

Source: [Elastic Beanstalk overview](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)

## Current-state caution

Cluster Mode was announced September 17, 2026. Treat it as a current-product correction, not a prediction of immediate exam inclusion. Standard Mode remains supported. Do not assume every Standard deployment-policy name or platform capability applies identically in Cluster Mode.

## Failure and architecture

Rolling policies can leave mixed revisions during rollout; immutable deployments create temporary replacement capacity. Blue/green environment swaps require application/data compatibility and DNS considerations. Externalize durable state to allow replacement and rollback.

Elastic Beanstalk orchestrates underlying resources; application instance roles, deployment permissions, networking, and secret access still need least-privilege configuration.

- [Mode concepts](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.html)
- [Cluster Mode release](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2026-09-17-cluster-mode.html)
