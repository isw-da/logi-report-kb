# Gotchas

Things that bite, taken from the FAQs, best practices, and the warnings buried in
the design guides. Ordered roughly by how likely they are to ruin a demo.

## Design decisions you cannot undo cheaply

**A page report's data resource type is fixed at creation.** The **Create Using
Business View** option decides whether the page report is query-based or business
view-based, and every data component in it must then use that type. There is no
mixing. Source:
[Inserting crosstabs in a report](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735527515799-inserting-crosstabs-in-a-report.md).

**Some starting components disappear in a business-view-based page report.**
Designer does not offer Horizontal Banded, Mailing Label, or Tabular when you add a
report tab to a business-view-based page report. Source:
[Creating reports](../docs/logi-report-v17-v19/designing-your-reports-logi-report-designer-v19/5735569787671-creating-reports.md).

**3-D charts are page-report-and-query only.** Business-view-based page reports,
web reports, and library components take 2-D charts. KPI is unavailable in
query-based page reports. Full matrix:
[Component placement in different report type](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/9898540172311-component-placement-in-different-report-type.md).

**Charts cannot go everywhere in a banded object, in a page report.** In both the
query-based and business-view-based page report tables, Chart is allowed in the
banded header, footer, group header, and group footer panels but not in the banded
page header, detail, or page footer panels. In a web report the same matrix marks
Chart as allowed in all of those panels, which is why the tutorial can drop a chart
into a banded object inside a web report. Check the table for your report type
rather than assuming. Same source.

**Query filter versus dataset filter.** A query filter changes the catalog and
therefore every report built on that query. If you only meant to filter this
report, use a dataset filter, which still pushes down to the database. Source:
[Filtering reports](../docs/logi-report-v17-v19/designing-your-reports-logi-report-designer-v19/5735534181911-filtering-reports.md).

**Component filters do not push down.** All the data comes back and the engine
filters locally. The documentation calls this very inefficient, and it usually
cannot be pushed down even with Push Down Group Query enabled. Same source.

## Layout and rendering

**A crosstab that splits across pages.** Pagination mode is the default and a wide
crosstab lands on two pages, which kills the read. Clear **Page Layout** on the
**View** menu tab for continuous mode. **Items per Row Block** and **Items per
Column Block** only work in continuous mode. Source:
[Lesson 6: Creating a crosstab report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735526201239-lesson-6-creating-a-crosstab-report.md).

**Page header on every page when you wanted it once.** There is no property for
"first page only". The documented method is a formula on the page header's
**Invisible** property: `pagenumber; pagenumber != 1`. Source:
[How to set a page header only for the first page of the page report](../docs/unversioned/faqs/360049996494-how-to-set-a-page-header-only-for-the-first-page-of-the-page.md).

**Page breaks by record count.** Page reports decide records per page dynamically
from page size and content. To force a count you write a global integer, initialise
it in the report header, increment it in the detail section, and drive the detail
section's **On New Page** property from a formula such as
`if (remainder(num,10)==0 && num!=0) return true else return false`. Source:
[How to control the page break by the number of records](../docs/unversioned/faqs/360050604573-how-to-control-the-page-break-by-the-number-of-records.md).

**Field name labels do not appear.** Several tutorial lessons depend on the
"Insert field name label with field" option in the Options dialog box being
enabled. With it off, Designer adds the field but no caption, and your table
header comes out empty. Source:
[Lesson 6: Creating a crosstab report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735526201239-lesson-6-creating-a-crosstab-report.md).

**Crosstab column and row header labels are blank by default.** The wizard's Label
text box starts empty, so nothing is shown unless you type one or tick **Auto Map
Field Name**. Source:
[Inserting crosstabs in a report](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735527515799-inserting-crosstabs-in-a-report.md).

**Crosstab field background colour does not take.** After setting Color in the
wizard you must also set the field's **Background** property to Transparent in the
Report Inspector. Same source.

## Fonts and PDF

