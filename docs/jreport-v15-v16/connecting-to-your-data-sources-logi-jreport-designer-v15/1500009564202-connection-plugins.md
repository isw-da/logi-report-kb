---
title: "Connection Plugins"
id: 1500009564202
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564202-Connection-Plugins
updated_at: 2021-07-24T05:55:45Z
---

# Connection Plugins

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584761-Developing-Reports-from-HDS)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592441-Queries)

# Connection Plugins

Data source connections can be used in Logi JReport as plugins. A connection plugin can have its own drivers, configuration dialog, and logo icon. The configuration dialog defined in a plugin can be used to create a connection to the database and can get drivers from the plugin. Currently Logi JReport provides three plugins for these databases: Oracle, MySQL, and SQL Server, which are stored in the `<install_root>\plugins` directory.

**To set up a connection to connect to the Oracle/MySQL/SQL Server database via plugin:**

1. Do one of the following to start:
   * On the Start Page, select **Oracle**, **MySQL** or **SQL Server** in the Connect category. In the [Create Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009586001-Create-Connection-Dialog) dialog, specify an existing catalog or create a new one and select **OK**.
   * In the Catalog Manager, right-click a data source and select **New JDBC Connection** from the shortcut menu, then select **Oracle**, **MySQL** or **SQL Server** in the Select Connection Type dialog.
   * In the Catalog Manager, select a data source and select **New Data Source** on the toolbar. In the [New Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009587961-New-Data-Source-Dialog) dialog, specify the name of the data source, then select the **Oracle**, **MySQL** or **SQL Server** connection type and select **OK**.
2. In the [Connect to Oracle/MySQL/SQL Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009564782-Connect-to-Oracle-Dialog) dialog, provide the necessary information to connect to the database. If you want to use URL to specify the connection information, select the **Show URL** checkbox and then configure the necessary information. To test whether the specified information is workable, select the **Test Connection** button. If your database has some special requirements, you can select the **More Options** button to modify the [options](https://devnet.logianalytics.com/hc/en-us/articles/1500009587701-Get-JDBC-Connection-Information-Dialog#Options) according to your requirements.

   ![Connect dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893965719/cnctn_plgin_cnnct.gif)
3. Select **OK** and the connection will be added in the specified catalog in the Catalog Manager.

   You can then [add DBMS objects](https://devnet.logianalytics.com/hc/en-us/articles/1500009564002-DBMS-Objects-in-a-JDBC-Connection) from the database into the Logi JReport catalog via the connection.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584761-Developing-Reports-from-HDS)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592441-Queries)
