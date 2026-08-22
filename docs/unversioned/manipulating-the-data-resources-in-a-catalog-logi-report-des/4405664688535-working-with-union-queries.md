---
title: "Working with Union Queries"
id: 4405664688535
section: "Manipulating the Data Resources in a Catalog - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664688535-Working-with-Union-Queries
updated_at: 2022-12-28T07:37:43Z
---

# Working with Union Queries

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664687383-Using-Pre-joins-in-Queries)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](#Manage)

# Working with Union Queries

You can combine specified records from more than one query into a result set using the Union option included in the Query Editor. Unlike a Join which creates one record with multiple columns from the two queries, the Union appends the results of one query to the results of the second query so the number of records is the sum of the two queries. This topic introduces how you can create and manage union queries.

This topic contains the following sections:

* [Creating Union Queries](#Create)
* [Managing Union Queries](#Manage)

## Creating Union Queries

When creating union queries, you must match each column of the first query to the second query with the same number of columns, the same SQL types, and the same sequence of columns. The names do not need to match. A common usage is to build a mashed-up query that combines a query from one instance of a database to a second instance of the database. For example, you want all the records for table Customers from one database appended to all the records from table Customers from a second database. The two Customers tables must match exactly the number of columns, the SQL type, and sequence.

**To create a union query**

1. In the Catalog Manager, right-click a query (here we call it the primary query) and select **Edit Query**.
2. In the Query Editor dialog box, navigate to **Menu** > **Query** > **Union** > **New**.
3. In the Enter Query Name dialog box, specify a name for the query and select **OK**.
4. Designer displays a new Query Editor dialog box. [Create the query](https://devnet.logianalytics.com/hc/en-us/articles/4405661917975-Creating-Queries-in-a-Catalog) as required.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg)

* When creating a union query, the selecting order should refer to the order in the primary query. The SQL type and the number of the selected columns should match those in the primary query. For example, if you select two columns in the primary query, the first one is of the Integer data type, and the second one is of String type. Then, in the union query, you should also first select an Integer column, and then a String type column.
* A union query cannot support formulas and parameters.

## Managing Union Queries

You can manage the union queries you have created by taking the following steps:

1. In the Catalog Manager, right-click the primary query and select **Edit Query**.
2. In the Query Editor dialog box, navigate to **Menu** > **Query** > **Union** > **Select**. Designer displays the Union dialog box.

   ![Union dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556106519/qury_union.gif)
3. To add a union to the query, select a union in the **Queries** box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550823447/btn_addarrow.gif); to remove a union from the query, select it in the **Union** box, and then select **Remove**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420550824215/btn_rmvarrow.gif).
4. In the Union box, select the **Attribute** column to specify the type of the union.
   * ![No Duplicate Records button](https://devnet.logianalytics.com/hc/article_attachments/4420550837783/qury_union1.gif): Select it if you do not want to return duplicate records.
   * ![All Records button](https://devnet.logianalytics.com/hc/article_attachments/4420542083351/qury_union2.gif): Select it if you want to return all records.
5. Select **OK** to confirm the changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664687383-Using-Pre-joins-in-Queries)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661921687-Locking-Queries)
