---
title: Amazon EC2
tags:
  - aws
  - dop-c02
  - service
  - domain-3
  - domain-4
status: consolidated-study-note
updated: 2026-10-03
read: false
---

# Amazon EC2

Amazon EC2 provides resizable virtual-machine compute with configurable instance types, storage, networking, tenancy and lifecycle controls.

## Simplified automatic recovery

Simplified automatic recovery is enabled by default when a supported instance is launched, unless it is explicitly disabled. When an AWS infrastructure problem causes the instance's **system status check** to fail, EC2 can attempt to move the instance to healthy hardware in the same Availability Zone. A failure of only the instance status check—for example, an exhausted-memory, kernel or guest-networking problem—does not trigger this recovery mechanism.

A successful recovery appears to the operating system as an unplanned reboot. EC2 preserves the instance ID, Availability Zone, public/private/Elastic IP addresses, instance metadata, placement group and attached EBS volumes. Volatile RAM contents are lost and operating-system uptime resets.

Monitor `StatusCheckFailed_System` and the AWS Health events:

- `AWS_EC2_SIMPLIFIED_AUTO_RECOVERY_SUCCESS`
- `AWS_EC2_SIMPLIFIED_AUTO_RECOVERY_FAILURE`

A failure event means the recovery attempt did not restore the instance; investigate the continuing status-check failure and use an appropriate manual recovery path. A stop/start commonly moves an EBS-backed instance to new hardware, but a non-Elastic public IPv4 address can change.

## Eligibility and restrictions

Simplified automatic recovery works only for documented supported instance families using shared tenancy or Dedicated Instances. It is not supported for:

- bare-metal (`*.metal`) instances;
- instances on Dedicated Hosts—use Dedicated Host auto recovery instead;
- instances with instance store volumes;
- instances using an Elastic Fabric Adapter (EFA);
- instances in an Auto Scaling group, where health replacement is the relevant fleet mechanism; or
- instances undergoing a scheduled maintenance event.

The instance must be in the `running` state, no applicable service event can be active in AWS Health, and EC2 must have replacement capacity for the instance type. Recovery can fail because of insufficient capacity or because the maximum daily recovery attempts were reached. Automatic recovery is an individual-instance availability feature; it does not provide zero-downtime failover or replace multi-instance, multi-AZ design.

## CloudWatch action-based recovery

CloudWatch action-based recovery is a separate, manually configured option for supported instances. A per-instance alarm—normally on `StatusCheckFailed_System`—invokes the EC2 recover action and can publish notifications through Amazon SNS. It supports some configurations excluded from simplified recovery, including bare-metal instances and selected instances with instance store volumes, but instance-store data is lost during recovery. Metric-math and composite alarms cannot perform the EC2 recover action.

## Exam clues

| Scenario clue | Best interpretation |
|---|---|
| Underlying host/system status check fails on one eligible standalone instance | Simplified automatic recovery can move the instance to healthy hardware |
| Guest OS, filesystem, memory or application failure only | Diagnose or replace/reboot through another mechanism; system-failure recovery is not triggered |
| Instance belongs to an Auto Scaling group | Use ASG health checks and replacement behavior rather than simplified instance recovery |
| Dedicated Host fails | Dedicated Host auto recovery is a separate feature |
| Requirement is AZ-resilient or zero-downtime service availability | Use multiple instances across AZs with load balancing/Auto Scaling; single-instance recovery is insufficient |

## Official AWS references

- [Automatic instance recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html)
- [Simplified automatic recovery requirements and configuration](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-configuration-recovery.html)
- [EC2 status checks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html)
- [CloudWatch EC2 recover actions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UsingAlarmActions.html)

Tasks 3.2 and 4.2. See [[Amazon EC2 Auto Scaling]], [[AWS Health]], [[Metric Alarms and Anomaly Detection]].
