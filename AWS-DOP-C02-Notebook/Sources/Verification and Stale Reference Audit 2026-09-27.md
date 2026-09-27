---
tags: [aws, dop-c02, audit, sources]
updated: 2026-09-27
read: false
---

# Verification and Stale Reference Audit 2026-09-27

## Result and scope

Reviewed the **209 existing Markdown pages** in the working notebook, using its recorded v1.4.5 validation as provenance and preserving subsequent user edits. No notebook ZIP was present. This run adds four audit notes, bringing the working vault to **213 notes**, including the same 99 service pages.

This is a page-by-page review with **targeted current verification of material claims**, a vault-wide reference scan, and structural validation. It is not a claim that every sentence, regional configuration, quota, or linked AWS document was independently reverified. Navigation and provenance pages receive the appropriate structural/historical review rather than an artificial technical “pass.” Original transcripts and prior release ZIPs were not available for an independent provenance comparison.

| Coverage group | Existing pages | Record |
|---|---:|---|
| Amazon and related service pages | 45 | [[Audit Amazon Services 2026-09-27]] |
| Other AWS services and comparisons | 84 | [[Audit Delivery and Comparisons 2026-09-27]] |
| Concepts and domain study paths | 46 | [[Audit Concepts and Domains 2026-09-27]] |
| Exam summaries, navigation and source records | 34 | Page table below |
| Total baseline coverage | 209 | Every baseline filename retained |

The official blueprint remains Domain 1 **22%**, Domain 2 **17%**, Domain 3 **15%**, Domain 4 **15%**, Domain 5 **14%**, and Domain 6 **17%**. Task ranges remain 1.1–1.4 and 2.1–6.3 (three tasks in each of Domains 2–6). [Official exam guide](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02.html). Full task-level mapping is in [[All-Domain Study Roadmap]]; Domain 1 headings were expanded to the official wording.

## Findings organized by exam domain

