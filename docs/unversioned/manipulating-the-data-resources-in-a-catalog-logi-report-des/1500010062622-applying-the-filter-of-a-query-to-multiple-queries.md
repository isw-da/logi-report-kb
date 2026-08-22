---
title: "Applying the Filter of a Query to Multiple Queries"
id: 1500010062622
section: "Manipulating the Data Resources in a Catalog - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010062622-Applying-the-Filter-of-a-Query-to-Multiple-Queries
updated_at: 2021-07-23T19:16:46Z
---

# Applying the Filter of a Query to Multiple Queries

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062642-Locking-Queries)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062602-Managing-the-Data-Retrieval-of-Queries)

# Applying the Filter of a Query to Multiple Queries

After you have added filter conditions to a query, you can set its Data Source Filter property to specify whether or not you want the filter of the query to work as a data source filter, so that you can apply the filter to other queries directly without having to define the filter conditions repeatedly in each of the queries. This topic describes how you can make use of the filter in a query as a data source filter to filter multiple queries.

This topic contains the following sections:

* [Using the Filter of a Query as a Data Source Filter](#Use)
* [Example of Applying a Data Source Filter](#Example)

## Using the Filter of a Query as a Data Source Filter

1. [Create the query](https://devnet.logianalytics.com/hc/en-us/articles/1500010062582-Creating-Queries-in-a-Catalog) with the required data resources.
2. [Create filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010062582-Creating-Queries-in-a-Catalog#FilterQuery) for the query and save the query.
3. In the Catalog Manager, select **Pre-join**.
4. In the Select Data Source dialog box, select the catalog data source in which the query is and select **OK**.
5. In the Pre-join Editor dialog box, select **Add Tables**.
6. In the Add Tables/Views/Queries dialog box, select the query you just created and the data resources which you want to join with the query, then select **OK**.
7. Define the joins between the query with the other data resources and save them. For more information, see
   [Editing Pre-joins in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010094041-Editing-Pre-joins-in-a-Catalog).
8. Set the [Data Source Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010100061-Query-Properties#Filter) property of the query to **true**.

You can now apply the filter defined in the query (the data source filter query) to all the other queries in the same catalog data source if the other queries can satisfy the following conditions:

* The queries contain the data resources with which the data source filter query is joined.
* The queries do not contain any of the data resources that are included in the data source filter query.

## Example of Applying a Data Source Filter

The following example shows the usage of data source filter in detail. In this example, we add a filter "Order ID > 3400" on a query and make it work as a data source filter.

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, right-click the **Queries** node in Data Source 1 and select **New Query** from the shortcut menu.
3. In the Enter Query Name dialog box, type **DSFQuery** and select **OK**.
4. In the Add Tables/Views/Queries dialog box, expand the JDBC connection > **Tables** node, select **Orders**, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) to add it to the right box, then select **OK**.

   ![Add Table for the Query](https://devnet.logianalytics.com/hc/article_attachments/4404848427031/qury_fltr_addtbl.gif)
5. In the Query Editor dialog box, select all the columns in the Orders table by selecting the top checkbox.
6. Select **Menu** > **Query** >  **Filter**.
7. In the Search Condition dialog box, select **Add Condition** and define the filter condition as follows. Select **OK** to accept the condition.

   ![Add Filter Condition for the Query](https://devnet.logianalytics.com/hc/article_attachments/4404848427671/qury_fltr_qryedtr.gif)
8. Select **OK** in the Query Editor dialog box and then close the prompted dialog box. Designer adds the query DSFQuery under the Queries node in the Catalog Manager and selects it by default.
9. Select **Show Properties** on the Catalog Manager toolbar, then set the query's **Data Source Filter** property to **true**.

   ![Set the Data Source Filter Property](https://devnet.logianalytics.com/hc/article_attachments/4404856843671/qury_fltr_setprpty.gif)

Next, we create a pre-join to join DSFQuery with the table Orders Detail.

1. Select **Pre-join** on the Catalog Manager toolbar.
2. In the Select Data Source dialog box, select **Data Source 1** and select **OK**.
3. In the Pre-join Editor dialog box, select **Add Tables**.
4. In the Add Tables/Views/Queries dialog box, add the table **Orders Detail** and the query **DSFQuery**, then select **OK**.

   ![Add Tables to Join](https://devnet.logianalytics.com/hc/article_attachments/4404856843927/qury_fltr_addtbls.gif)
5. Join DSFQuery and Orders Detail by connecting their **Order ID** columns.

   ![Joining Tables](https://devnet.logianalytics.com/hc/article_attachments/4404856844183/qury_fltr_cnct.gif)
6. Select **Save** to save the pre-join. Select **Yes** in the message dialog box to accept the default path.

Next, we create another query that contains the table joined with DSFQuery and use the query to create a report to test the data source filter.

1. [Repeat steps 2 to 5](#Step1) to create another query **OrdersDetail** which contains the **Orders Detail** table with all of its columns.
2. [Create a page report with a standard banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#Page) based on the OrdersDetail query, which displays the fields Order ID\_FK1, Quantity, and Unit Price.
3. Select the **View** tab to preview the report. The report displays only the records the order IDs of which are higher than 3400.

   ![Page report with a standard banded object](https://devnet.logianalytics.com/hc/article_attachments/4404848428055/qury_fltr_rst.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062642-Locking-Queries)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062602-Managing-the-Data-Retrieval-of-Queries)
