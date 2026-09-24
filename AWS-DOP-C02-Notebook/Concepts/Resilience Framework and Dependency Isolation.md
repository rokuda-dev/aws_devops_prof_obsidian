---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# Resilience Framework and Dependency Isolation

## Framework, not a single service

Define business objectives, enumerate failure modes/dependencies, observe the workload, detect failures, execute corrective/recovery actions, and refine through testing. Map every measure to [[RTO RPO SLA SLO and Error Budgets]].

| Dependency class | Questions to ask |
|---|---|
| Runtime | Database, cache, queue, DNS, network, identity, KMS, third-party API? |
| Build/deployment | Can the recovery Region obtain libraries, AMIs, images, templates, and secrets without the failed Region? |
| Operational | Does recovery depend on an unavailable console, person, approval path, or central account? |
| Regional | Are endpoints, keys, artifacts, and control actions usable independently in the recovery Region? |
| State | What must be replicated, restored, fenced, or reconciled before writes resume? |

## Design principles

Prefer regional autonomy and static stability: healthy deployments should continue serving with existing capacity and configuration during failures. Do not require a successful deployment or distant dependency call for every request.

Externalize instance-local state, but recognize that external state services can become dependencies themselves. Use managed services appropriately; they reduce operational work without removing application design responsibilities.

Provide redundancy, backups, observability, safe retries, timeouts, and bounded recovery automation. Redundancy addresses infrastructure failure; independent backups address unwanted state changes.

## Continuous monitoring

Use metrics for symptoms/objectives, logs for events/context, and traces for request paths/dependency latency. Monitor availability, latency, errors, saturation, replication lag, backup freshness, and recovery-action success—not CPU alone.

Test alarm thresholds and detection latency. A noisy alarm can trigger destructive recovery; a dependency-blind shallow health check can miss business failure.

## Sources and scope

Task 3.1. See [[Multi-Region Application Checklist]], [[Disaster Recovery Testing and Failback]].

- [Official Domain 3 objectives](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain3.html)
- [AWS Resilience Hub concepts](https://docs.aws.amazon.com/resilience-hub/latest/userguide/concepts-terms.html)

Resilience Hub assessments and AWS Fault Injection Service experiments are supplementary resilience tools. Estimated objectives still require validation through controlled drills.
