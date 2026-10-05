# RUNBOOK.md — SpaceBack

## Prerequisites
- macOS with Claude Code or the Claude desktop app (command/shell access).
- **Python 3.8 or newer** (`python3 --version`). On macOS: `xcode-select --install` if missing.

## Install (current: manual skill; plugin packaging in progress)
Place the `spaceback/` folder (with `SKILL.md` + `scripts/`) in your Claude skills
directory, then invoke `/spaceback`. (One-click plugin install is the next milestone.)

## Run
1. `/spaceback`
2. Answer the three questions (which folder to evaluate; remove duplicates or just report;
   organize when done). Confirm the folder path when asked.
3. Review the numbered plan; approve all, none, or specific duplicate groups.
4. SpaceBack byte-verifies, moves extras to Trash, organizes, optionally archives large
   media, and offers to generate the dashboard.

## Recovery / rollback
- Removed duplicates are in the **macOS Trash** — use **Put Back** to restore, until the
  Trash is emptied. SpaceBack never uses `rm`.
- Organizing only *moves* files into type folders in the same drive; drag them back if needed.

## Maintenance
- Re-run `/spaceback` monthly; `gen_dashboard.py` appends to the history so the tracker
  shows progress over time.

## Release / doc sync
- Commit to the repo as you work; on **"doc sync"**: push to `JDACLLC/SpaceBack`, snapshot
  source into Drive IP-18 `02 — Source`, and update the canonical README/Decision Log/Notion.

---

Jonathan Schafer / Founder | JDAC Consulting / JDAC.ai | 480 620 4682 / Human-centered AI. Smarter workflows. Real-world efficiency.
