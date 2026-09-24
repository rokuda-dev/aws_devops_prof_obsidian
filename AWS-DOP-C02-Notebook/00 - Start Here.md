---
title: AWS DevOps Professional Service Notebook
aliases:
  - DOP-C02 Service Notebook
tags:
  - aws
  - certification
  - dop-c02
  - moc
verified: 2026-09-20
read: false
---

# AWS DevOps Professional Service Notebook

> [!important] Purpose
> A service-centric Obsidian notebook for the AWS Certified DevOps Engineer – Professional exam. Domain pages explain what the blueprint tests; canonical service notes hold reusable details and exam distinctions.

## Exam blueprint

| Domain | Weight | Task statements |
|---|---:|---|
| [[Domain 1 - SDLC Automation]] | 22% | 1.1–1.4 |
| [[Domain 2 - Configuration Management and IaC]] | 17% | 2.1–2.3 |
| [[Domain 3 - Resilient Cloud Solutions]] | 15% | 3.1–3.3 |
| [[Domain 4 - Monitoring and Logging]] | 15% | 4.1–4.3 |
| [[Domain 5 - Incident and Event Response]] | 14% | 5.1–5.3 |
| [[Domain 6 - Security and Compliance]] | 17% | 6.1–6.3 |

## Start with these

- [[Service Selection Matrix]] — requirement → best first service
- [[High-Value Exam Patterns]] — recurring architectures
- [[Common Traps and Current Corrections]] — plausible distractors and outdated course statements
- [[Rapid Review]] — final-pass memory anchors
- [[All-Domain Study Roadmap]] — a consistent task-and-decision map for all six domains

## Core mental model

```text
Source → Build/Test → Artifact → Deploy → Observe → Govern/Remediate
```

| Function | Primary services |
|---|---|
| Source integration | [[AWS CodeCommit and CodeConnections]] |
| Orchestration | [[AWS CodePipeline]] |
| Build and test | [[AWS CodeBuild]] |
| Package registry | [[AWS CodeArtifact]] |
| Container/image artifacts | [[Amazon ECR and EC2 Image Builder]] |
| Application deployment | [[AWS CodeDeploy]] |
| Infrastructure deployment | [[AWS CloudFormation, CDK, and SAM]] |
| Runtime platforms | [[Amazon ECS Deployments]], [[AWS Lambda and API Gateway]], [[AWS Elastic Beanstalk]] |
| Configuration and fleet operations | [[AWS Systems Manager]], [[AWS AppConfig, Parameter Store, and Secrets Manager]] |
| Governance and compliance | [[AWS Organizations and Control Tower]], [[AWS Config]], [[AWS Service Catalog and RAM]] |
| Health signals | [[Amazon CloudWatch, X-Ray, and OpenTelemetry]] |

## Conventions

- **Exam cue** means wording that strongly suggests a service or feature.
- **Trap** means a plausible but incomplete or incorrect answer.
- Facts are verified against [[Official AWS Sources]].
- A service can appear in several domains; its canonical detail lives in one service note.
- Every note has a Boolean `read` property. Version 1.4.5 preserves the reviewed/unreviewed state from the edited v1.4.4 task archive; toggle it as you continue studying.


## Open in Obsidian

Extract the ZIP, then choose **Open folder as vault** and select the extracted AWS-DOP-C02-Service-Notebook folder. Start here; no plugins are required for the core Markdown/wiki links. The vault also retains the configured **Mark as Read** community plugin (`explorer-property-attributes`) for read-state display and toggling.

## Coverage and validation

- [[Service Index]] — all canonical service notes.
- [[Domain Coverage and Service Map]] — completed scope and explicit coverage limits.
- [[Notebook Provenance and Progress]] — exact inputs and limitations.
- [[Verification Ledger]] — current-fact checks.
- [[Notebook Changelog]] — version history.

> [!warning]
> This is exam-focused study coverage, not exhaustive documentation for every blueprint example, service, or feature. Use the official exam guide and current AWS documentation to confirm scope and changing product behavior.

## Domain 1 study path

Start at [[Domain 1 - SDLC Automation]], then review [[SDLC and CI-CD Fundamentals]], [[Testing and Pipeline Placement]], [[Artifact Management]], and [[Deployment Strategy Matrix]]. Use [[High-Value Exam Patterns]] and [[Service Selection Matrix]] to compare pipeline, artifact, and deployment choices.

## Domain 2 study path

Start at [[Domain 2 - Configuration Management and IaC]], then review [[AWS CloudFormation, CDK, and SAM]], [[AWS CloudFormation StackSets]], [[AWS Systems Manager]], and [[AWS Organizations and Control Tower]]. Separate infrastructure definition, multi-account governance, configuration state, and event-driven automation.

## Domain 3 study path

Read [[Domain 3 - Resilient Cloud Solutions]], then [[Domain 3 Scenario Decisions]], [[Domain 3 Architecture Patterns]], and [[Domain 3 Transcript Corrections]]. Recovery anchors: [[RTO RPO SLA SLO and Error Budgets]], [[Disaster Recovery Strategies]], [[Disaster Recovery Testing and Failback]].

## Domain 4 study path

Start at [[Domain 4 - Monitoring and Logging]], then [[Domain 4 Scenario Decisions]], [[Domain 4 Architecture Patterns]], and [[Domain 4 Transcript Corrections]]. Study collection → storage/search → notification → safe response as separate responsibilities.

## Domain 5 study path

Start at [[Domain 5 - Incident and Event Response]], then [[Domain 5 Scenario Decisions]], [[Domain 5 Architecture Patterns]], and [[Domain 5 Transcript Corrections]]. Keep prevention, detection, routing, remediation and evidence separate. Troubleshooting anchors: [[Incident Response Workflow and Evidence Preservation]], [[HTTPS Connectivity Troubleshooting]], [[CI-CD Failure Triage and Parallel Actions]].

## Domain 6 study path

Start at [[Domain 6 - Security and Compliance]], then [[Domain 6 Scenario Decisions]], [[Domain 6 Architecture Patterns]], and [[Domain 6 Transcript Corrections]]. Use [[Domain 6 Identity and Access at Scale]], [[Domain 6 Security Automation and Data Protection]], and [[Domain 6 Monitoring Auditing and Compliance]] as task-level reviews.
