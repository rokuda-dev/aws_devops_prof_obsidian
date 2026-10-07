---
title: CloudWatch vs EventBridge
tags:
  - aws
  - dop-c02
  - domain-4
verified: 2026-10-04
read: false
---

# CloudWatch vs EventBridge

CloudWatch observes and evaluates telemetry over time. EventBridge receives discrete events and routes matching events to consumers. They often form one design rather than compete: CloudWatch detects a sustained condition, then its alarm state-change event is routed by EventBridge.

## Fast decision

| Requirement | Choose | Why |
|---|---|---|
| Graph latency, errors, CPU, queue depth, or business KPIs | [[Amazon CloudWatch]] | Metrics and dashboards preserve time-series operational context |
| Alert when a value breaches a threshold for selected periods | CloudWatch alarm | Evaluates a numeric condition over time and tracks `OK`, `ALARM`, and `INSUFFICIENT_DATA` state |
| Search or aggregate stored application and service logs | CloudWatch Logs / Logs Insights | Works on retained log events; current log alarms can evaluate scheduled Logs Insights queries |
| React to an EC2 state change, deployment event, finding, or supported AWS API event | [[Amazon EventBridge]] | Matches fields in a discrete event and routes the event to targets |
| Route custom, AWS-service, or SaaS events to one or more consumers | EventBridge event bus | Content-based filtering and decoupled event delivery |
| Connect one supported source to one target with filtering or enrichment | EventBridge Pipes | Managed point-to-point integration |
| Invoke a target once or on a recurring schedule | EventBridge Scheduler | Scheduling is separate from telemetry evaluation; scheduled rules are the legacy option |
| Route an alarm to several response systems based on alarm metadata | CloudWatch alarm → EventBridge rule | CloudWatch evaluates the condition; EventBridge performs flexible routing |

## Different evaluation models

| Dimension | CloudWatch | EventBridge |
|---|---|---|
| Primary question | “Is the workload healthy, and what changed over time?” | “Did this event occur, and which consumers need it?” |
| Typical input | Metrics, logs, traces, application and infrastructure telemetry | AWS service events, custom application events, partner/SaaS events, or supported pipe sources |
| Matching | Thresholds, metric math, anomaly bands, composite states, or scheduled log-query results | Event-pattern fields such as `source`, `detail-type`, and values inside `detail` |
| Time semantics | Evaluates datapoints or query results across periods | Evaluates each arriving event against patterns |
| Output | Alarm state/action, dashboard, query result, or operational insight | Delivery to a target or subscriber; optional transformation/enrichment depends on the EventBridge feature |
| History | Metrics and logs have CloudWatch retention behavior | Do not treat an event bus as telemetry history; retention and replay depend on the bus type or archive configuration |
| Failure focus | Missing/delayed telemetry, incorrect dimensions/statistics, missing-data policy, alarm-action configuration | Pattern mismatch, source delivery level, target authorization, throttling, retries, DLQ, duplicates, or response loops |

## Compose the services

```text
Application/AWS resource
  └─ metrics or logs → CloudWatch alarm
                         └─ alarm state-change event → EventBridge
                                                          ├─ SNS notification
                                                          ├─ Lambda handler
                                                          └─ Step Functions / SSM workflow
```

CloudWatch sends alarm creation, configuration, deletion, and state-change events to EventBridge. AWS specifically guarantees delivery of alarm state-change events to EventBridge. EventBridge can then match fields such as the alarm name and new state and route the event to supported targets.

Keep two success criteria separate:

1. CloudWatch correctly evaluates the signal and changes alarm state.
2. EventBridge successfully delivers the matching event and the downstream workflow achieves the intended result.

An accepted target invocation does not prove that remediation completed. Monitor EventBridge delivery metrics, configure a supported SQS DLQ where appropriate, and make consumers idempotent because duplicate delivery is possible.

## Scenario judgment

| Scenario | Best answer | Common wrong turn |
|---|---|---|
| CPU exceeds 80% for three evaluation periods | CloudWatch metric alarm | EventBridge does not calculate a rolling CPU threshold |
| Five-minute error count from application logs breaches a threshold | CloudWatch metric filter plus alarm, or a supported log alarm | An EventBridge pattern does not query historical CloudWatch Logs |
| An EC2 instance enters `terminated` | EventBridge rule matching the native state-change event | Polling a metric for a discrete lifecycle transition |
| A captured `PutBucketPolicy` API call should trigger review | EventBridge rule matching the applicable CloudTrail-delivered event | Treating EventBridge as the authoritative audit archive; retain CloudTrail evidence separately |
| A high-severity alarm should notify one team and start a runbook for selected resources | CloudWatch alarm → EventBridge rules/targets | Trying to encode all routing in the alarm itself |
| Run a reconciliation job every night | EventBridge Scheduler | A CloudWatch alarm is not a general-purpose scheduler |

## Exam traps

> [!warning]
> **CloudWatch Events is the former name of the event-bus/rules capability now provided by Amazon EventBridge.** It does not mean that present-day CloudWatch and EventBridge are the same service.

- EventBridge does not continuously query arbitrary CloudWatch logs or calculate metric statistics. First create the appropriate CloudWatch signal if the requirement is based on telemetry over time.
- A CloudWatch alarm is not a generic event bus, queue, or workflow engine. Use EventBridge for event routing and Step Functions or Systems Manager Automation for stateful response logic.
- EventBridge matching requires the real event schema and correct account/Region. A CloudTrail-backed API event also depends on the applicable event being captured and delivered.
- A rule can match more events than intended and create a remediation loop. Narrow the pattern, recheck current state, and ensure the action does not continuously retrigger itself.
- EventBridge target permissions, retry/DLQ handling, and business-workflow failure handling are separate concerns.

## Related study

Tasks 4.1–4.3. See [[Log Subscription vs Metric Filter vs EventBridge Rule]], [[Metric Alarms and Anomaly Detection]], [[CloudWatch Logs Insights and Filter Patterns]], [[Event Sources and Response Contracts]], and [[Safe Event-Driven Remediation]].

## Official AWS references

- [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/)
- [What is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/)
- [CloudWatch alarm events and EventBridge](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-and-eventbridge.html)
- [EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html)
- [EventBridge rules and Scheduler guidance](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html)
- [EventBridge target dead-letter queues](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rule-dlq.html)
