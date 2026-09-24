---
title: Domain 5 Official Sources
tags: [aws, dop-c02, domain-5]
verified: 2026-09-18
read: false
---

# Domain 5 Official Sources

## Supplied resources — preserved in order

1. [Control traffic to subnets using network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
2. [Control traffic to AWS resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)
3. [Using Lambda with EventBridge — supplied legacy URL](https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents.html)
4. [CodeDeploy deployments](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-steps.html#deployment-steps-what-happens)
5. [AWS Best Practices for DDoS Resiliency](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/welcome.html)
6. [Storage Gateway RefreshCache](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_RefreshCache.html)
7. **Blank in the supplied list; no URL/title invented.**

Resource 3 currently redirects to [Invoke Lambda on a schedule](https://docs.aws.amazon.com/lambda/latest/dg/with-eventbridge-scheduler.html). Scheduling is not the same as event-pattern incident routing. The DDoS welcome URL redirects to the whitepaper root; the original supplied link remains above.

## Targeted verification sources

| Topic | Official evidence |
|---|---|
| Tasks 5.1–5.3 | [Current DOP-C02 Domain 5](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain5.html) |
| Rule destinations and boundaries | [Event bus targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html) |
| Health native event routing | [Health with EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html) |
| Historical exposed-key event/filter/workflow | [AWS event-driven operational response example](https://aws.amazon.com/blogs/compute/automate-your-it-operations-using-aws-step-functions-and-amazon-cloudwatch-events/) |
| Compromised credential containment | [AWS incident response containment guidance](https://aws.amazon.com/blogs/security/how-to-improve-your-security-incident-response-processes-with-jupyter-notebooks/) |
| Custom rule evaluators | [Config Lambda/Guard rules](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-aws-config-custom-rules-by-using-aws-cloudformation-guard-policies.html) |
| Response orchestration bridge | [SSM aws:executeStateMachine](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-executeStateMachine.html) |
| Organization rule response context | [Config organization-rule remediation](https://repost.aws/knowledge-center/add-config-remediation-actions) |
| Object ownership and ACL scope | [S3 Object Ownership](https://docs.aws.amazon.com/help-panel/AmazonS3/latest/console/hp-edit-object-ownership-page.html) |
| Object activity capture | [CloudTrail S3 data-event architecture](https://aws.amazon.com/blogs/aws/cloudtrail-update-capture-and-process-amazon-s3-object-level-api-activity/) |
| WAF rate-based controls | [WAF FAQs](https://aws.amazon.com/waf/faqs/) |
| Shield capabilities | [Shield features](https://aws.amazon.com/shield/features/) |
| L7 automation | [Shield Advanced automatic mitigation](https://aws.amazon.com/blogs/aws/aws-shield-advanced-update-automatic-application-layer-ddos-mitigation/) |
| Origin bypass prevention | [CloudFront restrict ALB access](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.html) |
| CodeDeploy Lambda/ECS callbacks/hooks | [AppSpec hooks](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html) |
| Minimum-host requirement | [Config CodeDeploy healthy-host rule](https://docs.aws.amazon.com/config/latest/developerguide/codedeploy-ec2-minimum-healthy-hosts-configured.html) |
| Action parallelism | [CodePipeline action declaration/runOrder](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-requirements.html) |
| Synthetic trace correlation | [CloudWatch Synthetics and X-Ray](https://aws.amazon.com/blogs/devops/debugging-with-amazon-cloudwatch-synthetics-and-aws-x-ray/) |
| Container collection setup | [CloudWatch FAQ](https://aws.amazon.com/cloudwatch/faqs/) |
| Fleet prerequisites | [Systems Manager Fleet Manager](https://aws.amazon.com/blogs/mt/streamline-server-fleet-management-aws-systems-manager-fleet-manager/) |
| OpsCenter availability/incident workflow | [OpsCenter migration guide](https://docs.aws.amazon.com/incident-manager/latest/userguide/migration-opscenter.html) |
| Dedicated Host license evidence | [Config features](https://aws.amazon.com/config/features/) |
| License-aware host management | [License Manager host resource groups](https://docs.aws.amazon.com/license-manager/latest/userguide/host-resource-groups.html) |
| Exact SSH rule semantics | [restricted-ssh](https://docs.aws.amazon.com/config/latest/developerguide/restricted-ssh.html) |
| Retired OpsWorks context | [OpsWorks Stacks end of life](https://aws.amazon.com/blogs/mt/seamlessly-off-board-from-aws-opsworks-stacks-by-detaching-resources/) |

## Evidence scope

Checked on September 18, 2026 using official AWS documentation/primary AWS material and relevant AWS guidance. Search result page chunks are authoritative excerpts; listing a page does not claim every line was read. Historical blog examples explain the lesson's origin, not a recommendation to deploy their old SDK/template unchanged.

Prior Domain 3/4 evidence is carried forward for RDS event timing, subscription collection, current service naming and other shared facts. No AWS account actions were performed.

[[Domain 5 Transcript Coverage]], [[Domain 5 Transcript Corrections]], [[Verification Ledger]], [[Official AWS Sources]].
