---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# Metric Alarms and Anomaly Detection

## Configuration checklist

Specify the exact metric identity/statistic, period, threshold or band, EvaluationPeriods (N), DatapointsToAlarm (M), missing-data treatment, actions and ownership. Separate warning/critical alarms can watch the same metric with different settings.

| Type | Evaluates | Best use |
|---|---|---|
| Static metric alarm | Metric/math value versus fixed threshold | Known business/technical limit |
| Anomaly alarm | Metric versus learned expected band | Variable/seasonal metric behavior |
| Composite alarm | Boolean conditions over alarm states | Reduce noise or correlate symptoms |

States include OK, ALARM and INSUFFICIENT_DATA for metric alarms. Test actual state transitions and delivery; an SNS email subscription must be confirmed.

## Anomaly detection

CloudWatch learns expected metric behavior and displays an upper/lower band. Alarm above, below or outside it as appropriate. GetMetricData with ANOMALY_DETECTION_BAND can retrieve band values.

Exclude/treat unusual training periods appropriately, allow for changing workloads, and calibrate sensitivity. An unexpected metric is not automatically a security intrusion. This feature does not ingest the cross-account raw log stream instead of Kinesis.

## Missing data

| Setting | Interpretation |
|---|---|
| missing | Missing points may lead to insufficient data |
| notBreaching | Treat missing points as within threshold |
| breaching | Treat missing points as violating threshold |
| ignore | Preserve alarm state for missing data |

Sparse error-count metrics and heartbeat metrics need different choices. Metric-filter default zero does not manufacture telemetry when no logs arrive. Evaluate M-of-N behavior, reporting lag and service-specific exceptions.

## Actions and rollback

Typical notifications occur on state transitions, not on every matching log event while ALARM persists. Auto Scaling actions have different repeating semantics.

CodeDeploy rollback requires the deployment's alarm integration and rollback options. An alarm does not automatically undo an S3 bucket policy change. Composite alarms have different action constraints from simple metric alarms; do not assume direct EC2/Auto Scaling actions work for every alarm type.

Use appropriate percentiles for tail latency; average can hide outliers. Preserve raw distribution data when percentile alarms matter.

Tasks 4.2–4.3. See [[Static vs Anomaly vs Composite Alarms]], [[AWS CodeDeploy]], [[Safe Event-Driven Remediation]].

- [Anomaly detection configuration](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_cloudwatch/README.html)
- [Composite alarm semantics](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-compositealarm.html)
- [[Domain 4 Official Sources]]
