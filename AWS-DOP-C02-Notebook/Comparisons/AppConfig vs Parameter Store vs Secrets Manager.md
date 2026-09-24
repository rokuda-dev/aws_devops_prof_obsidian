---
tags: [aws, dop-c02, comparisons]
updated: 2026-09-18
read: false
---

# AppConfig vs Parameter Store vs Secrets Manager

| Requirement | Choose | Operation/lifecycle cue |
|---|---|---|
| Safe runtime config/feature-flag rollout | [[AWS AppConfig]] | Validators, strategies, alarms/rollback |
| Hierarchical parameter lookup | [[AWS Systems Manager Parameter Store]] | String/StringList/SecureString, versions |
| Secret credential lifecycle/rotation | [[AWS Secrets Manager]] | External credential + version stages/rotation |
| Resource configuration compliance | [[AWS Config]] | Recorder/rules/conformance packs |

> [!warning]
> SecureString encryption is not external credential rotation. Updating a secret/parameter does not automatically refresh an app's cached or ECS launch-time injected value. A CloudFormation dynamic reference is not a general hot-reload mechanism.

