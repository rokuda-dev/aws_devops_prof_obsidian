---
title: AWS Storage Gateway
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# AWS Storage Gateway

Hybrid storage service. For this exam, distinguish the **S3 File Gateway RefreshCache API** from an S3 upload or a CloudFront invalidation.

## RefreshCache distinction

RefreshCache updates the cached inventory for a specified file share after objects were added, removed, or replaced directly in S3. It does not preload object contents into local cache storage, upload buffered local writes, or invalidate CloudFront caches.

The API starts an asynchronous operation. A successful API response is not proof that refreshing has finished; use the refresh-complete event notification before relying on the updated inventory. Respect documented request spacing/concurrency limits.

## Event response

An authorized handler can request a scoped refresh and correlate its completion notification to the request/file share. Avoid recursive change-trigger loops and broad refreshes on every object event.

## Links and sources

Additional-resource coverage only. [[Amazon S3]], [[Amazon EventBridge]], [[Event Sources and Response Contracts]].

- [RefreshCache — official resource](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_RefreshCache.html)
