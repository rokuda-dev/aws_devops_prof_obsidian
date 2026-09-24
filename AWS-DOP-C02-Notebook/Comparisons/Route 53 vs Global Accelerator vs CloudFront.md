---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# Route 53 vs Global Accelerator vs CloudFront

| Choice | Routing layer/role | Main cue | Boundary |
|---|---|---|---|
| Route 53 | DNS routing and health-based answers | Regional API custom domains, latency or primary/secondary DNS | Resolver caches and client connections affect failover |
| Global Accelerator | Static anycast IP frontend and supported endpoint routing | Stable IPs and regional ALB/NLB/EC2/EIP endpoint recovery | Not a cache; not direct API Gateway/RDS endpoint support |
| CloudFront | HTTP content distribution/cache and origin selection | Global static/media delivery, cached S3 content | Does not replicate databases; origin failover has method/status constraints |

All require working backends and appropriate data architecture. None automatically promotes an RDS replica merely by shifting customer traffic.

Tasks 3.1–3.3. See [[Amazon Route 53]], [[AWS Global Accelerator]], [[Amazon CloudFront]], [[Domain 3 Official Sources]].
