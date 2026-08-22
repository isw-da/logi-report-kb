---
title: "Example 2: Via the MySQL JDBC Driver"
id: 1500009584981
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584981-Example-2-Via-the-MySQL-JDBC-Driver
updated_at: 2021-07-24T05:55:48Z
---

# Example 2: Via the MySQL JDBC Driver

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585001-Example-1-Via-the-Oracle-JDBC-Driver)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564142-Example-3-Via-SQL-Server)

# Example 2: Via the MySQL JDBC Driver

This topic introduces how to set up a JDBC Connection via the MySQL JDBC Driver.

Assume that:

* You have already installed the MySQL JDBC driver and have appended the jar archive files of the driver to the ADDCLASSPATH variable in the file setenv.bat/setenv.sh in `<designer_install_root>\bin`.
* The MySQL database server has the host name qad08.jinfonet.com.cn, port number 3306, database demodb1000, user name jrDesign and password Test1234.
* A catalog has been created with a default data source.

Take the following steps to set up a connection which connects Logi JReport Designer to a database via the MySQL JDBC driver:

1. Start Logi JReport Designer and open the catalog.
2. In the Catalog Manager, right-click the node of the default data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.
3. In the Get JDBC Connection Information dialog, enter the JDBC driver class name **com.mysql.jdbc.Driver** into the Driver text field.
4. In the URL text field, specify the URL in the format `jdbc:mysql://<hostname>:<port>/<database>`. In this example, enter **jdbc:mysql://qad08.jinfonet.com.cn:3306/demodb1000**.
5. Input the user name **jrDesign** and password **Test1234** respectively.

   ![Get JDBC Connection Information dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893968151/cnctn_jdbc_set_mysql.gif)
6. Select **OK** to set up the connection.

**Notes:**

* If you need to use tables from more than one database, you can open the Options panel and in the Qualifier tab, select 2-Part Names. This creates the SQL with <database>.<table> in the FROM clause of the SQL.
* When you specify 2-Part Names you can leave the database name off the URL. In this example, the URL can be jdbc:mysql://qad08.jinfonet.com.cn:3306.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585001-Example-1-Via-the-Oracle-JDBC-Driver)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564142-Example-3-Via-SQL-Server)
