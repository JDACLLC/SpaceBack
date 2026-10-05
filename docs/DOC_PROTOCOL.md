# JDAC Development Documentation Protocol&trade;

**Protocol Version:** 2.0.5  
**Owner:** Jonathan Schafer / JDAC Systems  
**Status:** Approved governing release  
**Effective Date:** 2026-10-03  
**Last Updated:** 2026-10-03  
**Intended Working Filename:** `docs/DOC_PROTOCOL.md`

## Usage, Ownership, and Attribution

All parts of this protocol file — including governing rules, instructions, branded terminology, templates, and supporting text — are JDAC materials unless expressly identified otherwise.

Copyright © 2026 JDAC, LLC. All rights reserved.

An authorized recipient may use an unmodified copy of this protocol within projects the recipient owns or is authorized to maintain and may create or modify project-specific documentation produced through its use.

Unless authorized in writing by Jonathan Schafer or JDAC, LLC, do not alter, customize, rewrite, remove provisions from, create a derivative version of, sell, sublicense, publicly redistribute, publish, repackage, or present any governed portion of this protocol as the recipient's own work.

These terms do not restrict the recipient's ownership or normal use of the recipient's own code, project information, decisions, or project-specific documentation.

The JDAC Development Documentation Protocol™ must always be installed and used unchanged.

---

## Purpose

This protocol defines the repeatable JDAC standard for creating, maintaining, testing, versioning, publishing, and handing off documentation for software, applications, websites, browser extensions, automations, agents, internal systems, and other technical builds.

It keeps documentation, test evidence, decisions, versions, operations, recovery, and handoff information current while a product is being built--not reconstructed afterward.

> **You make the decisions. AI maintains the records. Project files remain authoritative.**

The intended result is a project that is understandable, maintainable, transferable, and handoff-ready.

This standalone file contains only the JDAC Development Documentation Protocol™. No separate scored assessment is included or required. Begin with the protocol’s own project inspection and Project Profile for Confirmation described below.

## Governing principles

1. Documentation is part of delivery, not a separate cleanup activity.
2. The live implementation and its authoritative records must agree.
3. AI may inspect, draft, update, cross-check, and regenerate records, but the builder verifies accuracy and retains decision authority.
4. Update only records materially affected by the work. Never manufacture entries, decisions, tests, or evidence.
5. Code, configuration, comments, chat history, platform scaffolding, and generated boilerplate are supporting evidence--not substitutes for authoritative project documentation.
6. Each subject has one designated source of truth. Summaries and generated outputs must never become competing truth.
7. Documentation depth must be proportionate to the project's type, complexity, data sensitivity, integrations, autonomy, payments, and consequence of failure.
8. Secret values, protected prompts, personal information, and sensitive operational details must not be exposed in public or user-facing documentation.

## Definition of done

> **Build -> Test -> Record -> Version -> Update -> Handoff**

A substantive change is not complete until its applicable documentation, verification, versioning, publication, and handoff requirements have been addressed.

## Installation and activation

### Fresh Bootstrap

Use **Fresh Bootstrap** when all of the following are true:

1. The project is being created for the first time.
2. The approved protocol is attached as part of the initial project-creation request.
3. The platform necessarily creates the project and its first substantive implementation in the same operation, so no inspectable blank project exists beforehand.
4. No preexisting custom implementation, project-specific documentation, release history, or prior project state exists outside that creation request.

For a qualified Fresh Bootstrap, the initial project-creation request constitutes authorization to install the attached protocol verbatim and initialize the smallest sufficient documentation set as part of the same first build, unless the user explicitly limits or withholds that authorization. A separate pre-build profile-confirmation, installation-authorization, and reconciliation-authorization sequence is not required because there is no inspectable project state before the platform creates the project.

During Fresh Bootstrap, the AI must:

1. Treat the user's initial build request and supplied project facts as current intent, not historical evidence.
2. Create `docs/DOC_PROTOCOL.md` with contents matching the approved attached source; do not customize, summarize, rewrite, or silently omit protocol requirements.
3. Apply the protocol's proportionality and authority-collision rules and initialize only the smallest sufficient set of authoritative records justified by the project as created.
4. Never fabricate prior decisions, completed work, releases, tests, incidents, recovery events, handoff evidence, or historical rationale.
5. Record only changes and verification that actually occur during the bootstrap operation. If a test was not run, do not record it as passed.
6. Distinguish current project facts and explicit initial design choices from reconstructed historical decisions.
7. Confirm after the first build that `docs/DOC_PROTOCOL.md` matches the approved source and report the exact authoritative records initialized.
8. Present a concise Fresh Bootstrap completion profile identifying the project, platform, consequence profile, documentation initialized, material exclusions or deferrals, verification actually performed, and any human confirmation still needed.

Fresh Bootstrap is an initial-creation path only. Once meaningful implementation exists, later protocol adoption or upgrade work follows the normal Fresh, In Flight, or Unclear activation sequence below.

### Begin standard activation without installing

For an existing project, or for a platform that permits an inspectable project shell before the first substantive build, attach the approved protocol file to the project's AI builder or coding environment and use this command:

> Read the attached protocol and inspect this project without modifying it. Present the concise Project Profile for Confirmation required by the protocol. Do not install or replace `docs/DOC_PROTOCOL.md` until I confirm the profile and separately authorize installation.

During this activation phase, the AI must:

