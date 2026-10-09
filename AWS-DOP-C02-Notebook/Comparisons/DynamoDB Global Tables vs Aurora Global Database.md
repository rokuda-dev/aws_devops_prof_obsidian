---
tags: [aws, dop-c02, comparisons]
updated: 2026-09-18
read: false
---

# DynamoDB Global Tables vs Aurora Global Database

| Dimension               | [[Amazon DynamoDB]] Global Tables                                           | [[Amazon Aurora Global Database]]                      |
| ----------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------ |
| Data model              | Key-value/document NoSQL                                                    | Relational MySQL/PostgreSQL-compatible                 |
| Regional write model    | Multi-active replicas                                                       | One primary write cluster                              |
| Consistency/replication | MREC asynchronous or MRSC synchronous, with different restrictions          | Storage-layer asynchronous replication                 |
| Secondary writes        | Every replica can serve reads and writes; there is no primary/secondary replica topology | Supported write forwarding sends writes to the primary |
| Account topology        | Same-account or multi-account MREC; MRSC is same-account only                | Global cluster members use the service's supported cross-Region cluster topology |
| Recovery                | Application can use another suitable replica; routing/design still required | Managed switchover/failover promotes a secondary       |
| Planned change          | Depends on app/routing/table design                                         | Switchover, healthy database, no data loss             |
| Outage caveat           | Consistency mode/topology determine semantics                               | Failover may lose unreplicated writes                  |

> [!warning]
> “Global” does not mean the same architecture. DynamoDB is not relational; Aurora write forwarding is not multi-active independent writes. Replication is not a substitute for backup.

Current references: [DynamoDB Global Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html), [Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html).
