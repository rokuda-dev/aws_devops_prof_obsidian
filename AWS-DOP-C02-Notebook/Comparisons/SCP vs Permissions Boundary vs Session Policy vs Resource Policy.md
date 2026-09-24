---
title: SCP vs Permissions Boundary vs Session Policy vs Resource Policy
tags: [aws, dop-c02, domain-6]
verified: 2026-09-20
read: false
---

# SCP vs Permissions Boundary vs Session Policy vs Resource Policy

| Control | What it does | Grants access? | Scope/caveat |
|---|---|---:|---|
| SCP | Organization permission ceiling | No | Member accounts/OUs; does not constrain the management account and generally not service-linked roles |
| Permissions boundary | Maximum identity-policy permissions | No | IAM users/roles, not groups; resource-policy exceptions matter |
| Session policy | Narrows a role/federated session | No | Effective for that session |
| Resource policy | Resource-attached allow/deny statements that name principals | Can | Service-specific; it can grant directly where supported, while explicit deny still applies. Same-account direct user/session grants have important implicit-deny behavior. |

Explicit denies still apply. Do not memorize “all policies simply intersect” without the resource-policy exceptions. [[Domain 6 Identity and Access at Scale]].
