---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# Domain 4 Official Sources

## Seven resources supplied by the user

1. [Using subscription filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SubscriptionFilters.html#LambdaFunctionExample)
2. [What is Amazon GuardDuty?](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
3. [What is AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
4. [AWS Config managed rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html)
5. [Monitoring AWS Health events with EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html)
6. [Monitoring CodeDeploy deployments with CloudWatch Events](https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-cloudwatch-events.html)
7. [What is Amazon OpenSearch Service?](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html)

## Targeted official checks — 2026-09-18

| Topic | AWS reference |
|---|---|
| Tasks 4.1–4.3 and metric-stream extension | [Official Domain 4 guide](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain4.html) |
| Dimension identity/custom aggregation | [Metric concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html) |
| Statistic sets and percentiles | [Publish custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) |
| Exact agent namespace/configuration | [Agent configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html) |
| Guest memory/disk metrics | [Host custom telemetry](https://repost.aws/knowledge-center/cloudwatch-memory-metrics-ec2) |
| Firehose cross-account destination support | [Account-level Firehose subscriptions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CrossAccountSubscriptions-Firehose-Account.html) |
| Kinesis cross-account routing | [Cross-account/cross-Region streaming](https://repost.aws/knowledge-center/streaming-cloudwatch-logs) |
| Native log centralization, encryption and new-data-only scope | [Centralization documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html) |
| Federation versus copies | [Centralization architecture explanation](https://aws.amazon.com/blogs/mt/simplifying-log-management-using-amazon-cloudwatch-logs-centralization/) |
| Forwarding metrics and bounded retries | [Subscription troubleshooting](https://repost.aws/knowledge-center/cloudwatch-failed-log-delivery) |
| Firehose compressed input/OpenSearch limitation | [CloudWatch input restrictions](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-cloudwatch-logs.html) |
| Firehose message extraction | [Feature announcement](https://aws.amazon.com/about-aws/whats-new/2024/02/amazon-data-firehose-message-extraction-cloudwatch-logs/) |
| Kinesis/OpenSearch ingestion | [Supported pipeline pattern](https://aws.amazon.com/blogs/big-data/use-amazon-kinesis-data-streams-to-deliver-real-time-data-to-amazon-opensearch-service-domains-with-amazon-opensearch-ingestion/) |
| Metrics export transport/account/Region | [Metric stream Firehose setup](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-setup-datalake.html) |
| Discovered fields and Standard log class | [Discovered fields](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData-discoverable-fields.html) |
| Default values and metric dimensions | [Metric-filter concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) |
| Insights examples | [Sample queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.html) |
| ECS current default log mode | [Account settings](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html) |
| ECS awslogs options by launch type | [LogConfiguration reference](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/ECS/Types/LogConfiguration.html) |
| ALB legacy delivery and enhanced integration notice | [Access log guide](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html) |
| Legacy ALB SSE-S3 constraint | [ALB construct documentation](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_elasticloadbalancingv2-readme.html) |
| ALB bucket permissions/Region | [Load balancer attributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyLoadBalancerAttributes.html) |
| Default history scope | [Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) |
| Organization and multi-Region scope | [CloudTrail concepts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html) |
| S3 object-level API event routing | [EventBridge/CloudTrail pattern](https://repost.aws/knowledge-center/eventbridge-rule-monitors-s3) |
| S3 data-event audit detail | [CloudTrail S3 audit analysis](https://aws.amazon.com/blogs/storage/amazon-s3-audit-logging-part-2-centralized-logging-and-analysis-of-s3-data-events-in-aws-cloudtrail-for-security-and-compliance/) |
| Digests and regional signatures | [Integrity validation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html) |
| Trail compliance trigger/parameters | [cloudtrail-enabled](https://docs.aws.amazon.com/config/latest/developerguide/cloudtrail-enabled.html) |
| Periodic rule default frequency | [Rule source detail documentation](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_config.CfnConfigRule.SourceDetailProperty.html) |
| GuardDuty native findings export | [S3 export](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_exportfindings.html) |
| Macie scope and organization administration | [Security tooling architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html) |
| Macie discovery output | [Sensitive-data results](https://docs.aws.amazon.com/macie/latest/user/discovery-results-repository-s3.html) |
| Trusted Advisor refresh events | [Event reference](https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-trustedadvisor.html) |
| Trusted Advisor current capability/refresh context | [Support FAQ](https://aws.amazon.com/premiumsupport/faqs/) |
| EC2 maintenance automation | [Health automation](https://docs.aws.amazon.com/health/latest/ug/automating-instance-actions.html) |
| Dedicated Instance versus Dedicated Host recovery | [Simplified recovery requirements](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-configuration-recovery.html) |
| Inventory/Explorer sync distinction | [Resource data sync](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-resourcedatasync.html) |
| REST API tracing | [API Gateway X-Ray](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-xray.html) |
| EventBridge propagation/replay limitation | [Tracing behavior](https://aws.amazon.com/blogs/compute/using-aws-x-ray-tracing-with-amazon-eventbridge/) |
| ServiceLens correlation | [CloudWatch features](https://aws.amazon.com/cloudwatch/features/) |
| Composite alarm behavior | [CompositeAlarm reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-compositealarm.html) |
| Anomaly band configuration | [CloudWatch construct documentation](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_cloudwatch/README.html) |
| Athena S3 log schema/partition pattern | [S3 audit analysis with Athena](https://aws.amazon.com/blogs/storage/amazon-s3-audit-logging-part-1-analyzing-server-access-logs-with-amazon-athena-for-performance-insights/) |
| QuickSight/Quick Suite current naming | [BI transition](https://aws.amazon.com/blogs/business-intelligence/reimagine-business-intelligence-amazon-quicksight-evolves-to-amazon-quick-suite/) |
| Unsupported DevOps dashboard solution | [Support notice](https://docs.aws.amazon.com/solutions/latest/devops-monitoring-dashboard-on-aws/solution-overview.html) |
| Inspector Classic retirement/template distinction | [Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html) |
| Retired OpsWorks Stacks | [Offboarding/end-of-life context](https://aws.amazon.com/blogs/mt/seamlessly-off-board-from-aws-opsworks-stacks-by-detaching-resources/) |

## Evidence boundaries

Targeted documentation chunks/pages and AWS guidance were read for disputed/current behavior. Listed sources are not a claim that every linked document was read in full. Stable summaries are paraphrased; no prices, runtime inventories or unverified recovery guarantees are inferred from old blogs.

Earlier checks carried forward: X-Ray SDK/daemon maintenance versus service support and Domain 3 scaling/health distinctions. Relevant service notes preserve their prior references and dates.

See [[Verification Ledger]], [[Domain 4 Transcript Corrections]], [[Domain 4 Transcript Coverage]].
