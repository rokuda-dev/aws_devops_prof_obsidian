---
title: Domain 6 Architecture Patterns
tags: [aws, dop-c02, domain-6]
verified: 2026-09-19
read: false
---

# Domain 6 Architecture Patterns

## Temporary identity with bounded access

Use Identity Center for workforce access, roles for AWS workloads, Roles Anywhere/federation for eligible external workloads and Cognito for application users. Separate role trust, permissions, session restrictions and organizational ceilings.

## Multi-account security control loop

Prevent unwanted state → detect noncompliance/finding → route event → assume a narrowly scoped target role → run idempotent remediation → re-evaluate → preserve evidence. Systems Manager Automation can target multiple accounts/Regions when central administration and target execution roles are configured.

## Sensitive-data release gate

Restricted S3 staging → Macie/classification result correlated to exact object version → transform/reject → verify → authorized release to curated storage. Classification is not enforcement.

## Encryption and recovery

Envelope encryption protects data keys; key policy controls use. Encryption defaults cover future writes while migration handles existing data. RDS encryption migration is a replacement/cutover workflow. Certificate management protects TLS identity, not stored secrets.

## Defense in depth

Use WAF for HTTP patterns, Shield for DDoS protection, Network Firewall for routed VPC inspection, DNS Firewall for Resolver-domain queries, security groups for stateful resource filtering and network ACLs for stateless subnet controls. Firewall Manager applies supported policies at organization scale when scope/prerequisites are configured.

[[Domain 6 Scenario Decisions]], [[Domain 6 Transcript Corrections]], [[Domain 6 Official Sources]].
