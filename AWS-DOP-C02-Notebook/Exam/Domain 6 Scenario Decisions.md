---
title: Domain 6 Scenario Decisions
tags: [aws, dop-c02, domain-6]
verified: 2026-09-19
read: false
---

# Domain 6 Scenario Decisions

| Requirement | Decision | Trap |
|---|---|---|
| On-premises SDK access | Human federation or Roles Anywhere/workload federation | Permanent access keys are not mandatory |
| Mobile S3/DynamoDB access | Cognito authentication plus identity pool when direct AWS credentials are needed; scoped roles | User pool ≠ identity pool; avoid full access |
| Private EC2 uploads to S3 | Instance role + a working network path (prefer an S3 gateway endpoint; NAT or an interface endpoint can also fit) + IAM/bucket controls + KMS permission if needed | An endpoint policy restricts endpoint use but does not replace IAM or bucket authorization |
| Keep buckets private | Block Public Access/preventive controls + Config detection + routed alert/bounded remediation | Config alone is detective |
| Secure multi-account foundation | Control Tower landing zone and applicable controls | Enrollment/control scope still matters |
| Organization network protections | Firewall Manager for supported policies | Not automatic for every resource/Region |
| Sensitive data must not enter lake | Restricted staging and verified release gate using Macie findings | Macie does not redact/block ingestion |
| Require a specific S3 KMS key | Default plus request-header/key policy if contract requires; migrate old objects | Default does not rewrite existing objects |
| Locally encrypt large data | Generate data key, encrypt locally, erase plaintext, retain encrypted data key | KMS key material ≠ returned plaintext data key |
| Encrypt existing RDS DB instance | Encrypt snapshot copy, restore new instance and cut over | No in-place toggle |
| Rotate DB/API credentials | Secrets Manager rotation and consumer refresh | KMS/ACM are not credential rotators |
| Shared encrypted Lambda connection string | Parameter Store SecureString for the listed static requirement; Secrets Manager if rotation is needed | IAM role alone does not encrypt DB credentials |
| Patch hybrid fleet | Managed nodes + Patch Manager + scheduling + compliance review | Config does not install patches |
| Approved AMIs and vulnerabilities | Approved-AMI/Allowed AMIs controls plus modern Inspector | Inspector Classic workflow is retired |

## RDS encryption quick answers

| Question | DB-instance answer |
|---|---|
| Encrypt after creation? | Not in place: encrypted snapshot copy → restore a new encrypted instance |
| Turn off encryption? | Not on an encrypted instance |
| Encrypt snapshot of unencrypted DB? | Create snapshot, then encrypted copy |
| Same-Region encrypted replica key? | Same KMS key as source |
| Cross-Region encrypted snapshot? | Authorize source and choose destination-Region key |

Do not automatically generalize these DB-instance rules to Aurora cluster workflows. The eleventh walkthrough question was not supplied; no answer was invented. [[Domain 6 Transcript Coverage]].
