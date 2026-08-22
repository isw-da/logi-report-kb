---
title: "Example 5: Via Informix"
id: 1500009584961
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584961-Example-5-Via-Informix
updated_at: 2021-07-24T05:55:47Z
---

# Example 5: Via Informix

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564102-Example-4-Via-DB2)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585021-Example-6-Via-PostgreSQL)

# Example 5: Via Informix

This topic introduces how to set up a JDBC Connection via Informix.

Assume that:

* You have already installed Informix driver, and have appended the archive files of the driver to the ADDCLASSPATH variable in the file setenv.bat in `<designer_install_root>\bin`.
* The Informix database server is with the following information:

  **Driver:** com.informix.jdbc.IfxDriver  
  **URL:**  jdbc:informix-sqli://qad02.jinfonet.com.cn:9090/DataType:INFORMIXSERVER=ol\_informix1210\_1  
  **User:** jrDesign  
  **Password:** Test1234
* A catalog has been created with a default data source.

Take the following steps to set up a connection which connects Logi JReport Designer to a database via Informix:

1. Start Logi JReport Designer and open the catalog.
2. In the Catalog Manager, right-click the node of the default data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.
3. In the Get JDBC Connection Information dialog, enter the JDBC driver class name **com.informix.jdbc.IfxDriver** in the Driver text field.
4. In the URL text field, specify the URL as **jdbc:informix-sqli://qad02.jinfonet.com.cn:9090/DataType:INFORMIXSERVER=ol\_informix1210\_1**.
5. Input the user name **jrDesign** and password **Test1234** respectively.

   ![Get JDBC Connection Information dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889396631/cnctn_jdbc_set_infmx.gif)
6. Select **OK** to set up the connection.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564102-Example-4-Via-DB2)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585021-Example-6-Via-PostgreSQL)
