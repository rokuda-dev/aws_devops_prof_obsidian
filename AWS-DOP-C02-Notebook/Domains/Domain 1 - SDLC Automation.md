---
tags:
  - aws
  - certification
  - dop-c02
  - domain-1
  - cicd
domain: 1 - SDLC Automation
weight: 22%
verified: 2026-09-19
read: true
---

# Domain 1 — SDLC Automation

> [!summary]
> Domain 1 is **22% of scored content** and tests pipeline implementation, automated testing, artifact management, and platform-appropriate deployment strategies.

## Task 1.1 — Implement CI/CD pipelines

Know [[SDLC and CI-CD Fundamentals]], single- and multi-account patterns, repositories, builds, secrets, and deployment strategies.

Core services:

- [[AWS CodePipeline]] — orchestrates stages/actions, approvals, variables, and cross-Region actions
- [[AWS CodeCommit and CodeConnections]] — Git source and third-party repository access
- [[AWS CodeBuild]] — compile, test, scan, package, report
- [[AWS CodeDeploy]] — deployments to EC2/on-premises, ECS, and Lambda
- [[AWS AppConfig, Parameter Store, and Secrets Manager]] — runtime configuration and protected build/deployment values

## Task 1.2 — Integrate automated testing

Know where unit, integration, acceptance, UI, security, load, and performance tests belong. See [[Testing and Pipeline Placement]].

Exam cues:

- Pull request/merge triggers a build → source event plus CodeBuild
- Fail pipeline when tests fail → non-zero exit status
- Preserve test results → CodeBuild report group
- Deployment health gate → CloudWatch alarms and CodeDeploy rollback
- Distributed request validation → traces in [[Amazon CloudWatch, X-Ray, and OpenTelemetry]]

## Task 1.3 — Build and manage artifacts

| Artifact | Best first thought |
|---|---|
| Language package | [[AWS CodeArtifact]] |
| Container/OCI image | [[Amazon ECR and EC2 Image Builder#Amazon ECR]] |
| AMI or hardened container image pipeline | [[Amazon ECR and EC2 Image Builder#EC2 Image Builder]] |
| Generic pipeline artifact | Versioned/encrypted Amazon S3 artifact bucket |

See [[Artifact Management]].

## Task 1.4 — Deployment strategies

Match the mechanism to the compute platform:

- EC2/on-premises → [[AWS CodeDeploy#EC2 and on-premises]]
- ECS → [[Amazon ECS Deployments]]
- Lambda → [[AWS Lambda and API Gateway#Lambda versions, aliases, and deployments]]
- Managed application platform → [[AWS Elastic Beanstalk]]
- Infrastructure changes → [[AWS CloudFormation, CDK, and SAM]]

See [[Deployment Strategy Matrix]].

## High-value distinctions

1. CI builds and tests every integrated change; continuous delivery keeps changes deployable and may retain a production approval; continuous deployment removes that gate.
2. CodePipeline orchestrates. CodeBuild builds/tests. CodeDeploy deploys application revisions.
3. Multi-Region CodePipeline uses an artifact store in every action Region. Cross-account access additionally needs IAM role trust, S3 permissions, and a customer-managed KMS key policy.
4. Mutable deployment changes running hosts. Immutable deployment replaces them with newly built resources.
5. Store secrets in Secrets Manager or Parameter Store, not plaintext pipeline/build variables.
6. Deployment strategy names and capabilities are platform-specific.

## Additional high-value coverage

- [[Amazon CloudFront and Lambda@Edge]] — origin failover and edge request/response customization
- [[AWS Elastic Beanstalk]] — managed application environments and deployment policies
- [[AWS Lambda and API Gateway]] — serverless delivery surface
- [[Amazon ECS Deployments]] — rolling and blue/green container delivery
- [[AWS Systems Manager]] — deployment/fleet automation
- [[Amazon CloudWatch, X-Ray, and OpenTelemetry]] — validation, logs, metrics, alarms, and traces

## Source

[Official Domain 1 blueprint](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain1.html)


## Current platform distinctions

See [[Amazon ECS]] and [[ECS Native vs CodeDeploy Deployments]]: native ECS also supports blue/green, canary, and linear deployment. Explicit CodeDeploy scenarios remain valid.

The blueprint also includes EKS deployment concepts. Use [[Amazon EKS]], [[ECS and EKS Failure Triage]], and the platform-specific deployment notes; do not interpret this index as exhaustive coverage of every Kubernetes implementation detail or blueprint example.

See [[Notebook Provenance and Progress]] for source and scope limitations.
