# TODO.md — SpaceBack (current work only)

Full backlog and roadmap: see `ROADMAP.md` (the designated triage/backlog record).

## In Progress
- Landing page (Lovable): build + publish the install section — copy-button + hardened 3-step instructions (DL-006). Lovable prompt is ready.

## Up Next
- Decide whether to add a "Requires a paid Claude plan" line near the landing-page button.
- Point the **IP-15** canonical record (Drive + Notion) to protocol **v2.0.5**.
- Double-check all authoritative docs reference v2.0.5 / assessment v2.0.4 (verify against Jon's new link).

## Windows version (v1.1 — after Mac ships; full plan in ROADMAP.md)
- Port the OS-specific layer: recoverable delete (Recycle Bin via `send2trash`), OS-aware paths, OS-branched `SKILL.md`, Windows readiness check.
- Test end-to-end on a real Windows machine/VM (needs a Windows box — not testable from macOS).
- Ship on the same repo/marketplace (install one-liner already works in PowerShell); bump → v1.1, validate, commit + push.
- Make it downloadable: cut a **GitHub Release** (tag `v1.1`) with a zipped source asset; landing page links it.
- Doc/IP sync afterward (DL, CHANGELOG, README, Drive snapshot, Notion).

## Waiting On
- Jon's new link to confirm the newest protocol/assessment versions.

## Recently Done
- Install-path decision + hardened instructions after external testing (DL-006); README install section rewritten.
- Smoke-tested the installed plugin end-to-end (`/spaceback:run`, v0.1.1): dedup correctness, `node_modules` exclusion, byte-verify, organize idempotency, persistent history.
- Packaged as the `spaceback` plugin in the `jdac` marketplace (`/spaceback:run`); manifests validated.
- Adopted JDAC DOC Protocol v2.0.5; reconciled the governed record set.
- Readiness preflight, intake validation, usage terms, dashboard generator, end-to-end test.

---

Jonathan Schafer / Founder | JDAC Consulting / JDAC.ai | 480 620 4682 / Human-centered AI. Smarter workflows. Real-world efficiency.