1. Read the attached protocol as the proposed governing standard.
2. Record or obtain the project's current repository revision before inspection when the environment supports revision history.
3. Inspect the project read-only and classify it as Fresh, In Flight, or Unclear. Fresh Bootstrap is not used here because it applies only when the protocol is supplied during the platform's initial project-creation/build operation.
4. Infer the proportional documentation approach from project evidence, present the concise profile, and ask only materially necessary questions.
5. Make no project or repository change, including creation of a plan artifact or regeneration of platform-managed code.
6. Compare the repository revision and changed-file list after inspection with the pre-inspection state.
7. Stop for profile confirmation and separate installation authorization only when no project artifact changed.

If inspection triggers automatic code generation, schema synchronization, formatting, dependency updates, plan persistence, or any other project mutation:

1. Do not claim the activation was read-only.
2. Disclose the exact changed files and the apparent trigger.
3. Stop without installing the protocol or making further changes.
4. Request explicit authorization before reverting, preserving, or incorporating the incidental change.

After installation is authorized, the installer must:

1. Create or replace `docs/DOC_PROTOCOL.md` with contents matching the approved source.
2. Not customize, summarize, rewrite, or silently omit protocol requirements.
3. Confirm that the installed file matches the attached source.
4. Make only the minimum adoption entry required by the existing authoritative change history.
5. Make no other project change until the separate reconciliation proposal is approved.
6. Keep the protocol file unchanged unless the owner explicitly approves a protocol upgrade.

After the installed protocol has been reviewed through several real work cycles and is trusted, it may also be saved as a platform workspace skill or equivalent reusable instruction set. The installed `docs/DOC_PROTOCOL.md` remains the project-visible governing record.

### Read-only and plan-mode integrity

When this protocol says an inspection, evaluation, simulation, or proposal is **read-only**, no durable project record may be created, edited, deleted, moved, or committed. This includes builder-managed plan files, archived plans, generated reports, task records, or other platform artifacts stored with the project.

If a platform necessarily persists chat state or a private planning artifact outside the authoritative project records, the operator must:

1. Disclose what the platform created or retained.
2. Confirm that it is not an authoritative project record and is excluded from protocol-alignment evidence.
3. Avoid presenting the project as untouched when a repository or project artifact changed.
4. Request authorization before removing or converting the artifact when removal would itself modify the project.

Plan mode is not automatically read-only. The platform's actual behavior controls the claim.

Repository files generated or refreshed automatically by a connected service are still project changes. A change is not exempt merely because the AI did not deliberately edit it.

### Initial project and documentation evaluation

For the standard activation path, inspect the project read-only before installation. Do not install, initialize, rewrite, or reconcile project documentation until the user confirms the project profile and separately authorizes installation. Fresh Bootstrap is the sole exception and follows the initial-creation rules above.

Determine from authoritative evidence where possible:

- Project name and purpose
- Product type and intended users
- Platform and deployment or publishing model
- Existing documentation and designated sources of truth
- Operational complexity and consequence profile
- Current application or product version, if one exists
- Documentation gaps, contradictions, obsolete records, and generated outputs

Classify the project as one of these states or activation paths:

- **Fresh Bootstrap:** The protocol is supplied with the platform's initial project-creation request and the platform necessarily creates the first substantive implementation at the same time; no inspectable pre-build project state exists.
- **Fresh project:** Only default scaffolding, placeholders, or an explicitly described new build exists; no meaningful custom implementation or project-specific documentation is established.
- **In-flight project:** Meaningful custom implementation, project-specific configuration, content, data structures, integrations, release history, or documentation already exists.
- **Unclear:** Available evidence does not safely distinguish the applicable standard state.

For an in-flight project, inspect the README or equivalent start-here record, repository structure, existing documentation, version source, platform metadata, and implementation evidence needed to understand the product. Preserve existing authoritative records and project-specific decisions. Infer the proportional documentation approach from the evidence and present the profile, material conflicts, and recommended initialization before creating or restructuring records.

For a fresh project using the standard activation path, state that no established project documentation exists yet and infer the smallest documentation set justified by the intended build. Do not create or propose historical entries, completed work, release evidence, test results, incidents, decisions, recovery events, or handoff evidence that have not actually occurred.

For Fresh Bootstrap, apply the same anti-fabrication and smallest-sufficient-set requirements during the first creation/build operation. The initial implementation may be documented as current project state and the bootstrap event may be recorded as the first change, but nothing may be backfilled as if it predated that event.

**The AI owns documentation-set applicability analysis.** The user confirms project facts and authorizes work; the user is not responsible for designing the documentation architecture. During activation and reconciliation planning, the AI must:

1. Apply the protocol's project-type, complexity, consequence, and conditional-record criteria to determine what is justified.
2. Recommend the smallest sufficient set of authoritative records for the actual project, reusing a clearly designated equivalent system when it already satisfies a requirement.
3. Add conditional or specialized records only when project evidence or confirmed requirements justify them.
4. Omit non-applicable records rather than creating empty or artificial placeholders, and identify material exclusions in the start-here record during reconciliation.
5. Ask the user only for unresolved facts that materially change applicability, authority, risk, ownership, or handoff requirements.
6. Never ask the user to choose between a "full suite" and a "reduced set," select records from a menu, or otherwise design the documentation suite when the protocol can determine applicability from evidence.

