# Concepts: how a Logi Report build nests

Nothing in Logi Report exists on its own. A report is always inside a catalog,
always bound to a dataset, and that dataset always comes from either a query or
a business view. Get this chain wrong and every later step fails, so read this
before touching a wizard.

```
connection  ->  tables / views / stored procedures / imported SQL
                    |
                    +-> query        -> page report (query-based)
                    |
                    +-> business view -> web report, ad hoc, visual analysis,
                                          business-view-based page report
all of the above live inside:  catalog file (.cat) + catalog folder
```

## Catalog

A catalog is the report and metadata repository. Every report must sit in a
catalog folder and be tied to a catalog file, a physical `.cat` file holding data
objects and their definitions. One catalog file can serve one report or many
reports in the same folder, and other resources such as images live in the same
folder. Source: [Catalogs](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511440151-catalogs.md).

A catalog file stores database connections, tables and views, stored procedures,
imported queries, user data sources, queries, business views, parameters,
formulas, summaries, and customised classes. Because the database architecture is
stored in the catalog, you can keep developing reports while offline from the
database. See also
[Knowing about catalogs](../docs/logi-report-v17-v19/creating-and-managing-catalogs-logi-report-designer-v19/5735520312215-knowing-about-catalogs.md)
and
[Creating, opening and saving catalogs](../docs/logi-report-v17-v19/creating-and-managing-catalogs-logi-report-designer-v19/5735563628951-creating-opening-and-saving-catalogs.md).

The Catalog Manager is the interface for the resources in a catalog: a toolbar, a
left data resource tree, and a right properties sheet. Detail in
[Managing the data resources in a catalog](../docs/logi-report-v17-v19/creating-and-managing-catalogs-logi-report-designer-v19/5735526919831-managing-the-data-resources-in-a-catalog.md).

## Connection

A connection is the gateway to raw data: driver, data source name, connection
URL, user ID, password. Designer supports JDBC, JSON, XML, SOAP web service,
MongoDB, Hive, Elasticsearch, user defined, and hierarchical connections, and
ships connection plug-ins for Oracle, MySQL, SQL Server, InterSystems IRIS, and
PostgreSQL. For anything else you install the JDBC driver and append its class
path to Designer's environment configuration file first. Source:
[Connections](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735506277911-connections.md),
with the supported database list in
[Supported report databases](../docs/unversioned/logi-report-get-started-guide/1500009742062-supported-report-databases.md).

Adding a connection does not add data. You then add tables, views, or synonyms
into the catalog from that connection, and those become available to queries and
business views.

## Query

A query is a catalog-level object, similar in concept to a database view but
stored in the catalog file rather than the database. Logi Report addresses it by
a unique mapping name instead of SQL's `table.column`. You build one in the Query
Editor by adding tables, selecting columns, and joining them; auto join is on by
default and Designer generates the SELECT statement, which you can inspect with
the SQL button. Source:
[Queries](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735519903895-queries.md)
and the worked example in
[Lesson 1: Creating a standard banded report](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735563121559-lesson-1-creating-a-standard-banded-report.md).

Queries are the data source for query-based page reports.

## Business view

A business view is a business-oriented, flat presentation of data. It hides
connections and joins from the end user while carrying the interactivity that
makes a report feel live: drill down and drill up, switching groups, exchanging
crosstab rows and columns, converting a chart to a crosstab and back. Source:
[Business views](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735526420375-business-views.md).

A business view is built from four element types:

- Group objects, typically fields and formulas you want to group by. They answer
  who, when, what, where, which.
- Aggregation objects, typically numeric fields using functions such as Sum.
- Detail objects, any field or formula you want to show in a detail row.
- Categories, folders that organise the other three.

It can also carry hierarchies, an ordered set of group objects such as
Year > Month > Day, which is what makes go up and go down work at runtime. The
step-by-step build is
[Track 2: Creating business views](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735519563927-track-2-creating-business-views.md).

Business views are the data source for web reports, ad hoc reports, visual
analysis, and business-view-based page reports.

Note the licence gate: the tutorial states that building a business view requires
a Live licence for Designer, and Page Report Studio's business view filters need
a Live licence for Server. See the same track and
[Applying filters](../docs/unversioned/editing-page-reports-in-page-report-studio/1500009691602-applying-filters.md).

## Dataset

A dataset is the report-level binding to a query or business view. It is where
you apply a dataset filter, which passes down to the database and affects only
the components in this report that use that dataset, unlike a query filter which
changes the catalog and therefore every report built on that query. Sources:
[Applying datasets in a report](../docs/logi-report-v17-v19/manipulating-report-datasets-logi-report-designer-v19/5735586128791-applying-datasets-in-a-report.md)
and
[Filtering datasets in a report](../docs/logi-report-v17-v19/manipulating-report-datasets-logi-report-designer-v19/5735555312279-filtering-datasets-in-a-report.md).

## Report

Three report types, covered properly in
[page-vs-web-reports.md](page-vs-web-reports.md): page report, web report, and
library component (widgets for JDashboard). Source:
[Report types](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511454487-report-types.md).
The file extensions `.cls` for a page report and `.wls` for a web report come from
[Lesson 3: Running reports](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735497665815-lesson-3-running-reports.md).
Which data source each type can use is set out in
[Creating reports](../docs/logi-report-v17-v19/designing-your-reports-logi-report-designer-v19/5735569787671-creating-reports.md):
web reports and library components on business views only, page reports on either.

## Designer and Server

Designer is a Swing IDE for building reports. Server is the Java runtime that
runs, schedules, secures, and delivers them, and hosts Page Report Studio, Web
Report Studio, JDashboard, and Visual Analysis. You publish from Designer to
Server; Server can only run what has been published to it. Sources:
[Logi Report product overview](../docs/unversioned/logi-report-get-started-guide/1500009742162-logi-report-product-overview.md)
and
[Lesson 2: Publishing resources](../docs/logi-report-v17-v19/logi-report-tutorial-v19/5735511100055-lesson-2-publishing-resources.md).

## Era note

The corpus spans two product names. `docs/jreport-v15-v16/` is Logi JReport
(Designer, Server, Studios all carry the JReport name). `docs/logi-report-v17-v19/`
is Logi Report. `docs/unversioned/` states no version and mixes both namings in
its prose. The concept chain above is identical across both eras: the v16
equivalents are
[Catalogs](../docs/jreport-v15-v16/logi-jreport-tutorial-v16/1500011463381-catalogs.md),
[Queries](../docs/jreport-v15-v16/logi-jreport-tutorial-v16/1500011463361-queries.md),
and
[Business views](../docs/jreport-v15-v16/logi-jreport-tutorial-v16/1500011431322-business-views.md).

Logi Report and Logi Composer are separate products with separate documentation.
Nothing in this corpus describes Logi Composer. Logi Report does pixel-perfect
paginated reporting through Designer and Server; do not transfer any procedure
here to a Composer engagement.
