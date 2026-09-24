---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# RDS Multi-AZ vs Read Replicas vs Aurora Global Database

| Choice | Write/replication model | Best cue | Important limitation |
|---|---|---|---|
| RDS Multi-AZ DB instance | Primary + synchronous standby | AZ HA and automatic regional failover | Standby not a read endpoint; not regional DR |
| RDS Multi-AZ DB cluster | Writer + reader topology, engine-specific | Regional HA with readable members | Different supported features/upgrade behavior from DB instance |
| RDS cross-Region read replica | Async copy of source | Read scaling and regional recovery target | Lag and explicit promotion; application/routing steps still needed |
| Traditional Aurora MySQL cross-Region replica | Binlog-based replication | Existing compatible replica design | Not the same mechanism as Global Database |
| Aurora Global Database | One primary Region, storage-based regional replication | Global relational reads and low recovery objectives | Secondary not an independent writer; outage failover can lose lagging writes |
| DynamoDB global tables | NoSQL multi-Region design; selected consistency mode | Compatible globally distributed NoSQL application | Not a drop-in relational replacement |

Planned Aurora switchover and unplanned failover have different data-loss implications. Write forwarding does not create a multi-primary Aurora database.

Tasks 3.1 and 3.3. See [[Amazon RDS]], [[Amazon Aurora Global Database]], [[DynamoDB Global Tables vs Aurora Global Database]], [[Domain 3 Official Sources]].
