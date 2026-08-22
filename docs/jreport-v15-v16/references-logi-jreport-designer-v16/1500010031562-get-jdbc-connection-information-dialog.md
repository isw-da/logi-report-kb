---
title: "Get JDBC Connection Information Dialog"
id: 1500010031562
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010031562-Get-JDBC-Connection-Information-Dialog
updated_at: 2021-07-24T10:38:38Z
---

# Get JDBC Connection Information Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066741-Geographic-Map-Wizard-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010066761-Go-Down-Dialog)

# Get JDBC Connection Information Dialog

The Get JDBC Connection Information dialog is used to get or create [JDBC](https://devnet.logianalytics.com/hc/en-us/articles/1500010064401-Setting-Up-JDBC-Connections-in-a-Catalog#Connection) or [Hive](https://devnet.logianalytics.com/hc/en-us/articles/1500010064281-Hive-Connections) connection information. It lists the database objects which are accessible through JDBC or JDBC-ODBC Bridge.

The dialog appears when you do one of the following:

* Select JDBC or Hive and select OK in the [New Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500010031882-New-Data-Source-Dialog) dialog.
* In the Catalog Manager, right-click a data source and select New JDBC Connection or New Hive Connection from the shortcut menu, then select JDBC in the Select Connection Type dialog.
* In the Catalog Manager, right-click a data source and select New Hive Connection from the shortcut menu.
* In the Catalog Manager, right-click an existing JDBC or Hive connection and select Edit Connection from the shortcut menu.
* Select OK in the [Create Connection to JDBC/Hive](https://devnet.logianalytics.com/hc/en-us/articles/1500010030082-Create-Connection-Dialog) dialog.
* In the [Manage Page Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010070881-Managing-Page-Reports) dialog, right-click the root folder Reports and select Export on the shortcut menu.

![Get JDBC Connection Information dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909176471/jdbccnnctn.gif)

The following are details about options in the dialog:

**Connection List**

Contains the previously added connection information. The format of the connection information is:

JDBC URL/(JDBC Driver Name)

For example:

`jdbc:oracle:thin:@192.168.1.1:OracleDB(oracle.jdbc.driver.OracleDriver)`

Choosing one of the connection information items from the Connection List will fill in the JDBC URL and driver name in the corresponding text boxes.

**Use ODBC Data Source**

Indicates that an ODBC Data Source will be used.

* **DSN Name**  
   Specifies the name for the ODBC data source.

**Use Connection Pool**

Specifies to connect the database through a WebLogic connection pool. It is disabled when Use ODBC Data Source is checked.

**Driver**

By default, this checkbox is checked. It is disabled when Use ODBC Data Source or Use Connection Pool is checked. Here you should input the JDBC driver class name that this connection will use. Otherwise, Logi JReport will try all JDBC drivers specified in the file jdbcdrivers.properties in `<install_root>\bin` for the JDBC URL given by you when it tries to setup a database connection. That is to say, JDBC driver's names also can be added into that property file.

**URL**

Specifies the valid JDBC URL which can establish a connection to the database that is to be used. The valid format of the URL should be provided by your JDBC Driver.

**User**

Specifies the user ID used for accessing the database through the JDBC data source.

**Password**

Specifies the password used for accessing the database through the JDBC data source.

**Test Connection**

Tests whether the provided information is available for JDBC Connection.

**OK**

Accepts all changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

## More Options/Less Options

Shows or hides the options for experienced users and special requirements of your database.

**Qualifier tab**

* **Name Pattern**  
   Specifies whether or not catalog or schema is used in data manipulation.
  + **Unqualified Name**  
     Neither catalog nor schema will be included in data manipulation. Example: SELECT t.c FROM t. If you add a table or view from a different schema you can create queries on it but when you run a report it will use the default schema and you will get an error that the table or view does not exist.
  + **2-Part Names**  
     Uses schema in data manipulation. Example: SELECT schema.t.c FROM schema.t. If you want to use tables and views from more than one schema you must use 2 part or 3 part names.
  + **3-Part Names**  
     Uses both catalog and schema in data manipulation. Example: SELECT catalog.schema.t.c from catalog.schema.t

  This is very useful when you want to build reports that get data from more than one catalog and/or schema. If you only use an unqualified name, the SQL statement generated by Logi JReport will not contain the catalog and schema name, and therefore the table or view may not be found in the default schema and/or catalog.
* **Quote Qualifier**  
   Specifies the characters, and then the qualifier name which contains the characters that will not be quoted.

  In Logi JReport, you need quotes with the character defined by the DBMS. The default character is double quotation marks (" "). Two properties exist for the Quote Qualifier.

  + **Default (JDBC)**  
     If selected, the program will get the extra name characters from JDBC.
  + **User Defined**  
     If selected, you can modify the quote character according to the database system being used.
    - **Extra Characters**  
       Specifies the extra characters for identifier names.
    - **Quote Character**  
       Specifies the quote character.
* **Modify Qualifier**  
   Edits the current qualifier.
  + **Qualifier**  
     Lists all the qualifiers available. You can change the current qualifier by selecting one from the drop-down list. The default value is the first one in the list. If the database do not support qualifier, there will be no drop-down list, and you cannot input the qualifier name.
  + **Apply To**
    - **Tables**  
       If checked, the modified qualifier will be applied to all tables in the connection.
    - **Views**  
       If checked, the modified qualifier will be applied to all views in the connection.
    - **Imported SQLs**  
       If checked, the modified qualifier will be applied to all imported SQLs in the connection
    - **Stored Procedures**   
       If checked, the modified qualifier will be applied to all stored procedures in the connection.

  **Note:** All the changes you made in the Modify Qualifier box will not be recorded in the Get JDBC Connection Information dialog. That is to say, if you change any value in the box and apply it, when you open the dialog next time, it will keep to the original.
* **Restore Default**  
   Restores values in the tab to defaults.
* **Apply**  
   Accept the changes.

**Date Format tab**

Different database systems use different Date and Time formats for Date and Time values. The Date Format tab is for specifying the format, so that when Logi JReport sends the SQL statement with Date or Time parameters, they can be correctly translated into the format of your database system.

For example, in an Oracle database, by default, the Date format is 'dd-MMM-yy'. However, in a MySQL database system, the Date format is 'yyyy-MM-dd'. Thus, the Date format in the connection object is required to be modified accordingly, in order for the Logi JReport generated SQL statements to function correctly with the database.

* **Date Format**  
   Specifies the date format.
* **Time Format**  
   Specifies the time format.
* **Timestamp Format**   
   Specifies the timestamp format.

  | Symbol | Meaning | Presentation |
  | --- | --- | --- |
  | y | year | number |
  | M | month in year | number |
  | d | day in month | number |
  | h | hour in day (0~23) | number |
  | m | minute in hour | number |
  | s | second in minute | number |
  | S | millisecond | number |

**Transaction tab**

* **Read Only**
  + **Default**  
     Accepts the settings from the database that you are connecting to.
  + **Read Only**  
     Users will only be able to access the database in read-only mode.
  + **Read & Write**  
     Users will be able to access the database in read-write mode.
* **Transaction Mode**
  + **Default**   
    Accepts the settings from the database that you are connecting to.
  + **None**  
     Transactions are not supported.
  + **Read Uncommitted**  
     Transactions are not isolated from each other. If the DBMS supports other transaction isolation levels, it ignores whatever mechanism it uses to implement those levels. So that they do not adversely affect other transactions, transactions running at the Read Uncommitted level are usually read-only.

    **Note:** When Read Only is set and Transaction Isolation to be Read Uncommitted, it provides faster access to the data but if a database transaction is rolled back the read will retrieve an invalid row and result in an inaccurate report.
  + **Read Committed**  
     When one transaction is reading, updating or deleting a row, other transactions cannot update or delete it until this transaction has been committed or rolled back.
  + **Repeatable Read**  
     When one transaction is updating, deleting several rows or inserting new rows into them, the other transactions cannot also update or delete these rows, until this transaction has been committed or rolled back.
  + **Serializable**  
     When one transaction is updating, deleting several rows or inserting new rows into them, the other transactions cannot update, delete these rows, or insert any new rows into these rows, until this transaction has been committed or rolled back.

**Schema tab**

* **Schema**  
   Enables you to choose the schemas you want and makes Logi JReport show the chosen schemas in the Add Tables/Views/Synonyms dialog.
  + **Schema List**   
     Lists the schemas for you to choose.
  + **Included Schemas**  
     Shows the selected schemas.
  + **Load All Schemas**  
     Enables Logi JReport Designer to show all the schemas in database.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif)  
     Adds the selected schemas to the Included Schemas box.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)  
     Removes the selected schemas from the Included Schemas box.
* **Modify Schema**   
   Edits the current schema.
  + **Schema List**  
     Lists all the schemas available.
  + **Apply To**
    - **Tables**  
       If checked, the selected schema will be applied to all tables in the connection.
    - **Views**  
       If checked, the selected schema will be applied to all views in the connection.
    - **Stored Procedures**  
       If checked, the selected schema will be applied to all stored procedures in the connection.

  **Note:** All the changes you made in the Modify Schema box will not be recorded in the Get JDBC Connection Information dialog. That is to say, if you change any value in the box and apply it, when you open the dialog next time, it will keep to the original.
* **Restore Default**  
   Restores values in the tab to defaults.
* **Apply**  
   Accepts the changes.

**Other tab**

When parameters are used to build queries, there may be special characters in the parameter values like a back slash (\), and you would like them to be interpreted literally, rather than as a special character. Then you can replace the special characters with another string according to your database. For example, for MySQL database, use \\ to represent \.

* **Characters to Be Replaced**  
   Specifies the characters that need to be replaced in parameter values when the parameter values are passed onto queries.
* **Replaced By**  
   Specifies the characters to replace with.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066741-Geographic-Map-Wizard-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010066761-Go-Down-Dialog)
