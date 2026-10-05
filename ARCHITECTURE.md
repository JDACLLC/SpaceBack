# ARCHITECTURE.md — SpaceBack

## What it is
A macOS storage-cleanup **Claude skill** (install kit). Claude runs the `SKILL.md`
playbook conversationally and calls three bundled Python scripts. No server, no network
calls, no stored data beyond a local run-history file the user keeps.

## Components

| Component | Role |
|---|---|
| `SKILL.md` | The engine — 8-step flow Claude follows (intake → readiness → scan → de-dup → organize → archive → dashboard → wrap-up) |
| `scripts/scan.py` | Duplicate detection: groups by exact size, then content hash (full MD5 ≤1 MB; head+tail 64 KB + size for larger). Outputs `dupes.json`. Never uses filenames to detect dupes. |
| `scripts/organize.py` | Sorts a folder's top-level items into 6 type folders (Images, Videos, Audio, Documents, Archives & Installers, Projects & Folders). Requires `--root`; refuses `$HOME`/`/`. Dry-run by default. |
| `scripts/gen_dashboard.py` | Writes a self-contained HTML "Storage Cleanup Tracker" from the run's metrics + a live folder scan; appends to a history JSON. |
| `dashboard-template.html` | Reference design for the tracker. |
| `docs/DOC_PROTOCOL.md` | Installed JDAC Development Documentation Protocol v2.0.5 (governs this project). |

## Data flow
`SKILL.md` (Claude) → confirm folder → `scan.py` → Claude separates safe vs. bundle-nested
duplicate groups and presents a numbered plan → user approves specific groups → full
byte-verify → move extras to Trash via Finder (`osascript`) → `organize.py --go` → optional
archive copy to a user-named destination → `gen_dashboard.py` writes the tracker.

## Boundaries & environments
- Runs inside Claude Code / Claude desktop with shell access; Python 3.8+.
- Deletions go to the macOS **Trash** (recoverable) via Finder — never `rm`.
- Duplicate detection never recurses into app bundles, `node_modules`, `.git`, or installed packages.
- Platform: macOS (v1.0). Windows is v1.1 (cross-platform trash + OS-aware paths).

## Sources of truth
In-repo governed records are authoritative (DL-004). GitHub `JDACLLC/SpaceBack` is live
source control; Drive IP-18 is the IP evidence package (snapshots at doc sync).

---

Jonathan Schafer / Founder | JDAC Consulting / JDAC.ai | 480 620 4682 / Human-centered AI. Smarter workflows. Real-world efficiency.
