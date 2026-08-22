---
title: "Predefined SQL Files"
id: 1500009564042
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564042-Predefined-SQL-Files
updated_at: 2021-07-24T05:55:49Z
---

# Predefined SQL Files

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564022-Stored-Procedures)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585421-XML-Connections)

# Predefined SQL Files

For users who wish to write their own SQL statement, Logi JReport enables them to put the SQL statement into a plain text file (.txt or .sql) and then load them from this file. At present each SQL file can only contain one SQL statement.

[Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009592441-Queries) and [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009562582-Business-Views) can be built on imported SQL files and a report is developed from a query (or something else which is functionally similar) or from a business view.

SQL files can also work the same as queries in Logi JReport, but there are some differences:

* Tables/views/synonyms of a connection can be used in queries only after they are added from the raw database into a Logi JReport catalog. However, even if they are not added into catalog, you can still import an SQL file as long as the connection is set up.
* Queries built using the interactive Query Editor will work with other data resources when you create or modify a working set. That is, if you design a report using interactively created queries, you can add additional data resources into the working set afterwards. However, when you design a report using an SQL file, you will only be able to use the contents already included in the SQL file. Due to this, you should make sure that you have included all the required fields in your SQL file.

The same as queries, you can use SQL files to create page reports directly, and use the [Data Manager](https://devnet.logianalytics.com/hc/en-us/articles/1500009592481-Data-Manager) to control the data retrieval of imported SQL files, including the number of rows to be displayed and the duration allowed for the retrieval, and use the manager to keep access information from previous runs of a UDS. You can also create [cached result files](https://devnet.logianalytics.com/hc/en-us/articles/1500009570622-Cached-Query-Results) for SQL files and save the result files somewhere in your machine, then when you view reports based on the SQL files, you can choose to use the data from the cached query result files as opposed to the database.

Below is a list of the sections covered in this topic:

> * [Creating the SQL Statement](#Create)
> * [Adding an SQL File to a Catalog](#Add)
> * [Updating an SQL File](#Update)

## Creating the SQL Statement

The SQL statement here supports the SQL 92 standard, although for different databases, it may vary. The basic statement of an SQL file is:

`SELECT...FROM...WHERE`

Nested queries are also supported.

The following is an example:

|  |
| --- |
| ``` SELECT Catalog."Product Type Name", Catalog."Product Type ID", Catalog.Description, Products.Category, Products."Product ID", Products.Price, Products."Product Name", Customers.Region, Customers."Contact Position", Customers.Country, Customers."Customer ID", Customers.Address2, Customers.Address1, Customers."Contact Title", Customers.Phone, Customers."Contact Last Name", Customers.City, Customers.Fax, Customers."Contact First Name", Customers."Annual Sales", Customers."Customer Name", Customers."Postal Code", Orders."Order ID", Orders."Required Date", Orders."Customer ID", Orders."Shipping Cost", Orders."Ship Date", Orders."Order Date", Orders."Employee ID", Orders.Shipped, Orders."Payment Received",Orders."Ship Via" FROM Catalog, Products, Customers, "Orders Detail", Orders WHERE (Products."Product Type ID"=Catalog."Product Type ID") AND ("Orders Detail"."Product ID"=Products."Product ID") AND (Orders."Customer ID"=Customers."Customer ID") AND (Orders."Order ID"="Orders Detail"."Order ID") AND (( Customers.Country='USA' )) ``` |

When you write the SQL statement, you can use parameters and [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009589701-Formula-Levels#CLF) predefined in the catalog data source in which the JDBC connection is created to calculate your data.

For example, if you need to get different result sets from the SQL file at runtime, you can [reference parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009590161-Dynamically-Filtering-Queries) in the WHERE clause of the SQL statement by *@ParamterName* or *:ParameterName* to dynamically filter the data. In [the above SQL example](#SQL), if you want to use a parameter to return a result set in which the customer ID is greater than the parameter, then the WHERE clause would be like this:

`WHERE (Products."Product Type ID"=Catalog."Product Type ID") AND ("Orders Detail"."Product ID"=Products."Product ID") AND (Orders."Customer ID"=Customers."Customer ID") AND (Orders."Order ID"="Orders Detail"."Order ID") AND ( ( Customers.Country='USA' )) AND  (Customers."Customer ID" > @pID)`

Where, pID is a parameter created in the catalog.

However, in an Oracle database, if you want to use a Date or DateTime type parameter or a specific date or time in the WHERE clause of the SQL statement to filter the dataset, you need to add the to\_date() or to\_timestamp() function in the clause, for example:

`WHERE (@COL_DATE = to_date(@p_DATE,'yyyy-mm-dd')`  
`WHERE (@COL_DATE = to_date('2003-12-06','yyyy-mm-dd')`

Besides using parameters, you can also use the special field User Name as @username in the WHERE clause of the SQL statement to filter the data (to specify the user name used for previewing the report created on such SQL file in Logi JReport Designer, go to **File** > **Options** on the menu bar, in the General category of the Options dialog, set the User Name value).

## Adding an SQL File to a Catalog

After you have set up the JDBC connection and created the SQL file, you can then add it to a catalog. To do this:

1. In the Catalog Manager resource tree, right-click the JDBC connection, then select **Add SQL** on the shortcut menu to display the Select an SQL File dialog.
2. Browse to the SQL file and select **Open**.
3. In the Input SQL Name dialog, enter a name for the SQL file in the SQL Name text box, then select **OK** to add the SQL file to the connection. The format of the SQL file, such as comments, are maintained when it is added into a Logi JReport catalog.

   After the SQL file is added in the catalog, you can also right-click it and select **Show SQL** from the shortcut menu to view the statement of SQL file.

## Updating an SQL File

If you make any changes to SQL files in the database, you will need to update them in the connection so that reports built on them can work properly. To do this:

1. Select any SQL file, right-click it and select **Update** from the shortcut menu.
2. In the Select an SQL File dialog, select the SQL files you want to update, and then select **Open**.
3. In the Select Catalog dialog, select a catalog from the From DB Catalog drop-down list.

   ![Select Catalog dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893971223/cnctn_jdbc_obj_sql_slctctlg.gif)
4. Select the **OK** button to close the dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564022-Stored-Procedures)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585421-XML-Connections)
