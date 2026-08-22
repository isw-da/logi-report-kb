# Building reports: the task router

Task-oriented layer over the 13,235-article Logi Report corpus in `../docs/`. Start
here, find your task, follow the link.

These guides were written against the v15 to v19 documentation, which is the most
detailed the corpus holds. The current v23 to v26 documentation is in
`../docs/current/` and covers the same ground more tersely. Check there before
quoting a procedure to anyone on v23 or later, and note that current docs call the
products simply "Report Designer" and "Report Server", dropping the Logi prefix.

Logi Report is insightsoftware's Java paginated and embedded reporting product:
Logi Report Designer (the IDE), Logi Report Server (the runtime), Page Report
Studio, Web Report Studio, JDashboard, and Visual Analysis. Logi Composer is a
separate product with a separate documentation set and nothing here applies to it.

## I want to...

| Task | Read |
| --- | --- |
| get something on screen fast | [quickstart.md](quickstart.md) |
| understand catalogs, queries, business views, datasets | [concepts.md](concepts.md) |
| decide between a page report and a web report | [page-vs-web-reports.md](page-vs-web-reports.md) |
| build a chart or a crosstab | [charts-and-crosstabs.md](charts-and-crosstabs.md) |
| group by region, quarter, product; sort; top N | [grouping-and-sorting.md](grouping-and-sorting.md) |
| prompt the user for a value, or narrow the data | [parameters-and-filters.md](parameters-and-filters.md) |
| export to PDF or Excel, or schedule delivery | [scheduling-and-export.md](scheduling-and-export.md) |
| run a full demo end to end | [demo-recipes.md](demo-recipes.md) |
| avoid the things that break demos | [gotchas.md](gotchas.md) |
| answer "does upgrading break our reports?" | [upgrading.md](upgrading.md) |

## Straight to a source document

The most-used articles, so you can skip a hop.

**Data layer**

- [Catalogs](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511440151-catalogs.md) - what a `.cat` file holds and why every report needs one
- [Connections](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735506277911-connections.md) - the nine connection types, and a JDBC walk-through
- [Queries](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735519903895-queries.md) - the Query Editor
- [Business views](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735526420375-business-views.md) - group, aggregation, detail, category, hierarchy
- [Track 2: Creating business views](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735519563927-track-2-creating-business-views.md) - the full build
- [Knowing about catalogs](../docs/logi-report-v17-v19/creating-and-managing-catalogs-logi-report-designer-v19/5735520312215-knowing-about-catalogs.md)
- [Data mashup in Logi Report](../docs/unversioned/tactics/360050174113-data-mashup-in-logi-report.md) - combining resources across connections

**Report types and components**

- [Report types](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511454487-report-types.md)
- [Choosing the report type](../docs/logi-report-v17-v19/designing-your-reports-logi-report-designer-v19/5735534332951-choosing-the-report-type.md)
- [Start creating new reports](../docs/unversioned/logi-report-get-started-guide/1500009742142-start-creating-new-reports.md) - every page report starting component
- [Component placement in different report type](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/9898540172311-component-placement-in-different-report-type.md) - the what-goes-where matrix
- [Chart types](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735527491351-chart-types.md)
- [Working with tables](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735512509719-working-with-tables.md),
  [crosstabs](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735498924183-working-with-crosstabs.md),
  [banded objects](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735527064599-working-with-banded-objects.md),
  [tabulars](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735564433175-working-with-tabulars.md),
  [subreports](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735521147415-working-with-subreports.md)

**Tutorial lessons, in build order**

- [Lesson 1: Standard banded report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735563121559-lesson-1-creating-a-standard-banded-report.md)
- [Lesson 4: Chart report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735526174871-lesson-4-creating-a-chart-report.md)
- [Lesson 5: Table report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511197847-lesson-5-creating-a-table-report.md)
- [Lesson 6: Crosstab report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735526201239-lesson-6-creating-a-crosstab-report.md)
- [Lesson 7: Tabular report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735506053399-lesson-7-creating-a-tabular-report.md)
- [Lesson 8: Report with a subreport](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511214359-lesson-8-creating-a-report-that-contains-a-subreport.md)
- [Lesson 9: Parameter-based report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735526219287-lesson-9-creating-a-parameter-based-report.md)
- [Web report, quick start](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735519967383-lesson-1-creating-a-web-report-using-the-quick-start-method.md)
- [Web report, wizard](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735498124567-lesson-2-creating-a-web-report-using-the-wizard.md)

**Server side**

- [Lesson 1: Starting Server](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735563057559-lesson-1-starting-server.md) - console, resource commands
- [Lesson 2: Publishing resources](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511100055-lesson-2-publishing-resources.md)
- [Lesson 3: Running reports](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735497665815-lesson-3-running-reports.md)
- [Lesson 4: Scheduling reports](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511111191-lesson-4-scheduling-reports.md)
- [Lesson 6: Security](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735563090967-lesson-6-security.md)
- [Running reports (v19 server guide)](../docs/logi-report-v17-v19/running-and-scheduling-reports-logi-report-server-v19/5741439314455-running-reports.md)

**Runtime studios**

- [Editing page reports in Page Report Studio](../docs/unversioned/editing-page-reports-in-page-report-studio/1500009691502-editing-page-reports-in-page-report-studio.md)
- [Editing web reports in Web Report Studio](../docs/unversioned/editing-web-reports-in-web-report-studio/1500009719081-editing-web-reports-in-web-report-studio.md)
- [One-select ad hoc operations](../docs/unversioned/one-select-ad-hoc-operations/1500009778981-one-select-ad-hoc-operations.md)
- [Drilling through the report data](../docs/unversioned/drilling-through-the-report-data/1500009691542-drilling-through-the-report-data.md)

**Embedding**

- [Options for embedding reports and dashboards into your software](../docs/unversioned/best-practices/360050173013-options-for-embedding-reports-and-dashboards-into-your-softw.md)
- [Addressing security and authentication for embedding reports](../docs/unversioned/best-practices/360050173193-addressing-security-and-authentication-for-embedding-reports.md)

**Install and prerequisites**

- [Logi Report product overview](../docs/unversioned/logi-report-get-started-guide/1500009742162-logi-report-product-overview.md)
- [System requirements](../docs/unversioned/logi-report-get-started-guide/1500009742182-system-requirements.md)
- [Supported report databases](../docs/unversioned/logi-report-get-started-guide/1500009742062-supported-report-databases.md)
- [Test server installation](../docs/unversioned/logi-report-get-started-guide/1500009769861-test-server-installation.md)
- [Logi Report licenses](../docs/unversioned/logi-report-get-started-guide/1500009769781-logi-report-licenses.md)

## Reading the corpus by era

| Directory | Product name | Notes |
| --- | --- | --- |
| `../docs/jreport-v15-v16/` | Logi JReport | v15 and v16. Designer, Server and Studios all carry the JReport name |
| `../docs/logi-report-v17-v19/` | Logi Report | v17, v17.1, v18, v19. The set to quote by default |
| `../docs/unversioned/` | mixed | no version stated; prose uses both product names |

Where a procedure differs between eras, each file below says so in its own era
note. When in doubt, prefer the v17 to v19 text and check whether the source marks
a feature "new for version 19" before promising it against an older deployment.

## Things this layer does not cover

Server administration, clustering, security system internals, the Java and
JavaScript APIs, URL invocation, national language support, and installation are
all in the corpus but outside these files. Start from
[llms.txt](../llms.txt) at the repo root, which indexes every article by section.
