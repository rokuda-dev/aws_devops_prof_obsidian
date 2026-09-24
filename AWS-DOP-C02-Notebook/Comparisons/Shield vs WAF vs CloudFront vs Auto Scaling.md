---
title: Shield vs WAF vs CloudFront vs Auto Scaling
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# Shield vs WAF vs CloudFront vs Auto Scaling

| Control | Main contribution | Not sufficient for |
|---|---|---|
| [[AWS Shield]] | DDoS detection/mitigation; distinguish Standard/Advanced setup | All app authorization or unconfigured/unprotected endpoints |
| [[AWS WAF]] | Web-layer inspection/rules/rate limiting | Arbitrary L3/L4 or non-HTTP services |
| [[Amazon CloudFront]] | Edge delivery/caching and origin-load reduction | Blocking direct origin access without origin controls |
| [[Amazon EC2 Auto Scaling]] | Elastic capacity and health replacement | Identifying attackers or shrinking exposed endpoints |
| [[AWS Systems Manager]] | Managed access, patching, desired state, approved operational changes | Dedicated real-time DDoS traffic filtering |

Combine controls according to layers, resource eligibility, latency/availability, and business requirements. Remove unnecessary public administrative exposure and segment privileges/dependencies; capacity alone does not reduce blast radius.

Task 5.2. [[DDoS Mitigation and Attack Surface Reduction]], [[Domain 5 Official Sources]].
