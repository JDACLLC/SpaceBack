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

## Use it

In Claude Code or the Claude desktop app, install the skill and run:

```
/spaceback
```

It will ask which folder to clean (default `~/Downloads`), whether to remove
duplicates or report-only first, and whether to organize the results — then
preview the plan before doing anything.

## What's in here

- `SKILL.md` — the SpaceBack engine (intake → preview → scan → act → organize → dashboard)
- `scripts/scan.py` — Python-3.9-safe duplicate scanner (size-group + content hash)
- `scripts/organize.py` — type-based folder organizer (dry-run by default)
- `scripts/gen_dashboard.py` — generates the Storage Cleanup Tracker + keeps a run history
- `dashboard-template.html` — reference design for the dashboard

## Status

Public beta — **v0.1.0**. Currently macOS-first; Windows support (via a
cross-platform trash step and OS-aware paths) is planned for v1.1.

---

Jonathan Schafer / Founder | JDAC Consulting / JDAC.ai | 480 620 4682 / Human-centered AI. Smarter workflows. Real-world efficiency.