| Domain / tasks | Finding and resulting exam judgment | Evidence and affected notes |
|---|---|---|
| 1 — 1.1 | CodePipeline's V2 Commands action runs shell commands on managed CodeBuild compute without a separately created project. Do not eliminate it using an absolute “orchestrators cannot execute commands” rule. | [Commands reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-Commands.html); [[AWS CodePipeline]], [[CodePipeline vs CodeBuild vs CodeDeploy]] |
| 1 — 1.1 | Cross-Region artifact buckets and keys belong in the pipeline account and action Region. Cross-account artifacts cannot move directly between two non-pipeline accounts. Prefer the full KMS key ARN. | [Cross-Region](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-create-cross-region.html), [cross-account](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create-cross-account.html); [[Cross-Account and Cross-Region CodePipeline]] |
| 1 — 1.3 | The grouped ECR/Image Builder note linked its ECR subsection to CodePipeline. Corrected the target. | Local navigation correction in [[Amazon ECR and EC2 Image Builder]] |
| 1 / 3 — 1.4, 3.1 | Added the OPTIONS cached-method prerequisite to CloudFront origin failover. Failover remains restricted to GET/HEAD/OPTIONS and configured failure conditions. | [Origin failover](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html); [[Amazon CloudFront]] |
| 2 — 2.1 | Domain index named Application Discovery Service without its new-customer restriction. Added the closure and AWS Transform direction. | [Availability notice](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html); [[Domain 2 - Configuration Management and IaC]] |
| 3 — 3.3 | RTO/RPO were expanded as “Return.” Corrected to **Recovery Time Objective** and **Recovery Point Objective**. | [AWS recovery definitions](https://docs.aws.amazon.com/drs/latest/userguide/CloudEndure-Concepts.html); [[RTO RPO SLA SLO and Error Budgets]] |
| 4 — 4.1–4.2 | “Quick Suite” was stale current naming. The current umbrella is **Amazon Quick**, with **Amazon Quick Sight** for BI; existing API/SDK integrations retain compatibility. Kept the familiar filename. | [Current product guide](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html); [[Amazon QuickSight]], [[Service Index]], [[Domain 4 Official Sources]] |
| 4 / 6 — 4.1–4.2, 6.3 | CloudTrail Lake closed to new customers May 31, 2026. Added a caveat specifically for Lake; ordinary trails remain supported. | [Lake availability](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html); [[AWS CloudTrail]] |
| 4 — 4.2–4.3 | Native log alarms can run scheduled Logs Insights queries without metric filters. Added this alternative; a one-time query still creates no continuous alarm. | [Alarm types](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html); [[Amazon CloudWatch]], [[Log Subscription vs Metric Filter vs EventBridge Rule]] |
| 5 — 5.2 | From March 26, 2026, AWS WAF Anti-DDoS managed rules supersede legacy Shield L7 automatic mitigation as the default HTTP flood solution. Existing legacy support and new-customer access differ. This does not mean a subscription automatically configures protection. | [Current transition](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-automatic-app-layer-response.html); [[AWS Shield]], [[AWS WAF]], [[DDoS Mitigation and Attack Surface Reduction]], comparison and summaries |
| 6 — 6.2 | Bucket defaults do not migrate existing objects. Eligible existing encrypted objects can use UpdateObjectEncryption without copying data; Object Lock, source encryption and replication restrictions matter. Added current option without changing the default-encryption distinction. | [Encryption update contract](https://docs.aws.amazon.com/AmazonS3/latest/userguide/update-sse-encryption.html); [[Amazon S3]] |
| 6 — 6.2 | Not every Secrets Manager rotation requires a Lambda function. Clarified managed/external-secret methods versus Lambda-based rotation. | [Rotation methods](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html); [[AWS Secrets Manager]] |

Exam summaries in [[Common Traps and Current Corrections]] and [[Rapid Review]] now reflect the material changes. Current product announcements do not establish when an exam question bank changes.

## Important existing corrections retained

The reviews retained CodeCommit's November 2025 return, X-Ray SDK/daemon maintenance versus supported tracing service, ECS-native traffic-shifting distinctions, Beanstalk Cluster Mode, DynamoDB MREC/MRSC versus Aurora single-writer semantics, Inspector Classic retirement, Audit Manager setup restrictions, ARC readiness-check restrictions, and the direct CloudWatch Logs → Firehose → OpenSearch limitation. Evidence is in the component reports and canonical notes.

ARC's precise April 30, 2026 closure date was initially unresolved in the service review; the integrating check confirmed it in [ARC document history](https://docs.aws.amazon.com/r53recovery/latest/dg/doc-history.html).

AWS sources can disagree: the indexed X-Ray PDF still describes a February 2027 end date, while the dedicated current [SDK/daemon support timeline](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-daemon-timeline.html) has maintenance from February 25, 2026 with no end date listed. The notebook follows that dedicated current timeline; it does not invent a service retirement date. Historical event examples and blogs are retained as context, not used to override current API/lifecycle pages.

## External reference findings

The automated HTTP scan retrieves status, final destination and page title. That detects HTTP failures and redirects; it does **not** prove the source supports the surrounding claim. Search/documentation reads supplied technical evidence separately.

| Reference problem | Resolution |
|---|---|
| Inspector Classic migration, overview and PDF URLs returned HTTP 404 in direct checks | **Unresolved source availability:** AWS search still exposes the [Classic PDF end-of-support notice](https://docs.aws.amazon.com/pdfs/inspector/v1/userguide/inspector-ug.pdf), including May 20, 2026. Retained this evidence link with the failure disclosed; it is not a repaired live reference. |
| Secrets Manager rotate-secrets URL redirected to a generic guide landing page | Replaced with [rotation methods](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) |
| Old CodePipeline connections and Lambda@Edge locations redirected | Updated study/source links to their current Developer Tools and CloudFront locations |
| DDoS welcome URL redirected to guide root | Added the [current whitepaper body](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-best-practices-ddos-resiliency.html); preserved the supplied historical URL in provenance |
| Supplied Lambda/EventBridge link now targets Scheduler | Retained original in provenance with the existing scheduling-versus-event-routing explanation |
| Supplied Systems Manager compliance URL redirects | Preserved supplied URL and documented canonical destination; a redirect is not automatically a broken reference |

Machine-readable results are in repository folder `audit/`; repeat the read-only structural check with `python scripts/verify_notebook.py --baseline audit/baseline-2026-09-27.json --output audit/structure-2026-09-27.json`. Add `--http` and a separate output filename to check external references. The tool requires network access for HTTP checks. It does not contact an AWS account.

## Exam, navigation and source page coverage

For scenario pages, verification focuses on decisive service boundaries and cross-note consistency using the linked service/concept audit evidence. Historical transcript coverage is preserved, not independently reconstructed.

| Page | Review performed / result |
|---|---|
| [[00 - Start Here]] | Weights/navigation checked; corrected local vault folder name; linked this report |
| [[Service Index]] | All 99 service files checked for one first-column entry; current Quick naming updated |
| [[Common Traps and Current Corrections]] | Lifecycle/integration traps checked; current findings propagated |
| [[Cross-Account and Cross-Region CodePipeline]] | Direct AWS cross-account/Region contract read; clarified ownership and artifact limits |
| [[Domain 3 Architecture Patterns]] | Replica promotion versus routing, cache versus durability and restore validation checked against canonical reviews |
| [[Domain 3 Scenario Decisions]] | RTO/RPO reasoning, supported endpoint choice and conditional recovery judgments retained |
| [[Domain 3 Transcript Corrections]] | High-risk scaling/DR/copy distinctions compared with reviewed services; historical transcript attribution not reverified |
| [[Domain 4 Architecture Patterns]] | Copied versus federated logs, data events, transport and remediation boundaries retained |
| [[Domain 4 Scenario Decisions]] | ECS/ALB collection paths and StopLogging versus Config trigger distinction checked |
| [[Domain 4 Transcript Corrections]] | Firehose restriction, ECS log default, CloudTrail scope and Classic retirement checked against canonical reviews |
| [[Domain 5 Architecture Patterns]] | Accepted event delivery differs from completed workflow; bounded incident pattern retained |
| [[Domain 5 Scenario Decisions]] | Hook callback, SIGKILL interpretation, SSM roles and RefreshCache API distinction checked |
| [[Domain 5 Transcript Corrections]] | SSH rule scope, event contracts, API actor versus configuration distinctions checked |
| [[Domain 6 Architecture Patterns]] | Identity, classification versus release enforcement, encryption and response-role distinctions retained |
| [[Domain 6 Scenario Decisions]] | Direct RDS encryption guide checked; retained encrypted-copy/restore workflow and scope caveats |
| [[Domain 6 Transcript Corrections]] | Current IAM/key/certificate/lifecycle distinctions checked against reviewed canonical notes |
| [[Domain Coverage and Service Map]] | Domain weights/task ranges checked; cross-domain role table reviewed |
| [[High-Value Exam Patterns]] | Compared with corrected services; generic scenario patterns remain applicable |
| [[Notebook Validation]] | Historical release checks retained and clearly separated from this run's narrower validation |
| [[Rapid Review]] | Material Commands, log alarm, Lake, WAF and S3 updates propagated |
| [[Service Selection Matrix]] | Service-choice cues compared with canonical reviews; no unconditional new-customer Lake/legacy L7 recommendation |
| [[Domain 3 Official Sources]] | Source inventory read; URLs included in HTTP scan; targeted technical evidence in component reports |
| [[Domain 3 Transcript Coverage]] | Provenance/coverage limits and links checked; original absent walkthrough not reconstructed |
| [[Domain 4 Official Sources]] | Repaired Inspector reference and current Quick naming evidence; URLs scanned |
| [[Domain 4 Transcript Coverage]] | Historical processing claims retained as provenance; current links checked |
| [[Domain 5 Official Sources]] | Added current WAF transition and DDoS body; preserved original supplied links |
| [[Domain 5 Transcript Coverage]] | Blank resource and absent walkthrough remain explicit; navigation checked |
| [[Domain 6 Official Sources]] | Added general rotation methods and current S3 encryption update evidence |
| [[Domain 6 Transcript Coverage]] | Provenance and absent walkthrough retained; navigation checked |
| [[Imported Domain 1 Index]] | Historical fenced import preserved; fenced links excluded from active-link validation |
| [[Notebook Changelog]] | Added dated audit entry; historical releases retained |
| [[Notebook Provenance and Progress]] | Identified current Markdown baseline and audit scope; historical archive claims not re-proved |
| [[Official AWS Sources]] | Updated stale target URLs; current sources take precedence over transcript wording |
| [[Verification Ledger]] | Added dated audit scope and evidence links without relabeling older reads as current |

## Validation and remaining limits

Final HTTP results: **291 of 292 unique URLs returned HTTP 200**, including three documented redirects. The Inspector Classic PDF returned HTTP 404 despite being available through indexed AWS search evidence. Structural checks found no errors across **2,081 active wiki links**. HTTP success alone does not establish technical correctness.

- All original note paths and captured Boolean read states are checked against `audit/baseline-2026-09-27.json`; the baseline contains **76 read / 133 unread** notes, reflecting the user's current study progress rather than the old release's 11/198 split.
- Active wiki targets and heading targets, duplicate note basenames/headings, frontmatter delimiters/duplicate keys/read flags, and the Service Index are checked by the script. It does not perform full YAML parsing or Obsidian plugin runtime testing.
- `.obsidian/workspace.json` changed during the session; the audit does not overwrite it or claim byte-for-byte preservation of that live UI file. Other captured plugin/configuration hashes are compared. No user source note was removed or reset.
- Exact engine/runtime/Region feature matrices, account-specific quotas, security-policy correctness for a deployed architecture, and performance/recovery guarantees remain scenario-specific checks. An overview reference does not validate every such detail.
- The exposed-key workflow is a historical AWS example, not evidence that every exposure generates an event or that its old implementation should be deployed unchanged.
- Full original transcript/ZIP fidelity, cloud behavior, and archive integrity were not retested. No new notebook release ZIP or AWS deployment is claimed by this check run.

Final machine counts and HTTP outcomes are recorded in [[Notebook Validation]].
