---
tags: [aws, dop-c02, sources]
updated: 2026-09-20
read: false
---

# Notebook Changelog

## v1.4.5 — 2026-09-20 — page-by-page completeness audit

- Read and audited all 209 notes, validating every written claim and every list whose wording or structure implied completeness; added exam-relevant omissions without turning the notebook into exhaustive service documentation.
- Completed the EC2/on-premises CodeDeploy hook and environment-variable sets, including the traffic hooks, reserved agent events, and S3/GitHub bundle-source variables.
- Corrected CodePipeline’s minimum-stage wording: a source action and an additional stage are required, but the later stage is not limited to Build or Deploy.
- Corrected the resource-policy comparison so it does not imply every resource policy always grants access, and rebuilt the Service Index as one uniform alphabetical catalog plus explicit compatibility-navigation pages.
- Rebased the release on the user-edited v1.4.4 task archive, preserving all 11 `read: true` states, the other 198 `read: false` states, and the configured **Mark as Read** plugin (`explorer-property-attributes` v1.3.2) with its `.obsidian` configuration.
- Rechecked time-sensitive service status against current first-party AWS material and reran metadata, link, heading, table, preservation, source-domain, and archive-integrity validation.

## v1.4.4 — 2026-09-19 — all-domain normalization release

- Removed current navigation and study-status language that treated Domains 3–6 as a separate expansion or transcript-processing tier.
- Replaced the Domains 3–6 expansion roadmap with an all-domain roadmap covering Domains 1–6 consistently.
- Added explicit Domain 1 and Domain 2 sections to High-Value Exam Patterns, Common Traps and Current Corrections, Rapid Review, Service Selection Matrix, and the start-page study paths.
- Moved source-collection caveats out of primary domain study pages while retaining factual provenance in the Sources notes.
- Preserved the Boolean `read: false` property on every page and revalidated active wiki links, heading targets, YAML, duplicate names/headings, filenames, and archive integrity.

## v1.4.3 — 2026-09-19 — read-tracking release

- Added the Boolean YAML property `read: false` to all 209 Markdown notes so Obsidian displays an unchecked read toggle on every page.
- Preserved every v1.4.2 filename, note body, internal link target, heading target, and existing front-matter property.
- Revalidated YAML types, exactly one read property per note, internal links/headings, duplicate names/headings, prior-file preservation, and ZIP integrity.

## v1.4.2 — 2026-09-19 — consolidated final-review release

- Replaced every link-only Domain 3–5 expansion block in the exam summary layer with substantive in-file coverage and added complete Domain 6 sections.
- Expanded High-Value Exam Patterns, Common Traps and Current Corrections, Rapid Review, and Service Selection Matrix for all six domains.
- Converted the Domains 3–6 expansion roadmap from navigation-only text into task-level decision summaries while preserving its filename and links.
- Added representative Domain 3–6 evidence directly to the consolidated official-sources note instead of using a link-only source expansion.
- Rechecked time-sensitive service corrections against current official AWS sources and reran full-vault placeholder, status, front-matter, duplicate-name, wiki-link, heading-target, preservation, and ZIP-integrity validation.

## v1.4.1 — 2026-09-19 — validated correction release

- Removed 30 stale current-version statements across 27 notes that incorrectly said Domain 6 was unfinished; retained the historical v1.3 changelog statement.
- Added the April 30, 2026 ARC readiness-check new-customer availability caveat.
- Clarified that private EC2-to-S3 connectivity can use a gateway endpoint, interface endpoint, or NAT-backed path; an endpoint policy does not replace IAM/bucket authorization.
- Added Domain 6-specific sections to shared IAM, governance, security, storage, audit, remediation, deployment and classification service pages.
- Rechecked the corrected claims against current official AWS documentation and reran notebook, preservation and archive validation.

## v1.4 — 2026-09-19 — Domain 6

- Processed supplied tasks 6.1–6.3 and retained all six additional resource URLs.
- Added canonical service notes, task reviews, comparisons, scenario decisions, architecture patterns, corrections and source coverage.
- Preserved all 184 prior notes, filenames and heading targets.
- Corrected federation, CodeCommit policy, permissions-boundary, Macie, secret retrieval, encryption, KMS/CloudHSM, ACM, Inspector Classic and Audit Manager shortcuts.
- The eleventh walkthrough question was not supplied and was not invented.

## v1.3 — 2026-09-18 — Domain 5

- Processed supplied tasks 5.1–5.3 and preserved all six resource URLs; blank resource 7 remains unfilled.
- Added five canonical services, 14 concepts/features, six comparisons, three exam aids, and two coverage/source notes.
- Preserved all 154 prior notes, filenames and heading targets; enriched shared services and navigation.
- Clarified actor auditing versus configuration compliance, event targets, exposed-key containment versus preventive scanning, DDoS control layers, Lambda hooks/callbacks, TLS and container triage, host licensing, and SSH remediation safety.
- Ninth walkthrough question was not supplied. Domain 6 remains unfinished.

## v1.2 — 2026-09-18 — Domain 4

- Processed supplied tasks 4.1–4.3 and preserved all seven additional resources.
- Added nine missing service notes, ten feature/concept notes, six comparisons, three exam aids, and two coverage/source notes.
- Enriched existing canonical services and retained all 124 prior notes, their filenames and heading targets.
- Corrected cross-account subscription options, Firehose/OpenSearch restrictions, CloudTrail scope/integrity, ECS role/driver setup, periodic Config versus API-event detection, SQS health wording and unsafe termination shortcuts.
- Identified unsupported DevOps Monitoring Dashboard and retired Inspector Classic/OpsWorks context.
- Completed ECS-to-S3 design; updated navigation/rapid review/provenance. Domains 5–6 remain unfinished.

## v1.1 — 2026-09-18 — Domain 3

- Processed the supplied transcript for tasks 3.1–3.3 and retained all six additional resources.
- Added 14 canonical services, six concepts, six comparisons, three exam aids, and two source/coverage notes.
- Enriched existing shared-service notes without renaming notes or deleting prior study content.
- Distinguished RDS upgrade topology/Blue-Green, replica promotion versus DNS routing, EKS pod/node scaling, NLB health thresholds, and backup/S3 replication limitations.
- Updated indexes, rapid review, provenance, and verification evidence. Domains 4–6 remain unfinished.

## v1.0 — 2026-09-18

- First packaged, downloadable notebook from this consolidation workflow.
- Preserved existing draft filenames and converted grouped services to navigation.
- Added individual canonical service notes, shared concepts, comparison tables, exam patterns, rapid review, source/progress ledgers, and six-domain navigation.
- Corrected ECS-native deployment availability, ADS new-customer closure, Global Tables consistency generalizations, and report-retention assumptions.
- Preserved CodeCommit return, X-Ray maintenance/service distinction, Beanstalk mode distinction, and retired Kinesis SQL/OpsWorks context.
- Domains 3–6 remain unfinished; cross-domain service notes do not mark them complete.

See [[Notebook Provenance and Progress]] for input limitations and continuation guidance.
