---
tags:
  - aws
  - dop-c02
  - domain-1
  - domain-2
  - systems-manager
read: false
---

# AWS Systems Manager

Systems Manager centrally views, manages, and operates managed nodes across AWS, on-premises, and multicloud environments.

## Feature selection

| Requirement | Feature |
|---|---|
| Execute non-interactive commands fleet-wide | Run Command |
| Interactive administration without inbound SSH/RDP | Session Manager |
| Maintain desired managed-node configuration | State Manager |
| Patch operating systems | Patch Manager / Quick Setup patch policies |
| Multi-step operational remediation | [[AWS Systems Manager Automation|Automation runbooks]] |
| Store hierarchical parameters | Parameter Store |
| Collect software/configuration inventory | Inventory |

## Managed nodes

SSM Agent and service connectivity are required.
For on-premises servers and external VMs, create a hybrid activation and register the machine as a managed node. (Managed hybrid instances will carry 'mi'-prefix.)
IAM roles/service roles and network access to Systems Manager endpoints must be correct.

## Important distinctions

- Run Command is non-interactive; Session Manager provides interactive access.
- State Manager maintains OS/software state; [[AWS Config]] evaluates AWS resource configuration.
- [[AWS Systems Manager Automation]] coordinates runbook steps and AWS API actions; Lambda is better for custom event-driven code, and Step Functions for application-level orchestration with complex branching/waits.

Source: [Systems Manager overview](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)

## Patch strategy

A patch baseline defines approval/rejection rules. Test updates in development/test before production and account for reboot/service interruption.

### Patch groups — traditional patching

Patch groups associate managed nodes with different patch baselines in traditional `AWS-RunPatchBaseline` workflows, such as using Run Command or a maintenance-window task.

- Assign a node with the case-sensitive tag key `PatchGroup` or `Patch Group`; the tag value is the group name, such as `DEV` or `PROD`. Prefer one key convention consistently. Use `PatchGroup` without a space when EC2 instance metadata tags are enabled.
- Register the patch-group value with a patch baseline. A managed node can belong to only one patch group, and a patch group can be registered with only one baseline for each operating-system type.
- During patching, SSM Agent and Patch Manager use the node's patch-group value to select the registered baseline. A node without a patch-group tag uses the currently configured default baseline for its operating-system type.
- Patch-group membership selects the baseline; it does not by itself run or schedule patching. Target the nodes and invoke `AWS-RunPatchBaseline` through Run Command or a maintenance window.

Example: nodes tagged `PatchGroup=DEV` can use a baseline that approves updates quickly, while `PatchGroup=PROD` can use a more conservative baseline after validation. A maintenance window can then target the appropriate tag value and control the production rollout schedule.

Do not confuse baseline lookup with tag targeting: baseline registration treats equal values under `PatchGroup` and `Patch Group` as the same patch group, but Run Command targeting treats those tag keys as different. Standardize on one key to avoid partial fleet targeting.

### Quick Setup patch policies

Quick Setup patch policies are the AWS-recommended centralized approach and do **not** use patch groups. A policy selects the baseline for each operating-system type and configures scan/install schedules across selected accounts and Regions or an organization. These require managed nodes and appropriate organization/service access; scan-only compliance reporting is not patch installation.

## Session and runbook security

Managed nodes need SSM Agent, authorized node/service roles, and outbound service connectivity. No inbound SSH/RDP is needed for standard Session Manager access, but IAM authorization and network prerequisites still apply. Standard session logging can be configured; do not assume encrypted SSH or port-forwarding session contents are recorded like ordinary shell sessions.

[[AWS Systems Manager Automation|Automation runbooks]] can interact with AWS resources without requiring every resource to be an SSM managed node. Run Command/State Manager host operations target managed nodes. Use approvals, scoped roles, and rate/error controls for high-impact fleet changes.

## Official AWS references

- [Hybrid/multicloud environments](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-hybrid-multicloud.html)
- [Patch groups](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-patch-groups.html)
- [Quick Setup patch policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-patch-manager.html)
- [Patch policy features](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-policies.html)
- [[AWS Systems Manager Automation]]
- [[Run Command vs Session Manager vs State Manager vs Automation]]

## Domain 3 — automated repair and recovery

Automation can build/customize AMIs and execute controlled drift repair/recovery runbooks. Include inputs, least-privilege roles, approvals where needed, bounded concurrency, retries, verification, and failure paths.

Config-triggered remediation and recovery tests are separate: repair an expected setting, then validate the application. Runbooks/artifacts and needed execution paths must remain available during the failure.

Tasks 3.2–3.3. See [[AWS Config]], [[EC2 Image Builder]], [[Disaster Recovery Testing and Failback]].

## Domain 4 — agents and configuration convergence

SSM Agent and CloudWatch agent serve different purposes. ASG events can trigger current-membership reconciliation followed by Run Command on a correctly managed batch host. Validate and update configuration safely; complete lifecycle hooks where used.

State Manager maintains supported desired configuration from an approved/versioned source; Automation coordinates multi-step response. These patterns replace the retired OpsWorks Stacks/Chef example.

Resource data sync has Inventory SyncToDestination and Explorer SyncFromSource uses. It does not replace Health → EventBridge → SNS notifications.

Tasks 4.1 and 4.3. See [[Safe Event-Driven Remediation]], [[CloudWatch Agent and Container Log Collection]].
- [Data sync types](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-resourcedatasync.html)

## Domain 5 — incident capability selection

Fleet Manager supports managed-node inspection/tools. OpsCenter centralizes OpsItems and contextual investigation. Run Command executes node commands, State Manager maintains configured desired state, Patch Manager handles patches, and Automation performs controlled multi-step operations.

Session Manager can reduce administrative attack surface by eliminating inbound SSH/RDP requirements; this does not make Systems Manager a DDoS traffic filter. Use segmentation/least privilege and dedicated traffic defenses where needed.

For datacenter-only SSH repair, use authoritative approved CIDRs and a scoped, live-state-aware runbook; avoid administrative lockout or altering unrelated rules.

Tasks 5.2–5.3. [[Systems Manager Incident Operations]], [[Fleet Manager vs OpsCenter vs Automation vs State Manager]], [[Security Group Remediation and Access Safety]].

## Domain 6 — multi-account security operations

Automation can run across configured accounts, OUs, and Regions using a central administration role and execution roles in targets. Patch Manager requires supported managed nodes; Quick Setup patch policies centralize schedules/baselines. Patch compliance is evidence, not proof that the application is vulnerability-free.

Tasks 6.2–6.3. [[Domain 6 Monitoring Auditing and Compliance]], [[Amazon Inspector]], [[AWS Config]].
