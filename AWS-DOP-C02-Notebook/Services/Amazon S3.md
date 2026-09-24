---
title: Amazon S3
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# Amazon S3

Durable object storage for pipeline artifacts, application objects, and logs.

## Exam mapping

Task statements: 1.3, 1.4, 3.1, 3.3, 4.1, 5.1, 6.2. See [[Domain 1 - SDLC Automation]], [[Domain 3 - Resilient Cloud Solutions]], [[Domain 4 - Monitoring and Logging]], [[Domain 5 - Incident and Event Response]], and [[Domain 6 - Security and Compliance]].

## Core components and behavior

Buckets contain versioned objects; lifecycle, encryption, access policies, and replication solve different requirements.

## Architecture pattern

[[AWS CodePipeline]] artifact store → scoped build/deployment consumers; retain tested release versions for rollback.

## IAM and security

Use least-privilege IAM/bucket policies, encryption, and public-access controls. Cross-account encrypted artifacts need both S3 access and appropriate KMS permissions.

## Failure, rollback, and lifecycle

Versioning can preserve prior objects but does not automatically reverse deployment. Replication configuration does not grant consumer access or replicate every historical object automatically.

## When to choose

> [!exam]
> Choose for object/artifact storage, not a mounted POSIX filesystem or block device.

## Do not confuse with and exam traps

> [!warning]
> [[Amazon EFS]] is shared filesystem storage; [[Amazon EBS]] is block storage; [[Amazon ECR]] stores container artifacts.

## Official AWS references

- [Amazon S3 official reference](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 3 — object recovery

CloudFront caches media for delivery; S3 cross-Region replication (CRR) creates a separate regional object copy. Configure versioning on source/destination, replication IAM, bucket policy, and appropriate regional KMS permissions. Verify eligibility and encryption configuration.

Live replication does not backfill all preexisting objects; use supported Batch Replication for existing or failed objects. S3 Replication Time Control has a 15-minute replication objective, not a blanket five-minute RPO guarantee. Measure the application's recoverable state.

Versioning helps recover overwrites/deletes; replication is not an independent historical backup and can propagate unwanted changes. Consider destination protection and, when required, immutable retention. Recovery includes destination bucket access, application configuration, and traffic/origin selection.

Tasks 3.1 and 3.3. See [[AWS Backup]], [[Disaster Recovery Testing and Failback]].
- [Batch Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-batch-replication-batch.html)
- [Replication configuration/RTC](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-add-config.html)

## Domain 4 — archive and object audit

Enable CloudTrail data events for required confidential-object operations. Default management history alone does not audit all GetObject/PutObject/DeleteObject activity.

Align lifecycle/expiration (including noncurrent versions as applicable) with audit retention. Protect raw logs/query outputs and encryption access. Delivery, retention and search indexing are separate capabilities.

Tasks 4.1–4.3. See [[AWS CloudTrail]], [[Amazon Athena]], [[Log Lifecycle Security and Integrity]], [[Domain 4 Scenario Decisions]].

## Domain 5 — policy state versus object actors

Public-list-only is a custom authorization requirement, not merely a generic public-permission finding. Confirm intended exposure and Block Public Access interactions; preserve authorized internal object access during repair.

CloudTrail data events answer relevant object actor questions; Config observes recorded configuration. With Bucket owner enforced Object Ownership, ACLs are disabled and policies control access.

S3 File Gateway RefreshCache updates externally changed object inventory; it is not an S3 upload or CloudFront invalidation operation.

Tasks 5.1–5.3. [[S3 Permission Monitoring and Remediation]], [[AWS Storage Gateway]], [[Config Compliance vs CloudTrail Actor Attribution]].
- [Object Ownership](https://docs.aws.amazon.com/help-panel/AmazonS3/latest/console/hp-edit-object-ownership-page.html)

## Domain 6 — public access, audit, and encryption

Use Block Public Access and least-privilege policies as preventive controls; Config findings are detective. CloudTrail S3 data events are required for object-level actor evidence. S3 encrypts new objects by default with SSE-S3, but a requirement for a specific SSE-KMS key needs deliberate bucket defaults/policy and migration of existing object versions.

Tasks 6.2–6.3. [[Domain 6 Security Automation and Data Protection]], [[Domain 6 Monitoring Auditing and Compliance]], [[AWS Key Management Service]].
