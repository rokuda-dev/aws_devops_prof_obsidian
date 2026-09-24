---
tags: [aws, dop-c02, exam]
updated: 2026-09-20
read: false
---

# Rapid Review

## Cross-domain foundations

| Cue | Recall |
|---|---|
| Orchestrate / build / deploy | CodePipeline / CodeBuild / CodeDeploy |
| Packages / containers / AMIs | CodeArtifact / ECR / Image Builder |
| Declarative / language-based / serverless IaC | CloudFormation / CDK / SAM |
| Many accounts and Regions | StackSets + correct trust/permissions |
| Lambda canary | Version + alias + CodeDeploy + alarms/hooks |
| ECS gradual rollout | Native strategies or CodeDeploy, match the controller |
| Preview infrastructure change | Change set; not a success guarantee |
| Maintain installed host software | State Manager |
| Commands everywhere / interactive shell | Run Command / Session Manager |
| Patch organization | Quick Setup patch policy, managed nodes required |
| Operational remediation / complex workflow | SSM Automation / Step Functions |
| Event routing / custom handler | EventBridge / Lambda |
| Resource history / actor / app behavior | Config / CloudTrail / CloudWatch |
| Central Config view | Aggregator, no enforcement |
| Permission cap / account vending | SCP / Control Tower Account Factory |
| Approved self-service / existing shared resource | Service Catalog / RAM |
| Runtime flags / parameters / rotating credentials | AppConfig / Parameter Store / Secrets Manager |
| Threat / vulnerability / investigation | GuardDuty / Inspector / Detective |
| Global multi-active NoSQL | DynamoDB Global Tables; distinguish MREC/MRSC |
| Global relational primary + secondaries | Aurora Global Database; switchover vs failover |
| Sensitive POST field at edge | CloudFront field-level encryption + HTTPS |
| Instances safely replaced | External state and backward-compatible data changes |

Read [[Common Traps and Current Corrections]] before relying on older training. For more precise differences, use [[Service Selection Matrix]] and the Comparisons folder.

## Domain 1 — final-pass anchors

| Cue | Recall |
|---|---|
| Orchestrate / build / deploy | CodePipeline / CodeBuild / CodeDeploy |
| Language packages / containers / AMIs | CodeArtifact / ECR / Image Builder |
| Immutable promotion | Build once, identify by version/digest, promote the same tested artifact |
| Cross-account pipeline | Trust + action role + artifact bucket/KMS permissions |
| Cross-Region action | Artifact store in each action Region |
| Lambda canary | Published version + alias + CodeDeploy + hooks/alarms |
| ECS blue/green | Match native ECS or CodeDeploy controller details to the scenario |
| EC2/on-premises deployment | Nine scriptable hooks; four agent-reserved events; deployment group, health thresholds, and rollback behavior |
| CodeDeploy hook variables | Five always available; add S3/GitHub bundle-source variables where applicable |
| Change set | Preview/review mechanism, not a guarantee of successful execution |
| Test evidence | CodeBuild reports expire; retain raw results externally when required |

## Domain 2 — final-pass anchors

| Cue | Recall |
|---|---|
| Declarative / language-based / serverless IaC | CloudFormation / CDK / SAM |
| Many accounts and Regions | StackSets + correct administrator/execution trust and permissions |
| Approved self-service / shared resource | Service Catalog / RAM |
| Account vending / permission ceiling | Control Tower Account Factory / Organizations SCP |
| Resource state / actor history | Config / CloudTrail |
| Central Config visibility | Aggregator; it does not enforce or remediate |
| Desired host state / operational runbook | State Manager / SSM Automation |
| Interactive access / fleet command | Session Manager / Run Command |
| Event routing / workflow | EventBridge / Step Functions |
| Configuration / parameter / secret | AppConfig / Parameter Store / Secrets Manager |

## Domain 3 — final-pass anchors

