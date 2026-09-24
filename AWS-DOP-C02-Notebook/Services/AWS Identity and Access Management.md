---
title: AWS Identity and Access Management
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# AWS Identity and Access Management

IAM authorizes AWS access through identities, roles, and policies. Domain 5 focus: least-privilege response roles, approved actors, and compromised credentials.

## Prevention versus detection

Use roles and temporary credentials for workloads where possible. Enforce access with policy; [[AWS CloudTrail]] provides actor/action audit evidence after API activity. Config compliance and an EventBridge rule do not replace authorization.

Do not put access keys in source, images, notebook examples, logs, or notifications. Pre-commit/CI secret scanning is a preventive control; AWS Health exposed-key detection is reactive.

## Containment

A verified exposed long-lived access key must be promptly deactivated or deleted according to the response plan. Identify the exact affected owner/key, preserve audit evidence, rotate dependent applications, and investigate persistence or privilege changes. Temporary role sessions require their own revocation/containment strategy, not deletion of an IAM user's access key.

## Links and sources

Tasks 5.1–5.3. [[Exposed Credential Response]], [[S3 Permission Monitoring and Remediation]], [[Safe Event-Driven Remediation]].

- [AWS containment guidance](https://aws.amazon.com/blogs/security/how-to-improve-your-security-incident-response-processes-with-jupyter-notebooks/)
- [AWS exposed-key workflow](https://aws.amazon.com/blogs/compute/automate-your-it-operations-using-aws-step-functions-and-amazon-cloudwatch-events/)

## Domain 6 — access at scale

Use temporary credentials and federation for humans and workloads where possible. Separate role trust from granted permissions; apply RBAC or ABAC deliberately; protect authorization tags; and treat permissions boundaries and SCPs as ceilings rather than grants. Resource-policy exceptions and explicit-deny behavior matter.

Task 6.1. [[Domain 6 Identity and Access at Scale]], [[SCP vs Permissions Boundary vs Session Policy vs Resource Policy]], [[AWS Security Token Service]], [[AWS IAM Identity Center]], [[AWS IAM Roles Anywhere]].
