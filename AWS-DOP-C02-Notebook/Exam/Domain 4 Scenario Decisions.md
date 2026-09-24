---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# Domain 4 Scenario Decisions

## Transcript scenarios

| Scenario | Correct first approach | Exam trap |
|---|---|---|
| Payment/refund transactions each minute | Custom CloudWatch metrics, batching/StatisticValues where suitable, alarm + SNS | EventBridge is not numeric metric storage; SampleCount != transaction Sum |
| Central indexed CloudWatch/VPC logs, current/future org accounts | Configure producers; subscriptions/destination authorization + Kinesis/custom indexing, or suitable current centralization + analysis design | One filter on today's groups does not onboard every future account |
| Real-time security analytics across accounts | Streaming log pipeline to intended analytics; separately use GuardDuty for supported threat detection | Numeric anomaly detection does not replace raw log delivery |
| ECS services + ALB logs into S3 | See completed design below | awslogs does not need a host CloudWatch agent merely to send stdout/stderr |
| Confidential S3 puts/gets/deletes audit | Enable relevant CloudTrail **data events**, deliver/query audit logs | Management events/event history alone do not cover object reads |
| Artifact bucket policy accidentally changed | CloudTrail record + metric filter/alarm/SNS or EventBridge API rule | Notification != automatic policy restoration; CodeDeploy rollback is deployment-specific |
| Dedicated single-instance workload availability | Verify eligible EC2 automatic recovery/status monitoring; notify on Health events | Single-instance recovery does not produce zero-downtime AZ/Region HA |
| Whole-infrastructure compliance dashboard | Config recording/rules + configured aggregator/views; optional prepared Athena/BI dataset | Tags/Trusted Advisor/Service Catalog alone do not evaluate all actual resource compliance |
| Compromised EC2 or SSH brute force | GuardDuty with required account/Region/protection scope; scoped investigation/response | Logs stored centrally do not enable every detector automatically |
| Suspicious activity findings into S3 | Native GuardDuty S3 findings export where it fits; event-driven custom delivery if needed | Firehose/EventBridge is not always needed for native export |
| SSH login after prior breach | Detect contextual access, preserve evidence, restrict/contain and verify | Terminating every instance that reports a login can destroy evidence/service availability |
| Low-utilization EC2 cleanup | Trusted Advisor/CloudWatch signal + owner/state/schedule review + safe scaling decision | Low CPU alone is not proof of waste; ASG may replace terminated instances |
| Hadoop nodes need maintenance notification | Health → EventBridge service/event filter → SNS | Metric filter cannot directly inspect an event bus; inventory sync is not notification transport |
| DynamoDB registration updates on ASG changes | ASG event/lifecycle hook → idempotent Lambda update + membership reconciliation | Event retries/order and hook completion need handling |
| Batch host config needs active ASG IPs | Event-triggered reconciliation → SSM Run Command/State Manager on managed host | Replaying incremental updates alone can leave a stale config |
| CloudTrail logging must remain enabled | Prevention + StopLogging API event detection + recheck/StartLogging + periodic assurance | Config periodic rule is not real-time or guaranteed exactly hourly |
| Shared cluster config changes | Versioned desired config + SSM State Manager/Run Command/Automation as appropriate | OpsWorks Stacks is retired; old Chef configure-event recipe is historical |

## Completed ECS-to-S3 design

1. Configure every application container's task definition to use awslogs, with the correct group, Region and identifying stream prefix. Give the log-delivery identity narrowly scoped permissions; preconfigure retention/encryption.
2. Create an appropriate CloudWatch Logs subscription to Firehose. Configure log decompression/message extraction if needed for the intended S3 format, and authorize Firehose's destination/error paths.
3. Deliver buffered records into a protected S3 bucket/prefix. Monitor forwarding errors, Firehose delivery/freshness, and missing expected records.
4. Enable ALB access logging separately. For traditional direct S3 delivery, satisfy same-Region bucket/policy and SSE-S3 requirements. Current enhanced ALB logging integrations are an alternative with their own delivery requirements.
5. Catalog/query suitable S3 records with Athena or another selected analytics tool. Set lifecycle/retention and access controls for raw logs and query outputs.

Near-real-time includes subscription, buffering and service delivery delays. FireLens is another deliberate container-routing option, not a requirement for awslogs.

## StopLogging trigger distinction

A CloudTrail API rule matches source aws.cloudtrail, detail-type AWS API Call via CloudTrail, eventSource cloudtrail.amazonaws.com and eventName StopLogging. A Config compliance-change rule matches a **different event** after evaluation. Neither should be called “instantaneous.”

Study patterns only: no AWS account actions were executed. See [[Safe Event-Driven Remediation]], [[Domain 4 Official Sources]].
