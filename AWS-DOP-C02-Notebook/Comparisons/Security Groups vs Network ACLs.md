---
title: Security Groups vs Network ACLs
tags:
  - aws
  - dop-c02
  - domain-5
verified: 2026-09-18
read: true
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

## Default behavior comparison

| Scenario                                  | Security group                                                                     | Network ACL                                                                                    |
| ----------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| New custom resource — inbound             | No inbound rules; denies inbound traffic                                           | Only the unmodifiable `*` deny rule; denies inbound traffic                                    |
| New custom resource — outbound            | Allows all outbound IPv4 and applicable IPv6 traffic                               | Only the unmodifiable `*` deny rule; denies outbound traffic                                   |
| New custom resource — initial association | Must be associated with a resource to apply                                        | Not associated with a subnet until explicitly associated                                       |
| VPC-provided default — inbound            | Allows traffic only from resources associated with the same default security group | Allows all IPv4 and applicable IPv6 traffic; unmatched traffic reaches the final `*` deny rule |
| VPC-provided default — outbound           | Allows all IPv4 and applicable IPv6 traffic                                        | Allows all IPv4 and applicable IPv6 traffic; unmatched traffic reaches the final `*` deny rule |

**Exam trap:** “default security group” and “new security group” are not identical, and “default network ACL” and “new custom network ACL” have opposite initial traffic behavior.

A new narrow SG rule does not override an existing broad allow. Flow Logs help identify ACCEPT/REJECT traffic but do not validate TLS or pinpoint every rule failure alone.

Task 5.3. [[HTTPS Connectivity Troubleshooting]], [[Security Group Remediation and Access Safety]].

- [Create a security group](https://docs.aws.amazon.com/vpc/latest/userguide/creating-security-groups.html)
- [Default security group](https://docs.aws.amazon.com/vpc/latest/userguide/default-security-group.html)
- [Default network ACL](https://docs.aws.amazon.com/vpc/latest/userguide/default-network-acl.html)
- [Create a custom network ACL](https://docs.aws.amazon.com/vpc/latest/userguide/create-network-acl.html)
