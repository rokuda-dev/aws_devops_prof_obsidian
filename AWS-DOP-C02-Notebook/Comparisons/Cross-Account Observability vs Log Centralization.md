---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# Cross-Account Observability vs Log Centralization

| Architecture | Copies logs? | Purpose | Limitation |
|---|---|---|---|
| OAM cross-account observability | Federated access, not independent log replication | Monitoring account views linked source telemetry | Regional setup/access; source retention still matters |
| CloudWatch Logs centralization | Yes, selected organizational logs | Central account/Region copies with optional backup Region | New data after rule creation; no historical backfill |
| Cross-account subscriptions | Forward new matches into configured pipeline | Custom processing, S3 delivery or search indexing | Policies/roles/Region topology and downstream capacity |
| Organization CloudTrail | Selected audit events delivered across accounts | Consistent API auditing | Not every application log or every data event automatically |

Central visibility, central storage and a central **indexed** store are different requirements. Organization/OU-scoped rules can help cover future accounts, but onboarding prerequisites, scope and delivery still need verification.

Task 4.1. See [[Centralized Logging Architecture]], [[CloudWatch Log Subscriptions and Cross-Account Destinations]], [[AWS Organizations]].

- [CloudWatch centralization behavior](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html)
- [Federation versus centralization](https://aws.amazon.com/blogs/mt/simplifying-log-management-using-amazon-cloudwatch-logs-centralization/)
