# SpaceBack

**Retire the app. Get your space back.**

> **SpaceBack™ — a JDAC product. Copyright © 2026 JDAC, LLC. All rights reserved.**
>
> All parts of SpaceBack — instructions, scripts, logic, branded terminology, and supporting text — are JDAC materials unless expressly identified otherwise. An authorized recipient may use an unmodified copy of SpaceBack for personal use on their own folders and projects only; it may not be used on, or to deliver services for, projects belonging to other people or clients. Unless authorized in writing by Jonathan Schafer or JDAC, LLC, do not alter, rewrite, create a derivative version of, sell, sublicense, publicly redistribute, publish, repackage, or present any part of SpaceBack as your own work. These terms do not restrict your ownership or normal use of your own files, data, or decisions.

SpaceBack is a safety-first storage-cleanup process for your Mac, packaged as a
[Claude](https://claude.com/claude-code) skill. Instead of a single-purpose disk
app, SpaceBack asks a couple of questions, explains what it will do, then scans a
folder, removes **content-verified** duplicates, organizes what's left into a
small set of type folders, optionally archives large media, and gives you a
dashboard you can re-check monthly.

> A reference run took a Downloads folder from **35 GB → 12 GB (~23 GB reclaimed)**
> and sorted it into 6 clean folders.

## Why not just a disk app?

A disk analyzer shows you what's big. SpaceBack does more, with you in control:

- **Finds true duplicates by content** (byte-verified), not just big files
- **Organizes** files into type folders as it goes
- **Explains every move and asks before deleting**
- **Deletes to the Trash** (recoverable) — never `rm`
- **Archives** large media off-drive when you want
- **Tracks progress** on a dashboard over time

## Safety rails (always on)

- Dry-run preview + explicit confirmation before anything destructive
- Duplicates byte-verified before removal
- Never de-duplicates inside app bundles, `node_modules`, `.git`, or installed packages
- Keeps a source archive when removing an extracted project's regenerable files

## Install and run

**Easiest path (new to Claude Code).** Copy one command, paste it in Terminal, then run SpaceBack in the app:

1. In **Terminal**, paste and run — then wait for the ✓ and **close Terminal**:
   ```
   claude plugin marketplace add JDACLLC/SpaceBack && claude plugin install spaceback@jdac
   ```
2. Open **Claude Code** — the "Code" tab in the Claude desktop app, **not** a regular Claude chat — and start a **new chat**.
3. Type **`/spaceback:run`** and answer the questions on screen.

*Terminal says `command not found: claude`? Install Claude Code first: <https://code.claude.com/docs/en/setup> (requires a paid Claude plan).*

**Already in Claude Code?** Do it all with slash commands:

```
/plugin marketplace add JDACLLC/SpaceBack
/plugin install spaceback@jdac
/spaceback:run
```

> Why the specific steps: plugins load once when a conversation starts, so a brand-new
> Claude Code chat (not the terminal prompt, and not a regular Claude chat) is what makes
> `/spaceback:run` available. See DL-006.

(Or just say "clean up my Downloads" and Claude invokes it.) It will ask which folder
to evaluate (default `~/Downloads`), whether to remove
duplicates or just report them, and whether to organize the results — then preview
the plan before doing anything.

> SpaceBack matches duplicates by their actual contents — not just file names — so even
> renamed copies get caught.

## What's in here

The installable plugin lives under `plugins/spaceback/` (manifest + the `run` skill):

- `plugins/spaceback/skills/run/SKILL.md` — the SpaceBack engine (intake → preview → scan → act → organize → dashboard)
- `plugins/spaceback/skills/run/scripts/scan.py` — Python-3.9-safe duplicate scanner (size-group + content hash)
- `plugins/spaceback/skills/run/scripts/organize.py` — type-based folder organizer (dry-run by default)
- `plugins/spaceback/skills/run/scripts/gen_dashboard.py` — generates the Storage Cleanup Tracker + keeps a run history
- `plugins/spaceback/skills/run/dashboard-template.html` — reference design for the dashboard
- `.claude-plugin/marketplace.json` — the JDAC marketplace entry; `plugins/spaceback/.claude-plugin/plugin.json` — the plugin manifest

## Documentation Status

**Protocol Version:** 2.0.5
**Application Version:** 0.1.0
**Documentation Last Reconciled With:** v0.1.0 (2026-10-05)
**Reconciled On:** 2026-10-05
**Known Exceptions:** None

**Authoritative records (start here):** `docs/DOC_PROTOCOL.md` (governing protocol) ·
`README.md` (this map) · `CHANGELOG.md` · `DECISION_LOG.md` · `ARCHITECTURE.md` ·
`RUNBOOK.md` · `TESTING.md` · `SECURITY.md` · `TODO.md` (current work) · `ROADMAP.md`
(backlog/triage). The Drive IP-18 folder holds point-in-time IP evidence snapshots.

## Status

Public beta — **v0.1.0**. Currently macOS-first; Windows support (via a
cross-platform trash step and OS-aware paths) is planned for v1.1.

## Cleanup, not an ongoing service

SpaceBack is a one-time cleanup — not an ongoing maintenance process. If you'd like
help setting up an ongoing process to keep things clean over time, reach out to
Jonathan Schafer at **jonathan@jdacllc.org** or **JDAC.ai**.

---

Jonathan Schafer / Founder | JDAC Consulting / JDAC.ai | 480 620 4682 / Human-centered AI. Smarter workflows. Real-world efficiency.
