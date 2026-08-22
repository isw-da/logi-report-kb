---
title: "Query Editor Dialog Box"
id: 5735552449687
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735552449687-Query-Editor-Dialog-Box
updated_at: 2022-11-02T07:53:28Z
---

# Query Editor Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735524392087-QR-Code-Expert-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735552456215-Query-Modifier-Editor-Dialog-Box)

# Query Editor Dialog Box

You can use the Query Editor dialog box to [create or edit a query](https://devnet.logianalytics.com/hc/en-us/articles/5735547138327-Creating-Queries-in-a-Catalog#Create), or edit the data resources used for a business view in the same way. This topic describes the options in the dialog box.

Designer displays the Query Editor dialog box when you do one of the following:

* In the Catalog Manager, right-click the Queries node, select New Query from the shortcut menu, type a name for the new query and select OK, then in the [Add Tables/Views/Queries dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565004567-Add-Tables-Views-Queries-Dialog-Box), add the resources to use for the query and select OK.
* In the Catalog Manager, right-click a query and select Edit Query on its shortcut menu.
* In the Catalog Manager, right-click the Business Views node, select New Business Views from the shortcut menu, type a name for the new business view and select OK, then in the [Add Tables/Views/Queries dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565004567-Add-Tables-Views-Queries-Dialog-Box), add more than one resource to use for the business view and select OK.
* In the Data panel, right-click a query and select Edit Query from the shortcut menu.
* In the [Business View Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735508168471-Business-View-Editor-Dialog-Box), navigate to Menu > Tools > Query Editor or select Query Editor on the toolbar.
* In the Data screen of the query-based component wizard, select a query and select Edit.
* In the dialog box where a query list is available, select <New Query...> under the Queries node, provide a name for the new query and select OK, then in the [Add Tables/Views/Queries dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565004567-Add-Tables-Views-Queries-Dialog-Box), add the resources to use for the query and select OK.

![Query Editor](https://devnet.logianalytics.com/hc/article_attachments/9898458224151/qryedtr.gif)

Designer displays these options:

**Menu**

* **Query**
  + **Apply**  
    Select to apply the changes to the query.
  + **Save As**  
    Select to save the query with the name you specify.
  + **Add Tables/Views/Queries**  
    Select to open the [Add Tables/Views/Queries dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565004567-Add-Tables-Views-Queries-Dialog-Box) to add tables, views, synonyms, queries, imported SQLs, stored procedures, and user-defined data sources in the current catalog data source to the query. When you select to add a query, imported SQL, stored procedure, or user-defined data source, Designer adds it as a single table with all of its columns.
  + **Delete Table/View/Query**  
    Select to remove the specified table from the query.
  + **Union**  
    Select to create and modify a union for the query.
  + **Filter**  
    Select to open the [Search Condition dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524967319-Search-Condition-Dialog-Box) to specify more criteria to limit the amount of data.
  + **Select Distinct**  
    Select to use the SELECT DISTINCT command instead of SELECT in the SQL statement of the query. Designer enables this option when the query contains only tables/views/synonyms from one JDBC connection, or tables from the same collection of a database in a MongoDB connection.
  + **Ignore Predicate If Parameter Value Is Null**  
    If you select this option, when the query uses a parameter and the parameter value is null at runtime, Server removes this condition from the query's or business view's criterion.

    If a query applies a String-typed parameter and users leave the value of the parameter blank at runtime:

    - If you select "Ignore Predicate If Parameter Value Is Null" for the query, Server regards the value of the parameter as "NULL" and does not display the predicate in the WHERE clause.
    - If you do not select "Ignore Predicate If Parameter Value Is Null" for the query, Server treats the value of the parameter as an empty string (¡®¡¯).
  + **Customized SQL Mode**  
    Select to use the [customized SQL mode](https://devnet.logianalytics.com/hc/en-us/articles/5735547138327-Creating-Queries-in-a-Catalog#SQLMode), in which Designer disables all the functions in the Query Editor dialog box and you can only edit the query by modifying the SQL statement in the SQL window. Designer enables this option when the query contains only tables/views/synonyms from one JDBC connection.
  + **Arrange Tables/Views/Queries**  
    Select to organize the tables that you add into the query.
  + **Show Mapping Names**  
    Select to display the full names of the columns in the criteria panel. This option does not affect the content in the definition. Designer enables this option when the query contains only tables/views/synonyms from one JDBC connection. When it is disabled, Designer treats it as selected.
  + **Show Table Names**  
    Select to display the full names of the columns in the tables in the criteria panel.
  + **Show Paths**  
    Select to show information of the pre-join paths among tables in the query, when you enable the [Pre-join](https://devnet.logianalytics.com/hc/en-us/articles/5735511752087-Editing-Pre-joins-in-a-Catalog) feature.
  + **Join Columns**  
    Select to join the specified columns in tables together.
  + **Auto Join**  
    Select to automatically join the tables that you add to the query based on the default auto join criteria specified in the [Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524192535-Options-Dialog-Box#Query). You can also reset the criteria to join the tables by selecting/clearing the commands on the Auto Join submenu.
    - **Join on foreign keys**  
      Select to automatically join tables in a query through a reference from Table A to a primary key in Table B. For example, an order form in Table A shows information on purchases that are made by a customer with a primary key of CustomerID. The customer ID # refers to a record in Table B which lists a specific address, phone number, name, and so on for the customer. CustomerID in Table A is a foreign key because it links the customer's ordering information in Table A to the customer's information in Table B using the CustomerID field.
    - **Join on primary keys with same names**  
      Select to automatically join tables in a query through a field or a combination of fields that uniquely and specifically identifies a record. For example, OrderID may be the primary key in a table for Orders and also for Payments.
    - **Join on same name**  
      Select to automatically join tables in a query through a link between two columns of the same name in two different tables. This often creates many invalid joins such as Amount that appears in both tables.
  + **Current Query Options**  
    Select to open the [Query Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567086615-Query-Options-Dialog-Box) to change the Auto Join and other options for the query.
* **Column**
  + **New Computed Column**  
    Select to open the [New Computed Column dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552025367-New-Computed-Column-Dialog-Box) to create functions to use for the query. Designer enables this option when the query contains only tables/views/synonyms from one JDBC connection.
  + **Add Formula Fields**  
    Select to open the [Add Formula Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735521729943-Add-Formula-Fields-Dialog-Box) to add formulas to the query.
  + **Delete Column**  
    Select to delete the specified column in the criteria panel. To add the column back, find it in the table and select its check mark.
* **View**  
  Designer enables the options on the View menu when the query contains only tables/views/synonyms from one JDBC connection.
  + **Edit SQL**  
    Select to show the SQL statement of the query.
  + **Preview**  
    Select to open the [Preview Option dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735515166871-Preview-Option-Dialog-Box) to preview the records of the query.
* **Help**  
  Select to view information about the dialog box.

**Toolbar**

* **Add Tables**  
  Select to open the [Add Tables/Views/Queries dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565004567-Add-Tables-Views-Queries-Dialog-Box) to add tables, views, synonyms, queries, imported SQLs, stored procedures, and user-defined data sources in the current catalog data source to the query. When you select to add a query, imported SQL, stored procedure, or user-defined data source, Designer adds it as a single table with all of its columns.
* **Delete Table**  
  Select to remove the specified table from the query.
* **New Computed Column**  
  Select to open the [New Computed Column dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552025367-New-Computed-Column-Dialog-Box) to create functions to use for the query. Designer enables this option when the query contains only tables/views/synonyms from one JDBC connection.
* **Add Formula Fields**  
  Select to open the [Add Formula Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735521729943-Add-Formula-Fields-Dialog-Box) to add formulas to the query.
* **Delete Column**  
  Select to delete the specified column in the criteria panel. To add the column back, find it in the table and select its check mark.
* **Arrange**  
  Select to organize the tables that you add into the query.
* **Preview**  
  Select to open the [Preview Option dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735515166871-Preview-Option-Dialog-Box) to preview the records of the query. Designer enables this option when the query contains only tables/views/synonyms from one JDBC connection.
* **Help**  
  Select to view information about the dialog box.

**Criteria panel**

The panel lists all the columns that you select to use in the query. You can specifically define criteria for the columns in this panel.

**SQL**

Select to view the SQL statement of the query. Designer enables this button when the query contains only tables/views/synonyms from one JDBC connection.

**Show Paths**

Select to view information of the pre-join paths among tables in the query, when you enable the Pre-join feature.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Apply**

Select to apply all changes and leave the dialog box open.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735524392087-QR-Code-Expert-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735552456215-Query-Modifier-Editor-Dialog-Box)
