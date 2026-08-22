---
title: "Adding and Deleting Tables in a Query"
id: 1500009570762
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009570762-Adding-and-Deleting-Tables-in-a-Query
updated_at: 2021-07-24T05:53:52Z
---

# Adding and Deleting Tables in a Query

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570662-Editing-a-Query)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592501-Joining-Tables-in-a-Query)

# Adding and Deleting Tables in a Query

This topic introduces how to add an delete tables in a query.

* **To add some extra tables to a query:**
  1. In the Query Editor, select **Menu** > **Query** > **Add Tables/Views/Queries**. The [Add Tables/Views/Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009585621-Add-Tables-Views-Queries-Dialog) dialog appears.

     ![Add Tables/Views/Queries dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893821975/addtbvwqy.gif)
  2. In the All Tables/Views/Queries box, all the tables, views, synonyms, queries, imported SQLs, stored procedures and user defined data sources in the current catalog data source in which the query is added are listed. Select the resources you want to use in the query and select **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)** to add them into the Selected Tables/Views/Queries box.
     You can mash up multiple data resources from the same catalog data source in a query if you want. When two resources (for example, a table and a view) use the same name, they cannot be added to the query at the same time, and when a table is already contained in a query, you cannot add the table and the query at the same time.

     To remove unwanted resources from the Selected Tables/Views/Queries box, select them and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)**.
  3. If the current catalog data source contains JDBC connections, the Include Added Tables/Views option is available. Check it if you want to show the tables, views and synonyms in the resource tree in the left box, which have already been added to the right box. You can then add the tables, views and synonyms of the JDBC connections to the query as many times as you want by providing different names for the tables, views and synonyms each time you add them.
  4. Select **OK** to add the selected resources to the current query. When a query, imported SQL, stored procedure or user defined data source is added, it will be added as a single table with all of its columns unselected to be included.
  5. Select **Menu** > **Query** > **Arrange Table/View/Query**  to organize the tables.
  6. Select the required columns in each table. To select all, select **\***. The columns will be displayed in the criteria panel in the lower part of the Query Editor. However for tables in MongoDB connection, you cannot select all columns by selecting **\***. The PrimaryKey and ForeignKey columns in each table cannot be selected to a query.
* **To remove tables from a query:**
  1. In the Query Editor, select the table that you want to delete, then do any of the following:
     + Select **Delete Table** on the toolbar.
     + Select **Menu** > **Query** > **Delete Table/View/Query**.
     + Select the **x** button at the top right corner of the table.
  2. Repeat the above steps to delete other tables. After deleting a table from a query, any [joins](https://devnet.logianalytics.com/hc/en-us/articles/1500009592501-Joining-Tables-in-a-Query) based on the table will be removed.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570662-Editing-a-Query)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592501-Joining-Tables-in-a-Query)
