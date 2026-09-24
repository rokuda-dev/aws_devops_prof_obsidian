---
tags: [aws, dop-c02, sources]
updated: 2026-09-18
read: false
---

# Imported Domain 1 Index

The attached Domain 1 index is preserved below as source text. Its original links refer to a vault not available in full; they are not active notebook links inside this fenced import. Consolidated links are in [[Domain 1 - SDLC Automation]].

```markdown
---
tags: [aws, certification, dop-c02, domain-1, cicd]
exam: AWS Certified DevOps Engineer - Professional (DOP-C02)
domain: 1 - SDLC Automation
weight: 22%
verified: 2026-09-18
---

# Domain 1 — SDLC Automation

> [!summary]
> Domain 1 is **22% of scored DOP-C02 content**. The current exam guide contains four task statements: CI/CD pipelines, automated testing, artifact management, and deployment strategies.

## Task statements

- [[Task 1.1 - Implement CI-CD Pipelines]]
- [[Task 1.2 - Integrate Automated Testing]]
- [[Task 1.3 - Build and Manage Artifacts]]
- [[Task 1.4 - Deployment Strategies]]

## Core concepts

- [[Concepts/SDLC and CI-CD Fundamentals]]
- [[Concepts/Testing Types and Pipeline Placement]]
- [[Concepts/Deployment Strategy Matrix]]

## AWS services to know

- [[Services/AWS CodePipeline]] — pipeline orchestration, stages/actions, manual approvals, cross-Region artifacts
- [[Services/AWS CodeBuild]] — builds, unit/integration tests, reports, artifacts, secret-backed environment variables
- [[Services/AWS CodeDeploy]] — EC2/on-prem, ECS, and Lambda deployment orchestration
- [[Services/AWS CodeArtifact]] — package repository
- [[Services/Amazon ECR]] — container/OCI artifact registry
- [[Services/EC2 Image Builder]] — managed AMI/container image pipelines
- [[Services/AWS Secrets Manager and Parameter Store]] — secrets/configuration used by builds and deployments
- [[Services/Amazon ECS Deployments]] — rolling, blue/green, linear, canary, CodeDeploy/external controllers
- [[Services/AWS Lambda Deployments]] — versions, aliases, canary/linear traffic shifting
- [[Services/AWS Systems Manager Automation]] — AMI automation, Run Command, Parameter Store
- [[Services/Observability - CloudWatch, X-Ray, OpenTelemetry]] — validation and health signals
- [[Services/Application Storage Patterns]] — S3/EBS/EFS/Storage Gateway decisions

## High-value exam distinctions

1. **SDLC ≠ CI/CD.** SDLC is the broader lifecycle; CI/CD automates and accelerates parts of it.
2. **Continuous delivery ≠ continuous deployment.** Delivery keeps every change deployable and can retain a manual production decision; deployment removes the human release gate.
3. **Artifact type drives repository choice.** Packages → CodeArtifact; container/OCI images → ECR; generic pipeline artifacts → S3.
4. **Deployment strategy is platform-specific.** Do not mix Elastic Beanstalk terms with CodeDeploy or ECS-native strategies.
5. **Secrets should not be plaintext pipeline variables.** Prefer Secrets Manager or Parameter Store integration through the consuming service.
6. **Multi-Region CodePipeline requires an artifact bucket per action Region.** CodePipeline copies input artifacts across Regions.
7. **Know what is legacy.** AWS CodeStar projects and OpsWorks Stacks should not be treated as current design choices; X-Ray SDKs/daemon are in maintenance mode.

## Source of truth

- AWS DOP-C02 Domain 1 exam guide: https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain1.html
- Full DOP-C02 exam guide: https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02.html

See [[Corrections/Skill Builder Transcript - Corrections and Updates]] for course-era statements that need qualification.
```

