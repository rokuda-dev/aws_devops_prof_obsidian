---
title: AWS X-Ray
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# AWS X-Ray

Distributed tracing backend for request paths, dependencies, latency, and failures.

## Exam mapping

Task statements: 1.2; cross-domain 4. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Trace segments/subsegments and service maps help identify downstream bottlenecks. Sampling controls volume. OpenTelemetry/ADOT can send traces to X-Ray.

## Architecture pattern

Instrument application with [[AWS Distro for OpenTelemetry]] → export traces → X-Ray request analysis.

## IAM and security

Scope trace publishing/reading and avoid embedding secrets in trace metadata.

## Failure, rollback, and lifecycle

X-Ray SDKs and daemon entered maintenance on February 25, 2026: security fixes only, no new enhancements. The X-Ray service remains supported.

## When to choose

> [!exam]
> Choose for end-to-end request tracing, not just aggregate metrics or API actor attribution.

## Do not confuse with and exam traps

> [!warning]
> SDK/daemon maintenance is not X-Ray service retirement. Prefer OpenTelemetry for new instrumentation.

## Official AWS references

- [AWS X-Ray official reference](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-daemon-timeline.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 4 — integration and correlation

Verify compatible settings, sampling, permissions and instrumentation. REST API stage tracing, Lambda service/function visualization and application downstream spans are separate details.

Supported EventBridge PutEvents tracing uses internal metadata, not an ordinary archived/replayable event field. Correlate trace IDs with structured logs and metric time windows. Searchable annotations differ from arbitrary metadata; avoid secrets/PII.

Task 4.2. See [[Monitoring Correlation Tracing and Dashboards]], [[AWS Distro for OpenTelemetry]].
- [REST API integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-xray.html)
- [EventBridge context](https://aws.amazon.com/blogs/compute/using-aws-x-ray-tracing-with-amazon-eventbridge/)

## Domain 5 — traced incident impact

Correlate sampled request paths with canary failures, application errors, logs and deployment changes. ServiceLens provides a correlated investigation view when relevant telemetry is configured; incomplete instrumentation/sampling can leave gaps.

For new instrumentation, favor the already documented OpenTelemetry/ADOT path; the X-Ray backend is distinct from SDK/daemon lifecycle status.

Task 5.3. [[CloudWatch Synthetics]], [[Monitoring Correlation Tracing and Dashboards]], [[Incident Response Workflow and Evidence Preservation]].
- [Synthetic trace correlation](https://aws.amazon.com/blogs/devops/debugging-with-amazon-cloudwatch-synthetics-and-aws-x-ray/)
