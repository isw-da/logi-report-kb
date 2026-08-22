---
title: "Imported SQL Files"
id: 1500010064341
section: "Connecting to Your Data Sources - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010064341-Imported-SQL-Files
updated_at: 2021-07-24T10:39:15Z
---

# Imported SQL Files

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029422-Stored-Procedures) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064381-Using-Data-Sources-via-OOJDBC)

# Imported SQL Files

For users who wish to write their own SQL statement, Logi JReport Enables them to put the SQL statement into a plain text file (.txt or .sql) and then import the file into a catalog and Logi JReport can load data from this file. At present each SQL file can only contain one SQL statement.

Below is a list of the sections covered in this topic:

* [Differences Between Queries and Imported SQL Files](#Dif)
* [Creating the SQL Statement](#Create)
* [Importing SQL Files into a Catalog](#Import)
* [Updating the Imported SQL Files](#Update)

## Differences Between Queries and Imported SQL Files

The imported SQL files can work the same as [queries](https://devnet.logianalytics.com/hc/en-us/articles/1500010070681-Queries) in Logi JReport, for example, you can use imported SQL files to create page reports directly, use the [Data Manager](https://devnet.logianalytics.com/hc/en-us/articles/1500010034662-Data-Manager) to control data retrieval of the imported SQL files, and create [cached result files](https://devnet.logianalytics.com/hc/en-us/articles/1500010034602-Cached-Query-Results) for the imported SQL files.

However there are still some differences between queries and imported SQLs:

* Tables/views/synonyms of a connection can be used in queries only after they are added from the raw database into a Logi JReport catalog. However, even if they are not added into catalog, you can still import an SQL file as long as the connection is set up.
* Queries built using the interactive Query Editor will work with other data resources when you create or modify a working set. That is, if you design a report using interactively created queries, you can add additional data resources into the working set afterwards. However, when you design a report using an SQL file, you will only be able to use the contents already included in the SQL file. Due to this, you should make sure that you have included all the required fields in your SQL file.

Imported SQL files can also be use to build queries and [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500010070641-Business-Views).

## Creating the SQL Statement

The SQL statement here supports the SQL 92 standard, although for different databases, it may vary. The basic statement of an SQL file is:

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

When you write the SQL statement, you can use [parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500010068961-Parameters) and [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010068561-Formula-Levels#CLF) predefined in the catalog data source in which the JDBC connection is created in the format *@FieldName* or *:FieldName* to calculate your data. For example, if you need to get different result sets from the SQL file at runtime, you can [reference parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500010068981-Parameter-Application-Cases#FilterQuery) in the WHERE clause of the SQL statement by to dynamically filter the data. In the above SQL example, if you want to use a parameter to return a result set in which the customer ID is greater than the parameter, then the WHERE clause would be like this:

`WHERE (Products."Product Type ID"=Catalog."Product Type ID") AND ("Orders Detail"."Product ID"=Products."Product ID") AND (Orders."Customer ID"=Customers."Customer ID") AND (Orders."Order ID"="Orders Detail"."Order ID") AND ( ( Customers.Country='USA' )) AND  (Customers."Customer ID" > @pID)`

Where, pID is a parameter created in the catalog.

However, if a parameter allows multiple values and is enabled to use one single value "All" to represent all its values (the parameter's [Enable the "All" Option](https://devnet.logianalytics.com/hc/en-us/articles/1500010069001-Creating-Parameters-in-a-Catalog#All) is true), to use the parameter in the SQL statement, you should embed the IN condition in parenthesis to enable the "All" value to work properly, for example:

`Select... from ... where ... and ... and (country in @pCountry) and (customerid in @pID)`

In addition, in an Oracle database, if you want to use a Date or DateTime type parameter or a specific date or time in the WHERE clause of the SQL statement to filter the data, you need to add the to\_date() or to\_timestamp() function in the clause, for example:

`WHERE (@COL_DATE = to_date(@p_DATE,'yyyy-mm-dd')`  
`WHERE (@COL_DATE = to_date('2003-12-06','yyyy-mm-dd')`

Besides using parameters, you can also use the special field [User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500010029242-Special-Fields#UserName) as *@username* in the WHERE clause of the SQL statement to filter the data.

## Importing SQL Files into a Catalog

After you have set up the JDBC connection and created the SQL files, you can import them into a catalog.

1. In the Catalog Manager resource tree, right-click the JDBC connection and select **Add SQL** on the shortcut menu.
2. In the Select an SQL File dialog, browse to the SQL file and select **Open**.
3. In the Enter SQL Name dialog, enter a name for the SQL file in the SQL Name text box and select **OK**.

   The SQL file is then added in the Imported SQLs node in the catalog resource tree. You can right-click it and select **Show SQL** from the shortcut menu to view the statement of SQL file if you want. The format of the SQL file, such as comments, are maintained when it is added into the Logi JReport catalog.

## Updating the Imported SQL Files

If you make any changes to an SQL file, you need to update it in the Logi JReport catalog so that reports built on it can work properly.

1. From the Imported SQLs node in the catalog resource tree, select the SQL file, right-click it and select **Update** from the shortcut menu.
2. In the Select an SQL File dialog, select the SQL file you want to update, then select **Open**.
3. In the Enter SQL Name dialog, select a catalog from the From DB Catalog drop-down list to specify the catalog
   in the database from which to get data in accordance with the SQL statement in the selected SQL file.

   ![Select Catalog dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901308439/cnctn_jdbc_obj_sql_slctctlg.gif)
4. Select **OK** to update the SQL file.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029422-Stored-Procedures) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064381-Using-Data-Sources-via-OOJDBC)
