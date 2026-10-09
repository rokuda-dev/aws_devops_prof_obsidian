---
title: Consistency and Exam Distinctions Audit 2026-10-07
tags:
  - aws
  - dop-c02
  - sources
  - audit
verified: 2026-10-07
read: false
---

# Consistency and Exam Distinctions Audit — 2026-10-07

## Scope

This targeted working-copy update compared the notebook's decision-heavy summaries and recently edited notes with the current DOP-C02 task statements, current in-scope service list, and first-party AWS documentation for disputed or high-impact distinctions. It did not revalidate every sentence, every Region/engine matrix, or every external URL.

## Material corrections

| Area | Correction |
|---|---|
| CodeBuild | Removed the false claim that parallel processing is unavailable; documented batch list/matrix/graph/fan-out distinctions |
| Elastic Beanstalk | Removed the EC2-only contradiction and separated Standard Mode from EKS-based Cluster Mode |
| Aurora Global Database | Removed an unsupported blanket incompatibility claim about Parallel Query |
| DynamoDB Global Tables | Added same-account versus multi-account topology and the MRSC same-account boundary |
| CloudWatch Logs | Propagated native scheduled Logs Insights log alarms into the canonical filter/query concept note |
| Trusted Advisor | Clarified configured weekly notification email versus support/check-dependent refresh behavior |

## Added exam-decision coverage

- [[SQS vs SNS vs EventBridge vs Kinesis]] — queue, fan-out, event routing, ordering, and replay semantics.
- [[Resilience Hub vs FIS vs Backup vs DRS vs ARC]] — assessment, fault injection, recovery mechanism, and orchestration boundaries.
- [[CloudWatch vs Managed Prometheus vs Managed Grafana vs X-Ray]] — telemetry backend, Prometheus model, visualization, tracing, and collection boundaries.

## Read-state handling

Notes whose study content changed were reset to `read: false`. Domain/navigation pages that received only links kept their existing read value. New notes start unread. No vault-wide reset was performed.

## Remaining coverage limits

The official in-scope service list is non-exhaustive and does not imply equal exam frequency. This update did not create shallow pages solely to match every named service. Lower-priority comparison gaps remain for App Runner versus other managed compute, Compute Optimizer versus Trusted Advisor/scaling actions, PrivateLink/connectivity choices, and several database/storage examples. Recheck them when a scenario or study question makes the distinction material.

## Primary evidence

- [Official DOP-C02 guide](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02.html)
- [Official in-scope services](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/dop-02-in-scope-services.html)
- [CodeBuild batch builds](https://docs.aws.amazon.com/codebuild/latest/userguide/batch-build.html)
- [CloudWatch alarm types](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html)
- [DynamoDB Global Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html)
- [Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html)

