---
title: Dedicated Host Compliance and Licensing
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# Dedicated Host Compliance and Licensing

## Placement requirement

A **Dedicated Host** is a physical host allocated to the account with host-level placement/licensing visibility. A **Dedicated Instance** also uses dedicated hardware but does not satisfy a requirement that specifically mandates an allocated Dedicated Host.

Record the relevant Config resource types. A scoped custom rule can evaluate designated application instances against placement tenancy/host identity and approved host inventory. Treat missing/stale evidence separately from confirmed compliance; do not use resource tags alone as proof of physical placement.

## License reporting

Config history can capture instance/host changes and host-level attributes relevant to licensing. Combine this with AMI/software inventory and the vendor's licensing terms. License Manager adds supported usage rules and host-group management.

A Config report can identify noncompliance but does not automatically ensure license spend never grows. Scaling, cores/sockets, reassignment restrictions, and license limits must be addressed.

## Remediation

Notify the owner, plan a controlled migration/redeployment to approved hosts, preserve data, and verify entitlement/capacity. Do not terminate an instance solely because a delayed Config evaluation reports noncompliance.

Task 5.3. [[AWS Config]], [[AWS License Manager]], [[AWS Health]], [[Domain 5 Scenario Decisions]].

- [Config Dedicated Host evidence](https://aws.amazon.com/config/features/)
- [License Manager host groups](https://docs.aws.amazon.com/license-manager/latest/userguide/host-resource-groups.html)
