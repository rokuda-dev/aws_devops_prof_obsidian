---
title: Domain 6 Identity and Access at Scale
tags: [aws, dop-c02, domain-6]
verified: 2026-09-19
read: false
---

# Domain 6 Identity and Access at Scale

## Choose the identity path

| Identity | Preferred pattern |
|---|---|
| Workforce | [[AWS IAM Identity Center]] federation and permission sets |
| AWS workload | IAM role attached to the service resource |
| External workload | [[AWS IAM Roles Anywhere]] or another temporary federation path |
| Application end user | [[Amazon Cognito]] when user/identity-pool capabilities fit |

Temporary credentials can be used outside AWS; “on premises” does not automatically mean permanent access keys. Protect root, enable MFA where supported, remove unused credentials and rotate only where a long-lived credential is unavoidable.

## Policy layers

Identity policies grant permissions; resource policies grant to principals; role trust policies allow assumption; session policies narrow a session; permissions boundaries cap identity-policy grants; SCPs cap member-account permissions but grant nothing. Explicit deny wins. See [[SCP vs Permissions Boundary vs Session Policy vs Resource Policy]].

## RBAC and ABAC

RBAC assigns job-function permissions. ABAC uses principal, resource and session tags/attributes. Control who may write authorization tags, test condition-key support, and use Null safeguards where a missing multivalued key could otherwise make a condition unsafe.

## Scenario anchors

- Current AWSCodeCommitPowerUser includes repository creation and Git push but not DeleteRepository; it is not an explicit deny against other policies. Use scoped customer policies and a distinct authorized merge path.
- Private EC2 → S3 needs instance-profile permissions, a working network path, bucket authorization and KMS permissions when applicable. An S3 gateway endpoint is the usual private, no-NAT path; NAT or an interface endpoint can also fit. Endpoint policy is an additional restriction, not a replacement for IAM or bucket policy.
- Cognito user and identity pools are different. Scope mobile permissions to required buckets, prefixes, tables and operations.

[[AWS Identity and Access Management]], [[AWS Security Token Service]], [[IAM Access Analyzer]], [[Domain 6 Official Sources]].
