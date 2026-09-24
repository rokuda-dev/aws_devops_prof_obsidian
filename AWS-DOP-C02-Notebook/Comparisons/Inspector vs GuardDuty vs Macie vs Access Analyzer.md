---
title: Inspector vs GuardDuty vs Macie vs Access Analyzer
tags: [aws, dop-c02, domain-6]
verified: 2026-09-19
read: false
---

# Inspector vs GuardDuty vs Macie vs Access Analyzer

| Signal | Best fit |
|---|---|
| Software vulnerabilities/exposure on supported workloads | [[Amazon Inspector]] |
| Suspicious behavior/threat detection | [[Amazon GuardDuty]] |
| Sensitive data and S3 policy risk | [[Amazon Macie]] |
| Unintended external/internal/unused IAM access and policy validation | [[IAM Access Analyzer]] |

A finding is evidence for triage, not automatic proof of exploit, data cleanliness or malicious intent. Centralize findings through [[AWS Security Hub]] where supported and keep remediation scoped.
