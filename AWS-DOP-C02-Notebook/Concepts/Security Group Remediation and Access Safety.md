---
title: Security Group Remediation and Access Safety
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# Security Group Remediation and Access Safety

## Define the desired access

The managed Config rule **restricted-ssh**, identifier **INCOMING_SSH_DISABLED**, checks whether incoming SSH is restricted rather than open to 0.0.0.0/0 or ::/0. It has no allowed-datacenter-CIDR parameter. “Not world-open” is weaker than “only the approved datacenter CIDR.”

Use a custom/appropriate policy evaluation for the stricter requirement. Check IPv4/IPv6 and the combined permissions of all attached security groups; adding one restricted rule does not cancel another broad allow.

## Controlled remediation

1. Identify the exact group/rule and approved source CIDR from an authoritative input.
2. Recheck live configuration and exceptions.
3. Establish an authorized recovery/management path to avoid locking out operations.
4. Use a scoped SSM Automation runbook to replace only the offending SSH access, preserving unrelated required rules.
5. Verify allowed and denied paths, reevaluate compliance, and notify/record the result.

Use approvals and concurrency/error limits appropriate to blast radius. Prefer Session Manager and no inbound SSH where requirements allow; do not remove a mandated access path without an agreed replacement.

Task 5.3. [[AWS Config]], [[AWS Systems Manager]], [[Security Groups vs Network ACLs]], [[Safe Event-Driven Remediation]].

- [restricted-ssh exact behavior](https://docs.aws.amazon.com/config/latest/developerguide/restricted-ssh.html)
- [Security groups — official resource](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)
