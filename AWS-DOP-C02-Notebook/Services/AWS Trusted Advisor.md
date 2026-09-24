---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# AWS Trusted Advisor

## Role

Recommendations/checks across supported cost, performance, security, fault-tolerance and related operational areas. Available checks, API access and refresh behavior depend on current support/service capabilities.

## Event integration

Trusted Advisor can emit check-item refresh notifications to EventBridge. Match the documented source/detail type and the relevant check result. Delivery is best effort; a check refresh is not a continuous per-minute utilization alarm.

The transcript's low-utilization → Lambda → terminate design is only a possible controlled workflow, not a safe default.

## Before changing capacity

Check sustained usage windows, workload schedules, ownership/tags, stateful storage, licensing, desired ASG capacity and business approvals. Low CPU does not mean an instance is unnecessary: it may be a standby, memory-heavy workload or periodic batch node.

Terminating an ASG instance without changing intended capacity may simply cause a replacement, saving nothing. Prefer a justified right-sizing/scaling plan with verification and rollback.

## Sources

Task 4.3. See [[AWS Health vs CloudWatch vs Trusted Advisor]], [[Safe Event-Driven Remediation]].

- [Trusted Advisor event reference](https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-trustedadvisor.html)
- [Support/check refresh capabilities](https://aws.amazon.com/premiumsupport/faqs/)

## Domain 5 — recommendations versus custom compliance

Public-bucket and unused/underutilized-resource checks support investigation. They do not prove a custom public-list-only policy or authorize immediate deletion.

Trusted Advisor refresh events, Config evaluation/compliance events and CloudWatch numeric metrics are distinct mechanisms. Check support/check availability and documented refresh timing.

Before load-balancer removal, validate ownership, sustained traffic, standby/DR purpose, DNS/service dependencies and an approved change/rollback path. Update intended IaC rather than leaving drift.

Task 5.1. [[S3 Permission Monitoring and Remediation]], [[Event Sources and Response Contracts]], [[Domain 5 Scenario Decisions]].
