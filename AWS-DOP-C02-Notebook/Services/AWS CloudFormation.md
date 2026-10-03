---
title: AWS CloudFormation
tags:
  - aws
  - dop-c02
  - service
status: consolidated-study-note
updated: 2026-10-03
read: false
---

# AWS CloudFormation

Declarative provisioning and lifecycle management of AWS infrastructure.

## Exam mapping

Task statements: 1.4, 2.1. See [[Domain 1 - SDLC Automation]] and [[Domain 2 - Configuration Management and IaC]].

## Core components and behavior

Templates define stacks; parameters customize deployments; outputs expose values. Nested stacks reuse templates; change sets preview creates, updates, and replacements. Drift detection covers supported resources and properties, not every possible out-of-band change.

## Architecture pattern

Source-controlled template → [[AWS CodePipeline]] creates change set → review/approval → execute → monitor stack events.

## Adding custom resources

A custom resource extends a stack with provisioning logic that a native CloudFormation resource type does not provide. Declare it as `Custom::<TypeName>` or `AWS::CloudFormation::CustomResource`, and point its required `ServiceToken` to a Lambda function or SNS topic in the **same Region** as the stack.

### End-to-end process

1. **Choose the extension model.** Use a custom resource for focused stack-time logic without registering a type. Prefer a CloudFormation registry resource type when you need a reusable first-class type with `Create`, `Read`, `Update`, `Delete`, and `List` handlers and drift detection.
2. **Define the provider contract.** Decide the input properties, returned `Data` attributes, stable physical identifier, update/replacement behavior, and deletion semantics before writing the template.
3. **Implement an idempotent provider.** Handle `Create`, `Update`, and `Delete`. Expect retries and partial work; use the request and existing physical ID to avoid duplicate resources. A delete handler should succeed when the external resource is already absent.
4. **Deploy the provider.** Create the Lambda function or SNS-backed listener, grant only the downstream permissions its logic requires, and ensure it can reach both target APIs and the presigned response URL. The provider can be defined in the same template or deployed separately.
5. **Declare the custom resource.** Set `ServiceToken`, an appropriate `ServiceTimeout`, and provider-specific properties. References such as `!GetAtt ProviderFunction.Arn` also establish the dependency on an in-template provider.
6. **Return exactly one response.** For every request path—including caught exceptions—the provider must PUT a `SUCCESS` or `FAILED` response to the request's presigned S3 `ResponseURL`. CloudFormation remains waiting until that response arrives or the operation times out.
7. **Test the full lifecycle.** Exercise create, in-place update, replacement update, delete, failed create and rollback. Validate the provider logs and stack events; template linting cannot prove that the runtime callback works.

### Template side

```yaml
Resources:
  ExternalWidget:
    Type: Custom::ExternalWidget
    Properties:
      ServiceToken: !GetAtt CustomResourceFunction.Arn
      ServiceTimeout: 300
      Name: !Sub "${AWS::StackName}-widget"
      Mode: managed

Outputs:
  WidgetId:
    Description: Identifier returned by the custom resource provider
    Value: !GetAtt ExternalWidget.WidgetId
```

`ServiceTimeout` is 1–3600 seconds and defaults to 3600. Set it long enough for the operation but short enough to fail promptly when the provider is broken. Properties besides `ServiceToken` and `ServiceTimeout` are the provider-defined request payload. Values returned under response `Data` are available through `Fn::GetAtt`.

### Request and response lifecycle

| Stack operation | Request details | Provider responsibility |
|---|---|---|
| Create | `RequestType: Create` and `ResourceProperties` | Create or locate the resource, return `SUCCESS` and a stable `PhysicalResourceId` |
| Update with changed properties | `RequestType: Update`, new and old properties, existing physical ID | Update in place and return the same ID, or return a new ID to signal replacement |
| Delete, rollback, or replacement cleanup | `RequestType: Delete`, properties and physical ID | Idempotently remove or release the resource and respond even if it is already absent |

Every response includes `Status`, `RequestId`, `StackId`, `LogicalResourceId`, and `PhysicalResourceId`; copy the request identifiers exactly. `FAILED` responses should include a useful `Reason`. `Data` and `NoEcho` are optional. Use `NoEcho` for sensitive response data, but do not put secrets in template properties, metadata, or stack outputs.

