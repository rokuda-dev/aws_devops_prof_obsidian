# AWS DevOps Professional Obsidian Notebook

An Obsidian study notebook for the **AWS Certified DevOps Engineer - Professional (DOP-C02)** exam. The vault lives in [`AWS-DOP-C02-Notebook/`](AWS-DOP-C02-Notebook/) and organizes study material around reusable service notes, domain study paths, and exam scenario decisions.

## Getting started

1. Clone or download this repository (extract it if downloaded as a ZIP).
2. In Obsidian, choose **Open folder as vault** and select the `AWS-DOP-C02-Notebook` folder inside the repository.
3. Open [00 - Start Here](AWS-DOP-C02-Notebook/00%20-%20Start%20Here.md) for navigation and suggested study paths.

The core Markdown notes and wiki links require no plugins. The vault includes Obsidian configuration and the **Mark as Read** community plugin (`explorer-property-attributes`) for displaying and toggling each note's Boolean `read` property. Notes can also be read directly on GitHub, although Obsidian provides navigation through the internal wiki links.

## What's included

The notebook contains **213 Markdown notes**, including **99 service pages** (individual service notes and grouped navigation pages) and four audit records from the September 27, 2026 verification run.

| Location | Contents |
| --- | --- |
| [Domains](AWS-DOP-C02-Notebook/Domains/) | Study paths for SDLC automation, configuration management and IaC, resilient cloud solutions, monitoring and logging, incident and event response, and security and compliance. |
| [Services](AWS-DOP-C02-Notebook/Services/) | Service details, exam cues, common traps, and links to related topics. |
| [Concepts](AWS-DOP-C02-Notebook/Concepts/) | Cross-service topics such as deployment strategies, disaster recovery, centralized logging, and automated remediation. |
| [Comparisons](AWS-DOP-C02-Notebook/Comparisons/) | Side-by-side distinctions between services, features, and architecture choices. |
| [Exam](AWS-DOP-C02-Notebook/Exam/) | Scenario decisions, architecture patterns, service selection, corrections, and rapid review. |
| [Sources](AWS-DOP-C02-Notebook/Sources/) | Official AWS references, verification records, source provenance, and notebook history. |

## Suggested study path

- Start with the [All-Domain Study Roadmap](AWS-DOP-C02-Notebook/Domains/All-Domain%20Study%20Roadmap.md), then follow the linked domain and service notes.
- Use the [Service Index](AWS-DOP-C02-Notebook/Service%20Index.md) to find a service and the [Service Selection Matrix](AWS-DOP-C02-Notebook/Exam/Service%20Selection%20Matrix.md) to practice choosing services from requirements.
- Review [High-Value Exam Patterns](AWS-DOP-C02-Notebook/Exam/High-Value%20Exam%20Patterns.md) and [Common Traps and Current Corrections](AWS-DOP-C02-Notebook/Exam/Common%20Traps%20and%20Current%20Corrections.md).
- Finish with [Rapid Review](AWS-DOP-C02-Notebook/Exam/Rapid%20Review.md), updating note `read` properties as you study.

### Reset reading progress

Each reader can start with a clean set of progress flags by running this command from the repository root:

```shell
python scripts/reset_read_flags.py
```

The script sets the YAML `read` property to `false` in every Markdown note under `AWS-DOP-C02-Notebook/`. It validates all notes before changing any of them and leaves notes that are already unread untouched. To preview the number of changes without modifying files, run:

```shell
python scripts/reset_read_flags.py --dry-run
```

The reset changes tracked notebook files, so run it in a personal clone or working copy when you do not want to alter another reader's recorded progress. A vault in a different location can be selected with `--vault PATH`.

## Sources and scope

This is exam-focused study material, not exhaustive AWS documentation. Refer to the notebook's [Official AWS Sources](AWS-DOP-C02-Notebook/Sources/Official%20AWS%20Sources.md) and confirm changing service behavior and exam scope against current AWS documentation.

The committed notebook identifies itself as **version 1.4.5**. See the [Notebook Changelog](AWS-DOP-C02-Notebook/Sources/Notebook%20Changelog.md), [Notebook Provenance and Progress](AWS-DOP-C02-Notebook/Sources/Notebook%20Provenance%20and%20Progress.md), and [Notebook Validation](AWS-DOP-C02-Notebook/Exam/Notebook%20Validation.md) for its history, coverage limits, and recorded release checks.

The latest [verification and stale-reference audit](AWS-DOP-C02-Notebook/Sources/Verification%20and%20Stale%20Reference%20Audit%202026-09-27.md) covers every original page, records targeted AWS-source checks and corrections, and separates current findings from historical release validation. Run `python scripts/verify_notebook.py --output audit/structure.json` for read-only structural checks; add `--http` for external link status and redirect checks.

## License

To the extent the repository maintainer holds copyright and related rights in the original notebook content and repository documentation, those rights are dedicated to the public domain under [CC0 1.0 Universal](LICENSE). You may copy, modify, and redistribute that material, including commercially, without asking permission or providing attribution. CC0 includes a fallback license where the waiver is not legally effective.

This dedication does not apply to third-party material or grant rights in trademarks. The bundled Mark as Read plugin remains under its own MIT license. See [Third-party notices](THIRD_PARTY_NOTICES.md) for details.

The material is provided as-is, without warranties, as described in CC0. This is an independent study resource and is not affiliated with or endorsed by Amazon Web Services or Obsidian. No guarantee of accuracy, exam results, or suitability for production use is made.