| Cue | Recall |
|---|---|
| RTO / RPO | End-to-end recovery duration / maximum acceptable recovered-data age |
| AZ failure / regional failure | Multi-AZ / deliberately designed multi-Region recovery |
| ALB cross-zone | On at LB level; TG-level override exists |
| NLB health | TG thresholds, cross-zone scope, DNS withdrawal, fail-open |
| Simple cooldown / warmup / hook | Simple-policy timing / scaling-metric stabilization / transition wait |
| EKS scaling | HPA pods versus Karpenter/CA/Auto Mode node capacity |
| Fargate | Hostless compute, not free idle allocations or automatic replica policy |
| DAX | Eventual read cache; strong/transaction reads pass through |
| MySQL major upgrade | Supported path/replica order/topology; consider Blue/Green |
| Route 53 failover | DNS answers only; does not promote a DB |
| Global Accelerator | Static IP frontend; supported ALB/NLB/EC2/EIP endpoints |
| Aurora Global | One primary; planned switchover versus unplanned possible-loss failover |
| Cross-Region RDS replica | Async lag + explicit promotion + reconnect/fencing |
| S3 CRR | Versioning/permissions; existing objects may need Batch Replication |
| Backup continuous copy | Snapshot at destination, not preserved continuous PITR stream |
| DR validation | Restore, failover, real app/data verification, failback; not drift only |

See [[Domain 3 Scenario Decisions]] and [[Domain 3 Transcript Corrections]].

## Domain 4 — final-pass anchors

| Cue | Recall |
|---|---|
| Guest memory/disk versus container stdout | CloudWatch agent versus awslogs task driver |
| Agent namespace | CWAgent, exact spelling |
| Custom metric identity | Namespace/name/dimensions; no automatic custom rollup |
| Aggregate observations | StatisticValues: Sum, SampleCount, Minimum, Maximum |
| Payment/refund total | Sum for the chosen minute; not SampleCount |
| Publish metric / export metric | PutMetricData or EMF / metric stream through Firehose |
| Log match to count / forward / investigate | Metric filter / subscription / Logs Insights |
| Cross-account subscriptions | Logical destination + policy/role; Kinesis or documented Firehose path |
| Federated view / copied logs | OAM / Logs centralization |
| Native log centralization | New data after rule creation, not historical backfill |
| S3 log archive SQL / indexed search | Athena / OpenSearch |
| Direct CW Logs → Firehose → OpenSearch | Currently unsupported batched-record path |
| ECS log roles | Fargate awslogs execution role; FireLens destination task role |
| Current ECS log mode | Non-blocking default unless overridden; explicit backpressure choice |
| CloudTrail event history | 90 days of regional management events |
| S3 object access audit | Explicit CloudTrail data-event selectors |
| Digest validation | Detects tampering; does not prevent it |
| Bucket-policy alert | CloudTrail → metric filter/alarm/SNS or API event → EventBridge |
| Variable metric / threat / sensitive S3 data | Anomaly band / GuardDuty / Macie |
| AWS maintenance | Health → EventBridge → SNS |
| Trail compliance / StopLogging | Periodic Config evaluation / API event detection |
| Health of SQS worker | Consumer/application controls, not built-in ALB-style SQS checks |
| Retired configuration example | OpsWorks Stacks; use supported SSM desired-state/workflows |
| Legacy dashboard / Inspector templates | Unsupported solution / retired Inspector Classic |

See [[Domain 4 Scenario Decisions]], [[Domain 4 Transcript Corrections]].

## Domain 5 — final-pass anchors

