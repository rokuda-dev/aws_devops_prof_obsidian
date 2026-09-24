---
tags:
  - aws
  - dop-c02
  - domain-3
verified: 2026-09-18
read: true
---

# Amazon Route 53

## Domain 3 routing choices

| Policy | Use |
|---|---|
| Failover | Primary/secondary DNS answers based on configured health |
| Latency | Route toward a Region with favorable measured network latency |
| Weighted | Controlled traffic split, such as release testing |
| Other policies | Match geographic, proximity, or address-selection requirements explicitly |

Latency routing is not necessarily nearest geography or lowest application execution time. A record policy does not provision capacity, replicate data, or promote a database.

## Health checks

Use endpoint health checks, CloudWatch-alarm checks, or calculated checks as appropriate. Evaluate Target Health on supported aliases lets a routing tree incorporate target health. Check the complete alias tree, not just the top record. Do not assume Evaluate Target Health is available for every AWS alias type.

Public health checkers cannot directly probe an arbitrary private VPC IP. Use a private probe that publishes a metric/alarm, then an alarm-based health check when suitable. Ensure health checks test the intended endpoint; they are separately configured, not automatically identical to the DNS record target.

## DNS timing

Failover changes authoritative answers; clients and recursive resolvers can retain prior answers until cache expiry. A lower configurable TTL helps but is not an end-to-end recovery guarantee. Alias TTLs can be determined by the target service. Existing connections may persist independently of DNS.

You can flush caches you control, not every customer's resolver. Plan for reconnection/retries and test actual client behavior. When every relevant record is unhealthy, Route 53 can return records under its fail-open behavior; do not treat DNS health as a strict firewall.

## Database failover gate

Promote the recovery replica, verify write readiness and acceptable data freshness, start/scale the recovery app, then shift traffic. Use fencing to avoid two independent writers. A read-only replica is not a recovered primary merely because DNS points toward it.

## Sources

Tasks 3.1–3.3. See [[Route 53 vs Global Accelerator vs CloudFront]], [[Disaster Recovery Testing and Failback]].

- [Configuring DNS failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring.html)
- [Complex failover configurations](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html)
