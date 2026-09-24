---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# Monitoring Correlation Tracing and Dashboards

## Correlation schema

Use consistent service/environment/account/Region identifiers and timestamps. Put request/trace IDs into structured logs; use low-cardinality dimensions for metrics. Align time windows and distinguish event time from ingestion time.

| Signal | Question |
|---|---|
| Metrics | How widespread/severe is the symptom? |
| Logs | What happened and with what context? |
| Traces | Which request/dependency path caused latency or failure? |
| CloudTrail | Which actor made an AWS API change? |
| Config | What configuration/compliance changed? |

ServiceLens correlates metrics/logs/X-Ray traces. Application Insights can help configure monitoring of an application and its resources; Application Signals is a distinct application performance/SLO capability. Do not treat all these names as interchangeable.

## Tracing integrations

API Gateway X-Ray tracing applies to supported **REST APIs**; do not assume identical support for HTTP/WebSocket APIs. Enable appropriate stage tracing and sampling.

Lambda tracing requires appropriate settings/permissions and application instrumentation for downstream/custom work. The transcript's two-node service/function map is a service visualization detail, not proof that all code is automatically instrumented.

EventBridge can propagate supported PutEvents trace context as internal metadata. It is not an ordinary visible event field and is not retained for archive replay/DLQ as a reusable original trace ID. Targets still need compatible tracing support.

Prefer OpenTelemetry/ADOT for new instrumentation. Existing X-Ray SDK/daemon maintenance does not mean the X-Ray backend service is retired. See [[AWS X-Ray]] for the carried-forward support check.

## Dashboard strategy

Start with business SLIs, errors, throughput, tail latency, saturation and alarm states. Use operational CloudWatch dashboards for live health, Config views for compliance, and Athena/QuickSight for prepared dataset analysis.

Collect a baseline, then tune thresholds/dimensions as actual failure behavior becomes clear. A one-time graph does not replace continuous monitoring.

For pipeline/environment dashboards, calculate meaningful definitions (failure rate, deployment volume, recovery time) and explicitly account for refresh delays. The old DevOps Monitoring Dashboard solution is unsupported.

Task 4.2. See [[Amazon CloudWatch]], [[AWS Distro for OpenTelemetry]], [[Amazon QuickSight]], [[Domain 4 Official Sources]].

- [ServiceLens](https://aws.amazon.com/cloudwatch/features/)
- [API Gateway REST tracing](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-xray.html)
- [EventBridge trace metadata limits](https://aws.amazon.com/blogs/compute/using-aws-x-ray-tracing-with-amazon-eventbridge/)
