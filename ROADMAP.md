# SpaceBack — Roadmap

**Approach: Mac-first.** Finish and ship the macOS version, then circle back to Windows.

## v1.0 — macOS (current focus)

- [x] Register as JDAC IP asset (IP-18): Notion record, Drive folder, README
- [x] `SKILL.md` engine (intake → preview → scan → act → organize → dashboard)
- [x] Bundle proven scripts: `scan.py` (dup scanner), `organize.py` (type organizer)
- [ ] **Dashboard generator** — script that auto-fills the Storage Cleanup Tracker with each run's real numbers (today it's a hand-filled template)
- [ ] **End-to-end test** — run `/spaceback` on a test folder; confirm intake, preview, Trash-safe delete, organize, dashboard
- [ ] **Package for install** — ship as a drop-in skill / `/spaceback` command (optionally wrap as a plugin)
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
