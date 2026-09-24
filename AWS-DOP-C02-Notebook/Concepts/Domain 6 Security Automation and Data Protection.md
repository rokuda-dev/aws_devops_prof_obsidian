---
title: Domain 6 Security Automation and Data Protection
tags: [aws, dop-c02, domain-6]
verified: 2026-09-19
read: false
---

# Domain 6 Security Automation and Data Protection

## Automated control loop

Prevent with IAM/SCP/Block Public Access and service controls. Detect with Config, Security Hub, CloudTrail, GuardDuty or data-classification findings. Route actionable events through EventBridge, remediate with a bounded Lambda or Systems Manager runbook, then re-evaluate and retain evidence. Detective Config rules do not alone prevent a public bucket.

## Secrets

Use roles instead of storing AWS access keys. Secrets Manager supports managed/custom rotation workflows: create, set, test and finish. Consumers must refresh. Parameter Store SecureString is KMS encrypted; String is plaintext. A Secrets Manager reference uses the special `/aws/reference/secretsmanager/<secret>` path and is supported by GetParameter/GetParameters, not GetParametersByPath. Advanced Parameter Store supports cross-account sharing through resource policies/RAM.

Launch-time environment injection can expose values through process/debug paths and does not automatically refresh a rotated value. Runtime retrieval with a scoped execution identity and protected cache is often safer.

## Sensitive-data gate

Macie discovers sensitive data in S3 asynchronously; it does not redact or synchronously block ingestion. Use restricted staging, correlate the exact object/version, transform or reject, verify the result and publish through a separate release identity. No finding is not proof a file is clean when formats, permissions or job coverage are incomplete.

## Encryption

S3 encrypts new objects by default with SSE-S3, but that is not the same as requiring a specific SSE-KMS key. Default encryption affects new writes, not existing objects. Use a request policy if callers must supply a specific encryption header/key, and migrate existing versions separately. RDS instance encryption migration usually requires encrypted snapshot copy, restore to a new instance and planned cutover.

[[AWS Key Management Service]], [[AWS Secrets Manager]], [[Amazon Macie]], [[AWS Glue]], [[Domain 6 Scenario Decisions]].
