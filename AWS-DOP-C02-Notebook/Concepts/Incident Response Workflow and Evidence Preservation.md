---
title: Incident Response Workflow and Evidence Preservation
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# Incident Response Workflow and Evidence Preservation

## Repeatable workflow

1. Establish impact, scope, severity, ownership, and an incident timeline.
2. Correlate metrics, logs, traces, deployment/configuration changes, and service-health events against a baseline.
3. Form hypotheses; safely test from the affected context and reproduce only when doing so will not worsen the incident.
4. Contain or roll back while preserving evidence. Restoration can precede a complete root-cause explanation.
5. Resolve the cause; verify application behavior, dependencies, and data integrity.
6. Monitor for recurrence, document decisions, and improve controls/runbooks through a review.

## Evidence safeguards

Keep timestamps/time zones, request/trace IDs, resource/account/Region identity, relevant versions, and error messages. Store sensitive evidence with controlled access and retention. Avoid dumping credentials or confidential payloads into alerts.

Do not destroy a compromised instance before preserving evidence required by the incident plan. Do not assume missing telemetry means the workload is healthy.

## Tool selection

[[Amazon CloudWatch]] for workload signals; [[AWS CloudTrail]] for API actors; [[AWS Config]] for resource state; [[AWS Health]] for AWS-impact notices; [[AWS X-Ray]] for request dependencies; [[AWS Systems Manager]] for approved investigation/remediation.

Task 5.3. [[Domain 5 Scenario Decisions]], [[Systems Manager Incident Operations]], [[Domain 5 Official Sources]].
