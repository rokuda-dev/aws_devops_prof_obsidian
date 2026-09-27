---
tags: [aws, dop-c02, audit]
updated: 2026-09-27
read: false
---

# Audit Delivery and Comparisons 2026-09-27

Read 54 AWS service/navigation pages and all 30 comparison pages. Each substantive row identifies the claim checked, not a claim that every sentence or linked document was independently reverified. Navigation pages received link/role checks. Comparison checks reuse the current evidence for their canonical services and the other two audit reports.

## Corrections and additions

- [[AWS CodeConnections]]: replaced the older redirected documentation URL.
- [[AWS CodePipeline]] and its comparison: clarified that V2 Commands can execute shell commands on managed CodeBuild compute without creating a separate project; prefer a full cross-account KMS key ARN.
- [[AWS CloudTrail]]: added the CloudTrail Lake new-customer restriction without generalizing it to trails.
- [[AWS Secrets Manager]]: distinguished Lambda rotation from managed and managed external-secret rotation.
- [[AWS Shield]] and its comparison: added the current WAF Anti-DDoS transition and legacy access caveat.
- [[Log Subscription vs Metric Filter vs EventBridge Rule]]: added native scheduled Logs Insights log alarms.

## Service page coverage

Domain/task associations remain in each study page. These checks chiefly cover Domain 1 tasks 1.1–1.4, Domain 2 tasks 2.1–2.3, and shared tasks 3.1–6.3.

