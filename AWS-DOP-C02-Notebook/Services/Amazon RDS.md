---
tags:
  - aws
  - dop-c02
  - domain-3
verified: 2026-09-18
read: true
---

# Amazon RDS

## Deployment and replication distinctions

| Design | Main objective | Recovery characteristic |
|---|---|---|
| Multi-AZ DB instance | Regional/AZ high availability | Synchronous standby; standby is not a read-scaling endpoint |
| Multi-AZ DB cluster | Regional HA and reader capacity | Different topology and supported engine/version behavior |
| Read replica | Read scaling; optional regional DR | Asynchronous replication; explicit promotion for independent writing |
| Snapshot/backup restore | Point-in-time or backup recovery | Provision/restore time and backup age determine recovery objectives |

Do not confuse [[Amazon Aurora Global Database]] with ordinary RDS read replicas or traditional Aurora MySQL binlog replicas.

## Major-version upgrade

Changing CloudFormation EngineVersion requests an upgrade; it is not a minimal-downtime architecture. Verify supported upgrade paths, parameter/feature compatibility, major-upgrade permissions, backups, prechecks, maintenance behavior, and application tests.

For a **classic Multi-AZ DB instance**, a major upgrade can affect primary and standby together and cause downtime. For a **Multi-AZ DB cluster**, engine-specific behavior differs: current MySQL major upgrades can upgrade members sequentially, while PostgreSQL major upgrades upgrade members together. Do not generalize one topology to all RDS.

For RDS MySQL, upgrade read replicas before upgrading the source when required by the documented upgrade path. A newly created replica is not automatically a safe writable fallback for an incompatible major-version change.

## Blue/Green Deployments

For supported RDS MariaDB, MySQL, and PostgreSQL configurations, maintain a synchronized green environment, upgrade/test it, then perform a guarded switchover. Support depends on engine/version/features; Aurora has its own documentation.

Typically short switchover downtime is not a universal SLA or an automatic rollback guarantee after new writes. Test application reconnection, replication lag, incompatible DDL, and rollback/data-divergence implications. See [[RDS Blue Green vs EngineVersion Update vs Read Replica Promotion]].

## Cross-Region recovery

Monitor replica lag, promote a replica explicitly, verify writer readiness, update/reconnect applications, and shift traffic. Async replication can lose recent writes after a regional outage. Fence the old writer; returning to the old Region requires deliberate replication/failback work.

RDS event notifications may take up to five minutes and are not ordered. SNS → Lambda can be part of automation, but one notification is not a sufficient instantaneous failure detector. Combine health evidence, validation, idempotency, permissions, and operator/automation safeguards.

## Sources

Tasks 3.1 and 3.3. See [[Domain 3 Scenario Decisions]].

- [RDS overview — official resource](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
- [RDS Blue/Green overview](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-overview.html)
- [Multi-AZ DB cluster upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-upgrading.html)
- [RDS MySQL upgrade strategies](https://aws.amazon.com/blogs/database/upgrade-strategies-for-amazon-rds-for-mysql-8-0-to-8-4/)
- [RDS event notification behavior](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.overview.html)

## Domain 5 — operational event response

Creation/restart/deletion, failover, storage and configuration notifications can route to handlers/notifications. Supplement source-specific events with database/app metrics and health evidence; notification lag/order already documented above means they are not instant authoritative application-health probes.

For scheduled updates, inspect impact/maintenance and recovery plans; do not trigger arbitrary reboots or replica promotion from every notification.

Tasks 5.1–5.2. [[Event Sources and Response Contracts]], [[AWS Health]], [[Safe Event-Driven Remediation]].
