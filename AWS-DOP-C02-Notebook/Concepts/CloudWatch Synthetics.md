---
title: CloudWatch Synthetics
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# CloudWatch Synthetics

Canaries run scripted checks to monitor endpoints and user journeys. Domain 5 cue: detect failed APIs/pages or a deployment regression independently of normal user traffic.

## Investigation

Check run results, success/latency metrics, logs, and configured artifacts. Separate an application failure from a canary failure: DNS, VPC routing, execution permissions, artifact/metric delivery, timeout, runtime changes, and script assertions can each fail.

Use safe test data and minimal permissions. Protect screenshots, response bodies, and artifacts that may contain confidential information.

## Trace correlation

With appropriate active tracing and instrumentation, canary requests can participate in X-Ray/ServiceLens investigation. Traces are sampled; a missing trace is not proof that no request occurred. A canary provides observations, not automatic root-cause remediation or a production load test.

Private network canaries need suitable subnet/service connectivity; public-subnet placement alone does not give their Lambda execution environment a public IP.

## Links and sources

Task 5.3. [[Amazon CloudWatch]], [[AWS X-Ray]], [[Incident Response Workflow and Evidence Preservation]].

- [Official Domain 5 monitoring/troubleshooting requirements](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain5.html)
- [[Domain 5 Official Sources]]
