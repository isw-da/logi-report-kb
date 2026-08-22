---
title: "Query Editor Dialog"
id: 1500010067501
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010067501-Query-Editor-Dialog
updated_at: 2021-07-24T10:38:30Z
---

# Query Editor Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010032222-QR-Code-Expert-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010032242-Query-Modifier-Editor-Dialog)

# Query Editor Dialog

The Query Editor helps you to [edit a query](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog#Create), or edit the data resources used for a business view in the same way. It appears when you do one of the following:

* In the Catalog Manager, right-click the Queries node, select New Query from the shortcut menu, input a name for the new query and select OK, then add the resources based on which to create the query in the [Add Tables/Views/Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500010064701-Add-Tables-Views-Queries-Dialog) dialog and select OK.
* In the Catalog Manager, right-click a query and select Edit Query on its shortcut menu.
* In the Catalog Manager, right-click the Business Views node, select New Business Views from the shortcut menu, input a name in the displayed dialog and select OK, then in the [Add Tables/Views/Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500010064701-Add-Tables-Views-Queries-Dialog) dialog, add more than one resource to use in the business view and select OK.
* Select Menu > Tools > Query Editor or select Query Editor in the [Business View Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010064841-Business-View-Editor-Dialog).

![Query Editor](https://devnet.logianalytics.com/hc/article_attachments/4404909131415/qryedtr.gif)

The following are details about options in the editor:

**Menu**

* **Query Menu**
  + **Apply**  
     Accepts the changes on the query or business view.
  + **Save As**  
     Saves the query with the name you specify.
  + **Add Tables/Views/Queries**  
     Opens the [Add Tables/Views/Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500010064701-Add-Tables-Views-Queries-Dialog) dialog to add tables, views, synonyms, queries, imported SQLs, stored procedures, and user defined data sources in the current catalog data source to the query or business view. When a query, imported SQL, stored procedure or user defined data source is added, it will be added as a single table with all of its columns.
  + **Delete Table/View/Query**  
     Removes the selected resource.
  + **Union**Creates and modifies a union for the query.
  + **Filter**  
     Opens the [Search Condition](https://devnet.logianalytics.com/hc/en-us/articles/1500010067981-Search-Condition-Dialog) dialog to specify more criteria to limit the amount of data.
  + **Select Distinct**  
     When selected, in the SQL statement, the SELECT DISTINCT command will be used instead of SELECT. The option is enabled when the query contains only tables/views/synonyms from one JDBC connection, or tables from the same collection of a database in a MongoDB connection.
  + **Ignore Predicate If Parameter Value Is Null**  
     If the query or business view uses a parameter, and the parameter value is null at runtime, then this condition will be removed from the query's or business view's criterion.

    For string type parameters, when the value is left blank, if Ignore Predicate If Parameter Is Null is set to true, the value of this parameter will be considered as NULL, and this predicate will not appear in the WHERE clause; if false, it will be treated as an empty string (¡®¡¯).
  + **Customized SQL Mode**  
     Specifies whether to use the [customized SQL mode](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog#SQLMode), in which Logi JReport will disable all the functions in the Query Editor and you can only edit the query by modifying the SQL statement in the SQL window. The option is enabled when the query contains only tables/views/synonyms from one JDBC connection.
  + **Arrange Tables/Views/Queries**  
     Organizes the resources added into the query or business view.
  + **Show Mapping Names**  
     Specifies to show the full names of the columns in the Query Editor. The option does not affect the contents in the definition. It is enabled when the query contains only tables/views from one JDBC connection. When it is disabled, the option is treated as checked or true.
  + **Show Table Names**  
     Specifies to show which table each column belongs to in the criteria panel of the Query Editor.
  + **Show Paths**  
     Specifies to show information of the pre-join paths among tables in the query, when the [Pre-join](https://devnet.logianalytics.com/hc/en-us/articles/1500010028522-Editing-Pre-joins-in-a-Catalog) feature is enabled.
  + **Join Columns**  
     Specifies to join the highlighted columns in tables together.
  + **Auto Join**  
     Specifies to join tables together based upon the default criteria set in the Options dialog (**File** > **Options** > **Query Editor** > **Auto Join**). You can also reset the criteria to join tables in the query or business view by checking/unchecking the items on the Auto Join submenu.
    - **Join on foreign keys**  
       Specifies to automatically join tables in a query through a reference from Table A to a primary key in Table B. For example, an order form in Table A shows information on purchases that are made by a customer with a primary key of CustomerID. The customer ID # refers to a record in Table B which lists a specific address, phone number, name, and so on for the customer. The CustomerID in Table A is a foreign key because it links the customer's ordering information in Table A to the customer's information in Table B using the CustomerID field.
    - **Join on primary keys with same names**  
       Specifies to automatically join tables in a query through a field or a combination of fields that uniquely and specifically identifies a record. For example, the OrderID may be the primary key in a table for Orders and also for Payments.
    - **Join on same name**  
       Specifies to automatically join tables in a query through a link between two columns of the same name in two different tables. This often creates many invalid joins such as Amount that appears in both tables.
  + **Current Query Options**  
     Opens the [Query Options](https://devnet.logianalytics.com/hc/en-us/articles/1500010067521-Query-Options-Dialog) dialog to change the Auto Join and other options for the current query.
* **Column**
  + **New Computed Column**  
     Opens the [New Computed Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010031802-New-Computed-Column-Dialog) dialog to create functions used for a particular query. It helps you to quickly and easily create columns with the functions available instead of writing a formula. The option is enabled when the query contains only tables/views/synonyms from one JDBC connection.
  + **Add Formula Fields**  
     Opens the [Add Formula Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010064661-Add-Formula-Fields-Dialog) dialog to add formulas to the query or business view.
  + **Delete Column**  
     Deletes the selected column in the Criteria menu. To undelete, find the field in the table you deleted and place a check mark beside it.
* **View menu**  
   The following two options are enabled when the query contains only tables/views from one JDBC connection.
  + **Edit SQL**  
     Shows the SQL statement of the query.
  + **Preview**  
     Opens the [Preview Option](https://devnet.logianalytics.com/hc/en-us/articles/1500010067441-Preview-Option-Dialog) dialog to preview the records.
* **Help**  
   Displays the help document about this feature

**Toolbar**

The following are commands on the toolbar:

* **Add Tables**  
   Opens the [Add Tables/Views/Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500010064701-Add-Tables-Views-Queries-Dialog) dialog to add tables, views, synonyms, queries, imported SQLs, stored procedures, and user defined data sources in the current catalog data source to the query or business view. When a query, imported SQL, stored procedure or user defined data source is added, it will be added as a single table with all of its columns.
* **Delete Table**  
   Removes the selected resource.
* **New Computed Column**  
   Opens the [New Computed Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010031802-New-Computed-Column-Dialog) dialog to create functions used for a particular query. It helps you to quickly and easily create columns with the functions available instead of writing a formula. The option is enabled when the query contains only tables/views/synonyms from one JDBC connection.
* **Add Formula Fields**  
   Opens the [Add Formula Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010064661-Add-Formula-Fields-Dialog) dialog to add formulas to the query.
* **Delete Column**  
   Removes some unwanted columns from a table.
* **Arrange**  
   Organizes the resources added into the query or business view.
* **Preview**  
   Opens the Preview Option dialog to preview the records. The option is enabled when the query contains only tables/views from one JDBC connection.
* **Help**  
   Displays the help document about this feature.

**Criteria panel**

Lists all columns added to the query. You can specifically define criteria for the columns in this panel.

**SQL**

Shows the SQL statement of the query. The option is enabled when the query contains only tables/views/synonyms from one JDBC connection.

**Show Paths**

Shows information of the pre-join paths among tables in the query, when the pre-join feature is enabled.

**OK**

Accepts all changes and closes the window.

**Cancel**

Does not retain any changes and closes the window.

**Apply**

Accepts all changes in the window.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010032222-QR-Code-Expert-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010032242-Query-Modifier-Editor-Dialog)
