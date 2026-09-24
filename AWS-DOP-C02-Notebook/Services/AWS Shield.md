---
title: AWS Shield
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# AWS Shield

Managed DDoS protection. Distinguish automatic Standard network/transport protection from Advanced protection for explicitly protected resources and its additional detection, response, and application-layer capabilities.

## Choosing a response

Shield Advanced can use WAF rules for automatic application-layer mitigation when appropriately configured. A subscription alone does not mean every application endpoint is protected or all WAF settings are enabled. Map protected resources and verify monitoring/response configuration.

## Exam traps

- Auto Scaling adds capacity; it does not identify malicious requests.
- WAF is HTTP/S filtering, not a replacement for all network-layer protection.
- CloudFront reduces origin exposure only when direct origin access is also controlled.
- Do not assume protection is an unlimited availability guarantee.

## Links and sources

Task 5.2. [[AWS WAF]], [[Amazon CloudFront]], [[DDoS Mitigation and Attack Surface Reduction]].

- [Shield capabilities](https://aws.amazon.com/shield/features/)
- [Automatic application-layer mitigation](https://aws.amazon.com/blogs/aws/aws-shield-advanced-update-automatic-application-layer-ddos-mitigation/)
