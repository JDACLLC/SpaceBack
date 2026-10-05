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

# SpaceBack

SpaceBack turns a messy folder into reclaimed space and a clean, organized
structure — safely, with the user in control. It replaces the clean-up-and-organize
job people buy a disk utility for, and does more: content-verified de-duplication,
type-based organizing, optional archiving, and a tracking dashboard.

**Core promise: nothing destructive happens without a preview and a confirmation,
and deletions go to the Trash (recoverable), never `rm`.**

## Step 1 — Intake (ask these, then stop and wait)

Ask the user up to three questions. Offer the defaults; accept short answers.

1. **Which folder should I clean?** (default: `~/Downloads`)
2. **Duplicates: move extras to Trash, or report-only first?** (default: report-only on the first run, then they confirm)
3. **Organize the remaining files into type folders when done?** (default: yes — ~6 folders by file type)

Do not scan or change anything yet.

## Step 2 — Scan and explain the plan (dry run)

1. Run the bundled scanner against the target folder:
   `python3 <skill_dir>/scripts/scan.py --root "<folder>" --out "<workdir>/dupes.json"`
   (It is Python-3.9-safe and uses size-group + content hashing.)
2. **Separate safe duplicates from risky ones.** Only act on duplicate groups whose
   copies are loose/top-level files. **Exclude** any group whose paths touch
   `node_modules`, `.app` bundles, `.git`, installed packages, `site-packages`,
   `.framework`, or similar — deleting inside those breaks apps/projects.
3. Present a short, readable plan: how much space the safe duplicates would reclaim,
   the top offenders, and (if organizing) the proposed type folders and counts.
4. **Stop and get an explicit "go" before deleting or moving anything.**

## Step 3 — De-duplicate (only after confirmation)

1. **Byte-verify** each duplicate group with a full hash before removing extras
   (the fast scan uses head+tail; confirm with a full compare).
2. Keep the cleanest-named copy (no `(1)`/` 2` copy markers; else oldest).
3. **Move the extras to the Trash via Finder** (recoverable, supports "Put Back"):
   `osascript -e 'tell application "Finder" to delete (POSIX file "<path>")'`
   Never use `rm`. Report how many files and how much space.

## Step 4 — Organize (if chosen)

Run the bundled organizer to sort remaining top-level items into type folders
(Images, Videos, Audio, Documents, Archives & Installers, Projects & Folders):
`python3 <skill_dir>/scripts/organize.py --root "<folder>" --go`
Preview the counts first (omit `--go` for a dry run).

## Step 5 — Dashboard (offer it)

Offer to generate / update the **Storage Cleanup Tracker** dashboard with this run's
real numbers (before→after size, space reclaimed, duplicates removed, folder counts),
so the user can re-run SpaceBack monthly and watch progress over time.

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
