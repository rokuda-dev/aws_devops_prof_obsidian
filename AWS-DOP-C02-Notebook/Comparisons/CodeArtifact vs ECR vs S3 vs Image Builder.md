---
tags: [aws, dop-c02, comparisons]
updated: 2026-09-18
read: false
---

# CodeArtifact vs ECR vs S3 vs Image Builder

| Requirement | Choose | Key distinction |
|---|---|---|
| Package dependencies/private package publication | [[AWS CodeArtifact]] | Domain/repository/upstream/external connection |
| Container/OCI registry | [[Amazon ECR]] | Manifests/layers/tags/digests/scanning |
| Generic zipped pipeline artifact | [[Amazon S3]] | Artifact bucket, versions, encryption/access |
| Validated AMI/container image pipeline | [[EC2 Image Builder]] | Build/test/distribute images |
| General custom build compute | [[AWS CodeBuild]] | Executes build commands, publishes elsewhere |

> [!important]
> Artifact creation, storage, promotion, distribution, and deployment are different activities. Keep the tested artifact immutable and retain enough history for rollback.

