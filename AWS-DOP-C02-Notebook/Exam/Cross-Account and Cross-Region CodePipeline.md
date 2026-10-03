---
tags:
  - aws
  - dop-c02
  - exam
updated: 2026-09-18
read: true
---

# Cross-Account and Cross-Region CodePipeline

## Four permission layers

| Layer | Requirement |
|---|---|
| Pipeline account | Pipeline service role may assume the target action role |
| Target account | Action role trusts the pipeline account's authorized role and has required action permissions |
| Artifact bucket | Target principal can access required objects/bucket metadata |
| Artifact encryption | Customer-managed KMS key policy and caller authorization permit required use |

Use the full customer-managed key ARN to make the owning account and Region explicit. Key aliases resolve in the caller's account; a bare key ID should not be treated as an unambiguous cross-account reference. An AWS-managed artifact key is not the cross-account solution.

## Regional topology

Use an artifact store in each action Region. CodePipeline copies required input artifacts for supported cross-Region actions. Each artifact bucket and encryption key must be in the action's Region and the pipeline's account, even when the action runs in another account.

A cross-account action can be in the same Region; a cross-Region action can be in the same account. Do not collapse the two into one requirement.

## Deployment role distinction

The assumed action role and a CloudFormation execution role are different layers. iam:PassRole is needed where a caller passes a provider execution role. Least privilege must hold at each boundary.

## Troubleshooting and traps

Access denied can come from trust, IAM permissions, S3 policy, KMS policy, or an organization deny. Granting AdministratorAccess to one layer is not a diagnosis.

Not every action category/provider supports cross-Region or cross-account operation. Consult current provider requirements rather than assuming a universal action pattern.

An artifact cannot pass directly between actions in two other accounts when neither account is the pipeline account. Cross-Region Source, third-party, and custom actions are not supported. These topology restrictions can invalidate an otherwise correctly authorized design.

- [Cross-account actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create-cross-account.html)
- [Cross-Region actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-create-cross-region.html)
