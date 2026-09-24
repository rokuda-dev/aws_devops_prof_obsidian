---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# AWS Application Auto Scaling

## Role

Scale supported service resources rather than EC2 group membership. Common Domain 3 examples are ECS service desired task count and DynamoDB provisioned throughput. [[Amazon EC2 Auto Scaling]] is the separate EC2 group service.

| Resource | Capacity being scaled | Important boundary |
|---|---|---|
| ECS service | Desired task count | Task capacity still needs Fargate or sufficient EC2 host capacity |
| DynamoDB provisioned table/GSI | Read or write capacity | Table and each GSI need appropriate policies and bounds |
| Other supported targets | Service-specific scalable dimension | Verify supported dimensions and quotas |

Register the scalable target, define minimum/maximum capacity, and configure the scaling policy or schedule. Use IAM roles appropriate to the service; policies cannot override downstream or account limits.

## DynamoDB distinction

Provisioned-mode target tracking reacts to observed utilization and alarm evaluation; bursts can throttle before capacity increases. On-demand mode manages capacity differently and does not require this provisioned-throughput target-tracking policy. Poor keys or a hot partition are not fixed merely by increasing aggregate capacity.

## ECS distinction

Service scaling adds tasks; EC2 capacity providers/ASGs add hosts. Fargate removes host management but does not choose the application replica count for you. Validate placement, deployment headroom, startup latency, and downstream connection limits.

## Sources

Task 3.2. See [[Amazon ECS]], [[Amazon DynamoDB]], [[Scaling Metrics and Troubleshooting]].

- [DynamoDB Auto Scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html)
- [Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html)
