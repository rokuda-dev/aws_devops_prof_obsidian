---
title: AWS Key Management Service
tags: [aws, dop-c02, domain-6]
verified: 2026-09-19
read: false
---

# AWS Key Management Service

KMS is a Regional managed key service. Key policies, grants and IAM policies control use. Envelope encryption uses a data key for local data encryption and a KMS key to protect that data key. GenerateDataKey can return both plaintext and encrypted data-key material to an authorized caller; erase plaintext after use and store the encrypted copy with the ciphertext.

Default encryption, transport encryption and authorization remain separate controls.

- [KMS concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html)
- [Data keys](https://docs.aws.amazon.com/kms/latest/developerguide/data-keys.html)