**Fonts truncate when the report moves to another platform.** A report designed in
Designer can render wrong on a Server on a different OS, because platforms use
different font systems and the JDK maps the fonts differently. The fix is the True
Type Font system: design with TTF and publish the fonts alongside the reports. For
PDF specifically, non-Acrobat-internal fonts get remapped, so embed the TTF in the
PDF result. Sources:
[Font face display issues in PDF export](../docs/unversioned/faqs/360047981574-font-face-display-issues-in-pdf-export.md)
and
[Applying True Type fonts in reports](../docs/logi-report-v17-v19/designing-your-reports-logi-report-designer-v19/5735534328983-applying-true-type-fonts-in-reports.md).

**PDF drilldown silently produces nothing.** It needs a page report on query
resources, grouped banded objects, and summaries on the groups, and it fails if
any of those summaries are hidden or suppressed. Source:
[Exporting reports to PDF](../docs/logi-report-v17-v19/delivering-your-reports-logi-report-designer-v19/5735531895447-exporting-reports-to-pdf.md).

**Run Linked Report on a large export.** It generates every linked report too, and
the documentation names it as a performance problem when the linked reports carry a
lot of data. Leave it cleared unless you need it. Same source.

**Compress Image plus image-generated charts kills transparency.** Selecting both
**Compress Image** and **Generate charts and barcodes using images** means the
transparency property of charts, barcodes, web controls, and UDOs stops working.
Same source.

## Export performance

**Excel export runs out of memory.** Page reports created before v17 GA default to
generating all pages at once, which on a large report can push Server into
OutOfMemory. The fix is per report: Report Inspector > Page Panel > **Excel Export
Page Setting**, set **Height Auto Fit** and **Width Auto Fit** to false. From v17
GA the page-by-page setting is on by default. Source:
[Troubleshooting Excel export performance](../docs/unversioned/best-practices/360049940474-troubleshooting-excel-export-performance.md).

**High precision is the default for PDF, RTF, Excel, Fax, and PostScript.** Better
layout, slower export. If the demo is about speed rather than fidelity, drop those
to Low in **File > Options > Export to > Layout Precision**, and remember custom
precision only applies to page report tabs whose **Precision Sensitive** property
is true. Source:
[Exporting reports](../docs/logi-report-v17-v19/delivering-your-reports-logi-report-designer-v19/5735544904599-exporting-reports.md).

**Exporting after an edit without refreshing.** If you modify a report after
opening it, export from view mode after selecting **Refresh Data**, otherwise the
engine has not refetched. Same source.

## Runtime performance

The consolidated list is
[Making high-efficiency reports](../docs/logi-report-v17-v19/designing-your-reports-logi-report-designer-v19/5735547328663-making-high-efficiency-reports.md).
The ones that matter most in a demo:

- Suppress unused banded panels (**Suppress** = true).
- Set DBField and record-level formula **Precision** no larger than needed.
- A chart that runs slowly and shows many duplicate categories should be rebuilt on
  summaries, not detail records. Source:
  [How data is represented in a chart](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735511926551-how-data-is-represented-in-a-chart.md).
- **Result Buffer Size** defaults to 4 pages held in memory; raise it if you have
  the RAM.
- **setFetchSize** in `JdbcDriversConfig.properties` under
  `<designer_install_root>\bin` limits rows per read and is the documented defence
  against Java heap exhaustion on large queries.
- **Push Down Group Query** moves group-level summary computation to the database.
- Pushing down on-screen filters is new in v19 and is counterproductive on small
  reports, because of the extra database round trips. Source:
  [Filtering reports](../docs/logi-report-v17-v19/designing-your-reports-logi-report-designer-v19/5735534181911-filtering-reports.md).

## Parameters

**Select N driven by a parameter with no positive default throws at runtime.** An
Integer parameter used for Top N or Bottom N needs at least one default value
greater than zero. Source:
[Grouping data in tables](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/5735527697943-grouping-data-in-tables.md).

**You cannot group on every SQL type.** `SQL_BINARY`, `SQL_BLOB`, `SQL_CLOB`,
`SQL_LONGVARCHAR`, `SQL_LONGVARBINARY`, `SQL_VARBINARY`, and `SQL_OTHER` are out.
Same source.

