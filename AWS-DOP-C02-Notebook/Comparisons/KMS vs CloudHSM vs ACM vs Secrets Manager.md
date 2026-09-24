---
title: KMS vs CloudHSM vs ACM vs Secrets Manager
tags: [aws, dop-c02, domain-6]
verified: 2026-09-19
read: false
---

# KMS vs CloudHSM vs ACM vs Secrets Manager

| Requirement | Service |
|---|---|
| Managed encryption-key operations and envelope encryption | [[AWS Key Management Service]] |
| Customer-controlled HSM cluster/cryptographic users | [[AWS CloudHSM]] |
| Public/imported TLS certificate lifecycle for supported integrations | [[AWS Certificate Manager]] |
| Private certificate authority | [[AWS Private CA]] |
| Application secret storage and rotation workflow | [[AWS Secrets Manager]] |

KMS does not replace a secret-rotation workflow. ACM is not a database-password store. CloudHSM requires client/key administration beyond KMS. [[Domain 6 Security Automation and Data Protection]].
