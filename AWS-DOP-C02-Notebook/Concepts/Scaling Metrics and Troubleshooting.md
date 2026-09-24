---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# Scaling Metrics and Troubleshooting

## Select the bottleneck metric

| Workload | Useful scaling signal | Caveat |
|---|---|---|
| Web tier | Request rate per target, CPU, latency/saturation | Latency can be a downstream problem |
| Worker tier | Queue backlog per worker and processing time | Total queue depth alone ignores capacity |
| Containers | CPU/memory/custom metric plus pending tasks/pods | Replica count and host capacity are separate |
| Database | Consumed capacity, throttles, hot-key evidence | Aggregate capacity cannot fix every key distribution |
| Recovery site | Headroom, lag, startup time, dependency readiness | “More instances” is not full recovery |

Ensure the metric is emitted, correctly dimensioned, timely, and compatible with the scaling policy. Target tracking needs a utilization signal that changes appropriately with capacity.

## Diagnostic order

1. Inspect alarm/policy and scaling activity history.
2. Check min/max/desired capacity, policy enablement, suspended processes, schedules/time zones, and conflicts.
3. Distinguish cooldown, instance warmup, lifecycle wait, health grace, and draining.
4. Inspect launch/placement failures: IAM, AMI/template, quota, AZ capacity, subnet IPs, networking, image/dependency access.
5. Verify healthy service registration and actual application throughput.
6. Examine downstream quotas/connections and hot partitions before adding more callers.

For scheduled actions, inspect the configured time zone and daylight-saving behavior rather than assuming local wall-clock time. For lifecycle waits, complete the action or diagnose timeout/handler failures.

## Architecture improvements

Use prebuilt tested AMIs, warm pools where appropriate, external state, multiple zones, and adequate deployment headroom. [[Amazon DynamoDB Accelerator (DAX)]] and [[Amazon CloudFront]] address appropriate repeated reads/content delivery; neither is a universal scaling solution.

## Sources

Task 3.2. See [[Amazon EC2 Auto Scaling]], [[AWS Application Auto Scaling]], [[Amazon EKS]].

- [ASG cooldown behavior](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-cooldowns.html)
- [DynamoDB scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html)
