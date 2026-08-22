---
title: "Example 8: Via Vertica"
id: 1500009564162
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564162-Example-8-Via-Vertica
updated_at: 2021-07-24T05:55:47Z
---

# Example 8: Via Vertica

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585061-Example-7-Via-WebLogic-6-1-Connection-Pool)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564122-Example-9-Via-Amazon-RDS)

# Example 8: Via Vertica

This topic introduces how to set up a JDBC Connection via Vertica.

Assume that:

* You have already installed the Vertica JDBC driver, and have appended the archive files of the driver to the ADDCLASSPATH variable in the file setenv.bat in `<designer_install_root>\bin`.
* The Vertica database server is with the following information:

  **Database Name:** vmartdb  
  **Driver:** com.vertica.jdbc.Driver  
  **URL:** jdbc:vertica://192.168.0.1:5433/vmartdb  
  **User:** dbadmin  
  **Password:** test1234
* A catalog has been created with a default data source.

For details about how to install Vertica, refer to <https://my.vertica.com/docs/6.1.x/HTML/index.htm#1318.htm>.

Take the following steps to set up a connection which connects Logi JReport Designer to a database via Vertica:

1. Start Logi JReport Designer and open the catalog.
2. In the Catalog Manager, right-click the node of the default data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.
3. In the Get JDBC Connection Information dialog, enter the JDBC driver class name **com.vertica.jdbc.Driver** in the Driver text field.
4. In the URL text field, specify the URL in the format `jdbc:vertica://<hostname>:<port>/<SID>`. In this example, enter **jdbc:vertica://192.168.0.1:5433/vmartdb**.
5. Input the user name **dbadmin** and password **test1234** respectively.

   ![Get JDBC Connection Information dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893966871/cnctn_jdbc_set_vtc.gif)
6. Select **OK** to set up the connection.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585061-Example-7-Via-WebLogic-6-1-Connection-Pool)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564122-Example-9-Via-Amazon-RDS)
