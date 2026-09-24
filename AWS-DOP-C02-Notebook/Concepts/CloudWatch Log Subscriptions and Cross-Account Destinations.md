---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# CloudWatch Log Subscriptions and Cross-Account Destinations

## Subscription purpose

Continuously forward **new matching log events** for processing/delivery. A subscription is not a historical query or a metric transformation.

| Destination/path | Use |
|---|---|
| Kinesis Data Streams | Custom consumers, buffering/replay, multiple consumers |
| Lambda | Custom processing with supported subscription permissions |
| Data Firehose | Managed buffered delivery, such as to S3 |
| OpenSearch integration | Supported searchable indexing path |

Cross-account sharing uses a receiver-side **logical destination** with an authorized resource/policy/role. Current documentation supports Kinesis Data Streams and Firehose-backed cross-account paths; do not generalize direct Lambda/OpenSearch destinations into the same logical-destination contract.

## Sender/receiver checklist

1. Create the actual destination resource in the recipient account.
2. Authorize CloudWatch Logs delivery through an appropriate role/trust policy.
3. Define the logical destination and access policy for intended senders/organization.
4. Create the sender subscription or appropriate account-level policy.
5. Test with a known matching event and verify source identity and downstream records.
6. Deploy/onboard the required policies for future accounts/log groups—not merely today's groups.

The source log group and logical destination must have the documented same-Region relationship; the underlying destination resource can support a different Region in documented architectures. Check the exact destination type rather than assuming one universal rule.

## Payload and delivery

CloudWatch batches/compresses subscription data. Decode/decompress the appropriate envelope, handle control messages, preserve individual event IDs and tolerate retries/duplicates.

Monitor ForwardedLogEvents, ForwardedBytes, DeliveryErrors and DeliveryThrottling. Retriable delivery errors are retried for a bounded window (documented up to 24 hours); permissions/resource errors require prompt correction. Do not assume infinite recovery/backfill.

Avoid recursive pipelines: exclude log groups produced by the processing pipeline when necessary. Centralizing a processor's output back into its input can create runaway volume/cost.

## Current native alternative

CloudWatch Logs centralization can copy selected organizational logs into a destination account/Region. OAM cross-account observability instead provides federated visibility. Neither automatically means those logs have been indexed in OpenSearch.

Task 4.1; reused in 4.2–4.3. See [[Cross-Account Observability vs Log Centralization]], [[Centralized Logging Architecture]].

- [Subscriptions — official resource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SubscriptionFilters.html#LambdaFunctionExample)
- [Cross-account Firehose setup](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CrossAccountSubscriptions-Firehose-Account.html)
- [Forwarding failure metrics/retries](https://repost.aws/knowledge-center/cloudwatch-failed-log-delivery)
