---
title: CloudWatch Container Insights
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# CloudWatch Container Insights

Collect, aggregate, and visualize container performance/log telemetry for supported ECS, EKS, and Kubernetes-on-EC2 environments.

## Collection is configured

ECS requires appropriate cluster/account opt-in and setup. EKS commonly uses the CloudWatch Observability add-on/agent and supported log collection. Configure roles, service connectivity, and the required log sources. Do not assume Container Insights is automatically enabled for every cluster.

## Incident signals

Correlate CPU/memory pressure, restarts, failed placement/scheduling, running task/pod counts, and application/health errors. Metric availability and aggregation levels vary by platform and enhanced/standard configuration; a task is not a Kubernetes pod.

Performance log events can use the embedded metric format, from which CloudWatch derives metrics. Query underlying logs for details not represented in aggregate dashboards; choose alarm thresholds based on the workload baseline.

## Boundaries

This is telemetry, not an autoscaler. HPA/CA/Karpenter/ECS scaling policies act on configured conditions. Control-plane audit logs and container application logs are distinct sources.

Task 5.3. [[ECS and EKS Failure Triage]], [[Amazon EKS]], [[Amazon ECS]], [[CloudWatch Agent and Container Log Collection]].

- [CloudWatch Container Insights setup FAQ](https://aws.amazon.com/cloudwatch/faqs/)
