---
title: "Edit Dynamic Connection Dialog Box Properties"
id: 1500009745922
section: "Logi Report Server Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009745922-Edit-Dynamic-Connection-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:49Z
---

# Edit Dynamic Connection Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746262-Dashboard-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745942-Edit-Dynamic-Display-Name-Dialog-Box-Properties)

# Edit Dynamic Connection Dialog Box Properties

This topic describes how you can use the Edit Dynamic Condition dialog box to edit the selected [dynamic connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009743582-Creating-and-Using-Dynamic-Connections).

Server displays the dialog box when an admin user selects a connection name in the Connection Name column of the Administration > Connection > Dynamic Connections page in the Server Console.

![Edit Dynamic Connection dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885513879/edtdyncnct.gif)

**Catalog**

Displays the catalog of the dynamic connection. It is read only.

**Data Source Name**

Displays the data source of the dynamic connection. It is read only.

**Connection Name**

Specifies a connection to connect to the data source from the drop-down list. It is read only.

**Properties**

Displays the properties of the database connection. You can select it to expand or collapse the property table.

Here you can change some properties of the database connection. The table shows the values of the original connection properties initially.

* **Check box**  
   After you select a property, you will be able to change the property value. Select the check box on the column header and the check boxes for all the properties will be selected. Initially all the properties are unselected and uneditable. Whenever a property is unselected, it always shows the original value regardless of whether you have changed the value or not.
* **Name**  
   Displays the property names.
* **Value**  
   Specifies the property values.

There are the following properties:

* **Date Format**  
   Specifies the default Date format corresponding to the database.
* **Description**  
   Specifies the description of the connection.
* **Driver**  
   Specifies the class name of the JDBC driver such as oracle.jdbc.driver.OracleDriver.
* **Is JNDI Data Source**  
   Specifies whether it is a JNDI data source.
* **JNDI Data Source Name**  
   Specifies the JNDI data source name when the Is JNDI Data Source property is true.
* **Name**  
   Specifies the name of the connection.
* **Name Pattern**  
   Specifies whether catalog or schema is used in data manipulation. Choose an option from the drop-down list.
  + **Unqualified** - Neither catalog nor schema is included in data manipulation. Example: SELECT t.c FROM t
  + **Qualified\_2part**  - Uses schema in data manipulation. Example: SELECT schema.t.c FROM schema.t
  + **Qualified\_3part**- Uses both catalog and schema in data manipulation. Example: SELECT catalog.schema.t.c from catalog.schema.t
* **Read Only**  
   Specifies the mode to open the connection to the JDBC data source. The initial setting is Default which uses the mode specified by the DBMS Administrator which could be read only or read & write. Choose an option from the drop-down list.
  + **Default** - May be read & write or read only depending on the DBMS default setting.
  + **Read only** - Allows the driver to optimize performance for reporting which does not need to write to the DBMS.
  + **Read & write** - Opens the DBMS with updates enabled which requires more processing to ensure concurrency control.
* **Time Format**  
   Specifies the default time format corresponding to the database.
* **Timestamp Format**  
   Specifies the default timestamp format corresponding to the database.
* **Transaction Mode**  
   Specifies the transaction mode for the connection. Choose an option from the drop-down list.
  + **Default** - Indicates the transaction information cannot be got from JDBC connection.
  + **None** - Indicates that transactions are not supported.
  + **Read\_uncommitted** - Dirty reads, non-repeatable reads and phantom reads can occur. This mode will speed up the transaction of the catalog.
  + **Read\_committed** - Dirty reads are prevented; non-repeatable reads and phantom reads can occur.
  + **Repeatable\_read** - Dirty reads and non-repeatable reads are prevented; phantom reads can occur.
  + **Serializable** - Dirty reads, non-repeatable reads and phantom reads are prevented.
* **URL**  
   Specifies the JDBC URL which establishes the connection to the database, for example, jdbc:oracle:thin:@localhost:1521:ORCL.
* **User Defined Extra Characters**  
   Specifies extra characters of user defined quote qualifier.
* **User Defined Quote Characters**  
   Specifies the quote character of user defined quote qualifier.
* **Default Database User**  
   Specifies the user name for connecting to the database, which is determined by the database DBA. Null means using the default database user name.
* **Default Database Password**  
   Specifies the password for connecting with the database, which is determined by the database DBA. Null means using the default database password.

**Add Database User Mapping**

Adds a new database user mapping. Select to create a new line at the end of the table.

**Delete**

Deletes the selected database user mappings.

**Database user mapping table**

Check boxes are used to specify whether to select the database user mapping. Select the check box on the column header to select all database user mappings. After you select the database user mappings, you can then delete them if you do not want them.

* **SID**  
   Specifies the security identifier (SID). A SID can be a group, role or user in the Logi Report Server security system. You can select a value from the drop-down list or type the value in the text box. The **x** in the text box is used to clear the input text. You can define at most one database user mapping for an SID within a dynamic connection.
* **Organization Name**  
   Double-click in the text box and then select an organization from the drop-down list. You can first specify the organization and then the SID. The column is available to system admin when the [Organization](https://devnet.logianalytics.com/hc/en-us/articles/1500009749922-Multitenancy-Supported-via-Organizations) feature is enabled.
* **Database User**  
   Specifies the database user name. Null means using the default database user name.
* **Database Password**  
   Specifies the database password. Passwords are masked.
* **Control**
  + **Test Connection**  
     Tests whether the connection configuration works using the database user name and password.

**OK**

Creates the dynamic connection and exits the dialog box.

**Cancel**

Cancels the creation of a dynamic connection and closes the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746262-Dashboard-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745942-Edit-Dynamic-Display-Name-Dialog-Box-Properties)