| Page | Selected claim/result | Evidence |
|---|---|---|
| [[AWS AppConfig]] | Validators, gradual rollout, configured alarm rollback; retained | [AppConfig][appconfig] |
| [[AWS AppConfig, Parameter Store, and Secrets Manager]] | Compatibility navigation to three distinct services; links checked | Canonical rows in this table |
| [[AWS Application Auto Scaling]] | ECS desired count and DynamoDB table/GSI capacity are supported targets; retained | [Scalable services][aas] |
| [[AWS Application Discovery Service]] | New-customer closure, collector/agent distinction; retained | [Availability][ads] |
| [[AWS Audit Manager]] | New setup/account/Region restrictions; retained | [Availability][auditmanager] |
| [[AWS Backup]] | Continuous copies become snapshots; no on-demand continuous copy; retained | [Continuous copies][backup] |
| [[AWS CDK]] | Infrastructure code deploys through CloudFormation; retained | [CDK overview][cdk] |
| [[AWS Certificate Manager]] | Eligible public certificates can be exported; retained | [Exportable certificates][acm] |
| [[AWS CloudFormation]] | Drift applies to supported resource types/properties; retained | [Drift detection][cfn] |
| [[AWS CloudFormation StackSets]] | Multi-account/Region template deployment; retained | [StackSets][stacksets] |
| [[AWS CloudFormation, CDK, and SAM]] | Compatibility navigation; links checked | Canonical rows in this table |
| [[AWS CloudHSM]] | Hardware-specific FIPS 140-3 versus historical 140-2 validation; retained | [Compliance][hsm] |
| [[AWS CloudTrail]] | Trails versus Lake lifecycle distinction; added caveat | [Lake availability][lake] |
| [[AWS CodeArtifact]] | Package repositories, domains, upstream/public dependency retrieval; retained | [Overview][artifact] |
| [[AWS CodeBuild]] | Reports expire after 30 days; raw S3 export is separate; retained | [Reporting][build] |
| [[AWS CodeCommit]] | Reopened November 25, 2025; retained | [Document history][commit] |
| [[AWS CodeCommit and CodeConnections]] | Storage versus external connection navigation; links checked | Canonical rows in this table |
| [[AWS CodeConnections]] | External repository integration; canonical URL updated | [Connections][connections] |
| [[AWS CodeDeploy]] | Platform-specific hook variables and success thresholds; retained | [Hooks][hooks], [configurations][deploy] |
| [[AWS CodePipeline]] | V2 feature distinction and managed Commands compute; clarified | [Pipeline types][pipeline], [Commands][commands] |
| [[AWS Config]] | Recorded state/compliance differs from per-object API audit; retained | [Overview][config] |
| [[AWS Control Tower]] | Landing zone, Account Factory, preventive/detective/proactive controls; retained | [Overview][tower] |
| [[AWS Elastic Beanstalk]] | Standard versus September 2026 EKS-backed Cluster Mode; retained | [Launch][beanstalk] |
| [[AWS Elastic Disaster Recovery]] | Crash-consistent disk replication; recovery timing depends on workload; retained | [Concepts][drs] |
| [[AWS Fargate]] | Task/pod requested resources accrue charges until termination; retained | [Billing basis][fargate] |
| [[AWS Firewall Manager]] | Organization/administrator and feature prerequisites; retained | [Prerequisites][fms] |
| [[AWS Global Accelerator]] | Standard ALB/NLB/EC2/EIP endpoints; retained | [Supported endpoints][ga] |
| [[AWS Glue]] | Data Catalog metadata is not sensitive-data enforcement; retained | [Catalog][glue] |
| [[AWS Health]] | EventBridge delivery and organization scope; retained | [Events][health] |
| [[AWS IAM Identity Center]] | Workforce access, applications and accounts; retained | [Overview][identitycenter] |
| [[AWS IAM Roles Anywhere]] | External workload X.509 trust anchors/profiles and temporary credentials; retained | [Overview][rolesanywhere] |
| [[AWS Identity and Access Management]] | Permission boundaries/direct resource grants require nuanced evaluation; retained | [Evaluation][iam] |
| [[AWS Key Management Service]] | Authorized plaintext data key differs from protected KMS key; retained | [Data keys][kms] |
| [[AWS Lambda]] | Alias points to a version and can split between two versions; retained | [Aliases][lambda] |
| [[AWS Lambda and API Gateway]] | Compatibility navigation; links checked | [[Audit Amazon Services 2026-09-27]] and Lambda row |
| [[AWS License Manager]] | Host resource groups automate placement/host lifecycle, with configurable license requirements; retained | [Host groups][license] |
| [[AWS Network Firewall]] | Stateful inspection and traffic steering; retained for standard routed design | [Overview][networkfirewall] |
| [[AWS Organizations]] | SCPs limit rather than grant, with management-account exceptions; retained | [SCPs][orgs] |
| [[AWS Organizations and Control Tower]] | Compatibility navigation; links checked | Canonical rows in this table |
| [[AWS Private CA]] | Private CA hierarchy and regional scope; retained | [Overview][pca] |
| [[AWS RAM]] | Shares supported existing resources, not copies; retained | [Overview][ram] |
| [[AWS SAM]] | CloudFormation extension and CLI; retained | [Overview][sam] |
| [[AWS Secrets Manager]] | Managed/external-secret rotation need not use customer Lambda; clarified | [Rotation methods][secrets] |
| [[AWS Security Hub]] | Security Hub versus CSPM posture distinction; retained | [Service distinction][securityhub] |
| [[AWS Security Token Service]] | Temporary federated/cross-account credentials; retained | [Temporary credentials][sts] |
| [[AWS Service Catalog]] | Approved self-service products/portfolios/constraints; retained | [Overview][catalog] |
| [[AWS Service Catalog and RAM]] | Provisioning versus sharing navigation; links checked | Canonical rows in this table |
| [[AWS Shield]] | New HTTP flood default versus legacy L7 automatic mitigation; caveat added | [Current transition][shield] |
| [[AWS Step Functions]] | Standard/Express duration, guarantees and retry distinction; retained | [Workflow types][sfn] |
| [[AWS Step Functions and EventBridge]] | Workflow versus routing navigation; links checked | Step Functions row and [[Audit Amazon Services 2026-09-27]] |
| [[AWS Storage and Stateless Application Patterns]] | Compatibility navigation; links checked | [[Audit Amazon Services 2026-09-27]] |
| [[AWS Storage Gateway]] | RefreshCache updates inventory asynchronously, not file preloading; retained | [API contract][gateway] |
| [[AWS Systems Manager]] | Managed nodes require Agent/connectivity; retained | [Overview][ssm] |
| [[AWS Systems Manager Parameter Store]] | Secrets reference prefix and GetParameter/GetParameters-only retrieval; retained | [Integration restrictions][ps] |

## Comparison page coverage

“Retained” means the selected distinction is consistent with the cited current evidence; it is not an exhaustive certification of every platform combination.

