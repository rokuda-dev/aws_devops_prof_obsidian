---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# Multi-AZ vs Multi-Region

| Dimension | Multi-AZ | Multi-Region |
|---|---|---|
| Failure boundary | Availability Zone within a Region | Regional impairment and geographic separation |
| State | Regional HA mechanisms, service dependent | Explicit cross-Region replication/restore and write topology |
| Latency/complexity | Usually less inter-site latency and operational complexity | More routing, data consistency, compliance and operations work |
| Typical cue | Survive an AZ outage | Geographically isolated DR or global local access |
| Missing protection | Does not alone survive regional failure or logical corruption | Does not alone prevent corrupted writes replicating |

Choose based on business requirements, not “more Regions is always better.” Global, regional, and zonal service scope affects where independent infrastructure must exist. Both patterns still need observability, capacity, backups, and drills.

Tasks 3.1–3.3. See [[Resilience Framework and Dependency Isolation]], [[Disaster Recovery Strategies]], [[Domain 3 Official Sources]].
