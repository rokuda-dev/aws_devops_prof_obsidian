---
tags:
  - aws
  - dop-c02
  - exam
updated: 2026-09-20
read: true
---

# Common Traps and Current Corrections

Status checked September 20, 2026. Product changes do not prove immediate exam question inclusion.

| Training statement/implication | Correct fact / exam consequence | Official source |
|---|---|---|
| CodeCommit is permanently unavailable to new customers | Reopened November 25, 2025; AWS-managed Git remains a valid service choice | [Document history](https://docs.aws.amazon.com/codecommit/latest/userguide/history.html) |
| X-Ray is retired | SDK/daemon maintenance began February 25, 2026; service remains supported; prefer OpenTelemetry instrumentation | [Support timeline](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-daemon-timeline.html) |
| Only CodeDeploy offers ECS blue/green/canary/linear | ECS-native supports these; use scenario/controller details to select | [Current AWS comparison](https://aws.amazon.com/blogs/devops/choosing-between-amazon-ecs-blue-green-native-or-aws-codedeploy-in-aws-cdk/) |
| Beanstalk means only EC2-based environments | Standard remains; Cluster Mode announced September 17, 2026 uses EKS | [Release note](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2026-09-17-cluster-mode.html) |
| Legacy Kinesis Data Analytics SQL architecture is current | SQL applications cannot be operated from January 27, 2026; retain streaming concepts, not this retired service | [Discontinuation notice](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/doc-history.html) |
| Application Discovery Service is open to every new customer | Closed to new customers November 7, 2025; AWS points to AWS Transform | [Availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html) |
| Discovery Connector is the current collector name | Use Agentless Collector; Discovery Agent supplies running-process information | [Collection options](https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html) |
| Install the standalone Inspector Agent | Obsolete legacy model; current scan integrations/modes differ | [Inspector overview](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) |
| All DynamoDB Global Tables are eventually consistent | MREC and MRSC have distinct semantics/restrictions | [Consistency modes](https://aws.amazon.com/blogs/database/best-practices-for-amazon-dynamodb-global-tables-part-1-operational-readiness/) |
| Aurora secondary write forwarding means multi-active writes | Writes are forwarded to the primary, not independently committed by multiple writers | [Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html) |
| OpsWorks Stacks is a current new architecture choice | Reached end of life May 26, 2024; the current exam guide still includes historical OpsWorks examples | [AWS migration announcement](https://aws.amazon.com/blogs/mt/seamlessly-off-board-from-aws-opsworks-stacks-by-detaching-resources/) |
| CodeBuild reports provide permanent retention | Reports expire after 30 days; export raw files to S3 for longer retention | [Test reports](https://docs.aws.amazon.com/codebuild/latest/userguide/test-reporting.html) |

## Domain 1 — SDLC traps

- “A CodePipeline’s second stage must be Build or Deploy” → a source action is required, but later stages can use supported Build, Test, Approval, Deploy, Invoke, or Compute actions. [Action requirements](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-requirements.html)
- “CodeDeploy blue/green supports on-premises” → only EC2 instances for blue/green on that compute platform; on-premises uses in-place. [Official overview](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html)
- “CodeDeploy ECS NLB supports canary/linear” → NLB supports ECSAllAtOnce only. [Deployment configurations](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html)
- “The four commonly shown CodeDeploy hook variables are the complete set” → EC2/on-premises hooks always receive five core variables, plus S3- or GitHub-specific bundle variables where applicable. [AppSpec hook variables](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html)
- “Deployment Succeeded means every EC2 instance updated” → built-in success thresholds/exceptions can allow partial failure; inspect target results and health.
- “CodeBuild cannot publish a Lambda version” → it can call authorized APIs; managed release tooling may still be the best answer.
- “Rollback reverses all writes” → traffic/artifact rollback does not automatically undo data or external effects.

## Domain 2 — configuration management and IaC traps

- “CDK is configuration as code” → Infrastructure as Code that synthesizes CloudFormation.
- “Chain sets” → CloudFormation StackSets.
- “AMI parameter changed, all instances upgraded” → stack/launch-template/fleet rollout is still required.
- “Config aggregator enforces” → visibility only.
- “SCP grants access” → maximum permission boundary only; grants must come elsewhere.
- “Run Command is interactive access” → Session Manager is the interactive capability.
- “Secrets/parameters update every running app immediately” → retrieval/caching/injection/update mechanics determine refresh.

## Cross-domain traps

- “CloudFront origin failover handles every HTTP method” → GET/HEAD/OPTIONS only, with appropriate cache behavior/options.
- “API keys authorize users securely” → not a substitute for API authorization.
- “GuardDuty, Inspector, Security Hub, Detective all do the same thing” → detection, vulnerabilities, prioritized posture/workflows, investigation.

## Domain 3 — resilience traps

| Trap | Correct exam interpretation |
|---|---|
| “Multi-AZ is multi-Region DR” | Multi-AZ addresses AZ failure inside a Region; regional recovery needs a deliberately prepared multi-Region design. |
| “Route 53 failover promotes the database” | Route 53 changes DNS answers. Promotion, write fencing, capacity, validation, and reconnection are separate recovery actions. |
| “A read replica proves the RPO” | Async replication lag must be monitored and tested against the stated maximum data-loss requirement. |
| “Global Accelerator can directly front any AWS service” | Standard endpoints are supported resources such as ALB, NLB, EC2, and Elastic IP—not direct RDS or API Gateway endpoints. |
| “DAX caches every DynamoDB read” | Strongly consistent and transactional reads pass through; DAX is for eligible eventually consistent read acceleration. |
| “Fargate automatically scales application replicas” | Fargate supplies compute. ECS desired-count policies or Kubernetes pod/node scaling still require configuration. |
| “ECR replication copies every existing image” | Replication applies to images pushed or restored after configuration; existing content needs a separate handling plan. |
| “Drift detection proves DR readiness” | Drift checks configuration. A DR test must restore/fail over, validate the application and data, and test failback. |

See [[Domain 3 Transcript Corrections]] for the full correction set.

## Domain 4 — monitoring and logging traps

| Trap | Correct exam interpretation |
|---|---|
| “CloudWatch automatically receives guest memory/disk metrics” | Install/configure the CloudWatch agent or another explicit publisher; default EC2 metrics do not include ordinary guest memory usage. |
| “SampleCount is the number of business transactions” | SampleCount counts metric samples; use Sum when each sample value represents a count to total. |
| “A centralized view is a copied archive” | OAM-linked observability differs from centralized copied logs and independent archival storage. |
| “CloudWatch Logs subscriptions automatically cover future accounts and groups” | Configure organization/OU centralization or explicit onboarding for new sources. |
| “ECS awslogs requires a host CloudWatch agent” | The log driver sends container stdout/stderr; host/guest telemetry is a separate agent concern. |
| “CloudTrail event history contains S3 object reads” | Event history shows 90 days of regional management events; object activity requires data-event selectors. |
| “CloudTrail digest files prevent tampering” | Digests enable integrity validation; access and storage controls prevent modification. |
| “Config periodic evaluation is the same as immediate API detection” | Config evaluates compliance on its trigger; CloudTrail/EventBridge can match the API event path separately. |
| “An alarm automatically remediates or rolls back” | The alarm must be connected to a supported action or deployment rollback configuration. |
| “Direct CloudWatch Logs → Firehose → OpenSearch always works” | The record format/path is not a universal direct integration; use a supported transformation/indexing design. |

See [[Domain 4 Transcript Corrections]] for the full correction set.

## Domain 5 — incident-response traps

| Trap | Correct exam interpretation |
|---|---|
| “A finding or event authorizes deletion” | Validate current state, ownership, exceptions, and impact before destructive remediation. |
| “A target invocation means the incident is resolved” | Monitor the handler/workflow and verify the real resource/application outcome. |
| “Config compliance identifies who accessed an S3 object” | Use CloudTrail data events and session identity for actor attribution; Config records resource state. |
| “Health exposed-key detection protects before source publication” | It is reactive; add preventive secret scanning and repository controls. |
| “Auto Scaling is DDoS protection” | Capacity can absorb demand but does not filter malicious traffic or prevent origin bypass. |
| “Lambda CodeDeploy uses ECS test-traffic hooks” | Lambda uses BeforeAllowTraffic and AfterAllowTraffic; the hook must report status to CodeDeploy. |
| “Exit code 137 always means out of memory” | It indicates SIGKILL; correlate stopped reason, memory, timeout, and operator/service actions. |
| “restricted-ssh permits only the corporate network” | The managed rule rejects world-open SSH; stricter approved-CIDR requirements need a custom policy/evaluation. |
| “OpsCenter and Fleet Manager are interchangeable” | OpsCenter tracks operational issues; Fleet Manager supplies managed-node administration tools. |
| “DLQ coverage proves workflow success” | A target DLQ captures certain delivery failures, not all errors inside an accepted execution. |

See [[Domain 5 Transcript Corrections]] and [[Detection vs Enforcement vs Remediation]].

## Domain 6 — security and compliance traps

| Trap | Correct exam interpretation |
|---|---|
| “On-premises workloads require long-lived access keys” | Use Roles Anywhere or another applicable federation method to obtain temporary credentials. |
| “An SCP or permissions boundary grants access” | Both limit maximum permissions; an identity/resource policy still must allow the action. |
| “A Config rule keeps an S3 bucket private” | Config is detective. Use Block Public Access and IAM/resource controls for prevention. |
| “A VPC endpoint policy replaces IAM or the bucket policy” | It restricts traffic through the endpoint; normal identity and resource authorization still applies. |
| “Macie redacts or blocks sensitive data during ingestion” | Macie discovers/classifies S3 data and policy risk; build a separate staged release/enforcement workflow. |
| “S3 default encryption rewrites existing objects or enforces a specific key in every request” | Defaults affect new writes; migrate old objects and add policy enforcement when the key contract matters. |
| “KMS never returns plaintext key material of any kind” | KMS key material stays protected, but GenerateDataKey can return an authorized plaintext data key. |
| “Encryption can be enabled in place on an existing unencrypted RDS DB instance” | Copy a snapshot with encryption, restore a replacement, and cut over; evaluate Aurora cluster workflows separately. |
| “KMS or ACM rotates database credentials” | Secrets Manager provides managed secret rotation; KMS protects cryptographic keys and ACM manages certificates. |
| “Inspector requires the old agent and assessment templates” | Inspector Classic is retired; use current Amazon Inspector coverage and integrations. |
| “All ARC capabilities closed to new customers” | The April 30, 2026 restriction applies to readiness checks; Region switch, routing controls, zonal shift, and zonal autoshift remain supported. |
| “Audit Manager is universally available for new setup” | New-account setup closed April 30, 2026; existing-customer availability is restricted. |

See [[Domain 6 Transcript Corrections]] for the full correction set.
