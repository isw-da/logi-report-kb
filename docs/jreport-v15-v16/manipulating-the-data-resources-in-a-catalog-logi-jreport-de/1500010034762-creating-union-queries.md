---
title: "Creating Union Queries"
id: 1500010034762
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010034762-Creating-Union-Queries
updated_at: 2021-07-24T10:37:45Z
---

# Creating Union Queries

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070741-Using-Pre-joins-in-Queries) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010070701-Using-a-Query-to-Filter-Multiple-Queries)

# Creating Union Queries

This topic introduces how to create union queries and how to manage the created union queries. The Menu > Query > Union option of the Query Editor enables you to combine specified records from more than one query into a result set. Unlike a Join which creates one record with multiple columns from the 2 queries, the Union appends the results of one query to the results of the second query so the number of records is the sum of the two queries. You must match each column of the first query to the second query with the same number of columns, the same SQL types, and the same sequence of columns. The names do not need to match.

A common usage is to build a mashup query that combines a query from one instance of a database to a second instance of the database. For example you want all the records for table Customers from one database appended to all the records from table Customers from a second database. The two Customers tables must match exactly the number of columns, the SQL type and sequence.

**To create a union query:**

1. In the Catalog Manager, right-click a selected query (here we call it primary query) and select **Edit Query** to open the Query Editor.
2. In the Query Editor, select **Menu** > **Query** > **Union** > **New**.
3. In the Enter Query Name dialog, specify a name for the query and select **OK**.
4. A new Query Editor is displayed. [Create the query](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog) as required.

**Notes:**

* When creating a union query, note that the selecting order should refer to the order in the primary query. The SQL type and the number of the selected columns should match those in the primary query. For example, if you select two columns in the primary query, the first one is of Integer type, and the second one is of String type. Then, in the union query, you should also first select an Integer column, and then a String type column.
* A union query cannot support formulas and parameters.

After union queries are created, you can also manage them as follows:

1. In the Catalog Manager, right-click the primary query and select **Edit Query**.
2. In the Query Editor, select **Menu** > **Query** > **Union** > **Select**. The Union dialog appears.

   ![Union dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909129623/qury_union.gif)
3. To add a union to the query, select a union in the Queries box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif). To remove a union from the query, select it in the Union box, and then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif).
4. In the Union box, select the Attribute column to specify the type of the union.
   * ![No Duplicate Records button](https://devnet.logianalytics.com/hc/article_attachments/4404909129879/qury_union1.gif): No duplicate records will be returned.
   * ![All Records button](https://devnet.logianalytics.com/hc/article_attachments/4404901140631/qury_union2.gif): All records will be returned.
5. When done, select **OK** to confirm the changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070741-Using-Pre-joins-in-Queries) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010070701-Using-a-Query-to-Filter-Multiple-Queries)
