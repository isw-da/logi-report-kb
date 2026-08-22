---
title: "Add Tables/Views/Queries Dialog Box"
id: 5735565004567
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735565004567-Add-Tables-Views-Queries-Dialog-Box
updated_at: 2022-11-02T04:14:16Z
---

# Add Tables/Views/Queries Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735521826967-Add-Tables-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735521836951-Add-Tables-Views-Synonyms-Dialog-Box)

# Add Tables/Views/Queries Dialog Box

You can use the Add Tables/Views/Queries dialog box to [add resources to use](https://devnet.logianalytics.com/hc/en-us/articles/5735547138327-Creating-Queries-in-a-Catalog#AddTable) in a query or a business view. This topic describes the options in the dialog box.

Designer displays the Add Tables/Views/Queries dialog box when you do one of the following:

* In the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552449687-Query-Editor-Dialog-Box), select Add Tables on the toolbar or navigate to Menu > Query > Add Tables/Views/Queries.
* In the Catalog Manager, right-click the Business Views node and select New Business View from the shortcut menu. Then provide a name in the displayed dialog box and select OK.

![Add Tables/Views/Queries dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898458199703/addtbvwqy.gif)

Designer displays these options:

**All Tables/Views/Queries**

This box list all the tables, views, synonyms, queries, imported SQLs, stored procedures, and user-defined data sources in the current catalog data source, which you can select to add to the query or business view.

When two resources (for example, a table and a view) use the same name, you cannot add them at the same time, and when a table is already contained in a query, you cannot add the table and the query at the same time.

**Selected Tables/Views/Queries**

This box lists all the tables, views, synonyms, queries, imported SQLs, stored procedures, and user-defined data sources that you select to add to the query or business view.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified resources from the left box to the right box. If the selected resources contain a table, view, or synonym that is already added, Designer displays the Input Table Name dialog box for you to specify another name for the resource.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified resources from the right box.

**Show Tables/Views Already Added**

Designer displays this option only when there is at least a JDBC connection in the current catalog data source. Select it if you want the tables/views/synonyms in the JDBC connections that you have added to the catalog still available in the All Tables/Views/Queries box, so that you can add them to the Selected Tables/Views/Queries box as many times as you want by providing different names each time you add them.

**OK**

Select to add the specified resources to the current query or business view. When you add a query, imported SQL, stored procedure, or user-defined data source, Designer adds it as a single table with all of its columns.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735521826967-Add-Tables-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735521836951-Add-Tables-Views-Synonyms-Dialog-Box)
