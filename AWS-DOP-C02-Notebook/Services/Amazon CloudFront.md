---
title: Amazon CloudFront
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-09-18
read: true
---

# Amazon CloudFront

Global content delivery with edge caching, origin failover, and request controls.

## Exam mapping

Task statements: 1.4; cross-domain resilience/security. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Distributions use cache behaviors, cache policies, origin request policies, and origins. Origin groups pair primary/secondary origins. TTL and cache-key cardinality affect hit ratio.

## Architecture pattern

Cache miss → primary origin → eligible failure → secondary origin; [[Lambda@Edge]] can customize origin requests/responses.

## IAM and security

Use HTTPS; use OAC for supported S3 origins; use signed URLs/cookies for restricted viewer access. See [[CloudFront Field-Level Encryption]].

## Failure, rollback, and lifecycle

Origin failover applies to GET, HEAD, and OPTIONS, not arbitrary POST writes. New requests normally start with primary: this is request-level failover, not persistent DNS failover.

## When to choose

> [!exam]
> Choose for edge caching, origin protection, global delivery, and supported request-level failover.

## Do not confuse with and exam traps

> [!warning]
> Longer TTL improves hit ratio only if freshness permits. Unnecessary cookies/headers/query keys fragment cache entries.

## Official AWS references

- [Amazon CloudFront official reference](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 3 — delivery versus regional recovery

Cache S3 media/static objects at edge locations to reduce origin requests and improve global delivery. Configure a secondary regional origin for supported request-level origin failover.

Origin failover is not a general failover mechanism for writes or a database replication service. Destination objects must already be available through an appropriate [[Amazon S3]] replication/recovery design.

Tasks 3.1–3.2. See [[Route 53 vs Global Accelerator vs CloudFront]], [[Multi-Region Application Checklist]].

## Domain 5 — DDoS and origin exposure

Edge caching/distribution can reduce origin load. Control direct access to the origin; supported private VPC origins or appropriate request/network restrictions prevent a public-origin bypass.

Use Shield/WAF and reduced administrative exposure as complementary layers. Auto Scaling is capacity handling, not malicious-traffic identification.

Task 5.2. [[DDoS Mitigation and Attack Surface Reduction]], [[AWS Shield]], [[AWS WAF]].
- [ALB origin restriction](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.html)
