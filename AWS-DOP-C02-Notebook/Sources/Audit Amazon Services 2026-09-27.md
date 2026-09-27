---
title: Audit Amazon Services 2026-09-27
tags: [aws, dop-c02, verification, sources]
audit_date: 2026-09-27
read: false
---

# Amazon and related service-page audit

Read all 45 assigned Markdown pages. This is a material-claim and stale-reference review, with live first-party AWS references for the checks below. “Checked” does not certify every sentence, region, quota, or linked resource. Existing read flags and historical verification dates were preserved.

## Corrections

- [[Amazon CloudWatch]]: broadened metric-only alarm wording to include current direct log-query and PromQL alarm types, supported by [AWS alarm documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html).
- [[AWS WAF]]: added the March 26, 2026 Anti-DDoS Managed Rule Group transition and legacy Shield access distinction, confirmed in the [dedicated AWS notice](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-automatic-app-layer-response.html).
- [[Amazon QuickSight]]: current documentation uses Amazon Quick, with Amazon Quick Sight as its BI feature; retained filename and exam terminology.
- [[Amazon CloudFront]]: OPTIONS origin failover also requires OPTIONS among cached HTTP methods.
- [[Amazon S3]]: clarified that general purpose buckets start unversioned; added eligible UpdateObjectEncryption behavior and Object Lock/replication boundaries.
- [[Amazon ECR and EC2 Image Builder]]: fixed the ECR subsection's wrong navigation target.

## Page coverage

Task numbers identify the relevant exam study area for the checked claim, not a reclassification of every section.

