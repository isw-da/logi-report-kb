---
title: "Connect to MySQL Dialog"
id: 1500009564762
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564762-Connect-to-MySQL-Dialog
updated_at: 2021-07-24T05:55:34Z
---

# Connect to MySQL Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585921-Connect-to-JReport-Server-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564782-Connect-to-Oracle-Dialog)

# Connect to MySQL Dialog

The Connect to MySQL dialog appears when you do one of the following:

* Select OK in the [Create Connection to MySQL](https://devnet.logianalytics.com/hc/en-us/articles/1500009586001-Create-Connection-Dialog) dialog.
* Select MySQL and select OK in the [New Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009587961-New-Data-Source-Dialog) dialog.
* In the Catalog Manager, right-click a data source and select New JDBC Connection or New HIVE Connection from the shortcut menu, then select MySQL in the Select Connection Type dialog and select OK.

The dialog helps you to specify the connection information and create a connection to MySQL.  [See the dialog](javascript:%20void(null)).

![Connect to MySQL dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893948439/cnnct2mysql.gif)

**Driver**

Specifies the MySQL JDBC driver name that this connection will use.

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

* **Driver**Specifies the MySQL JDBC driver name that this connection will use.
* **URL**  
   Specifies the valid JDBC URL which can establish a connection to the database. The valid format of the URL should be provided by your JDBC Driver.
* **User**Specifies the user ID used for accessing the database.
* **Password**Specifies the password used for accessing the database.

**Test Connection**

Tests whether the specified connection information can connect to the database successfully.

**More Options**

These options are designed for experienced users, and when your database has some special requirements. Select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009587701-Get-JDBC-Connection-Information-Dialog#Options) to see the details.

**OK**

Creates the connection to MySQL and closes the dialog.

**Cancel**

Cancels the connection creation and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585921-Connect-to-JReport-Server-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564782-Connect-to-Oracle-Dialog)
