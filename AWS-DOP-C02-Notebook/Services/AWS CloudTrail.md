---
title: AWS CloudTrail
tags: [aws, dop-c02, service]
status: consolidated-study-note
updated: 2026-09-18
read: false
---

# AWS CloudTrail

Audit AWS API activity and identify actors, actions, and resource access.

## Exam mapping

Task statements: 2.2; cross-domain 4–6. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Event history, trails, organization trails, and event-data-store capabilities support different audit needs. Management events and optional data events cover different operations.

## Architecture pattern

Account/organization API activity → trail/audit destination → analysis/alerting → [[Amazon EventBridge]] response where supported.

## IAM and security

Protect audit destinations with encryption, restricted access, retention, and optional integrity validation. Explicitly enable required data events; they are not all logged by default.

## Failure, rollback, and lifecycle

Investigate who changed a resource and when; retaining an API event does not revert the change. CloudTrail is not guest OS command logging.

## When to choose

> [!exam]
> Choose for actor attribution and AWS API audit evidence.

## Do not confuse with and exam traps

> [!warning]
> [[AWS Config]] answers configuration/history/compliance; [[Amazon CloudWatch]] answers workload telemetry. Default Event history is not a complete long-term organization audit archive.

## Official AWS references

- [AWS CloudTrail official reference](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 3 — cross-Region audit visibility

Use configured multi-Region/organization logging and a central destination for analysis/auditing as appropriate. Aggregated audit logs are not application metrics, data replication, or runtime failover.

Ensure regional recovery does not require successful access to the central audit Region for every request. Task 3.2. See [[Multi-Region Application Checklist]].

## Domain 4 — exact audit scope

| Capability | Meaning |
|---|---|
| Default event history | Past 90 days of management events, by account and Region; no user-created trail required |
| Trail | Retained delivery under actual event selectors and single/multi-Region scope |
| Organization trail | Configured audit coverage across organization accounts; not every event type automatically |
| CloudWatch Logs integration | Native authorized trail delivery for log search/filters |

Enable S3 GetObject/PutObject/DeleteObject **data events** explicitly. Lambda is not required merely to record these events. Current capabilities include management, data, Insights and network activity events. CloudTrail is not guest OS command logging.

Multi-Region collection does not make every CloudTrail resource global. Configure enabled-Region scope, appropriate administration, keys, destinations and retention.

## Domain 4 — alerts and integrity

CloudTrail → Logs metric filter → alarm → SNS can notify about policy changes. EventBridge can also match **AWS API Call via CloudTrail** when the required activity is captured.

Integrity validation produces hourly signed digests; validation detects modification/deletion, not prevention or automatic protection of arbitrary application files. StopLogging API events differ from periodic Config compliance events.

Tasks 4.1–4.3. See [[Safe Event-Driven Remediation]], [[Log Lifecycle Security and Integrity]], [[Domain 4 Scenario Decisions]].
- [Default history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html)
- [Trail concepts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html)
- [Signed digests](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html)

## Domain 5 — actor evidence, not authorization

Select relevant S3 data events for confidential object actions and relevant management events for bucket policy changes. Attribute using userIdentity/session context and approved role/identity definitions; an IAM group label is not a universal event field.

EventBridge can route captured API events. Config evaluates recorded resource state; IAM/S3 policies enforce access before execution. These roles complement each other.

Preserve audit evidence during exposed-key containment and report sanitized summaries. Do not log secrets into incident workflows.

Tasks 5.1–5.3. [[S3 Permission Monitoring and Remediation]], [[Exposed Credential Response]], [[Incident Response Workflow and Evidence Preservation]].

## Domain 6 — audit evidence

CloudTrail answers who called supported AWS APIs, from where, and with what result. Default Event history is 90 days of management events per Region; object data events and durable organization archives require configuration. Digest validation detects later log-file modification; it does not prevent an authorized deletion or replace destination controls.

Task 6.3. [[Domain 6 Monitoring Auditing and Compliance]], [[AWS Config]], [[AWS Audit Manager]].
