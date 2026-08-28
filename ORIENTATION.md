# Logi Report: a product briefing

Read this before answering anything from this repository. Logi Report carries two
renames, a name collision with an unrelated product, a version series with a
three-number hole in it, and documentation spread across three hosts. Each of
those has already produced a wrong answer in the field. What follows is what the
evidence supports, with the source named.

## What the product is

Logi Report is a Java reporting platform for pixel-perfect, paginated, scheduled
output. Its own product overview calls it "a complete Java reporting solution",
built on "a 100% Java EE architecture and a rich set of APIs", designed to be
embedded into an application. The devnet category description for the product
reads "Logi Report delivers embedded operational and pixel-perfect reporting".
The documents it is sold to produce are invoices, customer letters, compliance
documents and tightly branded PDFs.

Two shipping components:

- **Logi Report Server**, the reporting engine, scaling from a single CPU to a
  cluster. It exposes Java and JavaScript APIs, a Server Console, and URL
  invocation over HTTP GET or POST for running, scheduling and creating reports.
  Its system database is three logical databases: system, realm and profiling.
- **Logi Report Designer**, a Swing-based IDE. Reports and business views are
  authored here and published to Server for generation, delivery and management.

The browser-side and server-side modules are called studios: **Page Report
Studio** (dynamic viewer for page reports, with filter, search, sort and drill),
**Web Report Studio** (interactive web report viewer and designer), **Catalog
Studio**, the Template Editor, and from v19.2 a server-side **Logi Report
Studio** for page report templates. **JDashboard** and **Visual Analysis** are
separately licensed add-ons.

The object model, which is where most of the real vocabulary lives:

- A **catalog** is an OS folder holding a catalog file plus report object files.
  The catalog file carries database connections, tables and views, stored
  procedures, imported queries, user data sources, queries, business views,
  parameters, formulas and summaries. Formats are binary `.cat` (Designer only)
  and XML `.cat.xml`.
- A **business view** is the semantic layer: connections plus relationships
  between view elements, typed as category, group, aggregation and detail
  objects. Web reports take business views as their only data source.
- Report files are `.cls` for page reports and `.wls` for web reports. A page
  report can contain multiple reports; a web report holds exactly one.
- Data security is Business View Security, Record Level Security and Column
  Level Security, applied on catalog data objects.
- Export formats at v19: Mail, Logi Report Result, HTML, PDF, Excel, Text, RTF,
  XML, PostScript and Fax.

Lineage, both legs publicly cited. Jinfonet Software (founded 1998) was acquired
by Logi Analytics, announced 12 February 2019 (GlobeNewswire). Logi Analytics
was acquired by insightsoftware, announced 7 April 2021 (PRNewswire; CRN dated
it 6 April 2021).

## The rename: JReport became Logi Report at v17

Grounded three independent ways.

**The documentation sentences either side of the boundary are the same bytes
apart from the product name.** The v15 Get Started Guide opens "Logi JReport is
a complete Java reporting solution that provides sophisticated…"; the v17 copy
of the same article opens "Logi Report is a complete Java reporting solution
that provides sophisticated…". The feature-guide overview does the same thing:
"significant features of Logi JReport using GIF animations" at v16, "significant
features of Logi Report using GIF animations" at v19. The feature-guide topic
set stayed flat across the boundary, 45 topics at v16, 45 at v17, 46 by v17.1,
and the single net-new topic in that whole span is Flexible Time Zone Options.
Every other v16-to-v17 title change is a rename.

**The vendor acknowledges the lineage in the current documentation.** The v26
Designer Guide overview opens "Report Designer (formerly Logi JReport Designer)
is a Swing-based Integrated Development Environment", which is insightsoftware
naming the predecessor itself rather than a reader inferring it.

**The documentation host moved off the Jinfonet domain in the same era.** Every
v15 to v19 article in this mirror was published on `devnet.logianalytics.com`,
so by the time the v17 pages went up the product already sat under the Logi
Analytics domain rather than jinfonet.com.

The devnet documentation index agrees on the boundary: v17 and above are labelled
Logi Report, v16 and v15 Logi JReport.

### The rename was cosmetic, and it is still incomplete

Six years on, the JReport name is load-bearing in the build, the code and the
order-to-cash tooling:

- The JavaScript API is still one file called **`jreportapi.js`**, documented as
  such on the live v26 site, shipped at
  `<install_root>\public_html\webos\jsvm\lib`. The demo pages are
  `jreportapi-demo-rpt.html` and `jreportapi-demo-dsb.html`.
- v17.1, **after** the rename, added a brand new Java package
  `com.jinfonet.security.jacl` (replacing `java.security.acl`, which Oracle
  removed from JDK 14). The code namespace stayed Jinfonet by choice, not by
  neglect.
- The Designer main class is `com.jinfonet.designer.JReport`. The Server WAR is
  `jreport.war` with a `jinfonet/` folder of Server Console JSPs inside. The
  servlet is `jrserver` and the URL parameter namespace is `jrs.*`
  (`jrs.report`, `jrs.catalog`, `jrs.cmd`, `jrs.result_type`, `jrs.param$…`).
  Catalog classes carry a `JetU` prefix (`JetUJDBCConnection`, `JetUTableView`,
  `JetUFileQuery`, `JetUPrejoin`).

