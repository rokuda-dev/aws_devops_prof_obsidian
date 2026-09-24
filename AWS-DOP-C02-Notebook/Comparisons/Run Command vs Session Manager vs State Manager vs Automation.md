---
tags: [aws, dop-c02, comparisons]
updated: 2026-09-18
read: false
---

# Run Command vs Session Manager vs State Manager vs Automation

| SSM capability | Requirement | Execution clue |
|---|---|---|
| Run Command | Non-interactive commands across a fleet | Script/document on managed nodes |
| Session Manager | Interactive access without inbound SSH/RDP | IAM-authorized session over service connectivity |
| State Manager | Maintain desired software/host configuration | Association and scheduled/event-driven application |
| Automation | Multi-step operational runbook | AWS APIs, conditions, approvals, rate controls |
| Patch Manager | Patch compliance/install | Baseline + scheduling/reboot choices |
| Quick Setup patch policy | Organization/multi-Region patch setup | Centrally configured scan/install schedules |

Run Command/State Manager host actions need managed nodes. Automation can also operate on AWS resources using API actions. [[AWS Systems Manager]] supports hybrid activation for appropriate external hosts.

> [!warning]
> “SSH replacement” is usually Session Manager for interactive administration, not Run Command. No inbound port requirement does not remove outbound connectivity, Agent, IAM, and logging prerequisites.

