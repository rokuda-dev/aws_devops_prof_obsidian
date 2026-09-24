---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# Log Lifecycle Security and Integrity

## Separate collection, retention and protection

| Store | Lifecycle/security responsibility |
|---|---|
| CloudWatch log group | Explicit retention, encryption/access controls, log class/features |
| S3 archive | Lifecycle transitions/expiration, access policy, supported encryption, retention protection |
| OpenSearch index | Index retention/storage tiers, access and snapshot design |
| Query results/dashboards | Protect derived data and its own retention/access |

CloudWatch log groups can retain indefinitely unless configured otherwise. S3 lifecycle expiration can destroy needed audit evidence if misaligned with policy. Check lifecycle rules for current/noncurrent versions where versioning applies.

Log data is encrypted at rest by default in CloudWatch Logs; customer-managed KMS adds key-policy/access responsibilities. Grant only required ingestion/read/query actions. Redact sensitive data at source where possible; encryption does not stop authorized readers from seeing logged secrets.

## CloudTrail integrity

Enable trail log-file integrity validation to obtain hashes and hourly signed digest files. Digests reference delivered logs and previous digests; AWS uses regional signing key pairs. Validate the chain/logs with the appropriate tool.

**Detection, not prevention:** enabling digest delivery does not run validation automatically and does not prevent an authorized actor from modifying/deleting stored files. Combine restricted IAM/bucket access, retention protections and independent validation.

A missing or modified file can be detected when checking available chain/evidence. Integrity validation concerns CloudTrail-delivered logs, not arbitrary application files.

## ALB access logs

Enable the ALB's separate S3 access-log delivery and appropriate bucket policy. The bucket must satisfy regional requirements. The traditional direct-to-S3 ALB access-log path supports SSE-S3; do not simply mandate SSE-KMS on that path and assume delivery will work. Current ALB documentation also describes enhanced CloudWatch Logs integrations with CloudWatch Logs/Firehose/S3 destinations. Verify the selected path's permissions, format and encryption requirements rather than applying legacy constraints universally.

ALB access logs support request/latency investigation; delivery is best effort, not an exhaustive audit accounting guarantee. Keep CloudTrail object/API audit requirements separate.

Tasks 4.1 and 4.3. See [[AWS CloudTrail]], [[Amazon S3]], [[Elastic Load Balancing]].

- [CloudTrail integrity mechanism](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html)
- [ALB encryption constraint](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_elasticloadbalancingv2-readme.html)
- [ALB legacy access logs and enhanced integration notice](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html)
- [ALB bucket/Region configuration](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyLoadBalancerAttributes.html)
