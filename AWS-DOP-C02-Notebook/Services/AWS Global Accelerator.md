---
tags:
  - aws
  - dop-c02
  - domain-3
verified: 2026-09-18
read: true
---

# AWS Global Accelerator

## Role and exam cue

Use static anycast IP addresses and the AWS global network to improve access to regional endpoints and shift new traffic toward healthy deployments. Good cue: multi-Region application behind supported load balancers, stable frontend IPs, and failover that avoids retargeting DNS records.

| Control | Meaning |
|---|---|
| Regional endpoint group traffic dial | Adjust the share directed to an endpoint group |
| Endpoint weight | Relative distribution among endpoints within a group |
| Health evaluation | Uses ELB health for ALB/NLB; accelerator checks for EC2/EIP endpoints |

Standard accelerator endpoint types include ALB, NLB, EC2 instances, and Elastic IP addresses. **API Gateway and RDS endpoints are not direct supported endpoints.** Multi-Region Regional APIs commonly use [[Amazon Route 53]]; do not attach API Gateway directly to Global Accelerator.

## Resilience boundaries

Stable IPs avoid DNS refresh when changing backend endpoint routing. This does not move existing connections, replicate state, or promote a database. Validate recovery capacity and data readiness before allowing writes.

Global Accelerator is not an object cache; [[Amazon CloudFront]] is the content-delivery/cache choice. Application availability still depends on endpoint health design, retry behavior, and regional dependencies.

## Sources

Tasks 3.1–3.3. See [[Route 53 vs Global Accelerator vs CloudFront]], [[Multi-Region Application Checklist]].

- [Global Accelerator FAQ and endpoint types](https://aws.amazon.com/global-accelerator/faqs/)
- [Endpoint health guidance](https://repost.aws/knowledge-center/global-accelerator-unhealthy-endpoints)