Keep activation concise: the Project Profile should summarize the recommended initialization, not enumerate every possible protocol record. After protocol installation, the reconciliation proposal must state the exact records to preserve, add, update, retire or merge, and verify.

Ask no more than five concise questions, and only when the answers materially affect documentation structure, authority, risk, or project understanding. Prefer questions about:

1. Project purpose, intended users, or success outcome when ambiguous
2. Project type, platform, or publishing/deployment model when unclear
3. Which existing record or system is authoritative when sources conflict
4. Sensitive data, payments, regulated activity, autonomous actions, integrations, or failure consequences not safely determinable
5. Ownership, access, release, recovery, or handoff expectations that change the applicable documentation set

Do not ask the user to repeat facts already supported by reliable evidence. If there is no material ambiguity, present the inferred profile and request confirmation without manufacturing questions.

Keep the confirmation concise. Use this structure and omit any line that does not materially help the user confirm the setup:

```markdown
## Project Profile for Confirmation

**Project:** [Name]  
**State:** Fresh Bootstrap / Fresh / In Flight / Unclear  
**Type and purpose:** [One sentence]  
**Platform:** [Builder, framework, hosting or publishing model]  
**Documentation found:** [Concise list or "No established project records"]  
**Material considerations:** [Only meaningful risk, integration, payment, privacy, recovery, or handoff factors]  
**Recommended initialization:** [One sentence describing what will be created, preserved, or reconciled]

### Questions
1. [Only a material ambiguity]
```

Do not provide a long repository inventory, a readiness score, a detailed audit, or explanations of every protocol record during activation. Ask zero questions when no material ambiguity remains. Normally ask no more than three or four; five is the absolute limit.

For Fresh, In Flight, or Unclear standard activation, after the user confirms the profile, stop and request separate authorization to install or replace the governing protocol. Protocol installation authorizes only the verbatim creation or replacement of `docs/DOC_PROTOCOL.md` and the minimum adoption entry required by the existing authoritative change history. It does not authorize creating, retiring, merging, rewriting, or reconciling other project records.

After installation under the standard activation path, present a concise reconciliation proposal covering only the records that would be preserved, added, updated, retired or merged, and verified. Stop again and request separate authorization before performing that reconciliation work. Never modify the installed governing protocol to embed inferred project details.

Fresh Bootstrap follows its separate initial-creation authorization rule above and therefore does not require these three pre-build stops.

Inference may support a question or proposed record, but it must not be represented as already documented.

## Version identities

The protocol and the product have separate version identities. They must never be presented as the same thing.

| Field | Meaning | When it changes |
|---|---|---|
| **Protocol Version** | Version of the JDAC documentation rules in this file | Only when the governing protocol itself changes |
| **Application Version** | Version of the product or release being documented | When the product's approved versioning policy requires a release bump |
| **Documentation Last Reconciled With** | Application version or dated product state against which the authoritative documentation suite was last checked | After a documented reconciliation review |
| **Document Last Updated** | Date a specific record was materially updated | When that record changes |

Rules:

- Do not change **Protocol Version** merely because the application version changed.
- Do not label `DOC_PROTOCOL.md` with an **App Version** in a way that implies the protocol itself shares that version.
- Project-facing documents may state **Application Version** and **Document Last Updated** when useful.
- Record **Documentation Last Reconciled With** by default in a short **Documentation Status** block in the project's start-here `README.md` or equivalent documentation index. A project may designate another location only when the reason and authoritative location are recorded in the start-here record. Do not repeat it across every file unless automation reliably keeps all copies synchronized.
- When the protocol is upgraded, record the old and new protocol versions and the adoption date in `CHANGELOG.md` or the designated project adoption record.
- A protocol upgrade does not prove that the rest of the documentation has been reconciled with the current application. Record both events separately.
- Installing or upgrading this protocol must not set **Documentation Last Reconciled With** to the current application version unless the complete approved reconciliation was actually performed and verified.
- Immediately after protocol installation, use **Not yet reconciled under Protocol vX.Y** and **Pending** for the reconciliation fields until closeout is complete.

Use this default block:

```markdown
## Documentation Status

**Protocol Version:** X.Y  
**Application Version:** X.Y.Z or Not Versioned  
**Documentation Last Reconciled With:** Not yet reconciled under Protocol vX.Y  
**Reconciled On:** Pending  
**Known Exceptions:** None or links to the authoritative exception records
```

After the approved reconciliation is completed and verified, replace the two pending values with the application version or dated project state actually reviewed and the completion date.

## Project profile and proportionality

The applicable documentation set must be based on the actual project.

Consider:

- Informational or marketing website
- Content or publication website
- Web or mobile application
- Browser extension
- Internal tool
- Automation, integration, or agent
- Library, prototype, or infrastructure-only project
- Other specialized technical product

Increase documentation depth when the project includes sensitive data, authentication, payments, autonomous or scheduled actions, external integrations, regulatory considerations, multiple environments, business-critical workflows, or substantial recovery consequences.

A managed platform may replace traditional infrastructure procedures, but it does not eliminate the need to document access, publishing or deployment, configuration, verification, restoration, recovery, and ownership responsibilities.

The AI must apply these proportionality rules directly. It must not transfer documentation-architecture decisions to the user merely because multiple standard or conditional records are available. When applicability is uncertain and the uncertainty materially changes the documentation set, ask for the missing project fact; otherwise infer applicability and recommend the justified set.

### Proportional documentation decision sequence

