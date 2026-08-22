---
title: "Connect to SQL Server Dialog"
id: 1500010065061
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010065061-Connect-to-SQL-Server-Dialog
updated_at: 2021-07-24T10:39:06Z
---

# Connect to SQL Server Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065041-Connect-to-PostgreSQL-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010065101-Create-Banded-Object-Dialog)

# Connect to SQL Server Dialog

The Connect to SQL Server dialog helps you to specify the information for connecting to an SQL Server database [via the connection plugin](https://devnet.logianalytics.com/hc/en-us/articles/1500010029442-JDBC-Connection-Plugins). It appears when you do one of the following:

* Select OK in the [Create Connection to SQL Server](https://devnet.logianalytics.com/hc/en-us/articles/1500010030082-Create-Connection-Dialog) dialog.
* Select SQL Server and select OK in the [New Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500010031882-New-Data-Source-Dialog) dialog.
* In the Catalog Manager, right-click a data source and select New JDBC Connection from the shortcut menu, then select SQL Server in the Select Connection Type dialog and select OK.

![Connect to SQL Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909240087/cnnct2sqlsvr.gif)

**Driver**

Displays the SQL Server JDBC driver name that this connection uses.

**Server**

Specifies the host name or IP address of the database server.

**Port**

Specifies the port of the database server.

**Database**

Specifies the name of the database or schema.

**User**

Specifies the user ID used for accessing the database.

**Password**

Specifies the password used for accessing the database.

**Show URL**

Specifies to configure the connection information using URL.

* **Driver**  
   Specifies the SQL Server JDBC driver name that this connection will use.
* **URL**  
   Specifies the valid JDBC URL which can establish a connection to the database. The valid format of the URL should be provided by your JDBC Driver.
* **User**  
   Specifies the user ID used for accessing the database.
* **Password**  
   Specifies the password used for accessing the database.

**Test Connection**

Tests whether the specified connection information can connect to the database successfully.

**More Options**

These options are designed for experienced users, and when your database has some special requirements. [Select here](https://devnet.logianalytics.com/hc/en-us/articles/1500010031562-Get-JDBC-Connection-Information-Dialog#Options) for details about the options.

**OK**

Creates the connection to SQL Server and closes the dialog.

**Cancel**

Cancels the connection creation and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065041-Connect-to-PostgreSQL-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010065101-Create-Banded-Object-Dialog)
