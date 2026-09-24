---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# AWS Health

## Role and exam cue

AWS service/resource-impact events, such as scheduled EC2 maintenance/retirement and recovery outcomes. The old Personal Health Dashboard name should be read as AWS Health Dashboard in current notes.

AWS Health is not a continuous application health probe. CloudWatch system/instance status checks and application metrics answer different questions.

## Notification pattern

AWS Health → EventBridge rule → SNS team notification. Filter source, detail type, affected service and event category/type. A simple scheduled-change filter is:

```json
{
  "source": ["aws.health"],
  "detail-type": ["AWS Health Event"],
  "detail": {
    "service": ["EC2"],
    "eventTypeCategory": ["scheduledChange"]
  }
}
```

Scope exact event codes/resources as required. Configure permissions, subscribe/confirm recipients, and test delivery. Organization-wide monitoring requires organizational view/delegated-administrator setup, not merely a rule in an arbitrary account. Delivery can be at least once; handlers should be idempotent.

## Single dedicated EC2 instance

Eligible Dedicated Instances can support simplified automatic recovery; Dedicated Hosts use a different mechanism. Confirm instance/storage/network/ASG eligibility and available capacity. Recovery addresses system impairment and can lose RAM state; it does not provide zero-downtime application or AZ/Region HA.

Do not launch a random replacement from a generic Health notification without preserving identity, storage, configuration, licensing/tenancy constraints and traffic recovery.

## Sources

Tasks 4.2–4.3. See [[AWS Health vs CloudWatch vs Trusted Advisor]], [[Safe Event-Driven Remediation]].

- [EventBridge monitoring — official resource](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html)
- [Scheduled EC2 automation pattern](https://docs.aws.amazon.com/health/latest/ug/automating-instance-actions.html)
- [Simplified recovery requirements](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-configuration-recovery.html)

## Domain 5 — exposed keys and maintenance

Health publishes native EventBridge events for supported account/service impacts; CloudWatch polling of the Health API is not mandatory for notification.

The historical AWS_RISK_CREDENTIALS_EXPOSED event uses source aws.health and service RISK. It signals detected exposure, not preventive repository validation. Match current schema/affected entities and Region coverage, then run scoped containment/audit/notification.

Scheduled EC2/RDS actions require impact planning; a generic event should not blindly terminate or replace resources.

Tasks 5.1–5.3. [[Exposed Credential Response]], [[Event Sources and Response Contracts]], [[Systems Manager Incident Operations]].
