---
tags: [aws, dop-c02, audit]
updated: 2026-09-27
read: false
---

# Audit Concepts and Domains 2026-09-27

## Scope and method

Read all **39 Concepts pages and 7 Domains pages** in the working Markdown notebook. Checked the selected exam-deciding and stale-reference claims below against first-party AWS material accessed during this run. This is page coverage with targeted claim verification, not certification that every sentence, linked reference, regional feature matrix, or account-specific quota is current. Existing read flags and existing verification dates were preserved; this report records the new, narrower audit scope. No AWS resources were changed.

## Corrections

- [[RTO RPO SLA SLO and Error Budgets]]: **Return** was incorrect; both abbreviations use **Recovery**. Added direct AWS definition evidence.
- [[Domain 2 - Configuration Management and IaC]]: qualified Application Discovery Service as closed to new customers since November 7, 2025; AWS recommends AWS Transform for new discovery projects. [AWS availability notice](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).
- [[Domain 1 - SDLC Automation]]: expanded abbreviated Task 1.2 and 1.4 headings to match the official task statements.
- [[DDoS Mitigation and Attack Surface Reduction]]: added the March 26, 2026 WAF Anti-DDoS Managed Rule Group transition, preserving the distinction between legacy Shield L7 automation and Shield Advanced itself.

## Domain coverage

The [official DOP-C02 guide](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02.html) confirms weights **22%, 17%, 15%, 15%, 14%, 17%**. All 19 task statement mappings align. The roadmap deliberately uses short summaries rather than verbatim statements.

| Page read | Check and result | Evidence |
|---|---|---|
| [[All-Domain Study Roadmap]] | All six weights and 19 task mappings align | [Exam guide](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02.html) |
| [[Domain 1 - SDLC Automation]] | Weight/task structure checked; two headings expanded | [Domain 1](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain1.html) |
| [[Domain 2 - Configuration Management and IaC]] | Weight/task structure checked; availability qualification added | [Domain 2](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain2.html) |
| [[Domain 3 - Resilient Cloud Solutions]] | Weight/task structure checked; no blueprint correction needed | [Domain 3](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain3.html) |
| [[Domain 4 - Monitoring and Logging]] | Weight/task structure checked; no blueprint correction needed | [Domain 4](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain4.html) |
| [[Domain 5 - Incident and Event Response]] | Weight/task structure checked; no blueprint correction needed | [Domain 5](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain5.html) |
| [[Domain 6 - Security and Compliance]] | Weight/task structure checked; no blueprint correction needed | [Domain 6](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain6.html) |

## Concept coverage

“No correction” is limited to the stated checked claim, not every implementation detail on the page. The DDoS source retrieval limitation and historical/versioned sources are called out explicitly.

