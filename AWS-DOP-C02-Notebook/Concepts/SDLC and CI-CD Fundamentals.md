---
tags:
  - dop-c02
  - domain-1
  - sdlc
  - cicd
read: true
---

# SDLC and CI/CD Fundamentals

## SDLC phases

Requirements → design → implementation → testing → deployment → operations/maintenance. Models include waterfall, iterative/incremental, spiral, and Agile approaches. The exam usually tests the automation and feedback implications rather than definitions alone.

## CI/CD distinctions

| Practice | What is automated | Production gate |
|---|---|---|
| Continuous integration | Frequent merge, build, unit test | Not applicable |
| Continuous delivery | Build, broad testing, staging, release preparation | May be manual |
| Continuous deployment | Delivery pipeline through production | Automatic |

AWS defines CI as regular merging followed by automated builds/tests. Continuous delivery expands CI so changes are prepared for release; the manual production decision distinguishes it from continuous deployment.

## Pipeline anatomy

```text
Commit/PR
  → source
  → compile + unit test
  → package + scan
  → integration/acceptance test
  → staging deployment
  → approval or automated gate
  → production deployment
  → observe + rollback
```

Map this to [[AWS CodePipeline]], [[AWS CodeBuild]], artifact repositories, [[AWS CodeDeploy]], and [[Amazon CloudWatch, X-Ray, and OpenTelemetry]].

## Exam heuristics

- Shift fast tests left; run broader environment-dependent tests after deployment to a test environment.
- Promote the same immutable artifact across environments instead of rebuilding it.
- Keep infrastructure and application changes version-controlled.
- Use managed approvals and alarms rather than informal out-of-band gates.

Sources: [Continuous integration](https://aws.amazon.com/devops/continuous-integration/), [Continuous delivery](https://aws.amazon.com/devops/continuous-delivery/)
