---
title: Systems Manager Incident Operations
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# Systems Manager Incident Operations

## Fleet and issue workflows

Fleet Manager offers an aggregate managed-node view and interactive OS troubleshooting tools. Nodes need SSM Agent, permissions, registration where applicable, and service connectivity. Fleet-wide maintenance/convergence uses the appropriate Run Command, State Manager, Patch Manager, or Automation capability—not Fleet Manager alone.

OpsCenter centralizes operational work items called **OpsItems**, their related resources, and investigation context. CloudWatch alarms/EventBridge can generate OpsItems; engineers can use Automation runbooks to investigate and resolve them.

## Safe response

Attach evidence, ownership, severity, deduplication/correlation, and an approved runbook. Validate inputs/live state, bound concurrency, require approval where necessary, and verify resolution before closing the item.

Session Manager provides authorized administrative access without inbound SSH/RDP. State Manager maintains configured desired state; it does not replace an incident case record.

## Current status distinction

OpsCenter is not the same as Systems Manager Incident Manager. Current AWS documentation directs eligible Incident Manager migrations toward OpsCenter; Incident Manager's new-customer closure must not be misapplied to OpsCenter.

Tasks 5.2–5.3. [[AWS Systems Manager]], [[Fleet Manager vs OpsCenter vs Automation vs State Manager]].

- [Fleet Manager prerequisites/capabilities](https://aws.amazon.com/blogs/mt/streamline-server-fleet-management-aws-systems-manager-fleet-manager/)
- [OpsCenter incident workflow and migration context](https://docs.aws.amazon.com/incident-manager/latest/userguide/migration-opscenter.html)
