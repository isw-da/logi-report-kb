---
title: "Connect to MySQL Dialog Box"
id: 1500010095761
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010095761-Connect-to-MySQL-Dialog-Box
updated_at: 2021-07-23T19:15:07Z
---

# Connect to MySQL Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095741-Connect-to-Logi-Report-Server-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095781-Connect-to-Oracle-Dialog-Box)

# Connect to MySQL Dialog Box

You can use the Connect to MySQL dialog box to specify the information for connecting to a MySQL database [via the connection plug-in](https://devnet.logianalytics.com/hc/en-us/articles/1500010095221-Creating-JDBC-Connections-via-Plug-ins). This topic describes the options in the dialog box.

Designer displays the Connect to MySQL dialog box when you select OK in the [Add Driver dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095421-Add-Driver-Dialog-Box), or when you do one of the following in the case that you have already added the MySQL driver in Designer using the Add Driver dialog box:

* Select OK in the [Create Connection to MySQL dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095881-Create-Connection-Dialog-Box).
* Select MySQL and select OK in the [New Data Source dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059982-New-Data-Source-Dialog-Box).
* In the Catalog Manager, right-click a data source and select New JDBC Connection from the shortcut menu, then select MySQL in the Select Connection Type dialog box and select OK.

![Connect to MySQL dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848622743/cnnct2mysql.gif)

You see the following options in the dialog box:

**Driver**

The option shows the MySQL JDBC driver name that this connection uses.

**Server**

Specify the host name or IP address of the database server.

**Port**

Specify the port of the database server.

**Database**

Specify the name of the database or schema that you want Designer to connect with by default.

**User**

Specify the user ID used for accessing the database.

**Password**

Specify the password used for accessing the database.

**Show URL**

Select to show the URL used for connecting to the database server.

* **URL**  
  The option shows the URL which is formulated by the information you provide. You can also type the valid JDBC URL in the text box to establish the connection to the database server. The URL format is regulated by the driver itself.

**Test Connection**

Select to test whether the specified connection information can connect to the database successfully.

**More Options**/**Less Options**

Select to show or hide the [options](https://devnet.logianalytics.com/hc/en-us/articles/1500010097761-Get-JDBC-Connection-Information-Dialog-Box#Options) for experienced users to configure the connection to meet the special requirements of the database.

**OK**

Select to create the connection to the MySQL database and close the dialog box.

**Cancel**

Select to cancel the connection creation and close the dialog box.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095741-Connect-to-Logi-Report-Server-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095781-Connect-to-Oracle-Dialog-Box)
