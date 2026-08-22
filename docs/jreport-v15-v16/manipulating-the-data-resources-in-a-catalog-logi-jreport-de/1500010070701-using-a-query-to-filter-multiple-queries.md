---
title: "Using a Query to Filter Multiple Queries"
id: 1500010070701
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010070701-Using-a-Query-to-Filter-Multiple-Queries
updated_at: 2021-07-24T10:37:47Z
---

# Using a Query to Filter Multiple Queries

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010034762-Creating-Union-Queries) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010070721-Locking-Queries)

# Using a Query to Filter Multiple Queries

The [Data Source Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010069341-Query-Properties#Filter) property is added to queries for specifying whether or not a query works as a data source filter. By setting a query's Data Source Filter property to true and joining the query with other data resources, the filters defined in the query will be applied to all the other queries in the same catalog data source when the following conditions are satisfied:

* The queries contain the data resources with which the data source filter query is joined.
* The queries do not contain any of the data resources that are included in the data source filter query.

**To create a query and use it as a data source filter:**

1. [Create the query](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog) with the required data resources.
2. [Create filters](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog#FilterQuery) on the query, then save the query.
3. In the Catalog Manager, select **Pre-join**.
4. In the Select Data Source dialog, select the catalog data source in which the query is created and select **OK**.
5. In the Pre-join Editor, select **Add Tables**.
6. In the Add Tables/Views/Queries dialog, select the query you just created and the data resources which you want to join with the query, then select **OK**.
7. Define the joins between the query with the other data resources and save them. For more information, see
   [Editing Pre-joins in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010028522-Editing-Pre-joins-in-a-Catalog).
8. Set the Data Source Filter property of the query to **true**.

The following example shows the usage of data source filter in detail. In this example, we add a filter Order ID > 3400 on a query and make it work as a data source filter. The example is based on the SampleReports catalog in `<install_root>\Demo\Reports\SampleReports`.

1. In the Catalog Manager, right-click the **Queries** node in Data Source 1 and select **New Query** from the shortcut menu.
2. In the Enter Query Name dialog, input **DSFQuery** and select **OK**.
3. In the Add Tables/Views/Queries dialog, expand the **JDBC connection** > **Tables** node, select **Orders**, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif) to add it to the right box, then select **OK**.

   ![Add Tables/Views/Queries dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901141911/qury_fltr_addtbl.gif)
4. In the Query Editor, select all the columns in the Orders table by selecting the top checkbox.
5. Select **Menu** > **Query** > **Filter**.
6. In the Search Condition dialog, select **Add Condition** to add a line, define the filter as @"Order ID" > 3400, and then select **OK**.

   ![Search Condition dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909130391/qury_fltr_qryedtr.gif)
7. Select **OK** in the Query Editor and then close the prompted dialog. The query DSFQuery is now added under the Queries node in the Catalog Manager and selected by default.
8. In the Catalog Manager, select **Show Properties,** then set the query's Data Source Filter property to **true**.

Next, we will create a pre-join to join DSFQuery with the table Orders Detail.

1. Select **Pre-join** on the Catalog Manager toolbar.
2. In the Select Data Source dialog, select **Data Source 1** and select **OK**.
3. In the Pre-join Editor, select **Add Tables**.
4. In the Add Tables/Views/Queries dialog, add the table **Orders Detail** and the query **DSFQuery**, then select **OK**.

   ![Add Tables/Views/Queries dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909130647/qury_fltr_addtbls.gif)
5. Join DSFQuery and Orders Detail by connecting the Order ID columns.

   ![Pre-join Editor](https://devnet.logianalytics.com/hc/article_attachments/4404901142167/qury_fltr_cnct.gif)
6. Select **Save** to save the pre-join. Select **Yes** in the message dialog to accept the default path.

Next, we will create another query that contains the table joined with DSFQuery and use the query to create a report to test the data source filter.

1. [Repeat steps 1 to 4](#Step1) to create another query named  **OrdersDetail** which contains the **Orders Detail** table with all of its columns.
2. [Create a page report with a standard banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010034782-Creating-Reports#Page) based on the OrdersDetail query, which displays the fields Order\_ID\_FK1, Quantity and Unit Price.
3. Preview the report. We can see that only the records the order IDs of which are higher than 3400 are shown.

   ![Page report with a standard banded object](https://devnet.logianalytics.com/hc/article_attachments/4404901142423/qury_fltr_rst.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010034762-Creating-Union-Queries) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010070721-Locking-Queries)