Before proposing or creating project records, the AI must evaluate documentation applicability in this order:

1. Identify the subjects that materially require authoritative documentation for the actual project.
2. Map each subject to the protocol's existing authoritative record responsibilities.
3. Reuse an accessible, current, clearly designated equivalent when one already satisfies the requirement.
4. Create a conditional or specialized record only when its distinct function is materially needed and cannot be adequately governed by an existing authoritative record.
5. Do not create a separate file merely because the information could be organized separately.
6. Prefer fewer authoritative records with clear ownership over a larger suite with overlapping or competing responsibilities.
7. Record materially relevant non-applicable conditional records once in the start-here record or documentation index; do not create placeholder files for them.

### Authority-collision check

Before proposing any new record, check whether its subject is already governed by an existing protocol record or designated equivalent. Do not create, propose, or preserve a record that duplicates, subdivides, shadows, or competes with an existing authoritative responsibility unless this protocol explicitly defines the record as a separate conditional requirement or the project has a documented specialized need that cannot be served by the existing authority.

Examples:

- Material product, operational, release, and documentation changes belong in `CHANGELOG.md`; do not create `DOC_CHANGELOG.md`, `RELEASE_LOG.md`, a separate "Documentation History," or another competing historical ledger.
- Current work belongs in `TODO.md`; do not create a second current-work list.
- Ranked backlog, issues, risks, and deferred work belong in `TRIAGE.md` or a clearly designated equivalent; do not create a second issue register merely for convenience.
- Significant decision rationale belongs in `DECISION_LOG.md`; do not create parallel decision-history files by topic unless a specialized reference is genuinely required.
- Architecture belongs in `ARCHITECTURE.md` and operational procedures belong in `RUNBOOK.md`; do not split these into additional authoritative files unless project complexity materially justifies the separation and the start-here record names the authority boundary.

A specialized, generated, public, or stakeholder-facing output may summarize or transform authoritative information, but it must identify or derive from its authoritative source and must not become a competing source of truth.

## Authoritative documentation system

Use the standard filenames below when their function applies. A clearly designated equivalent system may satisfy a requirement when it is accessible, authoritative, current, and named in the project's start-here record.

### Core authoritative records

| Record | Governing responsibility |
|---|---|
| `DOC_PROTOCOL.md` | Documentation rules, update triggers, evidence requirements, and closeout workflow |
| `README.md` or documentation index | Start-here record: purpose, project type, setup entry point, authoritative-record map, and current-state orientation |
| `TODO.md` | Current work only: In Progress, Up Next, Waiting On, and Recently Done |
| `TRIAGE.md` | Complete prioritized issue, risk, and feature backlog |
| `CHANGELOG.md` | Single authoritative history of material unreleased and released changes |
| `DECISION_LOG.md` | Significant decisions, context, alternatives, and consequences |
| `ARCHITECTURE.md` | Components, routes or surfaces, services, integrations, dependencies, data flow, environments, and system boundaries |
| `RUNBOOK.md` | Setup, routine operation, publishing or deployment, monitoring, recovery, rollback, backup, and redeployment as applicable |
| `SECURITY.md` | Authentication, authorization, secrets handling, data controls, privacy boundaries, external services, and hardening history |
| Testing record or protocol | Critical workflows, expected results, failure signals, environments, evidence, and skipped checks |

The six core records highlighted in the JDAC Quick Start are `TODO.md`, `TRIAGE.md`, `CHANGELOG.md`, `DECISION_LOG.md`, `ARCHITECTURE.md`, and `RUNBOOK.md`. `DOC_PROTOCOL.md`, the start-here record, security documentation, and testing evidence govern or support that core and remain required when applicable to the project.

### Conditional records

| Record | Create or maintain when |
|---|---|
| `USER_GUIDE.md` | End users need installation, access, workflows, troubleshooting, accessibility guidance, or support information |
| `SCREEN_GUIDE.md` | Screen-by-screen or surface-by-surface reference materially improves use or maintenance |
| `ADMIN_RUNBOOK.md` | Privileged operational procedures must remain separate from public or general contributor guidance |
| `E2E_SMOKE_PROTOCOL.md` | Test scope, commands, evidence, or interpretation warrants a dedicated record |
| `HANDOFF.md` | The dedicated-handoff triggers in this protocol apply |
| `generated/` | The project produces machine-readable, in-app, public, or stakeholder documentation from authoritative sources |
| Specialized reference | The project needs an access guide, API reference, data dictionary, field mapping, editorial guide, compliance record, monetization plan, or other domain-specific record |

Do not create empty or artificial documents merely to satisfy a filename checklist. When a standard record is not applicable, document that decision once in the start-here record or documentation index.

## Authority and record boundaries

- `TODO.md` describes active work; `TRIAGE.md` contains the full ranked backlog.
- `CHANGELOG.md` records what changed; `DECISION_LOG.md` records why.
- `ARCHITECTURE.md` explains how the system is structured; `RUNBOOK.md` explains how to operate, restore, recover, and redeploy or republish it.
- `SECURITY.md` explains security and privacy boundaries without storing secret values.
- `USER_GUIDE.md` teaches user goals and workflows; `SCREEN_GUIDE.md` explains individual interfaces.
- A README or documentation index tells a newcomer where to begin and which record owns each subject.

