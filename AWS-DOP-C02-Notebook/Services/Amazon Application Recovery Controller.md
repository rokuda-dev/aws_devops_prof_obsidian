---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# Amazon Application Recovery Controller

## Current name and capabilities

Amazon Application Recovery Controller (ARC), formerly Amazon Route 53 Application Recovery Controller. Choose the capability matching the recovery problem:

| Capability | Purpose | Not a substitute for |
|---|---|---|
| Zonal shift / zonal autoshift | Shift supported application traffic away from an impaired AZ | Regional data recovery |
| Routing control and safety rules | Highly available control of DNS-based traffic shifts | Replication or database promotion |
| Readiness checks | Assess configured resource readiness/consistency for existing customers | Proof of runtime application health |
| Region switch | Orchestrate recovery actions across a multi-Region application | Designing and testing a recovery plan |

## Region switch

Execution plans can coordinate supported recovery blocks and custom logic. Current documented blocks include RDS read-replica promotion; use the database-specific block appropriate to the topology.

Do not confuse RDS **PromoteReadReplica** with the separate **SwitchoverReadReplica** action, whose documented engine scope differs. For MySQL regional recovery, use supported promotion behavior rather than assuming an Oracle-specific switchover block applies.

Include capacity, writer readiness, traffic shift, approval/safety gates, verification, and failure handling. Grant narrowly scoped permissions for every action. Supported services/features/Regions must be checked when implementing.

## Recovery boundaries

ARC does not replicate application data or determine an application's acceptable loss automatically. Routing control changes traffic eligibility; the target must already be capable of serving it safely. Readiness checks and failover drills serve different purposes.

> [!warning] Current availability
> ARC readiness checks closed to new customers on April 30, 2026. Existing customers can continue using them. Region switch, routing controls, zonal shift, and zonal autoshift remain supported.

## Sources

Tasks 3.1 and 3.3. See [[Disaster Recovery Strategies]], [[Disaster Recovery Testing and Failback]].

- [ARC capabilities](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html)
- [Readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html)
- [Region switch RDS promotion block](https://docs.aws.amazon.com/r53recovery/latest/dg/rds-promote-read-replica-block.html)
- [Separate RDS switchover block and supported engine](https://docs.aws.amazon.com/r53recovery/latest/dg/rds-switchover-read-replica-block.html)
