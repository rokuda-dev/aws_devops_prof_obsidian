---
tags: [aws, dop-c02, domains]
updated: 2026-09-19
read: false
---

# Domain 3 - Resilient Cloud Solutions

> [!summary]
> Domain 3 is 15% of the exam and tests high availability, scaling, and automated recovery against explicit resilience and business requirements.

## Task 3.1 — Implement highly available solutions to meet resilience and business requirements.

Start with the failure boundary. Multi-AZ designs survive an Availability Zone failure inside one Region; multi-Region designs require independently deployable compute, region-ready dependencies, replicated data, traffic controls, and an explicit recovery mode. Remove instance-local session state and single-AZ dependencies before choosing a traffic-shifting service.

For databases, distinguish availability from read scaling and regional recovery. RDS Multi-AZ provides synchronous regional standby behavior for supported deployments; read replicas are primarily asynchronous scaling/DR copies and require promotion; Aurora Global Database has one primary write Region with secondary clusters. DynamoDB global tables are multi-Region and multi-active, but use a different NoSQL data model.

> [!exam]
> “Survive an AZ failure” suggests Multi-AZ capacity and state. “Continue after a regional outage” requires a multi-Region data and application plan, not merely DNS failover.

Core services: [[Amazon CloudFront]], [[Amazon DynamoDB]], [[Amazon Aurora Global Database]], [[Amazon S3]], [[Elastic Load Balancing]], [[Amazon RDS]], [[Amazon Route 53]], [[AWS Global Accelerator]].

Study: [[Resilience Framework and Dependency Isolation]], [[RTO RPO SLA SLO and Error Budgets]], [[Multi-AZ vs Multi-Region]], [[Amazon DynamoDB Accelerator (DAX)]].

## Task 3.2 — Implement solutions that are scalable to meet business requirements.

Choose the scaling unit and the signal separately. EC2 Auto Scaling changes instance capacity; Application Auto Scaling adjusts supported scalable targets; ECS desired count, Kubernetes pods, and Kubernetes nodes are different layers. Fargate removes host management but does not choose the required number of application replicas.

Prefer horizontal scaling with disposable compute, external state, prebuilt artifacts, and compatible data/schema changes. Use demand-relevant metrics rather than assuming average CPU represents queue depth, request concurrency, or database pressure. Understand cooldown, instance warmup, lifecycle-hook delays, health-check grace periods, minimum/maximum bounds, and failed launch/placement events before changing a policy.

Caching is workload-specific: CloudFront caches edge content, DAX accelerates eligible eventually consistent DynamoDB reads, and ElastiCache provides application-managed in-memory caching. A cache does not replace authoritative storage or remove freshness/failure design.

Core services: [[Amazon EC2 Auto Scaling]], [[AWS Application Auto Scaling]], [[Amazon ECS]], [[Amazon EKS]], [[AWS Fargate]], [[AWS Lambda]], [[Amazon API Gateway]], [[Amazon ElastiCache]].

Study: [[Stateless Applications and External Session State]], [[Scaling Metrics and Troubleshooting]], [[Cooldown vs Warmup vs Lifecycle Hooks vs Health Check Grace Period]], [[Multi-Region Application Checklist]].

## Task 3.3 — Implement automated recovery processes to meet RTO and RPO requirements.

Translate RTO into the complete time budget for detection, decision, infrastructure readiness, data promotion/restoration, dependency recovery, validation, traffic change, DNS/client caching, and reconnection. Translate RPO into maximum acceptable recovered-data age and monitor the actual replication or backup lag that supports it.

Select the data-recovery mechanism first, then orchestrate compute and traffic. Route 53 and Global Accelerator steer traffic but do not promote databases. Backup copies, read replicas, Aurora Global Database, DynamoDB global tables, S3 replication, and Elastic Disaster Recovery provide different recovery points and behaviors. Step Functions, Systems Manager Automation, or ARC Region switch can coordinate supported actions, but workflows need idempotency, bounded retries, approvals, writer fencing, verification, and failback.

> [!warning]
> Configuration drift checks are useful evidence, not proof that restore, failover, application correctness, and failback meet the objectives.

Core services: [[AWS Backup]], [[AWS Elastic Disaster Recovery]], [[Amazon Application Recovery Controller]], [[Amazon Aurora Global Database]], [[AWS Systems Manager]], [[AWS Step Functions]], [[Amazon S3]].

Study: [[Disaster Recovery Strategies]], [[Disaster Recovery Testing and Failback]], [[RDS Multi-AZ vs Read Replicas vs Aurora Global Database]].

## Sources and deeper review

- [Official Domain 3 task statements](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain3.html)
- [[Domain 3 Scenario Decisions]]
- [[Domain 3 Architecture Patterns]]
- [[Domain 3 Transcript Corrections]]
- [[Notebook Provenance and Progress]]
- [[Domain 3 Transcript Coverage]]
- [[Domain 3 Official Sources]]