`CHANGELOG.md` is the sole authoritative history for material product, operational, release, and documentation changes. Never create or propose `DOC_CHANGELOG.md`, `RELEASE_LOG.md`, a separate documentation-history ledger, or another historical record as an authoritative project source. Public release notes, documentation-change summaries, private changelog views, stakeholder updates, and decks may be derived from `CHANGELOG.md`, but they are outputs, not additional sources of truth.

## Public, internal, and sensitive material

Clearly separate public or user-facing content from internal operational content.

Internal material may include account grants, credential-storage locations, administrator access, security operations, recovery procedures, proprietary logic, protected workflows, and incident response.

Never place secret values, credentials, access tokens, protected health information, personal data, or confidential prompts in documentation. Record the credential name, purpose, owner or role, storage system, rotation responsibility, and recovery path without recording the secret itself.

## Update triggers

For every substantive feature, interface, integration, workflow, architecture, security, operational, or release change, update only the records materially affected:

- [ ] User and screen guidance, when applicable
- [ ] Architecture and system boundaries
- [ ] Runbook, setup, deployment, rollback, recovery, monitoring, or backup procedures
- [ ] Security, privacy, permissions, secrets references, and protected workflows
- [ ] Active work, triage, and accepted-risk records
- [ ] Decision history when a significant choice was made
- [ ] `[Unreleased]` in `CHANGELOG.md`
- [ ] Application version and document metadata where applicable
- [ ] Generated, mirrored, in-app, or stakeholder outputs
- [ ] Relevant tests and test evidence
- [ ] Handoff information and current-state orientation

Every substantive change must update at least one maintained record. A no-documentation-impact conclusion must be explicit and defensible; do not create artificial entries.

## Work management and decisions

- Use stable identifiers in `TRIAGE.md` or the equivalent system; never renumber closed items.
- Rank work consistently, such as P0 through P3.
- Keep `TODO.md` short and synchronized with current activity.
- Move speculative or deferred work to a clearly labeled parking-lot section.
- Record meaningful decision context, including why the decision was needed, alternatives considered, consequences, owner, and date.
- Preserve decisions that constrain future changes, even when the implementation appears self-explanatory.

## Change and release history

Add every material code, documentation, configuration, workflow, integration, security, or behavior change under `[Unreleased]` when the work occurs. Move a coherent batch into a dated release section when a release is cut.

Use semantic versioning when appropriate:

- **Major:** Breaking change to a public contract, route, workflow, architecture, data model, or product direction
- **Minor:** New feature, page, integration, backend function, or notable capability
- **Patch:** Fix, copy or visual refinement, documentation correction, or dependency update

When the project uses a code-level application-version source, designate it as authoritative and reconcile it during release. Projects without meaningful releases may use dated change batches, but the chosen method must be explicit and consistent.

## Architecture, operations, security, and recovery

Documentation must allow another capable person to understand and safely operate the actual system without first reverse-engineering it.

As applicable, record:

- Components, routes or surfaces, services, integrations, and data flows
- Server/client, public/private, and trust boundaries
- Environments, dependencies, external systems, and sources of truth
- Access prerequisites and responsible roles
- Setup, configuration, publishing, deployment, and redeployment
- Monitoring, routine maintenance, backup, rollback, restore, recovery, and incident steps
- Security, privacy, data retention, credential references, and rotation responsibility
- Platform-managed functions versus owner-managed responsibilities
- Last-known-good state and how to return to it

Instructions must be usable but must not reveal secret values.

## End-user and screen documentation

Create `USER_GUIDE.md` when the product has end users who need guidance. A concise README may be sufficient for a small internal library, prototype, or simple project.

When user documentation exists:

- Organize it around user goals, not implementation structure.
- Use clear, supportive language appropriate to the audience; target approximately an eighth-grade reading level unless the audience requires otherwise.
- Provide numbered steps, descriptive headings, useful tips, common issues, and support guidance when they add value.
- Bold user-visible controls and fields.
- Use `[Screenshot: description]` for planned visuals.
- Include installation or access, primary workflows, troubleshooting, and next steps.
- Include accessibility guidance when accessibility features, assistive use, older users, health-adjacent use, or the intended audience makes it relevant.
- Keep user guides, screen guides, in-app help, screenshots, and current product behavior synchronized.
- Never expose internal-only procedures through public guidance.

## Generated, mirrored, and stakeholder outputs

Generated outputs may include machine-readable help, in-app documentation, public help pages, plain-language summaries, release communications, stakeholder summaries, and presentations.

Rules:

1. Designate the authoritative source from which each output is generated.
2. Store generated files under `docs/generated/` when appropriate and label them as generated.
3. Never edit generated output by hand unless the project explicitly documents a controlled exception.
4. Regenerate affected outputs when the source changes.
5. Verify that code or backend mirrors were updated and redeployed when required.
6. Record unsupported or skipped generation accurately.
7. Treat stakeholder decks as derived outputs, not sources of truth.
8. Never overwrite a historical stakeholder deck; increment its version suffix and label pre-launch, sprint, or monthly editions clearly.

The protocol may require a stakeholder presentation only when the project, audience, or engagement needs one and the active environment has a validated generation path. Capability on one platform must not be represented as available on another without verification.

Native stakeholder-PPTX generation has been verified in Lovable. Base44 may carry the policy through a workspace skill, but PPTX generation requires a custom or external implementation and must remain labeled unverified until tested successfully in the target project.

## Testing and evidence

