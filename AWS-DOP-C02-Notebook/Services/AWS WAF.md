---
title: AWS WAF
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# AWS WAF

Web application firewall for supported HTTP/S resources. Domain 5 cue: reject abusive web requests using a web ACL, managed/custom rules, and rate-based controls.

## Incident-response pattern

Measure legitimate traffic, identify an attack pattern, test a scoped rule in count mode where appropriate, then enforce and monitor false positives. Version changes and retain a rollback path. Rate limiting is not a substitute for authentication or complete volumetric protection.

## Boundaries

WAF addresses web-layer requests, not arbitrary SSH/database traffic. [[AWS Shield]] and edge architecture complement it. Associate the web ACL with the intended supported resource; an unprotected direct origin can bypass edge defenses.

## Links and sources

Tasks 5.1–5.2. [[DDoS Mitigation and Attack Surface Reduction]], [[Shield vs WAF vs CloudFront vs Auto Scaling]].

- [WAF FAQs](https://aws.amazon.com/waf/faqs/)
- [AWS DDoS resiliency guidance](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/welcome.html)
