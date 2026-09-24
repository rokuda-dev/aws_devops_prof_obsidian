---
title: Domain 5 Transcript Coverage
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# Domain 5 Transcript Coverage

## Input and status

The user supplied the three Domain 5 lesson sections for tasks 5.1–5.3, six resource URLs, and a blank item 7. All supplied lesson sections have been processed. Exam weight: 14%.

| Section | Topics processed | Main destinations |
|---|---|---|
| 5.1 event sources/response | Event sources, targets, public S3 permissions, Config/Trusted Advisor signals, safe load-balancer response, object actor audit and workflow integration | [[Event Sources and Response Contracts]], [[S3 Permission Monitoring and Remediation]], [[Config Compliance vs CloudTrail Actor Attribution]] |
| 5.2 configuration response | RDS/Health/ASG events, fleet capabilities, DDoS controls, exposed keys, Step Functions, Lambda deployment validation/alarms | [[Systems Manager Incident Operations]], [[DDoS Mitigation and Attack Surface Reduction]], [[Exposed Credential Response]], [[Lambda Deployment Validation Hooks]] |
| 5.3 troubleshooting | Incident process, Synthetics/traces, HTTPS networking, CI/CD failures/parallelism/minimum hosts, ECS/EKS triage, host licensing, SSH remediation, OpsItems | [[Incident Response Workflow and Evidence Preservation]], [[HTTPS Connectivity Troubleshooting]], [[CI-CD Failure Triage and Parallel Actions]], [[ECS and EKS Failure Triage]], [[Dedicated Host Compliance and Licensing]], [[Security Group Remediation and Access Safety]] |
| Six resources | VPC ACLs/SGs, Lambda/EventBridge link, CodeDeploy, DDoS whitepaper, Storage Gateway RefreshCache | [[Domain 5 Official Sources]], [[AWS Storage Gateway]] |
| Blank resource 7 | No title or URL supplied | Left unfilled; not invented |
| Ninth walkthrough question | Mentioned, content absent | Not marked processed |

## Editorial decisions and explicit extensions

- Preserve all prior notes, filenames, front matter and heading targets; enrich reusable canonical services rather than duplicating them.
- Paraphrase the supplied material and identify inaccurate shortcuts in [[Domain 5 Transcript Corrections]].
- Add practical evidence preservation, scoped remediation, duplicate/failure handling, TLS diagnostics and access-lockout safeguards.
- License Manager and preventive secret scanning extend the supplied licensing/credential scenarios; they are not claimed as named transcript content.
- RefreshCache is included because of the resource list, not because the transcript described a File Gateway scenario.
- The supplied old Lambda/EventBridge URL now redirects to a scheduling page; keep its original URL and explain the narrower current destination.

This is supplied-transcript coverage, not exhaustive blueprint or every possible service/platform configuration. Domain 6 is processed separately in [[Domain 6 Transcript Coverage]]. [[Notebook Provenance and Progress]], [[Notebook Changelog]].
