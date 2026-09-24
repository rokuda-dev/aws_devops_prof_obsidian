---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-19
read: false
---

# Domain 3 Transcript Coverage

## Input and processing status

The user supplied a three-part Domain 3 course transcript and six additional AWS resources. All three supplied task-statement sections have been processed into linked study notes. This is not a claim of exhaustive coverage of every exam blueprint example or of a separate fifth walkthrough question whose content was not provided.

| Input section | Topics retained | Main study destinations |
|---|---|---|
| Task 3.1 | Dependency/resilience framework; telemetry and business objectives; safe deployment; RDS upgrades; cross-zone/NLB health; CloudFront/DAX; regional database/DNS recovery | [[Resilience Framework and Dependency Isolation]], [[Domain 3 Scenario Decisions]], [[Amazon RDS]], [[Elastic Load Balancing]], [[Amazon Route 53]] |
| Task 3.2 | ASG/ELB; warm-pool lifecycle events; prebuilt AMIs; DynamoDB capacity; global service checklist; EKS/Fargate; SAM; Regional APIs; scaling diagnosis | [[Scaling Metrics and Troubleshooting]], [[Amazon EC2 Auto Scaling]], [[Multi-Region Application Checklist]], [[Amazon EKS]], [[AWS Fargate]] |
| Task 3.3 | RTO/RPO strategies; ARC/DRS; backups/copies; geographic RDS DR scenarios; S3 replication/versioning; drift and recovery tests | [[Disaster Recovery Strategies]], [[Disaster Recovery Testing and Failback]], [[AWS Backup]], [[Amazon Application Recovery Controller]], [[AWS Elastic Disaster Recovery]] |
| Six supplied resources | RDS, Config, Aurora replication, DynamoDB global tables, DNS failover, API canary release | [[Domain 3 Official Sources]] |

## Editorial method

Enrich existing canonical services, add missing services/concepts/comparisons, preserve established filenames/headings, and explicitly correct misleading recipes. The input has been paraphrased rather than transcribed verbatim.

Current AWS nuances were checked using targeted official documentation chunks/pages. Sources do not imply every linked document was read in full. The correction table identifies changes material to exam decisions.

Earlier Domain 1–2 provenance limitations remain documented in [[Notebook Provenance and Progress]].

## Coverage boundary

Domains 4–6 were processed in later releases. The Domain 3 fifth walkthrough question was not supplied, so it remains explicitly outside the claimed source coverage; no question or answer was invented.

See [[Domain 3 - Resilient Cloud Solutions]], [[Domain 3 Transcript Corrections]], [[Notebook Changelog]].