| Cue | Recall |
|---|---|
| Actor / compliance / numeric breach / AWS impact | CloudTrail / Config / CloudWatch alarm / Health |
| Event target succeeds | Still verify accepted handler/workflow and real recovery |
| Public-list-only S3 | Exact custom policy evaluation; listing is metadata exposure |
| Compliance-team object access | Policy enforcement + selected data events + role/session attribution |
| Config and Step Functions | Not a direct custom-rule evaluator; response can bridge via EventBridge/SSM |
| Exposed-key Health event | After detected exposure; preventive scanning is separate |
| Key containment | Exact verified key, prompt deactivate/delete, audit, rotate and investigate |
| Auto Scaling in DDoS | Capacity, not malicious-traffic filtering or reduced exposure |
| Shield / WAF / CloudFront | DDoS / web rules / edge; protect against direct origin bypass |
| SSM and attack surface | Session Manager can remove public SSH; not a DDoS filter |
| Lambda hook names | BeforeAllowTraffic and AfterAllowTraffic; test target version |
| Hook completion | PutLifecycleEventHookExecutionStatus callback, not return alone |
| Same runOrder | Parallel independent actions within a stage |
| MinimumHealthyHosts types | HOST_COUNT/FLEET_PERCENT are configuration, not health metrics |
| HTTPS regression | 443 + return path + DNS/routes + TLS + actual API response |
| ECS 137 | SIGKILL; confirm OOM versus stop timeout/other cause |
| Container Insights | Collection must be configured; not an autoscaler |
| Dedicated Host | Allocated host placement, not merely dedicated instance tenancy |
| restricted-ssh | No world-open SSH; not a datacenter-only guarantee |
| Fleet Manager / OpsCenter | Node tools / OpsItems with contextual investigation |
| RefreshCache | Async cached inventory update, not data preload/write flush |

[[Domain 5 Scenario Decisions]], [[Domain 5 Transcript Corrections]].

## Domain 6 — final-pass anchors

| Cue | Recall |
|---|---|
| Workforce / workload / application users | Identity Center / roles or Roles Anywhere / Cognito |
| Trust / permissions / session / organization ceiling | Who may assume / role capability / temporary restriction / SCP maximum |
| SCP or permissions boundary | Limits maximum permissions; grants nothing by itself |
| ABAC | Principal/resource/request tags with controlled tagging permissions |
| Private EC2 → S3 | Instance role + network path + IAM/bucket policy + KMS permission when applicable |
| S3 endpoint policy | Restricts endpoint use; does not replace IAM or bucket authorization |
| Keep S3 private | Block Public Access/preventive policy + Config detection + bounded remediation |
| Sensitive S3 data | Macie discovers/classifies; a separate gate enforces release or transformation |
| KMS / CloudHSM / ACM | Managed key integration / dedicated HSM / certificate lifecycle |
| Envelope encryption | Generate data key → local encryption → erase plaintext key → retain encrypted key |
| S3 bucket encryption default | Controls new writes; migrate old objects and enforce the required key separately |
| Existing unencrypted RDS DB | Snapshot → encrypted copy → restore replacement → cut over |
| Static encrypted parameter / rotating secret | Parameter Store SecureString / Secrets Manager |
| Parameter Store Secrets Manager reference | `/aws/reference/secretsmanager/<secret>`; path retrieval restrictions apply |
| WAF / Shield / Network Firewall / DNS Firewall | HTTP rules / DDoS / routed VPC inspection / Resolver-domain filtering |
| Firewall Manager | Organization-scale supported policies with prerequisites and scoped remediation |
| GuardDuty / Inspector / Macie / Access Analyzer | Threats / vulnerabilities / sensitive S3 data / external access analysis |
| Security Hub | Central findings and posture workflow; not the original detector |
| Hybrid patching | SSM managed nodes + Patch Manager scheduling/policy + compliance review |
| Approved AMI + vulnerability evidence | Allowed/approved AMI controls + current Inspector; not Inspector Classic |
| Audit actor / configuration / workload | CloudTrail / Config / CloudWatch |
| ARC availability caveat | Readiness checks closed to new customers; do not generalize to all ARC features |
| Audit Manager availability caveat | New-account setup closed April 30, 2026 |

[[Domain 6 Scenario Decisions]], [[Domain 6 Transcript Corrections]].
