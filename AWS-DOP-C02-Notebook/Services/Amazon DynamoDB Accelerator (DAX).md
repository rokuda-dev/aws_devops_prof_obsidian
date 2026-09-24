---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# Amazon DynamoDB Accelerator (DAX)

## Role

Managed, DynamoDB-compatible in-memory caching for repeated eventually consistent reads. Use when the same keys/queries are requested repeatedly and the workload tolerates cached data. DAX is not cross-Region database replication.

| Request/requirement | DAX implication |
|---|---|
| Repeated eventually consistent reads | Can benefit from item/query caching |
| Strongly consistent reads | Forwarded to DynamoDB; not cached |
| Transactional reads | Forwarded to DynamoDB; not cached |
| More write capacity | Cache does not increase DynamoDB write capacity |
| Regional disaster recovery | Use database replication/recovery, not DAX alone |

Use a DAX-compatible client and appropriate VPC networking/IAM. Select a resilient multi-node, multi-AZ configuration where required. Cache TTL and invalidation behavior affect freshness. Queries and item reads have distinct cache behavior; do not assume every write immediately refreshes every cached query result.

## Cost and failure considerations

DAX has cluster costs. Offloaded reads can reduce DynamoDB read consumption, but total cost savings depend on hit rate, provisioned cache size, traffic, and pricing. “Always cheaper” is incorrect.

Plan connection limits, cache misses, cold-cache load, and application behavior when cache nodes fail. Do not let a cache outage overwhelm the underlying table.

## Sources

Tasks 3.1–3.2. See [[DAX vs ElastiCache vs DynamoDB Global Tables]], [[Amazon DynamoDB]].

- [DAX consistency and request handling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.consistency.html)
