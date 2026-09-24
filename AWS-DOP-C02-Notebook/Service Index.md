---
tags: [aws, dop-c02, moc]
updated: 2026-09-20
read: false
---

# Service Index

Every file in `Services/` appears exactly once below. Canonical notes hold study content; compatibility navigation pages preserve earlier grouped filenames and route to those canonical notes.

## Canonical service notes

| Service | Role / study scope | Task mapping |
|---|---|---|
| [[Amazon API Gateway]] | Publish, secure, throttle, and observe REST, HTTP, and WebSocket APIs. | 1.4; cross-domain observation/security |
| [[Amazon Application Recovery Controller]] | Zonal, routing-control and Region switch capabilities | 3.1, 3.3 |
| [[Amazon Athena]] | SQL archive-log analysis | 4.1–4.2 |
| [[Amazon Aurora Global Database]] | Cross-Region Aurora with one primary Region, secondary clusters, and planned or unplanned recovery. | 3.1; 3.3 |
| [[Amazon CloudFront]] | Global content delivery with edge caching, origin failover, and request controls. | 1.4; cross-domain resilience/security |
| [[Amazon CloudWatch]] | Observe workloads through metrics, logs, alarms, dashboards, and related telemetry features. | 1.2, 1.4; cross-domain 4–5 |
| [[Amazon Cognito]] | Application-user authentication and temporary AWS access | 6.1 |
| [[Amazon Data Firehose]] | Buffered managed delivery; formerly Kinesis Data Firehose | 4.1–4.3 |
| [[Amazon Detective]] | Investigate security findings and relationships to help determine root cause. | 2.2; cross-domain 5–6 |
| [[Amazon DynamoDB Accelerator (DAX)]] | Eligible DynamoDB read caching | 3.1–3.2 |
| [[Amazon DynamoDB]] | Managed NoSQL tables, Streams, capacity, global tables, backups, and resilience semantics. | 2.3; 3.1–3.3 |
| [[Amazon EBS]] | Block storage attached to EC2, with volume/snapshot lifecycle independent of application deployment. | 1.4; cross-domain 3 |
| [[Amazon EC2 Auto Scaling]] | EC2 capacity, health replacement, warm pools and lifecycle hooks | 3.1–3.3 |
| [[Amazon ECR]] | Managed registry for container images and OCI artifacts. | 1.3, 1.4 |
| [[Amazon ECS]] | Container orchestration with rolling and native or CodeDeploy-controlled traffic-shifting deployments. | 1.4; cross-domain resilience |
| [[Amazon EFS]] | Managed shared NFS/POSIX filesystem for supported Linux workloads. | 1.4; cross-domain 3 |
| [[Amazon EKS]] | Regional Kubernetes clusters; pod versus node scaling | 3.1–3.3 |
| [[Amazon ElastiCache]] | Shared low-latency cache/session storage, with engine and deployment-specific resilience choices. | 1.4; cross-domain 3 |
| [[Amazon EventBridge]] | Route events to targets; Scheduler provides scheduled invocations. | 2.3; cross-domain 5 |
| [[Amazon GuardDuty]] | Managed threat detection for suspicious activity and potential compromise. | 2.2; cross-domain 5–6 |
| [[Amazon Inspector]] | Vulnerability management for supported workloads such as EC2, ECR images, and Lambda. | 2.2; cross-domain 6 |
| [[Amazon Kinesis Data Streams]] | Retained log stream and custom consumers | 4.1–4.3 |
| [[Amazon Macie]] | S3 sensitive-data/policy-risk analysis | 4.2 |
| [[Amazon OpenSearch Service]] | Indexed search/analytics | 4.1–4.3 |
| [[Amazon QuickSight]] | Prepared dataset BI; current Quick Suite context | 4.2 |
| [[Amazon RDS]] | HA topology, upgrades, replicas and promotion | 3.1, 3.3 |
| [[Amazon Route 53 Resolver DNS Firewall]] | DNS query filtering for VPC Resolver traffic | 6.2 |
| [[Amazon Route 53]] | DNS routing, health and cached failover behavior | 3.1–3.3 |
| [[Amazon S3]] | Durable object storage for pipeline artifacts, application objects, and logs. | 1.3, 1.4, 3.1, 3.3, 4.1, 5.1, 6.2 |
| [[Amazon SNS]] | Recovery notification path, not recovery orchestration itself | 3.1, 3.3 |
| [[Amazon SQS]] | Queue processing/monitoring; worker-health correction | 4.2–4.3 |
| [[AWS AppConfig]] | Validate and safely deploy application runtime configuration and feature flags. | 1.1, 2.1 |
| [[AWS Application Auto Scaling]] | Supported service capacity, ECS tasks and DynamoDB provisioned throughput | 3.2 |
| [[AWS Application Discovery Service]] | On-premises server and database discovery for migration assessment; closed to new customers. | 2.1; migration context |
| [[AWS Audit Manager]] | Assessment evidence with current availability caveat | 6.3 |
| [[AWS Backup]] | Policies/copies, recovery points and restore testing | 3.3 |
| [[AWS CDK]] | Define infrastructure using programming languages and synthesize CloudFormation templates. | 2.1 |
| [[AWS Certificate Manager]] | Managed public/imported TLS certificate lifecycle | 6.2 |
| [[AWS CloudFormation StackSets]] | Deploy a common stack definition across multiple accounts and Regions. | 2.1, 2.2 |
| [[AWS CloudFormation]] | Declarative provisioning and lifecycle management of AWS infrastructure. | 1.4, 2.1 |
| [[AWS CloudHSM]] | Customer-controlled HSM clusters and crypto users | 6.2 |
| [[AWS CloudTrail]] | Audit AWS API activity and identify actors, actions, and resource access. | 2.2; cross-domain 4–6 |
| [[AWS CodeArtifact]] | Managed package repositories, upstreams, domains, and package-version governance. | 1.3 |
| [[AWS CodeBuild]] | Managed build, test, scan, report, and artifact-production execution. | 1.2–1.3; 5.3 |
| [[AWS CodeCommit]] | Managed Git repositories with IAM-integrated authorization. | 1.1 |
| [[AWS CodeConnections]] | Managed authorization between AWS developer tools and supported external Git providers. | 1.1 |
| [[AWS CodeDeploy]] | Platform-specific EC2/on-premises, ECS, and Lambda deployments, hooks, traffic shifting, and rollback. | 1.4; 5.2–5.3 |
| [[AWS CodePipeline]] | Stage/action orchestration for release workflows, approvals, and cross-account or cross-Region delivery. | 1.1–1.4; 5.3 |
| [[AWS Config]] | Resource configuration history, compliance evaluation, aggregation, and remediation integration. | 2.2; 4.2–4.3; 5.1; 6.3 |
| [[AWS Control Tower]] | Set up and govern a multi-account landing zone and standardized account provisioning. | 2.2 |
| [[AWS Elastic Beanstalk]] | Managed application environments, deployment policies, health, and current Standard/Cluster distinctions. | 1.4; 3.1–3.2 |
| [[AWS Elastic Disaster Recovery]] | Supported server replication and recovery | 3.3 |
| [[AWS Fargate]] | Serverless container compute and capacity/billing boundaries | 3.2 |
| [[AWS Firewall Manager]] | Organization-wide supported security policies | 6.2 |
| [[AWS Global Accelerator]] | Stable anycast IPs and supported regional endpoints | 3.1–3.3 |
| [[AWS Glue]] | Catalog metadata for discovery/classification workflows | 6.2 |
| [[AWS Health]] | Service/resource-impact events and notification | 4.2–4.3 |
| [[AWS IAM Identity Center]] | Workforce access and permission sets | 6.1 |
| [[AWS IAM Roles Anywhere]] | Certificate-based temporary access for external workloads | 6.1 |
| [[AWS Identity and Access Management]] | Authorization, response-role scope and compromised credentials | 5.1–5.3 |
| [[AWS Key Management Service]] | Managed key control and cryptographic operations | 6.2 |
| [[AWS Lambda]] | Managed event-driven function execution; published versions and aliases enable controlled releases. | 1.4, 2.3; cross-domain response |
| [[AWS License Manager]] | Relevant extension for Dedicated Host license controls | 5.3 |
| [[AWS Network Firewall]] | Routed VPC traffic inspection | 6.2 |
| [[AWS Organizations]] | Manage AWS accounts, OUs, and organization-wide governance boundaries. | 2.2; cross-domain 6 |
| [[AWS Private CA]] | Private PKI and certificate issuance | 6.2 |
| [[AWS RAM]] | Share supported existing AWS resources across accounts and organizational boundaries. | 2.2 |
| [[AWS SAM]] | Serverless-focused Infrastructure as Code built on CloudFormation. | 1.4, 2.1 |
| [[AWS Secrets Manager]] | Store and manage secrets, including supported managed rotation workflows. | 1.1, 2.1; cross-domain 6 |
| [[AWS Security Hub]] | Centralize security findings and posture workflows across supported services/accounts/Regions. | 2.2; cross-domain 6 |
| [[AWS Security Token Service]] | Temporary role and federated credentials | 6.1 |
| [[AWS Service Catalog]] | Governed self-service provisioning of approved infrastructure products. | 2.1, 2.2 |
| [[AWS Shield]] | DDoS protection and configured Advanced response | 5.2 |
| [[AWS Step Functions]] | Stateful orchestration of multi-step workflows with branching, retries, waits, and service integrations. | 2.3; cross-domain 5 |
| [[AWS Storage Gateway]] | S3 File Gateway RefreshCache distinction | Additional resource |
| [[AWS Systems Manager Parameter Store]] | Hierarchical storage for parameters and KMS-encrypted SecureString values. | 1.1, 2.1 |
| [[AWS Systems Manager]] | Managed-node operations, desired state, patching, secure access, Automation, and incident workflows. | 2.1–2.3; 4.3; 5.1–5.3; 6.3 |
| [[AWS Transit Gateway]] | Regional hubs and inter-Region private peering | 3.2 |
| [[AWS Trusted Advisor]] | Refreshed recommendations/checks | 4.3 |
| [[AWS WAF]] | Web-layer inspection/rate-based response | 5.2 |
| [[AWS X-Ray]] | Distributed tracing backend for request paths, dependencies, latency, and failures. | 1.2; cross-domain 4 |
| [[EC2 Image Builder]] | Automate creation, testing, and distribution of AMIs and container images. | 1.3, 2.1 |
| [[Elastic Load Balancing]] | ALB/NLB/GWLB, cross-zone and target-group health | 3.1–3.2 |
| [[IAM Access Analyzer]] | Access analysis and IAM policy validation | 6.1, 6.3 |
| [[Lambda@Edge]] | Run Lambda logic at CloudFront viewer/origin request and response events. | 1.4 |

