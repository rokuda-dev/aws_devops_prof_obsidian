---
tags: [aws, dop-c02, comparisons]
updated: 2026-09-18
read: false
---

# Config vs CloudTrail vs Systems Manager

| Requirement | Best choice | Why the others distract |
|---|---|---|
| What was the resource configured like? | [[AWS Config]] | CloudTrail reports API activity; not a complete resource-state recorder |
| Who called an AWS API? | [[AWS CloudTrail]] | Config history is not the primary actor-attribution audit |
| Is resource configuration compliant? | Config rule/conformance pack | CloudWatch alarms generally evaluate workload metrics |
| Fix a resource/operate nodes | [[AWS Systems Manager]] Automation or host capability | Config aggregation itself performs no remediation |
| What happened in the app? | [[Amazon CloudWatch]] logs/metrics | CloudTrail does not collect arbitrary application events |
| Maintain a package/service on hosts | SSM State Manager | Config compliance evaluation is not host desired-state enforcement |

> [!exam]
> “Detect and automatically fix configuration noncompliance” combines evaluation and action: Config + scoped SSM Automation (or an event-driven response pattern), not an aggregator alone.

Recording, evaluation, event routing, and remediation are separate setup/permission boundaries. See [[AWS Config#Multi-account remediation design]].

## Domain 4 trigger distinction

Config compliance after evaluation, CloudTrail API events, CloudWatch metric/log alarms, and Systems Manager remediation are different stages. For StopLogging, use the actual API event for prompt detection plus periodic Config assurance; invoke a bounded authorized repair workflow.

See [[Safe Event-Driven Remediation]], [[Log Subscription vs Metric Filter vs EventBridge Rule]].
