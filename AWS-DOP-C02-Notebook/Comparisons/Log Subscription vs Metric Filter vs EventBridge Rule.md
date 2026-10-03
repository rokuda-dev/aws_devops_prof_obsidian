---
tags:
  - aws
  - dop-c02
  - domain-4
verified: 2026-09-18
read: true
---

# Log Subscription vs Metric Filter vs EventBridge Rule

| Mechanism | Input | Output | Timing |
|---|---|---|---|
| Log subscription | Matching CloudWatch log events | Forwarded batches to supported destination | New events; delivery/retry latency |
| Metric filter | Matching CloudWatch log events | Numeric metric samples | New ingested events; not historical backfill |
| EventBridge rule | Events on a bus | Target invocation | Event delivery/routing latency |
| Logs Insights query | Stored logs in selected window | Search/aggregation results | Query execution, not inherently a continuous action |
| CloudWatch log alarm | Scheduled Logs Insights query results | Alarm state/actions | M-out-of-N query evaluation; no metric filter required |

The log-alarm row reflects current product capabilities checked on 2026-09-27; a one-time Logs Insights query still does not create an alarm. See [CloudWatch alarm types](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html).

Example: S3 bucket-policy audit → CloudTrail → CloudWatch Logs → metric filter → alarm → SNS. Alternative: CloudTrail API event → EventBridge → SNS/Lambda response.

A metric alarm normally notifies on state changes, not per raw event. Use event routing if the requirement is a notification for every qualifying event.

Tasks 4.1–4.3. See [[Metric Alarms and Anomaly Detection]], [[Safe Event-Driven Remediation]], [[AWS CloudTrail]].
