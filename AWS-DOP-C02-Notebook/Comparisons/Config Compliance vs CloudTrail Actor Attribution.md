---
title: Config Compliance vs CloudTrail Actor Attribution
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# Config Compliance vs CloudTrail Actor Attribution

| Requirement | Config | CloudTrail |
|---|---|---|
| Is a recorded bucket configuration compliant? | Rules/configuration history | API history can explain how it changed |
| Which actor accessed/modified an object? | Not a complete per-object access/identity audit | Relevant S3 data events |
| Who changed a bucket policy? | Observe resulting recorded configuration | Relevant management API event |
| Which instance was on an allocated Dedicated Host? | Recorded host/instance state and timeline | Related launch/change API context |
| Enforce compliance-team-only access | Does not authorize requests | Does not authorize requests either |
| Start a response | Compliance event or configured remediation | Match captured API events through EventBridge |

Enforcement belongs to IAM/resource/network controls. A custom Config rule evaluator can use Lambda or Guard; Step Functions is not a direct Config custom-rule evaluator. This does **not** mean they cannot participate in the same response: EventBridge can start a state machine, and SSM Automation supports aws:executeStateMachine.

For the transcript's object-actor requirement, the main flaw in the proposed bucket-Config-only answer is the wrong evidence granularity, not an absolute integration prohibition.

Task 5.1. [[AWS Config]], [[AWS CloudTrail]], [[S3 Permission Monitoring and Remediation]], [[Domain 5 Official Sources]].
