---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# Domain 4 Transcript Corrections

## Evidence rule

The supplied transcript has been paraphrased and processed for tasks 4.1–4.3. Corrections use current official AWS sources checked on 2026-09-18. Product changes do not prove immediate exam refresh; retain historical wording only with an explicit caveat.

| Transcript statement/shortcut | Correct interpretation | Evidence/study note |
|---|---|---|
| CloudWatch has only metrics, logs and events | Useful historical model; current observability features are broader and EventBridge is the event-routing service | [[Amazon CloudWatch]], [[Amazon EventBridge]] |
| All AWS data lives in AWS/service namespaces | Namespaces organize metrics; not every AWS log/event is a namespaced metric | [[CloudWatch Metrics Namespaces and Dimensions]] |
| Agent default is “CW Agent” | Exact default namespace is CWAgent | [[CloudWatch Agent and Container Log Collection]] |
| Dimension is an instance name | Dimension is a name/value pair; InstanceId is distinct from a human Name tag | [[CloudWatch Metrics Namespaces and Dimensions]] |
| Send custom metric to CloudWatch Events | Publish into CloudWatch with PutMetricData/EMF or suitable log extraction | [[CloudWatch Metrics Namespaces and Dimensions]] |
| API parameter is “statistics value” | API field is StatisticValues; CLI --statistic-values | [[CloudWatch Metrics Namespaces and Dimensions]] |
| Aggregated publishing is always most cost-effective | Can reduce calls; cardinality, ingestion, resolution and chosen pipeline determine total cost | [[CloudWatch Metrics Namespaces and Dimensions]] |
| Statistic set supports arbitrary percentiles | Raw distribution needed except documented special cases | [[CloudWatch Metrics Namespaces and Dimensions]] |
| Kinesis is the only cross-account subscription destination | Current docs also support Firehose-backed logical destinations | [[CloudWatch Log Subscriptions and Cross-Account Destinations]] |
| Today's subscription filters cover future accounts | Add organization/OU scope or explicit future-account/group onboarding | [[Centralized Logging Architecture]] |
| A centralized view means a copied archive | OAM federation differs from Logs centralization/subscription copies | [[Cross-Account Observability vs Log Centralization]] |
| Native centralization includes historical logs | Processes new data after rule creation; plan historical backfill separately | [[Cross-Account Observability vs Log Centralization]] |
| Any Firehose input can be delivered directly to OpenSearch | Direct CloudWatch Logs → Firehose OpenSearch destination is currently unsupported | [[Amazon Data Firehose]] |
| Install CloudWatch agent to use ECS awslogs | awslogs handles container stdout/stderr; host agent is a separate telemetry mechanism | [[CloudWatch Agent and Container Log Collection]] |
| Attach ECS instance role for every launch type | Fargate log delivery uses execution role; FireLens destination calls use task role; EC2 role/agent behavior differs | [[CloudWatch Agent and Container Log Collection]] |
| Fargate versus EC2 changes whether centralized logs are possible | Both support configured centralized logging; deployment/IAM/host access differ | [[Amazon ECS]], [[AWS Fargate]] |
| awslogs writes directly to S3 | Use Logs subscription + Firehose, FireLens or another explicit route | [[Domain 4 Scenario Decisions]] |
| ALB logs are the same as container logs | Different producers/delivery configuration; combine in analysis if needed | [[Elastic Load Balancing]] |
| One universal ALB encryption rule covers every logging path | Legacy direct S3 supports SSE-S3; current enhanced integrations have separate requirements | [[Log Lifecycle Security and Integrity]] |
| ALB access logs account for every request exactly | Best-effort delivery; not an exhaustive accounting guarantee | [[Log Lifecycle Security and Integrity]] |
| Lambda must log S3 data API events | Enable CloudTrail data selectors; native trail delivery can send logs to archive/CloudWatch | [[AWS CloudTrail]] |
| CloudWatch Events cannot match API calls | EventBridge can match AWS API Call via CloudTrail events; trail/selectors must capture required activity | [[Amazon EventBridge]], [[AWS CloudTrail]] |
| “Amazon BPC” discovered fields | Amazon VPC flow logs; discovery depends on format/log class | [[CloudWatch Logs Insights and Filter Patterns]] |
| CloudTrail logs all activity by default | Default history is regional management events; data/network/Insights scopes require configuration | [[AWS CloudTrail]] |
| CloudTrail has only management and data event types | Current capabilities also include Insights and network activity events | [[AWS CloudTrail]] |
| Organization trail automatically logs every kind of event | Applies configured selectors/scope; object data events still need configuration | [[AWS CloudTrail]] |
| CloudTrail logs only its creation Region | Single-Region versus multi-Region trail setting controls scope; multi-Region collection does not change the service into a global-resource service | [[AWS CloudTrail]] |
| An alarm sends email on every policy event | Normal notifications occur on state changes; event routing fits per-event notification | [[Metric Alarms and Anomaly Detection]] |
| CodeDeploy rollback restores an arbitrary S3 policy | Deployment alarm rollback is distinct from resource-policy remediation | [[AWS CodeDeploy]] |
| Health Dashboard continuously detects application failure | AWS-impact events differ from system/instance checks and app SLIs | [[AWS Health]] |
| Launching a replacement gives single-instance HA | Recovery still has downtime/state/tenancy/capacity constraints | [[AWS Health]] |
| DevOps Monitoring Dashboard is a maintained solution | Current official notice says unsupported/no additional updates | [[Amazon QuickSight]] |
| Metric anomaly detection replaces security-log streaming | It evaluates numeric metric behavior, not raw log collection or complete intrusion detection | [[Metric Alarms and Anomaly Detection]], [[Amazon GuardDuty]] |
| GuardDuty findings need Firehose to reach S3 | Native findings export to S3 is available with permissions/KMS configuration | [[Amazon GuardDuty]] |
| Macie is a generic anomaly service | Sensitive-data discovery/S3 policy risk; not generic numeric anomaly or malware detection | [[Amazon Macie]] |
| API Gateway tracing means every API type supports it identically | Verify REST API X-Ray support; do not assume HTTP/WebSocket parity | [[Monitoring Correlation Tracing and Dashboards]] |
| EventBridge trace header is an ordinary replayable event field | Supported context is internal metadata; archive replay/DLQ do not preserve it as the original trace | [[Monitoring Correlation Tracing and Dashboards]] |
| CloudTrail integrity prevents tampering | Digests enable detection/validation; storage/access protection prevents changes | [[Log Lifecycle Security and Integrity]] |
| Integrity feature protects every application file | Applies to CloudTrail-delivered log/digest evidence, not arbitrary files | [[Log Lifecycle Security and Integrity]] |
| Every SSH login should trigger termination | Confirm compromise/approved access, preserve evidence and scope response | [[Safe Event-Driven Remediation]] |
| Low utilization means terminate every instance | Evaluate workload/state/owners/schedules; ASG replacement can negate savings | [[AWS Trusted Advisor]] |
| Health metric filter can directly inspect bus events | Metric filters operate on log groups; route/log first if needed, or notify directly | [[AWS Health]] |
| Resource data sync is only Inventory | Inventory and Explorer sync types exist; neither substitutes for Health event notifications | [[AWS Systems Manager]] |
| EKS has only two automatic scaling products | CA/Karpenter are node mechanisms; HPA and current Auto Mode are separate distinctions | [[Amazon EKS]] |
| Config CloudTrail rule always checks hourly | Periodic rule; verify configured frequency rather than assuming one hour | [[AWS Config]] |
| Config rule-change event equals StopLogging API event | Different triggers and latency; choose the actual API event for prompt change detection | [[Safe Event-Driven Remediation]] |
| SQS health-checks workers before pulling work | Consumers/integrations poll and control processing; SQS is not an ALB-style worker health checker | [[Amazon SQS]] |
| OpsWorks Chef configure lifecycle is a current solution | OpsWorks Stacks retired May 26, 2024; use supported desired-state/configuration tooling | [[AWS Systems Manager]] |

## Additional blueprint/current-product notes

Metric streams are explicitly in the official task 4.1 even though the transcript does not explain them. Inspector assessment-template wording in the guide is legacy Classic terminology; Inspector Classic ended support May 20, 2026. Current Inspector is a different continuous-assessment service.

See [[Domain 4 Transcript Coverage]], [[Domain 4 Official Sources]], [[Common Traps and Current Corrections]].
