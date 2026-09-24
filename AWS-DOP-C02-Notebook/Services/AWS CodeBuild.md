---
tags:
  - aws
  - dop-c02
  - domain-1
  - codebuild
read: true
---

# AWS CodeBuild

CodeBuild is a managed build service for compiling, testing, scanning, packaging, and producing artifacts.

## `buildspec.yml`

Typical phases:

```text
install → pre_build → build → post_build
```

Use `artifacts` for build output, `reports` for test/coverage results, and `cache` for reusable dependencies. Commands return non-zero exit status to fail a build.

## High-value features

- S3 cache works across hosts; local cache is tied to host reuse and is best-effort for on-demand builds.
- Batch builds support build graphs and build matrices.
- VPC configuration lets builds reach private resources. CodeBuild cannot assign a public IP to its VPC ENI, so private subnets need NAT or suitable VPC endpoints for required services.
- Docker image builds usually require privileged mode.
- Use the project service role; never embed long-lived AWS keys.

## Secrets

Reference Parameter Store or Secrets Manager values in the build environment. The role needs `ssm:GetParameters` or `secretsmanager:GetSecretValue` as appropriate.

> [!exam]
> CodeBuild can call AWS APIs if its role permits it, but select purpose-built deployment services when a question asks for controlled releases, traffic shifting, or deployment lifecycle management.

Related: [[AWS CodePipeline]], [[AWS CodeArtifact]], [[Amazon ECR and EC2 Image Builder]].

## Test report retention

CodeBuild test reports expire after **30** days. Export raw report files to S3 when longer retention is required; apply suitable S3 lifecycle/retention controls.

## Failure and artifact promotion

Report generation is not a substitute for correct test exit status. Do not swallow failed tests with shell commands that return success. Promote the same tested artifact rather than rebuilding an unrelated production revision. Cache is an optimization, not a durable source of release artifacts.

## Official AWS references

- [Test reports and expiration](https://docs.aws.amazon.com/codebuild/latest/userguide/test-reporting.html)
- [CodeBuild overview](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)
- [VPC support](https://docs.aws.amazon.com/codebuild/latest/userguide/vpc-support.html)

## Domain 5 — isolate the failing phase

Use build phase context/logs and test/report results to distinguish source/dependency download, buildspec/runtime, tests, artifact upload and permission failures. For VPC builds, diagnose service/internet connectivity from the build context, not a developer laptop.

Preserve the exact source revision, build image/dependencies and artifact identifiers. Fix demonstrated causes before retrying; do not treat every timeout as inadequate compute.

Task 5.3. [[CI-CD Failure Triage and Parallel Actions]], [[HTTPS Connectivity Troubleshooting]].
