# TESTING.md — SpaceBack

Proportionate smoke test for a file-moving tool. Run before declaring substantive work complete.

## Critical workflows to verify
1. **Duplicate detection by content** — identical files with different names are found; filenames alone are never the basis.
2. **Bundle safety** — duplicate files inside `node_modules` / app bundles are **not** touched.
3. **Byte-verify before delete** — full compare precedes any Trash move.
4. **Trash-safe delete** — removed files land in the Trash (recoverable), never `rm`.
5. **Selective approval** — only user-approved duplicate groups are acted on.
6. **Organize scope** — only the named folder's top-level items are sorted; `--root` required; `$HOME`/`/` refused.
7. **Dashboard** — self-contained HTML (no external requests) with real metrics.

## Verification Run — 2026-10-05

**Application Version or Change:** v0.1.0 engine + scripts
**Environment:** Local (throwaway test folder in a scratch directory)
**Checks Run:** Workflows 1–7 above, end to end (`scan.py` → selective de-dup → `organize.py --go` → `gen_dashboard.py`)
**Result:** Passed
**Evidence:** Test folder had 3 content-identical groups (incl. renamed copies) + a dup inside `node_modules`. Scan found the 3 safe groups and flagged the `node_modules` group as skipped. 4 extras byte-verified and moved to Trash; `node_modules` untouched. 11 items organized into type folders. Dashboard generated with 0 external references.
**Skipped or Blocked:** None
**Verified By:** Jonathan Schafer (with Claude)

## Known limitations
- macOS only (Trash via Finder). Windows is v1.1.
- Large-file scan uses a fast head+tail+size fingerprint to find *candidates*; a **full
  byte-for-byte** compare is always performed before any deletion.

---

Jonathan Schafer / Founder | JDAC Consulting / JDAC.ai | 480 620 4682 / Human-centered AI. Smarter workflows. Real-world efficiency.
