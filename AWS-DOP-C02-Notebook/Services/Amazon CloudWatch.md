---
title: Amazon CloudWatch
tags: [aws, dop-c02, service]
status: consolidated-study-note
updated: 2026-09-18
read: false
---

# Amazon CloudWatch

Observe workloads through metrics, logs, alarms, dashboards, and related telemetry features.

## Exam mapping

Task statements: 1.2, 1.4; cross-domain 4–5. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

CloudWatch Agent adds host/system/application logs and metrics. Logs Insights queries stored logs; metric filters turn new matching log events into metrics; alarms evaluate metric conditions.

## Architecture pattern

Application/agent → logs and metrics → alarm → [[Amazon EventBridge]]/deployment rollback/runbook.

## IAM and security

Scope telemetry publishing and log-reading access; apply retention and encryption. Keep secrets and personal data out of logs.

## Failure, rollback, and lifecycle

Metric filters do not retroactively generate metrics for old log events. Deployment rollback requires an enabled alarm integration, not merely an alarm's existence.

## When to choose

> [!exam]
> Choose for workload health, telemetry, alerting, and investigation of application behavior.

## Do not confuse with and exam traps

> [!warning]
> [[AWS CloudTrail]] audits AWS API activity; [[AWS Config]] tracks resource configuration/compliance. Default EC2 metrics do not include guest memory usage.

## Official AWS references

- [Amazon CloudWatch official reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 3 — signals tied to objectives

Track user success/latency, errors, saturation, healthy zonal capacity, replication lag, backup/copy freshness, and recovery action outcomes. Correlate metrics with logs/traces; CPU alone is insufficient.

Test detection/evaluation delay and false positives before wiring alarms to recovery actions. Publish private-resource probe outcomes for suitable alarm-based Route 53 health checks when public checkers cannot reach the endpoint.

Tasks 3.1–3.3. See [[Resilience Framework and Dependency Isolation]], [[Scaling Metrics and Troubleshooting]], [[Amazon Route 53]].

## Domain 4 — feature study map


| Topic | Study note |
|---|---|
| Custom metrics, dimensions and statistic sets | [[CloudWatch Metrics Namespaces and Dimensions]] |
| Host/container agents, roles and driver settings | [[CloudWatch Agent and Container Log Collection]] |
| Streaming and cross-account delivery | [[CloudWatch Log Subscriptions and Cross-Account Destinations]] |
| Stored-log analysis and filter syntax | [[CloudWatch Logs Insights and Filter Patterns]] |
| Threshold/band/composite alarms | [[Metric Alarms and Anomaly Detection]] |
| Continuous metric export | [[CloudWatch Metric Streams]] |
| Retention, encryption and validation | [[Log Lifecycle Security and Integrity]] |
| Application correlation/dashboards | [[Monitoring Correlation Tracing and Dashboards]] |

The agent default namespace is CWAgent. Numeric metric publication uses PutMetricData/EMF or suitable log extraction—not EventBridge.

Metric fidelity is retained at different periods: sub-minute points for three hours, one-minute for 15 days, five-minute for 63 days, and one-hour for 455 days. This automatic metric aggregation is distinct from log-group retention or S3 lifecycle.

A dashboard displays health but does not enforce compliance. See [[Domain 4 Architecture Patterns]], [[Domain 4 Official Sources]].

## Domain 5 — troubleshooting and monitored response

- [[CloudWatch Synthetics]] — endpoint/journey checks and canary failure investigation.
- [[CloudWatch Container Insights]] — explicitly configured container telemetry.
- [[ECS and EKS Failure Triage]] — correlate events, stopped reasons, logs and pressure.
- [[HTTPS Connectivity Troubleshooting]] — network and TLS evidence.
- [[CI-CD Failure Triage and Parallel Actions]] — inspect failed pipeline/build/deploy layers.
- [[Incident Response Workflow and Evidence Preservation]] — preserve evidence and verify recovery.

Logs must actually be published; the CloudWatch agent is not the only collection path. Alarms detect configured numeric states and can initiate supported actions/events; they do not themselves undo external side effects.

Tasks 5.1–5.3.
