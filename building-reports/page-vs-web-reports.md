# Page reports, web reports, and the studios that edit them

The first decision in any Logi Report build. Choose wrong and you spend the demo
apologising for the tool. The comparison below comes from
[Choosing the report type](../docs/logi-report-v17-v19/designing-your-reports-logi-report-designer-v19/5735534332951-choosing-the-report-type.md)
and
[Report types](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511454487-report-types.md);
the data source rule from
[Creating reports](../docs/logi-report-v17-v19/designing-your-reports-logi-report-designer-v19/5735569787671-creating-reports.md);
the `.cls` and `.wls` file extensions from
[Lesson 3: Running reports](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735497665815-lesson-3-running-reports.md).

## The three types

| | Page report | Web report | Library component |
| --- | --- | --- | --- |
| File extension | `.cls` | `.wls` | saved to the component library |
| Aimed at | paginated result sets, pixel-perfect output | web viewing, interactive analysis | widgets for JDashboard |
| Data source | query, or business view | business view | business view |
| Runtime studio | Page Report Studio | Web Report Studio | JDashboard |
| Editable in | Designer and Page Report Studio | Designer and Web Report Studio | Designer |

Stated plainly in
[Creating reports](../docs/logi-report-v17-v19/designing-your-reports-logi-report-designer-v19/5735569787671-creating-reports.md):
web reports and library components can only be based on business views; a page
report can apply either business views or queries, including stored procedures,
imported SQLs, imported APEs, user-defined data sources, and hierarchical data
sources. That choice is made once, when the page report is created, by the
**Create Using Business View** option, and every data component in the report must
then use the chosen type. Three starting components are unavailable in a
business-view-based page report: Horizontal Banded, Mailing Label, and Tabular.

## Page report

A page report holds one or more report tabs of the same or related purpose. You
design, maintain, run, and schedule the tabs together or separately, sharing data
sources across the tabs. Page reports are the only type that supports subreports,
bursting reports, and calculations that use global-variable formulas. They are
where pixel-perfect belongs.

Choose a page report when the demo is about a document: an invoice, a statement,
a regulatory return, a mailing label run, anything that will be printed or sent
as PDF with exact placement.

## Web report

Web reports create and run faster, and take a tabular layout for well-aligned
multi-component design aimed at web viewing. Most user actions happen in the
browser rather than a round trip to Server, so the same hardware serves many more
concurrent users. Each component gets its own local page navigation and scroll
bars, which a page report does not have, and exporting to PDF or printing still
produces page numbers and page breaks.

Choose a web report when the demo is about interaction: converting a table to a
crosstab to a chart in front of the audience, drilling, filtering, swapping
groups. That is the story
[Lesson 1: Creating a web report using the quick start method](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735519967383-lesson-1-creating-a-web-report-using-the-quick-start-method.md)
tells in about five minutes.

## Library component

Charts, tables, crosstabs, control components, and others, created and edited in
Designer for use in dashboards in JDashboard at runtime. They communicate with
each other by a messaging mechanism, which is what makes runtime data
synchronisation across a dashboard possible. The documented route to a good
library component is to build the data component inside a web report, test it,
then save it as a library component.

## What you can place where

Available components differ by report type, and the corpus gives a full matrix of
which component types are legal in which report areas:
[Component placement in different report type](../docs/logi-report-v17-v19/working-with-components-in-reports-logi-report-designer-v19/9898540172311-component-placement-in-different-report-type.md).
Two traps worth carrying into a demo:

- Query-based page reports can use every component except KPI. KPI is a web
  report and library component thing.
- Business-view-based page reports and web reports are restricted to 2-D charts.
  A 3-D chart needs a query-based page report.

## The two studios

Page Report Studio edits page reports at runtime. Its surface includes adding
report objects, filters, conditional formats, sorting, dynamic resources, web
controls, and export or print. Entry point:
[Editing page reports in Page Report Studio](../docs/unversioned/editing-page-reports-in-page-report-studio/1500009691502-editing-page-reports-in-page-report-studio.md).

Web Report Studio edits web reports at runtime, with a vertical visualisation
toolbar that converts a data component between table, crosstab, and chart in one
click, plus inserting components, applying parameters and filters, links,
conditional formats, and export or print. Entry point:
[Editing web reports in Web Report Studio](../docs/unversioned/editing-web-reports-in-web-report-studio/1500009719081-editing-web-reports-in-web-report-studio.md).

Server decides which studio opens: page reports run in Page Report Studio and web
reports in Web Report Studio by default. Run opens view mode, Edit opens edit
mode (Interactive View for a page report). Source:
[Lesson 1: Starting Server](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735563057559-lesson-1-starting-server.md).

## Which to pick for a demo

- Showing interactivity, conversion, drill, self-service: web report.
- Showing pixel-perfect output, bursting, subreports, print or PDF fidelity: page
  report.
- Showing a dashboard: build the pieces as a web report first, then save them as
  library components and assemble in JDashboard.

## Era note

The same three types exist in the Logi JReport era (v15 to v16). The v16
comparison is
[Page reports vs. web reports vs. library components](../docs/jreport-v15-v16/logi-jreport-tutorial-v16/1500011463341-page-reports-vs-web-reports-vs-library-components.md).
The substantive difference in the v17 to v19 text is the added emphasis that web
reports take a tabular layout and that page report templates are editable in both
Designer and Page Report Studio. Product names differ: Logi JReport Designer and
Logi JReport Server in the older set.

Logi Composer is a different product and none of the above applies to it.
