---
title: "Add Tables/Views/Queries Dialog Box"
id: 1500010058002
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010058002-Add-Tables-Views-Queries-Dialog-Box
updated_at: 2021-11-10T06:56:56Z
---

# Add Tables/Views/Queries Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095521-Add-Tables-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095541-Add-Tables-Views-Synonyms-Dialog-Box)

# Add Tables/Views/Queries Dialog Box

You can use the Add Tables/Views/Queries dialog box to [add resources to use](https://devnet.logianalytics.com/hc/en-us/articles/1500010062582-Creating-Queries-in-a-Catalog#AddTable) in a query or a business view. This topic describes the options in the dialog box.

Designer displays the Add Tables/Views/Queries dialog box when you do one of the following:

* In the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098321-Query-Editor-Dialog-Box), select Add Tables on the toolbar or select Menu > Query > Add Tables/Views/Queries.
* In the Catalog Manager, right-click the Business Views node and select New Business View from the shortcut menu. Then provide a name in the displayed dialog box and select OK.

![Add Tables/Views/Queries dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848429975/addtbvwqy.gif)

You see the following options in the dialog box:

**All Tables/Views/Queries**

The box list all the tables, views, synonyms, queries, imported SQLs, stored procedures, and user-defined data sources in the current catalog data source that you can select to add to the query or business view.

When two resources (for example, a table and a view) use the same name, you cannot add them at the same time, and when a table is already contained in a query, you cannot add the table and the query at the same time.

**Selected Tables/Views/Queries**

The box lists all the tables, views, synonyms, queries, imported SQLs, stored procedures, and user-defined data sources that you select to add to the query or business view.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified resources from the left box to the right box. If the selected resources contain a table, view, or synonym that is already added, Designer displays the Input Table Name dialog box for you to specify another name for the resource.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified resources from the right box.

**Show Tables/Views Already Added**

Designer displays the option only when there is at least a JDBC connection in the current catalog data source. Select it if you want the tables/views/synonyms in the JDBC connections that you have added to the catalog still available in the All Tables/Views/Queries box, so that you can add them to the Selected Tables/Views/Queries box as many times as you want by providing different names each time you add them.

**OK**

Select to add the specified resources to the current query or business view. When you add a query, imported SQL, stored procedure, or user-defined data source, Designer adds it as a single table with all of its columns.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095521-Add-Tables-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095541-Add-Tables-Views-Synonyms-Dialog-Box)
