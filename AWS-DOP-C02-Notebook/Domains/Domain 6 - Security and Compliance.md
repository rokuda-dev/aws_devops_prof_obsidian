---
tags: [aws, dop-c02, domains]
updated: 2026-09-19
read: false
---

# Domain 6 - Security and Compliance

> [!summary]
> Domain 6 is 17% of the exam and tests identity at scale, automated security and data protection, and monitoring, auditing, and compliance.

## Task 6.1 — Implement techniques for identity and access management at scale.

Design least-privilege human and machine access with temporary credentials, role trust, identity/resource/session policies, permissions boundaries, SCPs, federation, RBAC/ABAC and safe credential rotation.

- Services: [[AWS Identity and Access Management]], [[AWS Security Token Service]], [[AWS IAM Identity Center]], [[AWS IAM Roles Anywhere]], [[Amazon Cognito]], [[IAM Access Analyzer]], [[AWS Organizations]], [[AWS Secrets Manager]]
- Study: [[Domain 6 Identity and Access at Scale]], [[SCP vs Permissions Boundary vs Session Policy vs Resource Policy]], [[Domain 6 Scenario Decisions]]

## Task 6.2 — Apply automation for security controls and data protection.

Layer preventive, detective and responsive controls. Separate data classification from release enforcement, encryption defaults from request policy, key custody from ciphertext storage, and detection from verified remediation.

- Services: [[AWS Systems Manager]], [[AWS Config]], [[AWS Security Hub]], [[AWS Control Tower]], [[AWS Firewall Manager]], [[AWS WAF]], [[AWS Shield]], [[AWS Network Firewall]], [[Amazon Route 53 Resolver DNS Firewall]], [[Amazon Macie]], [[AWS Glue]], [[AWS Key Management Service]], [[AWS CloudHSM]], [[AWS Certificate Manager]], [[AWS Private CA]]
- Study: [[Domain 6 Security Automation and Data Protection]], [[KMS vs CloudHSM vs ACM vs Secrets Manager]], [[Domain 6 Architecture Patterns]]

## Task 6.3 — Implement security monitoring and auditing solutions.

Correlate actor, configuration, network, patch, deployment and vulnerability evidence. Scope remediation, preserve evidence and verify desired state after action.

- Services: [[AWS CloudTrail]], [[AWS Config]], [[Amazon GuardDuty]], [[Amazon Inspector]], [[Amazon Detective]], [[AWS Audit Manager]], [[AWS Systems Manager]], [[AWS CloudFormation]], [[AWS Service Catalog]]
- Study: [[Domain 6 Monitoring Auditing and Compliance]], [[Inspector vs GuardDuty vs Macie vs Access Analyzer]], [[Domain 6 Transcript Corrections]]

## Exam workflow

1. Identify the protected identity, resource or data.
2. Choose the preventive boundary.
3. Add the detective signal and durable evidence.
4. Route only actionable events.
5. Run a least-privilege, idempotent remediation.
6. Verify state and retain an audit trail.

## Sources and deeper review

- [Official Domain 6 task statements](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain6.html)
- [[Domain 6 Scenario Decisions]]
- [[Domain 6 Architecture Patterns]]
- [[Domain 6 Transcript Corrections]]
- [[Domain 6 Transcript Coverage]]
- [[Domain 6 Official Sources]]
- [[Notebook Provenance and Progress]]
