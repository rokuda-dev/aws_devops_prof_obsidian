---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# DAX vs ElastiCache vs DynamoDB Global Tables

| Choice | Purpose | Exam distinction |
|---|---|---|
| DAX | DynamoDB-aware cache | Repeated eventual reads; strong/transactional reads pass through |
| ElastiCache | Application cache/session/data patterns using supported engines | Application selects data model, keys, expiration and consistency behavior |
| DynamoDB global tables | Multi-Region database replication | Persistent NoSQL regional access/availability, not a cache |
| CloudFront | Edge content delivery/cache | Static/media/HTTP objects, not arbitrary database-query caching |

A cache can reduce backend read pressure; it does not replace a durable recovery strategy. Include cache failure/cold-start behavior. DAX cost savings depend on workload/hit rate, not simply enabling the cluster.

Tasks 3.1–3.2. See [[Amazon DynamoDB Accelerator (DAX)]], [[Amazon ElastiCache]], [[Amazon DynamoDB]], [[Domain 3 Official Sources]].