## Compatibility navigation pages

| Navigation page | Canonical destinations |
|---|---|
| [[AWS AppConfig, Parameter Store, and Secrets Manager]] | [[AWS AppConfig]], [[AWS Systems Manager Parameter Store]], [[AWS Secrets Manager]] |
| [[AWS CloudFormation, CDK, and SAM]] | [[AWS CloudFormation]], [[AWS CDK]], [[AWS SAM]] |
| [[AWS CodeCommit and CodeConnections]] | [[AWS CodeCommit]], [[AWS CodeConnections]] |
| [[AWS Lambda and API Gateway]] | [[AWS Lambda]], [[Amazon API Gateway]] |
| [[AWS Organizations and Control Tower]] | [[AWS Organizations]], [[AWS Control Tower]] |
| [[AWS Service Catalog and RAM]] | [[AWS Service Catalog]], [[AWS RAM]] |
| [[AWS Step Functions and EventBridge]] | [[AWS Step Functions]], [[Amazon EventBridge]] |
| [[AWS Storage and Stateless Application Patterns]] | [[Amazon S3]], [[Amazon EBS]], [[Amazon EFS]], [[Amazon ElastiCache]] |
| [[Amazon CloudFront and Lambda@Edge]] | [[Amazon CloudFront]], [[Lambda@Edge]] |
| [[Amazon CloudWatch, X-Ray, and OpenTelemetry]] | [[Amazon CloudWatch]], [[AWS X-Ray]], [[AWS Distro for OpenTelemetry]] |
| [[Amazon ECR and EC2 Image Builder]] | [[Amazon ECR]], [[EC2 Image Builder]] |
| [[Amazon ECS Deployments]] | [[Amazon ECS]], [[AWS CodeDeploy]], [[ECS Native vs CodeDeploy Deployments]] |
| [[Amazon GuardDuty and Inspector]] | [[Amazon GuardDuty]], [[Amazon Inspector]] |
| [[CloudFront Field-Level Encryption]] | [[Amazon CloudFront]] |

Shared concept: [[AWS Distro for OpenTelemetry]]. Related indexes: [[Service Selection Matrix]], [[Domain Coverage and Service Map]].
