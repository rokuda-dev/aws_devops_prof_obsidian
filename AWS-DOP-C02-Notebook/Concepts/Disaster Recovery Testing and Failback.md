---
tags:
  - aws
  - dop-c02
  - domain-3
verified: 2026-10-07
read: false
---

# Disaster Recovery Testing and Failback

## Test the service, not merely resource existence

Record business success criteria, recovery timestamp boundaries, actual recovered data age, end-to-end recovery time, and evidence. Exercise the same permissions, keys, artifacts, and network paths needed during a real outage.

| Drill | What it proves or exposes |
|---|---|
| Backup restore + data/application validation | Recovery points are usable, not merely created |
| Regional failover | Promotion, capacity, routing and reconnection work together |
| Isolation from primary dependencies | Recovery Region can operate autonomously |
| Configuration drift review | Templates/configuration match intended recovery deployment |
| Failure during recovery | Retries, approvals, rollback, idempotency and safe stopping work |
| Failback | Writes made during the outage are preserved and protection restored |

## Drift tools versus recovery proof

[[AWS Config]] can detect configured compliance/drift conditions and trigger remediation with appropriate rules/workflows. [[AWS CloudFormation]] drift detection compares supported properties to template expectations. Neither proves application/data recovery, nor covers every runtime configuration automatically.

Use [[AWS Systems Manager]] Automation for controlled repair/runbooks. Permissions, approvals, concurrency, rollback, and exception handling matter.

## Failback safeguards

Do not simply change DNS to the old database. Fence writers, reconcile divergence, rebuild replication in the needed direction, verify freshness and capacity, then perform the planned traffic/writer transition. Reestablish backups, alarms, and redundancy.

## Controlled fault tests

AWS Fault Injection Service experiments perform real disruptive actions and can use CloudWatch alarm stop conditions. Use isolated targets, limited blast radius, and explicit cleanup; stopping an experiment does not necessarily undo every induced state. Resilience Hub defines resilience goals, assesses supported application resources against them, and recommends improvements. An assessment is not a fault experiment, and neither replaces a successful restore/failover drill with measured RTO/RPO.

Keep the lifecycle distinct:

```text
Resilience policy/assessment -> controlled fault experiment -> recovery execution -> application/data validation -> failback
```

See [[Resilience Hub vs FIS vs Backup vs DRS vs ARC]] for the service-selection boundary.

## Sources

Task 3.3, with clearly labeled supplementary testing tools.

- [AWS Backup restore testing](https://aws.amazon.com/blogs/storage/implementing-restore-testing-for-recovery-validation-using-aws-backup/)
- [Resilience testing](https://docs.aws.amazon.com/resilience-hub/latest/userguide/arh-testing.html)
- [AWS Fault Injection Service concepts and stop conditions](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html)
- [AWS Config — official resource](https://docs.aws.amazon.com/config/latest/developerguide/aws-config-landing-page.html)
