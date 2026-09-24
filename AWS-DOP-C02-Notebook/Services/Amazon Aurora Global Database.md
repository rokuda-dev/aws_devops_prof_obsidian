---
tags:
  - aws
  - dop-c02
  - domain-2
  - domain-3
  - aurora
read: true
---

# Amazon Aurora Global Database

Aurora Global Database spans one primary Region and one or more secondary Regions. The primary cluster handles writes; secondary clusters provide local reads and disaster-recovery targets.

## Operational choices

- **Switchover** — planned movement of the primary when the global database is healthy; designed to avoid data loss.
- **Failover** — unplanned recovery from a primary-Region outage; potential data loss depends on replication lag.

## Compared with a traditional cross-Region read replica

Aurora Global Database uses dedicated cross-Region replication infrastructure and is designed for global reads and regional recovery with typically sub-second replication. A traditional Aurora MySQL cross-Region replica uses binlog replication and generally has greater lag.

## Exam cue

Global relational application + local reads + low RTO/RPO regional recovery → Aurora Global Database.

Do not confuse with [[Amazon DynamoDB]] Global Tables, which are multi-active NoSQL replicas.

## Writes, endpoints, and limits

Current documentation allows up to 10 secondary clusters in distinct Regions. Write forwarding can accept requests through a secondary and forward them to the primary; it does not make the secondary an independent writer. The Global Database writer endpoint follows the current primary after managed regional changes.

## IAM, encryption, and recovery

Use appropriate database authentication, security groups, and regional encryption access. Check engine/version/Region compatibility before assuming every managed switchover/failover feature is available. Replication is not backup: corruption or unwanted writes can propagate.

Regional disaster recovery must include application reconnection, dependent services, and tested failover procedures, not just a replica cluster. Sub-second replication is typical behavior, not a guaranteed zero-loss RPO for unplanned outages.

## Official AWS references

- [Current Global Database overview](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html)
- [Aurora MySQL cross-Region binlog replica](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.CrossRegion.html)
- [[DynamoDB Global Tables vs Aurora Global Database]]

## Domain 3 — safe regional recovery

Compare a traditional Aurora MySQL binlog replica with the Global Database storage-based replication design; do not reuse one topology's failover recipe blindly.

RDS → [[Amazon SNS]] → [[AWS Lambda]] can convey notifications, but **RDS notifications can take up to five minutes and are not ordered**. Confirm failure independently and make recovery idempotent. Prefer supported managed Global Database recovery where appropriate.

Monitor lag, fence old writing when necessary, verify the new writer, reconnect applications, and coordinate traffic. [[Amazon Route 53]] changes answers, not database role. Current [[Amazon Application Recovery Controller]] Region switch can coordinate supported database-specific recovery actions.

Tasks 3.1 and 3.3. See [[RDS Multi-AZ vs Read Replicas vs Aurora Global Database]], [[Disaster Recovery Testing and Failback]].
- [Event delivery limitations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.overview.html)
