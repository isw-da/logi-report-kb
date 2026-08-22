---
title: "Creating Queries in a Catalog"
id: 1500009635981
section: "Manipulating the Data Resources in a Catalog - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009635981-Creating-Queries-in-a-Catalog
updated_at: 2021-07-24T16:03:25Z
---

# Creating Queries in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009613142-Queries) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009636061-Using-Pre-joins-in-Queries)

# Creating Queries in a Catalog

This topic introduces how to create and edit queries in a catalog as follows:

* [Predefining Queries in a Catalog](#Create)
* [Adding Extra Tables to a Query](#AddTable)
* [Removing Tables from a Query](#RemoveTable)
* [Joining Tables in a Query](#Join)
* [Editing the Joins in a Query](#EditJoin)
* [Filtering a Query](#FilterQuery)
  + [Filtering with the QBE Format](#QBE)
  + [Filtering with the Filter Format](#Filter)
    - [Inputting Filter Condition Values Manually](#InputValue)
    - [Using Sub-queries in the Filter Conditions](#Subquery)
* [Creating Computed Columns in a Query](#ComputedColumn)
* [Adding Formula Fields to a Query](#FormulaField)
* [Editing the SQL Statements of a Query](#EditSQL)
* [Previewing a Query](#Preview)

## Predefining Queries in a Catalog

1. [Open the required catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs#Open), then do either of the following:
   * In the Catalog Manager, expand the data source in which you want to create the query, then select the **Queries** node or any existing query in the data source and select **New Query** on the Catalog Manager toolbar, or right-click the **Queries** node in the data source and select **New Query** from the shortcut menu.
   * Select **Home** > **New** > **Query** or **File** > **New** > **Query**, specify the data source in which the query will be created, then select **OK**.
2. In the Enter Query Name dialog, give a name for the query and select **OK**. The [Add Tables/Views/Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009607182-Add-Tables-Views-Queries-Dialog) dialog appears.

   ![Add Tables/Views/Queries dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911634967/addtbvwqy.gif)
3. Add the resources based on which to create the query.

   If the catalog data source is connected with multiple connections, you can mash up multiple data resources in the query that come from all these connections, including tables, views, synonyms, queries, imported SQLs, imported APEs, stored procedures and user defined data sources. When a query, imported SQL, imported APE, stored procedure or user defined data source is added, it will be added as a single table with all of its columns. When two resources (for example, a table and a view) use the same name, they cannot be added to the query at the same time, and when a table is already contained in a query, you cannot add the table and the query at the same time.

   If the current catalog data source contains JDBC connections, the Show Tables/Views Already Added option is available. Select it if you want to show the tables, views and synonyms in the resource tree in the left box, which have already been added to the right box. You can then add the tables, views and synonyms of the JDBC connections to the query as many times as you want by providing different names for the tables, views and synonyms each time you add them.
4. Select **OK**. The [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009609882-Query-Editor-Dialog) appears, with the selected resources displayed as tables.

   ![Query Editor](https://devnet.logianalytics.com/hc/article_attachments/4404904196375/qryedtr.gif)
5. You can select **Add Tables** on the toolbar to [add more data to the query](#AddTable).
6. Select the required columns in each table. To select all, select **\***. The columns will be displayed in the criteria panel in the lower part of the Query Editor. However for tables from MongoDB connections, you cannot select all columns by selecting **\***. The PrimaryKey and ForeignKey columns in such table cannot be selected to a query.
7. [Join the tables](#Join) as required.
8. [Create filters](#FilterQuery) to narrow down data retrieved to the query.
9. You can add [computed columns](#ComputedColumn) and [formula fields](#FormulaField) to the query.
10. Select **Apply** to save the query and then select **OK** to close the editor.

Besides predefining queries in a catalog from the Catalog Manager, you can also add queries to a catalog from the query resource tree in the Data screen of the report wizard. For example, when you insert a chart in a query based page report, you can select the <New Query...> item in the resource tree to create a query using the Query Editor for the chart.

**Note:** Normally, a query returns all the records that match its search criteria without considering whether there are duplicated ones. You can decide to get only one copy for each record by selecting Menu > Query > Select Distinct. When this option is enabled, SQL SELECT statements are treated as SELECT DISTINCT statements. The query will search for identical records and ensures to return them only once instead of returning duplicate records from the database. However, this feature works when the query contains only tables, views, and synonyms from JDBC connections, or only tables from collections of the same MongoDB database of MongoDB 3.2 or higher and all joins between the tables are left-outer equi-joins of one-way link.

## Adding Extra Tables to a Query

1. In the Query Editor, select **Menu** > **Query** > **Add Tables/Views/Queries**. The [Add Tables/Views/Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009607182-Add-Tables-Views-Queries-Dialog) dialog appears.

   ![Add Tables/Views/Queries dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911634967/addtbvwqy.gif)
2. In the All Tables/Views/Queries box, all the tables, views, synonyms, queries, imported SQLs, stored procedures and user defined data sources in the current catalog data source in which the query is added are listed. Select the resources you want to use in the query and select **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif)** to add them into the Selected Tables/Views/Queries box.
   You can mash up multiple data resources from the same catalog data source in a query if you want. When two resources (for example, a table and a view) use the same name, they cannot be added to the query at the same time, and when a table is already contained in a query, you cannot add the table and the query at the same time.

   To remove unwanted resources from the Selected Tables/Views/Queries box, select them and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)**.
3. If the current catalog data source contains JDBC connections, the Show Tables/Views Already Added option is available. Select it if you want to show the tables, views and synonyms in the resource tree in the left box, which have already been added to the right box. You can then add the tables, views and synonyms of the JDBC connections to the query as many times as you want by providing different names for the tables, views and synonyms each time you add them.
4. Select **OK** to add the selected resources to the current query. When a query, imported SQL, stored procedure or user defined data source is added, it will be added as a single table with all of its columns unselected to be included.
5. Select **Menu** > **Query** > **Arrange Table/View/Query**  to organize the tables.
6. Select the required columns in each table. To select all columns in a table, select **\*** at the top of the table. The columns will be displayed in the criteria panel in the lower part of the Query Editor. However for tables in MongoDB connection, you cannot select all columns by selecting **\***. The PrimaryKey and ForeignKey columns in each table cannot be selected to a query.

## Removing Tables from a Query

1. In the Query Editor, select the table that you want to delete, then do any of the following:
   * Select **Delete Table** on the toolbar.
   * Select **Menu** > **Query** > **Delete Table/View/Query**.
   * Select the **x** button at the top right corner of the table.
2. Repeat the above steps to delete other tables. After deleting a table from a query, any joins based on the table will be removed.

## Joining Tables in a Query

Based on the [Auto Join](https://devnet.logianalytics.com/hc/en-us/articles/1500009609482-Options-Dialog#Query) options that are selected in the Query Editor category of the Options dialog, Logi Report will join the tables in a query automatically. You can also add more joins among these tables manually. Any joins defined between two tables are represented as arrows connecting the key fields from the two tables. Logi Report supports joining tables that come from different connections in the same catalog data source to create distributed joins.

* **To join the tables in a query automatically:**The Auto Join feature enables you to join tables together automatically based upon the following criteria:
  + **Foreign Keys**  
     If there is a column that is defined as foreign key in one table and a primary key in another at the same time, these two tables will be joined together. Not all database systems provide enough information to JDBC drivers to recognize this condition.
  + **Primary Keys with Same Names**  
     If a column is defined as a primary key in one table and appears in another table in the same query, these two tables will be joined together.
  + **Same Column Names**  
     Tables with the same column name will be joined together. This usually results in many joins being not valid. It takes longer to remove the invalid joins than it does to delete the tables. In this case, delete the tables, then add them again to add the joins manually.

  By default all the three auto join criteria are turned on. If you do not want to apply any criteria in a query, in the Query Editor open **Menu** > **Query > Auto Join** and clear the criteria you want to turn off. To turn off the criteria for all queries, go to **File > Options > Query Editor** and clear the criteria you want to turn off in the Options dialog. However if you have specified to [use pre-joins in your queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009636061-Using-Pre-joins-in-Queries), the Auto Join feature will not take effect.
* **To join the tables in a query manually:**
  + Position the mouse pointer over the column that will be the source of the join, then select and hold the left mouse button while dragging the join away from the source column to the destination column.
  + Select the columns from two tables while pressing CTRL, then select **Menu** > **Query** > **Join Columns**.

  The join relationship is then established between the tables. When more than one relationship is required between two tables, you can create multiple joins between them.

However when you use the Auto Join feature to join the tables in a query automatically, you often see many joins that are not valid. You can delete unneeded joins by double-clicking the join icon ![Join button](https://devnet.logianalytics.com/hc/article_attachments/4404904196631/btn_join.gif) and selecting Delete Join in the Join Options dialog.

**Alerting when Cartesian product is used**

A Cartesian product is used when tables are included in a query together with no join specifications. You can specify whether to alert when this happens for a query as follows: in the Query Editor select **Menu** > **Query** > **Current Query Option**, then in the [Query Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009633161-Query-Options-Dialog) dialog, select or clear **Warning When Cartesian Exists** and select **OK**.

For example, Table A has three values: A, B and C. Table B has three values: 1, 2 and 3. Value A matches value 1, value B matches value 2, and so on. This is a specific match. However a Cartesian product could have value A matching with 1, 2 and 3, and value B matching with 1, 2 and 3, and so on. Depending on the data values, Cartesian products can produce a large dataset as unnecessary information will be duplicated. For every record in Table A a record will be created for every record in Table B, thus if Table A has 10 records and Table B has 10 records the result will be a dataset containing 100 rows. However not all Cartesian products are bad so you could use Cartesian product if the result is what you need.

## Editing the Joins in a Query

1. In the Query Editor, double-click the join icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404904196631/btn_join.gif) in the join line. The [Join Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009608902-Join-Options-Dialog) dialog appears.

   ![Join Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911635607/jnoptn.gif)
2. To make the join an [outer join](https://devnet.logianalytics.com/hc/en-us/articles/1500009605262-Editing-Pre-joins-in-a-Catalog#OuterJoin), select the **Outer Join** option, then select either the **Left**, **Right** or **Full** radio button if you would like all rows of the left table, right table, or both tables to be retrieved.
   Regardless of where the tables are placed in the Query Editor, left table is where the arrow starts and right table is where the arrow points.
3. Edit the join condition in the Condition panel according to your requirements.

   Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) beside the two text boxes to select a column in the two tables involved in the join, or a [parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009611462-Parameters) or [constant level formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009611142-Formula-Levels#CLF) in the current catalog data source and select the operator to compose the condition. You can also manually type the column, parameter, or formula name in the text boxes (the input format for parameters and formulas should be *@FieldName* or *:FieldName*.). When a parameter is referenced in a join condition, the Ignore Predicate If Parameter Value Is Null setting of the parameter will be ignored. Using parameters in the join conditions can dynamically change query results at runtime. It works similarly as in [query filters](https://devnet.logianalytics.com/hc/en-us/articles/1500009611482-Parameter-Application-Cases#FilterQuery).

   To add another condition line, select the **Add Condition** button and define the condition as required. Then from the logic drop-down list, specify the relationship between the two condition lines. You can repeat this to add more condition lines.

   To make some conditions grouped, select them and select the **Group** button, then the selected conditions will be added in one group and work as one line of conditional expression. Conditions and groups together can be further grouped.

   To take any condition or group in a group out, select it and select **Ungroup**.

   To adjust the priority of the conditions, select it and select the **Up** or **Down** button.

   To delete a condition line, select it and select the **Delete** button.
4. Select the **OK** button to accept the changes and close the Join Options dialog.

   Select the **Delete Join** button if you want to delete the join.

**Notes:**

* In Logi Report Designer, the joins in one path should never form a loop (any table in this path will have direct or indirect joins with all the other tables). If you specify a path which forms a loop, Logi Report Designer will prompt you to re-select the joins.
* Not all forms of joins are supported by all database systems; for example, MySQL does not support Full Outer Join so be sure to check your DBMS manuals.
* When the tables in a query come from the same collection of a MongoDB database, the joins between them cannot be edited.

## Filtering a Query

You can specify criteria to filter the columns to be retrieved from the database for a query, so that when you build reports on the query, the returned results will be narrowed down.

Filter condition can be composed in both the format of a QBE (Query By Example) and a filter. Using the filter format, you can define the condition on the query and any tables in the query. The overall filter condition applied to a query will include all of them, that is *QBE filter AND query filter AND table filter*. Always select the SQL button to view your condition and parse the query to ensure the syntax is valid.

### Filtering with the QBE format

The criteria panel in the lower part of the Query Editor is for you to filter out some unnecessary records in a query. This filter is in the format of Query by Example (QBE). The advantage of QBE retrieval is that you don't need to learn a query language to frame a query. All the data fields added to a query are shown to you, and all you need to do is to specify the information that restricts the search to the required criteria. Any fields left blank will match everything.

When filtering with the QBE format, you are prompted to type the search criteria into a template resembling the data record. For example, if a column is labeled REGION, and it is a list of all 50 states in the United States. If you only want to see information from California (CA) and New York (NY), in the criteria panel, you can pick out CA and NY by placing their names in the column as below.

![Search criteria in criteria panel](https://devnet.logianalytics.com/hc/article_attachments/4404904197015/qury_edt_fltr1.gif)

You just need to type in NY and CA. Logi Report Designer automatically places ='xx' (equal sign and quotes). See a list of the syntax available:

* Comparison predicates ( =, >, <, >=, <=, <> ).
* BETWEEN predicate (example: BETWEEN 1 AND 100).
* IN predicate (example: NOT IN (1, 3, 5)).
* LIKE predicate (example: LIKE '%apple%').
* NULL predicate (example: IS NOT NULL).

Note that in an Oracle database, if you want to use a Date or DateTime type parameter or a specific date or time to filter the column in a query, you need to apply the *to\_date()* or *to\_timestamp()* function in the filter condition, for example:

![Search criteria for Date type](https://devnet.logianalytics.com/hc/article_attachments/4404904197271/qury_edt_fltr2.gif)

**Tips:**

* In the criteria panel, if you do not want to show the table names for the columns, you can clear **Menu** > **Query** > **Show Table Names**.

  ![Criteria panel with Table Names and criteria panel without Table Names](https://devnet.logianalytics.com/hc/article_attachments/4404911635991/qury_edt_tbl.gif)
* From the criteria panel you can delete any column in a table. To do this, select the column in the panel and select **Delete Column** on the toolbar or select **Menu** > **Column** > **Delete Column**. To undo the deletion, find the column in the table and place a check mark beside it.

### Filtering with the Filter Format

Compared with QBE, the filter format provides you with more flexibility with composing the conditions. The expression includes not only the DBFields, but also formulas and parameters. You can also manually type in strings that are supported by the database, for example, you can reference functions predefined in the database like *qualifier.functionname* (*qualifier* is optional) in the conditions.

When you use the filter format to filter a query, you can add the filter conditions on both the query and any tables in the query. A filter based on a query is applied as long as the query is used or referenced, while a filter based on a specific table in a query is applied only when the table is queried at runtime.

* To create a filter based on a query, select **Menu** > **Query** > **Filter** in the Query Editor. In the [Search Condition](https://devnet.logianalytics.com/hc/en-us/articles/1500009610542-Search-Condition-Dialog) dialog specify the filter conditions. The
  resources available for use are the table columns in the query, the parameters, queries and valid formulas of the query in the same catalog data source as the query, and the special field [User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500009606442-Special-Fields#UserName).
* To create a filter based on a specific table in a query, select the button ![Table Filter button](https://devnet.logianalytics.com/hc/article_attachments/4404911636247/btn_tblfltr.gif) on the title bar of the table in the Query Editor. In the [Table Filter Condition](https://devnet.logianalytics.com/hc/en-us/articles/1500009610622-Table-Filter-Condition-Dialog) dialog specify the filter conditions. The resources available for use are the columns in the table, the parameters, queries and valid formulas of the table in the same catalog data source as the query, and the special field User Name.

You can compose the filter conditions as follows:

1. Select the **Add Condition** button to add a condition line.

   ![Filter Condition Line](https://devnet.logianalytics.com/hc/article_attachments/4404911636503/qury_crt_fltr.gif)
2. In the field text box, specify the field to be filtered. You can either type in the name of the field manually (the input format should be *@FieldName* or *@"Field Name"* when the field name contains blank space) or select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) to specify the field in the [Expressions](https://devnet.logianalytics.com/hc/en-us/articles/1500009631041-Expressions-Dialog) dialog.
3. From the operator drop-down list, set the operator with which to compose the filter expression.
4. In the value text box, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) to specify the value of how to filter the field in the Expressions dialog or [type the value manually](#InputValue). You can also use [sub-queries](#Subquery) to narrow down the result, or use the special field [User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500009606442-Special-Fields#UserName) or [a parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009611482-Parameter-Application-Cases#FilterQuery) to filter the query dynamically.
5. Select **Add Condition** to add more condition lines and define the logic (And or Or) between the condition lines.

   To make some condition lines grouped, select them and select the **Group** button, then the selected condition lines will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup**.

   To adjust the priority of the condition lines, select it and select the **Up** or **Down** button.

   To delete a condition line, select it and select the **Delete** button.
6. Select **OK** to save the condition.

#### Inputting Filter Condition Values Manually

When you type in the value manually for a condition, you need to pay attention to the following:

* Multiple values should be separated with ",". If "," or "\" is contained in the values, write it as "\," or "\\".
* **For String type values**  
  Quote the values with single quotes.

  Example1: Customers\_Country='USA'.

  Example2: Customers\_Country in 'Australia','Germany','Mexico'

  The quote marks can be typed by yourself or be added by Logi Report Designer automatically. To have the quote marks automatically added by Logi Report Designer, follow the steps below:

  1. Select **Options** in the Catalog Manager.
  2. In the Options dialog, switch to the Query Editor category and select **Automatically add quotation marks on input values**.
  3. Select **OK** to save the settings.
* **For Date type values**  
  Make sure the format of the value you specify is consistent with that of your database. Filters are done in the RDBMS side and some RDBMS have special requirements for the date format, and you need to make sure the date formats specified in the [Data Format tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009608882-Get-JDBC-Connection-Information-Dialog#DateFormat) of the Get JDBC Connection Information dialog are supported by your database.

  In an Oracle database, if you want to use a Date or DateTime type parameter or a specific date or time to filter the fields of a query, you need to use the *to\_date()* or *to\_timestamp()* function in the filter condition, for example:

  ![Search Condition - filter condition](https://devnet.logianalytics.com/hc/article_attachments/4404904197655/qury_edt_fltr3.gif)

#### Using Sub-queries in the Filter Conditions

When filtering the fields of a query with the filter format, you are also enabled to use sub-queries to narrow down the result. The following are syntaxes that can be used in sub-queries.

**Quantified predicate**

A quantified predicate compares a value with a set of values.

* **Syntax**  
  `expression----+- = --+- SOME --+-- ( subselect )  
                                   +- <>  -+  ANY    ---+  
                                   +- ! = --+  ALL   ----+    
                                   +- <   --+  
                                   +- >   --+  
                                   +- <=  --+  
                                   +- ! >  --+  
                                   +- >=  --+  
                                   +- ! < --+`

  The subselect must specify a single result column and can return any number of values, whether they are null or not.

  + When ALL is specified, the result of the predicate is:
    - True if the result of the subselect is empty, or if the specified relationship is true for every value returned by the subselect.
    - False if the specified relationship is false for at least one value returned by the subselect.
    - Unknown if the specified relationship is not false for any values returned by the subselect and at least one comparison is unknown because of a null value.
  + When SOME or ANY is specified, the result of the predicate is:
    - True if the specified relationship is true for at least one value returned by the subselect.
    - False if the result of the subselect is empty, or if the specified relationship is false for every value returned by the subselect.
    - Unknown if the specified relationship is not true for any of the values returned by the subselect and at least one comparison is unknown because of a null value.
* **Examples**  
  `Select qty FROM sales WHERE qty>= ALL (SELECT qty FROM sales)  
   SELECT BUYERID, ITEM FROM ANTIQUES WHERE PRICE != ANY (SELECT PRICE FROM ANTIQUES);`

**EXISTS predicate**

The EXISTS predicate tests for the existence of certain rows.

* **Syntax**  
  `- [ NOT ] EXISTS--(subselect)`

  The subselect may specify any number of columns and,

  + The result is true only if the number of rows specified by the subselect is not zero.
  + The result is false only if the number of rows specified by the subselect is zero.
  + The result cannot be unknown.
* **Example**  
  `Select DISTINCT pub_name FROM publishers WHERE EXISTS (SELECT * FROM titles WHERE pub_id = publishers.pub_id AND type = 'business')`

**IN predicate**

The IN predicate compares a value with a set of values.

* **Syntax**  
  `expression----+-- [NOT] IN --+-- ( subselect )`

  In the subselect form, the subselect must identify a single result column and may return any number of values, whether null or not null.
* **Example**  
  `Select distinct pub_name FROM publishers WHERE pub_id IN (SELECT pub_id FROM titles WHERE type = 'business')`

The following example explains how to apply a subquery when filtering a field:

1. Create a query named mainin in the catalog, add the table Customers and select the following columns: Customers\_Customer ID, Customer Name, Customers\_City, and Customers\_Region.
2. Select **Menu** > **Query** > **Filter** to open the Search Condition dialog.
3. Select the **Add Condition** button to add a condition line.
4. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) beside the field text box. In the Expressions dialog, select the column **Customers\_Customer ID**, then close the dialog.
5. Select **in** as the operator from the operator drop-down list.
6. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) beside the value text box. In the Expressions dialog, select the **Subquery** tab. Select an existing query in the catalog to be the subquery. If you want to edit the selected query, select the **Edit Subquery** button. To create a new subquery, select the **New Subquery** button.

   Here, we create a new query named subin, add the table Orders, select the column Orders\_Customer ID, and add a condition "Ship Via=Express Delivery" in the Search Condition dialog.
7. Select **OK**. The subquery subin will then be added into the value text box. Select **OK** to close the Search Condition dialog.

Now, the subquery subin will be applied to the filter when you build a report that uses the Customers\_Customer ID column.

**Notes:**

* If a query uses a parameter in its filter criteria, you can decide what the query does in case that the parameter value is NULL at runtime (for example, not provided). You can choose to remove the parameter condition from the query's filter criteria, or treat the parameter value as a default value (0) or an empty string, which can cause great differences in your report result.

  To remove the parameter condition from a query if this happens, select **Menu** > **Query** > **Ignore Predicate If Parameter Value Is Null** in the Query Editor.
* For string type parameters, when the value is blank, if the Ignore Predicate If Parameter Value Is Null is selected, the value of this parameter will be considered as NULL, and this predicate will not appear in the where clause; if not selected, it will be treated as an empty string ("").
* The following SQL type of data cannot be filtered: Db.SQL\_BINARY, Db.SQL\_BLOB, Db.SQL\_CLOB, Db.SQL\_LONGVARCHAR, Db.SQL\_LONGVARBINARY, Db.SQL\_VARBINARY and Db.SQL\_OTHER.
* After a table filter is applied in a query, you should not [edit the SQL statement](#EditSQL) of the query because Logi Report cannot parse the filter conditions back to a table based filter, thus the table filter may be applied the same as a query filter.

## Creating Computed Columns in a Query

Computed columns can be created in a query that is built on tables, views, and synonyms from one JDBC connection only.

1. In the Query Editor, select **New Computed Column** on the toolbar or select **Menu** > **Column** > **New Computed Column**. The [New Computed Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009609142-New-Computed-Column-Dialog) dialog appears.

   ![New Computed Column dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911636759/nwcmptclmn.gif)
2. Type a name for the column in the Computed Column Name text box.
3. Compose your functions for the column.

   In the lower part of the dialog, there are functions and tables/columns of the query. These are just for your reference. You can specify the expression by yourself in the editing text box, only if the expression can be accepted by your database.

   In addition, the functions in this dialog are not from the Logi Report system. They are from the database you are connected to. If you change your database, some of these functions may no longer exist. For each database, a different set of supported functions will be returned. The following functions will help you with writing an expression.

   * **+**: Add numbers or fields together in the Expression menu.
   * **-**: Subtract numbers or fields together in the Expression menu.
   * **\***: Multiply numbers or fields together in the Expression menu.
   * **/**: Divide numbers or fields together in the Expression menu.
   * **=**: Equate fields together.
   * **"**: Place quotations on long character strings or names that have blanks in them (example: place quotes on values such as "New York" or "Washington DC").
   * **||**: Place fields together in the same Expression menu. (Example: "New York" || "Washington DC").
   * **()**: Place your fields in parentheses.
4. Select **OK** to create the computed column.

The computed columns added to a query are placed in the criteria panel of the Query Editor together with the table columns in the query. If you want to edit a computed column, you can double-click its name in the criteria panel and then edit in the displayed dialog.

When a computed column is created, it will be added to the [SQL of the query](#EditSQL). Suppose you have added a computed column named Net Total in a query and the computation is @UNITPRICE \* @QUANTITY \* (100 - @DISCOUNT) / 100, when you view the SQL statements of the query, you will see the following SQL statement being inserted into the SQL: @UNITPRICE \* @QUANTITY \* (100 - @DISCOUNT) / 100 AS "Net Total".

## Adding Formula Fields to a Query

In addition to the table columns, you can also add formula fields to a query.

1. In the Query Editor, select **Add Formula Fields** on the toolbar or select **Menu** > **Column** > **Add Formula Fields**. The [Add Formula Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009629781-Add-Formula-Fields-Dialog) dialog appears.

   ![Add Formula Fields dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911637015/addfmlfld.gif)
2. The formulas in the current catalog data source that are valid for the query are listed in the Formulas box. Choose the required formula in the box and select **Add**. The formula is then added in the criteria panel of the Query Editor. If the table that contains the columns the selected formula references doesn't exist in the query, this table will be automatically added to the query with the involved columns selected at the same time.
3. Repeat the above step until you have added all the required formulas.
4. Select **Close** to exit the dialog. The selected formula fields will be added to the SELECT columns in the [SQL of the query](#EditSQL).

You can replace any formula field added to a query with another one. To do this, double-click its name in the criteria panel and then choose the required field in the [Replace Formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009610042-Replace-Formula-Dialog) dialog.

**Note:** The processing is very different from adding a [computed column](#ComputedColumn) even though the data looks the same. The computed column is calculated by the database engine before the data is returned. The formula value is calculated by Logi Report after the data is returned so is less efficient.

## Editing the SQL Statements of a Query

For a query built on tables, views, and synonyms from one JDBC connection only, its SQL statements can be edited. To do this, in the Query Editor select the **SQL** button or select **Menu** > **View** > **Edit SQL**, the SQL dialog is then displayed showing the SQL statements used to execute the query like below. You can edit the query statements in the text area as you want. To see whether the statements can be successfully processed by the database, select **Execute**; to accept the changes you have made, select **OK**.

![SQL statements](https://devnet.logianalytics.com/hc/article_attachments/4404911637399/qury_edt_sql.gif)

**Customized SQL mode**

When creating a query using the Query Editor, Logi Report allows you to copy and paste your own SQL statements directly in the SQL dialog as explained above. However, because Logi Report query parser recognizes a limited set of the SQL 92 standard, sometimes Logi Report is not able to parse the customized SQL statements. For example, functions such as aggregations using the GROUP BY clause are not supported. In this case, a warning message is displayed after you select the OK button in the SQL dialog asking whether to continue using the customized SQL statements. If you choose Yes, the customized SQL mode is enabled, in which all the functions in the Query Editor will be disabled, and you can only edit the query by modifying the SQL statements in the SQL dialog. You should guarantee the correctness of the customized SQL statements since Logi Report will not parse it although you can check it by using Execute and passing it to the database to check.

While using the customized SQL mode, you can see that the Menu > Query > Customized SQL Mode option of the Query Editor is enabled and selected. By clearing this option, you can go back to use functions of the Query Editor, in which case the customized SQL statements will be lost and the SQL statements generated by Logi Report will be applied instead.

Therefore, if you want to use customized SQL, it is much better to copy your SQL to a text file and import it using the [Import SQL](https://devnet.logianalytics.com/hc/en-us/articles/1500009606822-Creating-and-Importing-SQL-Statements) feature.

**Notes:**

* If there are parameters in this query, their default values will be used to construct a valid statement.
* If you want to use a parameter which allows multiple values and is enabled to use one single value "All" to represent all its values (the parameter's [Enable the "All Values" Option](https://devnet.logianalytics.com/hc/en-us/articles/1500009611502-Creating-Parameters-in-a-Catalog#All) is true) in the SQL statement, you should embed the IN condition in parenthesis to enable the "All" value to work properly, for example:

  `Select... from ... where ... and ... and (country in @pCountry) and (customerid in @pID)`

## Previewing a Query

1. In the Query Editor, select **Preview**. The Preview Option dialog appears.

   ![Preview Option dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904197911/prvwoptn.gif)
2. In the Max Records text box, specify the maximum number of records to be displayed.
3. In the Records per Page text box, specify the number of records displayed on one page.
4. In the Range box, specify the range of the records for previewing.

   * **Max Records**  
      If the option is selected, the Max Records option will take effect.
   * **All**  
      If the option is selected, all the records will be displayed when you preview the query, and the Max Records option will be disabled.
5. Select **OK**. If the query has parameters, you will be prompted to [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009634541-Specifying-Parameter-Values).

   The Preview dialog appears showing the records. In the dialog, JTable is used to display the result set. When you open the dialog, the result set is cached, and when you close the dialog, the result set is released.

   ![Preview dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911637783/qury_prvw.gif)
6. Select ![First Page button](https://devnet.logianalytics.com/hc/article_attachments/4404904170135/btn_fstpg.gif), ![Previous Topic button](https://devnet.logianalytics.com/hc/article_attachments/4404904170391/btn_prvspg.gif), ![Next Topic button](https://devnet.logianalytics.com/hc/article_attachments/4404911594647/btn_nxtpg.gif) and ![Last Page button](https://devnet.logianalytics.com/hc/article_attachments/4404904170775/btn_lastpg.gif) to browse the records. If the type of the result set is TYPE\_FORWARD\_ONLY, the last page button will be disabled until you have browsed the last page.
7. To refetch the result set, select **Refetch**. Select **Stop** to stop Logi Report from refetching the result set.
8. To print the result set, select **Print** . If you want to preview the result set before printing, select **Print Preview**.
9. If you want to set up the page parameters, select **Page Setup**.
10. Selectthe close button of the dialog to close the Preview dialog.

**Notes:**

* The values shown in the Preview Option dialog when it appears are the default values. These values can be specified in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009609482-Options-Dialog#Query) category in the Options dialog.
* If there are a large number of records in a query, it may take a long time when previewing the query and possibly run out of memory. In this case, it is best to use a parameter value which returns a small number of records.
* When you preview a query, values from [computed columns](#ComputedColumn) are shown in the Preview dialog, while results of [formula fields](#FormulaField) are not shown.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009613142-Queries) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009636061-Using-Pre-joins-in-Queries)
