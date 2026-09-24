---
title: DDoS Mitigation and Attack Surface Reduction
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# DDoS Mitigation and Attack Surface Reduction

## Complementary controls

| Goal | Controls |
|---|---|
| Absorb traffic and keep capacity elastic | Edge distribution/caching and appropriate Auto Scaling |
| Detect/mitigate DDoS | Shield protections and correctly configured Advanced capabilities where required |
| Filter malicious HTTP/S patterns | WAF web ACL, managed/custom and rate-based rules |
| Prevent direct origin bypass | Private VPC origin where supported, or restricted origin network/request access |
| Reduce administrative exposure | Session Manager with no inbound SSH/RDP; least privilege and hardened configuration |
| Reduce compromise propagation | Segmented networks/roles, scoped credentials, controlled dependencies |

Auto Scaling alone does not shrink attack surface or distinguish legitimate traffic. It can also increase costs during an attack.

Systems Manager is not a dedicated DDoS filtering service, but the transcript's blanket claim that it cannot reduce exposure is too strong: Session Manager can remove public SSH requirements and State Manager can maintain hardened settings. Patch Manager reduces vulnerability risk, not volumetric attack traffic.

## Origin restrictions

Putting an ALB behind CloudFront without controlling direct access can leave a bypass. Use supported private origins or appropriate origin checks/network restrictions and HTTPS. Keep secret origin-header values out of source and logs.

Task 5.2. [[AWS Shield]], [[AWS WAF]], [[Amazon CloudFront]], [[Amazon EC2 Auto Scaling]], [[AWS Systems Manager]].

- [DDoS best practices — official resource](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/welcome.html)
- [Restrict ALB origin access](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.html)
