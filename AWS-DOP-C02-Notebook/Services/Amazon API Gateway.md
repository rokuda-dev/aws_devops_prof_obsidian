---
title: Amazon API Gateway
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# Amazon API Gateway

Publish, secure, throttle, and observe REST, HTTP, and WebSocket APIs.

## Exam mapping

Task statements: 1.4; cross-domain observation/security. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

REST APIs provide richer API-management features such as usage plans/API keys; HTTP APIs fit many lower-cost HTTP proxy workloads; WebSocket APIs support bidirectional connections.

## Architecture pattern

API stage/integration → [[AWS Lambda]] production alias; API deployment changes may use REST API canary release settings.

## IAM and security

Use supported IAM/authorizer mechanisms and resource controls. API keys identify usage-plan consumers; they are not a substitute for authorization.

## Failure, rollback, and lifecycle

Separate API deployment rollback from Lambda alias rollback. Investigate integration permissions, request mapping, downstream latency, and logs.

## When to choose

> [!exam]
> Choose based on required protocol, authorization, management, and integration features.

## Do not confuse with and exam traps

> [!warning]
> Do not transfer REST API-only features automatically to HTTP APIs. API canary percentages and Lambda alias percentages are separate controls.

## Official AWS references

- [Amazon API Gateway official reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 3 — Regional multi-Region APIs

Deploy a separate Regional API in each chosen Region, configure the same custom domain on each deployment, and use [[Amazon Route 53]] latency/health routing. Keep regional certificates/configuration, Lambda integration, permissions, quotas and state access ready.

Regional endpoints are directly regional, not API Gateway's edge-optimized CloudFront endpoint. They can serve public clients; “Regional” does not restrict clients to that Region.

REST API canary releases send a percentage of stage traffic to a deployment. This is different from a Lambda alias canary and from cross-Region failover. [[AWS Global Accelerator]] does not directly support API Gateway as a standard endpoint.

Task 3.2.
- [Endpoint types](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-endpoint-types.html)
- [Canary releases — official resource](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.html)

## Domain 4 — tracing

X-Ray tracing is documented for REST API stages and supported endpoint types. Do not assume HTTP/WebSocket API parity. Sampling does not capture every request automatically.

Pair errors/latency and authorized access logs with downstream traces; avoid logging tokens/confidential payloads.

Task 4.2. See [[Monitoring Correlation Tracing and Dashboards]].
- [REST API tracing](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-xray.html)
