---
title: "Filtering the Fields of a Query"
id: 1500009570722
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009570722-Filtering-the-Fields-of-a-Query
updated_at: 2021-07-24T05:53:53Z
---

# Filtering the Fields of a Query

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592501-Joining-Tables-in-a-Query)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570742-Editing-the-SQL-Statements-of-a-Query)

# Filtering the Fields of a Query

You can specify certain criteria for the fields of a query to be retrieved from the database via a filter, so that when you build reports on the query, the returned results will be narrowed down. In addition, you can also apply sub-queries to a filter. You can type your filter criteria both in the format of a filter and a QBE (Query By Example). The overall conditions will include them both. Always select the SQL button to view your conditions and parse the query to ensure the syntax is valid.

Below is a list of the sections covered in this topic:

> * [Filtering with the QBE Format](#QBE)
> * [Filtering with the Filter Format](#Filter)
> * [Using Sub-queries in Filters](#Subquery)

## Filtering with the QBE Format

The criteria panel in the lower part of the Query Editor is for you to filter out some unnecessary records in a query. This filter is in the format of Query by Example (QBE).

When filtering with the QBE format, you are prompted to type the search criteria into a template resembling the data record. The advantage of query-by-example retrieval is that you don't need to learn a query language to frame a query. All the data fields are shown to you, and all you need to do is to enter the information that restricts the search to the required criteria. Any fields left blank, however, will match everything.

The columns and menus allow you to specifically define criteria for the fields in Logi JReport Designer. For example, if a field is labeled REGION, and this field is a list of all 50 states in the United States. If you only want to see information from California (CA) and New York (NY), in the criteria menu, you can pick out CA and NY by placing their names in the column as seen below.

![](https://devnet.logianalytics.com/hc/article_attachments/4404893822999/qury_edt_fltr1.gif)

You just need to type in NY and CA. Logi JReport Designer automatically places the ='xx' (equal sign and quotes) in the column for you. Below is a list of the syntax available:

* Comparison predicates ( =, >, <, >=, <=, <> ).
* BETWEEN predicate (example: BETWEEN 1 AND 100).
* IN predicate (example: NOT IN (1, 3, 5)).
* LIKE predicate (example: LIKE '%apple%').
* NULL predicate (example: IS NOT NULL).

Note that in an Oracle database, if you want to use a Date or DateTime type parameter or a specific date or time to filter the field of a query, you need to apply the to\_date() or to\_timestamp() function in the filter condition, for example:

![](https://devnet.logianalytics.com/hc/article_attachments/4404893823255/qury_edt_fltr2.gif)

**Tip:** In the criteria panel, if you do not want to show the table names for the selected columns, you can uncheck **Menu** > **Query** > **Show Table Names**.

![](https://devnet.logianalytics.com/hc/article_attachments/4404889297431/qury_edt_tbl.gif)

From the criteria panel you can also delete any column in a table. To do this, select the column in the panel and select **Delete Column** on the toolbar or select **Menu** > **Column** > **Delete Column**. To undo the deletion, find the column in the table and place a check mark beside it.

## Filtering with the Filter Format

Compared with QBE, the filter provides you with more flexibility with entering your conditions. The expression includes not only the DBField selected, but also formulas and parameters. You can also manually type in strings that are supported by the database.

To filter with the filter format, select **Menu** > **Query** > **Filter** in the Query Editor. The [Search Condition](https://devnet.logianalytics.com/hc/en-us/articles/1500009588921-Search-Condition-Dialog) dialog appears.

![Search Condition dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889297687/srchcdtn.gif)

**Specifying expressions**

The expressions are the main section of the filter. To place a criterion, follow the steps below:

1. Select the **Add Condition** button to add a condition line.
2. In the field text box, specify the field to be filtered. You can either type in the name of the field manually or select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) to specify the field in the [Expressions](https://devnet.logianalytics.com/hc/en-us/articles/1500009565482-Expressions-Dialog) dialog.
3. From the operator drop-down list, set the operator with which to compose the filter expression.
4. In the value text box, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) to specify the value of how to filter the field in the Expressions dialog or [input the value manually](#InputValue). You can also use [sub-queries](#Subquery) to narrow down the result, or use the special field [User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500009584241-Special-Fields#UserName) or [a parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009590161-Dynamically-Filtering-Queries) to filter the query dynamically.
5. Select **Add Condition** to add more condition lines and define the logic between the condition lines.

   To make some condition lines grouped, select them and select the **Group** button, then the selected condition lines will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.**

   To adjust the priority of the condition lines, select it and select the **Up** or **Down** button.

   To delete a condition line, select it and select the **Delete** button.
6. Select **OK** to save the condition.

**Inputting filter condition values manually**

When you input the value manually for a condition, you need to pay attention to the following:

* Multiple values should be separated with ",". If "," or "\" is contained in the values, write it as "\," or "\\".
* **For String type values**  
   Quote the values with single quotes.

  Example1: Customers\_Country='USA'.

  Example2: Customers\_Country in 'Australia','Germany','Mexico'

  The quote marks can be typed by yourself or be added by Logi JReport Designer automatically. To have the quote marks automatically added by Logi JReport Designer, follow the steps below:

  1. Select **Options** in the Catalog Manager windown.
  2. In the Options dialog, switch to the Query Editor category and check **Automatically add quotation marks on input values**.
  3. Select **OK** to save the settings.
* **For Date type values**  
   Make sure the format of the value you enter is consistent with that of your database.
  Filters are done in the RDBMS side and some RDBMS have special requirements for the date format, and you need to make sure the date formats specified in the [Data Format tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009587701-Get-JDBC-Connection-Information-Dialog#DateFormat) of the Get JDBC Connection Information dialog are supported by your database.

  **Note:** In an Oracle database, if you want to use a Date or DateTime type parameter or a specific date or time to filter the fields of a query, you need to use the to\_date() or to\_timestamp() function in the filter condition, for example:

  ![Search Condition - filter condition](https://devnet.logianalytics.com/hc/article_attachments/4404893823511/qury_edt_fltr3.gif)

## Using Sub-queries in Filters

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
  `SELECT qty FROM sales WHERE qty>= ALL (SELECT qty FROM sales)  
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
  `SELECT DISTINCT pub_name FROM publishers WHERE EXISTS (SELECT * FROM titles WHERE pub_id = publishers.pub_id AND type = 'business')`

**IN predicate**

The IN predicate compares a value with a set of values.

* **Syntax**  
  `expression----+-- [NOT] IN --+-- ( subselect )`

  In the subselect form, the subselect must identify a single result column and may return any number of values, whether null or not null.
* **Example**  
  `SELECT distinct pub_name FROM publishers WHERE pub_id IN (SELECT pub_id FROM titles WHERE type = 'business')`

The following example explains how to apply a subquery when filtering a field:

1. Create a query named mainin in the catalog, add the table Customers and select the following columns: Customers\_Customer ID, Customer Name, Customers\_City, and Customers\_Region.
2. Select **Menu** > **Query** > **Filter** to open the Search Condition dialog.
3. Select the **Add Condition** button to add a condition line.
4. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) beside the field text box. In the Expressions dialog, select the column **Customers\_Customer ID**, then close the dialog.
5. Select **in** as the operator from the operator drop-down list.
6. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) beside the value text box. In the Expressions dialog, select the **Subquery** tab. Select an existing query in the catalog to be the subquery. If you want to edit the selected query, select the **Edit Subquery** button. To create a new subquery, select the **New Subquery** button.

   Here, we create a new query named subin, add the table Orders, select the column Orders\_Customer ID, and add a condition "Ship Via=Express Delivery" in the Search Condition dialog.
7. Select **OK**. The subquery subin will then be added into the value text box. Select **OK** to close the Search Condition dialog.

Now, the subquery subin will be applied to the filter when you build a report that uses the Customers\_Customer ID column.

**Notes:**

* If a query uses a parameter in its search criteria, you can decide what the query does in case that the parameter value is NULL at runtime (for example, not provided). You can choose to remove the parameter condition from the query's criterion, or treat the parameter value as a default value (0) or an empty string, which can cause great differences in your report result.

  To remove the parameter condition from a query if this happens, check **Menu** > **Query** > **Ignore Predicate If Parameter Value Is Null** in the Query Editor.
* For string type parameters, when the value is blank, if the Ignore Predicate If Parameter Value Is Null is checked, the value of this parameter will be considered as NULL, and this predicate will not appear in the where clause; if not checked, it will be treated as an empty string ("").
* The following SQL type of data cannot be filtered: Db.SQL\_BINARY, Db.SQL\_BLOB, Db.SQL\_CLOB, Db.SQL\_LONGVARCHAR, Db.SQL\_LONGVARBINARY, Db.SQL\_VARBINARY and Db.SQL\_OTHER.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592501-Joining-Tables-in-a-Query)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570742-Editing-the-SQL-Statements-of-a-Query)