| Page read | Claim checked / result | First-party evidence |
|---|---|---|
| [[Artifact Management]] | CodeArtifact package repository versus image/stage artifacts | [AWS source](https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html) |
| [[AWS Distro for OpenTelemetry]] | X-Ray SDK/daemon maintenance began 2026-02-25; instrumentation migration | [AWS source](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-daemon-timeline.html) |
| [[Centralized Logging Architecture]] | Native centralization only copies logs arriving after rule creation | [AWS source](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html) |
| [[CI-CD Failure Triage and Parallel Actions]] | Pipeline stage/action structure; triage layering | [AWS source](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html) |
| [[CloudWatch Agent and Container Log Collection]] | Non-blocking ECS default; account/container override | [AWS source](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html) |
| [[CloudWatch Container Insights]] | ECS enhanced collection requires configuration; default disabled | [AWS source](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html) |
| [[CloudWatch Log Subscriptions and Cross-Account Destinations]] | Firehose cross-account/Region path; bounded throttling retries | [AWS source](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CrossAccountSubscriptions-Firehose-Account.html) |
| [[CloudWatch Logs Insights and Filter Patterns]] | Metric filters not retroactive; default zero requires ingestion and no dimensions | [AWS source](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) |
| [[CloudWatch Metric Streams]] | Firehose stream same account/Region; final destination may differ | [AWS source](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-setup-datalake.html) |
| [[CloudWatch Metrics Namespaces and Dimensions]] | Metric identity; statistic set percentile exceptions | [AWS source](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) |
| [[CloudWatch Synthetics]] | VPC canary networking and endpoint connectivity | [AWS source](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html) |
| [[DDoS Mitigation and Attack Surface Reduction]] | Added current WAF Anti-DDoS transition; confirmed CloudFront origin restriction pattern | [AWS transition](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-automatic-app-layer-response.html), [Origin access](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.html) |
| [[Dedicated Host Compliance and Licensing]] | License Manager host resource groups | [AWS source](https://docs.aws.amazon.com/license-manager/latest/userguide/host-resource-groups.html) |
| [[Deployment Strategy Matrix]] | Native ECS blue/green is a current choice | [AWS source](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-blue-green.html) |
| [[Disaster Recovery Strategies]] | Four recovery strategies; trade-offs and objectives | [AWS source](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_disaster_recovery.html) |
| [[Disaster Recovery Testing and Failback]] | Stopping FIS experiment does not universally undo actions | [AWS source](https://docs.aws.amazon.com/fis/latest/userguide/stop-experiment.html) |
| [[Domain 6 Identity and Access at Scale]] | AWSCodeCommitPowerUser v18 grants Create*/GitPush, omits DeleteRepository | [AWS source](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCodeCommitPowerUser.html) |
| [[Domain 6 Monitoring Auditing and Compliance]] | Inspector Classic support ended May 20, 2026 | [AWS source](https://docs.aws.amazon.com/pdfs/inspector/v1/userguide/inspector-ug.pdf) |
| [[Domain 6 Security Automation and Data Protection]] | Secrets reference API restrictions | [AWS source](https://docs.aws.amazon.com/systems-manager/latest/userguide/integration-ps-secretsmanager.html) |
| [[ECS and EKS Failure Triage]] | ECS service events/stopped reasons and host log distinction | [AWS source](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/stopped-task-errors.html) |
| [[Event Sources and Response Contracts]] | Supported EventBridge targets | [AWS source](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html) |
| [[Exposed Credential Response]] | Historical AWS RISK event example and containment-first sequence | [AWS source](https://aws.amazon.com/blogs/compute/automate-your-it-operations-using-aws-step-functions-and-amazon-cloudwatch-events//) |
| [[HTTPS Connectivity Troubleshooting]] | Stateful security-group behavior | [AWS source](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) |
| [[Incident Response Workflow and Evidence Preservation]] | Contain threat while preserving evidence | [AWS source](https://docs.aws.amazon.com/security-ir/latest/userguide/contain.html) |
| [[Lambda Deployment Validation Hooks]] | Lambda hook names, explicit callback and one-hour failure window | [AWS source](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html) |
| [[Log Lifecycle Security and Integrity]] | ALB enhanced logging notice; CloudTrail validation versus prevention | [AWS source](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html) |
| [[Metric Alarms and Anomaly Detection]] | Metric versus composite alarm semantics | [AWS source](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) |
| [[Monitoring Correlation Tracing and Dashboards]] | EventBridge trace metadata absent from replay/DLQ | [AWS source](https://aws.amazon.com/blogs/compute/using-aws-x-ray-tracing-with-amazon-eventbridge/) |
| [[Multi-Region Application Checklist]] | ECR replication scope and preexisting-image caveat | [AWS source](https://docs.aws.amazon.com/AmazonECR/latest/userguide/replication.html) |
| [[Resilience Framework and Dependency Isolation]] | Static stability architectural principle (versioned AWS source) | [AWS source](https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/rel_withstand_component_failures_static_stability.html) |
| [[RTO RPO SLA SLO and Error Budgets]] | Corrected Return to Recovery for both abbreviations | [AWS source](https://aws.amazon.com/disaster-recovery/faqs/) |
| [[S3 Permission Monitoring and Remediation]] | Bucket owner enforced disables ACLs | [AWS source](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) |
| [[Safe Event-Driven Remediation]] | cloudtrail-enabled is periodic; not an hourly guarantee | [AWS source](https://docs.aws.amazon.com/config/latest/developerguide/cloudtrail-enabled.html) |
| [[Scaling Metrics and Troubleshooting]] | Target tracking signal must respond appropriately to capacity | [AWS source](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html) |
| [[SDLC and CI-CD Fundamentals]] | Continuous delivery versus continuous deployment | [AWS source](https://aws.amazon.com/devops/continuous-delivery/) |
| [[Security Group Remediation and Access Safety]] | restricted-ssh has no allowed-CIDR parameter | [AWS source](https://docs.aws.amazon.com/config/latest/developerguide/restricted-ssh.html) |
| [[Stateless Applications and External Session State]] | Externalize sessions to resilient stores (versioned AWS source) | [AWS source](https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_mitigate_interaction_failure_stateless.html) |
| [[Systems Manager Incident Operations]] | OpsCenter migration and OpsItems; no built-in paging/on-call | [AWS source](https://docs.aws.amazon.com/incident-manager/latest/userguide/migration-opscenter.html) |
| [[Testing and Pipeline Placement]] | CodeBuild reports and deployment hook platform boundaries | [AWS source](https://docs.aws.amazon.com/codebuild/latest/userguide/test-reporting.html) |

## Limits and follow-up triggers

- DDoS whitepaper landing page returned no extractable body in this tool. Direct AWS WAF and CloudFront documentation subsequently verified the transition and origin-access claims; a complete Region eligibility matrix was not checked.
- The exposed-key event schema was recovered from AWS's historical 2017 article (the double-trailing-slash URL returned article content; the ordinary URL returned navigation only). This supports the historical example, not a guarantee of exhaustive detection or present-day account/event coverage. Validate real Health event samples before deployment.
- Static stability and statelessness searches returned versioned AWS Well-Architected pages. Used only for architectural principles, not present-day service availability or defaults.
- Deployment-strategy review checked native ECS blue/green availability; it does not independently verify every controller/load-balancer/Region combination. Container triage checked ECS evidence sources; EKS version/add-on compatibility was not exhaustively rechecked.
- IAM review checked the cited managed-policy actions; it was not an exhaustive policy-evaluation/security audit. Secrets review checked the Parameter Store reference API contract; no secret values were retrieved.
- No live AWS account, deployment, performance drill, or account-specific quota test was performed. Recovery timings remain objectives to measure, not guarantees.
- This audit did not bulk-refresh frontmatter verification dates because selected-claim review is narrower than full-page revalidation.
