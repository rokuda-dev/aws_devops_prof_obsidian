---
tags:
  - aws
  - dop-c02
  - domain-2
  - dynamodb
read: true
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

## Global Tables consistency modes

Global Tables support multi-Region eventual consistency (MREC) and multi-Region strong consistency (MRSC), with different topology/Region/feature restrictions. Do not state that all global tables are eventually consistent. MREC asynchronous conflict handling uses last-writer-wins; MRSC synchronously replicates writes and supports strongly consistent reads when requested.

## Stream-consumer operations

Design Lambda processing to tolerate duplicate delivery. A failed record/batch can delay progress; configure supported partial-batch handling, retry/failure destinations, and monitoring appropriately. Per-item ordering is not a universal global ordering of every item modification.

Scope execution-role access to the stream and downstream resources. Restrict table administration separately from application data access; ensure backups/restoration are tested.

## Official AWS references

- [DynamoDB overview](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
- [Global Tables operational readiness and consistency](https://aws.amazon.com/blogs/database/best-practices-for-amazon-dynamodb-global-tables-part-1-operational-readiness/)
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
