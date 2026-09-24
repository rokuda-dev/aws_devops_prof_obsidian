---
tags: [aws, dop-c02, exam]
updated: 2026-09-19
read: false
---

# Domain Coverage and Service Map

| Domain | Weight | Task statements | Decision focus |
|---|---:|---|---|
| [[Domain 1 - SDLC Automation]] | 22% | 1.1–1.4 | Source, build, test, artifacts, and deployment strategies |
| [[Domain 2 - Configuration Management and IaC]] | 17% | 2.1–2.3 | IaC, multi-account governance, managed nodes, and automation |
| [[Domain 3 - Resilient Cloud Solutions]] | 15% | 3.1–3.3 | High availability, scaling, and automated recovery |
| [[Domain 4 - Monitoring and Logging]] | 15% | 4.1–4.3 | Collection, storage, analysis, auditing, and monitoring automation |
| [[Domain 5 - Incident and Event Response]] | 14% | 5.1–5.3 | Event processing, configuration response, and troubleshooting |
| [[Domain 6 - Security and Compliance]] | 17% | 6.1–6.3 | Identity at scale, data protection, security automation, and auditing |

## Cross-domain navigation

| Service family | Strongest exam association | Other domain relevance |
|---|---|---|
| [[AWS CodePipeline]], [[AWS CodeBuild]], [[AWS CodeDeploy]] | Domain 1 | Domain 5 deployment failures |
| [[AWS CloudFormation]], [[AWS CDK]], [[AWS SAM]], [[AWS CloudFormation StackSets]] | Domain 2; pipeline links in 1 | Domains 5–6 response/drift |
| [[AWS Systems Manager]], [[AWS Config]] | Domain 2 | Domains 4–6 inventory/remediation/compliance |
| [[Amazon ECS]], [[AWS Lambda]], [[Amazon API Gateway]] | Domain 1 | Domains 3–5 scaling/observation/recovery |
| [[Amazon CloudWatch]], [[AWS X-Ray]], [[AWS CloudTrail]] | Domain 1–2 supporting material | Domains 4–6 |
| [[AWS Organizations]], [[AWS Control Tower]], [[AWS Service Catalog]], [[AWS RAM]] | Domain 2 | Domain 6 governance |
| [[AWS AppConfig]], [[AWS Systems Manager Parameter Store]], [[AWS Secrets Manager]] | Domains 1–2 | Domains 5–6 safe configuration/security |
| [[Amazon EventBridge]], [[AWS Step Functions]] | Domain 2 | Domains 4–5 event automation |
| [[Amazon DynamoDB]], [[Amazon Aurora Global Database]], [[Amazon ElastiCache]] | Cross-domain additions | Domain 3 resilience |
| [[Amazon GuardDuty]], [[Amazon Inspector]], [[AWS Security Hub]], [[Amazon Detective]] | Domain 2 governance context | Domains 5–6 |

> [!important]
> Services are cross-domain. Select them from scenario requirements rather than treating their note location or strongest exam association as an ownership boundary.
