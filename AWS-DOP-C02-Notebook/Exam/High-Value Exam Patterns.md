---
tags: [aws, dop-c02, exam]
updated: 2026-09-20
read: false
---

# High-Value Exam Patterns

## Domain 1 — SDLC automation

### Source to release

[[AWS CodeCommit]] or external source through [[AWS CodeConnections]] → [[AWS CodeBuild]] build/test/scan → appropriate registry/artifact store → [[AWS CodeDeploy]] or platform deployment → [[Amazon CloudWatch]].
Retain commit/digest metadata and promote the same tested artifact.

### Cross-account and cross-Region pipeline

See [[Cross-Account and Cross-Region CodePipeline]]. Cross-account trust + S3 + customer-managed KMS authorization; artifact store in each action Region. These are independent dimensions.

### Lambda alias canary

Publish immutable version → CodeDeploy routes a small percentage through an alias → pre/post validation and alarms → full traffic or rollback. Keep the old version; rollback cannot reverse external side effects.

### ECS blue-green with CodeDeploy

New task definition/image → replacement task set → two target groups → optional test listener → AppSpec Lambda validation → production traffic shift → alarms and rollback. Native ECS is an alternative: [[ECS Native vs CodeDeploy Deployments]].

### CloudFormation change set pipeline

Source template → create change set → review/manual approval → execute change set with scoped CloudFormation role → stack events. Change set approval is not a guarantee of update success.

### Environment-specific CodeDeploy hook

EC2/on-premises AppSpec hook → one of the five always-available variables (`APPLICATION_NAME`, `DEPLOYMENT_ID`, `DEPLOYMENT_GROUP_NAME`, `DEPLOYMENT_GROUP_ID`, `LIFECYCLE_EVENT`) or an applicable S3/GitHub bundle variable → controlled environment-specific logic.
ApplicationStop comes from the previous successful revision; keep lifecycle scripts idempotent and compatible.

## Domain 2 — configuration management and IaC

### Config rule remediation

Recorded resource/evaluation → NON_COMPLIANT → authorized SSM Automation → recheck actual state → remediate or exception. Scope role, concurrency, retries, and approval for destructive runbooks.

### Multi-account Config governance

Organizations → distributed organization rules/conformance packs.
Aggregators provide a central view in a separate visibility branch; compliant/noncompliant events or locally configured remediation trigger action in the appropriate accounts. Do not model the aggregator as the enforcement engine.

### Account vending

Control Tower landing zone → Account Factory → standardized enrolled/governed account → continued controls and drift operations.

### Governed self-service

Approved CloudFormation template → Service Catalog product/version → portfolio + launch-role constraint → authorized user provisions product.

### Hybrid managed nodes

Create hybrid activation → register external server using SSM Agent/activation → managed node → Run Command, State Manager, patching.
Agent connectivity and IAM are prerequisites, not optional extras.

### DynamoDB item-change automation

Item change → DynamoDB Streams → Lambda event-source mapping → idempotent processing/remediation.
Monitor consumer failures and avoid assuming exactly-once delivery.

### Event-driven multi-step remediation

EventBridge pattern → Step Functions → API/Lambda task → retry/catch/approval → notify/compensate.
Use SSM Automation instead when an operational runbook directly matches the requirement.

## Cross-domain foundations

### Alarm-driven rollback

Deployment/config rollout with enabled alarm integration → adverse health metric → stop/rollback action → verify application recovery.
Alarm creation alone does not configure the deployment service to roll back.

### External state

Disposable application instances/tasks → external session/database/files/object store → safe replacement.
Stickiness cannot preserve instance-local state after termination.

## Domain 3 — resilience, scaling, and recovery

| Requirement | High-value pattern | Decisive safeguard |
|---|---|---|
| Survive an AZ failure | Multi-AZ load-balanced compute with enough surviving capacity and highly available regional state | Remove single-AZ dependencies; enable appropriate health replacement |
| Meet a regional RTO/RPO | Prebuilt recovery stack + suitable cross-Region data replication + promotion/orchestration + traffic failover | Measure lag and full recovery time; fence the old writer before accepting writes |
| Global relational workload | Regional application stacks + [[Amazon Aurora Global Database]] | One primary write Region; plan reconnect, switchover/failover, and possible data loss |
| Global NoSQL active writes | [[Amazon DynamoDB]] global tables with the required MREC/MRSC model | Do not substitute a different data model merely because it is multi-Region |
| Fast, repeatable EC2 scale-out | Golden AMI + launch-template version + multi-AZ Auto Scaling group | Roll out the new version; keep dynamic secrets/configuration outside the image |
| Controlled DR execution | [[AWS Step Functions]], SSM Automation, or ARC Region switch for ordered recovery actions | Idempotency, bounded retries, approvals, validation, and failback |
| DNS or accelerator failover | Route 53 health-based routing or Global Accelerator with supported endpoints | Traffic steering does not promote databases or create recovery capacity |
| Prove recoverability | Restore and failover exercises with application/data validation | Config or CloudFormation drift detection alone is not a DR test |

