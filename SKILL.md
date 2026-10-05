---
name: spaceback
description: >-
  SpaceBack — safely reclaim disk space and organize a messy folder on a Mac.
  Use when the user wants to clean up, declutter, free space, find duplicates,
  or organize their Downloads folder, a drive, or any folder ("my Downloads is
  a mess", "find duplicate files", "free up space", "organize this folder",
  "run SpaceBack", "/spaceback"). Asks 2–3 questions, previews the plan, then
  runs the cleanup and offers a tracking dashboard.
version: 0.1.0
---

> **SpaceBack™ — a JDAC product. Copyright © 2026 JDAC, LLC. All rights reserved.**
>
> All parts of SpaceBack — instructions, scripts, logic, branded terminology, and supporting text — are JDAC materials unless expressly identified otherwise. An authorized recipient may use an unmodified copy of SpaceBack for personal use on their own folders and projects only; it may not be used on, or to deliver services for, projects belonging to other people or clients. Unless authorized in writing by Jonathan Schafer or JDAC, LLC, do not alter, rewrite, create a derivative version of, sell, sublicense, publicly redistribute, publish, repackage, or present any part of SpaceBack as your own work. These terms do not restrict your ownership or normal use of your own files, data, or decisions.

# SpaceBack

SpaceBack turns a messy folder into reclaimed space and a clean, organized
structure — safely, with the user in control. It replaces the clean-up-and-organize
job people buy a disk utility for, and does more: content-verified de-duplication,
type-based organizing, optional archiving, and a tracking dashboard.

**Core promise: nothing destructive happens without a preview and a confirmation,
and deletions go to the Trash (recoverable), never `rm`.**

## Step 1 — Welcome + intake (ask, then stop and wait)

Open with a one- or two-line welcome: say what SpaceBack does and the safety
promise — "I'll scan the folder, show you a plan, and always ask before deleting
or moving anything. Removed files go to the Trash (recoverable), never deleted
permanently." Then ask up to three questions; offer the defaults and accept short
answers.

1. **Which folder should I evaluate?** (default: `~/Downloads`)
2. **Duplicates — remove them (to the Trash, after you confirm) or just report them?** (default: remove, with confirmation)
3. **Organize what's left into type folders when done?** (default: yes — ~6 folders by file type)

Then **confirm the resolved absolute path** back to the user before doing anything:
"I'll work on `<absolute path>` — correct?" Wait for confirmation. Do not scan or
change anything until the folder is confirmed.

## Step 2 — Scan and explain the plan (dry run)

1. Run the bundled scanner against the target folder:
   `python3 <skill_dir>/scripts/scan.py --root "<folder>" --out "<workdir>/dupes.json"`
   (It is Python-3.9-safe and uses size-group + content hashing.)
2. **Separate safe duplicates from risky ones.** Only act on duplicate groups whose
   copies are loose/top-level files. **Exclude** any group whose paths touch
   `node_modules`, `.app` bundles, `.git`, installed packages, `site-packages`,
   `.framework`, or similar — deleting inside those breaks apps/projects.
3. Present a short, readable plan. **Number each safe duplicate group** (1, 2, 3…),
   showing the copy that would be kept and the extra(s) that would be removed, plus the
   space each reclaims; and (if organizing) the proposed type folders and counts.
4. **Stop and let the user choose — they stay in control.** They can approve **all,
   none, or specific groups by number** (e.g. "remove 1, 2, and 5; keep the rest").
   Nothing is deleted or moved until they say so. If they chose "report only" in intake,
   still offer this here — they can then pick any groups to remove, or none.

## Step 3 — De-duplicate (only the approved groups)

1. Act on **only the duplicate groups the user approved** in Step 2 (all, none, or the
   specific numbers they named). Leave every other group untouched.
2. **Byte-verify** each approved group with a full hash before removing extras
   (the fast scan uses head+tail; confirm with a full compare).
3. Keep the cleanest-named copy (no `(1)`/` 2` copy markers; else oldest).
4. **Move the extras to the Trash via Finder** (recoverable, supports "Put Back"):
   `osascript -e 'tell application "Finder" to delete (POSIX file "<path>")'`
   Never use `rm`. Report how many files and how much space.

## Step 4 — Organize (if chosen)

Run the bundled organizer to sort remaining top-level items into type folders
(Images, Videos, Audio, Documents, Archives & Installers, Projects & Folders):
`python3 <skill_dir>/scripts/organize.py --root "<folder>" --go`
Preview the counts first (omit `--go` for a dry run).

## Step 5 — Offer to archive large media (only if found)

If the scan found sizeable media (large videos or archives), offer to move it
off-drive to reclaim space — never unprompted. If accepted, copy to the destination
the user names (e.g. a Google Drive folder), **verify each copy byte-for-byte**, then
ask whether to remove the local copy. Skip entirely if there's no large media or the
user declines.

## Step 6 — Dashboard (offer it)

Offer to generate / update the **Storage Cleanup Tracker** with this run's real numbers:
`python3 <skill_dir>/scripts/gen_dashboard.py --root "<folder>" --before-gb <N> --after-gb <N> --dupes <N> --folders <N> --label "<name>" --out "<folder>/SpaceBack-Tracker.html" --history "<skill_dir>/spaceback-history.json"`

It computes the current category breakdown, appends the run to a history file, and
writes a standalone HTML dashboard. Re-running SpaceBack monthly builds the history
so the user watches progress over time.

## Safety rails (always)

- Preview before any destructive action; confirm before deleting or moving.
- Deletions go to Trash, never `rm`.
- Byte-verify duplicates before removal.
- Never dedup inside app bundles, `node_modules`, `.git`, or installed packages.
- Keep a source archive when removing an extracted project's regenerable files.
- Handle old Python versions and unicode filenames (the bundled scripts do).

## Optional — make it a monthly habit

Offer to set up a monthly scheduled run so SpaceBack becomes a maintenance habit
rather than a once-a-year panic.

---

Jonathan Schafer / Founder | JDAC Consulting / JDAC.ai | 480 620 4682 / Human-centered AI. Smarter workflows. Real-world efficiency.