| Page | Selected distinction/result | Evidence |
|---|---|---|
| [[AppConfig vs Parameter Store vs Secrets Manager]] | Config rollout, parameter lookup and credential rotation remain distinct | [AppConfig][appconfig], [rotation][secrets], [parameters][ps] |
| [[AWS Health vs CloudWatch vs Trusted Advisor]] | AWS-impact event versus workload alarm/recommendation; retained | [Health][health], [alarms][alarms]; Trusted Advisor scope in [[Audit Amazon Services 2026-09-27]] |
| [[CodeArtifact vs ECR vs S3 vs Image Builder]] | Creation versus package/container/object storage; retained | [CodeArtifact][artifact]; other services in [[Audit Amazon Services 2026-09-27]] |
| [[CodePipeline vs CodeBuild vs CodeDeploy]] | Roles retained, V2 Commands exception clarified | [Commands][commands], [reports][build], [deployment][deploy] |
| [[Config Compliance vs CloudTrail Actor Attribution]] | Configuration versus API actor evidence; retained | [Config][config], [[AWS CloudTrail]] |
| [[Config vs CloudTrail vs Systems Manager]] | Evaluation, audit and operation differ; retained | [Config][config], [Systems Manager][ssm] |
| [[Cooldown vs Warmup vs Lifecycle Hooks vs Health Check Grace Period]] | Simple cooldown does not stop target/step scale-out; retained | [Cooldowns][cooldown] |
| [[Cross-Account Observability vs Log Centralization]] | Federated views versus copied new logs; retained | [Centralization][centralization] |
| [[DAX vs ElastiCache vs DynamoDB Global Tables]] | Cache versus persistent multi-Region data; retained | Current canonical-service checks in [[Audit Amazon Services 2026-09-27]] |
| [[Detection vs Enforcement vs Remediation]] | Policy enforcement differs from detection and authorized repair; retained | [IAM evaluation][iam], [Config][config] |
| [[DynamoDB Global Tables vs Aurora Global Database]] | MREC/MRSC versus one Aurora primary; retained | Current database checks in [[Audit Amazon Services 2026-09-27]] |
| [[ECS Native vs CodeDeploy Deployments]] | Controller/service revision versus CodeDeploy/task set; retained | Current ECS checks in [[Audit Amazon Services 2026-09-27]] |
| [[Fleet Manager vs OpsCenter vs Automation vs State Manager]] | Node tools, cases, runbooks and desired state differ; retained | [Systems Manager][ssm]; incident operations check in [[Audit Concepts and Domains 2026-09-27]] |
| [[GuardDuty vs Inspector vs Security Hub vs Detective]] | Detector/posture/prioritization/investigation roles; retained | [Security Hub/CSPM][securityhub]; canonical checks in [[Audit Amazon Services 2026-09-27]] |
| [[Inspector vs GuardDuty vs Macie vs Access Analyzer]] | Vulnerability/threat/classification/access scopes; retained | Canonical checks in [[Audit Amazon Services 2026-09-27]] |
| [[Kinesis Data Streams vs Firehose vs EventBridge]] | Retained stream versus buffered delivery versus event routing; retained | Canonical checks in [[Audit Amazon Services 2026-09-27]] |
| [[KMS vs CloudHSM vs ACM vs Secrets Manager]] | Data keys, HSM validation, certificates and secrets; retained | [KMS][kms], [HSM][hsm], [ACM][acm], [rotation][secrets] |
| [[Lambda vs ECS vs EC2 CodeDeploy Hooks]] | Hook names and execution/callback differ by platform; retained | [Hooks][hooks] |
| [[Log Subscription vs Metric Filter vs EventBridge Rule]] | Added native log alarm option; one-off query remains different | [Alarm types][alarms] |
| [[Logs Insights vs Athena vs OpenSearch]] | Search choice follows data location/ingestion; retained | Canonical checks in [[Audit Amazon Services 2026-09-27]] |
| [[Multi-AZ vs Multi-Region]] | AZ protection does not by itself provide regional recovery; retained | Resilience checks in [[Audit Concepts and Domains 2026-09-27]] |
| [[Organizations vs Control Tower vs Service Catalog vs RAM vs StackSets]] | Account governance, vending, self-service, sharing and stack deployment; retained | [Organizations][orgs], [Control Tower][tower], [Catalog][catalog], [RAM][ram], [StackSets][stacksets] |
| [[RDS Blue Green vs EngineVersion Update vs Read Replica Promotion]] | Synchronized staging/switchover differs from replica promotion; retained | [Blue/Green][bluegreen]; RDS checks in [[Audit Amazon Services 2026-09-27]] |
| [[RDS Multi-AZ vs Read Replicas vs Aurora Global Database]] | Regional HA versus regional DR/write topology; retained | RDS/Aurora checks in [[Audit Amazon Services 2026-09-27]] |
| [[Route 53 vs Global Accelerator vs CloudFront]] | DNS versus static IP endpoints versus edge cache; retained | [Global Accelerator][ga]; DNS/CDN checks in [[Audit Amazon Services 2026-09-27]] |
| [[Run Command vs Session Manager vs State Manager vs Automation]] | Managed-node commands versus sessions/state/runbooks; retained | [Systems Manager][ssm]; concepts checks in [[Audit Concepts and Domains 2026-09-27]] |
| [[SCP vs Permissions Boundary vs Session Policy vs Resource Policy]] | Implicit-deny exceptions depend on principal/grant; retained | [IAM evaluation][iam], [SCPs][orgs] |
| [[Security Groups vs Network ACLs]] | Stateful allow rules versus ordered stateless allow/deny; retained | [Security groups][sg], [ACLs][nacl] |
| [[Shield vs WAF vs CloudFront vs Auto Scaling]] | Added current HTTP flood default; capacity is not filtering | [Transition][shield] |
| [[Static vs Anomaly vs Composite Alarms]] | Fixed/learned thresholds versus alarm-state expressions; retained | [Alarm types][alarms]; alarm checks in [[Audit Concepts and Domains 2026-09-27]] |

