---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# Amazon EC2 Auto Scaling

## Role and exam cues

Maintain and change EC2 capacity through an Auto Scaling group (ASG). Use a launch template, distribute instances across Availability Zones, and register them with [[Elastic Load Balancing]]. Externalize state using [[Stateless Applications and External Session State]].

| Requirement | Mechanism |
|---|---|
| Keep a utilization metric near a target | Target tracking |
| Different capacity changes at different alarm severities | Step scaling |
| Predictable calendar demand | Scheduled scaling |
| Prepare instances before a surge | Warm pool and/or prebuilt AMI |
| Replace application-unhealthy instances | Enable ELB health checks for the ASG |
| Roll out a launch-template/AMI change | Instance refresh with health and rollback planning |

A load balancer stops routing to unhealthy targets; that alone does not configure ASG replacement based on ELB health. Confirm the health-check type.

## Timing distinctions

See [[Cooldown vs Warmup vs Lifecycle Hooks vs Health Check Grace Period]].

- Simple scaling waits for its cooldown before another simple-policy action.
- Target tracking and step scaling can scale out without waiting for the simple-scaling cooldown. Instance warmup affects aggregated scaling metrics and scale-in behavior.
- Lifecycle hooks hold an instance in a transition wait state so initialization, draining, or other work can finish. Send completion/heartbeat calls; handle timeout and failed work.
- Health-check grace periods suppress premature replacement during initialization; they are not metric warmup.

## Warm pools and EventBridge

Warm pools trade prepared capacity cost for faster launch. Pool instances still need correct images, configuration, credentials, and dependency access. Events are best effort, so handlers must tolerate duplicate/missing events and retries.

An example EventBridge detail filter for a warm-pool instance entering active ASG capacity is:

```json
{
  "source": ["aws.autoscaling"],
  "detail-type": ["EC2 Instance-launch Lifecycle Action"],
  "detail": {
    "Origin": ["WarmPool"],
    "Destination": ["AutoScalingGroup"]
  }
}
```

Field names are case-sensitive. Filter the ASG identity when needed. A filter routes an event; the handler must still complete the appropriate lifecycle action. See [[Amazon EventBridge]].

## Operational checklist

Inspect scaling activity history, alarm state and metric dimensions, min/max/desired bounds, suspended processes, instance warmup, lifecycle waits, launch-template validity, EC2 quotas, subnet addresses, and zonal capacity. Check scheduled-action time zones/DST and conflicting actions. A policy cannot exceed maximum capacity or solve an unavailable dependency.

Bake libraries into a tested AMI with [[EC2 Image Builder]] or [[AWS Systems Manager]] Automation. Publish a launch-template version and deliberately roll out instances; creating an AMI does not update running instances.

## Sources and task mapping

Tasks 3.1–3.3. See [[Scaling Metrics and Troubleshooting]], [[Domain 3 Scenario Decisions]].

- [Cooldowns](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-cooldowns.html)
- [Warm-pool events](https://docs.aws.amazon.com/autoscaling/ec2/userguide/warm-pools-eventbridge-events.html)
- [Scheduled actions, time zones, and DST](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html)

## Domain 4 — membership automation

Use lifecycle/state events for registrations/config updates, with retry-safe handling and current-membership reconciliation. Hooks need heartbeat/completion.

ASG replacement differs from eligible standalone-instance recovery. Terminating a low-utilization ASG instance can simply trigger replacement unless intended capacity changes.

Task 4.3. See [[Safe Event-Driven Remediation]], [[AWS Systems Manager]], [[AWS Health]].

## Domain 5 — membership-driven changes

Route relevant launch/terminate/lifecycle events through EventBridge, reconcile live membership, then update dependent data/configuration with an idempotent handler or Run Command on an authorized managed node. Complete/heartbeat lifecycle hooks where used.

Health replacement aids resilience; traffic absorption during DDoS does not shrink attack surface. Verify intended capacity before deleting instances or reacting to low-utilization recommendations.

Tasks 5.1–5.3. [[Event Sources and Response Contracts]], [[DDoS Mitigation and Attack Surface Reduction]], [[Scaling Metrics and Troubleshooting]].
