---
title: "Connect to InterSystems IRIS Dialog Box"
id: 5735528584343
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735528584343-Connect-to-InterSystems-IRIS-Dialog-Box
updated_at: 2022-11-02T08:16:27Z
---

# Connect to InterSystems IRIS Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735565201943-Connect-to-MySQL-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735508318999-Connect-to-PostgreSQL-Dialog-Box)

# Connect to InterSystems IRIS Dialog Box

You can use the Connect to InterSystems IRIS dialog box to specify the information for connecting to an InterSystems IRIS database [via the connection plug-in](https://devnet.logianalytics.com/hc/en-us/articles/5735512833815-Creating-JDBC-Connections-via-Plug-ins). This topic describes the options in the dialog box.

Designer displays the Connect to InterSystems IRIS dialog box when you do one of the following:

* Select OK in the [Create Connection to InterSystems IRIS dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735528726551-Create-Connection-Dialog-Box).
* Select InterSystems IRIS and select OK in the [New Data Source dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735530467735-New-Data-Source-Dialog-Box).
* In the Catalog Manager, right-click a data source and select New JDBC Connection from the shortcut menu, then select InterSystems IRIS in the Select Connection Type dialog box and select OK.

![Connect to InterSystems IRIS dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898532976663/cnnct2iris.gif)

Designer displays these options:

**Driver**

This option shows the InterSystems IRIS JDBC driver name that this connection uses.

**Server**

Specify the host name or IP address of the database server.

**Port**

Specify the port of the database server.

**Namespace**

Specify the namespace that you want Designer to connect with by default.

**User**

Specify the user ID used for accessing the database.

**Password**

Specify the password used for accessing the database.

**Show URL**

Select it to show the URL used for connecting to the database server.

* **URL**  
  This option shows the URL which is formulated by the information you provide. You can also type the valid JDBC URL in the text box to establish the connection to the database server. The URL format is regulated by the driver itself.

**Test Connection**

Select to test whether the specified connection information can connect to the database successfully.

**More Options**/**Less Options**

Select to show or hide the [options](https://devnet.logianalytics.com/hc/en-us/articles/5735530237847-Get-JDBC-Connection-Information-Dialog-Box#Options) for experienced users to configure the connection to meet the special requirements of the database.

**OK**

Select to create the connection to the InterSystems IRIS database and close the dialog box.

**Cancel**

Select to quit creating the connection and close the dialog box.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735565201943-Connect-to-MySQL-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735508318999-Connect-to-PostgreSQL-Dialog-Box)
