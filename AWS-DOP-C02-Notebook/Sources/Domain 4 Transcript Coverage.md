---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# Domain 4 Transcript Coverage

## Input and status

The user supplied three Domain 4 transcript sections and seven AWS resource links. All supplied sections for tasks 4.1–4.3 have been processed. Domain 4 has 15% exam weight.

| Supplied section | Topics processed | Main destinations |
|---|---|---|
| 4.1 collection/aggregation/storage | CloudWatch/agent/namespace/dimensions; transactions/statistic sets; subscriptions/cross-account pipelines; ECS/ALB logging; S3 audit/search; retention and CloudTrail scope | [[CloudWatch Metrics Namespaces and Dimensions]], [[CloudWatch Agent and Container Log Collection]], [[Centralized Logging Architecture]], [[AWS CloudTrail]] |
| 4.2 audit/analysis | Baselines/correlation; dashboards; policy-change alerts; single-instance recovery; Config compliance; CI/CD BI; anomalies; GuardDuty/Macie; X-Ray integrations | [[Monitoring Correlation Tracing and Dashboards]], [[Metric Alarms and Anomaly Detection]], [[Domain 4 Scenario Decisions]], [[Amazon GuardDuty]], [[Amazon Macie]] |
| 4.3 automation | Signed digests; login/utilization response; Health notifications; ASG/DynamoDB/config updates; ECS/EKS scaling links; log processing; Config/StopLogging; health checks; shared configuration | [[Log Lifecycle Security and Integrity]], [[Safe Event-Driven Remediation]], [[AWS Health]], [[AWS Systems Manager]], [[Amazon SQS]] |
| Seven additional resources | Subscriptions, GuardDuty, CloudTrail, Config managed rules, Health events, CodeDeploy events, OpenSearch | [[Domain 4 Official Sources]] |

## Editorial decisions

Existing canonical services and filenames/headings are retained. New missing services, feature/concept pages, comparisons, scenario decisions and corrections are linked from the Domain 4 page.

The unanswered ECS-to-S3 question is completed in [[Domain 4 Scenario Decisions]]. The seventh walkthrough question itself was not supplied and is not marked processed.

The original wording is paraphrased, not reconstructed as a verbatim transcript. Incorrect/obsolete statements are preserved as identifiable correction-table entries rather than operational instructions.

## Explicit extensions

- Metric streams: included because official task 4.1 explicitly requires them.
- Current log centralization, enhanced ALB integration notice, EKS Auto Mode and modern naming: current context, not claims of original transcript coverage or guaranteed exam inclusion.
- Inspector Classic status: distinguishes old blueprint terminology from current service behavior.
- Safer destructive-response controls: turn simplified examples into bounded, evidence-aware study patterns.

See [[Notebook Provenance and Progress]], [[Notebook Changelog]], and [[Domain 4 Transcript Corrections]].
