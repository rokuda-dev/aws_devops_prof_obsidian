---
tags:
  - aws
  - dop-c02
  - observability
  - opentelemetry
updated: 2026-09-18
read: true
---

# AWS Distro for OpenTelemetry

ADOT provides AWS-supported OpenTelemetry tooling for vendor-neutral instrumentation and telemetry collection/export. It is instrumentation/collection, not a replacement backend for [[AWS X-Ray]] or [[Amazon CloudWatch]].

## Exam-relevant pattern

Application instrumented with OpenTelemetry → supported collector/exporter → X-Ray traces and CloudWatch telemetry.

> [!important]
> X-Ray SDKs/daemon entered maintenance mode on February 25, 2026. Prefer OpenTelemetry for new instrumentation; the X-Ray service remains supported.

## Security and operation

Scope exporters' AWS permissions, keep sensitive data out of telemetry, configure sampling, and observe collector failures/resource use. Installing a collector does not automatically instrument every application.

## Official reference

- [X-Ray SDK/daemon support timeline](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-daemon-timeline.html)
- [AWS Distro for OpenTelemetry](https://aws.amazon.com/otel/)

## Domain 4 — collection context

Use compatible instrumentation/collectors/exporters for the chosen platform. Correlate trace IDs in logs and keep metric dimensions low-cardinality. Service trace propagation is not full application instrumentation.

The carried-forward X-Ray SDK/daemon maintenance check favors OpenTelemetry for new instrumentation; it is not backend retirement.

Task 4.2. See [[AWS X-Ray]], [[Monitoring Correlation Tracing and Dashboards]].