See [[Domain 3 Architecture Patterns]], [[Domain 3 Scenario Decisions]], and [[Domain 3 Transcript Corrections]].

## Domain 4 — monitoring and logging

| Requirement | High-value pattern | Decisive safeguard |
|---|---|---|
| Guest OS logs and memory/disk metrics | CloudWatch agent → log groups and CWAgent/custom metrics | Correct node identity, permissions, network path, retention, and dimensions |
| Container stdout/stderr | ECS `awslogs` or FireLens route | Execution role versus task role depends on the delivery path |
| Central cross-account archive | Log subscription or native organization centralization → protected destination/S3 | New-account onboarding, delivery monitoring, encryption, retention, and backfill plan |
| S3 object-access audit | CloudTrail data-event selectors → protected trail destination and analysis | Management event history does not include ordinary object reads/writes |
| Numeric workload alarm | Custom metric/EMF or metric filter → alarm → SNS or deployment integration | Choose the correct statistic, dimensions, period, and missing-data behavior |
| Compliance detection and repair | Config recording/rule → compliance event → authorized Automation/Lambda → re-evaluation | Detection, routing, authorization, and remediation are separate capabilities |
| API change response | CloudTrail-captured API event → EventBridge → bounded handler/workflow | Match the actual API schema; accepted delivery is not verified recovery |
| Federated versus copied observability | OAM for linked views; centralization/subscriptions for copied data | A federated view is not an independent archive |

See [[Domain 4 Architecture Patterns]], [[Domain 4 Scenario Decisions]], and [[Domain 4 Transcript Corrections]].

## Domain 5 — incident and event response

| Requirement | High-value pattern | Decisive safeguard |
|---|---|---|
| Select the event source | CloudTrail for actor/API, Config for compliance, alarms for numeric state, Health for AWS-impact events | Choose the source before the target; schemas and latency differ |
| Bounded incident automation | Event → validate/recheck → contain/remediate → verify → record/escalate | Preserve evidence, handle duplicates, and scope the target role |
| S3 public-policy remediation | Exact Config/custom evaluation → scoped repair + notification | Do not destroy approved exceptions or confuse bucket state with object actors |
| Exposed access key | Preventive secret scanning plus reactive containment, audit, rotation, and investigation | Scope the exact key; a Health event is reactive, not a pre-commit control |
| Lambda deployment validation | Candidate version → BeforeAllowTraffic callback → alias shift → alarms/post-hook | Returning from the hook is insufficient; report status to CodeDeploy |
| HTTPS regression triage | Validate DNS/routes, port and return path, TLS identity/SNI, and application response from workload context | Flow Logs ACCEPT or a laptop test does not prove end-to-end success |
| Container failure triage | Service/pod events + stopped reason/exit code + logs + health/IAM/network | Exit 137 is SIGKILL, not uniquely proof of OOM |
| Operational case management | OpsCenter OpsItem + evidence + approved Automation | Fleet Manager is node tooling, not the incident record system |

See [[Domain 5 Architecture Patterns]], [[Domain 5 Scenario Decisions]], and [[Domain 5 Transcript Corrections]].

## Domain 6 — security and compliance

| Requirement | High-value pattern | Decisive safeguard |
|---|---|---|
| Workforce access at scale | IAM Identity Center/federation → permission sets/roles → temporary sessions | SCPs and boundaries cap permissions but grant none |
| External workload access | Roles Anywhere or another supported federation path → temporary role credentials | Avoid permanent IAM-user keys where temporary identity is supported |
| Multi-account control loop | Prevent → detect → route → assume scoped target role → remediate → re-evaluate → preserve evidence | Delegated administration and execution roles must be configured explicitly |
| Sensitive-data ingestion | Restricted staging → Macie/classification result tied to the object version → transform/reject → verified release | Macie classifies; it does not synchronously block or redact ingestion |
| Local envelope encryption | KMS GenerateDataKey → encrypt locally → erase plaintext data key → store encrypted data key with ciphertext | KMS key material remains protected; authorized plaintext data keys can be returned |
| Encrypt an existing RDS DB instance | Snapshot → encrypted copy → restore replacement → cut over | Encryption is not toggled in place |
| Rotating application credentials | Secrets Manager rotation + consumer refresh/reconnect | KMS and ACM do not rotate database credentials |
| Organization network controls | Firewall Manager applies supported WAF/Shield/security-group/network-firewall policies | Prerequisites, account/Region scope, tags, and remediation settings still matter |
| Hybrid patch compliance | Managed nodes + Patch Manager policy/schedule + compliance reporting | Config can detect state but does not install operating-system patches |
| Vulnerability and AMI governance | Allowed/approved AMI controls + current Amazon Inspector findings | Do not use Inspector Classic assessment-template/agent workflows |

See [[Domain 6 Architecture Patterns]], [[Domain 6 Scenario Decisions]], and [[Domain 6 Transcript Corrections]].
