---
tags:
  - aws
  - certification
  - dop-c02
  - domain-2
  - iac
  - configuration-management
domain: 2 - Configuration Management and IaC
weight: 17%
verified: 2026-09-19
read: true
---

# Domain 2 — Configuration Management and IaC

> [!summary]
> Domain 2 is **17% of scored content**. It tests reusable infrastructure, automated multi-account governance, and large-scale operational automation.

## Task 2.1 — Define cloud infrastructure and reusable components to provision and manage systems throughout their lifecycle

- [[AWS CloudFormation, CDK, and SAM]] — templates, stacks, change sets, StackSets, reusable constructs
- [[AWS Service Catalog and RAM]] — governed self-service and resource sharing
- [[AWS Systems Manager]] — managed-node configuration and operations
- [[AWS Config]] — configuration inventory, history, compliance, and remediation triggers
- [[AWS AppConfig, Parameter Store, and Secrets Manager]] — application configuration, parameters, and secrets

## Task 2.2 — Deploy automation to create, onboard, and secure AWS accounts in a multi-account or multi-Region environment

- [[AWS Organizations and Control Tower]] — OUs, SCPs, landing zones, controls, Account Factory
- [[AWS Config]] — organization rules/conformance packs and aggregators
- [[AWS Service Catalog and RAM]] — approved products and supported cross-account resource sharing
- [[Amazon GuardDuty and Inspector]] — threat detection versus vulnerability management

## Task 2.3 — Design and build automated solutions for complex tasks and large-scale environments

- [[AWS Systems Manager]] — inventory, State Manager, Automation, Patch Manager, Run Command, Session Manager
- [[AWS Step Functions and EventBridge]] — event routing and multi-step orchestration
- AWS Lambda — custom event-driven automation
- [[AWS Application Discovery Service]] — migration discovery and dependency information

## Domain mental model

```text
DEFINE        CloudFormation / CDK / SAM
DEPLOY        CodePipeline / CloudFormation / CodeDeploy
GOVERN        Organizations / Control Tower / Service Catalog
EVALUATE      AWS Config
OPERATE/FIX   Systems Manager
```

## High-value distinctions

- Config asks, “What is/was the resource configuration, and is it compliant?”
- CloudTrail asks, “Who called which AWS API?”
- Systems Manager asks, “How do I operate or remediate managed nodes?”
- AppConfig deploys application runtime configuration; AWS Config evaluates AWS resource configuration.
- An SCP limits maximum permissions but grants nothing.
- A Config aggregator centralizes data but does not enforce configuration.
- State Manager maintains desired managed-node state; Config evaluates resource compliance.

## Source

[Official Domain 2 blueprint](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain2.html)


## Canonical service navigation

Canonical IaC notes: [[AWS CloudFormation]], [[AWS CDK]], [[AWS SAM]], [[AWS CloudFormation StackSets]]. Canonical governance notes: [[AWS Organizations]], [[AWS Control Tower]], [[AWS Service Catalog]], [[AWS RAM]]. Security context: [[AWS Security Hub]], [[Amazon Detective]], [[Amazon GuardDuty]], [[Amazon Inspector]].

> [!warning]
> The official guide still mentions OpsWorks examples. OpsWorks Stacks reached end of life May 26, 2024; do not present it as a current new deployment choice. See [[Common Traps and Current Corrections]].

Coverage is consolidated study material, not exhaustive transcript parity. See [[Notebook Provenance and Progress]].
