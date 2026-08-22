---
title: "Add Tables/Views/Queries Dialog"
id: 1500009585621
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585621-Add-Tables-Views-Queries-Dialog
updated_at: 2021-07-24T05:55:39Z
---

# Add Tables/Views/Queries Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564482-Add-Tables-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585641-Add-Tables-Views-Synonyms-Dialog)

# Add Tables/Views/Queries Dialog

The Add Tables/Views/Queries dialog appears when you do one of the following:

* In the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009567142-Query-Editor-Dialog), select Add Tables on the toolbar or select Menu > Query > Add Tables/Views/Queries.
* In the Catalog Manager, right-click the Business Views node and select New Business View from the shortcut menu. Then provide a name in the displayed dialog and select OK.

It helps you to [add resources to use](https://devnet.logianalytics.com/hc/en-us/articles/1500009570762-Adding-and-Deleting-Tables-in-a-Query) in a query or a business view. [See the dialog](javascript:%20void(null)).

![Add Tables/Views/Queries dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893821975/addtbvwqy.gif)

**All Tables/Views/Queries**

List all the tables, views, synonyms, queries, imported SQLs, stored procedures, and user defined data sources in the current catalog data source that can be added to the query or business view.

When two resources (for example, a table and a view) use the same name, they cannot be added at the same time, and when a table is already contained in a query, you cannot add the table and the query at the same time.

**Selected Tables/Views/Queries**

Lists all the added tables, views, synonyms, queries, imported SQLs, stored procedures, and user defined data sources.

**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)**

Adds the selected resources from the left box to the right box. If the selected resources contain a table, view or synonym that is already added, the Input Table Name dialog is displayed for you to specify another name for the resource.

**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**

Removes the selected resources from the right box.

**Show Tables/Views Already Added**

Specifies whether to show the tables, views and synonyms in JDBC connections in the All Tables/Views/Queries box, which have already been added to the right box. This option is available only when there is at least a JDBC connection in the current catalog data source.

**OK**

Adds the selected resources to the current query or business view. When a query, imported SQL, stored procedure or user defined data source is added, it will be added as a single table with all of its columns.

If the query or business view does not contain only tables/views from one JDBC connection, the computed column, customized SQL, and preview features cannot work anymore.

**Cancel**

Exits the dialog and discards the setting.

**Help**

Displays the help document of this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564482-Add-Tables-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585641-Add-Tables-Views-Synonyms-Dialog)
