---
title: "Connect to Oracle Dialog"
id: 1500009630121
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009630121-Connect-to-Oracle-Dialog
updated_at: 2021-07-24T16:04:56Z
---

# Connect to Oracle Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009630101-Connect-to-MySQL-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607462-Connect-to-PostgreSQL-Dialog)

# Connect to Oracle Dialog

The Connect to Oracle dialog helps you to specify the information for connecting to an Oracle database [via the connection plug-in](https://devnet.logianalytics.com/hc/en-us/articles/1500009606862-JDBC-Connection-Plug-ins). It appears when you do one of the following:

* Select OK in the [Create Connection to Oracle](https://devnet.logianalytics.com/hc/en-us/articles/1500009630221-Create-Connection-Dialog) dialog.
* Select Oracle and select OK in the [New Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009609222-New-Data-Source-Dialog) dialog.
* In the Catalog Manager, right-click a data source and select New JDBC Connection from the shortcut menu, then select Oracle in the Select Connection Type dialog and select OK.

![Connect to Oracle dialog](https://devnet.logianalytics.com/hc/article_attachments/4404916815511/cnnct2orcl.gif)

**Driver**

Displays the Oracle JDBC driver name that this connection uses.

**Connection Type**

Specifies the way using which to connect to the Oracle database: Service Name, SID, or TNS.

**Server**

Specifies the host name or IP address of the database server.

**Port**

Specifies the port of the database server.

**Service Name/SID/TNS**

Specifies the service name/SID/TNS of the database instance that you want Logi Report Designer to connect with by default.

**User**

Specifies the user ID used for accessing the database.

**Password**

Specifies the password used for accessing the database.

**Show URL**

Specifies to show the URL used for connecting to the database server.

* **URL**  
  Displays the URL which is formulated by the information you have provided. You can also type the valid JDBC URL in the text box to establish the connection to the database server. The URL format is regulated by the driver itself. When Service Name is selected as the connection type, the format is `jdbc:oracle:thin:@//<host>:<port>/<service_name>`; when SID is selected, the format is `jdbc:oracle:thin:@<host>:<port>:<SID>`; for TNS, the format is `jdbc:oracle:thin:@<TNS>`.

**Test Connection**

Tests whether the specified connection information can connect to the database successfully.

**More Options/Less Options**

Shows or hides the options for experienced users to configure the connection to meet the special requirements of the database. [Go here](https://devnet.logianalytics.com/hc/en-us/articles/1500009608882-Get-JDBC-Connection-Information-Dialog#Options) for details about the options.

**OK**

Creates the connection to the Oracle database and closes the dialog.

**Cancel**

Cancels the connection creation and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009630101-Connect-to-MySQL-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607462-Connect-to-PostgreSQL-Dialog)
