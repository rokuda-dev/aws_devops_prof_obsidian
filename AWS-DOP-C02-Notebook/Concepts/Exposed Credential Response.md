---
title: Exposed Credential Response
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# Exposed Credential Response

## Preventive and reactive controls

Secret scanning before commits/pushes and during CI can block leaks. AWS Health detection of AWS_RISK_CREDENTIALS_EXPOSED happens after exposure is detected; it is not a pre-push GitHub validation service or a guarantee that every leaked credential is discovered.

## Automated response

EventBridge can match the Health event and start a Step Functions workflow:

1. Validate account, event, affected identity/key, and response authorization.
2. Promptly deactivate or delete the verified long-lived key under the pre-approved containment policy. Failure must escalate.
3. Preserve and inspect relevant CloudTrail activity, credential/permission changes, and resources created by an attacker.
4. Notify the security owner with a sanitized summary.
5. Rotate affected application access, verify recovery, remove old credentials, and review root cause.

The historical AWS example deletes the key first. Deactivation can be a containment step, but never reactivate a known leaked key as an application rollback. Do not delay containment while preparing a report.

## Pattern example

```json
{
  "source": ["aws.health"],
  "detail-type": ["AWS Health Event"],
  "detail": {
    "service": ["RISK"],
    "eventTypeCode": ["AWS_RISK_CREDENTIALS_EXPOSED"]
  }
}
```

This is a filter, not a deployable response system. Confirm current schema/affected entities and global-event Region coverage. Use scoped roles, duplicate-safe processing, and failure monitoring. Do not put secret key values in state-machine logs or SNS.

Task 5.2. [[AWS Identity and Access Management]], [[AWS Health]], [[AWS Step Functions]].

- [AWS historical response architecture and event schema](https://aws.amazon.com/blogs/compute/automate-your-it-operations-using-aws-step-functions-and-amazon-cloudwatch-events/)
- [AWS current containment guidance](https://aws.amazon.com/blogs/security/how-to-improve-your-security-incident-response-processes-with-jupyter-notebooks/)
