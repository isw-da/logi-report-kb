---
title: "Joining Tables in a Query"
id: 1500009592501
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009592501-Joining-Tables-in-a-Query
updated_at: 2021-07-24T05:53:53Z
---

# Joining Tables in a Query

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570762-Adding-and-Deleting-Tables-in-a-Query)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570722-Filtering-the-Fields-of-a-Query)

# Joining Tables in a Query

There are two ways to create joins between tables in a query, automatically or manually. Any joins defined between two tables are represented as arrows connecting the key fields from the two tables. Besides joining tables in the same data source connection, Logi JReport also allows you to join tables that come from different connections to create distributed joins.

Below is list of the sections covered in this topic:

> * [Joining Tables Automatically](#Automatically)
> * [Joining Tables Manually](#Manually)
> * [Editing a Join](#Edit)
> * [Alerting When Cartesian Product is Used](#Alert)

## Joining Tables Automatically

The Auto Join feature enables you to join tables together automatically based upon the following criteria. However if you have specified to [use pre-joins in your queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009592581-Using-Pre-joins-in-Queries), the Auto Join feature will not take effect.

* **Foreign Keys**  
   If there is a column that is defined as foreign key in one table and a primary key in another at the same time, these two tables will be joined together. Not all database systems provide enough information to JDBC drivers to recognize this condition.
* **Primary Keys with Same Names**  
   If a column is defined as a primary key in one table and appears in another table in the same query, these two tables will be joined together.
* **Same Column Names**  
   Tables with the same column name will be joined together. This usually results in many joins being not valid. It takes longer to remove the invalid joins than it does to delete the tables. In this case, delete the tables, then add them again to add the joins manually.

By default all the three auto join criteria are turned on. If you do not want to apply any criteria in a query, in the Query Editor open **Menu** > **Query > Auto Join** and uncheck the criteria you want to turn off. To turn off the criteria for all queries, go to **File > Options > Query Editor** and uncheck the criteria you want to turn off in the Options dialog.

## Joining Tables Manually

To create manual joins, use one of the following two ways:

* Position the mouse pointer over the column that will be the source of the join, then select and hold the left mouse button while dragging the join away from the source column to the destination column.
* Select the columns from two tables while pressing CTRL, then select **Menu** > **Query** > **Join Columns**.

The join relationship is then established between the tables. When more than one relationship is required between two tables, you can create multiple joins between them.

## Editing a Join

No matter whether a join is created automatically or manually, you can further edit it if required. To do this:

1. Double-click the join icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404893822743/btn_join.gif) in the join line. The [Join Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009566602-Join-Options-Dialog) dialog appears.

   ![Join Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889297175/jnoptn.gif)
2. To make the join an [outer join](https://devnet.logianalytics.com/hc/en-us/articles/1500009583161-Defining-the-Join-Relationships-Between-Resources#OuterJoin), check the **Outer Join** option, then select either the **Left**, **Right** or **Full** radio button if you would like all rows of the left table, right table, or both tables to be retrieved.
   Regardless of where the tables are placed in the Query Editor, left table is where the arrow starts and right table is where the arrow points.
3. Edit the join condition in the Condition panel according to your requirements.

   Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) beside the two text boxes to select a column in the two tables involved in the join, or a parameter or constant level formula in the current catalog data source and select the operator to compose the condition. You can also manually input the column, parameter or formula name in the text boxes (parameters and formulas should be input in the format *@ParameterName* or *:ParameterName*.). When [a parameter is referenced](https://devnet.logianalytics.com/hc/en-us/articles/1500009568682-Referencing-Parameters-in-a-Join-Condition) in a join condition, the Ignore Predicate If Parameter Value Is Null setting of the parameter will be ignored.

   To add another condition line, select the **Add Condition** button and define the condition as required. Then from the logic drop-down list, specify the relationship between the two condition lines. Repeat this to add more condition lines if necessary.

   To make some conditions grouped, select them and select the **Group** button, then the selected conditions will be added in one group and work as one line of conditional expression. Conditions and groups together can be further grouped.

   To take any condition or group in a group out, select it and select **Ungroup**.

   To adjust the priority of the conditions, select it and select the **Up** or **Down** button.

   To delete a condition line, select it and select the **Delete** button.
4. Select the **OK** button to accept the changes and close the Join Options dialog.

   Select the **Delete Join** button if you want to delete the join.

**Notes:**

* The feature of multiple joins (more than one join existing between two tables) is supported.
* In Logi JReport Designer, the joins in one path should never form a loop (any table in this path will have direct or indirect joins with all the other tables). If you specify a path which forms a loop, Logi JReport Designer will prompt you to re-select the joins.
* Not all forms of joins are supported by all database systems; for example, MySQL does not support Full Outer Join so be sure to check your DBMS manuals.
* When the tables in a query come from the same collection of a MongoDB database, the joins between them cannot be edited.

## Alerting when Certian Product is Used

A Cartesian product is used when tables are included in the query together with no join specifications.

For example, Table A has three values: A, B and C. Table B has three values: 1, 2 and 3. Value A matches value 1, value B matches value 2, and so on. This is a specific match. However, a Cartesian product could have value A matching with 1, 2 and 3, and value B matching with 1, 2 and 3, and so on. Depending on the data values, Cartesian products can produce a large dataset as unnecessary information will be duplicated. For every record in Table A a record will be created for every record in Table B, thus, if Table A has 10 records and Table B has 10 records the result will be a dataset containing 100 rows. Not all Cartesian products are bad though so it is supported if the result is what you need to use.

You can specify whether to alert when this happens as follows:

1. In the Query Editor, select **Menu** > **Query** > **Current Query Option**.
2. In the [Query Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009567182-Query-Options-Dialog) dialog, check or clear **Warning When Cartesian Exists** and select **OK**.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570762-Adding-and-Deleting-Tables-in-a-Query)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570722-Filtering-the-Fields-of-a-Query)
