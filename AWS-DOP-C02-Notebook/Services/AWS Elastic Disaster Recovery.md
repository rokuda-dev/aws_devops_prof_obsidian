---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# AWS Elastic Disaster Recovery

## Role and exam cue

Replicate supported server disks continuously into an AWS staging environment and orchestrate recovery instances. Useful for physical/virtual on-premises servers, other clouds, and supported EC2 recovery designs; cross-Region and cross-AZ recovery can be supported.

The staging model reduces the cost of maintaining full production capacity while preserving a recoverable server image. Recovery still needs networking, IAM, credentials, capacity, application startup, dependencies, and traffic changes.

## RTO/RPO interpretation

Low RPO and recovery in minutes are product design objectives/typical behavior, not guarantees for every workload. Measure replication lag and complete application recovery time. Block-level replication is crash-consistent; application consistency and transactional correctness need explicit design/validation.

## Choosing the tool

- Recover a supported server workload with continuous disk replication → consider Elastic Disaster Recovery.
- Recover managed RDS/Aurora databases → use appropriate managed database replication/backup mechanisms.
- Coordinate routing and application recovery → combine with [[Amazon Application Recovery Controller]], [[Amazon Route 53]], or other orchestration as suitable.
- Preserve independent historical recovery points → plan backups as well; replication can propagate bad changes.

Test launch settings, isolated recovery drills, boot behavior, dependency order, and failback. Avoid unintended writes from drill instances.

## Sources

Task 3.3. See [[Disaster Recovery Strategies]], [[RTO RPO SLA SLO and Error Budgets]].

- [Elastic Disaster Recovery concepts](https://docs.aws.amazon.com/drs/latest/userguide/CloudEndure-Concepts.html)
