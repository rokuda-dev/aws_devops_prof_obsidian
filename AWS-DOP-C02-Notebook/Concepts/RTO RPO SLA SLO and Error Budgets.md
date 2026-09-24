---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# RTO RPO SLA SLO and Error Budgets

| Term | Meaning | Example interpretation |
|---|---|---|
| SLA | External agreement, often with defined remedies | Contractual service commitment |
| SLO | Operational reliability target | Target availability or latency over a window |
| SLI | Measurement used to evaluate a target | Fraction of successful valid requests |
| Error budget | Allowed unreliability under the chosen SLO | Remaining permissible failed requests/time |
| RTO | Maximum acceptable time to restore the required service | Business service usable within two hours |
| RPO | Maximum acceptable loss expressed as time/data age | At most five minutes of accepted changes lost |

SLA, SLO, and RTO are not interchangeable. An error budget is not automatically an AWS service credit.

## Measure the complete path

RTO includes detection, decision/approval, provisioning or scale-up, data promotion/restore, application initialization, validation, routing changes, and client reconnection. Database promotion time alone is not application RTO.

RPO depends on the last valid recoverable state: backup interval, copy completion, replication lag, and the failure boundary. “Replica exists” does not prove freshness.

## Five-minute RPO / two-hour RTO

A cross-Region asynchronous RDS replica can be a candidate if measured lag/loss stays within five minutes and the complete recovery path stays within two hours. Pilot light versus warm standby depends on tested provisioning time, cost, and operational risks.

S3 replication has separate timing characteristics. S3 Replication Time Control's 15-minute objective is not a five-minute guarantee for the whole workload.

## Sources

Tasks 3.1–3.3. See [[Disaster Recovery Strategies]], [[Domain 3 Scenario Decisions]].

- [Domain 3 business/recovery objectives](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain3.html)
- [Validating recovery objectives](https://aws.amazon.com/blogs/mt/validating-and-improving-the-rto-and-rpo-using-aws-resilience-hub/)
