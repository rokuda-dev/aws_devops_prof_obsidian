---
tags:
  - aws
  - dop-c02
  - domain-2
  - dynamodb
read: false
---

# Amazon DynamoDB

DynamoDB is a serverless managed key-value/document database designed for consistent single-digit millisecond performance at scale.

## Exam-relevant capabilities

- On-demand capacity for unpredictable traffic; provisioned capacity where explicit capacity control is appropriate.
- DynamoDB Streams captures an ordered sequence of item-level modifications and can trigger Lambda.
- Global Tables provide multi-Region, multi-active replication.
- Point-in-time recovery and on-demand backups.
- Encryption at rest by default.

## Event-driven pattern

```text
item insert/update/delete → DynamoDB Stream → Lambda → automation
```

## Distinction

DynamoDB Global Tables accept writes in multiple replica Regions. [[Amazon Aurora Global Database]] normally uses one primary write Region and read-oriented secondary clusters.

## Secondary indexes — LSI vs GSI

Secondary indexes provide alternate `Query` access patterns; DynamoDB does not choose an index automatically as a relational query optimizer would. The application names the index, and DynamoDB maintains its entries when the base-table items change.

| Decision point   | Local secondary index (LSI)                                                                       | Global secondary index (GSI)                                                                                                                |
| ---------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Key schema       | ==Same partition key as the base table==; a different sort key is required                        | A different partition key and optional sort key; either can differ from the base table                                                      |
| Query scope      | One base-table partition-key value                                                                | Data across all base-table partitions                                                                                                       |
| Lifecycle        | Must be defined when the table is created; ==**cannot later be added or deleted independently**== | Can be created with the table or added/deleted later                                                                                        |
| Read consistency | Eventually or strongly consistent                                                                 | Eventually consistent only                                                                                                                  |
| Capacity         | Uses the base table's read/write capacity                                                         | Has separate provisioned read/write capacity when the table uses provisioned mode; table and GSI scaling policies are configured separately |
| Size and count   | Item collection for any one partition-key value is limited to 10 GB; up to 5 LSIs per table       | No per-partition-key-value size restriction; 20 GSIs per table is the default quota                                                         |

Use an LSI when the access pattern must retain the base table's partition key but needs another ordering/range condition, and strong reads are required. The create-time-only choice and 10 GB item-collection limit make an LSI a deliberate data-model decision. Use a GSI when the access pattern needs a different partition key, must span the table, or may need to be introduced after table creation.

### Worked table example

An `Orders` table can store these simplified items:

| `CustomerId` | `OrderKey` | `TotalCents` | `FulfillmentKey` | `CreatedAt` |
|---|---|---:|---|---|
| `CUSTOMER#42` | `2026-10-03T09:00:00Z#ORDER#9001` | 12900 | `WAREHOUSE#FRA#PENDING` | `2026-10-03T09:00:00Z` |
| `CUSTOMER#42` | `2026-10-04T14:30:00Z#ORDER#9015` | 4500 | `WAREHOUSE#BER#SHIPPED` | `2026-10-04T14:30:00Z` |

The table and indexes expose different access patterns over the same items:

| Target | Partition key | Sort key | Example access pattern |
|---|---|---|---|
| Base table | `CustomerId` | `OrderKey` | Query one customer's orders in chronological order |
| `OrdersByAmount` LSI | `CustomerId` | `TotalCents` | Query one customer's highest-value orders; a strongly consistent query is allowed |
| `OrdersByFulfillment` GSI | `FulfillmentKey` | `CreatedAt` | Query pending orders for one warehouse by creation time; results are eventually consistent |

The LSI reuses `CustomerId`, so it cannot query across customers. The GSI introduces a new partition key and can group items independently of the customer partition. Using only `PENDING` as the GSI partition key would concentrate traffic on a low-cardinality value; prefixing it with a warehouse distributes that workload better, although a very busy warehouse might still require write sharding.

### Projection, sparsity, and operational traps

- `KEYS_ONLY`, `INCLUDE`, and `ALL` control which attributes are copied into an index. Smaller projections reduce index storage and write cost. A GSI query cannot fetch non-projected attributes from the base table; an LSI query can, but doing so consumes additional base-table read capacity.
- An item appears in a secondary index only when its index key attributes are present. This enables a sparse-index pattern for querying a selected subset of items.
- GSI updates are asynchronous. A newly written item might not immediately appear in a GSI query, and strong consistency cannot be requested against a GSI.
- A GSI has its own partition distribution. A low-cardinality or skewed GSI partition key can become hot even when the base table is well distributed. Insufficient GSI write capacity or a hot GSI partition can apply back-pressure and throttle writes to the base table.
- Adding a GSI to an existing table performs an online backfill. Monitor the index build and provision enough write capacity for the backfill and continuing application traffic.

**Exam clue:** “query by a new partition key” usually points to a GSI. “Same partition key, alternate sort order, strong read” points to an LSI—but only if it was designed when the table was created.

## Global Tables consistency modes

Global Tables support multi-Region eventual consistency (MREC) and multi-Region strong consistency (MRSC), with different topology/Region/feature restrictions. Do not state that all global tables are eventually consistent. MREC asynchronous conflict handling uses last-writer-wins; MRSC synchronously replicates writes and supports strongly consistent reads when requested.

Current Global Tables also distinguish account ownership. Same-account global tables keep all replicas under one account boundary. Multi-account global tables place replicas in different accounts with distinct IAM, KMS, billing, CloudTrail, and governance boundaries. Both models are multi-active, but MRSC is supported only for same-account global tables; a multi-account design uses MREC. Account topology and consistency mode are separate choices.

## Stream-consumer operations

Design Lambda processing to tolerate duplicate delivery. A failed record/batch can delay progress; configure supported partial-batch handling, retry/failure destinations, and monitoring appropriately. Per-item ordering is not a universal global ordering of every item modification.

Scope execution-role access to the stream and downstream resources. Restrict table administration separately from application data access; ensure backups/restoration are tested.

## Official AWS references

- [DynamoDB overview](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
- [Secondary-index comparison](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html)
- [GSI write throttling and back-pressure](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/gsi-throttling.html)
- [Secondary-index design best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-indexes.html)
- [Global Tables operational readiness and consistency](https://aws.amazon.com/blogs/database/best-practices-for-amazon-dynamodb-global-tables-part-1-operational-readiness/)
- [Current Global Tables consistency and account models](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html)
- [[DynamoDB Global Tables vs Aurora Global Database]]

## Domain 3 — capacity, caching, and regional state

Provisioned-mode [[AWS Application Auto Scaling]] adjusts read/write capacity within configured bounds; table and GSI policies must be considered separately. Reactive changes do not prevent every burst throttle. On-demand mode manages capacity without these provisioned target-tracking policies. Hot keys require data-model analysis.

[[Amazon DynamoDB Accelerator (DAX)]] caches eligible eventual reads; strong and transactional reads pass through. Global tables replicate database state across Regions and are not a cache or a drop-in relational replacement.

Tasks 3.1–3.2. See [[DAX vs ElastiCache vs DynamoDB Global Tables]], [[Scaling Metrics and Troubleshooting]].
- [Provisioned Auto Scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html)

## Domain 4 — registration automation

ASG changes can invoke an authorized Lambda to update registrations. Use idempotent keys/live-membership reconciliation instead of assuming ordered exactly-once events.

Provisioned throughput auto scaling is separate from EC2 membership and DAX caching.

Task 4.3. See [[AWS Application Auto Scaling]], [[Safe Event-Driven Remediation]].