## Evidence limits

This report covers **84 pages**. Counts are reconciled against the machine inventory in the main report. Overview sources validate the selected service role, not all integrations, policies or limits. No account-specific quotas, all-Region feature matrix, runtime compatibility matrix, or deployment test was performed. Existing historical frontmatter dates remain historical. Current source checks and HTTP checks are different kinds of evidence.

[appconfig]: https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html
[aas]: https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html
[ads]: https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html
[auditmanager]: https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html
[backup]: https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery-copying.html
[cdk]: https://docs.aws.amazon.com/cdk/v2/guide/home.html
[acm]: https://docs.aws.amazon.com/acm/latest/userguide/export-public-certificate.html
[cfn]: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html
[stacksets]: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html
[hsm]: https://docs.aws.amazon.com/cloudhsm/latest/userguide/fips-validation.html
[lake]: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html
[artifact]: https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html
[build]: https://docs.aws.amazon.com/codebuild/latest/userguide/test-reporting.html
[commit]: https://docs.aws.amazon.com/codecommit/latest/userguide/history.html
[connections]: https://docs.aws.amazon.com/dtconsole/latest/userguide/connections.html
[hooks]: https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html
[deploy]: https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html
[pipeline]: https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-types-planning.html
[commands]: https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-Commands.html
[config]: https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html
[tower]: https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html
[beanstalk]: https://aws.amazon.com/about-aws/whats-new/2026/09/elastic-beanstalk-cluster-mode/
[drs]: https://docs.aws.amazon.com/drs/latest/userguide/CloudEndure-Concepts.html
[fargate]: https://aws.amazon.com/fargate/pricing/
[fms]: https://docs.aws.amazon.com/waf/latest/developerguide/fms-prereq.html
[ga]: https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints.html
[glue]: https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/aws-glue-data-catalog.html
[health]: https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html
[identitycenter]: https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html
[rolesanywhere]: https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html
[iam]: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic_policy-eval-denyallow.html
[kms]: https://docs.aws.amazon.com/kms/latest/developerguide/data-keys.html
[lambda]: https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html
[license]: https://docs.aws.amazon.com/license-manager/latest/userguide/host-resource-groups.html
[networkfirewall]: https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html
[orgs]: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html
[pca]: https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html
[ram]: https://docs.aws.amazon.com/ram/latest/userguide/what-is.html
[sam]: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html
[secrets]: https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html
[securityhub]: https://docs.aws.amazon.com/securityhub/latest/userguide/what-are-securityhub-services.html
[sts]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html
[catalog]: https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html
[shield]: https://docs.aws.amazon.com/waf/latest/developerguide/ddos-automatic-app-layer-response.html
[sfn]: https://docs.aws.amazon.com/step-functions/latest/dg/choosing-workflow-type.html
[gateway]: https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_RefreshCache.html
[ssm]: https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html
[ps]: https://docs.aws.amazon.com/systems-manager/latest/userguide/integration-ps-secretsmanager.html
[cooldown]: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-cooldowns.html
[centralization]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html
[alarms]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html
[bluegreen]: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-overview.html
[sg]: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html
[nacl]: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html
