---
title: "Connect to Oracle Dialog"
id: 1500009564782
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564782-Connect-to-Oracle-Dialog
updated_at: 2021-07-24T05:55:34Z
---

# Connect to Oracle Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564762-Connect-to-MySQL-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564802-Connect-to-SQL-Server-Dialog)

# Connect to Oracle Dialog

The Connect to Oracle dialog appears when you do one of the following:

* Select OK in the [Create Connection to Oracle](https://devnet.logianalytics.com/hc/en-us/articles/1500009586001-Create-Connection-Dialog) dialog.
* Select Oracle and select OK in the [New Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009587961-New-Data-Source-Dialog) dialog.
* In the Catalog Manager, right-click a data source and select New JDBC Connection or New HIVE Connection from the shortcut menu, then select Oracle in the Select Connection Type dialog and select OK.

The dialog helps you to specify the connection information and create a connection to Oracle.  [See the dialog](javascript:%20void(null)).

![Connect to Oracle dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893948183/cnnct2orcl.gif)

**Driver**

Specifies the Oracle JDBC driver name that this connection will use.

**Connection Type**

Specifies a way for JDBC thin driver to connect to Oracle:

* **ServiceName**  
   The format is `jdbc:oracle:thin:@//<host>:<port>/<service_name>`. It is recommended.
* **SID**  
   The format is `jdbc:oracle:thin:@<host>:<port>:<SID>`.
* **TNSName**  
   The format is `jdbc:oracle:thin:@<TNSName>`.

**Server**

Specifies the host name or IP address of the database server.

**Port**

Specifies the port of the database server.

**Service Name**/**TNS Name**

Specifies the service name or TNS name of the database instance.

**User**

Specifies the user ID used for accessing the database.

**Password**

Specifies the password used for accessing the database.

**Show URL**

Specifies to configure the connection information using URL.

* **Driver**Specifies the Oracle JDBC driver name that this connection will use.
* **URL**  
   Specifies the valid JDBC URL which can establish a connection to the database. The valid format of the URL should be provided by your JDBC Driver.
* **User**Specifies the user ID used for accessing the database.
* **Password**Specifies the password used for accessing the database.

**Test Connection**

Tests whether the specified connection information can connect to the database successfully.

**More Options**

These options are designed for experienced users, and when your database has some special requirements. Select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009587701-Get-JDBC-Connection-Information-Dialog#Options) to see the details.

**OK**

Creates the connection to Oracle and closes the dialog.

**Cancel**

Cancels the connection creation and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564762-Connect-to-MySQL-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564802-Connect-to-SQL-Server-Dialog)
