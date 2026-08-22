---
title: "Using Imported SQLs"
id: 1500010095181
section: "Connecting to Your Data Sources - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010095181-Using-Imported-SQLs
updated_at: 2021-07-23T19:14:54Z
---

# Using Imported SQLs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057662-Using-Stored-Procedures)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095201-Using-Data-Sources-via-OOJDBC-in-a-Catalog)

# Using Imported SQLs

After you have set up JDBC connections in a catalog, you can use imported SQLs in the catalog based on the tables/views/synonyms in the databases the connections refer to, by writing SQL statements directly in Designer or importing from SQL files (plain text files: .txt or .sql) which contain SQL statements. This topic introduces the syntax of the SQL statements, the differences between imported SQLs and queries, and how you can add imported SQLs into a catalog via the JDBC connections and update them.

This topic contains the following sections:

* [Syntax of the SQL Statements](#Syntax)
* [Differences Between Queries and Imported SQLs](#Dif)
* [Adding Imported SQLs into a Catalog](#Add)
* [Updating Imported SQLs](#Update)

## Syntax of the SQL Statements

The SQL statement supports the SQL 92 standard, although for different databases, it may vary. The basic SQL statement is:

`Select...FROM...WHERE`

Designer only supports SQL of one single statement, and the SQL statement can contain nested queries.

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

When you write the SQL statement, you can use [parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500010099721-Working-with-Parameters) and [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010061022-Formula-Levels#CLF) predefined in the catalog data source in which you have created the JDBC connection in the format *@FieldName* or *:FieldName* to calculate your data. For example, if you need to get different result sets from the SQL statement at runtime, you can [reference parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500010099741-Parameter-Application-Cases#FilterQuery) in the WHERE clause of the SQL statement to dynamically filter the data. In the above SQL example, if you want to use a parameter to return a result set in which the customer ID is greater than the parameter, then the WHERE clause would be like this:

`WHERE (Products."Product Type ID"=Catalog."Product Type ID") AND ("Orders Detail"."Product ID"=Products."Product ID") AND (Orders."Customer ID"=Customers."Customer ID") AND (Orders."Order ID"="Orders Detail"."Order ID") AND ( ( Customers.Country='USA' )) AND  (Customers."Customer ID" > @pID)`

Where, pID is a parameter created in the catalog.

However, if a parameter allows for multiple values and is enabled to use one single value "All" to represent all its values (the parameter's [Enable the "All Values" Option](https://devnet.logianalytics.com/hc/en-us/articles/1500010099761-Creating-Parameters-in-a-Catalog#All) is true), to use the parameter in the SQL statement, you should embed the IN condition in parenthesis to enable the "All" value to work properly, for example:

`Select... from ... where ... and ... and (country in @pCountry) and (customerid in @pID)`

In addition, in an Oracle database, if you want to use a Date or DateTime type parameter or a specific date or time in the WHERE clause of the SQL statement to filter the data, you need to add the *to\_date()* or *to\_timestamp()* function in the clause, for example:

`WHERE (@COL_DATE = to_date(@p_DATE,'yyyy-mm-dd')`  
`WHERE (@COL_DATE = to_date('2003-12-06','yyyy-mm-dd')`

Besides using parameters, you can also use the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500010094881-Working-with-Special-Fields#UserName)" as *@username* in the WHERE clause of the SQL statement to filter the data.

## Differences Between Queries and Imported SQLs

The imported SQLs can work the same as [queries](https://devnet.logianalytics.com/hc/en-us/articles/1500010062562-Working-with-Queries) in Designer. For example, you can use imported SQLs to create page reports directly, use the [Data Manager](https://devnet.logianalytics.com/hc/en-us/articles/1500010062602-Managing-the-Data-Retrieval-of-Queries) to control data retrieval of the imported SQLs, and create [cached result files](https://devnet.logianalytics.com/hc/en-us/articles/1500010101101-Working-with-Cached-Query-Results) for the imported SQLs.

However, there are still some differences between queries and imported SQLs:

* You can use tables/views/synonyms in queries only after you have added them from the raw database into a catalog via a JDBC connection. However, even if you have not added them into the catalog, you can still use imported SQLs as long as you have created the connection.
* Queries built using the interactive Query Editor work with other data resources when you create or modify a working set. That is, if you design a report using interactively created queries, you can add additional data resources into the working set afterwards. However, when you design a report using an imported SQL, you can only use the data already included in the statement of the imported SQL. Due to this, you should make sure that you have included all the required fields in the imported SQL.

You can also use imported SQLs to build queries and [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500010101021-Working-with-Business-Views).

## Adding Imported SQLs into a Catalog

You can add imported SQLs into a catalog using the Imported SQL Editor after you have set up a JDBC connection.

1. In the Catalog Manager resource tree, right-click the JDBC connection and select **Add SQL** on the shortcut menu. Designer displays the [Imported SQL Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059562-Imported-SQL-Editor-Dialog-Box).

   ![Imported SQL Editor](https://devnet.logianalytics.com/hc/article_attachments/4404848525079/imptdsqledtr.gif)
2. In the **SQL Name** text box, type a name for the imported SQL. You should provide a unique name that has not been used in the catalog; otherwise, Designer prompts you a warning message when you save the imported SQL.
3. In the **From DB Catalog** drop-down list, select the catalog in the database which contains the tables/views/synonyms you want to use in the imported SQL.
4. Create the statement of the imported SQL. You can write the SQL statement directly in the text panel, paste it from an outside editor, or import it from an SQL file. Make use of the buttons on the toolbar above the text panel to help write the SQL statement. If you want to bookmark a line so that you can search for it easily later, select the **Add Bookmark** button ![Add Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404856870039/btn_bkmrk.gif). Select the **Check** button ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4404856870295/btn_check.gif) to check whether there are errors in the SQL statement.

   To import the SQL statement from an SQL file, select **Import SQL**. In the Select an SQL File dialog box, browse to the SQL file and select **Open**. Designer then loads the SQL statement in the file into the Imported SQL Editor dialog box.

   ![SQL Statement](https://devnet.logianalytics.com/hc/article_attachments/4404857028631/cnctn_jdbc_obj_sql_impt.gif)

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) When you import the SQL statement from an SQL file,

   * Designer overwrites the existing content in the text panel directly if there is any. You can further edit the SQL statement in the panel.
   * If the database catalog selected in the From DB Catalog drop-down list does not contain the tables/views/synonyms referenced in the SQL statement, Designer displays an error message when you select the Check button ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4404856870295/btn_check.gif) to check the statement syntax. In this case, you can re-select the catalog from the drop-down list in accordance with the actual database catalog of the SQL statement. There is also another way to avoid such error: you can use 3-part names in the SQL file, for example, `SELECT catalog.schema.t.c from catalog.schema.t`, then no matter what database catalog you have selected in the From DB Catalog drop-down list, the SQL statement imported from an outside SQL file can always work correctly in Designer.
5. To export the SQL statement to an SQL file, select **Export SQL**. Next in the Save SQL dialog box, provide the location and name of the SQL file and then select **Save**.

   ![Export SQL dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404857029015/cnctn_jdbc_obj_sql_expt.png)
6. Select **Save & Exit** to save the imported SQL into the catalog and exit the editor. Designer then adds it to the **Imported SQLs** node in the catalog resource tree. You can right-click the imported SQL and select **Show SQL** from the shortcut menu to view its statement if you want.

## Updating the Imported SQLs

You can update the imported SQLs when needed so that reports can obtain the latest data from them.

1. From the **Imported SQLs** node in the catalog resource tree, select an imported SQL, right-click it and select **Update** from the shortcut menu.
2. In the Imported SQL Editor dialog box, work with the SQL statement as seen above, except that you cannot change the SQL Name.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057662-Using-Stored-Procedures)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095201-Using-Data-Sources-via-OOJDBC-in-a-Catalog)
