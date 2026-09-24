---
tags:
  - aws
  - dop-c02
  - domain-2
  - migration
  - discovery
read: true
---

# AWS Application Discovery Service

Application Discovery Service collects on-premises configuration and utilization information for migration assessment and integrates with Migration Hub.

## Collection choices

| Need | Choice |
|---|---|
| Broad VMware discovery with low per-VM installation effort | Agentless Collector |
| Running processes and network connection/dependency detail | Discovery Agent |

The Agentless Collector is deployed in VMware and gathers infrastructure/performance information but does not provide the same in-guest process detail as the agent.

> [!warning]
> Older training may say “Discovery Connector.” Current documentation uses **Agentless Collector**.

## Current availability

> [!warning]
> Current AWS documentation says Application Discovery Service is no longer open to new customers and points to AWS Transform as an alternative. Preserve the collector/agent distinction for existing-service and historical scenarios; do not recommend ADS onboarding unconditionally for a new customer.

Select a Migration Hub home Region before discovery; discovered data is stored there. File-based import is another assessment route. The agent supplies running-process information; do not infer universal current network-collection limitations for every collector module from old training.

## Official AWS references

- [Service overview](https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html)
- [Availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html)
