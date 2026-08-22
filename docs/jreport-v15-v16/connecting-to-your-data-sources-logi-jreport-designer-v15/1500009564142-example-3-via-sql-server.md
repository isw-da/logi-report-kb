---
title: "Example 3: Via SQL Server"
id: 1500009564142
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564142-Example-3-Via-SQL-Server
updated_at: 2021-07-24T05:55:46Z
---

# Example 3: Via SQL Server

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584981-Example-2-Via-the-MySQL-JDBC-Driver)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564102-Example-4-Via-DB2)

# Example 3: Via SQL Server

This topic introduces how to set up a JDBC Connection via the SQL Server.

Assume that:

* You have already installed the SQL driver, and have appended the archive files of the driver to the ADDCLASSPATH variable in the file setenv.bat in `<designer_install_root>\bin`.
* The SQL Server is with the following information:

  **Driver:** com.microsoft.sqlserver.jdbc.SQLServerDriver  
  **URL:**  jdbc:sqlserver://db35.jinfonet.com.cn:1433;DatabaseName=test  
  **User:** test  
  **Password:** 1234
* A catalog has been created with a default data source.

Take the following steps to set up a connection which connects Logi JReport Designer to a database via SQL Server:

1. Start Logi JReport Designer and open the catalog.
2. In the Catalog Manager, right-click the node of the default data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.
3. In the Get JDBC Connection Information dialog, enter the JDBC driver class name **com.microsoft.sqlserver.jdbc.SQLServerDriver** in the Driver text field.
4. In the URL text field, specify the URL as **jdbc:sqlserver://db35.jinfonet.com.cn:1433;DatabaseName=test**.
5. Input the user name **test** and password **1234** respectively.

   ![Get JDBC Connection Information](https://devnet.logianalytics.com/hc/article_attachments/4404893967127/cnctn_jdbc_set_sqlsvr.gif)
6. Select **OK** to set up the connection.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584981-Example-2-Via-the-MySQL-JDBC-Driver)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564102-Example-4-Via-DB2)
