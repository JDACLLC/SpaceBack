# Changelog — SpaceBack

Authoritative history of material changes. Semantic versioning. Dates are local calendar dates.

## [Unreleased]

### Added
- SpaceBack skill engine (`SKILL.md`): 8-step flow — welcome + intake, readiness check,
  scan + explain, selective de-duplicate, organize, archive offer, dashboard, wrap-up.
- `scripts/scan.py` — content-hash duplicate scanner (size-group → smart hash), Python 3.9-safe.
- `scripts/organize.py` — type-based organizer into 6 folders; requires `--root`.
- `scripts/gen_dashboard.py` — generates the self-contained Storage Cleanup Tracker (system
  fonts, no external requests) and appends each run to a history file.
- JDAC usage terms (top disclaimer + attribution footer) on distributable files and script
  headers; "cleanup-only, not an ongoing service" boundary + contact.
- Readiness preflight check (Python 3.8+, folder access, Trash, shell) with plain-language fixes.
- JDAC Development Documentation Protocol v2.0.5 installed at `docs/DOC_PROTOCOL.md`;
  governed record set reconciled (this file, DECISION_LOG, ARCHITECTURE, RUNBOOK, TESTING,
  SECURITY, TODO; ROADMAP designated as the backlog/triage equivalent).

### Fixed
- `organize.py` hardcoded-path bug — now requires `--root` and refuses `$HOME`/`/` (DL-001).

### Verification
- End-to-end test on a throwaway folder: content-based duplicates found, `node_modules`
  skipped, byte-verified before Trash, organized into type folders, dashboard generated.
  See `TESTING.md`.

---

Protocol adoption: JDAC Development Documentation Protocol v2.0.5 adopted 2026-10-05 (DL-003).

---

Jonathan Schafer / Founder | JDAC Consulting / JDAC.ai | 480 620 4682 / Human-centered AI. Smarter workflows. Real-world efficiency.