Every project must define a proportionate smoke-test process before substantive work or a release is declared complete. A small website may use a concise manual checklist; a complex or high-consequence application may require automated and area-specific coverage.

For each applicable test, record:

- Critical workflow or previously working path
- Expected result and failure signal
- Test environment
- Test date or run identifier
- Result and evidence location
- Known limitation, skipped check, or reason automation is not practical

Run relevant checks before declaring a feature complete. Run the aggregate suite before release when practical. Never report a skipped or inaccessible check as passed.

`E2E_SMOKE_PROTOCOL.md` or its equivalent defines what to test and how to interpret the result. Evidence of an actual run must also be recorded in the test record, the `CHANGELOG.md` verification section, CI output, or another designated authoritative evidence location.

Use this minimum test-run evidence format regardless of where it is stored:

```markdown
### Verification Run -- YYYY-MM-DD

**Application Version or Change:** [Version, release, or work item]  
**Environment:** [Local, preview, staging, production-safe check, or other]  
**Checks Run:** [Applicable protocol sections, commands, or workflows]  
**Result:** Passed / Failed / Partial  
**Evidence:** [Path, CI run, screenshot reference, or recorded observations]  
**Skipped or Blocked:** [None, or check plus reason]  
**Verified By:** [Person, role, or authorized agent with human confirmation]
```

## Handoff and transfer standard

Handoff is a required outcome for every substantive project. A dedicated `HANDOFF.md` is mandatory for every high-consequence project. Lower-consequence projects may satisfy the outcome across the authoritative documentation suite unless another dedicated-handoff trigger applies.

### Universal handoff outcome

Another capable, authorized person must be able to:

1. Locate the start-here record and all authoritative documentation.
2. Understand the product's purpose, users, scope, boundaries, and current state.
3. Identify the current application version and the state with which documentation was last reconciled.
4. Obtain the necessary access through documented owners or roles without exposing secret values.
5. Set up, operate, publish or deploy, verify, maintain, and continue the project as applicable.
6. Restore, recover, roll back, redeploy, or republish the project using the platform-appropriate method when applicable.
7. Identify remaining work, accepted risks, deferred items, known limitations, and skipped checks.
8. Understand which decisions and invariants must not be reversed accidentally.
9. Know what must be verified before future work is considered complete.

### When `HANDOFF.md` is required

Create or refresh a dedicated `HANDOFF.md` when one or more of these conditions applies:

- Responsibility is actively transferring to another person or organization.
- An outside developer, operator, agency, client, buyer, or maintainer will assume work.
- The project is being paused, archived, sold, licensed, or prepared for due diligence.
- The project has high operational complexity or material business, privacy, security, payment, regulatory, or recovery consequences.
- Critical handoff information is distributed across records in a way that makes transition unreliable.
- The owner explicitly requires a formal acceptance record.

For this rule, a project is high-consequence when failure, misuse, loss of access, or an unsafe change could materially affect health-adjacent workflows, sensitive or regulated data, authentication or authorization, payments or subscriptions, scheduled or automated operations, material business continuity, security, privacy, or recovery. When any of those consequences apply, `HANDOFF.md` may not be deferred, replaced by a future intention, or declared unnecessary merely because no recipient has yet been identified.

If no real recipient exists, create the record as a readiness document. Name the current owner or responsible role as the verifying owner; document access ownership, transfer prerequisites, operational and recovery checks, unresolved single-holder dependencies, accepted risks, and the evidence still required before an actual handoff can be accepted. The absence of completed transfer verification must be stated honestly and does not excuse the record's absence.

A small, low-risk project may satisfy handoff through a strong README or documentation index plus current architecture, runbook, change, work, security, and testing records.

### Handoff acceptance

When a real recipient exists, the recipient or owner must confirm that the applicable handoff outcome can be completed. Record unresolved questions, missing access, accepted risks, skipped checks, recovery limitations, and follow-up ownership. Handoff is not complete merely because files were delivered.

Record acceptance in `HANDOFF.md` when that file is required; otherwise use the release record, project closeout record, or another location named in the start-here record.

Use this minimum handoff evidence format:

```markdown
### Handoff Verification -- YYYY-MM-DD

**Project / Application Version:** [Project and current version or dated state]  
**Recipient or Verifying Owner:** [Person or role]  
**Scope:** [What responsibility or project state is being handed off]  
**Verification Performed:** [Locate, understand, access, operate, recover, redeploy, or other applicable checks]  
**Result:** Accepted / Accepted with Exceptions / Not Accepted  
**Unresolved Items and Accepted Risks:** [None or links to authoritative records]  
**Follow-up Owner and Due Point:** [Person or role and date/milestone, if applicable]
```

Review handoff readiness at launch, major release, project pause, ownership transfer, outside-developer involvement, material platform change, and pre-sale or pre-licensing review.

## Exceptions and temporary deviations

Proportionality is not permission to silently ignore a requirement. Record the authoritative exception in `DECISION_LOG.md` by default because accepting, deferring, replacing, or declaring a governing requirement not applicable is a project decision. If the exception creates follow-up work, add a linked item in `TRIAGE.md`. If it materially affects a transfer, reference the same decision in the handoff record. Another authoritative system may replace this pattern only when it is named in the start-here record and preserves the same evidence.

An exception record must include:

- Requirement being deferred, replaced, or treated as not applicable
- Reason and supporting evidence
- Scope and affected project state
- Risk created by the exception
- Compensating control or interim approach, if any
- Person or role accepting the risk
- Review date, release, or milestone at which the exception expires or must be reconsidered

