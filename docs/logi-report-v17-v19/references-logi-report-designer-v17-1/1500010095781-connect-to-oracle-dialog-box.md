---
title: "Connect to Oracle Dialog Box"
id: 1500010095781
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010095781-Connect-to-Oracle-Dialog-Box
updated_at: 2021-07-23T19:15:07Z
---

# Connect to Oracle Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095761-Connect-to-MySQL-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058282-Connect-to-PostgreSQL-Dialog-Box)

# Connect to Oracle Dialog Box

You can use the Connect to Oracle dialog box to specify the information for connecting to an Oracle database [via the connection plug-in](https://devnet.logianalytics.com/hc/en-us/articles/1500010095221-Creating-JDBC-Connections-via-Plug-ins). This topic describes the options in the dialog box.

Designer displays the Connect to Oracle dialog box appears when you do one of the following:

* Select OK in the [Create Connection to Oracle dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095881-Create-Connection-Dialog-Box).
* Select Oracle and select OK in the [New Data Source dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059982-New-Data-Source-Dialog-Box).
* In the Catalog Manager, right-click a data source and select New JDBC Connection from the shortcut menu, then select Oracle in the Select Connection Type dialog box and select OK.

![Connect to Oracle dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848622103/cnnct2orcl.gif)

You see the following options in the dialog box:

**Driver**

The option shows the Oracle JDBC driver name that this connection uses.

**Connection Type**

Specify the way using which to connect to the Oracle database: Service Name, SID, or TNS.

**Server**

Specify the host name or IP address of the database server.

**Port**

Specify the port of the database server.

**Service Name/SID/TNS**

Specify the service name/SID/TNS of the database instance that you want Designer to connect with by default.

**User**

Specify the user ID used for accessing the database.

**Password**

Specify the password used for accessing the database.

**Show URL**

Select to show the URL used for connecting to the database server.

* **URL**  
  The option shows the URL which is formulated by the information you provide. You can also type the valid JDBC URL in the text box to establish the connection to the database server. The URL format is regulated by the driver itself. When Service Name is selected as the connection type, the format is `jdbc:oracle:thin:@//<host>:<port>/<service_name>`; when SID is selected, the format is `jdbc:oracle:thin:@<host>:<port>:<SID>`; for TNS, the format is `jdbc:oracle:thin:@<TNS>`.

**Test Connection**

Select to test whether the specified connection information can connect to the database successfully.

**More Options**/**Less Options**

Select to show or hide the [options](https://devnet.logianalytics.com/hc/en-us/articles/1500010097761-Get-JDBC-Connection-Information-Dialog-Box#Options) for experienced users to configure the connection to meet the special requirements of the database.

**OK**

Select to create the connection to the Oracle database and close the dialog box.

**Cancel**

Select to cancel the connection creation and close the dialog box.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095761-Connect-to-MySQL-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058282-Connect-to-PostgreSQL-Dialog-Box)
