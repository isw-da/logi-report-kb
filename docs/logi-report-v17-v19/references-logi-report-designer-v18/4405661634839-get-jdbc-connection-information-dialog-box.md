---
title: "Get JDBC Connection Information Dialog Box"
id: 4405661634839
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661634839-Get-JDBC-Connection-Information-Dialog-Box
updated_at: 2022-11-07T03:46:24Z
---

# Get JDBC Connection Information Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664512151-Geographic-Map-Wizard-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661606807-Go-Down-Dialog-Box)

# Get JDBC Connection Information Dialog Box

You can use the Get JDBC Connection Information dialog box to create or edit a [JDBC](https://devnet.logianalytics.com/hc/en-us/articles/4405661427991-Setting-Up-JDBC-Connections-in-a-Catalog#Connection) or [Hive](https://devnet.logianalytics.com/hc/en-us/articles/4405661421335-Connecting-via-Hive-Connections) connection. This topic describes the options in the dialog box.

Designer displays the Get JDBC Connection Information dialog box when you do one of the following:

* Select JDBC or Hive and select OK in the [New Data Source dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661654807-New-Data-Source-Dialog-Box).
* In the Catalog Manager, right-click a data source and select New JDBC Connection or New Hive Connection from the shortcut menu, then select JDBC in the Select Connection Type dialog box.
* In the Catalog Manager, right-click a data source and select New Hive Connection from the shortcut menu.
* In the Catalog Manager, right-click an existing JDBC or Hive connection and select Edit Connection from the shortcut menu.
* Select OK in the [Create Connection dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661482135-Create-Connection-Dialog-Box).
* In the [Page Report Manager](https://devnet.logianalytics.com/hc/en-us/articles/4405664693399-Managing-Page-Reports), right-click the root folder Reports and select Export on the shortcut menu.
* In the [Publish to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661678103-Publish-to-Logi-Report-Server-Dialog-Box), select a catalog in the resource box, select More Options, then in the Connection tab, select a JDBC connection and select Modify.
* In the [Choose JDBC Connection dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4411769082647-Choose-JDBC-Connection-Dialog-Box), select <Add JDBC Connection...> from the connection drop-down list and select OK.

![Get JDBC Connection Information dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542114967/jdbccnnctn.gif)

You see the following options in the dialog box:

**Connection List**

This drop-down list contains the connection information that you previously added. The format of the connection information is:

JDBC URL/(JDBC Driver Name)

For example:

`jdbc:oracle:thin:@192.168.1.1:OracleDB(oracle.jdbc.driver.OracleDriver)`

Designer fills in the JDBC URL and driver name in the corresponding text boxes after you choose one of the connection items from the Connection List.

**Use ODBC Data Source**

Select to use an ODBC data source for the connection.

* **DSN Name**  
  Specify the name for the ODBC data source.

**Use Connection Pool**

Select to connect the database through a WebLogic connection pool.

**Driver**

Designer selects this option by default and disables it if you select Use ODBC Data Source or Use Connection Pool. Here you should type the JDBC driver class name such as oracle.jdbc.driver.OracleDriver which you want to use for this connection; otherwise, Designer tries all the JDBC drivers that you have added in the file jdbcdrivers.properties in `<install_root>\bin` for the JDBC URL you provide, when it tries to set up a database connection. That is to say, you can also add names of the JDBC drivers into that property file.

**URL**

Specify the valid JDBC URL which can establish a connection to the database.

**User**

Specify the user name for connecting to the database.

**Password**

Specify the password for connecting to the database.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) Designer disables all the preceding options when you use the dialog box for editing an existing connection in the Catalog Manager.

**Test Connection**

Designer displays this button when you use the dialog box for creating a connection. You can select it to test whether the specified connection information can connect to the database successfully.

**More Options**/**Less Options**

Select to show or hide the [options](#Options) for configuring the connection to meet the special requirements of the database.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## Options

Experienced users can configure the JDBC or Hive connection to meet the special requirements of the database in the following tabs:

* [Qualifier Tab](#Qualifier)
* [Date Format Tab](#DateFormat)
* [Transaction Tab](#Transaction)
* [Schema Tab](#Schema)
* [Other Tab](#Other)

### Qualifier Tab

Use this tab to specify the qualifier options for the connection.

![JDBC Connection Options - Qualifier](https://devnet.logianalytics.com/hc/article_attachments/4420556151703/jdbccnnctn_qulfr.gif)

**Name Pattern**

You can specify whether to use catalog or schema in data manipulation in this box.

* **Unqualified Name**  
  Select to include neither catalog nor schema in data manipulation. If you add a table or view from a different schema, you can create queries on it and use the queries to build reports, but when you run the reports, the table or view applies the default schema and you get an error that the table or view does not exist.

  Example: SELECT t.c FROM t
* **2-Part Names**  
  Select to use schema in data manipulation. If you want to use tables and views from more than one schema, you must use 2 part or 3 part names.

  Example: SELECT schema.t.c FROM schema.t
* **3-Part Names**  
  Select to use both catalog and schema in data manipulation.

  Example: SELECT catalog.schema.t.c from catalog.schema.t

This is very useful when you want to build reports that get data from more than one catalog and/or schema. If you only use an unqualified name, the SQL statement that Designer generates does not contain the catalog and schema name, and therefore Designer may not be able to find the table or view in the default schema and/or catalog.

**Quote Qualifier**

You can specify the characters, and then the qualifier name which contains the characters that you do not want to quote in this box. In Designer, you need quotes with the character defined by the DBMS. The default character is double quotation marks (" ").

* **Default (JDBC)**  
  Select to get the extra name characters from JDBC.
* **User Defined**  
  Select to modify the quote character according to the database system.
  + **Extra Characters**  
    Specify the extra characters for identifier names.
  + **Quote Character**  
    Specify the quote character.

**Modify Qualifier**

You can edit the current qualifier in this box.

* **Qualifier**  
  This drop-down list contains all the available qualifiers. You can change the current qualifier by selecting one from the drop-down list. The default value is the first one in the list. If the database dose not support qualifier, Designer does not display the drop-down list, and you cannot type the qualifier name.
* **Apply To**  
  Specify to which data resources to apply the modified qualifier.
  + **Tables**  
    Select to apply the modified qualifier to all tables in the connection.
  + **Views**  
    Select to apply the modified qualifier to all views in the connection.
  + **Imported SQLs**  
    Select to apply the modified qualifier to all imported SQLs in the connection
  + **Stored Procedures**  
    Select to apply the modified qualifier to all stored procedures in the connection.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) Designer does not record the changes that you make in the Modify Qualifier box, meaning, if you change any value in the box and apply it, when you open the dialog box the next time, Designer displays its original value.

**Restore Default**

Select to restore the values in the tab to their defaults.

**Apply**

Select to accept the changes.

### Date Format Tab

Different database systems use different Date and Time formats for Date and Time values. You can use the Date Format tab to specify the format, so that when Designer sends the SQL statement with Date or Time parameters, they can be correctly translated into the format of your database system. For example, in an Oracle database, the default Date format is "dd-MMM-yy"; while in a MySQL database system, it is "yyyy-MM-dd". Thus, you need to modify the Date format for the connection accordingly, so that the Designer generated SQL statements can function correctly with the database.

![JDBC Connection Options - Data Format](https://devnet.logianalytics.com/hc/article_attachments/4420550884631/jdbccnnctn_dtfmt.gif)

**Date Format**

Specify the default format for Date type data for the connection.

**Time Format**

Specify the default format for Time type data for the connection.

**Timestamp Format**

Specify the default format for Timestamp type data for the connection.

| Symbol | Meaning | Presentation |
| --- | --- | --- |
| y | year | Number |
| M | month | Number |
| d | day in month | Number |
| H | hour in day (0~23) | Number |
| h | hour in am/pm (1~12) | Number |
| m | minute in hour | Number |
| s | second in minute | Number |
| S | millisecond | Number |

The Date and Time formats Logi Report supports follows that of Java. For more information, refer to the java.text package DateFormat interface in the Java API Specification.

### Transaction Tab

Use this tab to specify the transaction options for the connection.

![JDBC Connection Options - Transaction](https://devnet.logianalytics.com/hc/article_attachments/4420550885271/jdbccnnctn_trsctn.gif)

**Read Only**

Select the mode to open the connection to the JDBC database. The initial setting is "Default" which uses the mode specified by the DBMS administrator which could be "Read Only" or "Read & Write".

* **Default**  
  Select to apply the default setting of the DBMS, which can be "Read & Write" or "Read Only".
* **Read Only**  
  Select to allow users to access the database in read-only mode. This allows the driver to optimize performance for reporting which does not need to write to the DBMS.
* **Read & Write**  
  Select to allow users to access the database in read-write mode. This opens the DBMS with updates enabled which requires more processing to ensure concurrency control.

**Transaction Mode**

Select the transaction mode for the connection.

* **Default**  
  Select to apply the setting from the database.
* **None**  
  Select to not use transactions in the connection.
* **Read Uncommitted**  
  Select to allow dirty reads, non-repeatable reads, and phantom reads to occur in the connection. This mode can speed up the transaction of the connection. If you select this mode, transactions are not isolated from each other. When the DBMS supports other transaction isolation levels, it ignores whatever mechanism is used to implement those levels, so that they do not adversely affect other transactions. Transactions running at the Read Uncommitted level are usually read-only.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) When you set the Read Only option and select the Transaction Isolation option of "Read Uncommitted", it provides faster access to the data; however, if a database transaction is rolled back, the read retrieves an invalid row and results in an inaccurate report.
* **Read Committed**  
  Select to prevent dirty reads, and allow non-repeatable reads and phantom reads to occur in the connection. If you select this mode, when one transaction is reading, updating, or deleting a row, other transactions cannot update or delete it until this transaction has been committed or rolled back.
* **Repeatable Read**  
  Select to prevent dirty reads and non-repeatable reads, and allow phantom reads to occur in the connection. If you select this mode, when one transaction is updating, deleting several rows, or inserting new rows into them, other transactions cannot also update or delete these rows, until this transaction has been committed or rolled back.
* **Serializable**  
  Select to prevent dirty reads, non-repeatable reads, and phantom reads in the connection. If you select this mode, when one transaction is updating, deleting several rows, or inserting new rows into them, other transactions cannot update, delete these rows, or insert any new rows into these rows, until this transaction has been committed or rolled back.

### Schema Tab

Use this tab to specify the schema options for the connection.

![JDBC Connection Options - Schema](https://devnet.logianalytics.com/hc/article_attachments/4420542115479/jdbccnnctn_schema.gif)

**Schema**

You can choose the required schemas and show them in the Add Tables/Views/Synonyms dialog box in this box.

* **Schema List**  
  This box lists the schemas for you to choose.
* **Included Schemas**  
  This box shows the schemas that you select.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550823447/btn_addarrow.gif)**Add button**  
  Select to add the specified schemas to the Included Schemas box.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420550824215/btn_rmvarrow.gif)**Remove button**  
  Select to remove the specified schemas from the Included Schemas box.
* **Load All Schemas**  
  Select to show all the schemas in database.

**Modify Schema**

You can modify the current schema in this box.

* **Schema List**  
  This drop-down list contains all the available schemas. You can change the current schema by selecting one from the drop-down list.
* **Apply To**  
  Specify to which data resources to apply the modified schema.
  + **Tables**  
    Select to apply the specified schema to all tables in the connection.
  + **Views**  
    Select to apply the specified schema to all views in the connection.
  + **Stored Procedures**  
    Select to apply the specified schema to all stored procedures in the connection.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) Designer does not record the changes that you make in the Modify Schema box, meaning, if you change any value in the box and apply it, when you open the dialog box the next time, Designer displays its original value.

**Restore Default**

Select to restore the values in the tab to their defaults.

**Apply**

Select to accept the changes.

### Other Tab

When you use parameters to build queries, there may be special characters in the parameter values like a back slash (\), and you would like Designer to interpret them literally, rather than as a special character. In this case, you can replace the special characters with another string according to your database, for example, for an MySQL database, use "\\" to represent "\". You can specify these settings in the Other tab.

![JDBC Connection Options - Other](https://devnet.logianalytics.com/hc/article_attachments/4420550885527/jdbccnnctn_other.gif)

**Characters to Be Replaced**

Specify the characters that need to be replaced in parameter values when Designer passes the parameter values to queries.

**Replaced By**

Specify the characters to replace with.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664512151-Geographic-Map-Wizard-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661606807-Go-Down-Dialog-Box)
