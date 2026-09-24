---
tags:
  - dop-c02
  - domain-1
  - testing
read: true
---

# Testing and Pipeline Placement

| Test | Typical placement | Signal |
|---|---|---|
| Static analysis / lint | Earliest build phase | Findings or exit status |
| Unit | Build phase, every change | Fast deterministic result |
| Dependency/security scan | Build/package phase | Policy threshold |
| Integration | Ephemeral/test environment | Cross-component behavior |
| Acceptance/UI | Staging | Business/user workflow |
| Load/stress | Dedicated performance environment | Latency, throughput, saturation |
| Smoke | Immediately after deployment | Critical path works |
| Canary validation | During limited traffic shift | Error/latency alarms |

## AWS patterns

- CodeBuild runs commands and fails on non-zero exit status.
- CodeBuild report groups preserve test and coverage reports.
- CodeDeploy validation hooks run scripts for EC2/on-premises or Lambda validation functions for ECS/Lambda.
- CloudWatch alarms can stop and roll back a CodeDeploy deployment.
- X-Ray/OpenTelemetry traces help isolate downstream latency and failures.

> [!exam]
> Tests that require deployed dependencies do not belong in the earliest unit-test stage. Build once, deploy the candidate artifact into a controlled environment, then run integration/acceptance tests.
