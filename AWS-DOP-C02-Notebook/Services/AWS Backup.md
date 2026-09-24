---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# AWS Backup

## Role

Centralize backup policies, recovery points, retention, supported cross-Region/cross-account copies, and restore testing. Verify the service/Region feature matrix; not every resource supports every copy or restore feature.

A backup plan defines when backups and copies occur. A restore plan also needs keys, permissions, network configuration, application initialization, dependency sequencing, and traffic switching.

## RTO/RPO

Backup interval + completion/copy lag determines recovery-point age. Restore + infrastructure provisioning + validation + traffic/reconnection determines recovery time. A completed backup job does not prove either application objective.

Replication improves availability but is not an independent immutable backup. Choose retention and destination protections based on corruption, deletion, and account-compromise risks.

## Continuous-backup copy correction

Copying a supported continuous backup creates/copies a snapshot; continuous point-in-time recovery is not preserved as a live continuous stream at the destination. Current documentation does not support on-demand copies of continuous backups. Do not apply the transcript's generic “automatic or on-demand copy” claim to every backup type.

## Encryption and testing

Encryption behavior varies: fully managed backup resources can use independent vault encryption; other resources can inherit source-service encryption characteristics. Validate IAM, vault policy, and source/destination KMS access for both backup and restore.

Restore testing can schedule supported resource restores. Add application/data validation and report validation outcomes; resource restoration alone does not prove business continuity. Clean up test resources safely.

## Sources

Task 3.3. See [[Disaster Recovery Testing and Failback]].

- [Continuous backup copies](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery-copying.html)
- [Encryption behavior](https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html)
- [Restore testing and validation](https://aws.amazon.com/blogs/storage/implementing-restore-testing-for-recovery-validation-using-aws-backup/)
