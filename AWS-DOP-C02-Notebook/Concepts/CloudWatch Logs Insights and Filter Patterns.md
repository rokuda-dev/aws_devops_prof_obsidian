---
tags:
  - aws
  - dop-c02
  - domain-4
verified: 2026-10-07
read: false
---

# CloudWatch Logs Insights and Filter Patterns

## Three different languages/purposes

| Tool | Result | Continuous? |
|---|---|---|
| Metric-filter pattern | Extract/count log matches into a metric | New ingested events |
| Subscription-filter pattern | Forward matching events | New ingested events |
| Logs Insights query | Search/aggregate stored logs | One-time query or separately scheduled query over selected windows |
| CloudWatch log alarm | Evaluate an aggregated Logs Insights query result | Scheduled M-out-of-N evaluation and alarm actions |

EventBridge event patterns use a different JSON matching structure; do not paste an Insights query into a rule.

## Query versus continuous evaluation

Running a Logs Insights query once does not create an alarm. A current CloudWatch **log alarm** schedules an aggregated Logs Insights query and evaluates recent results against a threshold using M-out-of-N logic, without first creating a metric filter. Use a metric filter when the durable output should be a reusable CloudWatch metric; use a log alarm when the supported scheduled query result is the signal itself.

## Discovered fields

Standard-class log groups support automatic field discovery. Relevant supported formats include default VPC flow logs, Route 53 logs, Lambda logs, CloudTrail JSON and application JSON. The transcript's “Amazon BPC” is VPC.

System fields include @message, @timestamp, @ingestionTime, @logStream and @log; entity information can also be present. Do not confuse event time with ingestion time.

Use parse for unsupported/custom formats. For Lambda, only the first embedded JSON fragment is automatically discovered. JSON-encoded strings are not nested objects; use an appropriate parsing function before traversing their content.

## Query examples

Selected log groups must already contain the corresponding CloudTrail records:

```text
fields @timestamp, eventName, userIdentity.arn, sourceIPAddress
| filter eventSource = "s3.amazonaws.com"
  and eventName in ["PutBucketPolicy", "DeleteBucketPolicy"]
| sort @timestamp desc
| limit 100
```

For application error counts:

```text
fields @timestamp, @message
| filter @message like /ERROR/
| stats count(*) as errors by bin(5m)
```

Use a narrow time range and appropriate log groups to reduce scan volume. bin(5m) is safer than expressing five minutes as bin(300s), because time-unit caps apply.

## Metric-filter example

```text
{ ($.eventSource = "s3.amazonaws.com") && (($.eventName = "PutBucketPolicy") || ($.eventName = "DeleteBucketPolicy")) }
```

Publish 1 per match, then alarm on Sum >= 1 for the chosen period. Specify whether failed attempts should count or only successful changes. Broader ACL/lifecycle/replication changes require additional deliberate matching.

Filters are not retroactive. A default metric value applies when logs are ingested without matches; a period with no ingested logs does not automatically publish zero. Dimensioned metric filters cannot specify that default value. Choose alarm missing-data behavior accordingly.

## Sources

Tasks 4.1–4.2. See [[Log Subscription vs Metric Filter vs EventBridge Rule]], [[Metric Alarms and Anomaly Detection]].

- [Discovered fields and log classes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData-discoverable-fields.html)
- [Metric-filter concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html)
- [Official sample queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.html)
- [Log alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-log.html)
