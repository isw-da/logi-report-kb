---
title: "Connect to PostgreSQL Dialog Box"
id: 4405664437783
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664437783-Connect-to-PostgreSQL-Dialog-Box
updated_at: 2022-01-27T20:38:07Z
---

# Connect to PostgreSQL Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661474071-Connect-to-Oracle-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661475607-Connect-to-SQL-Server-Dialog-Box)

# Connect to PostgreSQL Dialog Box

You can use the Connect to PostgreSQL dialog box to specify the information for connecting to a PostgreSQL database [via the connection plug-in](https://devnet.logianalytics.com/hc/en-us/articles/4405664415895-Creating-JDBC-Connections-via-Plug-ins). This topic describes the options in the dialog box.

Designer displays the Connect to PostgreSQL dialog box when you do one of the following:

* Select OK in the [Create Connection to PostgreSQL dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661482135-Create-Connection-Dialog-Box).
* Select PostgreSQL and select OK in the [New Data Source dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661654807-New-Data-Source-Dialog-Box).
* In the Catalog Manager, right-click a data source and select New JDBC Connection from the shortcut menu, then select PostgreSQL in the Select Connection Type dialog box and select OK.

![Connect to PostgreSQL dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420402524695/cnnct2pstgrsql.gif)

You see the following options in the dialog box:

**Driver**

This option shows the PostgreSQL JDBC driver name that this connection uses.

**Server**

Specify the host name or IP address of the database server.

**Port**

Specify the port of the database server.

**Database**

Specify the name of the database that you want Designer to connect with by default.

**User**

Specify the user ID used for accessing the database.

**Password**

Specify the password used for accessing the database.

**Show URL**

Select to show the URL used for connecting to the database server.

* **URL**  
  This option shows the URL which is formulated by the information you provide. You can also type the valid JDBC URL in the text box to establish the connection to the database server. The URL format is regulated by the driver itself.

**Test Connection**

Select to test whether the specified connection information can connect to the database successfully.

**More Options**/**Less Options**

Select to show or hide the [options](https://devnet.logianalytics.com/hc/en-us/articles/4405661634839-Get-JDBC-Connection-Information-Dialog-Box#Options) for experienced users to configure the connection to meet the special requirements of the database.

**OK**

Select to create the connection to the PostgreSQL database and close the dialog box.

**Cancel**

Select to quit creating the connection and close the dialog box.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661474071-Connect-to-Oracle-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661475607-Connect-to-SQL-Server-Dialog-Box)
