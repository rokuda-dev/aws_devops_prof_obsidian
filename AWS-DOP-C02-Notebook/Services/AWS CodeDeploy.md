---
tags:
  - aws
  - dop-c02
  - domain-1
  - codedeploy
read: true
---

# AWS CodeDeploy

CodeDeploy automates application deployments to EC2/on-premises instances, Amazon ECS, and Lambda. Deployment behavior and AppSpec hooks depend on the compute platform.

## EC2 and on-premises

- EC2 supports in-place and blue/green deployments; on-premises instances support in-place, not CodeDeploy blue/green.
- CodeDeploy agent runs lifecycle scripts from the AppSpec file.
- The complete EC2/on-premises scriptable lifecycle set is:
  - `ApplicationStop`
  - `BeforeInstall`
  - `AfterInstall`
  - `ApplicationStart`
  - `ValidateService`
  - `BeforeBlockTraffic`
  - `AfterBlockTraffic`
  - `BeforeAllowTraffic`
  - `AfterAllowTraffic`
  Traffic hooks run only when that lifecycle applies to the deployment or rollback.
- `ApplicationStop` uses the **previous successfully deployed revision**, so it does not run on the first deployment to an instance. A broken old stop script can block later deployments.
- Five hook environment variables are always available: `APPLICATION_NAME`, `DEPLOYMENT_ID`, `DEPLOYMENT_GROUP_NAME`, `DEPLOYMENT_GROUP_ID`, and `LIFECYCLE_EVENT`.
- An S3 revision also supplies `BUNDLE_BUCKET`, `BUNDLE_KEY`, `BUNDLE_ETAG`, and—when S3 versioning is enabled—`BUNDLE_VERSION`. A GitHub revision supplies `BUNDLE_COMMIT`.
- `DownloadBundle`, `Install`, `BlockTraffic`, and `AllowTraffic` are reserved agent events and cannot be scripted in the AppSpec file.

## ECS

CodeDeploy creates a replacement task set and shifts load-balancer traffic between two target groups. Validation hooks are Lambda functions:

`BeforeInstall` → `AfterInstall` → `AfterAllowTestTraffic` → `BeforeAllowTraffic` → `AfterAllowTraffic`.

A test listener enables pre-production validation against the replacement task set.

With a Network Load Balancer, only CodeDeployDefault.ECSAllAtOnce is supported. Use supported ALB configurations for CodeDeploy canary/linear traffic shifting.

## Lambda

CodeDeploy shifts an alias between two immutable function versions. It supports all-at-once, canary, and linear configurations. Hooks are `BeforeAllowTraffic` and `AfterAllowTraffic` Lambda validation functions.

## Rollback

Enable automatic rollback on deployment failure or CloudWatch alarm. For ECS/Lambda, rollback redirects traffic. For EC2, rollback creates a new deployment of the last known good revision.

Sources: [AppSpec hooks](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html), [deployment workflows](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-steps.html)

## Security and side effects

Keep the CodeDeploy service role distinct from the EC2 instance profile or function execution role. EC2/on-premises hosts require the CodeDeploy agent and artifact connectivity; ECS/Lambda do not use the EC2 CodeDeploy agent. Hook functions must return deployment validation status through the supported callback API.

Rollback does not undo schema migrations or external side effects. Use backward-compatible expand/contract database changes and make scripts safe to re-run.

## Current ECS distinction

ECS-native blue/green, canary, and linear strategies are also available. An exam scenario that specifies CodeDeploy AppSpec, deployment groups, or task sets still points to this CodeDeploy pattern; do not call the supported CodeDeploy service retired.

- [[ECS Native vs CodeDeploy Deployments]]
- [[High-Value Exam Patterns#Lambda alias canary]]

## Deployment-configuration traps

CodeDeployDefault.AllAtOnce on EC2 can report overall success when only one target instance deploys successfully. OneAtATime also has a last-instance failure exception for multi-instance groups. Do not equate deployment Succeeded with every host running the new revision: inspect per-instance status and application health.

- [Platform deployment configuration rules](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html)
- [EC2 versus on-premises blue/green support](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html)

## Domain 4 — notifications versus rollback

Instance/deployment state-change events can route through EventBridge (older docs say CloudWatch Events).

Deployment alarm integration and rollback must be configured for the actual deployment/platform. They do not restore an arbitrary S3 bucket policy or repair every root cause.

Tasks 4.2–4.3. See [[Metric Alarms and Anomaly Detection]], [[Safe Event-Driven Remediation]].
- [Deployment events resource](https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-cloudwatch-events.html)

## Domain 5 — validation and failure analysis

Lambda uses BeforeAllowTraffic and AfterAllowTraffic, not ECS's AfterAllowTestTraffic. Validate the explicit target version and send the hook execution result through PutLifecycleEventHookExecutionStatus; a Lambda return alone is insufficient.

Configure the relevant failure/alarm rollback behavior separately. Service metrics and dimensions must match the API/function/load-balancer signal being monitored.

MinimumHealthyHosts with HOST_COUNT or FLEET_PERCENT is an EC2/on-premises deployment-configuration constraint, not a generic health metric for Lambda. Inspect deployment/per-target results and application health rather than equating overall success with every target succeeding.

Tasks 5.2–5.3. [[Lambda Deployment Validation Hooks]], [[Lambda vs ECS vs EC2 CodeDeploy Hooks]], [[CI-CD Failure Triage and Parallel Actions]].
