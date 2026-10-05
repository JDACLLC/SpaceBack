# SECURITY.md — SpaceBack

## Posture
SpaceBack is a local, user-run cleanup tool. It has **no server, no accounts, no network
calls, and stores no secrets**. It reads file metadata and content hashes locally to find
duplicates and generates a local HTML report.

## Data handling
- Operates only on the folder the user names (confirmed before any action).
- Deletions go to the macOS **Trash** (recoverable), never `rm`.
- The dashboard is **self-contained** — no external requests, no telemetry.
- The run-history JSON is local to the user's machine.

## Boundaries
- Duplicate detection never recurses into app bundles, `node_modules`, `.git`, or installed
  packages, so it cannot corrupt applications or projects.
- A full byte-for-byte compare precedes any deletion.

## Credentials / secrets
None used or stored by SpaceBack. (The maintainer's publishing credentials — e.g. GitHub —
live in the macOS Keychain, outside this repo, and are never committed.)

## Reporting
Security concerns → Jonathan Schafer, jonathan@jdacllc.org.

---

Jonathan Schafer / Founder | JDAC Consulting / JDAC.ai | 480 620 4682 / Human-centered AI. Smarter workflows. Real-world efficiency.
