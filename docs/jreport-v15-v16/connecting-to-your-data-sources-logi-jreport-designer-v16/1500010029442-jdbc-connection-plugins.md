---
title: "JDBC Connection Plugins"
id: 1500010029442
section: "Connecting to Your Data Sources - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010029442-JDBC-Connection-Plugins
updated_at: 2021-07-24T10:39:14Z
---

# JDBC Connection Plugins

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064401-Setting-Up-JDBC-Connections-in-a-Catalog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064321-DBMS-Objects-in-JDBC-Connections)

# JDBC Connection Plugins

Logi JReport Designer provides connection plugins for the most commonly used relational databases: Oracle, MySQL, SQL Server and PostgreSQL, to include the JDBC drivers required for these databases for an easy connection setup procedure (by default Logi JReport does not include the MySQL driver in the MySQL connection plugin for license concern so you will need to provide it by yourself).

A connection plugin can have its own driver, configuration dialog and logo. The configuration dialog defined in a plugin can be used to create a connection to the database and can get driver from the plugin.

**To set up a JDBC connection to connect to the Oracle/MySQL/SQL Server/PostgreSQL database via plugin:**

1. Do one of the following:
   * On the Start Page, select **Oracle**, **MySQL**, **SQL Server** or **PostgreSQL** in the Connect category. In the [Create Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500010030082-Create-Connection-Dialog) dialog, specify an existing catalog or create a new one and select **OK**.
   * In the Catalog Manager, right-click a data source and select **New JDBC Connection** from the shortcut menu, then select **Oracle**, **MySQL**, **SQL Server** or **PostgreSQL** in the Select Connection Type dialog.
   * In the Catalog Manager, select a data source and select **New Data Source** on the toolbar. In the [New Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500010031882-New-Data-Source-Dialog) dialog, specify the name of the data source, then select the **Oracle**, **MySQL**, **SQL Server** or **PostgreSQL** connection type and select **OK**.
2. For MySQL, if its driver cannot be found, the [Add Driver](https://devnet.logianalytics.com/hc/en-us/articles/1500010064641-Add-Driver-Dialog) dialog is displayed. Select **Add** to select the MySQL driver jar file from your local disk. Then select **OK** and the driver will be loaded into the MySQL connection plugin.
3. The [Connect to Oracle](https://devnet.logianalytics.com/hc/en-us/articles/1500010030002-Connect-to-Oracle-Dialog)/[Connect to MySQL](https://devnet.logianalytics.com/hc/en-us/articles/1500010065021-Connect-to-MySQL-Dialog)/[Connect to SQL Server](https://devnet.logianalytics.com/hc/en-us/articles/1500010065061-Connect-to-SQL-Server-Dialog)/[Connect to PostgreSQL](https://devnet.logianalytics.com/hc/en-us/articles/1500010065041-Connect-to-PostgreSQL-Dialog) dialog appears (below shows a sample dialog).

   ![Connect to Oracle dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909240599/cnnct2orcl.gif)
4. The Driver drop-down list displays the driver included in the connection plugin by default.
5. For Oracle, from the Connection Type drop-down list choose whether to use ServiceName, SID, or TNSName to connect to the database. Then in the text box of Service Name/TNS Name which corresponds to the connection type, specify the service name or TNS name of the database instance.

   For MySQL/SQL Server/PostgreSQL, you need to specify the name of the database or schema in the Database text box.
6. In the Server text box, specify the host name or IP address of the database server.
7. Specify the port of the database server in the Port text box.
8. Specify
   the user ID and password used for accessing the database.
9. If you want to use URL to specify the connection information, select the **Show URL** checkbox and then configure the necessary information. To test whether the specified information is workable, select the **Test Connection** button.
10. If your database has some special requirements, you can select the **More Options** button to modify the [options](https://devnet.logianalytics.com/hc/en-us/articles/1500010031562-Get-JDBC-Connection-Information-Dialog#Options) according to your requirements.
11. Select **OK** and the connection will be added in the specified catalog in the Catalog Manager.

    You can then [add DBMS objects](https://devnet.logianalytics.com/hc/en-us/articles/1500010064321-DBMS-Objects-in-JDBC-Connections) from the database into the Logi JReport catalog via the connection.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064401-Setting-Up-JDBC-Connections-in-a-Catalog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064321-DBMS-Objects-in-JDBC-Connections)
