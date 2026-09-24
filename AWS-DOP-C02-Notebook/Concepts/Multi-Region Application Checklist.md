---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# Multi-Region Application Checklist

| Layer | Preparation and failure question |
|---|---|
| Traffic | Route 53 or supported Global Accelerator endpoints; health/routing/reconnection tested? |
| Compute | Regional ASGs/ECS/EKS/API deployments, capacity headroom and quotas ready? |
| Database | Correct writer topology, lag visibility, promotion/fencing, failback strategy? |
| Objects | S3 destination bucket/versioning/replication; existing objects and permissions covered? |
| Images/AMIs | ECR and AMI copies present locally, including preexisting artifacts? |
| Secrets/keys | Regional Secrets Manager copies, regional KMS access, rotation and IAM tested? |
| Network | VPCs, routes, load balancers, addresses, peering/private endpoints ready? |
| Observability | Region-independent metrics/logs/traces and recovery alarms available? |
| Governance | CloudTrail/Security Hub aggregation deliberately configured; not mistaken for runtime recovery? |
| Operations | Templates, runbooks, approvals, ownership, drill/failback evidence available? |

## Transcript-specific service choices

- [[Amazon Route 53]] latency routing for Regional endpoints.
- [[Amazon CloudFront]] for cached static content and configured origin failover.
- [[AWS Secrets Manager]] for supported cross-Region secret replication.
- [[Amazon ECR]] for image replication to configured destinations; existing images need separate handling.
- [[AWS Transit Gateway]] for **inter-Region** peering with explicit routes.
- Regional [[Amazon EKS]] clusters with deliberate pod/node scaling.
- [[Amazon Aurora Global Database]] for a compatible global relational transactional design.
- [[AWS Global Accelerator]] for supported regional ALB/NLB endpoints.

Avoid essential dependencies only reachable in the primary Region. Central audit aggregation is useful but should not be required for the recovery application to serve requests.

## Sources

Tasks 3.1–3.3. See [[Resilience Framework and Dependency Isolation]].

- [ECR replication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/replication.html)
- [Transit gateway peering routes](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering-add-route.html)
- [[Domain 3 Official Sources]]