Exceptions do not count as completed requirements. Expired exceptions become open work until renewed or resolved. Permanent project-specific alternatives must identify the equivalent control and be preserved as a decision.

## Publishing and closeout workflow

1. Build or modify the product.
2. Update the authoritative records materially affected.
3. Regenerate derived documentation and mirrors when supported.
4. Run applicable smoke tests and record results accurately.
5. Review public/internal boundaries and the quality checklist.
6. Reconcile the live build, current-state record, application version, and `[Unreleased]` changelog.
7. Commit or save through the project's normal version-control process.
8. Publish or deploy through the normal release process.
9. Verify the released or published result.
10. Confirm the applicable handoff outcome and record unresolved items.

## Release gates

Before declaring substantive work or a release complete, confirm:

- [ ] The live build and authoritative documentation agree.
- [ ] Only materially affected records were updated.
- [ ] Applicable test results and skipped checks were recorded accurately.
- [ ] `CHANGELOG.md` includes the work under `[Unreleased]` or the correct released version.
- [ ] Significant decisions preserve context, alternatives, and consequences.
- [ ] Architecture, security, operations, recovery, and user guidance are current where applicable.
- [ ] Generated and mirrored outputs were regenerated or accurately marked unsupported or skipped.
- [ ] Protocol Version, Application Version, and Documentation Last Reconciled With are not confused.
- [ ] Links, routes, commands, filenames, owners, and access references are current.
- [ ] Handoff and recovery are clear for this project's type and risk.

## Documentation quality checklist

- [ ] Content is accurate, current, concise, and written for its audience.
- [ ] Instructions are numbered and actionable where appropriate.
- [ ] User-visible controls and fields are named accurately and bolded where useful.
- [ ] User guidance includes relevant tips, common issues, screenshots or placeholders, accessibility, and support information.
- [ ] Tables of contents and navigation links are current.
- [ ] Written, generated, mirrored, and in-app help agree.
- [ ] Each positive test claim has evidence.
- [ ] Inference is not presented as documentation.
- [ ] Internal-only or sensitive content is not exposed publicly.
- [ ] Sources of truth are clear and no derived output competes with them.
- [ ] Version identities and last-updated information are accurate.
- [ ] A successor can determine where to start and what remains unresolved.

## Standard entry templates

### Decision

```markdown
## [Decision] -- YYYY-MM-DD

**Owner:** [Person or role]

### Context
[Why a decision was needed]

### Decision
[What was chosen]

### Alternatives
[What else was considered]

### Consequences
[Benefits, costs, risks, and follow-up work]
```

### Changelog release

```markdown
## [Application Version or Dated Release] -- YYYY-MM-DD

### Added
- New capability.

### Changed
- Updated behavior.

### Fixed
- Corrected issue.

### Removed
- Removed deprecated behavior.

### Verification
- Checks run, results, evidence, and skipped checks with reasons.
```

## Protocol governance

- Only the owner or an explicitly authorized maintainer may approve changes to this governing protocol.
- Project-specific needs belong in the project's authoritative records; they must not silently rewrite the installed protocol.
- Improvements discovered in a project should be proposed back to the governing protocol, reviewed, versioned, and then distributed as an explicit upgrade.
- Preserve source lineage and the protocol change history.

## Ownership and attribution

**JDAC Development Documentation Protocol™**  
**Owner:** Jonathan Schafer / JDAC, LLC  
Copyright © 2026 JDAC, LLC. All rights reserved.

JDAC Development Documentation Protocol™ is a proprietary JDAC methodology and governing documentation standard. Usage, modification, redistribution, and attribution terms are stated in this file’s Usage, Ownership, and Attribution section.

