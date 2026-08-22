---
title: "Example 6: Via PostgreSQL"
id: 1500009585021
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585021-Example-6-Via-PostgreSQL
updated_at: 2021-07-24T05:55:47Z
---

# Example 6: Via PostgreSQL

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584961-Example-5-Via-Informix)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585061-Example-7-Via-WebLogic-6-1-Connection-Pool)

# Example 6: Via PostgreSQL

This topic introduces how to set up a JDBC Connection via PostgreSQL.

Assume that:

* You have already installed PostgreSQL driver, and have appended the archive files of the driver to the ADDCLASSPATH variable in the file setenv.bat in `<designer_install_root>\bin`.
* The PostgreSQL database server is with the following information:

  **Driver:** org.postgresql.Driver  
  **URL:**  jdbc:postgresql://qad04.jinfonet.com.cn:5432/postgres  
  **User:** jrDesign  
  **Password:** Test1234
* A catalog has been created with a default data source.

Take the following steps to set up a connection which connects Logi JReport Designer to a database via PostgreSQL:

1. Start Logi JReport Designer and open the catalog.
2. In the Catalog Manager, right-click the node of the default data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.
3. In the Get JDBC Connection Information dialog, enter the JDBC driver class name **org.postgresql.Driver** in the Driver text field.
4. In the URL text field, specify the URL as **jdbc:postgresql://qad04.jinfonet.com.cn:5432/postgres**.
5. Input the user name **jrDesign** and password **Test1234** respectively.

   ![Get JDBC Connection Information dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893967639/cnctn_jdbc_set_pstgrsql.gif)
6. Select **OK** to set up the connection.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584961-Example-5-Via-Informix)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585061-Example-7-Via-WebLogic-6-1-Connection-Pool)
