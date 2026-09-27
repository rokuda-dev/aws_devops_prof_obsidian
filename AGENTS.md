# Repository context for ChatGPT and coding agents

## Purpose

This repository contains an Obsidian study vault for the **AWS Certified DevOps Engineer – Professional (DOP-C02)** exam. Help readers study through scenario-based exam judgment, practice questions, detailed explanations, service comparisons, architecture walkthroughs, troubleshooting, targeted review, and correction of stale course material.

The collection phase is complete. Treat the current Markdown vault as the working study source; improve and verify it rather than rebuilding it from scratch.

## Repository map

- `AWS-DOP-C02-Notebook/` — Obsidian vault.
- `AWS-DOP-C02-Notebook/00 - Start Here.md` — notebook entry point.
- `AWS-DOP-C02-Notebook/Domains/` — official exam-domain study paths and roadmap.
- `AWS-DOP-C02-Notebook/Services/` — canonical AWS service notes.
- `AWS-DOP-C02-Notebook/Concepts/` — cross-service architecture and operational concepts.
- `AWS-DOP-C02-Notebook/Comparisons/` — service and feature decision guides.
- `AWS-DOP-C02-Notebook/Exam/` — scenario decisions, traps, patterns, and rapid review.
- `AWS-DOP-C02-Notebook/Sources/` — first-party references, provenance, audits, and validation history.
- `scripts/verify_notebook.py` — structural and optional external-reference checks.
- `scripts/reset_read_flags.py` — validates all notes, then resets every YAML `read` flag to `false`.
- `audit/` — machine-readable verification snapshots and results.

## Exam organization

Keep study material aligned to the official domains and task statements:

1. SDLC Automation — 22%
2. Configuration Management and IaC — 17%
3. Resilient Cloud Solutions — 15%
4. Monitoring and Logging — 15%
5. Incident and Event Response — 14%
6. Security and Compliance — 17%

Prioritize the clues that determine the best exam answer: operational burden, blast radius, recovery objectives, deployment behavior, event delivery guarantees, account and Region boundaries, security controls, and managed-service limitations. Avoid generic service summaries when a scenario comparison is more useful.

## Technical authority and freshness

Use current first-party AWS sources for technical claims, preferably AWS Documentation, official service pages and announcements, official AWS blogs, and official sample repositories. Avoid third-party sources when AWS publishes an authoritative source.

Treat course transcripts and historical notebook statements as leads that may be stale. Current AWS documentation takes precedence. When they conflict, update the study guidance and explain the discrepancy. Recheck service availability and retirement, names, defaults, integrations, quotas, regional behavior, and security capabilities whenever those details affect the answer.

Do not silently turn a targeted check into a claim that every sentence or every regional variation was verified. Record the evidence and limits of broad verification work under `Sources/`.

## Editing rules

- Preserve Obsidian wiki-link syntax and existing note organization.
- Every note must retain YAML front matter with exactly one Boolean `read: true` or `read: false` property.
- A reader's `read` values are personal progress. Do not change them during ordinary content edits. Only reset them when explicitly requested, using `python scripts/reset_read_flags.py` (preview with `--dry-run`).
- Preserve user changes and historical provenance. Do not rewrite release history as though a newer audit were part of an older release.
- Keep `.obsidian/workspace.json` changes made by the editor out of unrelated work where possible.
- Add links to the most specific first-party source that supports the claim. A successful HTTP response alone does not prove that a source supports nearby text.
- When changing a service fact, propagate material exam-impacting corrections to relevant comparison, domain, trap, and rapid-review notes.
- Keep navigation pages concise and place detailed technical content in the canonical service or concept note.

## Validation

Run the structural check after notebook edits:

```powershell
python scripts/verify_notebook.py --output audit/structure.json
```

When the task includes stale-link checking and network access is available, run:

```powershell
python scripts/verify_notebook.py --http --output audit/references.json
```

The verifier checks active wiki links and heading targets, duplicate note names/headings, limited front-matter invariants, and Service Index coverage. It is not a full YAML parser and does not establish the correctness of technical claims.

Before handing off changes, also run `git diff --check` and summarize what changed, the first-party evidence used, validation results, and any unresolved limitations.
