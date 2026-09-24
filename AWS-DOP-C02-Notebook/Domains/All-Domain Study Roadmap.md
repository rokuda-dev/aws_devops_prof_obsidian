---
tags: [aws, certification, dop-c02, roadmap]
verified: 2026-09-19
read: false
---

# All-Domain Study Roadmap

Use this roadmap to apply the same study method to every domain: identify the task statement, isolate the deciding requirement, choose the service or pattern, and verify the operational safeguard.

## Domain 1 — SDLC Automation

**22%**. Build repeatable paths from source through testing, artifact promotion, and safe application or infrastructure deployment.

| Task | What to decide |
|---|---|
| 1.1 CI/CD pipelines | Source integration, orchestration, permissions, cross-account/Region artifacts, and execution behavior |
| 1.2 Automated testing | Test stage, test type, reports, quality gates, security scans, and failure handling |
| 1.3 Artifact management | Immutable versioning, registry/store, encryption, retention, replication, and provenance |
| 1.4 Deployment strategies | Platform-specific in-place, rolling, canary, linear, or blue/green behavior; hooks, alarms, and rollback |

High-value choices: CodePipeline versus build/deployment responsibilities; CodeArtifact versus ECR versus S3; Lambda alias, ECS, EC2/on-premises, API Gateway, and CloudFormation deployment mechanics; cross-account trust versus cross-Region artifact stores.

Study: [[Domain 1 - SDLC Automation]], [[SDLC and CI-CD Fundamentals]], [[Testing and Pipeline Placement]], [[Artifact Management]], [[Deployment Strategy Matrix]].

## Domain 2 — Configuration Management and IaC

**17%**. Define infrastructure, distribute governed configurations across accounts, and automate desired state without confusing visibility with enforcement.

| Task | What to decide |
|---|---|
| 2.1 IaC components | CloudFormation, CDK, or SAM; dependencies, parameters, change preview, drift, and deployment safety |
| 2.2 Multi-account management | StackSets, Organizations, Control Tower, Service Catalog, RAM, delegated administration, and guardrails |
| 2.3 Automation | Config detection, Systems Manager operations, EventBridge routing, Step Functions orchestration, and bounded remediation |

High-value choices: declarative versus programming-language versus serverless IaC; StackSets versus Service Catalog versus RAM; Config detection versus SSM remediation; EventBridge routing versus Step Functions workflows.

Study: [[Domain 2 - Configuration Management and IaC]], [[AWS CloudFormation, CDK, and SAM]], [[AWS CloudFormation StackSets]], [[AWS Systems Manager]], [[AWS Organizations and Control Tower]].

## Domain 3 — Resilient Cloud Solutions

**15%**. Decide separately how the workload survives component/AZ failure, scales under demand, and recovers from regional failure.

| Task | What to decide |
|---|---|
| 3.1 Highly available solutions | Multi-AZ compute/state, dependency isolation, health replacement, and compatible deployments |
| 3.2 Scalable solutions | Scaling signal, compute versus application capacity, caching, statelessness, and warmup/cooldown behavior |
| 3.3 Automated recovery | RTO/RPO, replication topology, promotion, traffic steering, orchestration, validation, and failback |

High-value choices: Multi-AZ versus multi-Region; RDS replica versus Aurora Global Database; DynamoDB global tables; Route 53 versus Global Accelerator; AWS Backup versus Elastic Disaster Recovery; golden AMIs and external state. Traffic failover never substitutes for data promotion or recovery validation.

Study: [[Domain 3 - Resilient Cloud Solutions]], [[Domain 3 Architecture Patterns]], [[Domain 3 Scenario Decisions]], [[Domain 3 Transcript Corrections]].

## Domain 4 — Monitoring and Logging

**15%**. Treat collection, transport/storage, query/analysis, notification, and remediation as separate design decisions.

| Task | What to decide |
|---|---|
| 4.1 Collection and storage | Producer/agent/driver, metric identity, cross-account delivery, archive/index destination, retention and encryption |
| 4.2 Audit and analysis | CloudTrail event scope, Config compliance, Logs Insights/Athena/OpenSearch choice, integrity and actor attribution |
| 4.3 Monitoring automation | Alarm/event source, exact schema or statistic, target authorization, failure handling, and outcome verification |

High-value choices: agent versus `awslogs`; metric filter versus subscription versus query; OAM federation versus copied central logs; CloudTrail management versus data events; alarms versus EventBridge rules; GuardDuty, Inspector and Macie boundaries.

Study: [[Domain 4 - Monitoring and Logging]], [[Domain 4 Architecture Patterns]], [[Domain 4 Scenario Decisions]], [[Domain 4 Transcript Corrections]].

## Domain 5 — Incident and Event Response

**14%**. Select the correct event source, apply a bounded and authorized change, and troubleshoot from evidence rather than one ambiguous symptom.

| Task | What to decide |
|---|---|
| 5.1 Event processing | CloudTrail, Config, CloudWatch alarm, Health, or native event; EventBridge routing; workflow and notification targets |
| 5.2 Configuration response | Live-state recheck, least-privilege remediation, idempotency, exception handling, evidence, and post-action verification |
| 5.3 Troubleshooting | Deployment/service events, logs, metrics, traces, network/TLS/IAM checks, container exit context, and rollback safety |

High-value choices: Step Functions versus SSM Automation versus Lambda; compliance state versus actor history; reactive exposed-key handling versus preventive scanning; WAF/Shield versus scaling; OpsCenter versus Fleet Manager; Lambda/ECS/EC2 CodeDeploy hook differences.

Study: [[Domain 5 - Incident and Event Response]], [[Domain 5 Architecture Patterns]], [[Domain 5 Scenario Decisions]], [[Domain 5 Transcript Corrections]].

## Domain 6 — Security and Compliance

**17%**. Build temporary least-privilege identity, layer preventive/detective/responsive controls, and retain verifiable security evidence.

| Task | What to decide |
|---|---|
| 6.1 IAM at scale | Workforce/workload/application identity, role trust, identity/resource/session policy, boundary/SCP ceilings, federation and ABAC |
| 6.2 Security and data protection automation | Prevention, classification, encryption/key custody, secret lifecycle, network controls, event routing and safe remediation |
| 6.3 Monitoring and auditing | CloudTrail/Config/GuardDuty/Inspector/Macie evidence, patch compliance, approved AMIs, centralized findings and audit retention |

High-value choices: Identity Center versus Roles Anywhere versus Cognito; SCP versus permissions boundary; KMS versus CloudHSM versus ACM versus Secrets Manager; WAF/Shield/Network Firewall/DNS Firewall; Config detection versus SSM remediation; current Inspector versus retired Inspector Classic.

Study: [[Domain 6 - Security and Compliance]], [[Domain 6 Architecture Patterns]], [[Domain 6 Scenario Decisions]], [[Domain 6 Transcript Corrections]].

> [!important]
> These summaries are usable on their own; the linked notes provide scenario depth, corrections, and source evidence. The notebook remains an exam-focused study aid rather than exhaustive service documentation.


## Individual task indexes

- [[Domain 1 - SDLC Automation]]
- [[Domain 2 - Configuration Management and IaC]]
- [[Domain 3 - Resilient Cloud Solutions]]
- [[Domain 4 - Monitoring and Logging]]
- [[Domain 5 - Incident and Event Response]]
- [[Domain 6 - Security and Compliance]]
