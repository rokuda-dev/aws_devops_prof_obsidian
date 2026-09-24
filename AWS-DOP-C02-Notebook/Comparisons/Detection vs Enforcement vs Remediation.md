---
title: Detection vs Enforcement vs Remediation
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# Detection vs Enforcement vs Remediation

| Layer | Question | Examples | Limit |
|---|---|---|---|
| Enforcement | Is this action allowed now? | IAM/S3 policy, security group, WAF | Incorrect policies can still permit undesirable behavior |
| Detection | What happened or is wrong? | CloudTrail, Config, CloudWatch, Health, GuardDuty | Usually observes after activity/state change |
| Routing/notification | Who should handle this signal? | EventBridge, SNS, queue fan-out | Accepted delivery is not completed repair |
| Remediation | What controlled change resolves it? | Lambda, SSM Automation, Step Functions workflow | Requires scoped authority and verification |
| Evidence/learning | Why did it happen and how to avoid recurrence? | Protected audit history, incident review | Restoration alone does not answer root cause |

Example: IAM restricts confidential objects; CloudTrail detects audited access; EventBridge routes a suspicious event; the response workflow contains and investigates it. Config can assess bucket configuration but is not per-request authorization.

Task 5.1. [[S3 Permission Monitoring and Remediation]], [[Event Sources and Response Contracts]], [[Safe Event-Driven Remediation]], [[Domain 5 Official Sources]].
