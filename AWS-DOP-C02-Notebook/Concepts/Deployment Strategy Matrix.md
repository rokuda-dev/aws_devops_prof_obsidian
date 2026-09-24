---
tags:
  - dop-c02
  - domain-1
  - deployments
read: true
---

# Deployment Strategy Matrix

| Strategy | Capacity/cost | Risk and rollback | Best cue |
|---|---|---|---|
| In-place / rolling | Lower extra capacity | Mixed versions; rollback may redeploy | Gradual replacement, cost sensitive |
| All-at-once | Minimal extra capacity | Highest blast radius | Fast non-production deployment |
| Blue/green | Duplicate environment/task set | Fast traffic reversal | Minimize downtime, validate green |
| Canary | Small initial exposure | Metrics decide continuation | Limit blast radius |
| Linear | Fixed increments over time | Gradual validation | Controlled ramp |
| Immutable | New resources, then cut over | Old fleet retained temporarily | Eliminate configuration drift |

## Platform mapping

- CodeDeploy: EC2 supports in-place or blue/green; on-premises supports in-place, not CodeDeploy blue/green.
- ECS: native blue/green/canary/linear or CodeDeploy blue/green with supported traffic configurations; match the controller and load-balancer support.
- Lambda CodeDeploy: alias traffic shifting between versions; all-at-once, canary, or linear.
- Elastic Beanstalk Standard: all-at-once, rolling, rolling with additional batch, immutable, traffic splitting, blue/green by environment swap.
- CloudFormation: infrastructure update semantics, change sets, replacement behavior, rollback, and resource-specific update policies.

> [!warning]
> Do not assume that a strategy supported on one compute platform exists with identical semantics on another.
