# Beginner-friendly CISSP study guide

Read these chapters in order for a connected introduction, or use their objective navigation and term indexes to revisit a topic. Each chapter includes explanations, detailed concepts from the original notes, application questions with reasoning, and AI lessons mapped to existing objectives.

| Domain | Content file |
| --- | --- |
| 1 | [Security and Risk Management](CISSP-Domain-1-Content.md) |
| 2 | [Asset Security](CISSP-Domain-2-Content.md) |
| 3 | [Security Architecture and Engineering](CISSP-Domain-3-Content.md) |
| 4 | [Communication and Network Security](CISSP-Domain-4-Content.md) |
| 5 | [Identity and Access Management](CISSP-Domain-5-Content.md) |
| 6 | [Security Assessment and Testing](CISSP-Domain-6-Content.md) |
| 7 | [Security Operations](CISSP-Domain-7-Content.md) |
| 8 | [Software Development Security](CISSP-Domain-8-Content.md) |

The [combined PDF](../output/pdf/CISSP-Beginner-Study-Guide.pdf) is a generated local artifact. It includes linked contents, objective bookmarks, term indexes, and source links. Wide reference tables are presented as labeled records in the PDF to maintain readable text. The `output/` directory is intentionally ignored by Git.

## Source alignment and coverage

The structure follows [CONTENT-OUTLINE.md](../CONTENT-OUTLINE.md) and the original eight domain objective files. ISC2's published exam outline, effective April 15, 2024, and its domain-level AI guidance inform the organization. Objective placements for AI and the Harbor Services scenarios are editorial applications, not official exam questions.

The original objective files are unchanged. [coverage.jsonl](coverage.jsonl) maps all 4,648 nonblank source lines to the new chapters and records revised text. [EDITORIAL-CORRECTIONS.md](EDITORIAL-CORRECTIONS.md) identifies substantive corrections and qualifications. [coverage-summary.json](coverage-summary.json) records source hashes and chapter counts. Mapping proves traceability and preservation of the recorded text, not independent certification of every source claim.

## Rebuild and verify

From the repository root, with Python 3 and ReportLab installed:

```sh
python3 scripts/verify_content.py
python3 scripts/build_content_pdf.py
```

The verification command uses the Python standard library. The PDF builder requires `reportlab` and uses Arial when available on macOS, with a Helvetica fallback. An alternate output path can be supplied with `--output`.

Edit the chapter Markdown directly. If a mapped passage is changed, update its coverage record and record any substantive correction. Rebuild and visually check the PDF after content or layout changes.
