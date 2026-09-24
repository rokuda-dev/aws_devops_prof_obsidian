---
tags:
  - aws
  - dop-c02
  - domain-3
verified: 2026-09-18
read: true
---

# Amazon EKS

## Regional architecture

EKS manages a Kubernetes control plane for a regional cluster. Multi-Region designs use separate regional clusters and deploy compatible manifests, images, secrets, networking, and data access to each.

**Trap:** a managed control plane does not mean every application's pods and nodes automatically scale across Regions.

| Layer | Scaling mechanism |
|---|---|
| Application replicas | Horizontal Pod Autoscaler (HPA), using configured metrics |
| EC2 node capacity | Karpenter, Cluster Autoscaler, or configured EKS Auto Mode |
| Fargate pod execution | Provisioned per eligible pod; pod replica count still needs a policy |
| Regional traffic/data | Separate routing and data-replication architecture |

Horizontal Pod Autoscaler (HPA) needs an appropriate metrics source. CPU-based utilization requires suitable resource requests. Pending pods can mean node capacity, placement, quotas, storage, or policy problems—not necessarily an HPA failure.

EKS Auto Mode uses Karpenter-based capacity management; do not assume it is enabled in every existing cluster. Choose and configure the node-scaling mechanism intentionally.

## Global application pattern

Regional EKS clusters + locally available [[Amazon ECR]] images + [[Amazon Aurora Global Database]] for a compatible relational transactional model + [[AWS Global Accelerator]] in front of supported ALB/NLB endpoints. Aurora remains a single-primary global relational design; regional application replicas do not make every Region a writer.

## Recovery considerations

Replicate manifests/configuration and images; test storage classes, load balancers, workload identities, regional secrets/KMS access, network paths, quotas, and database reconnection. Backing up YAML alone is not recovery of persistent application data.

## Sources

Tasks 3.1–3.3. See [[AWS Fargate]], [[Multi-Region Application Checklist]].

- [EKS HPA](https://docs.aws.amazon.com/eks/latest/userguide/horizontal-pod-autoscaler.html)
- [EKS Auto Mode scaling architecture](https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode/)

## Domain 4 — scaler distinctions

Cluster Autoscaler adjusts configured node-group ASGs; Karpenter directly provisions EC2 capacity. HPA adjusts pods. Current EKS Auto Mode offers managed Karpenter-based node capacity.

These are different layers, not merely “two autoscalers.” Correlate replica demand, pending pods, nodes, latency and downstream saturation.

Task 4.3. See [[Scaling Metrics and Troubleshooting]], [[Monitoring Correlation Tracing and Dashboards]].

## Domain 5 — workload and node diagnosis

Inspect pod status/events, describe output, current/previous logs, restarts, probes, image pulls and resource requests/limits. Diagnose pod replica policy separately from node provisioning/scheduling.

Configure Container Insights/add-on and required control-plane log types explicitly. Container telemetry does not automatically turn on all audit logs or remediate scheduling failures.

Task 5.3. [[ECS and EKS Failure Triage]], [[CloudWatch Container Insights]], [[Incident Response Workflow and Evidence Preservation]].
