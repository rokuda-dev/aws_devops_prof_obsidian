---
title: AWS Security Token Service
tags: [aws, dop-c02, domain-6]
verified: 2026-09-19
read: false
---

# AWS Security Token Service

STS issues temporary credentials for roles and federated sessions. The credentials include an access key ID, secret access key and session token. Trust policies answer who may assume a role; permissions and optional session policies answer what the session may do. Use AssumeRole, AssumeRoleWithSAML or web-identity flows for the matching trust protocol.

**Exam cue:** temporary cross-account or federated access. Request signing authenticates a request; it does not itself authorize the action.

- [Temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)
- [[Domain 6 Identity and Access at Scale]]
