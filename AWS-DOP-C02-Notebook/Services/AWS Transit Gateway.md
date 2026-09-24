---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# AWS Transit Gateway

## Role

Regional hub router connecting VPCs and other supported networks. Multi-Region private connectivity can use a transit gateway in each Region with **inter-Region peering**.

VPC peering can fit a small, simple topology; transit gateways help manage larger hub-and-spoke estates. More Regions alone is not sufficient reason to ignore cost, routing requirements, and operational complexity.

## Peering checklist

- Create/accept the correct regional peering attachment.
- Configure static routes toward the peering attachment in both transit gateway route tables.
- Configure VPC subnet routes and security controls for the required paths.
- Check address overlap, return routing, DNS resolution design, and network dependencies.
- Do not assume routes propagate automatically across transit gateway peering.

Private routing does not make an application multi-Region resilient by itself. A recovery Region that calls essential services only in the failed Region still has a primary-Region dependency.

## Sources

Task 3.2. See [[Multi-Region Application Checklist]].

- [Inter-Region peering pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-the-setup-of-inter-region-peering-with-aws-transit-gateway.html)
- [Static peering routes](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering-add-route.html)
