# Logi Report knowledge base — how to use this repo

You are reading this because someone asked you to do something with Logi Report:
build a report, design a demo, answer a how-to, or debug a deployment. Everything
you need is in this repo. Do not search the web first; search here first.

## Before anything else: three products share this name

This is the most common way to get Logi Report wrong, and two of the three wrong
answers sit inside insightsoftware's own documentation.

| Which | What it is | In this repo? |
|---|---|---|
| **JReport, renamed Logi Report at v17** | Java, pixel-perfect paginated reporting. Server, Designer, Page and Web Report Studio, JDashboard. Currently v26.2. | **Yes. This repo is entirely about this one.** |
| A LogiXML product called "Logi Report", around 2004 | Formerly LGX Report, a free web-based BI reporting tool, later retired. No Jinfonet lineage. | No. This is what a public web search will return. Ignore it. |
| A cut-down edition of **Logi Info**, also called "Logi Report" | v10/v11, built in Logi Studio, a Windows .NET IDE. A different product line entirely. | No. It lives in the devnet `logi-info` corpus, which this repo excludes. |

If a user says "Logi Report" and anything about the context smells like .NET, Logi
Studio, or a free web BI tool, stop and confirm which product they mean before
answering. Inside this repo, "Logi Report" always means the first row.

## And it is not Logi Composer

Logi Report and Logi Composer are separate products. They share no documentation
surface at all: zero hits for "Logi Report", "JReport", "pixel-perfect" or
"Report Designer" across the whole current Composer documentation set.

- **Logi Report** does pixel-perfect, paginated, scheduled reporting against a
  catalogue of report definitions.
- **Logi Composer** does dashboards and embedded analytics. Its "reports" are
  dashboard screenshots on a timer, delivered as PDF, PNG or XLSX by email or
  file drop. The report unit is a dashboard, never a report definition, and it
  has no catalogue, template, page or render endpoint.

If someone asks for pixel-perfect, paginated, banded, sub-reports, page headers
and footers, bursting, or a Crystal Reports replacement, they want Logi Report.
If they ask for interactive dashboards or embedded self-service analytics, they
want Composer and this repo will not help them. Say so rather than improvising.

"Logi Symphony" is a deprecated name for Logi Composer. Do not use it as a live
product name, even though insightsoftware's own public site still does.

## How to search this repo

Start with the index, not with grep over 13,235 files.

- `MANIFEST.json` — every document with title, id, section, era, source URL,
  body hash and duplicate grouping. **It is about 10MB. Never `cat` or `Read` it
  whole; filter it in code.** `llms.txt` is 1.8MB, same warning.
- `llms.txt` — the same index grouped by era and section, in the llms.txt
  convention.
- `ORIENTATION.md` — what the product is, the version map, the lineage.
- `api/README.md` — which API surface to reach for.
- `building-reports/README.md` — task-oriented routing. **Start here for
  anything of the form "how do I build X".**

**The most important retrieval fact about this corpus: half of it is reference,
not instructions.** 6,518 documents are property tables and dialog-box reference,
against 1,719 procedural ones. So a title search for "chart" returns "Chart
Legend Properties" long before it returns anything telling you how to add a
chart. When the user wants to DO something, filter `doc_kind == "procedural"`
first, and fall back to `reference` only for the specific property they need.
Better still, start at [building-reports/README.md](building-reports/README.md),
which exists precisely because raw retrieval over this corpus misleads.

About 9% of the corpus is a byte-identical copy of another document, because
upstream publishes the same article under several Zendesk ids, both across
Designer and Server and across versions. Nothing has been deleted, because two
identical articles in different versions tell you the topic did not change.
Filter on `is_canonical` to collapse duplicates, and check `uses_jreport_naming`
when you need to know whether an unversioned article predates the v17 rename.

A reliable pattern:

```bash
python3 -c "
import json
m = json.load(open('MANIFEST.json'))
for d in m['documents']:
    if (d['is_canonical'] and d['doc_kind'] == 'procedural'
            and 'crosstab' in d['title'].lower()):
        print(d['era'], d['path'])
"
```

Prefer `docs/current/` when the user has not named a version, because 9,344 of
the 13,235 articles describe v15 to v19 and unfiltered retrieval skews old.

Then read the specific file. Prefer reading two or three whole documents over
grepping fragments across hundreds.

## Which era to use

`docs/` is split four ways, and the split is honest about what it does not know.

| Directory | What it holds | Use it when |
|---|---|---|
| `docs/current/v26/` | v26, 1,473 articles | **Default.** Current is v26.2. |
| `docs/current/v23-v25/` | v23, v24, v25, 2,418 articles | The customer names one of these versions. |
| `docs/logi-report-v17-v19/` | v17, v17.1, v18, v19, 5,039 articles | The customer is on v17-v19, or you need detail the newer docs dropped. |
| `docs/jreport-v15-v16/` | The JReport era, 2,637 articles | The customer says "JReport", or is on v15 or v16. Patches were still being cut against v15.6 in August 2026, so these installs are live. |
| `docs/unversioned/` | 1,668 articles whose section and frontmatter state no version | Last resort. Do not assume an era for these; the source does not give one. |

