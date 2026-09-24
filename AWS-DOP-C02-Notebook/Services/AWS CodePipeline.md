---
tags:
  - aws
  - dop-c02
  - domain-1
  - codepipeline
  - cicd
verified: 2026-09-20
read: true
---

# AWS CodePipeline

CodePipeline orchestrates release workflows as stages containing actions. It integrates source, build, test, approval, deploy, and custom actions; it does not compile code or perform host-level deployment itself.

## Know for the exam

- A pipeline requires a source action and at least one additional stage. Later stages can use supported Build, Test, Approval, Deploy, Invoke, or Compute actions; the second stage is not required to be Build or Deploy.
- Parallel actions in a stage run concurrently; stages run in order.
- Manual approval actions provide a managed production gate.
- Pipeline/action variables pass metadata such as commit IDs or CloudFormation outputs.
- V2 pipelines add trigger filters, pipeline variables, stage conditions, and execution modes.

| Execution mode | Behavior | Good fit |
|---|---|---|
| `SUPERSEDED` | Newer execution replaces older at stage boundaries | Only newest change matters |
| `QUEUED` | FIFO | Shared environments and ordered changes |
| `PARALLEL` | Independent concurrent executions | Isolated revisions/environments |

## Cross-Region and cross-account

- Cross-Region actions require an artifact store in every action Region; CodePipeline copies artifacts.
- Cross-account deployment requires all of:
  - a target role trusted by the pipeline account
  - artifact-bucket permissions
  - a customer-managed KMS key policy that permits the target role
  Use a key ARN/ID rather than relying on an alias across accounts.

## Exam traps

- CodePipeline is the orchestrator; [[AWS CodeBuild]] builds/tests and [[AWS CodeDeploy]] deploys application revisions.
- `PARALLEL` is inappropriate when executions mutate shared state or ordering matters.
- A connection created through IaC/API remains pending until its provider authorization is completed.

Sources: [Pipeline structure](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html), [Action structure and requirements](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-requirements.html), [CodePipeline use cases](https://docs.aws.amazon.com/codepipeline/latest/userguide/best-practices.html), [CloudFormation delivery with CodePipeline](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline.html)

## Permissions and troubleshooting

The pipeline role orchestrates actions; an action role may assume into a target account; the deployment provider can use a separate execution role. Grant only the access each layer needs. Cross-Region actions cannot be used for every action category; check the provider's support.

For access denied, inspect all three boundaries: role trust/permissions, artifact S3 policy, and KMS key authorization. For unexpected ordering, distinguish parallel actions within a stage from PARALLEL pipeline executions.

## Official AWS references

- [Cross-account pipeline actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create-cross-account.html)
- [Cross-Region actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-create-cross-region.html)
- [[Cross-Account and Cross-Region CodePipeline]]

## Domain 5 — diagnosis and execution time

Inspect failed stage/action execution details, revision and artifact handoffs, roles, approval state and downstream build/deploy evidence. Record legitimate approval rejection; do not auto-bypass the gate.

Equal runOrder values parallelize independent actions within the same stage. This is separate from pipeline execution mode and does not remove artifact dependencies or make function internals concurrent.

Task 5.3. [[CI-CD Failure Triage and Parallel Actions]].
- [Action run order](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-requirements.html)
