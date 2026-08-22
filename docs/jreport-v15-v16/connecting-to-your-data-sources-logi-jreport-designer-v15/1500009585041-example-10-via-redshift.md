---
title: "Example 10: Via RedShift"
id: 1500009585041
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585041-Example-10-Via-RedShift
updated_at: 2021-07-24T05:55:47Z
---

# Example 10: Via RedShift

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564122-Example-9-Via-Amazon-RDS)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584841-Setting-Up-OOJDBC-Connections)

# Example 10: Via RedShift

This topic introduces how to set up a JDBC Connection via RedShift.

Assume that:

* You have already installed the PostgreSQL JDBC driver, and have appended the archive files of the driver to the ADDCLASSPATH variable in the file setenv.bat in `<designer_install_root>\bin`.
* The RedShift database server is with the following information:

  **Driver:** org.postgresql.Driver  
  **URL:** jdbc:postgresql://jinfonet-rsdw-demo.cfcn5ogc14yr.us-east-1.redshift.amazonaws.com:5439/sampledb (The URL is dynamically generated when you apply an instance.)  
  **User:** dbadmin  
  **Password:** test1234
* A catalog has been created with a default data source.

For details about how to install RedShift, refer to <http://docs.aws.amazon.com/redshift/latest/dg/c_intro_to_admin.html>.

Take the following steps to set up a connection which connects Logi JReport Designer to a database via RedShift:

1. Start Logi JReport Designer and open the catalog.
2. In the Catalog Manager, right-click the node of the default data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.
3. In the Get JDBC Connection Information dialog, enter the JDBC driver class name **org.postgresql.Driver** in the Driver text field.
4. In the URL text field, specify the URL as **jdbc:postgresql://jinfonet-rsdw-demo.cfcn5ogc14yr.us-east-1.redshift.amazonaws.com:5439/sampledb**.
5. Input the user name **dbadmin** and password **test1234** respectively.

   ![Get JDBC Connection Information dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889396247/cnctn_jdbc_set_redshift.gif)
6. Select **OK** to set up the connection.

**Notes:**

* Redshift does not support the "Double" data type and it uses "Decimal" or "Double Precision" instead.
* Redshift does not support "Bytea", "Bit(N)" or "Bit varying (N)" data type, and so far there is no alternative data type for that, therefore Logi JReport binary data fields like photos stored in the demo database cannot be imported to Redshift.
* For detailed features, functions, and data types that are not supported in Redshift, see <http://docs.aws.amazon.com/redshift/latest/dg/c_redshift-and-postgres-sql.html>.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564122-Example-9-Via-Amazon-RDS)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584841-Setting-Up-OOJDBC-Connections)
