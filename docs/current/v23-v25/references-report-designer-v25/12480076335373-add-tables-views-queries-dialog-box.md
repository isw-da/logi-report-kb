---
title: "Add Tables/Views/Queries Dialog Box"
id: 12480076335373
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480076335373-Add-Tables-Views-Queries-Dialog-Box
updated_at: 2026-02-25T23:50:06Z
source_host: docs-report.zendesk.com
---
# 
Add Tables/Views/Queries Dialog Box

You can use the Add Tables/Views/Queries dialog box to add resources to use in a query or a business view. This topic describes the options in the dialog box.
    

Designer displays the Add Tables/Views/Queries dialog box when you do one of the following:

- In the Query Editor dialog box, select Add Tables on the toolbar or navigate to Menu > Query > Add Tables/Views/Queries.

- In the Catalog Manager, right-click the Business Views node and select New Business View from the shortcut menu. Then provide a name in the displayed dialog box and select OK.

Designer displays these options:

All Tables/Views/Queries

This box list all the tables, views, synonyms, queries, imported SQLs, stored procedures, and user-defined data sources in the current catalog data source, which you can select to add to the query or business view.

When two resources (for example, a table and a view) use the same name, you cannot add them at the same time, and when a table is already contained in a query, you cannot add the table and the query at the same time.

Selected Tables/Views/Queries

This box lists all the tables, views, synonyms, queries, imported SQLs, stored procedures, and user-defined data sources that you select to add to the query or business view.

Add button

Select to add the specified resources from the left box to the right box. If the selected resources contain a table, view, or synonym that is already added, Designer displays the Input Table Name dialog box for you to specify another name for the resource.

Remove button

Select to remove the specified resources from the right box.

Show Tables/Views Already Added

Designer displays this option only when there is at least a JDBC connection in the current catalog data source. Select it if you want the tables/views/synonyms  in the JDBC connections that you have added to the catalog still available in the All Tables/Views/Queries box, so that you can add them to the Selected Tables/Views/Queries box as many times as you want by providing different names each time you add them.

OK

Select to add the specified resources to the current query or business view. When you add a query, imported SQL, stored procedure, or user-defined data source, Designer adds it as a single table with all of its columns.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.
