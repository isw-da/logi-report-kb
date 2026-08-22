---
title: "Example 1: Via the Oracle JDBC Driver"
id: 1500009585001
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585001-Example-1-Via-the-Oracle-JDBC-Driver
updated_at: 2021-07-24T05:55:47Z
---

# Example 1: Via the Oracle JDBC Driver

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584941-Setting-Up-a-JDBC-Connection)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584981-Example-2-Via-the-MySQL-JDBC-Driver)

# Example 1: Via the Oracle JDBC Driver

This topic introduces how to set up a JDBC Connection via the Oracle JDBC Driver.

Assume that:

* You have already installed the Oracle JDBC driver, and have appended the archive files of the thin driver to the ADDCLASSPATH variable in the file setenv.bat in `<designer_install_root>\bin`.
* The Oracle database server has the name p02\_wuhb, port number 1521, database orcl, user name scott and password tiger.
* A catalog has been created with a default data source.

Take the following steps to set up a connection which connects Logi JReport Designer to a database via the Oracle JDBC driver:

1. Start Logi JReport Designer and open the catalog.
2. In the Catalog Manager, right-click the node of the default data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.
3. In the Get JDBC Connection Information dialog, enter the JDBC driver class name **oracle.jdbc.OracleDriver** in the Driver text field.
4. In the URL text field, specify the URL in the format `jdbc:oracle:thin:@<hostname>:<port>:<SID>`. In this example, enter **jdbc:oracle:thin:@p02\_wuhb:1521:orcl**.
5. Input the user name **scott** and password **tiger** respectively.

   ![Get JDBC Connection Information dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893967895/cnctn_jdbc_set_oracle.gif)
6. Select **OK** to set up the connection.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584941-Setting-Up-a-JDBC-Connection)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584981-Example-2-Via-the-MySQL-JDBC-Driver)
