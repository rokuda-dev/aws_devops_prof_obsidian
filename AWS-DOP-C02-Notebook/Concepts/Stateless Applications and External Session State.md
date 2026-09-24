---
tags: [aws, dop-c02, concepts]
updated: 2026-09-18
read: false
---

# Stateless Applications and External Session State

Instances/tasks must be replaceable when using Auto Scaling, immutable deployment, or blue/green releases. Instance-local sessions/files create a hidden dependency on the old host.

| State | Externalization choice | Design caveat |
|---|---|---|
| Fast shared user sessions/cache | [[Amazon ElastiCache]] | Pick resilience/durability/loss tolerance deliberately |
| Key-based durable sessions | [[Amazon DynamoDB]] | Access patterns, TTL, capacity/consistency |
| Shared Linux filesystem | [[Amazon EFS]] | Network, permissions, AZ/deployment-model resilience |
| Durable objects/assets | [[Amazon S3]] | Object API, not mounted POSIX semantics |
| Local block data | [[Amazon EBS]] | AZ scope, attach/replacement/backup lifecycle |

> [!exam]
> A user loses a session when Auto Scaling replaces a host → externalize state. Stickiness may keep requests on one instance but does not make that instance's state durable.

Traffic rollback does not restore incompatible database changes. Use expand/contract schemas and old/new application compatibility.

See [[AWS Storage and Stateless Application Patterns]] and [[Deployment Strategy Matrix]].