**Grouping by intervals is page-report-and-query only.** The Special Function
column does not exist for business-view data. Same source.

## Server and environment

**Report session expires early on Chrome.** Servers older than 15.6 Update 1 on
Chrome 71 and above hit this, because Chrome enforces strict MIME type and the
`.jz` extension used by some built-in JavaScript files is not configured. Fix by
adding `.jz` to `content-type.properties` on a standalone server, or to the
`excludedFiles` parameter in `web.xml` in an embedded environment. Source:
[Unexpected report session expiration](../docs/unversioned/faqs/360045464914-unexpected-report-session-expiration.md).

**Server cannot find a jar file.** Documented separately:
[Logi Report Server unable to find jar file](../docs/unversioned/faqs/360051648593-logi-report-server-unable-to-find-jar-file.md).

**Load JavaFormula error.**
[How to fix the load JavaFormula error](../docs/unversioned/faqs/360048411274-how-to-fix-the-load-javaformula-error.md).

**Publishing.** A report must go up with its catalog the first time. After that you
can publish report updates alone only while the catalog stays published and
unchanged. Source:
[Lesson 2: Publishing resources](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511100055-lesson-2-publishing-resources.md).

**Scheduled publish path to disk.** Under **Publish to Server Resource Tree** the
path must start with `/`, which writes into `<install_root>\jreports`. A full path
such as `C:\temp\file.pdf` writes outside the resource tree. Source:
[Lesson 4: Scheduling reports](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511111191-lesson-4-scheduling-reports.md).

**Schedule priority is ignored by default.** The Priority field only takes effect
if `server.properties` sets `queue.policy` to something other than 0, and it is
visible to administrators only. Source:
[Scheduling to run a report](../docs/logi-report-v17-v19/running-and-scheduling-reports-logi-report-server-v19/5741463322647-scheduling-to-run-a-report.md).

**To Disk is unavailable to organisation users** under multitenancy. Same source.

## Team working

**Merging catalogs.** Use **Save To** in Designer, and make sure the original and
target catalog files have exactly the same name; catalog names are not stored in
reports, so renaming before a merge breaks nothing. Agree a naming convention for
queries, formulas, summaries, and parameters up front, because duplicate names
across the two catalogs force a rename during the merge. Sources:
[General guidelines for multiple report developer environment](../docs/unversioned/best-practices/360049508214-general-guidelines-for-multiple-report-developer-environment.md)
and
[Merging catalogs](../docs/logi-report-v17-v19/creating-and-managing-catalogs-logi-report-designer-v19/5735498385175-merging-catalogs.md).

**Catalog Doctor** is the documented repair tool for a catalog that has drifted:
[Maintaining catalogs with the Catalog Doctor](../docs/logi-report-v17-v19/creating-and-managing-catalogs-logi-report-designer-v19/5735498397591-maintaining-catalogs-with-the-catalog-doctor.md).

## Licence gates

Two features the tutorial explicitly gates behind a Live licence: building a
business view in Designer
([Track 2: Creating business views](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735519563927-track-2-creating-business-views.md)),
and business view filters in Page Report Studio
([Applying filters](../docs/unversioned/editing-page-reports-in-page-report-studio/1500009691602-applying-filters.md)).
Check both before committing to a proof of concept. Licence overview:
[Logi Report licenses](../docs/unversioned/logi-report-get-started-guide/1500009769781-logi-report-licenses.md).

## Naming

Do not describe a Logi Report build as a Logi Composer build. They are distinct
products with distinct documentation, and this corpus covers only Logi Report:
Designer, Server, Page Report Studio, Web Report Studio, JDashboard, and Visual
Analysis. Logi Report produces pixel-perfect paginated output; that is not what
Composer's scheduled dashboard snapshots do. Conflating them has already caused a
real mislabelling in a live deal.

The older material calls the product Logi JReport (v15 to v16). Read
`docs/jreport-v15-v16/` as the older product name for the same product line, and
`docs/unversioned/` as undated text that uses both namings.
