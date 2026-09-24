---
title: ECS and EKS Failure Triage
tags:
  - aws
  - dop-c02
  - domain-5
verified: 2026-09-18
read: true
---

# ECS and EKS Failure Triage

## ECS

Start with service events, deployment status, and stopped-task reasons. Inspect container exit codes/reasons, image resolution and pull permissions, capacity/placement constraints, network access, health checks, startup grace period, and application logs.

Exit 137 indicates SIGKILL, not proof of OOM: correlate memory data and stopped reasons; shutdown timeout or a manual kill can also explain it. Exit 143 can be expected during normal termination.

With awslogs configured, stdout/stderr goes to CloudWatch Logs. Fargate does not expose a host for Docker debugging. On authorized EC2 container instances, local docker logs can help when the logging driver retains local logs. Destination permissions and application task-role permissions are different.

## EKS

Inspect workload status/events, pod descriptions, current/previous container logs, restarts, readiness/liveness probes, image pulls, resource requests/limits, node scheduling, and application dependencies. Check HPA/pod demand separately from node capacity/CA/Karpenter behavior.

Enable required control-plane log types explicitly; use Container Insights/add-on and collection configuration for workload telemetry. CloudWatch availability does not mean all cluster logs/metrics are already collected.

## Close the loop

Preserve deployment version/digest and incident evidence, remediate the demonstrated cause, then verify user-facing behavior. Avoid blind restart loops or replacing healthy nodes without evidence.

Task 5.3. [[Amazon ECS]], [[Amazon EKS]], [[AWS Fargate]], [[CloudWatch Container Insights]], [[CI-CD Failure Triage and Parallel Actions]], [[Domain 5 Official Sources]].
