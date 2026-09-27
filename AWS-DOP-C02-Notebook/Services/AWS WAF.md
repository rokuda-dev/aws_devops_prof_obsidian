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

For HTTP request floods, AWS identifies the WAF Anti-DDoS Managed Rule Group as the default solution from March 26, 2026, superseding legacy Shield Advanced Layer 7 Auto Mitigation. Existing Shield Advanced customers can continue using the legacy feature; new customers needing it must contact AWS Support. This describes the preferred solution, not automatic enablement of every web ACL.

- [Current Anti-DDoS versus legacy Shield mitigation notice](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-automatic-app-layer-response.html)

WAF addresses web-layer requests, not arbitrary SSH/database traffic. [[AWS Shield]] and edge architecture complement it. Associate the web ACL with the intended supported resource; an unprotected direct origin can bypass edge defenses.

## Links and sources

Tasks 5.1–5.2. [[DDoS Mitigation and Attack Surface Reduction]], [[Shield vs WAF vs CloudFront vs Auto Scaling]].

- [WAF FAQs](https://aws.amazon.com/waf/faqs/)
- [AWS DDoS resiliency guidance](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-best-practices-ddos-resiliency.html)
