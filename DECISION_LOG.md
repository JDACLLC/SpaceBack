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

---

Jonathan Schafer / Founder | JDAC Consulting / JDAC.ai | 480 620 4682 / Human-centered AI. Smarter workflows. Real-world efficiency.
