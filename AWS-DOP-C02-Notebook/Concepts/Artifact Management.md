---
tags:
  - dop-c02
  - domain-1
  - artifacts
read: true
---

# Artifact Management

## Choose by artifact type

| Artifact | Store |
|---|---|
| npm, Maven, PyPI, NuGet, Swift, Cargo, generic package | [[AWS CodeArtifact]] |
| Docker/OCI image | Amazon ECR |
| AMI or managed container image recipe output | EC2 Image Builder + AMI/ECR |
| CodePipeline stage artifact | Amazon S3 artifact store |

## Lifecycle controls

- Version artifacts and make release artifacts immutable.
- Encrypt at rest; use customer-managed KMS keys when cross-account principals must decrypt.
- Apply least-privilege repository/bucket policies.
- Scan dependencies and container images.
- Apply repository/image lifecycle policies to expire unneeded versions.
- Promote the same tested artifact across environments.

## Common trap

CodeArtifact is a language-package repository, not a container registry. ECR is the container/OCI registry. S3 is commonly used by CodePipeline for generic stage artifacts.
