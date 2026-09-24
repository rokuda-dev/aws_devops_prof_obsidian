---
tags:
  - aws
  - dop-c02
  - exam
updated: 2026-09-19
read: true
---

# Service Selection Matrix

## Cross-domain quick selection

| Requirement                               | Best first thought                                                 |
| ----------------------------------------- | ------------------------------------------------------------------ |
| Pipeline orchestration                    | [[AWS CodePipeline]]                                               |
| Compile/test/scan/package                 | [[AWS CodeBuild]]                                                  |
| Managed application deployment            | [[AWS CodeDeploy]]                                                 |
| AWS-managed Git                           | [[AWS CodeCommit]]                                                 |
| External Git provider authorization       | [[AWS CodeConnections]]                                            |
| Language packages                         | [[AWS CodeArtifact]]                                               |
| Container/OCI registry                    | [[Amazon ECR]]                                                     |
| Build/test/distribute AMIs                | [[EC2 Image Builder]]                                              |
| Declarative IaC                           | [[AWS CloudFormation]]                                             |
| Programming-language IaC                  | [[AWS CDK]]                                                        |
| Serverless IaC                            | [[AWS SAM]]                                                        |
| Stack deployment across accounts/Regions  | [[AWS CloudFormation StackSets]]                                   |
| Container orchestration                   | [[Amazon ECS]]                                                     |
| Controlled Lambda canary                  | [[AWS Lambda]] alias + CodeDeploy                                  |
| API layer canary                          | REST API feature in [[Amazon API Gateway]]                         |
| Managed app platform                      | [[AWS Elastic Beanstalk]]                                          |
| Runtime config/feature rollout            | [[AWS AppConfig]]                                                  |
| Hierarchical encrypted parameters         | [[AWS Systems Manager Parameter Store]]                            |
| Credential lifecycle/rotation             | [[AWS Secrets Manager]]                                            |
| Resource configuration/history/compliance | [[AWS Config]]                                                     |
| Actor/API audit                           | [[AWS CloudTrail]]                                                 |
| Metrics/logs/alarms                       | [[Amazon CloudWatch]]                                              |
| Distributed request trace                 | [[AWS X-Ray]] + [[AWS Distro for OpenTelemetry]]                   |
| Fleet commands / interactive access       | [[AWS Systems Manager]] Run Command / Session Manager              |
| Desired host state / patches              | SSM State Manager / Patch Manager                                  |
| Operational runbook                       | SSM Automation                                                     |
| Multi-step orchestration                  | [[AWS Step Functions]]                                             |
| Event routing                             | [[Amazon EventBridge]]                                             |
| Custom event handler                      | [[AWS Lambda]]                                                     |
| Permission cap across accounts            | [[AWS Organizations]] SCP                                          |
| Standardized account vending              | [[AWS Control Tower]]                                              |
| Governed self-service stacks              | [[AWS Service Catalog]]                                            |
| Share an existing supported resource      | [[AWS RAM]]                                                        |
| Central Config visibility                 | [[AWS Config#Config aggregators]]                                  |
| Threat / vulnerability / investigation    | [[Amazon GuardDuty]] / [[Amazon Inspector]] / [[Amazon Detective]] |
| Central security risk workflow            | [[AWS Security Hub]]                                               |
| Item-change automation                    | [[Amazon DynamoDB]] Streams + Lambda                               |
| Multi-active global NoSQL                 | DynamoDB Global Tables                                             |
| Global relational read locality/DR        | [[Amazon Aurora Global Database]]                                  |
| Protect selected sensitive POST fields    | [[CloudFront Field-Level Encryption]]                              |
| Disposable instances with shared sessions | [[Stateless Applications and External Session State]]              |

> [!exam]
> “Best first thought” is not a universal answer. Read the account/Region scope, platform, consistency, downtime, IAM, cost, and operational-effort requirements before eliminating alternatives.

## Domain 1 — SDLC automation

| Requirement | Best first thought | Do not confuse with |
|---|---|---|
| Orchestrate source, build, test, approval, and deployment stages | [[AWS CodePipeline]] | [[AWS CodeBuild]], which executes build/test commands |
| Compile, test, scan, or package | [[AWS CodeBuild]] | A deployment controller |
| Store language packages or container images | [[AWS CodeArtifact]] or [[Amazon ECR]] | A pipeline artifact bucket used for action handoff |
| Deploy to EC2/on-premises, Lambda, or ECS with CodeDeploy semantics | [[AWS CodeDeploy]] | CloudFormation infrastructure deployment |
| Shift Lambda traffic gradually | Published version + alias + CodeDeploy | Editing `$LATEST` without controlled traffic shifting |
| Preview an infrastructure update | CloudFormation change set | Proof that execution will succeed |

## Domain 2 — configuration management and IaC

| Requirement | Best first thought | Do not confuse with |
|---|---|---|
| Declarative, language-based, or serverless IaC | [[AWS CloudFormation]], [[AWS CDK]], or [[AWS SAM]] | Runtime configuration rollout |
| Deploy stacks across accounts and Regions | [[AWS CloudFormation StackSets]] | [[AWS RAM]], which shares supported existing resources |
| Govern approved self-service infrastructure | [[AWS Service Catalog]] | Account vending through Control Tower Account Factory |
| Record resource configuration and evaluate compliance | [[AWS Config]] | CloudTrail actor/API history |
| Maintain fleet state or execute operational runbooks | [[AWS Systems Manager]] State Manager or Automation | Session Manager interactive access |
| Route events or coordinate multi-step work | [[Amazon EventBridge]] or [[AWS Step Functions]] | Treating event delivery as proof of remediation success |

## Domain 3 — resilient solutions

| Requirement | Best first thought | Do not confuse with |
|---|---|---|
| AZ-resilient relational database | RDS Multi-AZ or an appropriate Aurora regional topology | An ordinary read replica treated as an automatic standby |
| Cross-Region relational reads and managed recovery | [[Amazon Aurora Global Database]] | Multi-active independent relational writers |
| Cross-Region RDS DR for a supported engine | Cross-Region read replica + explicit promotion/runbook | Route 53 automatically promoting the replica |
| Multi-Region active-active NoSQL | DynamoDB global tables with required MREC/MRSC semantics | DAX, which is a regional read cache |
| Static/media edge delivery | [[Amazon CloudFront]] | S3 replication, which creates object copies rather than an edge cache |
| Static IP global traffic entry | [[AWS Global Accelerator]] with supported regional endpoints | Direct API Gateway or RDS endpoint attachment |
| DNS-based regional routing | [[Amazon Route 53]] health/latency/failover routing | Application or database recovery orchestration |
| Server-based disaster recovery | [[AWS Elastic Disaster Recovery]] | Backup-only restore without continuous server replication |
| Central backup policy and supported copy | [[AWS Backup]] | Proof that the application can actually recover |
| Fast EC2 fleet replacement | Golden AMI + launch-template version + ASG rollout | Merely changing an AMI parameter |
| Pod scaling versus node capacity | HPA versus Karpenter/Cluster Autoscaler/EKS Auto Mode | Fargate automatically choosing replica count |
| Coordinated regional recovery actions | ARC Region switch, Step Functions, or SSM Automation as requirements dictate | Traffic control alone |

See [[Domain 3 Scenario Decisions]] for requirement-sensitive choices.

## Domain 4 — monitoring and logging

| Requirement | Best first thought | Do not confuse with |
|---|---|---|
| Guest logs, memory, disk, or process metrics | CloudWatch agent | Default EC2 metrics |
| ECS container stdout/stderr | `awslogs` driver; FireLens for deliberate routing/transformation | Host CloudWatch agent as a prerequisite for awslogs |
| Count patterns in logs | CloudWatch Logs metric filter | Logs Insights interactive query |
| Forward matching log records | CloudWatch Logs subscription | Metric filter, which emits metrics rather than raw records |
| Query archived logs in S3 with SQL | [[Amazon Athena]] | [[Amazon OpenSearch Service]] indexed search |
| Federated cross-account CloudWatch view | OAM cross-account observability | Copied centralized log archive |
| Copy new organization logs centrally | CloudWatch Logs centralization or organization-aware subscription design | Historical backfill occurring automatically |
| Export metric updates continuously | CloudWatch metric streams → Firehose | PutMetricData, which publishes custom metrics |
| Audit S3 object APIs | CloudTrail data events | Default management-event history |
| Detect resource configuration noncompliance | [[AWS Config]] rule | CloudTrail actor history |
| Detect supported threat activity | [[Amazon GuardDuty]] | Inspector vulnerabilities or Macie sensitive-data discovery |
| Notify about AWS maintenance/impact | [[AWS Health]] → EventBridge | CloudWatch metric filter against an event bus |

See [[Domain 4 Scenario Decisions]] for collection, analysis, and response pipelines.

## Domain 5 — incident and event response

| Requirement | Best first thought | Do not confuse with |
|---|---|---|
| React to an AWS API call | CloudTrail-captured event → EventBridge | Config compliance-change event |
| React to numeric threshold | CloudWatch alarm | EventBridge as metric storage |
| React to AWS service maintenance | AWS Health → EventBridge | Polling CloudWatch for Health events |
| Repair a noncompliant resource | Config evaluation → SSM Automation or scoped Lambda | Aggregator as enforcement engine |
| Stateful response with retries/branches/approval | [[AWS Step Functions]] | Lambda-only ad hoc orchestration |
| Fleet operational runbook | SSM Automation | Run Command interactive access |
| Investigate an operational issue | Systems Manager OpsCenter/OpsItem | Fleet Manager node administration |
| Validate a Lambda deployment | CodeDeploy BeforeAllowTraffic/AfterAllowTraffic hooks + alarms | ECS AfterAllowTestTraffic hook |
| Parallel independent pipeline actions | Equal CodePipeline `runOrder` values in the same stage | Pipeline execution mode |
| Diagnose ECS failure | Service events + stopped reason/exit code + logs + target health/IAM/network | Exit code alone |
| Diagnose EKS failure | Pod/node events, logs, probes, resources, configured observability | Container Insights as an autoscaler |
| Reduce public administrative exposure | Session Manager + network/IAM hardening | SSM as a DDoS filtering service |

See [[Domain 5 Scenario Decisions]] and [[Detection vs Enforcement vs Remediation]].

## Domain 6 — security and compliance

| Requirement | Best first thought | Do not confuse with |
|---|---|---|
| Workforce access across accounts | [[AWS IAM Identity Center]] permission sets and temporary role sessions | IAM users with permanent credentials |
| Temporary AWS access for external workloads | [[AWS IAM Roles Anywhere]] or supported federation | Mandatory long-lived access keys |
| Application users and optional temporary AWS credentials | Cognito user pool + identity pool when direct AWS access is needed | User pool alone issuing AWS credentials |
| Maximum permissions across organization accounts | Organizations SCP | A policy that grants the requested action |
| Maximum permissions for an IAM principal | Permissions boundary | Session policy or resource policy |
| Analyze unintended external access | [[IAM Access Analyzer]] | GuardDuty runtime threat detection |
| Discover sensitive data in S3 | [[Amazon Macie]] | A synchronous ingestion-blocking or redaction service |
| Cryptographic key management integrated with AWS services | [[AWS Key Management Service]] | Secrets Manager credential lifecycle or ACM certificates |
| Dedicated customer-controlled HSM cluster | [[AWS CloudHSM]] | KMS multi-tenant managed key service |
| Public/private TLS certificate lifecycle | [[AWS Certificate Manager]] / [[AWS Private CA]] | Storage of database passwords |
| Rotating database/API secrets | [[AWS Secrets Manager]] | Parameter Store static configuration |
| Hierarchical encrypted configuration | [[AWS Systems Manager Parameter Store]] SecureString | Managed rotation by default |
| Organization-scale supported security policies | [[AWS Firewall Manager]] | A firewall that automatically covers every resource/Region |
| HTTP(S) request filtering | [[AWS WAF]] | Shield DDoS protection or Network Firewall routed inspection |
| Routed VPC network inspection | [[AWS Network Firewall]] | Security groups or DNS Firewall |
| DNS-domain filtering for Route 53 Resolver | [[Amazon Route 53 Resolver DNS Firewall]] | HTTP request inspection |
| Vulnerability management | Current [[Amazon Inspector]] | Inspector Classic agents/assessment templates |
| Central findings/posture workflow | [[AWS Security Hub]] | The original detector or remediation engine |
| Hybrid OS patching and compliance | SSM managed nodes + Patch Manager | Config installing patches |

See [[Domain 6 Scenario Decisions]] and [[KMS vs CloudHSM vs ACM vs Secrets Manager]].
