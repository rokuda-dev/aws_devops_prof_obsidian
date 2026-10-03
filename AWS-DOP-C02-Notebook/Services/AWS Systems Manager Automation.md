---
title: AWS Systems Manager Automation
tags:
  - aws
  - dop-c02
  - service
  - systems-manager
  - automation
updated: 2026-10-03
read: false
---

# AWS Systems Manager Automation

Systems Manager Automation runs controlled, multi-step operational workflows against AWS resources and managed nodes. The workflow definition is an **Automation runbook**, an SSM document of type `Automation`; AWS supplies managed runbooks, and teams can create versioned YAML or JSON runbooks of their own.

## Exam mapping

Primary task: 2.3. Also relevant to 3.3 recovery, 5.1–5.3 event response and troubleshooting, and 6.2–6.3 multi-account remediation. See [[Domain 2 - Configuration Management and IaC]], [[Domain 5 - Incident and Event Response]], and [[AWS Systems Manager]].

## Runbook model

An Automation runbook uses schema version `0.3`. It declares parameters and ordered steps under `mainSteps`; a step selects an Automation action, supplies inputs, and can expose outputs to later steps as `{{ stepName.outputName }}`.

Common building blocks include:

| Need | Representative action |
|---|---|
| Call an AWS API | `aws:executeAwsApi` |
| Run Python or PowerShell | `aws:executeScript` |
| Run a Command document on a managed node | `aws:runCommand` |
| Test or wait for resource state | `aws:assertAwsResourceProperty`, `aws:waitForAwsResourceProperty` |
| Branch or repeat | `aws:branch`, `aws:loop` |
| Pause for a human decision | `aws:approve` |
| Reuse another runbook | `aws:executeAutomation` |
| Start a Step Functions workflow | `aws:executeStateMachine` |

Shared step properties include `maxAttempts`, `timeoutSeconds`, `onFailure`, `onCancel`, `nextStep`, `isCritical`, and `isEnd`. Use them deliberately: a retry needs idempotent behavior, `onFailure: Continue` is not recovery, and a successful API response is not proof that the application recovered.

## Permissions and execution context

By default, Automation uses the permissions of the principal that started the execution. An Automation assume role lets the service run with a defined permission set instead; the starter needs permission to pass that role. Prefer a dedicated least-privilege role whose permissions cover only the runbook's actions and resources.

An assume role is required in some cases, including a State Manager association that runs a runbook, operations expected to exceed 12 hours, and a non-Amazon-owned runbook whose `aws:executeScript` action calls AWS APIs. The role's trust and permissions are separate from the caller's permission to start the automation and `iam:PassRole` authorization.

> [!warning]
> Access to Automation does not grant the downstream EC2, S3, RDS, IAM, or other service permissions used by a runbook. Conversely, an overpowered assume role can turn permission to start a runbook into an unintended privilege-escalation path. Constrain who may start which document, which role may be passed, parameter values where possible, and the role's resource scope.

## Targets and safe fleet rollout

Automation can map a runbook parameter to resources selected by parameter values, tags, or Resource Groups. With targets, Systems Manager creates child automations for the resolved resources.

- `MaxConcurrency` limits how many targets run at once; use a small canary batch for disruptive production changes.
- `MaxErrors` is a stop-sending threshold, not transactional rollback. Work already started can still finish.
- A CloudWatch alarm can cancel a rate-control execution when it enters `ALARM`; design the `onCancel` path and post-change verification.
- Recheck live state before mutating a resource. This matters especially for Config auto-remediation, which can start from a stale compliance snapshot.

For high-impact operations, combine precise targets, validation, bounded retries, approvals where supported, explicit failure/cancellation paths, and outcome verification. Preserve unrelated configuration and avoid locking out administrative access.

## Multi-account and multi-Region operation

A central account can start automations across specified accounts, organizational units, and Regions. This requires the administration role in the initiating account, execution roles in target accounts, `iam:PassRole`, and target-location controls. Location-level concurrency/error controls govern account-Region pairs; resource-level rate controls govern targets inside each location.

The `aws:approve` action does **not** support multi-account and multi-Region automations. Do not choose a design that depends on an embedded approval step in that execution mode.

## Common DOP-C02 patterns

```text
Config evaluation -> NON_COMPLIANT -> Automation runbook
  -> recheck live state -> bounded repair -> verify compliance/outcome

EventBridge event -> Automation runbook
  -> collect context -> approve if supported -> change -> validate -> notify/escalate

Central operations account -> target accounts/Regions
  -> target execution role -> rate-controlled child automations -> central status review
```

- **Golden AMI workflow:** validate inputs, create a temporary builder or invoke commands, create the image, wait for availability, test, tag, and distribute deliberately. [[EC2 Image Builder]] is the purpose-built image pipeline alternative.
- **Config remediation:** pair a rule with an Amazon-owned or custom Automation document. Pass the resource ID correctly, use remediation retry/rate controls, and make the runbook safe if the recorded evaluation is stale.
- **Incident runbook:** gather evidence before mutation, use narrow changes, retain execution output, validate recovery, and create or update the operational record.
- **Disaster recovery:** Automation can coordinate supported AWS operations, but traffic switching alone does not promote data stores or prove recovery. Include ordering, writer fencing, validation, and failback.

## Choose Automation versus adjacent services

| Requirement | Better first choice |
|---|---|
| Repeatable multi-step AWS operational runbook | Automation |
| One non-interactive command across managed nodes | Run Command |
| Continuously maintain managed-node configuration | State Manager |
| Interactive shell without inbound SSH/RDP | Session Manager |
| Application/business workflow with rich state-machine orchestration | [[AWS Step Functions]] |
| Focused custom event handler | [[AWS Lambda]] |
| Record/evaluate resource configuration | [[AWS Config]]; invoke Automation separately for remediation |

Automation does not universally require the target to be a managed node: AWS API actions can operate on AWS resources directly. A step that uses `aws:runCommand`, however, requires a properly registered and connected managed node with SSM Agent and suitable permissions.

> [!exam]
> Choose Automation when the scenario emphasizes an operational runbook, AWS resource changes, approvals, rate-controlled targets, or reusable remediation. Choose Step Functions for broader application orchestration and Run Command for a direct fleet command. Always separate detection, authorization, execution, and verification.

## Official AWS references

- [Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
- [Automation actions reference](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-actions.html)
- [Setting up Automation and assume-role permissions](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup.html)
- [Run automated operations at scale](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-automations-scale.html)
- [Run automations in multiple accounts and Regions](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-automations-multiple-accounts-regions.html)
- [AWS Config automatic remediation](https://docs.aws.amazon.com/config/latest/developerguide/setup-autoremediation.html)
- [[Run Command vs Session Manager vs State Manager vs Automation]]

