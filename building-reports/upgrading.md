# Upgrading, and whether existing reports break

Added after an adversarial review found this repo had no route at all for one of
the most routine presales questions: "we are on an old version, does upgrading
break our reports?" Searching the whole authored layer for upgrade, migrate,
backward or compatible returned one hit, and it was about PDF encryption.

This page is deliberately short and points at primary sources, because the honest
answer to the question is version-specific.

## The upgrade mechanism

Install the new version over the old directory. Back up the system database
first. Old resources are backed up to `bak\previous_version`. Migration tools are
only needed when coming from below v6.0. Both upgrade paths require converting
the old report resources so they comply with the new server version.

Source: [Upgrading Report Server (v26)](../docs/current/v26/introduction-to-report-server/45203988660237-upgrading-report-server.md),
and the [install or upgrade checklist (v26)](../docs/current/v26/introduction-to-report-server/45203975545357-checklist-for-an-install-or-upgrade-of-report.md).
For v25, see [Upgrading Report Server (v25)](../docs/current/v23-v25/introduction-to-report-server-v25/28891674626829-upgrading-report-server.md)
and [Migrating Server and Server data (v25)](../docs/current/v23-v25/introduction-to-report-server-v25/28891700527245-migrating-server-and-server-data.md).
On Docker: [Using and upgrading Report Server on Docker](../docs/current/v23-v25/starting-accessing-and-shutting-down-report-server-v25/28891673170573-using-and-upgrading-report-server-on-docker.md).

The concrete backup and restore commands (`MigrationTool -backup:<path>` and
`-restore:<path>`) are in
[Using the Migration Tool](../docs/unversioned/faqs/360050379574-using-the-migration-tool-to-upgrade-logi-report-server-from.md).

## "Will my reports render the same?" Read the release notes, not the guides

This is the part the upgrade guides do not answer and the part the customer
actually cares about. Rendering behaviour has demonstrably drifted across major
versions, and the evidence lives in release notes as fixed regressions. Two real
examples from the v26.2 notes:

- "On New Page Behavior Change from v19 to v24"
- "BF Section New Page Property Ignored in v26"

Source: [Report v26.2 Release Notes (Server)](../docs/current/v26/release-notes-for-report-server/47013071115789-report-v26-2-release-notes.md)
and [Report v26.2 Release Notes (Designer)](../docs/current/v26/release-notes-for-report-designer/47011446368781-report-v26-2-release-notes.md).

**So the method for answering the question honestly is:** identify the customer's
current version and the target, then read every release-notes section between
them for entries describing behaviour changes rather than new features. Those
sections are under `../docs/current/v26/release-notes-for-report-server/`,
`../docs/current/v23-v25/`, and for the older line
`../docs/logi-report-v17-v19/release-notes-for-logi-report-server-v19/`.

Do not answer "it will be fine". The corpus does not support that, and the notes
above show it has not always been true.

## A related trap in this repo

[gotchas.md](gotchas.md) documents an `On New Page` formula technique drawn from
a v19-era FAQ. The v26.2 note above records that `On New Page` behaviour changed
between v19 and v24. If you are advising someone on v24 or later, verify that
technique against their version before relying on it.

## Customers on the JReport era are still live

Patches were still being cut against v15.6 in August 2026, so a v15 or v16
installation is not automatically unsupported. See [ORIENTATION.md](../ORIENTATION.md)
for the version map and what changed at the v17 rename.
