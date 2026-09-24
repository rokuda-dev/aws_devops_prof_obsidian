---
tags:
  - aws
  - dop-c02
  - domain-2
  - config
  - compliance
read: true
---

# AWS Config

AWS Config records supported resource configurations and relationships and evaluates them against rules.

## Capabilities

- Configuration recorder and history
- AWS managed or custom Config rules
- Periodic or change-triggered evaluation, depending on rule
- Conformance packs: collections of rules and remediation definitions
- Organization rules/conformance packs for scale
- Aggregators for multi-account, multi-Region centralized views
- Remediation through Systems Manager Automation

## Standard remediation pattern

```text
resource change → Config evaluation → NON_COMPLIANT
  → SSM Automation remediation → compliant or exception
```

## Critical distinctions

- Config: what is/was the resource configuration and is it compliant?
- CloudTrail: who called which AWS API, from where, and when?
- CloudWatch: what is the workload emitting/doing?

> [!warning]
> An aggregator centralizes inventory and compliance data. It does not enforce or remediate by itself.

Source: [What is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)

## Config aggregators

Aggregators collect configuration/compliance data from configured accounts and Regions. Recording and evaluation still occur in the source accounts/Regions. An aggregator is a read-oriented visibility layer, not the enforcement or runbook execution plane.

## Multi-account remediation design

Use organization rules/conformance packs for appropriate distributed evaluation. Do not assume an organization rule's central definition directly supports the same remediation attachment workflow as an ordinary local rule. One documented organization-rule response pattern deploys EventBridge compliance-change rules and SSM Automation targets into member accounts with StackSets. Organization conformance packs with remediation are another documented architecture.

Remediation should recheck live state, be idempotent, use limited Automation roles, and apply concurrency/error controls. Aggregated compliance data is not an authorization to make a destructive change.

## Official AWS references

- [Organization-rule remediation response](https://repost.aws/knowledge-center/add-config-remediation-actions)
- [Conformance packs with remediation](https://aws.amazon.com/blogs/mt/manage-custom-aws-config-rules-with-remediation-using-conformance-packs/)
- [[Config vs CloudTrail vs Systems Manager]]

## Domain 3 — drift and recovery-region assurance

Rules and supported remediation workflows can detect undesired configuration and invoke Systems Manager Automation. Select the resource types/rules explicitly; Config does not automatically identify every application drift condition.

An aggregator is a visibility mechanism, not universal enforcement. Check regional recording, rules, remediation permissions and exceptions. Drift checks do not substitute for restoration/failover/failback drills.

Task 3.3. See [[AWS CloudFormation]], [[Disaster Recovery Testing and Failback]].
- [AWS Config — official resource](https://docs.aws.amazon.com/config/latest/developerguide/aws-config-landing-page.html)

## Domain 4 — compliance monitoring and response

Use recording/rules and configured aggregators for compliance visibility; optional prepared Athena/QuickSight datasets support BI analysis. A view does not enforce.

**cloudtrail-enabled** (CLOUD_TRAIL_ENABLED) is periodic. Verify configured frequency rather than assuming exactly hourly. Its compliance-change event is not the immediate StopLogging API event.

Supported remediation must recheck live state and use limited roles, exceptions and rate/error controls. StartLogging on an existing trail does not fix deleted trails, missing selectors or broken keys/buckets.

Tasks 4.2–4.3. See [[Safe Event-Driven Remediation]], [[Amazon QuickSight]].
- [Managed rule](https://docs.aws.amazon.com/config/latest/developerguide/cloudtrail-enabled.html)

## Domain 5 — specific requirements and safe repair

| Need | Appropriate evaluation |
|---|---|
| Public S3 list-only requirement | Custom desired-state policy analysis; public-risk check alone is insufficient |
| Confidential-object actor audit | CloudTrail data events; not bucket configuration alone |
| Required Dedicated Host placement | Recorded host/instance evidence and scoped custom placement check |
| No world-open SSH | restricted-ssh, identifier INCOMING_SSH_DISABLED |
| Only approved datacenter SSH | Stricter custom/appropriate policy check of allowed sources and combined SGs |

Custom rules can use Lambda or Guard. State machines may participate in the response, not serve as direct custom-rule evaluators. Scoped SSM Automation remediation must recheck current state, preserve required access, handle exceptions and verify compliance.

Tasks 5.1–5.3. [[S3 Permission Monitoring and Remediation]], [[Dedicated Host Compliance and Licensing]], [[Security Group Remediation and Access Safety]].
- [SSH rule](https://docs.aws.amazon.com/config/latest/developerguide/restricted-ssh.html)
- [Custom policy rules](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-aws-config-custom-rules-by-using-aws-cloudformation-guard-policies.html)

## Domain 6 — compliance and remediation

Config records supported resource state and evaluates configured rules; it is not a preventive authorization control. For automated remediation, scope the SSM Automation role and targets, recheck live state, handle exceptions/rate limits, and verify compliance afterward.

Tasks 6.2–6.3. [[Domain 6 Monitoring Auditing and Compliance]], [[Domain 6 Security Automation and Data Protection]], [[AWS Systems Manager]].
