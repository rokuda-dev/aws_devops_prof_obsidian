---
title: AWS CloudHSM
tags: [aws, dop-c02, domain-6]
verified: 2026-09-19
read: false
---

# AWS CloudHSM

CloudHSM provides customer-controlled HSM clusters. IAM manages cluster resources, while CloudHSM users and client software perform cryptographic key operations. Deploy across appropriate Availability Zones for resilience. Certification claims depend on the hardware model and operating mode; current hsm2m.medium guidance describes FIPS 140-3 Level 3 validation, so do not memorize a blanket “FIPS 140-2” statement.

- [CloudHSM FIPS validation](https://docs.aws.amazon.com/cloudhsm/latest/userguide/fips-validation.html)
