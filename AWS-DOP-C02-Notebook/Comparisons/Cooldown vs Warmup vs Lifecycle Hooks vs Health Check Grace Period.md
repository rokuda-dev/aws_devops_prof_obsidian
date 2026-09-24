---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# Cooldown vs Warmup vs Lifecycle Hooks vs Health Check Grace Period

| Mechanism | What it controls | Common trap |
|---|---|---|
| Simple scaling cooldown | Timing of subsequent simple-policy actions | Treating it as a universal block on all scaling |
| Instance warmup | New-instance contribution to aggregate scaling metrics and scale-in stabilization | Assuming no further scale-out can occur |
| Lifecycle hook | Transition wait state for initialization/termination work | Forgetting completion, heartbeat, retry, timeout |
| Health-check grace period | Delay before ASG acts on certain unhealthy status during startup | Treating it as metric warmup |
| Deregistration/draining | Existing request/connection completion during removal | Assuming immediate termination is safe |

Target tracking and step scaling can scale out while prior instances warm up; scale-in behavior is deliberately constrained during warmup. Scheduled scaling and unhealthy replacement do not simply wait for a simple-scaling cooldown.

Task 3.2. See [[Amazon EC2 Auto Scaling]], [[Scaling Metrics and Troubleshooting]].

- [Official cooldown behavior](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-cooldowns.html)
