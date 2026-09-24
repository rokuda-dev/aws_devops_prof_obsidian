---
title: Domain 5 Scenario Decisions
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# Domain 5 Scenario Decisions

| Supplied scenario | Best first approach | Why / pitfall |
|---|---|---|
| Public S3 buckets may allow list only | Clarify intentional exposure; custom desired-state policy evaluation and scoped repair + notification | Trusted Advisor alone cannot prove this exact policy |
| Compliance team alone may access/change confidential objects | Enforce approved roles; audit relevant S3 data events and inspect actor/session context | Bucket Config state alone misses per-object actor history |
| Unused load balancers reported | Validate ownership, dependencies, traffic window/standby need; approved IaC change | Refreshed recommendation is not deletion authorization |
| RDS failover/low-storage/config event | RDS event route plus relevant metrics/app verification | Event delivery may lag; low-storage metrics and notification differ |
| EC2/RDS scheduled maintenance | Health EventBridge filtering → SNS/OpsItem and controlled response | No mandatory polling of Health API through CloudWatch |
| DDoS attack surface/blast radius | Shield/WAF/edge plus restricted origins, segmentation and reduced admin exposure | Auto Scaling alone absorbs demand; SSM is not a DDoS filter |
| IAM key exposed in GitHub | Preventive scanning plus reactive Health/EventBridge/Step Functions containment | Detection occurs after exposure, not before push |
| Test Lambda APIs before production | Candidate-version tests in BeforeAllowTraffic; callback status; alarms/post-hook; rollback enabled | AfterAllowTestTraffic is ECS, not Lambda |
| HTTP changed to HTTPS and app fails | Check 443/return path, DNS/routes, TLS trust/SNI/hostname and real API response from workload context | Laptop Postman success/Flow Logs ACCEPT is incomplete proof |
| Pipeline too slow | Parallelize truly independent same-stage actions with equal runOrder | Preserve artifacts/dependencies; not the same as pipeline execution mode |
| CodeDeploy healthy-host setting | Inspect MinimumHealthyHosts type/value and actual per-target behavior | HOST_COUNT/FLEET_PERCENT are policy types, not current health metrics |
| ECS deployment/process fails | Service events + stopped reasons/exit status + configured logs + target health/IAM/network | Exit 137 does not uniquely prove OOM |
| EKS process fails | Pod/node/events/logs/probes/resources + configured Container Insights/control-plane logging | Collection and autoscaling are distinct configured systems |
| App must run only on Dedicated Hosts without license growth | Config host/instance evidence + custom placement check and license-term/limit reporting | Dedicated Instance ≠ allocated Dedicated Host; compliance ≠ cost cap |
| SSH open from anywhere; require datacenter only | Stricter CIDR evaluation and scoped SSM remediation with recovery path | restricted-ssh merely rejects world-open SSH; check IPv6 and all SGs |
| Investigate/remediate operational issues | OpsCenter OpsItem + evidence + Automation runbook | Fleet Manager is node tooling, not the incident case system |

## Troubleshooting sequence

Read [[Incident Response Workflow and Evidence Preservation]], then [[HTTPS Connectivity Troubleshooting]], [[CI-CD Failure Triage and Parallel Actions]], and [[ECS and EKS Failure Triage]].

## Additional-resource scenario: RefreshCache

When S3 objects change outside an S3 File Gateway, RefreshCache updates the share's cached inventory. Wait for asynchronous completion; it does not preload data or flush local writes. This is supporting-resource coverage, not a transcript scenario.

Task 5.1–5.3. [[Domain 5 Architecture Patterns]], [[Domain 5 Transcript Corrections]], [[AWS Storage Gateway]].

The ninth walkthrough question was mentioned but not supplied; no solution is invented for it.
