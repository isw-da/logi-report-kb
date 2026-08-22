---
title: "Creating and Importing SQL Statements"
id: 1500009606822
section: "Connecting to Your Data Sources - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009606822-Creating-and-Importing-SQL-Statements
updated_at: 2021-07-24T16:05:07Z
---

# Creating and Importing SQL Statements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606802-Stored-Procedures) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606842-Using-Data-Sources-via-OOJDBC)

# Creating and Importing SQL Statements

![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")You can make use of the Imported SQL Editor to write your own SQL statements directly in Logi Report Designer, or import SQL statements from SQL files. SQL files are plain text files (.txt or .sql). Logi Report Designer saves SQL statements into a catalog so that you can use them to create reports.

You can jump to the following links in this topic:

* [Differences Between Queries and Imported SQLs](#Dif)
* [Adding SQL Statements into a Catalog](#Add)
* [Updating Imported SQLs](#Update)
* [Writing the SQL Statement](#Write)

## Differences Between Queries and Imported SQLs

The imported SQL statements can work the same as [queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009613142-Queries) in Logi Report, for example, you can use imported SQLs to create page reports directly, use the [Data Manager](https://devnet.logianalytics.com/hc/en-us/articles/1500009613182-Data-Manager) to control data retrieval of the imported SQLs, and create [cached result files](https://devnet.logianalytics.com/hc/en-us/articles/1500009635961-Cached-Query-Results) for the imported SQLs.

However, there are still some differences between queries and imported SQLs:

* Tables/views/synonyms of a connection can be used in queries only after they are added from the raw database into a Logi Report catalog. However, even if they are not added into the catalog, you can still import SQL statements as long as the connection is set up.
* Queries built using the interactive Query Editor will work with other data resources when you create or modify a working set. That is, if you design a report using interactively created queries, you can add additional data resources into the working set afterwards. However, when you design a report using an imported SQL statement, you will only be able to use the data already included in the imported SQL. Due to this, you should make sure that you have included all the required fields in your imported SQL.

You can also use imported SQL statements to build queries and [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009635921-Business-Views).

## This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.Adding SQL Statements into a Catalog

You can add SQL statements into a catalog using the Imported SQL Editor after you have set up a JDBC connection.

1. In the Catalog Manager resource tree, right-click the JDBC connection and select **Add SQL** on the shortcut menu. The [Imported SQL Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009631981-Imported-SQL-Editor-Dialog) opens.

   ![Imported SQL Editor](https://devnet.logianalytics.com/hc/article_attachments/4404916786327/imptdsqledtr.gif)
2. In the **SQL Name** text box, type a name for the SQL statement. You should provide a unique name that has not used in the catalog. Otherwise, you will get a warning message when saving the statement.
3. In the **From DB Catalog** drop-down list, select the catalog in the database where comes the SQL statement.
4. [Write the SQL statement](#Write) directly in the text panel or paste the statement from an outside editor.
5. To import the SQL statement from an SQL file (.txt or .sql), select **Import SQL**. Then in the Select an SQL File dialog, browse to the SQL file and select **Open**. The SQL statement in the file will be loaded into the editor. Note that the existing content in the editor will be overwritten directly. You can only store the latest SQL statement.

   ![Import SQL dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904415255/cnctn_jdbc_obj_sql_impt.png)
6. Make use of the buttons on the toolbar above the text panel to help write the SQL statement. If you want to bookmark a line so that you can search for it easily later, select the **Add Bookmark** button ![Add Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404911666967/btn_bkmrk.gif).
7. Make sure your SQL statement is correct before saving it. You can select the **Check** button ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4404911667223/btn_check.gif) to check whether there are errors in it.
8. To export the SQL statement to an SQL file, select **Export SQL**. Next in the Save SQL dialog, provide the location and name of the SQL file and then select **Save**.

   ![Export SQL dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904415767/cnctn_jdbc_obj_sql_expt.png)
9. Select **Save & Exit** to save the SQL statement into the catalog and exit the editor. The SQL statement is then added to the **Imported SQLs** node in the catalog resource tree. You can right-click it and select **Show SQL** from the shortcut menu to view its statement if you want.

## This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.Updating the Imported SQL Files

You can update the imported SQL statements when needed in the Logi Report catalog so that reports will be able to obtain the latest data from them.

1. From the **Imported SQLs** node in the catalog resource tree, select an SQL statement, right-click it and select **Update** from the shortcut menu.
2. In the [Imported SQL Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009631981-Imported-SQL-Editor-Dialog), work with the SQL statement as you do in the section above [Adding SQL Statements into a Catalog](#Add), except that you cannot change the SQL statement's name.

## Writing the SQL Statement

The SQL statement here supports the SQL 92 standard, although for different databases, it may vary. The basic statement of an SQL is:

`Select...FROM...WHERE`

Nested queries are also supported.

The following is an example:

```
SELECT Catalog."Product Type Name", Catalog."Product Type ID",  
Catalog.Description, Products.Category,  
Products."Product ID", Products.Price, Products."Product Name",  
Customers.Region, Customers."Contact Position", Customers.Country,  
Customers."Customer ID", Customers.Address2, Customers.Address1,  
Customers."Contact Title", Customers.Phone, Customers."Contact Last Name",  
Customers.City, Customers.Fax, Customers."Contact First Name",  
Customers."Annual Sales", Customers."Customer Name", Customers."Postal Code",  
Orders."Order ID", Orders."Required Date", Orders."Customer ID",  
Orders."Shipping Cost", Orders."Ship Date", Orders."Order Date",  
Orders."Employee ID", Orders.Shipped, Orders."Payment Received",Orders."Ship Via"  
FROM Catalog, Products, Customers, "Orders Detail", Orders  
WHERE (Products."Product Type ID"=Catalog."Product Type ID")  
AND ("Orders Detail"."Product ID"=Products."Product ID")  
AND (Orders."Customer ID"=Customers."Customer ID")  
AND (Orders."Order ID"="Orders Detail"."Order ID")  
AND (( Customers.Country='USA' ))
```

When you write the SQL statement, you can use [parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009611462-Parameters) and [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009611142-Formula-Levels#CLF) predefined in the catalog data source in which the JDBC connection is created in the format *@FieldName* or *:FieldName* to calculate your data. For example, if you need to get different result sets from the SQL statement at runtime, you can [reference parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009611482-Parameter-Application-Cases#FilterQuery) in the WHERE clause of the SQL statement by to dynamically filter the data. In the above SQL example, if you want to use a parameter to return a result set in which the customer ID is greater than the parameter, then the WHERE clause would be like this:

`WHERE (Products."Product Type ID"=Catalog."Product Type ID") AND ("Orders Detail"."Product ID"=Products."Product ID") AND (Orders."Customer ID"=Customers."Customer ID") AND (Orders."Order ID"="Orders Detail"."Order ID") AND ( ( Customers.Country='USA' )) AND  (Customers."Customer ID" > @pID)`

Where, pID is a parameter created in the catalog.

However, if a parameter allows multiple values and is enabled to use one single value "All" to represent all its values (the parameter's [Enable the "All Values" Option](https://devnet.logianalytics.com/hc/en-us/articles/1500009611502-Creating-Parameters-in-a-Catalog#All) is true), to use the parameter in the SQL statement, you should embed the IN condition in parenthesis to enable the "All" value to work properly, for example:

`Select... from ... where ... and ... and (country in @pCountry) and (customerid in @pID)`

In addition, in an Oracle database, if you want to use a Date or DateTime type parameter or a specific date or time in the WHERE clause of the SQL statement to filter the data, you need to add the to\_date() or to\_timestamp() function in the clause, for example:

`WHERE (@COL_DATE = to_date(@p_DATE,'yyyy-mm-dd')`  
`WHERE (@COL_DATE = to_date('2003-12-06','yyyy-mm-dd')`

Besides using parameters, you can also use the special field [User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500009606442-Special-Fields#UserName) as *@username* in the WHERE clause of the SQL statement to filter the data.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606802-Stored-Procedures) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606842-Using-Data-Sources-via-OOJDBC)
