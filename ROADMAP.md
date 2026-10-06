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
- [x] **Packaged as a plugin** — `jdac` marketplace + `spaceback` plugin; 2-command install, run `/spaceback:run` (manifests validated)
- [x] Smoke-test the **installed** plugin end-to-end (add marketplace → install → `/spaceback:run`)
- [x] **Install UX decided + hardened** — Terminal one-liner → Claude Code (new chat) → `/spaceback:run` (DL-006); landing copy + copy-button specced
- [ ] **Optional monthly schedule** — set up a recurring run so cleanup is a habit
- [x] **GitHub repo** `JDACLLC/SpaceBack` (private) — created and pushed
- [ ] Branding pass — [x] favicon (concept C: before→after bars, SVG + PNG set); [ ] name lockup / optional mascot — reuse the "Retire the app" graphics
- [ ] Build + publish the Lovable landing page (install section prompt ready)

## v1.1 — Windows (circle back after Mac ships)

**A. Port the OS-specific layer** (~80% of logic — scan, content-hash de-dup, organize — is already OS-agnostic)
- [ ] Replace the macOS Finder/Trash delete step with a cross-platform recoverable delete (`send2trash` → Recycle Bin on Windows, Trash on macOS)
- [ ] OS-aware default paths (`~/Downloads` vs `%USERPROFILE%\Downloads`; history → `%USERPROFILE%\.spaceback\`); handle backslashes, drive letters, long paths, unicode
- [ ] Branch the `SKILL.md` intake/run flow by OS (Trash step + commands); shared scan/organize logic stays common
- [ ] Windows readiness check — detect OS, verify Python (`py` launcher) + PowerShell + folder access, with plain-language fixes

**B. Test**
- [ ] End-to-end on a real Windows machine/VM (install → `/spaceback:run` → dedup to Recycle Bin → organize → Reclaim Report) — *requires a Windows box; can't be verified from macOS*

**C. Ship to GitHub** (same repo, same marketplace — install one-liner is already identical in PowerShell)
- [ ] Bump version → 1.1, update manifest (note Windows support), `claude plugin validate`, commit + push
- [ ] Adjust landing wording "Terminal" → "Terminal / PowerShell"

**D. Make it downloadable**
- [ ] Cut a **GitHub Release** (tag `v1.1`) with a zipped source asset as the real download link; landing page points to it (optionally also link the Drive snapshot)

**E. Doc/IP sync**
- [ ] DL entry (Windows shipped), CHANGELOG, README (Windows steps), new Drive snapshot + Notion Last Verified

> The headline: **install is already cross-platform** — Windows is mainly (A) the Recycle-Bin/paths port + (B) a real Windows test; "downloadable" is best served by a tagged GitHub Release, not a loose file.

## IP & canonical housekeeping

- [x] JDAC usage disclaimer (top) + attribution footer on `SKILL.md`, `README.md`, and script headers
- [x] **Gather SpaceBack documents + graphics into the canonical IP-18 Drive folder** — "Retire the App" graphics (3 variants) in `06 — Commercialization/Marketing Graphics/`; install + landing copy in `06`; favicon set as a brand asset
- [ ] Update the footer phone number in the IP-2 Markdown Attribution Standard (still lists the old number)
- [ ] Fold "every MD/collateral gets the top usage disclaimer + footer" into the IP-2 documentation/QA protocol (the standing check)
- [x] Installed **JDAC Development Documentation Protocol v2.0.5** at `docs/DOC_PROTOCOL.md` (verbatim; DL-003)
- [ ] **Reconcile SpaceBack docs under Protocol v2.0.5** — create the governed record set (CHANGELOG, TODO, TRIAGE, DECISION_LOG, ARCHITECTURE, RUNBOOK, testing/security as applicable); pending authorization
- [ ] **Point the IP-15 canonical record (Drive + Notion) to protocol v2.0.5** — it currently holds only the v0.1 draft
- [ ] Double-check all authoritative docs reference the newest versions (protocol v2.0.5, assessment v2.0.4) — verify against the new link Jon will provide