There was never a v20, v21 or v22. Release history runs 19.2.3 straight into
23.1, both dated 31 January 2023. If a user mentions v21, they are mistaken or
talking about a different product.

Answer from the era the user is actually on. A v26 procedure given to someone on
v16 is worse than saying you need to check.

## The product name has THREE stages, and current docs use the third

This directly affects how you search. Counts are files whose BODY text (excluding
this repo's own frontmatter) contains each phrase:

| Era | files | "Logi JReport" | "Logi Report" | bare "Report Designer" |
|---|---|---|---|---|
| `jreport-v15-v16` | 2,637 | 1,462 | 1 | 659 |
| `logi-report-v17-v19` | 5,039 | 8 | 2,275 | 6 |
| `current/v23-v25` | 2,418 | 4 | 71 | 128 |
| `current/v26` | 1,473 | 2 | 38 | 93 |

So: **Logi JReport** (v15-v16), then **Logi Report** (v17-v19), then in the current
documentation the "Logi" prefix is largely dropped and it is simply **Report
Designer** and **Report Server**. All 35 v26 section titles are named that way;
none contains "Logi".

**Consequence: searching the current corpus for "Logi Report" finds almost
nothing.** Only 38 of 1,473 v26 files use that phrase. Search for "Report
Designer", "Report Server", or the feature name instead. Searching the v15/v16
corpus has the mirror problem: search "JReport" there, not "Logi Report".

The v26 Designer Guide overview states the lineage itself: "Report Designer
(formerly Logi JReport Designer) is a Swing-based Integrated Development
Environment". That parenthetical is the vendor's own acknowledgement, not a
leftover.

## Naming inside the code never changed

The v17 rename was cosmetic and remains incomplete. These are still in the
**current v26** documentation, so when you see them they are correct and current,
not stale typos. Counts are files in this repo mentioning each term:

| Internal name | JReport era | v17-v19 | current (v23-v26) |
|---|---|---|---|
| `com.jinfonet.*` packages | 29 | 39 | 29 |
| `jreport.war` | 14 | 42 | 34 |
| `jet.server.servlets.JRServlet` | 11 | 13 | 8 |
| `jreportapi.js` (the JavaScript API) | 1 | 5 | 2 |
| `jrs.` URL parameter prefix | 64 | 108 | 89 |
| `~/.jreport/default` report home | 3 | 12 | 8 |

Java packages are `jet.*` and `com.jinfonet.*`, and the Designer main class is
`com.jinfonet.designer.JReport`.

So a user seeing "jreport" or "jinfonet" in a stack trace, a filename, a WAR name
or a URL parameter is on a current, supported Logi Report. Reassure them rather
than sending them hunting for something ancient. Reproduce these strings exactly;
do not "correct" them to "logireport".

## Repo layout

```
docs/            13,235 documentation articles, split by era (see above)
api/             the API surfaces: server, catalog, design, security,
                 information bus, RMI, JavaScript, URL invocation
building-reports/  task-oriented guides. The demo layer.
scripts/
  build_index.py   regenerates MANIFEST.json and llms.txt
  pull_docs.py     refreshes docs/current/ from the live Zendesk APIs
  verify_kb.py     the gate. Run it after any change.
```

After changing anything under `docs/`, run `python3 scripts/build_index.py` then
`python3 scripts/verify_kb.py`. The gate fails if the manifest and the tree
disagree in either direction.

## Honest limits, so you do not overclaim

- **This is a documentation mirror, not the product.** You cannot verify that a
  procedure works, only that the documentation says it. For a demo, say which
  version the guidance came from.
- **`docs/current/` was converted from HTML.** Tables are preserved (637
  articles carry one), but complex layout, images and some nesting are lost.
  Every document carries its `url` in the frontmatter; that page is the
  authority when the conversion is unclear.
- **No Javadoc is included.** The Java API reference exists publicly for v19
  through v24 at `reportkbase.logianalytics.com`, but not for v25 or v26.
  `api/` describes the surfaces from prose documentation, which is thinner than
  a class reference.
- **No public REST admin API is documented.** If someone asks for one, the
  answer is that the documented surfaces are the Java APIs, the JavaScript API
  and URL invocation.
- **Snapshot dated in `docs/current/PROVENANCE.json`.** Documentation changes.
  Re-run `scripts/pull_docs.py` before relying on it for anything current.
- **JDashboard has been in maintenance mode since v19** ("we will not be adding
  new features to it"). The phrase appears in 16 v17-v19 files and is still in 39
  current v23-v26 files, and in none from the JReport era, so the freeze began at
  v19 and still holds. Do not build a demo around JDashboard without flagging it.