Commercially the old name has receded: current v26 documentation drops the "Logi"
prefix entirely and speaks of Report Designer and Report Server. Inside the
product the JReport and Jinfonet strings are still the correct, current ones, so
reproduce them exactly rather than "correcting" them.

## The name collision, which is a live trap

**"Logi Report" is the name of two unrelated products, and the internet will hand
you the wrong one.**

Logi Analytics (as LogiXML) began marketing a product called **Logi Report** in
2004, previously called **LGX Report**, described as a free web-based BI
reporting tool. The devnet Logi Info corpus documents it as a cut-down edition of
Logi Info, authored in Logi Studio (a stand-alone Windows .NET application)
targeting IIS or Java web servers, at versions 10 and 11. It was later retired.

That product has **no Jinfonet lineage whatsoever**. It is not an ancestor of the
Logi Report in this repository. The name was simply free by the time v17 shipped
in 2020, and was reused for the renamed JReport.

The two are documented in mutually exclusive corpora: a grep for "JReport" over
the entire devnet Logi Info tree returns zero files.

So: anyone researching "Logi Report history" from public sources will land on
2004, LogiXML, and a free web reporting tool, and will conclude the product is
twenty-two years old under that name and came out of Logi Analytics. Every part
of that is wrong for this product. The product in this repository is JReport,
built by Jinfonet, renamed in 2020.

## The version map

    v15 (2017 Q4)  v15.6 (2018 Q4)  v16      <- named Logi JReport
    v17 (2020 Q2)  v17.1  v18 (30 Apr 2021)  v19 (to 19.2.3)
    23.1 (31 Jan 2023)  23.2  23.3  23.4
    24.x   25.x (25.1 31 Mar 2025, 25.3 30 Sep 2025)
    26.x   26.1  26.2 (30 Jun 2026)  <- current

**There was never a v20, v21 or v22.** The release line runs 19.2.3 straight
into 23.1, both dated 31 January 2023, with nothing between them. The hole shows
up twice in the public documentation: paging all 2,418 article titles on
docs-report.zendesk.com, a regex for v20, v21 or v22 returns nothing (release
notes run v23.1, v23.2, v23.3, v23.4, v24.1, v24.3, v25.1, v25.3), and scanning
all 314 devnet section names returns nothing either. The v19 series gave way to
year-dot-quarter calendar versioning at 23.1.

Current is **26.2**, released 30 June 2026. The product is not sunset: the v26
documentation carries dated release notes through 2026, and the 26.2 line was
still shipping updates when this snapshot was taken. No published end-of-life or
end-of-support date for Logi Report was found on any of the three documentation
hosts.

One feature-level closure is worth knowing, because it is not product EOL:
JDashboard was sunset in the documentation at v19.1, though a module of that name
still ships at v26.

## Why the documentation is split across hosts

| Host | Versions | Scale |
|---|---|---|
| `devnet.logianalytics.com` | v15, v16, v17, v17.1, v18, v19 | 9,344 articles, ends 31 Jan 2023 |
| `docs-report.zendesk.com` | v23, v24, v25 (v23 marked Archive) | 2,418 articles, oldest created 23 Jan 2023 |
| `logi-report-v26.insightsoftware.com` | v26 | 1,473 articles, category last updated 31 Jul 2026 |

**The devnet corpus stops dead on 31 January 2023 because the documentation
moved that day, not because the product stalled.** The 23.1 release notes were
published on docs-report.zendesk.com; Logi Composer's docs left devnet for
docs-composer.zendesk.com in the same move. v24 was briefly split across a devnet
landing page and Zendesk section pages, which is exactly why a devnet-only mirror
looks truncated. v26 then moved again, to an insightsoftware-hosted Zendesk. A
fourth move, to Mintlify from MadCap Flare and Zendesk, was in progress in 2026.

Staleness in the devnet snapshot is therefore a hosting artefact. Of its 9,344
articles, 6,113 date to 2021 and 3,165 to 2022. Do not read that as evidence of
an abandoned product; read the v26 host, which carries dated release notes with
customer case numbers on them.

Two stale links to know about: the devnet index points at v26 sections
31291757367821 and 44224754072461, neither of which exists on the live v26 site.
The canonical ids are 45189079491341 (Designer) and 45202990176141 (Server).

## What Logi Report is not

**Logi Report and Logi Composer are different products.** They are not versions
of each other, not tiers of each other, and not a successor and predecessor pair.
The separation is total:

- Separate engineering histories: Logi Report descends from Jinfonet's JReport,
  Composer from a different acquisition entirely, and the two are tracked,
  built and supported as separate products.
