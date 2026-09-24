---
title: Domain 5 Transcript Corrections
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# Domain 5 Transcript Corrections

The transcript supplies exam scenarios, not production-ready authorization. These corrections keep simplified or outdated claims identifiable.

| Transcript claim / shortcut | Correct study interpretation |
|---|---|
| Auto-heal an OpsWorks stack | OpsWorks Stacks reached end of life May 26, 2024; use supported fleet/configuration patterns |
| S3 events monitor unauthorized actions generally | Native events cover specific operations; CloudTrail capture and IAM enforcement answer different audit/security requirements |
| Public-list-only follows from Trusted Advisor | A custom requirement needs exact policy evaluation; intentional public listing can expose names/metadata |
| Config changes, Trusted Advisor check results and CloudWatch metrics are interchangeable | They are distinct sources, schemas and evaluation/refresh timings |
| Select “CloudWatch alarms” as generic EventBridge targets | Current targets include CloudWatch log groups and built-in actions; alarms can emit events, not serve as arbitrary rule destinations |
| Delete unused load balancers immediately | Review traffic, standby role, DNS/service dependencies, ownership and approved change/rollback |
| Config cannot directly use Step Functions, therefore no workflow can combine them | Lambda/Guard evaluate custom rules; EventBridge or SSM Automation can connect response workflows to Step Functions |
| Bucket-level Config alone identifies approved object actors | Use relevant CloudTrail S3 data events and identity/session attribution; enforce with policies |
| CloudWatch must call the Health API to notify | Health publishes native EventBridge events; direct API polling is a separate option |
| SSM cannot reduce attack surface/blast radius in any way | It is not a DDoS filter, but Session Manager and desired-state hardening can reduce exposure; capacity alone is insufficient |
| CloudFront placement fully hides the origin | Restrict direct origin access or use supported private origins |
| Exposed-key Health event validates code before GitHub push | Reactive detection; add preventive scanning and do not assume complete detection coverage |
| Delete every credential as generic remediation | Scope verified affected key/identity; promptly contain, preserve audit, rotate and investigate |
| Lambda uses test-traffic lifecycle hooks like ECS | Lambda has BeforeAllowTraffic/AfterAllowTraffic; explicitly test the target version |
| Returning from a validation Lambda completes validation | Report Succeeded/Failed through PutLifecycleEventHookExecutionStatus; absent callback times out |
| Several Lambda functions are a CodeDeploy host fleet | Model each function/version/alias deployment and coordinate the application pipeline |
| Generic 5XX metric/ASG settings apply to every Lambda deployment | Match service namespace and platform; Lambda Errors and EC2 minimum hosts are different concerns |
| HTTP→HTTPS only needs port 443 | Also validate return path, DNS/routes, TLS/certificate/proxy behavior and application response |
| CloudWatch Logs always requires an EC2 agent | Required logs must be published, but agents, APIs, drivers and other integrations are different paths |
| HOST_COUNT/FLEET_PERCENT monitor actual healthy hosts | MinimumHealthyHosts configuration types; check actual deployment/application health separately |
| Every ECS 137 exit means OOM | SIGKILL also follows shutdown timeout/manual kill; correlate stopped reason and memory |
| CloudWatch automatically enables all Container Insights | Appropriate ECS opt-in/EKS collection setup and permissions are required |
| Dedicated Instance satisfies Dedicated Host licensing placement | Different tenancy/host models; evaluate exact placement and contractual rules |
| Config alone guarantees no software-license cost increase | Evidence/reporting is not an automatic cap; configure usage limits/host strategy and verify terms |
| restricted-ssh means only the datacenter may connect | It rejects world-open IPv4/IPv6, not every unapproved restricted CIDR; use stricter evaluation |
| OpsCenter and Fleet Manager are the same maintenance feature | OpsItems/incident context versus managed-node tools; Automation/State Manager perform different actions |

Evidence: [[Domain 5 Official Sources]], [[Verification Ledger]]. Prior-domain current facts carried forward are not all claimed newly reread.

Tasks 5.1–5.3. [[Config Compliance vs CloudTrail Actor Attribution]], [[Lambda vs ECS vs EC2 CodeDeploy Hooks]], [[Shield vs WAF vs CloudFront vs Auto Scaling]], [[Security Groups vs Network ACLs]].
