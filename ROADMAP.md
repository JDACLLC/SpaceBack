# SpaceBack — Roadmap

**Approach: Mac-first.** Finish and ship the macOS version, then circle back to Windows.

## v1.0 — macOS (current focus)

- [x] Register as JDAC IP asset (IP-18): Notion record, Drive folder, README
- [x] `SKILL.md` engine (intake → preview → scan → act → organize → dashboard)
- [x] Bundle proven scripts: `scan.py` (dup scanner), `organize.py` (type organizer)
- [x] **Dashboard generator** — `gen_dashboard.py` auto-fills the self-contained tracker with each run's real numbers + keeps a run history
- [x] **End-to-end test** — ran the full flow on a test folder (dupes found by content, `node_modules` skipped, Trash-safe delete, organize, dashboard)
- [x] **Intake flow validated** — welcome, folder-path confirmation, numbered selective per-group dedup
- [x] **Readiness preflight check** — Python 3.8+, folder access, Trash, shell; plain-language fixes instead of mid-run failures
- [ ] **Package as a plugin** — one-click / fewest-clicks install that wraps the skill (next)
- [ ] **Optional monthly schedule** — set up a recurring run so cleanup is a habit
- [x] **GitHub repo** `JDACLLC/SpaceBack` (private) — created and pushed
- [ ] Branding pass (name lockup, optional mascot) — reuse the "Retire the app" graphics

## v1.1 — Windows (circle back after Mac ships)

- [ ] Replace the macOS Finder/Trash delete step with a cross-platform recoverable delete (`send2trash` → Recycle Bin on Windows, Trash on macOS)
- [ ] OS-aware default paths (`~/Downloads` vs `%USERPROFILE%\Downloads`, Trash vs Recycle Bin)
- [ ] Branch the `SKILL.md` intake/run flow by OS
- [ ] Note Python install prerequisite on Windows
- [ ] Test end-to-end on Windows

> ~80% of the logic (scan, content-hash de-dup, organize) is already OS-agnostic.
> The Windows work is mainly the delete step and path defaults.

## IP & canonical housekeeping

- [x] JDAC usage disclaimer (top) + attribution footer on `SKILL.md`, `README.md`, and script headers
- [ ] **Gather all SpaceBack documents + graphics into the canonical IP-18 Drive folder** — including the "Retire the App" graphics and any assets Jon created elsewhere, so the canonical record is complete (do later)
- [ ] Update the footer phone number in the IP-2 Markdown Attribution Standard (still lists the old number)
- [ ] Fold "every MD/collateral gets the top usage disclaimer + footer" into the IP-2 documentation/QA protocol (the standing check)
- [x] Installed **JDAC Development Documentation Protocol v2.0.5** at `docs/DOC_PROTOCOL.md` (verbatim; DL-003)
- [ ] **Reconcile SpaceBack docs under Protocol v2.0.5** — create the governed record set (CHANGELOG, TODO, TRIAGE, DECISION_LOG, ARCHITECTURE, RUNBOOK, testing/security as applicable); pending authorization
- [ ] **Point the IP-15 canonical record (Drive + Notion) to protocol v2.0.5** — it currently holds only the v0.1 draft
- [ ] Double-check all authoritative docs reference the newest versions (protocol v2.0.5, assessment v2.0.4) — verify against the new link Jon will provide
