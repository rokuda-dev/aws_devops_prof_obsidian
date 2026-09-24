---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# AWS Health vs CloudWatch vs Trusted Advisor

| Tool | Main signal | Example cue | Boundary |
|---|---|---|---|
| AWS Health | AWS service/resource-impact and scheduled events | EC2 retirement/maintenance notification | Not a continuous app health check |
| CloudWatch | Workload metrics/logs/alarms | CPU, status checks, latency, payment counts | Not a recommendation engine or complete API audit |
| Trusted Advisor | Refreshed recommendations/check results | Underutilized resource review | Support/refresh scope matters; low use does not prove safe deletion |
| Config | Resource configuration/compliance | Required trail enabled; compliance dashboard | Periodic/change triggers vary; not strict prevention |
| GuardDuty | Threat findings | Suspicious workload/credential behavior | Optional protections and separate remediation |
| Macie | S3 sensitive-data and policy-risk findings | Discover confidential data | Not generic intrusion detection |

Task 4.2–4.3. See [[AWS Health]], [[AWS Trusted Advisor]], [[Amazon CloudWatch]], [[AWS Config]], [[Amazon GuardDuty]], [[Amazon Macie]].
