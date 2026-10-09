---
title: CloudWatch vs Managed Prometheus vs Managed Grafana vs X-Ray
tags:
  - aws
  - dop-c02
  - comparisons
  - observability
verified: 2026-10-07
read: false
---

# CloudWatch vs Managed Prometheus vs Managed Grafana vs X-Ray

| Need | Best first thought | Boundary |
|---|---|---|
| AWS-native metrics, logs, alarms, dashboards, and telemetry actions | [[Amazon CloudWatch]] | Broad observability service; collection and dimensions still require configuration |
| Prometheus-compatible container metrics, PromQL, and managed metric storage/query | Amazon Managed Service for Prometheus (AMP) | Metric backend, not a general log store or Grafana dashboard service |
| Managed Grafana workspaces across CloudWatch, AMP, X-Ray, OpenSearch, and other sources | Amazon Managed Grafana | Visualization/query workspace; it does not replace the underlying telemetry stores |
| Distributed request traces, service maps, latency, and downstream errors | [[AWS X-Ray]] | Trace backend, not aggregate metric storage or API actor auditing |
| Vendor-neutral instrumentation and telemetry collection/export | [[AWS Distro for OpenTelemetry]] (ADOT) | Instrumentation/collector path; it is not itself the long-term query or dashboard destination |

## Compose rather than substitute

```text
Application/container instrumentation
  -> ADOT / Prometheus-compatible collection
  -> CloudWatch, AMP, and/or X-Ray backends
  -> CloudWatch dashboards/alarms or Managed Grafana visualization
```

The scenario should decide the data model and query language before the dashboard product. PromQL and an existing Prometheus ecosystem point toward AMP. AWS service metrics/logs and native alarm actions point toward CloudWatch. Cross-source Grafana dashboards point toward Amazon Managed Grafana, but the data remains in configured sources. Request-path causality points toward traces in X-Ray.

Current CloudWatch can also evaluate PromQL alarms for metrics ingested through its OTLP endpoint. Do not infer that every PromQL scenario requires AMP, or that a Grafana workspace stores the source telemetry.

Tasks 4.1–4.2. See [[Monitoring Correlation Tracing and Dashboards]], [[CloudWatch Metrics Namespaces and Dimensions]], and [[Amazon CloudWatch, X-Ray, and OpenTelemetry]].

## Official AWS references

- [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
- [CloudWatch PromQL alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-promql.html)
- [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html)
- [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html)
- [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
- [AWS Distro for OpenTelemetry](https://aws-otel.github.io/docs/introduction/)
