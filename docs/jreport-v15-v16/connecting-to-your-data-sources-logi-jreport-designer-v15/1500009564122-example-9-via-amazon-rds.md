---
title: "Example 9: Via Amazon RDS"
id: 1500009564122
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564122-Example-9-Via-Amazon-RDS
updated_at: 2021-07-24T05:55:47Z
---

# Example 9: Via Amazon RDS

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564162-Example-8-Via-Vertica)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585041-Example-10-Via-RedShift)

# Example 9: Via Amazon RDS

This topic introduces how to set up a JDBC Connection via Amazon RDS.

Assume that:

* You have already installed the JDBC driver, and have appended the archive files of the driver to the ADDCLASSPATH variable in the file setenv.bat in `<designer_install_root>\bin`.
* The RDS database server is with the following information:

  **Driver:** com.mysql.jdbc.Driver  
  **URL:** jdbc:mysql://jrdbtest.c4fb8hiicidz.us-west-2.rds.amazonaws.com:3306/sampledb1110 (The URL is dynamically generated when you apply an instance.)  
  **User:** dbadmin  
  **Password:** test1234
* A catalog has been created with a default data source.

For details about how to install Amazon RDS, refer to [Getting Started with Amazon RDS](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html).

Take the following steps to set up a connection which connects Logi JReport Designer to a database via Amazon RDS:

1. Start Logi JReport Designer and open the catalog.
2. In the Catalog Manager, right-click the node of the default data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.
3. In the Get JDBC Connection Information dialog, enter the JDBC driver class name **com.mysql.jdbc.Driver** in the Driver text field.
4. In the URL text field, specify the URL as **jdbc:mysql://jrdbtest.c4fb8hiicidz.us-west-2.rds.amazonaws.com:3306/sampledb1110**.
5. Input the user name **dbadmin** and password **test1234** respectively.

   ![Get JDBC Connection Information dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893967383/cnctn_jdbc_set_rds.gif)
6. Select **OK** to set up the connection.

**Notes:**

* It is not recommended to use RDS for small data queries since it takes a long time in the cloud.
* The RDS MySQL database is case sensitive for table names and column names, which may result in that Logi JReport sample reports cannot run.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](#)[Next Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009585041-Example-10-Via-RedShift)![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)
