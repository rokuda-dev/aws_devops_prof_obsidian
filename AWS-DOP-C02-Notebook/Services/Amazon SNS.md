---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# Amazon SNS

## Role in Domain 3

Publish notifications to subscribed endpoints, including Lambda. The transcript uses RDS → SNS → Lambda as a database-recovery event path.

A notification transport is not itself a recovery workflow, strong failure detector, or data replication mechanism. RDS event delivery can be delayed and out of order.

## Handler safeguards

Validate source/account/resource and event meaning; tolerate duplicate/replayed events and retry behavior; use idempotent recovery actions. Combine independent health evidence and data-readiness checks before promoting a writer.

Configure topic permissions, subscription permissions, encryption access, dead-letter/failure handling where supported, alarms, and least-privilege Lambda actions. Avoid a recovery function that depends solely on resources in the failed Region.

For multi-step recovery with gates/retries, consider [[AWS Step Functions]] or [[Amazon Application Recovery Controller]] Region switch rather than hiding every recovery decision in one notification handler.

## Sources

Tasks 3.1 and 3.3. See [[Amazon RDS]], [[AWS Lambda]], [[Domain 3 Architecture Patterns]].

- [RDS event notifications and delivery timing](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.overview.html)
- [SNS overview](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)

## Domain 4 — team notification

Confirm subscriptions and test permissions/actual trigger delivery. Normal metric-alarm notifications follow state changes rather than every matching event while ALARM persists.

Tasks 4.2–4.3. See [[AWS Health]], [[Metric Alarms and Anomaly Detection]].

## Domain 5 — response boundaries

Use SNS for sanitized incident notifications/fan-out. Confirm subscriptions/permissions and recipients; a published message is not verified recovery.

Tasks 5.1–5.3 where applicable. [[Domain 5 Scenario Decisions]], [[Safe Event-Driven Remediation]], [[Domain 5 Official Sources]].
