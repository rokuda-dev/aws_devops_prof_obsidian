---
tags: [aws, dop-c02, sources]
updated: 2026-09-20
read: false
---

# Verification Ledger

## Verification scope — September 18, 2026

| Item | Check completed |
|---|---|
| Exam domains/weights | Current official DOP-C02 guide read |
| Domain 1 tasks | Official statements 1.1–1.4 read |
| Domain 2 tasks | Official statements 2.1–2.3 read |
| CodeCommit status | Current document history and official return announcement checked |
| X-Ray SDK/daemon status | Current support timeline checked |
| Beanstalk modes | Current concepts and September 17, 2026 release checked |
| ECS-native strategies | Updated official comparison and container guidance checked |
| DynamoDB global consistency | Official MREC/MRSC operational readiness guidance checked |
| Aurora topology/recovery/current limit | Current Global Database overview read |
| ADS collection/availability | Current overview read; new-customer closure recorded |
| Kinesis SQL retirement | Current documentation discontinuation notice checked |
| OpsWorks Stacks retirement | Official end-of-life/migration announcement checked |
| CodeBuild reports | Current reporting retention and report-group behavior checked |
| CodeDeploy platform limits | On-premises blue/green exclusion, ECS NLB traffic limits, and EC2 success thresholds checked |
| CloudFront | Origin failover behavior/method limits and field-encryption requirements checked |
| Organization Config remediation | Official AWS response/conformance-pack architectures checked |
| Patch organization coverage | Quick Setup patch-policy documentation checked |
| Security Hub/CSPM naming | Current official distinction checked |

## How to interpret references

Every service note provides an official starting reference. A listed reference is not a claim that every linked page was read in full during this session. Stable service summaries were consolidated from the existing draft, provided review, AWS guidance, and targeted current-document checks; time-sensitive changes and important disputed behavior received explicit checks above.

Current-product facts are not predictions of exam refresh timing. Avoid unnecessary memorization of quotas, runtimes, or recently announced features without scenario relevance.

## Future verification triggers

- If a complete unseen earlier ZIP is later supplied, compare it before claiming byte-for-byte historical consolidation.
- Recheck current-service status and platform-specific limitations whenever the notebook is updated.

## Domain 3 verification — v1.1

Targeted official checks covered task statements 3.1–3.3; classic RDS versus Multi-AZ cluster upgrades; MySQL replica ordering and Blue/Green; RDS event delay/order; ALB/NLB cross-zone behavior, weighted groups and health thresholds; ASG timing/warm-pool events; DynamoDB capacity and DAX consistency; EKS pod/node scaling and Fargate allocation; Regional APIs/SAM build containers; Route 53 and Global Accelerator boundaries; ARC current capabilities/promotion; DRS; continuous backup copies/encryption/restore validation; S3 RTC/Batch Replication; ECR and transit gateway peering.

Sources and corrections: [[Domain 3 Official Sources]], [[Domain 3 Transcript Corrections]]. Earlier v1.0 checks above are retained as historical evidence, not claimed as newly rechecked during the Domain 3 update.

## Domain 4 verification — v1.2

Checked official task statements 4.1–4.3 and all seven supplied resources. Targeted checks covered metric identity/statistic sets/agent namespace; Firehose cross-account subscriptions; native log centralization/new-data scope; forwarding errors/retries; direct CloudWatch Logs Firehose/OpenSearch limitation; metric-stream transport/account/Region; discovered fields/log class; ECS current log mode/options; ALB legacy versus enhanced logging notice; default CloudTrail history/organization scope/API matching/digests; cloudtrail-enabled periodic trigger; GuardDuty native findings export; Macie scope; Health/recovery eligibility; Trusted Advisor refresh events; SSM data-sync types; REST API/EventBridge tracing; Quick Suite BI naming; unsupported dashboard solution and Inspector Classic retirement.

Evidence: [[Domain 4 Official Sources]], [[Domain 4 Transcript Corrections]]. Earlier release checks remain historical/carry-forward evidence, not claims of new reads. No AWS resource actions were executed.

## Domain 5 verification — v1.3

Checked official tasks 5.1–5.3 and all six supplied links, including the Lambda link's current Scheduler redirect and RefreshCache asynchronous inventory semantics. Targeted checks covered EventBridge rule target enumeration; Health exposed-key event origin/schema and current containment guidance; Config Lambda/Guard evaluation and SSM state-machine bridge; S3 Object Ownership/data-event scope; DDoS layer/mitigation and origin restrictions; CodeDeploy platform-specific hooks/callback; same-stage CodePipeline runOrder; healthy-host configuration; Container Insights collection setup and synthetic trace correlation; Fleet Manager prerequisites/OpsCenter distinction; Dedicated Host evidence/license groups; restricted-ssh exact behavior; OpsWorks retirement.

