---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# Domain 3 Architecture Patterns

| Requirement | Architecture pattern | Recovery/rollback safeguard |
|---|---|---|
| Release EC2 web version safely | ALB weighted target groups + separate ASGs, or separate stack with controlled traffic shift | Health gates, explicit rollback, compatible sessions/schema |
| Survive AZ failure | Multi-AZ targets, sufficient surviving capacity, suitable regional state HA | Enable ASG ELB health replacement; avoid shared single-AZ dependency |
| Major MySQL upgrade with reduced downtime | Supported RDS Blue/Green design, synchronized/tested green environment | Compatibility/prechecks, guarded switchover, reconnect and data-aware rollback |
| Scale photo-sharing web tier quickly | Multi-AZ ASG + ALB, prebuilt AMI, external DynamoDB sessions, S3 media | Publish launch-template version, instance refresh, initialization health |
| Repeated DynamoDB eventual reads | DAX in a resilient regional configuration | Strong/transactional reads pass through; cold-cache fallback |
| Global static/media delivery | CloudFront in front of S3 | Cache freshness and authorized origin access; separate object replication |
| Multi-Region Regional API | Separate APIs + same custom domain per Region + Route 53 latency/health routing | Regional certs/configuration and data readiness; no direct GA API endpoint |
| Global relational EKS application | Regional EKS clusters, Aurora Global Database, supported GA ALB/NLB endpoints | Single relational writer, pod/node scaling, reconnect after writer changes |
| RDS regional DR | Cross-Region async replica, recovery application stack, promotion workflow, Route 53 failover | Lag validation, old-writer fencing, write-ready gate before traffic |
| Server-based hybrid DR | Elastic Disaster Recovery staging/replication and tested recovery launch | Full network/dependency/app recovery, not disk replication alone |
| Central recovery-point policy | AWS Backup with supported copy rules and protected destination | Copy freshness, key access, restore + application validation |
| Coordinated recovery | ARC Region switch or explicit SSM/Step Functions orchestration | Idempotent actions, bounded retries, approvals/safety gates |

## Recovery workflow ownership

Traffic control, compute capacity, data recovery, and application validation are different responsibilities. Route 53/Global Accelerator are not database promotion services; replicas are not release rollback plans; Config drift checks are not DR drills.

Tasks 3.1–3.3. See [[Domain 3 Scenario Decisions]], [[Disaster Recovery Strategies]], [[Domain 3 Official Sources]].