**Contact**  
Jonathan Schafer  
JDAC Systems / JDAC, LLC  
[JDAC.ai](https://jdac.ai)  
[Jonathan@JDACLLC.org](mailto:Jonathan@JDACLLC.org)

## Source lineage

This approved governing release consolidates and reconciles:

- IP-15 JDAC Development Documentation Protocol draft v0.1
- IP-12 PageSweep Documentation Protocol v0.1.0 and its identical project copy
- StickerReady NHA CPT Prep project protocol, App Version 2.2.1
- JDAC Marketing Site project protocol
- CareSync End-User Documentation Protocol Generator source v0.1
- JDAC Documentation Protocol Overview v1.0
- JDAC Documentation Protocol Quick Start v1.2

Project-specific copies remain evidence of implementation and do not become competing master protocols.

## Version history

| Date | Protocol Version | Change |
|---|---:|---|
| 2026-10-03 | 2.0.5 | Standalone protocol release with self-contained usage terms; preserved initial project evaluation, concise questions, profile confirmation, installation and reconciliation gates, and all ongoing governance rules. No separate scored assessment is included or required. |
| 2026-09-16 | 2.0.4 | Removed obsolete draft, review-candidate, and pending-legal-review language from the approved governing release; reorganized ownership and usage terms for the then-current distribution format; no operational protocol behavior changed. |
| 2026-09-06 | 2.0.3 | Added **Fresh Bootstrap** for platforms that necessarily create the project and first substantive implementation in the same initial request; allowed verbatim protocol installation and proportionate documentation initialization during that first build while preserving anti-fabrication, smallest-sufficient-set, authority-collision, verification, and post-bootstrap disclosure requirements; retained the separate confirmation and authorization gates for later Fresh, In Flight, and Unclear adoption. |
| 2026-09-06 | 2.0.2 | Added an explicit proportional-documentation decision sequence and authority-collision check; required reuse of existing authoritative responsibilities before creating new records; prohibited duplicate or shadow histories such as `DOC_CHANGELOG.md`, `RELEASE_LOG.md`, or separate documentation-history ledgers; strengthened `CHANGELOG.md` as the sole authoritative history for material product, operational, release, and documentation changes. |
| 2026-09-06 | 2.0.1 | Required the AI to infer and recommend the smallest justified documentation set from project evidence; prohibited asking users to choose "full suite vs. reduced set" or otherwise design the documentation architecture when applicability can be determined by the protocol; reinforced fresh-project anti-fabrication behavior and exact-record disclosure in the post-install reconciliation proposal. |
| 2026-09-03 | 2.0.0 | Promoted release candidate rc.4 without substantive rule changes after controlled validation across Garage Gazette, CareSync, and StickerReady on Lovable and Base44. |
| 2026-09-02 | 2.0.0-rc.4 | Required a dedicated `HANDOFF.md` for high-consequence projects even when no recipient exists, with an honest readiness record for access ownership, transfer prerequisites, unresolved dependencies, risks, and verification still required. |
| 2026-09-02 | 2.0.0-rc.3 | Added mandatory pre/post revision comparison after the CareSync activation triggered an automatic Supabase type-file change during an intended read-only inspection. |
| 2026-09-02 | 2.0.0-rc.3 | Required immediate disclosure and stop when inspection causes code generation, schema synchronization, formatting, dependency updates, plan persistence, or another incidental mutation; any cleanup requires separate authorization. |
| 2026-09-02 | 2.0.0-rc.2 | Corrected the first-install sequence so read-only project profiling and confirmation occur before protocol installation, followed by separate installation and reconciliation authorizations. |
| 2026-09-02 | 2.0.0-rc.2 | Replaced the contradictory install-first activation command with a no-install inspection command and explicitly prohibited plan-artifact creation during activation. |
| 2026-09-02 | 2.0.0-rc.1 | Established the first formally versioned release candidate of the consolidated governing protocol. The 2.0 major version reflects the move from project-specific documentation instructions to a cross-platform operating standard with staged adoption, reconciliation, evidence, version separation, exceptions, and handoff governance. |
| 2026-09-02 | 2.0.0-rc.1 | Preserved the Garage Gazette pilot corrections from draft v0.6 for read-only and plan-mode integrity. |
| 2026-09-02 | 0.6 Draft | Defined read-only and plan-mode integrity after the Garage Gazette pilot showed that a builder may persist a plan artifact during a proposal-only phase. |
| 2026-09-02 | 0.6 Draft | Required disclosure and evidence exclusion for unavoidable platform-managed planning artifacts and prohibited claiming the project was untouched when any durable artifact changed. |
| 2026-09-02 | 0.5 Draft | Separated profile confirmation, protocol installation authorization, reconciliation proposal, reconciliation authorization, execution, and closeout into distinct gates. |
| 2026-09-02 | 0.5 Draft | Prohibited protocol installation from implying documentation reconciliation and required explicit pending reconciliation metadata until the approved work is completed and verified. |
| 2026-09-02 | 0.4 Draft | Added a concise activation-profile format, normally limited material questions to three or four with five as the absolute maximum, and prohibited activation from becoming a detailed audit. |
| 2026-09-02 | 0.4 Draft | Designated `DECISION_LOG.md` as the default authoritative exception record, with linked triage and handoff references only when applicable. |
| 2026-09-02 | 0.4 Draft | Clarified that recipients may modify their own project documentation but may not alter or derive the governing protocol without written authorization; standardized attribution to Jonathan Schafer. |
| 2026-09-02 | 0.3 Draft | Added fresh-versus-in-flight activation, evidence-based project profiling, a five-question ambiguity limit, and confirmation before documentation initialization or reconciliation. |
| 2026-09-02 | 0.3 Draft | Standardized the README Documentation Status block, test-run evidence, handoff verification evidence, and controlled exception records. |
| 2026-09-02 | 0.3 Draft | Added outward-facing trademark, attribution, internal-use, modification, and redistribution terms for owner and legal review. |
| 2026-09-02 | 0.2 Draft | Consolidated the governing standard across PageSweep, StickerReady, JDAC Marketing Site, CareSync lineage, and the two outward-facing operational blueprints. |
| 2026-09-02 | 0.2 Draft | Separated Protocol Version, Application Version, Documentation Last Reconciled With, and Document Last Updated. |
| 2026-09-02 | 0.2 Draft | Added install-unchanged activation, initial read-only project evaluation, proportional documentation rules, explicit record authority, and platform-aware equivalents. |
| 2026-09-02 | 0.2 Draft | Defined universal handoff outcomes, conditional `HANDOFF.md` triggers, acceptance requirements, and review events. |
| 2026-09-02 | 0.2 Draft | Preserved the PNG quick-start core and release gates while clarifying conditional records, generated outputs, and stakeholder-deck support. |

---

JDAC Development Documentation Protocol&trade;  
Jonathan Schafer | JDAC Systems / JDAC, LLC  
[JDAC.ai](https://jdac.ai) | [Jonathan@JDACLLC.org](mailto:Jonathan@JDACLLC.org)
