---
name: run
description: >-
  SpaceBack — safely reclaim disk space and organize a messy folder on a Mac.
  Use when the user wants to clean up, declutter, free space, find duplicates,
  or organize their Downloads folder, a drive, or any folder ("my Downloads is
  a mess", "find duplicate files", "free up space", "organize this folder",
  "run SpaceBack", "/spaceback:run"). Asks 2–3 questions, previews the plan, then
  runs the process and offers a tracking dashboard.
version: 0.1.1
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

Open with this welcome (verbatim), then ask the three questions; offer the defaults
and accept short answers.

> 👋 **I'm SpaceBack, a JDAC tool.** I'll help you get your space back and tidy up a folder — safely, with you in control.
>
> I'll look through the folder you choose, find true duplicates and clutter, and show you a plan *before* doing anything. **Nothing gets deleted or moved without your okay, and anything I remove goes to the Trash (recoverable) — never deleted for good.**
>
> Three quick questions to start 👇

1. **Which folder should I evaluate?** (default: `~/Downloads`)
2. **Duplicates — remove them (to the Trash, after you confirm) or just report them?** (default: remove, with confirmation)
3. **Organize what's left into type folders when done?** (default: yes — ~6 folders by file type)

Then **confirm the resolved absolute path** back to the user before doing anything:
"I'll work on `<absolute path>` — correct?" Wait for confirmation. Do not scan or
change anything until the folder is confirmed.

## Step 2 — Readiness check (make sure everything's ready)

After the folder is confirmed and before scanning, quietly verify the environment.
If everything checks out, say a short "✓ Ready" and continue. If anything is missing,
**stop and explain it in plain language with the fix** — never let a script fail mid-run.

Check:
- **Python 3.8 or newer** is available (`python3 --version`). The scripts need it.
- The **target folder** exists and is readable and writable.
- The **Trash mechanism** works (macOS Finder via `osascript`).
- Claude can **run shell commands** in this environment.

Plain-language messages when something's missing, for example:
- No/old Python: "SpaceBack needs Python 3.8 or newer to run. On macOS, install Apple's
  Command Line Tools with `xcode-select --install`, then try me again."
- Folder not accessible: "I can't read or write `<path>` — double-check the folder name
  and its permissions."
- No command access: "This environment won't let me run the cleanup — SpaceBack needs
  Claude Code or the Claude desktop app with command access."

## Step 3 — Scan and explain the plan (dry run)

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

## Step 4 — De-duplicate (only the approved groups)

1. Act on **only the duplicate groups the user approved** in Step 3 (all, none, or the
   specific numbers they named). Leave every other group untouched.
2. **Byte-verify** each approved group with a full hash before removing extras
   (the fast scan uses head+tail; confirm with a full compare).
3. Keep the cleanest-named copy (no `(1)`/` 2` copy markers; else oldest).
4. **Move the extras to the Trash via Finder** (recoverable, supports "Put Back"):
   `osascript -e 'tell application "Finder" to delete (POSIX file "<path>")'`
   Never use `rm`. Report how many files and how much space.

## Step 5 — Organize (if chosen)

Run the bundled organizer to sort remaining top-level items into type folders
(Images, Videos, Audio, Documents, Archives & Installers, Projects & Folders):
`python3 <skill_dir>/scripts/organize.py --root "<folder>" --go`
Preview the counts first (omit `--go` for a dry run).

## Step 6 — Offer to archive large media (only if found)

If the scan found sizeable media (large videos or archives), offer to move it
off-drive to reclaim space — never unprompted. If accepted, copy to the destination
the user names (e.g. a Google Drive folder), **verify each copy byte-for-byte**, then
ask whether to remove the local copy. Skip entirely if there's no large media or the
user declines.

## Step 7 — Reclaim Report (offer it)

Offer to generate / update the **Reclaim Report** with this run's real numbers:
`python3 <skill_dir>/scripts/gen_dashboard.py --root "<folder>" --before-gb <N> --after-gb <N> --dupes <N> --folders <N> --label "<folder name>" --out "<folder>/SpaceBack-Reclaim-Report.html" --history "$HOME/.spaceback/history.json"`

The history is kept in `~/.spaceback/history.json` so it **persists across plugin updates**.
The report computes the current category breakdown, appends the run to the history, and
writes a standalone HTML report. Offer to open it (`open "<path>"`). Re-running SpaceBack
monthly builds the history so the user watches progress over time.

## Safety rails (always)

- Preview before any destructive action; confirm before deleting or moving.
- Deletions go to Trash, never `rm`.
- Byte-verify duplicates before removal.
- Never dedup inside app bundles, `node_modules`, `.git`, or installed packages.
- Keep a source archive when removing an extracted project's regenerable files.
- Handle old Python versions and unicode filenames (the bundled scripts do).

## Step 8 — Wrap up

Offer to set up a **monthly scheduled run** so SpaceBack becomes a maintenance habit
rather than a once-a-year panic. Then close with this note:

> **SpaceBack is a one-time cleanup — not an ongoing maintenance process.** If you'd like
> help setting up an ongoing process to keep things clean over time, reach out to Jonathan
> Schafer at **jonathan@jdacllc.org** or **JDAC.ai**.

---

Jonathan Schafer / Founder | JDAC Consulting / JDAC.ai | 480 620 4682 / Human-centered AI. Smarter workflows. Real-world efficiency.
