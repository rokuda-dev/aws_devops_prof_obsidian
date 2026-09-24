---
tags: [aws, dop-c02, validation]
updated: 2026-09-20
read: false
---

# Notebook Validation

The release validation checks every active Obsidian wiki link and heading target, duplicate note basenames/headings, YAML front matter presence and syntax, Markdown table structure, source domains, summary-layer placeholders, stale completion text, and preservation of prior files. Fenced imported source text is not treated as active notebook links.

Release checks:

- 209 Markdown notes in v1.4.5; all 209 edited-v1.4.4 note filenames retained.
- 1,858 active wiki links, including seven heading targets.
- 99 service pages, including existing grouped navigation pages.
- All 219 files from the edited v1.4.4 task archive retained: 209 notes and 10 `.obsidian` configuration/plugin files. Corrected note bodies and release metadata are documented in the changelog and verification ledger.
- No missing wiki-link targets.
- No missing heading-link targets.
- No duplicate note basenames.
- No duplicate headings in a note.
- Every note includes valid YAML front matter.
- Every note includes exactly one Boolean `read` property, with the edited-v1.4.4 state preserved exactly: 11 `true` and 198 `false`.
- The configured **Mark as Read** plugin (`explorer-property-attributes` v1.3.2), its three plugin files, and all seven other `.obsidian` files are preserved byte-for-byte; the enabled-plugin configuration and manifest identity are also validated.
- All 527 external references resolve to the first-party source domains used by this notebook: `docs.aws.amazon.com`, `aws.amazon.com`, or `repost.aws`.
- All 99 service files appear exactly once as either a canonical entry or a compatibility-navigation entry in [[Service Index]].
- No current navigation or study-status language treats Domains 3–6 as a separate expansion, release, or transcript-completion tier.
- Start-page study paths and the four consolidated exam-review notes contain explicit in-file sections for Domains 1–6.
- The all-domain roadmap contains task-level decisions, high-value choices, and study links for every domain.
- Grouped compatibility service pages and explicit indexes remain navigation pages by design; they identify that purpose and link to canonical notes.
- Archive contents and compression integrity tested before delivery.
- Current-version status scan leaves no active unfinished-domain statement or Domains 3–6 special-status marker; historical release wording remains only where needed to preserve the changelog and source provenance.

Every note received a page-by-page claim review. Complete-looking lists and strong-claim wording were checked explicitly; the final automated pass revisited 461 lines containing terms such as “all,” “always,” “only,” “every,” “must,” “complete,” or “cannot.” This scope validates what the notebook writes and adds exam-relevant omissions; it does not claim exhaustive documentation of every AWS feature or testing of every possible Obsidian theme/plugin renderer. The bundled plugin files and configuration were preservation-validated, not behavior-tested across every Obsidian release or platform. [[Verification Ledger]] defines the technical evidence scope.
