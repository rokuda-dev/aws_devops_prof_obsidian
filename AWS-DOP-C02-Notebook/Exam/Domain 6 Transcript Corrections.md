---
title: Domain 6 Transcript Corrections
tags: [aws, dop-c02, domain-6]
verified: 2026-09-19
read: false
---

# Domain 6 Transcript Corrections

| Transcript shortcut | Current study interpretation |
|---|---|
| On-premises applications need access keys | Federation/Roles Anywhere can avoid permanent IAM-user keys |
| Console access means IAM username/password | Identity Center/federation provide other paths |
| CodeCommitPowerUser cannot create repositories | Current policy includes Create*; it omits DeleteRepository but is not an explicit deny |
| Cognito is the only federation method and always creates roles | IAM/STS support other paths; Cognito can create/select roles depending on setup |
| Mobile role should allow all S3/DynamoDB | Scope resources/actions/prefixes/items |
| Boundaries intersect every possible grant | Same-account direct resource-policy grants have documented implicit-deny exceptions |
| Config guarantees private buckets | Config detects; use preventive public-access controls too |
| Firewall Manager protects everything automatically | Policy type, prerequisites, scope, Regions/tags and remediation settings matter |
| Macie monitors all usage and redacts ingestion | Macie discovers S3 sensitive data/policy risks; build a separate release gate |
| Environment variables are always the safest secret path | Launch-time injection has exposure/refresh tradeoffs; runtime retrieval may be safer |
| Only Secrets Manager has resource policies | Advanced Parameter Store supports cross-account resource-policy/RAM sharing |
| Parameter secret references only need a slash | Use /aws/reference/secretsmanager/<secret>; path retrieval is restricted |
| S3 bucket encryption means every existing object uses KMS | Defaults cover new writes; request enforcement and migration are separate |
| No plaintext key can leave KMS HSMs | KMS key material stays protected; GenerateDataKey can return an authorized plaintext data key |
| CloudHSM is always FIPS 140-2 Level 3 | Validation depends on model/mode; hsm2m.medium has FIPS 140-3 Level 3 guidance |
| ACM certificates cannot be exported | Current ACM supports eligible exportable public certificates |
| Inspector needs Classic agent/tag assessments | Inspector Classic retired May 20, 2026 |
| Audit Manager is open for new setup | New-account setup closed April 30, 2026; existing availability is restricted |
| Task 6.3 repeats automation title | Official task 6.3 is security monitoring and auditing |
| A private EC2 instance must use an S3 endpoint | A gateway endpoint is the usual private path, but NAT or an interface endpoint can also provide connectivity; authorization layers still apply |
| ARC readiness checks are generally available to any new customer | Readiness checks closed to new customers April 30, 2026; other ARC capabilities remain supported |

Verified September 19, 2026. Current-product facts are not predictions of exam refresh timing. [[Domain 6 Official Sources]].
