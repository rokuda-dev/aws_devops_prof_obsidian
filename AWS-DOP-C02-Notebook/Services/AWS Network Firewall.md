---
title: AWS Network Firewall
tags: [aws, dop-c02, domain-6]
verified: 2026-09-19
read: false
---

# AWS Network Firewall

Network Firewall provides managed VPC traffic inspection with stateless and stateful rules. Traffic must actually route through firewall endpoints, and return-path symmetry matters. Use it for network-layer inspection; use [[AWS WAF]] for HTTP application-layer rules and [[Amazon Route 53 Resolver DNS Firewall]] for DNS-domain filtering.

- [Network Firewall documentation](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)
