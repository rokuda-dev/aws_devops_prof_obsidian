---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# Domain 3 Official Sources

## Six resources supplied by the user

1. [What is Amazon RDS?](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
2. [Using AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/aws-config-landing-page.html)
3. [Replicating Amazon Aurora across Regions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.CrossRegion.html)
4. [Amazon DynamoDB global tables](https://aws.amazon.com/dynamodb/global-tables/)
5. [Configuring DNS failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring.html)
6. [API Gateway canary release deployment](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.html)

## Targeted verification references

| Topic | Official AWS reference |
|---|---|
| Exam tasks 3.1–3.3 | [Domain 3 guide](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain3.html) |
| MySQL major upgrade and replica ordering | [Upgrade strategies](https://aws.amazon.com/blogs/database/upgrade-strategies-for-amazon-rds-for-mysql-8-0-to-8-4/) |
| Different Multi-AZ cluster upgrade behavior | [Cluster upgrade guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-upgrading.html) |
| Supported RDS Blue/Green topology | [Blue/Green overview](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-overview.html) |
| RDS event latency/order | [Event notifications](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.overview.html) |
| ALB cross-zone overrides | [Target-group attributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-target-group-attributes.html#modify-cross-zone) |
| NLB health thresholds and DNS | [Target groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html) |
| Weighted ALB rollback behavior | [AWS weighted-group guidance](https://repost.aws/knowledge-center/elb-make-weighted-target-groups-for-alb) |
| Cross-zone costs are LB-specific | [NLB data transfer](https://aws.amazon.com/blogs/networking-and-content-delivery/exploring-data-transfer-costs-for-aws-network-load-balancers/) |
| ASG cooldown/warmup distinction | [Cooldown guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-cooldowns.html) |
| Scheduled scaling and DST | [Scheduled scaling guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html) |
| Warm-pool event fields | [Warm-pool events](https://docs.aws.amazon.com/autoscaling/ec2/userguide/warm-pools-eventbridge-events.html) |
| ASG application-health replacement | [Health-check guidance](https://docs.aws.amazon.com/help-panel/autoscaling/ec2/help-panel/health-checks.subtopic.html) |
| Provisioned DynamoDB scaling | [Auto Scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html) |
| DAX read consistency | [DAX consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.consistency.html) |
| Pod scaling | [EKS HPA](https://docs.aws.amazon.com/eks/latest/userguide/horizontal-pod-autoscaler.html) |
| Node scaling in Auto Mode | [EKS Auto Mode architecture](https://aws.amazon.com/blogs/containers/faster-nodes-smarter-scaling-whats-new-inside-amazon-elastic-kubernetes-service-amazon-eks-auto-mode/) |
| Fargate allocated capacity costs | [EKS Fargate cost explanation](https://aws.amazon.com/blogs/containers/saving-money-pod-at-time-with-eks-fargate-and-aws-compute-savings-plans/) |
| Regional API endpoints | [Endpoint types](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-endpoint-types.html) |
| SAM build-container distinction | [SAM build example](https://aws.amazon.com/blogs/dotnet/building-serverless-net-applications-with-aws-lambda-and-the-sam-cli/) |
| Global Accelerator endpoint support | [FAQ](https://aws.amazon.com/global-accelerator/faqs/) |
| DNS health routing tree | [Complex failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html) |
| Private health-check approach | [Private-resource probing](https://aws.amazon.com/blogs/networking-and-content-delivery/performing-route-53-health-checks-on-private-resources-in-a-vpc-with-aws-lambda-and-amazon-cloudwatch/) |
| Current ARC capabilities | [ARC overview](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html) |
| Region switch RDS promotion | [Promotion block](https://docs.aws.amazon.com/r53recovery/latest/dg/rds-promote-read-replica-block.html) |
| Server replication/recovery | [Elastic Disaster Recovery concepts](https://docs.aws.amazon.com/drs/latest/userguide/CloudEndure-Concepts.html) |
| Continuous-copy limitation | [AWS Backup continuous copies](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery-copying.html) |
| Backup encryption differences | [Backup encryption](https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html) |
| Backup restore validation | [Restore testing](https://aws.amazon.com/blogs/storage/implementing-restore-testing-for-recovery-validation-using-aws-backup/) |
| Existing S3 objects | [Batch Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-batch-replication-batch.html) |
| S3 RTC objective | [Replication configuration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-add-config.html) |
| ECR replication scope | [ECR replication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/replication.html) |
| Transit gateway routes | [Peering routes](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering-add-route.html) |
| Supplementary resilience assessment | [Resilience Hub concepts](https://docs.aws.amazon.com/resilience-hub/latest/userguide/concepts-terms.html) |
| Supplementary fault testing | [Resilience testing](https://docs.aws.amazon.com/resilience-hub/latest/userguide/arh-testing.html) |

## Evidence interpretation

Verified 2026-09-18 using official AWS sources, including targeted documentation-search chunks. Older AWS blogs supply stable architecture explanations, not authority for current runtime lists, prices, or quotas. No guarantee is inferred from typical product recovery timings.

See [[Domain 3 Transcript Corrections]], [[Domain 3 Transcript Coverage]], [[Verification Ledger]].