- Different documentation sites, with no shared publishing pipeline.
- **They were documented in total isolation for a decade, and v26 is the first
  release where they connect.** This claim was previously written as "zero shared
  documentation surface in both directions" and an adversarial review refuted it.
  The refutation matters, so the corrected position is stated in full:

  *Composer to Report:* the current Composer v25 and v26 documentation (1,774
  files) mentions "Logi Report", "JReport", "Jinfonet", "pixel-perfect" and
  "Report Designer" zero times each. That direction is genuinely clean.

  *Report to Composer:* **not clean.** Report-side documentation writes the
  product name as plain "Composer", never "Logi Composer", so a grep for the full
  name returns zero and looks like proof of isolation. Searching for "Composer"
  alone finds five files, **all of them v26**:

  ```
  cd ~/logi-report-kb
  for d in docs/jreport-v15-v16 docs/logi-report-v17-v19 docs/unversioned \
           docs/current/v23-v25 docs/current/v26; do
    echo "$d -> $(grep -rl 'Composer' $d --include='*.md' | wc -l)"
  done
  # 0, 0, 0, 0, 5
  ```

  What those five contain is a real product integration, new in v26.2 and dated
  30 July 2026. `Composer Trusted Access Credentials` documents a system-level
  Client ID and Client Secret "shared by every Composer import in Catalog Studio,
  connection refresh, Composer Source import, and Server Console Composer User or
  Group import". The v26.2 release notes add: "Composer source content can now be
  translated to BV (Business View), enabling seamless migration and reuse of
  existing Composer report definitions within the BV environment."

  So the accurate statement is: separate products, separate lineages, and no
  documentation overlap at all from v15 through v25. Then in v26 Logi Report gains the ability to import from Composer
  and translate Composer sources into Business Views. Anyone selling or migrating
  needs to know that path exists, and that it is only months old.
- They share the number 26 because both sit on a common calendar release train.
  A customer seeing v26 on both must not infer a single product.

The word that causes the trouble is "report", because Composer uses it for
something else. A Composer **scheduled dashboard report** renders an existing
dashboard on a timer and mails it out. It is produced by a screenshot
microservice, not a report layout engine; PNG output defaults to 1280 by 720
pixels, set by `dashboard.scheduling.screenshot.png.width/height`. Formats are
PDF, PNG and XLSX (raw data or visual data); delivery is EMAIL by default or
FILE_DROP to SFTP. The unit being scheduled is a dashboard, never a report
definition. The Composer REST API bears this out: the only report endpoints are
dashboard-report settings CRUD under `/api/dashboards/{dashboardId}/reports`,
and across its tags there is no report catalogue, layout, template, page or
render endpoint. Composer's own documentation has no crosstab and no report
bursting.

Logi Report, by contrast, is the banded, paginated engine: `.cls` page reports
and `.wls` web reports against `.cat` catalogs, smart pagination, automatic
subtotals, Table of Contents with page numbers, barcode symbologies (PDF417 and
Datamatrix added recently), and export to PDF, Excel, RTF, PostScript and Fax. Pixel-perfect, paginated
output is what Logi Report is sold to do, and Composer's own documentation does
not claim it.

**This section exists because the confusion is real.** The product is routinely
referred to by approximations such as "logi reporter" or just "reporting", which
leaves the listener unable to tell which product is being described. Use the full
name, and say "paginated" or "pixel-perfect" when that is what is meant.

### Naming hygiene

"Logi Symphony" is a **deprecated** bundle name for what is now Logi Composer.
Do not use it as a live product name. Be aware that insightsoftware's own public
Logi Report page still does, in a FAQ heading contrasting Logi Report
"Reporting" with Logi Symphony "Reporting" (accessed 22 August 2026), so a
customer may well arrive using it.

The current product name is **Logi Report**, and the current documentation calls
its two components Report Designer and Report Server. Use those.

## Who else ships it

**InterSystems Reports is OEM'd Logi Report.** InterSystems' own community site
states "InterSystems Reports is powered by Logi Report, a product of
insightsoftware." InterSystems Reports 25.1 bundles Logi Report 25.1;
InterSystems Reports 24.1 bundles Logi Report 24.1SP2. So a customer describing
InterSystems Reports behaviour is describing Logi Report behaviour, on a version
that tracks the Logi Report release.

OEM is a first-class channel here rather than an accident: the product uses
server-based licensing, and the documentation describes the Design API and Server
Design API as separately licensed surfaces intended for exactly that kind of
embedding.

## What this briefing does not settle

- No end-of-life or end-of-support date for Logi Report is published on any of
  the three documentation hosts. Absence of a date is the finding; do not invent
  one, and do not read it as a guarantee either.
- Per-version supported-platform matrices were not found in the documentation
  swept for this mirror.
- Secondary summaries of the Logi product family routinely transpose the founding
  years of Jinfonet (1998) and LogiXML (2000) between Logi Report and Logi Info.
  Check any per-product attribution against the acquisition announcements above.

## Where to go next

- [README.md](README.md) for what this repository contains, how it was pulled,
  and its limits.
- [`docs/`](docs/) for the mirrored articles, one directory per era.
- [`llms.txt`](llms.txt) and [`MANIFEST.json`](MANIFEST.json) for the index.
