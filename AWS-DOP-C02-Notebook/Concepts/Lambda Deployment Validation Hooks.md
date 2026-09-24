---
title: Lambda Deployment Validation Hooks
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# Lambda Deployment Validation Hooks

## Correct Lambda model

CodeDeploy shifts traffic between published versions through an alias. The Lambda AppSpec identifies the function, alias, current version, and target version. Coordinate a multi-function application with its individual deployments/pipeline rather than treating several functions as an EC2 host fleet.

## Validation contract

| Hook | Purpose |
|---|---|
| BeforeAllowTraffic | Validate the target version before alias traffic shifts |
| AfterAllowTraffic | Validate after production traffic shifts |

Invoke the **target version** explicitly for pre-traffic tests; testing the production alias alone can test the old version. API-level validation must ensure requests actually reach the candidate path. Lambda has no CodeDeploy AfterAllowTestTraffic hook; that name belongs to the ECS deployment workflow.

The validation function reports Succeeded or Failed using PutLifecycleEventHookExecutionStatus with the deployment and hook execution IDs. Returning from Lambda without the callback does not satisfy the hook. CodeDeploy treats absent notification within one hour as failure.

## Failure and rollback

Enable applicable automatic rollback on deployment failure and alarm-stop events. Hook validation failure and CloudWatch alarm breach are distinct triggers. Choose relevant service metrics: Lambda Errors/Duration are not an HTTP 5XX metric; API Gateway or load-balancer HTTP signals use their own namespaces/dimensions.

Rollback does not reverse database writes or external side effects. Use compatible data changes and safe tests.

Tasks 5.2–5.3. [[AWS CodeDeploy]], [[AWS Lambda]], [[Lambda vs ECS vs EC2 CodeDeploy Hooks]].

- [Platform-specific AppSpec hooks](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html)
- [Deployment workflows — official resource](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-steps.html#deployment-steps-what-happens)
