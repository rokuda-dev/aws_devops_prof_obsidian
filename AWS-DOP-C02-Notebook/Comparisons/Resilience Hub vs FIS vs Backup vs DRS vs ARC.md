---
title: Resilience Hub vs FIS vs Backup vs DRS vs ARC
tags:
  - aws
  - dop-c02
  - comparisons
  - resilience
verified: 2026-10-07
read: false
---

# Resilience Hub vs FIS vs Backup vs DRS vs ARC

| Requirement | Best first thought | What it does not prove or provide |
|---|---|---|
| Define recovery objectives and assess supported application posture | AWS Resilience Hub | An assessment/recommendation is not a measured recovery test |
| Inject a controlled failure into real resources | AWS Fault Injection Service (FIS) | A stopped experiment does not necessarily undo every induced state or prove data recovery |
| Policy-managed recovery points, copies, restores, and restore testing | [[AWS Backup]] | A recovery point alone does not prove the complete application meets RTO/RPO |
| Continuously replicate supported servers for regional recovery | [[AWS Elastic Disaster Recovery]] | Application consistency, dependency recovery, routing, validation, and failback still require design |
| Coordinate supported zonal/regional recovery and traffic controls | [[Amazon Application Recovery Controller]] | Traffic control or orchestration does not create recovery capacity or independently promote every data store |

## Correct sequence

```text
Business RTO/RPO
  -> resilience policy and architecture assessment
  -> recovery mechanism and prepared capacity
  -> controlled failure/restore/failover test
  -> measure application and recovered-data outcome
  -> repair findings and test failback
```

Use Resilience Hub to identify posture gaps and recommended tests. Use FIS when the requirement is to create a real disruptive condition with scoped targets, roles, actions, and CloudWatch-alarm stop conditions. Use Backup or DRS for the actual recovery data/server mechanism as applicable. Use ARC, Step Functions, or Systems Manager Automation when ordered recovery coordination is required.

## Exam traps

- Estimated RTO/RPO is not achieved RTO/RPO.
- Fault injection is not a backup or disaster-recovery strategy.
- Backup creation is not restore validation.
- DNS or ARC traffic movement does not promote an unsupported database automatically.
- Stopping an FIS experiment is a safety control, not universal rollback of its effects.

Tasks 3.1 and 3.3. See [[Disaster Recovery Testing and Failback]], [[Disaster Recovery Strategies]], and [[RTO RPO SLA SLO and Error Budgets]].

## Official AWS references

- [AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html)
- [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html)
- [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)
- [AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html)
- [Amazon Application Recovery Controller](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html)

