---
title: HTTPS Connectivity Troubleshooting
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# HTTPS Connectivity Troubleshooting

## HTTP-to-HTTPS regression checklist

1. Verify the external service supports the intended HTTPS hostname/path and whether redirects/authentication changed.
2. Resolve DNS from the affected workload context; verify routes, NAT/proxy/VPC endpoints as applicable.
3. Check outbound TCP 443 on every applicable security group and outbound/return-path NACL rules.
4. Test TCP connection, then TLS handshake: certificate hostname, trust chain, expiry, SNI, supported protocols, and proxy behavior.
5. Check HTTP status/application errors only after transport and TLS succeed.
6. Correlate application logs, deployment changes, traces, and VPC Flow Logs by time and destination.

A successful Postman request from a laptop does not prove EC2 has the same network path, trust store, or credentials. Test from an authorized equivalent environment without exposing secrets.

## Interpreting evidence

Security groups are stateful; NACLs are stateless and must allow applicable return traffic/ephemeral ports. Flow-log REJECT suggests a network-policy problem but does not by itself identify the exact offending rule. ACCEPT does not prove certificate or API success.

CloudWatch Logs can help only if the required logs are being published. The CloudWatch agent is one collection path, not a universal prerequisite for every log source.

Task 5.3. [[Security Groups vs Network ACLs]], [[Amazon CloudWatch]], [[AWS X-Ray]].

- [Security groups — official resource](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)
- [Network ACLs — official resource](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
