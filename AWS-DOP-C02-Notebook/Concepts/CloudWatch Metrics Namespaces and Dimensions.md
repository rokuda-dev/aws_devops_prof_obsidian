---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# CloudWatch Metrics Namespaces and Dimensions

## Identity and resolution

A CloudWatch metric is a time series identified by its namespace, metric name, and dimension set within an account/Region. A data point adds timestamp, value/statistics and unit. A dimension is a case-sensitive name/value pair, not a free label automatically ignored during aggregation.

| Item | Example | Exam distinction |
|---|---|---|
| AWS namespace | AWS/EC2, AWS/S3 | AWS/ is reserved for AWS service metrics |
| Agent default namespace | CWAgent | Exact spelling; not “CW Agent” |
| Custom namespace | Payments/Production | Keep unrelated/custom measurements appropriately organized |
| Dimension | Operation=Payment | Each distinct combination creates a separate custom metric |
| Standard-resolution custom data | 60-second storage resolution | Appropriate for the transcript's per-minute counts |
| High-resolution custom data | StorageResolution=1 | Use only when finer detail justifies cost and supported alarm settings |

Certain AWS service metrics support aggregation across omitted dimensions; **custom metrics do not automatically roll up across dimensions**. Publish deliberate rollups, use appropriate metric math/querying, or configure supported agent aggregation.

EC2 basic/detailed service monitoring does not add guest memory/disk-space measurements. The agent or another custom publisher is needed for those measurements.

## Payment/refund example

Publish to CloudWatch, not EventBridge. Use separate metrics or an Operation dimension, then alarm on the correct one-minute **Sum**. A statistic set reduces calls:

```json
{
  "Namespace": "Payments/Production",
  "MetricData": [
    {
      "MetricName": "Transactions",
      "Dimensions": [{"Name": "Operation", "Value": "Payment"}],
      "Unit": "Count",
      "StatisticValues": {
        "SampleCount": 3,
        "Sum": 11,
        "Minimum": 2,
        "Maximum": 5
      }
    }
  ]
}
```

This summarizes three observations of 2, 4 and 5 transactions: Sum=11, SampleCount=3. SampleCount is not the transaction total. Use the exact API field **StatisticValues**; the CLI parameter is --statistic-values. Add an appropriate timestamp and separately publish the refund series.

Statistic sets do not preserve arbitrary percentile distributions. CloudWatch needs raw samples except documented special cases (one sample or equal min/max). Prefer raw Values/Counts or suitable telemetry when p95/p99 is required.

## Cost and schema

Keep request IDs/customer IDs in logs or traces, not high-cardinality metric dimensions. Use low-cardinality service/environment/operation dimensions. Batch publication can reduce API calls but does not prove it is universally cheaper than EMF or log filters.

Task 4.1; reused in 4.2–4.3. See [[Metric Alarms and Anomaly Detection]], [[CloudWatch Logs Insights and Filter Patterns]].

- [Metric/dimension concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html)
- [Statistic-set publication](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
- [Agent namespace/configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html)
