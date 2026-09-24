---
tags: [aws, dop-c02, domains]
updated: 2026-09-19
read: false
---

# Domain 4 - Monitoring and Logging

> [!summary]
> Domain 4 is 15% of the exam and tests telemetry collection and storage, evidence analysis, auditing, and monitoring automation.

## Task 4.1 — Configure the collection, aggregation, and storage of logs and metrics.

Identify the producer, required latency, account/Region scope, retention, query pattern, and security boundary. EC2 guest logs and memory/disk metrics normally need the CloudWatch agent or another explicit publisher. ECS container stdout/stderr can use `awslogs`; FireLens is a deliberate alternative for routing and transformation. ALB access logs, CloudTrail records, VPC Flow Logs, and application logs are separate producers with different configuration and completeness guarantees.

For cross-account designs, distinguish linked observation from copied data. OAM provides federated CloudWatch visibility; Logs centralization or subscription destinations copy new records to a monitoring/central account; Firehose commonly delivers buffered data to S3; OpenSearch supports indexed search; Athena queries structured data in S3. Plan future-account onboarding, encryption, delivery-error monitoring, retention, and historical backfill.

Metric identity is namespace + name + dimensions. Choose the correct statistic and period; `Sum` and `SampleCount` answer different questions. Metric streams export updates, while PutMetricData/EMF publish custom metrics.

Core services: [[Amazon CloudWatch]], [[AWS CloudTrail]], [[Amazon S3]], [[Amazon Kinesis Data Streams]], [[Amazon Data Firehose]], [[Amazon OpenSearch Service]], [[Amazon Athena]].

Study: [[CloudWatch Metrics Namespaces and Dimensions]], [[CloudWatch Agent and Container Log Collection]], [[CloudWatch Log Subscriptions and Cross-Account Destinations]], [[Centralized Logging Architecture]], [[CloudWatch Logs Insights and Filter Patterns]], [[CloudWatch Metric Streams]], [[Log Lifecycle Security and Integrity]], [[Cross-Account Observability vs Log Centralization]], [[Log Subscription vs Metric Filter vs EventBridge Rule]].

## Task 4.2 — Audit, monitor, and analyze logs and metrics to detect issues.

Match the evidence to the question. CloudTrail attributes AWS API activity to an actor/session; Config records supported resource configuration and evaluates compliance; CloudWatch provides workload metrics/logs/alarms; traces correlate supported request paths. CloudTrail event history is not an all-purpose audit archive: ordinary S3 object activity requires data-event selectors, and trail delivery/integrity/storage protections must be configured.

Use Logs Insights for interactive CloudWatch Logs analysis, Athena for SQL over S3 data, and OpenSearch when indexed search/analytics is justified. Static, anomaly-detection, and composite alarms solve different signal problems. GuardDuty detects supported threat activity, Inspector manages supported vulnerability findings, and Macie discovers sensitive S3 data and policy risk; none is a generic substitute for the others.

Core services: [[Amazon CloudWatch]], [[AWS X-Ray]], [[AWS Distro for OpenTelemetry]], [[AWS Config]], [[Amazon GuardDuty]], [[Amazon Inspector]], [[Amazon Macie]], [[AWS Health]].

Study: [[Metric Alarms and Anomaly Detection]], [[Monitoring Correlation Tracing and Dashboards]], [[Logs Insights vs Athena vs OpenSearch]], [[Static vs Anomaly vs Composite Alarms]]. Supporting consumers include [[Amazon QuickSight]], [[Amazon API Gateway]], and [[AWS Lambda]].

## Task 4.3 — Automate monitoring and event management of complex environments.

Choose the trigger before the response. CloudWatch alarms represent numeric conditions; EventBridge matches supported service/API/state events; Config emits compliance evaluations; Health publishes AWS-impact events. A metric filter operates on log groups, not directly on an event bus. Match the real schema, account and Region scope, and expected latency.

Then design a bounded response: authorize the target narrowly, recheck live state, make actions idempotent, handle retries and duplicates, route failures, preserve evidence, and verify the outcome. Lambda is suitable for focused custom handling, Step Functions for stateful branching/retries/approval, and Systems Manager Automation for operational runbooks. A dashboard, finding, alarm, or accepted target invocation is not itself remediation.

Core services: [[Amazon EventBridge]], [[AWS Systems Manager]], [[AWS Lambda]], [[AWS Step Functions]], [[AWS Config]], [[Amazon SNS]], [[AWS Trusted Advisor]].

Study: [[Safe Event-Driven Remediation]], [[AWS Health vs CloudWatch vs Trusted Advisor]], [[Domain 4 Architecture Patterns]]. Workload targets may include [[Amazon EC2 Auto Scaling]], [[Amazon ECS]], [[Amazon EKS]], [[Amazon SQS]], and [[AWS CodeDeploy]].

## Sources and deeper review

- [Official Domain 4 task statements](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain4.html)
- [[Domain 4 Scenario Decisions]]
- [[Domain 4 Architecture Patterns]]
- [[Domain 4 Transcript Corrections]]
- [[Notebook Provenance and Progress]]
- [[Domain 4 Official Sources]]
- [[Domain 4 Transcript Coverage]]