See [[Domain 5 Official Sources]], [[Domain 5 Transcript Corrections]]. Previous-release evidence remains carried forward where not newly checked. No AWS account mutations or credential retrieval occurred.

## Domain 6 verification — v1.4

Checked official tasks 6.1–6.3 and all six supplied links. Targeted checks covered temporary identity choices; Roles Anywhere/Cognito federation; current CodeCommitPowerUser permissions; boundaries/resource-policy exceptions; ABAC/SCP scope; private EC2-to-S3 layers; cross-account Automation; Security Hub/Firewall Manager scope; Macie pipeline limits; Secrets Manager rotation and Parameter Store integration; S3/EBS/RDS encryption; KMS data keys and CloudHSM validation; ACM export; approved AMIs, Inspector Classic retirement and Audit Manager availability.

Evidence: [[Domain 6 Official Sources]], [[Domain 6 Transcript Corrections]]. Earlier-release evidence remains carry-forward evidence where not newly checked. No AWS account mutations or credential retrieval occurred.

## v1.4.1 correction verification

Rechecked the current ARC readiness-check availability notice, S3 private-subnet connectivity alternatives, IAM permissions-boundary/resource-policy distinctions, and RDS encrypted-snapshot workflow against official AWS documentation. Removed all stale current-version “Domain 6 unfinished” statements while retaining the historically correct v1.3 changelog entry. Added task 6 sections to shared service pages and reran active-link, heading-target, duplicate-basename, front-matter, preservation and archive-integrity checks.

## v1.4.2 consolidated-review verification

Rechecked the time-sensitive CodeCommit new-customer return, X-Ray SDK/daemon maintenance status, Inspector Classic end of support, Audit Manager and ARC readiness-check availability changes, Elastic Beanstalk Cluster Mode release, and Kinesis Data Analytics for SQL discontinuation against current official AWS documentation on September 19, 2026.

Compared the consolidated exam summaries with the Domain 3–6 architecture, scenario-decision, transcript-correction, task-index, and official-source notes. Replaced link-only expansion blocks with in-file decision tables, traps, patterns, and rapid-review cues. A vault-wide scan then checked for remaining expansion placeholders, stale completion statements, missing front matter, duplicate basenames, unresolved wiki links and headings, and accidental file removal. No AWS account actions, credential access, or secret retrieval occurred.

## v1.4.4 all-domain normalization verification

Reviewed the start page, domain coverage map, all six domain indexes, exam summary notes, service notes, source index, provenance, and roadmap for current language or structure that assigned Domains 3–6 a separate expansion, release, or transcript-completion status. Normalized current study navigation across Domains 1–6 and retained source-specific history only in provenance and historical changelog records. A fresh vault-wide validation checked Boolean read properties, YAML, active wiki links and headings, duplicate basenames and headings, the intentional roadmap rename, residual current-status language, and ZIP integrity. No AWS account actions, credential access, or secret retrieval occurred.

## v1.4.5 page-by-page completeness audit — 2026-09-20

Read all 209 Markdown notes across the start page, service index, Domains, Services, Concepts, Comparisons, Exam, and Sources sections. The audit evaluated each written claim, tables and enumerations that implied a complete set, cross-note consistency, current-product statements, and exam-relevant omissions. A vault-wide strong-claim/enumeration scan was used to revisit wording such as “all,” “only,” “must,” “complete,” and “every”; it did not substitute for the manual page review.

Corrections completed in this release:

- Replaced the incomplete CodeDeploy hook-variable list with the five always-available variables and the applicable S3/GitHub bundle variables.
- Listed all nine scriptable EC2/on-premises lifecycle hooks and separated the four reserved agent lifecycle events.
- Corrected the CodePipeline minimum-stage statement and added the official action-requirements reference.
- Corrected the resource-policy comparison from an unconditional grant statement to a service- and principal-sensitive capability.
- Rebuilt the Service Index so all 99 service pages are accounted for in one canonical catalog or an explicit compatibility-navigation table, without domain-era “additions” sections.

Time-sensitive checks covered CodeCommit’s November 2025 return for new customers, the X-Ray SDK/daemon maintenance boundary, Application Discovery Service’s new-customer closure, Kinesis Data Analytics for SQL discontinuation, Inspector Classic retirement, Audit Manager and ARC readiness-check availability, and the current Elastic Beanstalk mode distinction. Final validation checked all notes, YAML and preserved Boolean read values (11 `true`, 198 `false`), duplicate basenames/headings, active wiki links and heading targets, table structure, source domains, and prior-file preservation. It also compared all 10 `.obsidian` files byte-for-byte with the user-edited v1.4.4 baseline, verified the enabled `explorer-property-attributes` plugin and its v1.3.2 manifest identity, and tested ZIP integrity. No AWS account actions, credential access, or secret retrieval occurred.