The physical ID controls lifecycle semantics:

- Return a stable ID from `Create` and ordinary `Update` calls to keep one logical resource associated with the same external object.
- Return a different ID from `Update` only when replacement is intentional. CloudFormation treats the new ID as the replacement and later sends `Delete` for the old physical ID.
- Never generate a fresh ID on every update accidentally; that creates replacements and cleanup requests.

### Provider safety and troubleshooting

- Scope the Lambda execution role or subscriber credentials to the APIs and resources the provider actually manages. The stack execution role and provider execution role are separate authorization boundaries.
- Do not log secrets from `ResourceProperties`, old properties, or response data. `NoEcho` masks supported CloudFormation displays; it is not a general log or output-redaction system.
- If a VPC-attached provider cannot reach the presigned S3 response URL, the function can finish while the stack waits and eventually times out. Provide NAT or an appropriate S3 endpoint path; restrictive endpoint policies must permit the regional `cloudformation-custom-resource-response-<region>` bucket.
- Use a deterministic client token or lookup before creation where the downstream API supports it. Record enough state in the physical ID or an external store to complete later update/delete requests.
- A custom-resource failure participates in normal stack rollback. The provider must therefore tolerate a `Delete` after a partially completed or failed `Create`.
- Start troubleshooting with the custom resource's stack event, then correlate the request ID with provider logs. “No response” commonly points to an uncaught exception, malformed callback body, blocked network path, or timeout.

> [!exam]
> `ServiceToken` selects the provider; it is not the external resource itself. CloudFormation sends lifecycle requests and waits for the callback. A Lambda invocation that returns normally without sending the required response does **not** complete the custom resource.

## IAM and security

Separate pipeline/action roles from the CloudFormation execution role; scope iam:PassRole. A stack policy restricts updates through CloudFormation, not direct API changes.

## Failure, rollback, and lifecycle

Creation/update failures normally trigger rollback, subject to configured options. DeletionPolicy controls stack deletion/removal; UpdateReplacePolicy controls the old resource after replacement. Retain/Snapshot do not prevent every replacement.

## When to choose

> [!exam]
> Choose for repeatable, versioned infrastructure and dependency-aware updates.

## Do not confuse with and exam traps

> [!warning]
> A change set predicts operations, not successful execution. Parameter changes alone do not refresh running fleets.

## Official AWS references

- [AWS CloudFormation official reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
- [Create custom provisioning logic with custom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html)
- [Custom resource request and response reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref.html)
- [Lambda-backed custom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources-lambda.html)
- [CloudFormation registry resource types](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html)
- [[Official AWS Sources]] — source inventory and verification scope.

## Domain 3 — repeatable recovery infrastructure

Deploy a compatible regional application stack from templates, with explicit regional images, keys, secrets, networking and data endpoints. Desired ASG capacity must fit quotas and tested recovery timing.

Updating RDS EngineVersion is an infrastructure operation, not a guarantee of short downtime. Review [[Amazon RDS]] engine/topology upgrade behavior and [[RDS Blue Green vs EngineVersion Update vs Read Replica Promotion]].

Use supported stack drift detection, but it does not inspect every runtime setting or prove data freshness/recovery. Tasks 3.1 and 3.3. See [[Disaster Recovery Testing and Failback]].

## Domain 5 — failed deployments and repair

Start with stack events and the failing logical resource/status reason; correlate recent changes, IAM, quotas/capacity and downstream dependencies. An automated retry or rollback can fail for the same underlying condition.

Document whether a proposed response changes, replaces or deletes resources, and preserve persistent data. Supported drift checks evaluate infrastructure state, not the entire application incident.

Task 5.3. [[CI-CD Failure Triage and Parallel Actions]], [[Incident Response Workflow and Evidence Preservation]].

## Domain 6 — security and drift

Use templates to encode reviewed security controls and drift detection to compare supported stack resources with expected configuration. Drift is not a vulnerability scan or complete application audit. Protect deployment roles, review change sets, and avoid plaintext secrets in templates/parameters.

Tasks 6.2–6.3. [[Domain 6 Monitoring Auditing and Compliance]], [[AWS Config]], [[AWS Service Catalog]].
