---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# Domain 3 Scenario Decisions

## Transcript scenarios, corrected

| Scenario | Best first design | What must also be true |
|---|---|---|
| ASG + ALB, new release without disruption | Canary/blue-green with isolated old/new capacity | Explicit traffic controller, health gates, rollback, compatible shared data |
| Major RDS MySQL upgrade | Supported Blue/Green where suitable; otherwise plan/test supported upgrade downtime | Replica upgrade order and topology/engine behavior verified |
| ALB cross-zone override | Disable at target-group level if justified | Surviving zonal capacity and correct metrics/policies; LB-level setting stays on |
| NLB A1 unhealthy, A2 healthy; B1/B2 healthy | With cross-zone on/default thresholds, both IPs can remain in DNS | Every TG threshold evaluated; nondefault settings may change outcome |
| S3 media + DynamoDB repeated reads | CloudFront for media; DAX for eligible eventual database reads | Cache freshness, DAX client/networking, actual total cost |
| Aurora cross-Region failover | Prefer suitable Aurora Global Database managed recovery; compare existing binlog-replica design | Single writer, replication lag, safe promotion, reconnection and routing |
| Slow EC2 bootstrap | Tested golden AMI + ASG launch template; optionally warm pool | AMI is rolled out; secrets/config stay appropriately dynamic |
| ASG warm-pool event handling | EventBridge Origin/Destination filters + lifecycle action handler | Case-sensitive fields; correct ASG; retries and completion |
| EKS global transactional workload | Regional clusters + compatible Aurora Global Database; GA for supported LB endpoints | HPA versus node scaling configured; regional copies/dependencies ready |
| Regional API Gateway deployment | Regional APIs + same custom domain + Route 53 latency/health routing | Separate regional deployments; compatible state; client cache behavior |
| Scaling policy not responding | History/alarm/bounds first, then timing/launch/placement failures | Distinguish cooldown, warmup, lifecycle hooks and health grace |
| Scheduled action not responding | Check timezone/DST, history, conflicts, suspension and bounds | Capacity/IAM/template failures may still prevent launch |
| RPO five minutes, RTO two hours, geographic DR | Cross-Region RDS replica + pilot light or warm standby + recovery orchestration + Route 53 | Measured lag within RPO; complete recovery within RTO; promote before writes |
| Lowest feasible recovery time/data loss | Prepared recovery capacity and continuous suitable replication | No generic zero-loss guarantee; choose data topology, then prove objectives |
| Recovery configuration drift | Config rules/remediation and CloudFormation drift where supported | Also test restoration, real failover, data correctness and failback |

## Two-hour / five-minute reasoning

Do not answer solely “Route 53 failover.” Route 53 can redirect customers to a site that is still read-only or unprovisioned. Promotion, scale-up, dependencies, validation, DNS caching and client reconnection belong inside the two-hour recovery budget.

An async replica's lag must be observed; existence is not evidence that five minutes of maximum loss is achieved. Object storage and other state stores need their own objectives and mechanisms.

Tasks 3.1–3.3. See [[RTO RPO SLA SLO and Error Budgets]], [[Domain 3 Transcript Corrections]], [[Domain 3 Architecture Patterns]].
