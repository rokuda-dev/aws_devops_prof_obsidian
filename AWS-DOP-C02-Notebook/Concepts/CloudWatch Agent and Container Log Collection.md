---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# CloudWatch Agent and Container Log Collection

## Host telemetry versus container stdout

| Requirement | Mechanism | Permissions/configuration |
|---|---|---|
| EC2/on-prem OS memory/disk metrics and file logs | Unified CloudWatch agent | Publishing identity, paths, metrics, namespace and network access |
| ECS container stdout/stderr to CloudWatch | awslogs task log configuration | ECS/log delivery role and group/stream configuration |
| ECS multi-destination/transformed logs | FireLens log router | Task role for router destinations; router resources/configuration |
| Remote command/configuration operations | Systems Manager Agent | Managed-node registration/role/service connectivity |

Installing an agent does not automatically collect every service/application metric. Define the needed measurements and log paths; deploy and verify configuration consistently, including ASG replacements.

**CloudWatch agent is not required merely to use ECS awslogs.** Fargate does not expose an EC2 host for installing a host agent. On EC2, confirm the ECS agent/driver support and configured instance/execution-role behavior.

## Task-definition fragment

```json
{
  "logConfiguration": {
    "logDriver": "awslogs",
    "options": {
      "awslogs-group": "/ecs/payments",
      "awslogs-region": "us-east-1",
      "awslogs-stream-prefix": "service",
      "mode": "blocking"
    }
  }
}
```

This is a fragment, not a complete task definition. Precreate the log group and set retention/encryption, or authorize group creation deliberately. Stream prefix is required for Fargate and useful on EC2 for identifying task/container logs.

Fargate awslogs uses the task execution role for log delivery; application API calls use the task role. FireLens runs in the task and needs task-role permissions for its destinations. Never solve this by broadly granting every role all logging/storage permissions.

## Backpressure trade-off

Current ECS default log-driver mode is non-blocking unless configured otherwise. A full buffer can drop logs. Blocking mode can stall the application during log-delivery problems. Set the mode explicitly according to audit/availability requirements; blocking is not an end-to-end guarantee that every log reaches every later destination.

Plan multiline handling, volume, sensitive-data redaction, network endpoints, container startup and monitoring. Do not route the log router's own diagnostics recursively through itself.

## S3 requirement

awslogs sends to CloudWatch Logs, not directly to S3. Use a subscription to [[Amazon Data Firehose]] for buffered S3 delivery, or a deliberate FireLens route. ALB access logs use their own S3 delivery configuration.

Tasks 4.1 and 4.3. See [[Domain 4 Scenario Decisions]], [[Amazon ECS]], [[AWS Fargate]].

- [ECS log-driver account settings](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html)
- [ECS log options](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/ECS/Types/LogConfiguration.html)
- [Host memory/disk custom metrics](https://repost.aws/knowledge-center/cloudwatch-memory-metrics-ec2)
