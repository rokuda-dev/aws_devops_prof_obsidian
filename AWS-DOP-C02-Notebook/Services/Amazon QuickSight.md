---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# Amazon QuickSight

## Role and naming

Business-intelligence datasets, analyses and dashboards. The transcript calls this Amazon QuickSight; current AWS material places BI under **Quick Sight** within **Amazon Quick Suite**. Retain the familiar service name here for exam and existing-source continuity.

## Domain 4 use

Visualize CI/CD performance and compliance datasets, often queried through Athena. Define a dataset, suitable calculated fields, refresh/direct-query behavior, access controls, and dashboard ownership.

| Requirement | Better first tool |
|---|---|
| Operational metric graphs and alarm status | CloudWatch dashboards |
| AWS resource compliance evaluation | Config rules and compliance views/aggregators |
| BI analysis of prepared historical datasets | QuickSight with a suitable source, such as Athena |
| Alert/action on an event | EventBridge/CloudWatch alarm workflow |

QuickSight does not evaluate Config rules or generate operational telemetry by itself. Snapshot or scheduled refresh may not meet near-real-time requirements.

## Historical solution caveat

The AWS DevOps Monitoring Dashboard solution mentioned in the transcript is **no longer supported and receives no further updates**. Its metric/data-lake/BI architecture can still illustrate a pattern; do not present the old solution as a maintained recommended deployment.

## Sources

Task 4.2. See [[Monitoring Correlation Tracing and Dashboards]], [[AWS Config]].

- [QuickSight/Quick Suite transition](https://aws.amazon.com/blogs/business-intelligence/reimagine-business-intelligence-amazon-quicksight-evolves-to-amazon-quick-suite/)
- [DevOps dashboard support notice](https://docs.aws.amazon.com/solutions/latest/devops-monitoring-dashboard-on-aws/solution-overview.html)
