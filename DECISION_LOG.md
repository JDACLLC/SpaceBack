# DECISION_LOG.md — SpaceBack

Significant decisions, context, alternatives, and consequences. **Authoritative**
(repo copy per DL-004). The Drive IP-18 Decision Log is retained as IP evidence.

## DL-001 — File-moving/deleting scripts require an explicit target
**2026-10-05 · Adopted.** Scripts that move/delete/reorganize files must take the target
folder as a required argument (no hardcoded path) and refuse `$HOME`/`/`; the target comes
from user intake. Found when `organize.py` hardcoded `~/Downloads` and acted on the wrong
folder during testing. `organize.py` now requires `--root` and guards broad roots.

## DL-002 — macOS first, Windows later
**2026-10-05 · Adopted.** Ship macOS v1.0 first, then Windows v1.1 (swap the Finder/Trash
delete for a cross-platform approach; OS-aware paths). ~80% of the logic is already
OS-agnostic. Tradeoff: Windows users wait for v1.1.

## DL-003 — Adopted JDAC Development Documentation Protocol v2.0.5
**2026-10-05 · Adopted.** Installed the protocol verbatim at `docs/DOC_PROTOCOL.md`;
SpaceBack is now protocol-governed.

## DL-004 — In-repo records are the authoritative documentation set
**2026-10-05 · Adopted.** The in-repo governed records (this file, `CHANGELOG.md`,
`ARCHITECTURE.md`, `RUNBOOK.md`, `TESTING.md`, `SECURITY.md`, `TODO.md`, and `ROADMAP.md`
as the backlog/triage equivalent) are authoritative. We write to them while working and
push copies to the Drive IP-18 evidence package at each "doc sync."
**Alternative considered:** keep the Drive IP-18 records authoritative (rejected — in-repo
travels with GitHub and is edited during the work).

## DL-005 — Packaged as a plugin (marketplace "jdac", command `/spaceback:run`)
**2026-10-05 · Adopted.** Packaged SpaceBack as a Claude Code plugin in a JDAC marketplace:
`.claude-plugin/marketplace.json` (name `jdac`), plugin at `plugins/spaceback/`, skill at
`skills/run/`. Install is two commands (`/plugin marketplace add JDACLLC/SpaceBack` →
`/plugin install spaceback@jdac`); the command is **`/spaceback:run`** — plugin skills are
always prefixed, and "run" was chosen over "clean" so it doesn't imply automatic deletion.
Validated with `claude plugin validate`.
**Alternatives considered:** a standalone skill for a bare `/spaceback` (rejected — loses
the one-click marketplace install).

## DL-006 — Distribution/install path for the non-technical (Skool) audience
**2026-10-05 · Adopted.** Primary install path: a **copy-button** on the landing page puts a
single chained Terminal command on the clipboard —
`claude plugin marketplace add JDACLLC/SpaceBack && claude plugin install spaceback@jdac` —
the user pastes it once in **Terminal**, closes Terminal, then opens **Claude Code** (the
desktop app's "Code" tab), starts a **new chat**, and runs **`/spaceback:run`**.
External testing surfaced three failures — all instructional; the install itself verified
correct (installed + enabled + files on disk): (1) typing `/spaceback:run` at the zsh prompt →
`no such file or directory`; (2) typing it in a conversation opened *before* the install →
"Unknown skill" (plugins load once, at session start); (3) typing it in **regular Claude**
instead of **Claude Code** → not recognized. Resolved by hardened instructions: step 1 ends
"**close Terminal**", step 2 names "**Claude Code** (Code tab), not a regular Claude chat,
start a **new** chat", step 3 names the message box. The command-not-found footnote links to
`https://code.claude.com/docs/en/setup`. Requires a paid Claude plan (Claude Code).
The install one-liner is byte-for-byte identical on Windows (PowerShell), so this path also
eases the future Windows release (DL-002); only the Trash/path runtime remains Windows-specific.
**Alternatives considered:** in-app `/plugin` GUI install (rejected as primary — the marketplace
store pane covers the window and adds navigation/clicks); download-a-zip-and-drop into
`~/.claude/plugins` (rejected — a hidden folder, and it doubles the instructions on Windows for
no runtime benefit).

---

Jonathan Schafer / Founder | JDAC Consulting / JDAC.ai | 480 620 4682 / Human-centered AI. Smarter workflows. Real-world efficiency.
