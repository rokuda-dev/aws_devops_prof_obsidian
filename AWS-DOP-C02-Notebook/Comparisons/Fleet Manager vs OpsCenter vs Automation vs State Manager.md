---
title: Fleet Manager vs OpsCenter vs Automation vs State Manager
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# Fleet Manager vs OpsCenter vs Automation vs State Manager

| Capability | Primary role | Domain 5 example |
|---|---|---|
| Fleet Manager | View/manage supported managed-node OS information/tools | Inspect an affected server |
| OpsCenter | Aggregate/investigate operational work items | Create an OpsItem with evidence/related resources |
| Automation | Multi-step operational runbook | Validate, approve, change, verify and escalate |
| State Manager | Maintain defined managed-node state | Reapply approved configuration |
| Run Command | Execute approved non-interactive node commands | Reconcile ASG membership into a batch-node config |
| Session Manager | Authorized interactive access without inbound SSH/RDP | Investigate while minimizing admin exposure |
| Patch Manager | Scan/install controlled patches | Reduce vulnerability risk with tested maintenance |

The incident case, one-time repair, and ongoing desired-state policy are distinct. Required managed-node setup and permissions depend on the feature; an AWS API-only Automation action is not the same as a command on an unmanaged server.

Tasks 5.2–5.3. [[AWS Systems Manager]], [[Systems Manager Incident Operations]], [[Run Command vs Session Manager vs State Manager vs Automation]], [[Domain 5 Official Sources]].
