---
title: "Connect to MySQL Dialog"
id: 1500009630101
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009630101-Connect-to-MySQL-Dialog
updated_at: 2021-07-24T16:04:56Z
---

# Connect to MySQL Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607442-Connect-to-Logi-Report-Server-Dialog)

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607442-Connect-to-Logi-Report-Server-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630121-Connect-to-Oracle-Dialog)

# Connect to MySQL Dialog

The Connect to MySQL dialog helps you to specify the information for connecting to a MySQL database [via the connection plug-in](https://devnet.logianalytics.com/hc/en-us/articles/1500009606862-JDBC-Connection-Plug-ins). It appears when you select OK in the [Add Driver](https://devnet.logianalytics.com/hc/en-us/articles/1500009607102-Add-Driver-Dialog) dialog, or when you do one of the following in the case that the MySQL driver has been added in Logi Report Designer using the Add Driver dialog:

* Select OK in the [Create Connection to MySQL](https://devnet.logianalytics.com/hc/en-us/articles/1500009630221-Create-Connection-Dialog) dialog.
* Select MySQL and select OK in the [New Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009609222-New-Data-Source-Dialog) dialog.
* In the Catalog Manager, right-click a data source and select New JDBC Connection from the shortcut menu, then select MySQL in the Select Connection Type dialog and select OK.

![Connect to MySQL dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904385815/cnnct2mysql.gif)

**Driver**

Displays the MySQL JDBC driver name that this connection uses.

**Server**

Specifies the host name or IP address of the database server.

**Port**

Specifies the port of the database server.

**Database**

Specifies the name of the database or schema that you want Logi Report Designer to connect with by default.

**User**

Specifies the user ID used for accessing the database.

**Password**

Specifies the password used for accessing the database.

**Show URL**

Specifies to show the URL used for connecting to the database server.

* **URL**  
  Displays the URL which is formulated by the information you have provided. You can also type the valid JDBC URL in the text box to establish the connection to the database server. The URL format is regulated by the driver itself.

**Test Connection**

Tests whether the specified connection information can connect to the database successfully.

**More Options/Less Options**

Shows or hides the options for experienced users to configure the connection to meet the special requirements of the database. [Go here](https://devnet.logianalytics.com/hc/en-us/articles/1500009608882-Get-JDBC-Connection-Information-Dialog#Options) for details about the options.

**OK**

Creates the connection to the MySQL database and closes the dialog.

**Cancel**

Cancels the connection creation and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607442-Connect-to-Logi-Report-Server-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630121-Connect-to-Oracle-Dialog)
