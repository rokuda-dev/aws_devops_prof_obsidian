---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# CloudWatch Metric Streams

## Blueprint extension

Official task 4.1 explicitly includes **metric streams**, making this an important companion to custom-metric and log-subscription patterns.

CloudWatch metric stream → same-account/same-Region Firehose delivery stream → supported destination, such as S3 or a partner endpoint.

| Concept | Do not confuse it with |
|---|---|
| PutMetricData | Publishing measurements into CloudWatch |
| Metric stream | Continuously exporting metric updates from CloudWatch |
| Log subscription | Forwarding matching log events |
| Metric filter | Producing metrics from log matches |
| S3 archive | Storage destination, not itself the metric stream transport |

Select metric namespaces/filters/output format and authorize CloudWatch to put records into Firehose. Configure downstream delivery permissions, encryption, freshness/error monitoring and storage lifecycle.

The Firehose resource for the metric stream must be in the same account and Region as the stream. A supported final destination can provide separate cross-account/cross-Region functionality; do not directly apply cross-account **log subscription** setup to metric streams.

## Sources

Task 4.1. See [[Amazon Data Firehose]], [[CloudWatch Metrics Namespaces and Dimensions]].

- [Metric stream custom Firehose setup](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-setup-datalake.html)
- [Official task 4.1](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain4.html)
