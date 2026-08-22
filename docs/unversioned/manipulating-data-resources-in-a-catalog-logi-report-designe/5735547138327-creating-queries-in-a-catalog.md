---
title: "Creating Queries in a Catalog"
id: 5735547138327
section: "Manipulating Data Resources in a Catalog - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735547138327-Creating-Queries-in-a-Catalog
updated_at: 2022-11-02T08:17:43Z
---

# Creating Queries in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735547176855-General-Introduction-to-Queries)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735555451159-Using-Pre-joins-in-Queries)

# Creating Queries in a Catalog

Designer includes the interactive Query Editor to help you create and edit queries easily. This topic introduces how you can create and edit queries in a catalog using the functions the editor provides.

This topic contains the following sections:

* [Predefining Queries in a Catalog](#Create)
* [Adding Extra Tables to a Query](#AddTable)
* [Removing Tables from a Query](#RemoveTable)
* [Joining Tables in a Query](#Join)
  + [Joining Tables Automatically](#Auto)
  + [Joining Tables Manually](#Manual)
  + [Alerting When Cartesian Product Exists](#Alert)
* [Editing the Joins in a Query](#EditJoin)
* [Filtering a Query](#FilterQuery)
  + [Filtering with the QBE Format](#QBE)
  + [Filtering with the Filter Format](#Filter)
    - [Inputting Filter Condition Values Manually](#InputValue)
    - [Using Subqueries in the Filter Conditions](#Subquery)
* [Creating Computed Columns in a Query](#ComputedColumn)
* [Adding Formula Fields to a Query](#FormulaField)
* [Editing the SQL Statements of a Query](#EditSQL)
* [Previewing a Query](#Preview)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You can use all of the functions in the Query Editor only when the query is based on tables, views, and synonyms from JDBC connections. If a query mashes up multiple data resources, you can only use part of the functions in the editor.

## Predefining Queries in a Catalog

You can predefine queries in a catalog, so you can use them directly to create reports.

1. [Open the catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735563628951-Creating-Opening-and-Saving-Catalogs#Open), then do either of the following:
   * In the Catalog Manager, expand the data source to create the query, then select the **Queries** node or any existing query in the data source and select **New Query** on the Catalog Manager toolbar, or right-click the **Queries** node in the data source and select **New Query** from the shortcut menu.
   * Navigate to **Home**/**File** > **New** > **Query**, specify the data source to create the query, then select **OK**.
2. In the Enter Query Name dialog box, give a name for the query and select **OK**. Designer displays the [Add Tables/Views/Queries dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565004567-Add-Tables-Views-Queries-Dialog-Box).

   ![Add Tables/Views/Queries dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898458199703/addtbvwqy.gif)
3. In the **All Tables/Views/Queries** box, expand the resource node, select the resources you want to use for the query, select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif) to add the resources to the **Selected Tables/Views/Queries** box, then select **OK**.
   * When the catalog data source is connected with multiple connections, you can mash up multiple data resources in the query that come from all these connections, including [tables, views, synonyms](https://devnet.logianalytics.com/hc/en-us/articles/5735521508887-Using-Tables-Views-Synonyms), [imported SQLs](https://devnet.logianalytics.com/hc/en-us/articles/5735507746711-Using-Imported-SQLs), [imported APEs](https://devnet.logianalytics.com/hc/en-us/articles/5735512889367-Using-Imported-APEs), [stored procedures](https://devnet.logianalytics.com/hc/en-us/articles/5735521490199-Using-Stored-Procedures), [user-defined data sources](https://devnet.logianalytics.com/hc/en-us/articles/5735521621399-Using-User-Defined-Data-Sources) and other existing queries. When you add a query, imported SQL, imported APE, stored procedure, or user-defined data source, Designer adds it as a single table with all of its columns. When two resources (for example, a table and a view) use the same name, you cannot add them to the query at the same time, and when a table is already contained in a query, you cannot add the table and the query at the same time.
   * When the current catalog data source contains JDBC connections, Designer displays the **Show Tables/Views Already Added** option. Select it if you want to show the tables, views, and synonyms in the resource tree in the All Tables/Views/Queries box, which you have already added to the Selected Tables/Views/Queries box. You can then add the tables, views, and synonyms of the JDBC connections to the query as many times as you want by providing different names for the tables, views, and synonyms each time you add them.
4. Designer displays the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552449687-Query-Editor-Dialog-Box), showing the selected resources as tables.

   ![Query Editor](https://devnet.logianalytics.com/hc/article_attachments/9898458224151/qryedtr.gif)
5. You can select **Add Tables** on the toolbar to [add more data to the query](#AddTable).
6. Select the columns in each table that you want to use for the query. To select all columns in a table, select **\***. Designer then displays the columns in the criteria panel in the lower part of the Query Editor dialog box. However, for tables from MongoDB connections, you cannot select all columns by selecting **\***, because you cannot use the PrimaryKey and ForeignKey columns in such table for a query.
7. [Join the tables](#Join).
8. [Create filters](#FilterQuery) to narrow down data retrieved to the query.
9. You can add [computed columns](#ComputedColumn) and [formula fields](#FormulaField) to the query.
10. Select **Apply** to save the query.
11. Select **OK** to close the editor.

Besides predefining queries in a catalog from the Catalog Manager, Designer also provides you quick access to create queries from the UI where a query list is available, for example, in the Data screen of the component wizard. In this query list, you can find the option **<New Query...>** on the top. Select the option and you can create a query in the catalog and use it for the current scenario.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) Normally, a query returns all the records that match its search criteria without considering whether there are duplicated ones. You can choose to get only one copy for each record by selecting **Select Distinct** on the Query menu in the Query Editor dialog box. When you select this option, Logi Report Engine treats SQL SELECT statements as SELECT DISTINCT statements. Logi Report Engine then searches for identical records and ensures to return them only once instead of returning duplicate records from the database. However, this feature works when the query contains only tables, views, and synonyms from JDBC connections, or only tables from collections of the same MongoDB database of MongoDB 3.2 or later and all joins between the tables are left-outer equi-joins of one-way link.

## Adding Extra Tables to a Query

1. In the Query Editor dialog box, navigate to **Menu** > **Query** > **Add Tables/Views/Queries**. Designer displays the [Add Tables/Views/Queries dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565004567-Add-Tables-Views-Queries-Dialog-Box).

   ![Add Tables/Views/Queries dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898458199703/addtbvwqy.gif)
2. In the **All Tables/Views/Queries** box, Designer lists all the tables, views, synonyms, queries, imported SQLs, stored procedures, and user-defined data sources in the current catalog data source that contains the query. Select the resources you want to use in the query and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif) to add them to the **Selected Tables/Views/Queries** box.
   You can mash up multiple data resources from the same catalog data source in a query if you want. When two resources (for example, a table and a view) use the same name, you cannot add them to the query at the same time, and when a table is already contained in a query, you cannot add the table and the query at the same time. To remove unwanted resources from the **Selected Tables/Views/Queries** box, select them and select **Remove**![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif).
3. When the current catalog data source contains JDBC connections, the **Show Tables/Views Already Added** option is available. Select it if you want to show the tables, views, and synonyms in the resource tree in the All Tables/Views/Queries box, which you have already added to the Selected Tables/Views/Queries box. You can then add the tables, views, and synonyms of the JDBC connections to the query as many times as you want by providing different names for the tables, views, and synonyms each time you add them.
4. Select **OK** to add the selected resources to the query. When you add a query, imported SQL, stored procedure, or user-defined data source, Designer adds them as a single table with all of their columns cleared.
5. Navigate to **Menu** > **Query** > **Arrange Table/View/Query** to organize the tables.
6. Select the required columns in each table. To select all columns in a table, select **\*** at the top of the table. Designer then displays the columns in the criteria panel in the lower part of the Query Editor dialog box. However, for tables from MongoDB connections, you cannot select all columns by selecting **\***, because you cannot use the PrimaryKey and ForeignKey columns in such table for a query.

## Removing Tables from a Query

1. In the Query Editor dialog box, select the table that you want to delete, then do one of the following:
   * Select **Delete Table** on the toolbar.
   * Navigate to **Menu** > **Query** > **Delete Table/View/Query**.
   * Select **x** at the top right corner of the table.
2. Repeat the preceding steps to delete other tables. After you delete a table from a query, Designer automatically removes any joins based on the table.

## Joining Tables in a Query

Based on the [Auto join](https://devnet.logianalytics.com/hc/en-us/articles/5735524192535-Options-Dialog-Box#Query) settings in the Query Editor category of the Options dialog box, Designer joins the tables in a query automatically. You can also add more joins among these tables manually. Any joins defined between two tables are represented as arrows connecting the key fields from the two tables. Designer supports joining tables that come from different connections in the same catalog data source to create distributed joins.

### Joining Tables Automatically

The Auto Join feature enables you to join tables together automatically based on the following criteria:

* **Foreign Keys**  
   If there is a column that is defined as foreign key in one table and a primary key in another at the same time, Designer joins these two tables together. Not all database systems provide enough information to JDBC drivers to recognize this condition.
* **Primary Keys with Same Names**  
  If a column is defined as a primary key in one table and appears in another table in the same query, Designer joins these two tables together.
* **Same Column Names**  
  Designer joins tables with the same column name together. This usually results in many joins being not valid.

By default, Designer turns on all the three auto join criteria. If you do not want to apply any criterion in a query, in the Query Editor dialog box, navigate to **Menu** > **Query** > **Auto Join** and clear the criterion you want to turn off. To turn off the criteria for all queries, go to **File** > **Options** > **Query Editor** and clear the criteria you want to turn off in the Options dialog box. However, if you have specified to [use pre-joins in your queries](https://devnet.logianalytics.com/hc/en-us/articles/5735555451159-Using-Pre-joins-in-Queries), the auto join criteria cannot take effect.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) When you use the Auto Join feature to join the tables in a query automatically, you often see many joins that are not valid. You can delete unneeded joins by double-clicking the join icon ![Join button](https://devnet.logianalytics.com/hc/article_attachments/9898458229271/btn_join.gif) and selecting **Delete Join** in the Join Options dialog box. However, it takes longer to remove the invalid joins than it does to delete the tables. In this case, delete the tables, then add them again to add the joins manually.

### Joining Tables Manually

You can join the tables manually using either of the following methods:

* Point to the column that is the source of the join, then select and hold the left mouse button while dragging the join away from the source column to the destination column.
* Select the columns from two tables while selecting Ctrl, then navigate to **Menu** > **Query** > **Join Columns**.

Designer then establishes the join relationship between the tables. When more than one relationship is required between two tables, you can create multiple joins between them.

### Alerting When Cartesian Product Exists

A Cartesian product is used when you add tables to a query with no join specifications. You can specify whether to alert when this happens for a query as follows: in the Query Editor dialog box, navigate to **Menu** > **Query** > **Current Query Option**, then in the [Query Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567086615-Query-Options-Dialog-Box), select or clear **Warn When Cartesian Exists** and select **OK**.

For example, Table A has three values: A, B, and C. Table B has three values: 1, 2, and 3. Value A matches value 1, value B matches value 2, and so on. This is a specific match. However, a Cartesian product could have value A matching with 1, 2, and 3, and value B matching with 1, 2, and 3, and so on. Depending on the data values, Cartesian products can produce a large dataset as unnecessary information is duplicated. For every record in Table A, a record is created for every record in Table B, thus if Table A has 10 records and Table B has 10 records, the result is a dataset containing 100 rows. However, not all Cartesian products are bad so you could use Cartesian product if the result is what you need.

## Editing the Joins in a Query

1. In the Query Editor dialog box, double-click the join icon ![](https://devnet.logianalytics.com/hc/article_attachments/9898458229271/btn_join.gif) in the join line. Designer displays the [Join Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735551861527-Join-Options-Dialog-Box).

   ![Join Options dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898475302679/jnoptn.gif)
2. To make the join an [outer join](https://devnet.logianalytics.com/hc/en-us/articles/5735511752087-Editing-Pre-joins-in-a-Catalog#OuterJoin), select **Outer Join**, then select **Left**, **Right**, or **Full** if you would like all rows of the left table, right table, or both tables to be retrieved.
   Regardless of where you place the tables in the Query Editor dialog box, left table is where the arrow starts and right table is where the arrow points.
3. Edit the join condition in the **Condition** panel.
   * Select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) beside the two text boxes to select a column in the two tables involved in the join, or a [parameter](https://devnet.logianalytics.com/hc/en-us/articles/5735532413719-Working-with-Parameters) or [constant level formula](https://devnet.logianalytics.com/hc/en-us/articles/5735525461399-Formula-Levels#CLF) in the current catalog data source and select the operator to compose the condition. You can also type the column, parameter, or formula name in the text boxes, and the input format for parameters and formulas should be *@FieldName* or *:FieldName*.
   * Select **Add Condition** to define more condition lines and specify the logic relationship between the condition lines: "And", "Or", "And Not", or "Or Not".
     + To group some condition lines, select them and select **Group**, Designer then adds the selected condition lines in one group and applies them as one line of filter expression (you can also group conditions and groups together).
     + To take out any condition or group from a group, select it and select **Ungroup**.
     + To adjust the priority of the condition lines, select it and select **Up** or **Down**.
     + To delete a condition line, select it and select **Delete**.
   * When you reference a parameter in a join condition, Designer ignores the **Ignore Predicate If Parameter Value Is Null** setting of the parameter. Using parameters in the join conditions can dynamically change query results at runtime. It works similarly as in [query filters](https://devnet.logianalytics.com/hc/en-us/articles/5735525858199-Parameter-Application-Cases#FilterQuery).
4. Select **OK** to accept the changes and close the Join Options dialog box. Select **Delete Join** if you want to delete the join.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* The joins in one path should never form a loop (any table in this path has direct or indirect joins with all the other tables). If you specify a path which forms a loop, Designer prompts you to reselect the joins.
* Not all database systems support all the join forms. For example, MySQL does not support Full Outer Join, so be sure to check your database manuals.
* When the tables in a query come from the same collection of a MongoDB database, you cannot edit the joins between them.

## Filtering a Query

You can specify criteria to filter the columns you prefer to retrieve from the database for a query, so that when you build reports on the query, the returned result is narrowed down.

You can compose filter conditions in both the format of a QBE (Query By Example) and a filter. Using the filter format, you can define the conditions on the query and any tables in the query. The overall filter conditions applied to a query includes all of them, that is *QBE filter AND query filter AND table filter*. Always select the SQL button to view your conditions and parse the query to ensure the syntax is valid.

### Filtering with the QBE format

The criteria panel in the lower part of the Query Editor dialog box is for you to filter out some unnecessary records in a query. This filter is in the QBE format. The advantage of QBE retrieval is that you do not need to learn a query language to frame a query. Designer shows you all the data fields you have added to the query, and all you need to do is to specify the information that restricts the search to the required criteria. Any fields left blank match everything.

When filtering with the QBE format, you type the search criteria into a template resembling the record. For example, if a column is labeled REGION, and it is a list of all 50 states in the United States. If you only want to see information from California (CA) and New York (NY), in the criteria panel, you can pick out CA and NY by placing their names in the column as follows:

![Search criteria in criteria panel](https://devnet.logianalytics.com/hc/article_attachments/9898475315351/qury_edt_fltr1.gif)

You just need to type **NY** and **CA**. Designer automatically places ='xx' (equal sign and quotes). The following is a list of the available syntax:

* Comparison predicates ( =, >, <, >=, <=, <> ).
* BETWEEN predicate (example: BETWEEN 1 AND 100).
* IN predicate (example: NOT IN (1, 3, 5)).
* LIKE predicate (example: LIKE '%apple%').
* NULL predicate (example: IS NOT NULL).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* If your query uses tables from an Oracle database and you want to use a parameter of the Date or DateTime data type or a specific date or time to filter the column in the query, you need to apply the *to\_date()* or *to\_timestamp()* function in the filter condition, for example:

  ![Search criteria for Date type](https://devnet.logianalytics.com/hc/article_attachments/9898458285463/qury_edt_fltr2.gif)
* If you do not want to show the table names for the columns in the criteria panel, clear **Show Table Names** on the Query menu in the Query Editor dialog box.

  ![Criteria panel with Table Names and criteria panel without Table Names](https://devnet.logianalytics.com/hc/article_attachments/9898458296983/qury_edt_tbl.gif)
* You can delete any column in a table from the criteria panel: select the column in the panel and select **Delete Column** on the toolbar or navigate to **Menu** > **Column** > **Delete Column** in the Query Editor dialog box. To undo the deletion, find the column in the table and select the checkbox for it.

### Filtering with the Filter Format

Compared with QBE, the filter format provides you with more flexibility with composing the conditions. The expression includes not only the DBFields, but also formulas and parameters. You can also manually type in strings that the database supports. For example, you can reference functions predefined in the database like *qualifier.functionname* ("qualifier" is optional) in the conditions.

When you use the filter format to filter a query, you can add the filter conditions on both the query and any tables in the query. Logi Report Engine applies a filter that is based on a query as long as the query is used or referenced, while a filter based on a specific table in a query is applied only when the table is queried at runtime.

* **To create a filter based on a query**  
  Navigate to **Menu** > **Query** > **Filter** in the Query Editor dialog box. In the [Search Condition dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524967319-Search-Condition-Dialog-Box), specify the filter conditions. The resources available for use are the table columns in the query, the parameters, queries, and valid formulas of the query in the same catalog data source as the query, and the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/5735564398999-Working-with-Special-Fields#UserName)".
* **To create a filter based on a specific table in a query**  
  Select **Filter**![Table Filter button](https://devnet.logianalytics.com/hc/article_attachments/9898475341335/btn_tblfltr.gif) on the title bar of the table in the Query Editor dialog box. In the [Table Filter Condition](https://devnet.logianalytics.com/hc/en-us/articles/5735567745431-Table-Filter-Condition-Dialog-Box) dialog box, specify the filter conditions. The resources available for use are the columns in the table, the parameters, queries, and valid formulas of the table in the same catalog data source as the query, and the special field "User Name".

To specify the filter conditions

1. Select **Add Condition** to add a condition line.

   ![Filter Condition Line](https://devnet.logianalytics.com/hc/article_attachments/9898458334999/qury_crt_fltr.gif)
2. In the field text box (the first text box), specify the field you want to filter. You can either type the name of the field manually (the input format should be *@FieldName* or *@"Field Name"* when the field name contains blank space) or select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) to specify the field in the [Expressions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735529359895-Expressions-Dialog-Box).
3. From the operator drop-down list, set the operator with which to compose the filter expression.
4. In the value text box (the second text box), specify the value of how to filter the field. You can [type the value manually](#InputValue) or select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) to specify the value in the Expressions dialog box. You can also use [subqueries](#Subquery) to narrow down the result, or use the special field "User Name" or [a parameter](https://devnet.logianalytics.com/hc/en-us/articles/5735525858199-Parameter-Application-Cases#FilterQuery) to filter the query dynamically.
5. Repeat the preceding steps to define more condition lines and specify the logic relationship between the condition lines: "And", "Or", "And Not", or "Or Not".
   * To group some condition lines, select them and select **Group**, Designer then adds the selected condition lines in one group and applies them as one line of filter expression (you can also group conditions and groups together).
   * To take out any condition or group from a group, select it and select **Ungroup**.
   * To adjust the priority of the condition lines, select it and select **Up** or **Down**.
   * To delete a condition line, select it and select **Delete**.
6. Select **OK** to save the condition.

#### Inputting Filter Condition Values Manually

When you type the value manually for a condition, you need to pay attention to the following.

* You should separate multiple values with ","; if a value contains the character "," or "\", write the character as "\," or "\\".
* **For String type values**  
  Quote the values with single quotes.

  Example1: Customers\_Country='USA'

  Example2: Customers\_Country in 'Australia','Germany','Mexico'

  You can type the quotation marks by yourself or let Designer add them automatically. To have the quotation marks automatically added by Designer, take the following steps:

  1. Select **Options** in the Catalog Manager.
  2. In the Options dialog box, select the **Query Editor** category and select **Automatically add quotation marks on input values**.
  3. Select **OK** to save the settings.
* **For Date type values**  
  Make sure the format of the value you specify is consistent with that of your database. Filters are executed in the database side and some databases have special requirements for the date format, so you need to make sure your database supports the date formats that you specify in the [Data Format tab](https://devnet.logianalytics.com/hc/en-us/articles/5735530237847-Get-JDBC-Connection-Information-Dialog-Box#DateFormat) of the Get JDBC Connection Information dialog box.

  If your query uses tables from an Oracle database and you want to use a parameter of Date or DateTime data type or a specific date or time to filter the fields of a query, you need to use the *to\_date()* or *to\_timestamp()* function in the filter condition, for example:

  ![Search Condition - filter condition](https://devnet.logianalytics.com/hc/article_attachments/9898475408407/qury_edt_fltr3.gif)

#### Using Subqueries in the Filter Conditions

When filtering the fields of a query with the filter format, you can also use subqueries to narrow down the result. The following shows the subquery syntax.

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

  The *subselect* must specify a single result column and can return any number of values, whether they are null or not.

  + When ALL is specified, the result of the predicate is:
    - "True" if the result of the *subselect* is empty, or if the specified relationship is true for every value returned by the *subselect*.
    - "False" if the specified relationship is false for at least one value returned by the *subselect*.
    - "Unknown" if the specified relationship is not false for any values returned by the *subselect* and at least one comparison is unknown because of a null value.
  + When SOME or ANY is specified, the result of the predicate is:
    - "True" if the specified relationship is true for at least one value returned by the *subselect*.
    - "False" if the result of the *subselect* is empty, or if the specified relationship is false for every value returned by the *subselect*.
    - "Unknown" if the specified relationship is not true for any of the values returned by the *subselect* and at least one comparison is unknown because of a null value.
* **Examples**  
  `Select qty FROM sales WHERE qty>= ALL (SELECT qty FROM sales)  
  SELECT BUYERID, ITEM FROM ANTIQUES WHERE PRICE != ANY (SELECT PRICE FROM ANTIQUES);`

**EXISTS predicate**

The EXISTS predicate tests for the existence of certain rows.

* **Syntax**  
  `- [ NOT ] EXISTS--(subselect)`

  The *subselect* may specify any number of columns and,

  + The result is "true" only if the number of rows specified by the *subselect* is not zero.
  + The result is "false" only if the number of rows specified by the *subselect* is zero.
  + The result cannot be unknown.
* **Example**  
  `Select DISTINCT pub_name FROM publishers WHERE EXISTS (SELECT * FROM titles WHERE pub_id = publishers.pub_id AND type = 'business')`

**IN predicate**

The IN predicate compares a value with a set of values.

* **Syntax**  
  `expression----+-- [NOT] IN --+-- ( subselect )`

  In the *subselect* form, the *subselect* must identify a single result column and may return any number of values, whether null or not null.
* **Example**  
  `Select distinct pub_name FROM publishers WHERE pub_id IN (SELECT pub_id FROM titles WHERE type = 'business')`

The following example explains how to apply a subquery when filtering a field.

1. Create a query **mainin** in the catalog, add the **Customers** table and select the following columns: Customers\_Customer ID, Customer Name, Customers\_City, and Customers\_Region.
2. Navigate to **Menu** > **Query** > **Filter** to open the Search Condition dialog box.
3. Select **Add Condition** to add a condition line.
4. Select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) beside the field text box. In the Expressions dialog box, select the column **Customers\_Customer ID**, then close the dialog box.
5. Select **in** as the operator from the operator drop-down list.
6. Select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) next to the value text box. In the Expressions dialog box, select the **Subquery** tab. Select an existing query in the catalog to be the subquery. If you want to edit the selected query, select **Edit Subquery**. To create a new subquery, select **New Subquery**.

   Here, we create a new query **subin**, add the **Orders** table, select the **Orders\_Customer ID** column, and add a condition "Ship Via=Express Delivery" in the Search Condition dialog box.
7. Select **OK**. Designer then adds the subin subquery into the value text box. Select **OK** to close the Search Condition dialog box.

Designer applies the subin subquery to the filter when you build a report that uses the Customers\_Customer ID column.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* When you use a parameter in the filter criteria of a query, you can specify how to handle the case when the parameter value is NULL at runtime (for example, not provided). You can remove the parameter condition from the query's filter criteria or treat the parameter value as a default value (0) or an empty string, which could cause great differences in your reports.
  If you want to remove the parameter condition from the query when this happens, select **Ignore Predicate If Parameter Value Is Null** on the **Query** menu in the Query Editor dialog box. For a parameter of String data type, when its value is blank, if you select Ignore Predicate If Parameter Value Is Null, Logi Report Engine considers the value of this parameter as NULL, and this predicate does not appear in the where clause; if you do not select Ignore Predicate If Parameter Value Is Null, Logi Report Engine treats the value as an empty string ("").
* You cannot filter the following SQL types of data: Db.SQL\_BINARY, Db.SQL\_BLOB, Db.SQL\_CLOB, Db.SQL\_LONGVARCHAR, Db.SQL\_LONGVARBINARY, Db.SQL\_VARBINARY, and Db.SQL\_OTHER.
* After you apply a table filter to a query, you should not [edit the SQL statement](#EditSQL) of the query because Logi Report Engine cannot parse the filter conditions back to a table-based filter, thus it may apply the table filter the same as a query filter.

## Creating Computed Columns in a Query

You can create computed columns in a query which is based on tables, views, and synonyms from one JDBC connection only.

1. In the Query Editor dialog box, select **New Computed Column** on the toolbar or navigate to **Menu** > **Column** > **New Computed Column**. Designer displays the [New Computed Column dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552025367-New-Computed-Column-Dialog-Box).

   ![New Computed Column dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898475416855/nwcmptclmn.gif)
2. Type a name for the column in the **Computed Column Name** text box.
3. Compose your functions for the column.

   In the lower part of the dialog box, there are functions and tables/columns of the query. They are just for your reference. You can specify the expression by yourself in the editing text box, only if the expression can be accepted by your database. In addition, the functions in this dialog box are not from the Logi Report system. They are from the database you are connecting to. For each database, you may get a different set of the functions. Thus, if you change your database, some of these functions may no longer exist. You can use the following functions to write an expression:

   * **String**  
     Select to use a String formula in the expression.
   * **Numeric**  
     Select to use a Numeric formula in the expression.
   * **Time & Date**  
     Select to use a Time or Date formula in the expression.
   * **+**  
     Select to add the numbers or fields together in the expression.
   * **-**  
     Select to subtract the numbers or fields in the expression.
   * **\***  
     Select to multiply the numbers or fields in the expression.
   * **/**  
     Select to divide the numbers or fields in the expression.
   * **=**  
     Select to equate fields together.
   * **"**  
     Select to place quotations on long character strings or names that have blanks in them. For example, you should place quotes on values such as "New York" or "Washington DC".
   * **||**  
     Select to place fields together in the same expression. For example, "New York" || "Washington DC".
   * **()**  
     Select to place fields in parentheses.
4. Select **OK** to create the computed column.

Designer places the computed columns you add to a query in the criteria panel of the Query Editor dialog box together with the table columns in the query. If you want to edit a computed column, you can double-click its name in the criteria panel and then edit it in the dialog box Designer displays.

After you create a computed column, Designer adds it to the [SQL of the query](#EditSQL). Suppose you have added the Net Total computed column in a query and the computation is *@UNITPRICE \* @QUANTITY \* (100 - @DISCOUNT) / 100*, when you view the SQL statements of the query, you see the following SQL statement being inserted into the SQL: *@UNITPRICE \* @QUANTITY \* (100 - @DISCOUNT) / 100 AS "Net Total"*.

## Adding Formula Fields to a Query

In addition to the table columns, you can also add formula fields to a query.

1. In the Query Editor dialog box, select **Add Formula Fields** on the toolbar or navigate to **Menu** > **Column** > **Add Formula Fields**. Designer displays the [Add Formula Field dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735521729943-Add-Formula-Fields-Dialog-Box).

   ![Add Formula Fields dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898475431575/addfmlfld.gif)
2. Designer lists the formulas in the current catalog data source that are valid for the query in the **Formulas** box. Choose the required formula and select **Add**. Designer then adds the formula in the criteria panel of the Query Editor dialog box. If the table that contains the columns the selected formula references doesn't exist in the query, Designer automatically adds this table to the query with the involved columns selected at the same time.
3. Repeat the preceding step until you add all the required formulas.
4. Select **Close** to exit the dialog box. Designer adds the formula fields to the SELECT columns in the [SQL of the query](#EditSQL).

You can replace any formula field added to a query with another one as follows: double-click its name in the criteria panel and then choose the required field in the [Replace Formula dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735544213527-Replace-Formula-Dialog-Box).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) The processing of a formula field is very different from a [computed column](#ComputedColumn) even though the data looks the same. The computed column is calculated by the database engine before the data is returned, while the formula value is calculated by Logi Report Engine after the data is returned so is less efficient.

## Editing the SQL Statements of a Query

For a query that uses tables, views, and synonyms from one JDBC connection only, you can edit its SQL statements.

1. In the Query Editor dialog box, select **SQL** or navigate to **Menu** > **View** > **Edit SQL**. Designer displays the SQL dialog box, showing the SQL statements used to execute the query.

   ![Query SQL Statements](https://devnet.logianalytics.com/hc/article_attachments/9898458415383/qury_edt_sql.gif)
2. Edit the query statements in the text area as you want.
3. To see whether the statements can be successfully processed by the database, select **Execute**; to accept the changes you have made, select **OK**.

**Customized SQL mode**

When creating a query using the Query Editor, Designer enables you to copy and paste your own SQL statements directly in the SQL dialog box. However, because the Logi Report Query Parser recognizes a limited set of the SQL 92 standard, sometimes, Designer is not able to parse the customized SQL statements. For example, Designer cannot support functions such as aggregations using the GROUP BY clause. In this case, Designer displays a warning message after you select the OK button in the SQL dialog box, asking you whether to continue using the customized SQL statements. If you choose Yes, Designer enables the customized SQL mode, in which all the functions in the Query Editor are disabled, and you can only edit the query by modifying the SQL statements in the SQL dialog box. You should guarantee the correctness of the customized SQL statements since Designer does not parse it although you can check it by using Execute and passing it to the database to check .Therefore, if you want to use customized SQL, you should copy your SQL to a text file and import it using the [Imported SQL](https://devnet.logianalytics.com/hc/en-us/articles/5735507746711-Using-Imported-SQLs) feature.

While using the customized SQL mode, you can see that the Customized SQL Mode command is enabled and selected on the Query menu in the Query Editor dialog box. By clearing the command, you can go back to use functions of the Query Editor. After doing this, the customized SQL statements is lost and the SQL statements generated by Designer are applied instead.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* If there are parameters in this query, Logi Report Engine uses their default values to construct a valid statement.
* If you want to use a parameter which allows multiple values and is enabled to use one single value "All" to represent all its values (the parameter's [Enable the "All Values" Option](https://devnet.logianalytics.com/hc/en-us/articles/5735516481047-Creating-Parameters-in-a-Catalog#All) is true) in the SQL statement, you should embed the IN condition in parenthesis to enable the "All" value to work properly, for example:

  `Select... from ... where ... and ... and (country in @pCountry) and (customerid in @pID)`

## Previewing a Query

1. In the Query Editor dialog box, select **Preview**. Designer displays the Preview Option dialog box.

   ![Preview Option dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898475462423/prvwoptn.gif)
2. In the **Max Records** text box, specify the maximum number of records you want to display.
3. In the **Records per Page** text box, specify the number of records to display on one page.
4. In the **Range** box, specify the range of the records for previewing.
   * **Max Records**  
     Select to display the maximum number of records that you specify for the query.
   * **All**  
     Select to display all the records for the query.
5. Select **OK**. Designer displays the Preview dialog box, showing the records (if the query contains parameters, Designer prompts you to [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/5735525892247-Specifying-Parameter-Values) first). Designer uses JTable to display the result set. When the Preview dialog box is open, Designer caches the result set; when you close the dialog box, Designer releases the result set.

   ![Preview dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898458442007/qury_prvw.gif)
6. Select the navigation buttons to browse the records. If the type of the result set is TYPE\_FORWARD\_ONLY, Designer disables the Last Page button ![Last Page button](https://devnet.logianalytics.com/hc/article_attachments/9898405262487/btn_lastpg.gif) until you browse the last page.
7. To refetch the result set, select **Refetch**. Select **Stop** to stop Designer from refetching the result set.
8. To print the result set, select **Print**. If you want to preview the result set before printing, select **Print Preview**; to set up the page properties for printing, select **Page Setup** and specify the settings.
9. Select the close button of the dialog box to close it.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* If there are a large number of records in a query, Designer may take a long time to display the records when you preview the query and possibly run out of memory. In this case, it is best to use a parameter value which returns a small number of records.
* When you preview a query, Designer displays values from [computed columns](#ComputedColumn) in the Preview dialog box, while Designer does not display results of [formula fields.](#FormulaField)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735547176855-General-Introduction-to-Queries)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735555451159-Using-Pre-joins-in-Queries)
