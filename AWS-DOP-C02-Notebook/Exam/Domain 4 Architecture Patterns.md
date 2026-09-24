---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# Domain 4 Architecture Patterns

| Requirement | Pattern | Critical configuration |
|---|---|---|
| OS/app file logs and guest metrics | CloudWatch agent → configured logs/custom metrics | Node identity, paths, CWAgent/custom namespace, retention and connectivity |
| Payment/refund counts per minute | PutMetricData or suitable EMF/log filters → CloudWatch alarm → SNS | Correct metric/dimensions, Sum, period, missing data and confirmed notification |
| Indexed compliance logs across accounts | CloudWatch subscriptions → authorized central Kinesis → processor → OpenSearch | Future-account onboarding, source identity, individual documents and lag/error handling |
| Central archive with SQL analysis | CloudWatch subscription → Firehose → S3 → Athena | Payload format, delivery role, partition/schema, encryption and lifecycle |
| Native central CloudWatch log copy | Organization/OU centralization rules → destination log groups | New data only, source/Region scope, encryption and destination retention |
| Federated operational visibility | OAM monitoring/source account setup | Regional links/access; not an independent copied archive |
| ECS container + ALB logs in S3 | awslogs → Logs subscription → Firehose → S3; separately configure ALB logging | Execution-role/driver setup, buffering, ALB destination-specific permissions |
| Audit confidential S3 object access | CloudTrail data selectors → protected archive and optional CloudWatch Logs | GetObject/PutObject/DeleteObject data events explicitly enabled |
| Notify on bucket-policy changes | CloudTrail → Logs metric filter → alarm → SNS, or API event → EventBridge → target | Distinguish event notification from supported remediation |
| Scheduled EC2 maintenance notification | Health event → EventBridge → SNS | Exact service/category/code, organizational scope, confirmed subscription |
| Detect suspicious activity | GuardDuty in required accounts/Regions with delegated administration | Correct protection plans; scoped finding response and export |
| Detect resource noncompliance | Config rule → evaluation → supported Automation remediation | Trigger frequency, source recording, live-state recheck and safe permissions |
| StopLogging detection/recovery | Protected audit event → precise EventBridge rule → authorized handler → verify | Periodic Config assurance as fallback; handle deletion/selector/key drift separately |
| ASG membership-dependent config | Lifecycle/state events → current-membership reconciliation → SSM Run Command/State Manager | Hook completion where used, managed target, atomic validated config |
| Correlate dependency failures | Structured log IDs + compatible traces + metrics → ServiceLens/analysis | Sampling, propagation, time alignment and actual instrumentation |
| Export metric updates | CloudWatch metric stream → same-account/Region Firehose → supported destination | Namespace/format selection and independent delivery monitoring |

## Operational rule

Collection, search, notification and remediation are four separate capabilities. A dashboard does not enforce compliance; a finding does not authorize deletion; an alarm does not automatically roll back every changed resource.

Tasks 4.1–4.3. See [[Domain 4 Scenario Decisions]], [[Domain 4 Transcript Corrections]], [[Domain 4 Official Sources]].
