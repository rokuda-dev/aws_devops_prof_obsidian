---
tags:
  - aws
  - dop-c02
  - domain-1
  - codeartifact
  - artifacts
read: true
---

# AWS CodeArtifact

CodeArtifact is a managed software package repository. It supports formats such as npm, Maven, PyPI, NuGet, Swift, Cargo, and generic packages.

## Concepts

- **Domain** — top-level container, encryption and cross-repository policy boundary.
- **Repository** — stores packages.
- **Upstream repository** — lets a repository obtain packages from another CodeArtifact repository.
- **External connection** — connects to a supported public package repository and caches packages on demand.

## Pipeline pattern

```text
CodeBuild role
  → obtain short-lived CodeArtifact token
  → restore dependencies / publish package
```

The role commonly needs `codeartifact:GetAuthorizationToken`, `GetRepositoryEndpoint`, `ReadFromRepository`, and `sts:GetServiceBearerToken`; publishing needs package-write permissions.

## Exam traps

- CodeArtifact stores language packages; Amazon ECR stores container/OCI images.
- Authentication tokens are temporary; obtain a fresh token during the build instead of caching credentials.
- Cross-account access requires appropriate identity and resource policies; customer-managed KMS is important where cross-account decryption is required.

## Package lifecycle and governance

Use package versions and origin controls to manage provenance. An upstream/external connection can resolve dependencies; it does not automatically make every public package an approved release. Scope publishing separately from reading and retain versions needed for reproducibility.

## Official AWS references

- [CodeArtifact concepts](https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html)
- [Authentication tokens](https://docs.aws.amazon.com/codeartifact/latest/ug/tokens-authentication.html)
- [[CodeArtifact vs ECR vs S3 vs Image Builder]]
