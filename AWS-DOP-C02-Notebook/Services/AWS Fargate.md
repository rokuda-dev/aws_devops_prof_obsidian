---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# AWS Fargate

## Role

Serverless container compute for supported ECS tasks and EKS pods. Removes EC2 host provisioning/patching from the user's responsibilities, not application scaling, security, deployment, or data architecture.

| Platform | Replica scaling | Compute behavior |
|---|---|---|
| ECS on Fargate | ECS service policies through Application Auto Scaling | Fargate supplies compute for scheduled tasks |
| EKS on Fargate | Kubernetes pod-replica scaling, such as HPA | Eligible pods run on Fargate based on configured profiles |

Allocate suitable CPU/memory, networking, IAM roles, and observability. Check service-specific limitations and regional/account capacity quotas. Load balancer health, task startup, and database connection capacity remain important.

## Billing correction

Running allocated tasks/pods incur CPU/memory charges even when the application is idle. “Serverless never pays for idle capacity” is not universally true. Lambda provisioned concurrency is another counterexample.

Fargate removes idle EC2 host management but does not automatically scale an application to zero. Use realistic replica bounds and availability requirements.

## Sources

Task 3.2. See [[Amazon ECS]], [[Amazon EKS]], [[AWS Application Auto Scaling]].

- [EKS Fargate allocation and cost explanation](https://aws.amazon.com/blogs/containers/saving-money-pod-at-time-with-eks-fargate-and-aws-compute-savings-plans/)
- [Fargate overview](https://aws.amazon.com/fargate/)

## Domain 4 — telemetry

Use supported task log drivers/routers rather than installing an EC2 host agent on inaccessible Fargate infrastructure. Configure awslogs group/Region/prefix and execution-role permissions; FireLens uses task resources and task-role destination access.

Tasks 4.1 and 4.3. See [[CloudWatch Agent and Container Log Collection]], [[Domain 4 Scenario Decisions]].

## Domain 5 — task investigation boundary

Use task/service status, stopped reasons and configured container logs. Do not prescribe SSH or Docker commands against a customer-managed Fargate host. Verify execution-role log/image access separately from application task-role API access.

Task 5.3. [[ECS and EKS Failure Triage]], [[CloudWatch Container Insights]].
