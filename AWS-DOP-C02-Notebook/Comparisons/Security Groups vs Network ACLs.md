---
title: Security Groups vs Network ACLs
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# Security Groups vs Network ACLs

| Property | Security group | Network ACL |
|---|---|---|
| Scope | Attached network interfaces/resources | Associated subnet |
| Behavior | Stateful | Stateless |
| Rules | Allow rules | Allow and deny rules |
| Evaluation | Combined applicable group permissions | Ordered rule numbers, first matching rule |
| Return traffic | Automatically allowed for tracked permitted connections | Must be allowed explicitly |
| HTTPS regression | Check outbound TCP 443 and actual attached groups | Check outbound 443 plus appropriate return/ephemeral path |
| Restrict SSH | Narrow all relevant inbound allow paths | Additional subnet boundary; not a replacement for correct SG configuration |

A new narrow SG rule does not override an existing broad allow. Flow Logs help identify ACCEPT/REJECT traffic but do not validate TLS or pinpoint every rule failure alone.

Task 5.3. [[HTTPS Connectivity Troubleshooting]], [[Security Group Remediation and Access Safety]].

- [Security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)
- [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
