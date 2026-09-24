---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# Disaster Recovery Strategies

## Match objectives before naming a strategy

| Strategy | Recovery Region before failure | Relative trade-off |
|---|---|---|
| Backup and restore | Recoverable backups; infrastructure rebuilt/restored | Lower standing cost, usually longer recovery |
| Pilot light | Essential data/core components present; remaining compute started | Moderate preparation, scale/provision steps required |
| Warm standby | Complete functional deployment at reduced capacity | Faster recovery, more ongoing cost |
| Multi-site active/active | Multiple sites actively serve appropriate traffic | Potentially very fast recovery, high data/routing complexity |

These are architecture patterns, not guaranteed numerical RTO/RPO tiers. Active/passive can be pilot light or warm standby; active/active requires an explicit data-consistency/write-conflict model.

## Recovery sequence

1. Detect and confirm impairment; determine scope.
2. Fence or isolate the old writer when necessary.
3. Verify recoverable state and acceptable data age.
4. Promote/restore the appropriate database and provision/scale compute.
5. Validate application dependencies and write readiness.
6. Shift traffic and observe client recovery.
7. Stabilize, rebuild protection, and plan failback.

Use [[AWS Backup]] for supported recovery points/copies, [[AWS Elastic Disaster Recovery]] for supported server replication, and native database mechanisms for managed databases. Coordinate actions using [[AWS Systems Manager]], [[AWS Step Functions]], or [[Amazon Application Recovery Controller]].

## Common distractors

Multi-AZ is not cross-Region DR. Replication is not backup. Snapshot copying is not always “hours,” but cannot be assumed to meet a short objective without measured copy/restore times. Raising desired ASG capacity does not solve stale data, quotas, or missing regional dependencies.

## Sources

Task 3.3. See [[Multi-AZ vs Multi-Region]], [[Disaster Recovery Testing and Failback]].

- [Official Domain 3 recovery requirements](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain3.html)
- [[Domain 3 Official Sources]]
