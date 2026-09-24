---
title: Domain 6 Monitoring Auditing and Compliance
tags: [aws, dop-c02, domain-6]
verified: 2026-09-19
read: false
---

# Domain 6 Monitoring Auditing and Compliance

## Evidence types

| Question | Primary evidence |
|---|---|
| Who called an API? | [[AWS CloudTrail]] |
| Did configuration meet a rule? | [[AWS Config]] |
| Was network traffic accepted/rejected? | VPC Flow Logs |
| Are patches installed? | Systems Manager inventory/compliance |
| Is a deployment/template drifting? | CloudFormation drift and Config |
| Is a supported workload vulnerable? | [[Amazon Inspector]] |
| Is activity suspicious? | [[Amazon GuardDuty]] and [[Amazon Detective]] |
| Is S3 data sensitive? | [[Amazon Macie]] |

No single evidence source proves complete compliance. Define scope, ownership, retention, access and integrity; correlate IDs/timestamps; preserve artifacts before destructive remediation; and verify state afterward.

## Patch and AMI governance

Register supported AWS/on-premises nodes with Systems Manager, define baselines, schedule with Maintenance Windows or scoped Quick Setup patch policies, and review compliance. A compliant patch scan is not proof the application is safe or vulnerability-free.

Use the Config approved-amis-by-id rule or EC2 Allowed AMIs to identify/prevent unapproved images according to requirements. Modern Inspector scanning is separate from AMI approval. Inspector Classic's agent/tag assessment workflow retired May 20, 2026. Blindly terminating a bad instance can lose evidence or allow an Auto Scaling group to recreate it from the same image; fix the source and perform controlled replacement.

[[AWS Audit Manager]], [[AWS Systems Manager]], [[Domain 6 Transcript Corrections]].
