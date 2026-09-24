---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# Amazon Macie

## Role and exam distinction

Data security/privacy service focused on S3: discover sensitive data using automated discovery or configured jobs and identify relevant bucket-security policy risks.

Macie is not a generic numeric metric anomaly detector or a substitute for GuardDuty's threat detection. Keep its role scoped to sensitive-data discovery and S3 security posture.

| Need | First distinction |
|---|---|
| Sensitive content in S3 objects | Macie |
| Suspicious account/workload behavior | GuardDuty, with appropriate protection plans |
| Vulnerabilities in supported workloads | Inspector |
| Unexpected numeric metric behavior | CloudWatch anomaly detection |

## Operations

Configure account/Region scope, organization administration, supported object formats, S3/KMS access and discovery coverage. Findings and detailed discovery results are different outputs; neither should expose actual sensitive values unnecessarily.

Route relevant findings to an authorized response/investigation workflow. A finding is not an authorization to delete data.

## Sources

Task 4.2; supporting tasks 4.2 and 6.2, with Domain 6 coverage in [[Domain 6 Security Automation and Data Protection]]. See [[Amazon GuardDuty]], [[AWS Security Hub]], [[Domain 4 Transcript Corrections]].

- [AWS security architecture: Macie scope and administration](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html)
- [Sensitive data discovery results](https://docs.aws.amazon.com/macie/latest/user/discovery-results-repository-s3.html)

## Domain 6 — classification gate

Macie discovery is asynchronous and does not redact, tokenize, or synchronously block an upload. Put untrusted objects in restricted staging, correlate findings/results to the exact object version, perform approved transformation/review, and release through a separate authorized path.

Task 6.2. [[Domain 6 Security Automation and Data Protection]], [[Inspector vs GuardDuty vs Macie vs Access Analyzer]].
