---
tags:
  - aws
  - dop-c02
  - domain-3
verified: 2026-09-18
read: true
---

# Elastic Load Balancing

## Choose the load balancer

| Type | Typical cue | Cross-zone default |
|---|---|---|
| Application Load Balancer (ALB) | HTTP/HTTPS, host/path routing, weighted target groups | On at load-balancer level; target-group override can disable it |
| Network Load Balancer (NLB) | TCP/UDP/TLS, network-level distribution | Off by default; configurable |
| Gateway Load Balancer (GWLB) | Transparent insertion/scaling of network appliances | Off by default; configurable |

Multi-AZ registration improves availability only when targets, state dependencies, and capacity can survive the loss of a zone. Health checks should detect meaningful application failure without creating a shared-dependency failure cascade.

## Cross-zone balancing

Enabled: a load-balancer node can send traffic to eligible targets in other enabled zones. Disabled: provide sufficient healthy capacity in each serving zone. Disabling cross-zone does not automatically create per-AZ ASG policies or metric dimensions.

Do not infer universal cost savings. NLB cross-AZ traffic can have data-transfer cost implications; ALB and NLB billing behavior is not interchangeable. Consider zonal isolation, capacity, and architecture as well as latency/cost.

## NLB DNS health and fail-open

Target-group health thresholds control DNS failover and routing failover. With cross-zone off, thresholds are evaluated against zonal targets; with it on, against targets across enabled zones. Count and percentage thresholds can both apply.

A failing attached target group can cause zonal DNS withdrawal that affects every target group on the NLB. Cached DNS answers can still reach that zone. If all zones fail health requirements, fail-open behavior can send traffic to unhealthy targets; health checks are not an absolute traffic-blocking guarantee.

Transcript example: A1 unhealthy, A2 healthy; B1 and B2 healthy. With cross-zone on and default healthy-count thresholds, each target group has a healthy target across zones, so both zonal IPs can remain in DNS. Different configured thresholds can change the result.

## Canary deployments

One ALB can split traffic between old/new target groups backed by separate ASGs. A separate ALB/stack is also possible, with a separate traffic-switching mechanism. Specify monitoring, observation duration, capacity, session behavior, and rollback.

**Trap:** ALB weighted target groups do not automatically transfer an unhealthy group's assigned weight to another healthy group. Use an explicit release controller or operational rollback. Database/schema compatibility remains necessary.

## Sources

Tasks 3.1–3.2. See [[Amazon EC2 Auto Scaling]], [[Deployment Strategy Matrix]], [[Domain 3 Transcript Corrections]].

- [ALB target-group attributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-target-group-attributes.html#modify-cross-zone)
- [NLB target groups and health thresholds](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html)
- [AWS guidance on weighted ALB groups](https://repost.aws/knowledge-center/elb-make-weighted-target-groups-for-alb)

## Domain 4 — ALB request logs

Configure ALB logs separately from ECS container logs. Traditional direct-to-S3 delivery needs an authorized same-Region bucket and supports SSE-S3. Delivery is eventually consistent/best effort, not an exact request ledger.

Current docs also describe enhanced CloudWatch Logs integrations with CloudWatch Logs/Firehose/S3 destinations. Check the selected path's permissions/encryption/format rather than treating legacy constraints as universal.

Target health governs routing but does not prove every business transaction succeeds.

Tasks 4.1 and 4.3. See [[Log Lifecycle Security and Integrity]], [[Domain 4 Scenario Decisions]].
- [Legacy and enhanced logging notice](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html)

## Domain 5 — response boundaries

Unused-resource recommendations require dependency/standby/traffic investigation before removal. During deployment failures, inspect target health/path/port/grace timing and network access; do not destroy a low-traffic recovery endpoint blindly.

Tasks 5.1–5.3 where applicable. [[Domain 5 Scenario Decisions]], [[Safe Event-Driven Remediation]], [[Domain 5 Official Sources]].