| Page | Tasks | Material claim checked / result | First-party evidence |
|---|---|---|---|
| [[Amazon API Gateway]] | 1.4, 3.2, 4.2 | REST/HTTP feature and tracing differences | [AWS documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html) |
| [[Amazon Application Recovery Controller]] | 3.1, 3.3 | Readiness closed to new customers; other ARC features supported | [AWS documentation](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html) |
| [[Amazon Athena]] | 4.1–4.2 | Serverless SQL over S3; analytics role | [AWS documentation](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) |
| [[Amazon Aurora Global Database]] | 3.1, 3.3 | Single writer; 10 secondary Regions; switchover/failover | [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html) |
| [[Amazon CloudFront]] | 1.4, 3.1–3.2 | Corrected OPTIONS cached-method prerequisite; failover request scope | [AWS documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html) |
| [[Amazon CloudFront and Lambda@Edge]] | 1.4 | Navigation reviewed; canonical pages checked | [AWS documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html) |
| [[Amazon CloudWatch]] | 4.1–4.3 | 3-hour/15-day/63-day/455-day metric retention | [AWS documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html) |
| [[Amazon CloudWatch, X-Ray, and OpenTelemetry]] | 4.2 | Navigation reviewed; SDK maintenance distinct from backend | [AWS documentation](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-daemon-timeline.html) |
| [[Amazon Cognito]] | 6.1 | User pool tokens versus identity pool credentials | [AWS documentation](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) |
| [[Amazon Data Firehose]] | 4.1–4.3 | CloudWatch gzip input and OpenSearch destination limitation | [AWS documentation](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-cloudwatch-logs.html) |
| [[Amazon Detective]] | 5.3, 6.3 | Investigation and behavior graphs | [AWS documentation](https://docs.aws.amazon.com/detective/latest/userguide/what-is-detective.html) |
| [[Amazon DynamoDB]] | 3.1–3.2 | MREC/MRSC consistency and per-item stream ordering | [AWS documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html) |
| [[Amazon DynamoDB Accelerator (DAX)]] | 3.1–3.2 | Eventual caching; strong reads pass through; cache distinctions | [AWS documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.consistency.html) |
| [[Amazon EBS]] | 3.1 | Block storage and AZ-scoped volumes | [AWS documentation](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) |
| [[Amazon EC2 Auto Scaling]] | 3.1–3.3 | WarmPool/AutoScalingGroup lifecycle event field casing | [AWS documentation](https://docs.aws.amazon.com/autoscaling/ec2/userguide/warm-pools-eventbridge-events.html) |
| [[Amazon ECR]] | 1.3–1.4, 3.2 | Replication applies to newly pushed/restored content; no automatic backfill | [AWS documentation](https://docs.aws.amazon.com/AmazonECR/latest/userguide/replication.html) |
| [[Amazon ECR and EC2 Image Builder]] | 1.3 | Corrected ECR section link to ECR instead of Image Builder | [AWS documentation](https://docs.aws.amazon.com/AmazonECR/latest/userguide/replication.html) |
| [[Amazon ECS]] | 1.4, 4.1 | Rolling rollback; native blue/green; non-blocking log default | [AWS documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html) |
| [[Amazon ECS Deployments]] | 1.4 | Navigation reviewed; native blue/green exists | [AWS documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-blue-green.html) |
| [[Amazon EFS]] | 3.1 | Shared filesystem, Regional/One Zone distinctions | [AWS documentation](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) |
| [[Amazon EKS]] | 3.2, 4.3 | HPA scales pods using configured metrics | [AWS documentation](https://docs.aws.amazon.com/eks/latest/userguide/horizontal-pod-autoscaler.html) |
| [[Amazon ElastiCache]] | 3.1 | Managed cache; engine/deployment distinctions | [AWS documentation](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html) |
| [[Amazon EventBridge]] | 2.3, 5.1–5.2 | Supported targets and delivery/authorization boundaries | [AWS documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html) |
| [[Amazon GuardDuty]] | 4.2, 6.3 | Native S3 finding export and permissions | [AWS documentation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_exportfindings.html) |
| [[Amazon GuardDuty and Inspector]] | 6.3 | Navigation reviewed; legacy/current Inspector distinction | [AWS documentation](https://docs.aws.amazon.com/pdfs/inspector/v1/userguide/inspector-ug.pdf) |
| [[Amazon Inspector]] | 4.2, 6.3 | Classic retirement May 20, 2026; modern service distinction; migration/overview/PDF URLs return 404; indexed PDF evidence retained with availability caveat | [AWS documentation](https://docs.aws.amazon.com/pdfs/inspector/v1/userguide/inspector-ug.pdf) |
| [[Amazon Kinesis Data Streams]] | 4.1–4.3 | Cross-account log destinations; source/destination Region relationship | [AWS documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CrossAccountSubscriptions.html) |
| [[Amazon Macie]] | 4.2, 6.2 | S3 sensitive-data discovery role | [AWS documentation](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) |
| [[Amazon OpenSearch Service]] | 4.1–4.3 | Managed indexed analytics; Firehose caveat separately confirmed | [AWS documentation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) |
| [[Amazon QuickSight]] | 4.2 | Corrected current naming to Amazon Quick / Amazon Quick Sight | [AWS documentation](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html) |
| [[Amazon RDS]] | 3.1, 3.3 | Engine-specific cluster upgrade behavior; notification delay/order | [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-upgrading.html) |
| [[Amazon Route 53]] | 3.1–3.3 | Complex health trees and unhealthy-record fail-open behavior | [AWS documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html) |
| [[Amazon Route 53 Resolver DNS Firewall]] | 6.2 | DNS filtering boundary | [AWS documentation](https://docs.aws.amazon.com/vpc/latest/userguide/resolver-dns-firewall.html) |
| [[Amazon S3]] | 3.1, 6.2 | Corrected default versioning; added eligible in-place encryption update | [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/update-sse-encryption.html) |
| [[Amazon SNS]] | 3.1, 3.3 | RDS notification transport; up to five-minute delay and unordered delivery | [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.overview.html) |
| [[Amazon SQS]] | 4.2–4.3 | Visibility timeout, deletion and duplicate-processing boundary | [AWS documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) |
| [[AWS Transit Gateway]] | 3.2 | Static routes for peering attachment | [AWS documentation](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering-add-route.html) |
| [[AWS Trusted Advisor]] | 4.3, 5.1 | Check-item refresh events and best-effort delivery | [AWS documentation](https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-trustedadvisor.html) |
| [[AWS WAF]] | 5.1–5.2 | Supported web-resource filtering boundary | [AWS documentation](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) |
| [[AWS X-Ray]] | 4.2 | SDK/daemon maintenance February 25, 2026; OpenTelemetry direction | [AWS documentation](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-daemon-timeline.html) |
| [[CloudFront Field-Level Encryption]] | 6.2 | Selected POST fields, maximum 10, chunked origin encoding | [AWS documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html) |
| [[EC2 Image Builder]] | 1.3, 2.1 | AMI/container build/test/distribution role | [AWS documentation](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) |
| [[Elastic Load Balancing]] | 3.1–3.2, 4.1 | NLB thresholds; enhanced ALB logging confirmed separately | [AWS documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html) |
| [[IAM Access Analyzer]] | 6.1, 6.3 | External/internal/unused analysis scope | [AWS documentation](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/Welcome.html) |
| [[Lambda@Edge]] | 1.4 | us-east-1 and numbered-version restrictions | [AWS documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-edge-function-restrictions.html) |

## Additional evidence

- [ECS rolling deployment failure detection](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html): circuit breaker and alarm rollback are configuration-dependent.
- [ALB access logging](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html): the notebook already distinguishes legacy S3 delivery from enhanced CloudWatch Logs delivery.
- [RDS notification contract](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.overview.html): five-minute possible delay and no ordering guarantee remain documented.
- [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html): disabled by default.
- [Unsupported DevOps Monitoring Dashboard solution](https://docs.aws.amazon.com/solutions/latest/devops-monitoring-dashboard-on-aws/solution-overview.html): existing warning remains correct.
- [Firehose CloudWatch input](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-cloudwatch-logs.html): the explicit OpenSearch limitation remains in current AWS documentation.
- [CloudFront origin failover](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html): origin Lambda can run again during failover.

## Limits and follow-up triggers

All pages were read; live checks concentrated on explicit lifecycle dates, newer naming, defaults, numeric limits, integration boundaries and consequential scenario distinctions. This is not a sentence-by-sentence proof or runtime deployment test. Broad overview pages support service scope; they do not prove all security configurations or regional combinations. No AWS account was accessed.

The ARC closure page did not itself display the notebook's April 30, 2026 date. Integration follow-up confirmed that date in [ARC document history](https://docs.aws.amazon.com/r53recovery/latest/dg/doc-history.html). Exact engine/version/Region matrices, IAM policies, quota adjustments, and price/support-plan entitlements still need scenario-specific revalidation. The separate HTTP reference pass is recorded in [[Verification and Stale Reference Audit 2026-09-27]]; HTTP success alone does not validate a claim.

Some current AWS target lists still include Inspector assessment templates even though the dedicated Inspector Classic retirement notice says the service ended support. Use the dedicated lifecycle notice when choosing a current deployment, and retain legacy terminology only to interpret exam/course wording.

Skills used as checklists: aws-containers and aws-observability. Skill text was not treated as evidence overriding AWS documentation.
