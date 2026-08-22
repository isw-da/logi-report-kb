---
title: "Setting Up a JDBC Connection"
id: 1500009584941
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584941-Setting-Up-a-JDBC-Connection
updated_at: 2021-07-24T05:55:48Z
---

# Setting Up a JDBC Connection

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584801-Setting-Up-the-JDBC-Driver)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585001-Example-1-Via-the-Oracle-JDBC-Driver)

# Setting Up a JDBC Connection

This procedure assumes you have set up the JDBC driver as described in the [previous topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584801-Setting-Up-the-JDBC-Driver).

**To connect a Logi JReport catalog with a relational database via a JDBC driver:**

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009562722-Creating-a-Catalog) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog).
2. In the Catalog Manager, right-click the node of a data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.

   If you want to set up the connection in a new data source in the catalog, select any of the existing catalog data sources, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog, specify the name of the data source, select the **JDBC** connection type and select **OK**.
3. In the [Get JDBC Connection Information](https://devnet.logianalytics.com/hc/en-us/articles/1500009587701-Get-JDBC-Connection-Information-Dialog) dialog, provide the necessary information to connect with the database. If your database has some special requirements, you can select the **More Options** button to modify the options according to your requirements. Select **Test Connection**
   to test whether the JDBC information you provide is available.

   ![Get JDBC Connection Information dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893870487/jdbccnnctn.gif)
4. Select **OK** to set up the connection, and you will be prompted with a message box showing the status of connecting to the JDBC driver.

   Upon the finishing setting up the connection, the Add Tables dialog is displayed, prompting you to [add tables from the database to the connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009584821-Tables-Views-Synonyms#Add). If you want to add tables at a later date, select **Done**.

You have four ways to set up a JDBC connection:

* **Setting up by adding an existing connection**
  1. In the Get JDBC Connection Information dialog, select the connection from the Connection List. This list contains previously added connection information.
  2. The JDBC URL and JDBC driver name will then appear in the corresponding text fields. Select **OK**.

  **Note:** The format of the connection information should be JDBC URL/(JDBC Driver Name). For example: `jdbc:odbc:jinfonet/(sun.jdbc.odbc.JdbcOdbcDriver)`.
* **Setting up an ODBC connection**
  1. In the Get JDBC Connection Information dialog, uncheck the **Driver** checkbox and check **Use ODBC Data Source** box.
  2. Enter the ODBC data source name in the DSN Name field.
  3. Input the user name and password to enable accessing the database through the ODBC data source, and then select **OK.**

  **Notes:**

  + The ODBC-JDBC bridge is not included in Java JDKs after version 7. If you are using JDK 8 or later you will get an error that "No suitable driver found for jdbc:odbc".
  + The JDK that Logi JReport uses must match the ODBC data source that the operating system uses. For example, 32-bit ODBC data source can be connected by 32-bit JDK only.
* **Setting up a JDBC connection**
  1. In the Get JDBC Connection Information dialog, specify the driver in the Driver text field.

     The most common error is a ClassNotFound error which is caused by the driver class name not being found in the classpath. If you have included the JDBC driver jar file in the setenv.bat/setenv.sh file then it might be an error in the class name. The class name is case sensitive so if it says OracleDriver it must be the exact case. The driver name is not the name of the JDBC driver jar file.
  2. In the URL text field, specify the URL of the JDBC driver.

     The URL format is regulated by the driver itself. That is, different drivers have different URL formats.

     The format of the driver template in Logi JReport Designer jdbcdrivers.properties is `jdbc.drivers=JDBCDriverName:JDBCDriverName:...`

     where, JDBCDriverName is the JDBC driver name that can be auto-loaded when Logi JReport starts up and "**:**" is the delimiter between two driver names. Logi JReport will search from the beginning of the classpath and find one that contains the class specified.

     Below is an example of the jdbcdrivers.properties file which specifies an Oracle thin driver and an Interbase thin driver:

     `jdbc.drivers=oracle.jdbc.driver.OracleDriver:interbase.interclient.Driver`
  3. Input the user name and password respectively, and then select **OK**.

  **Tip:** After entering the JDBC URL, user name and password, you can leave the Driver text field empty and instead supply it in the property file jdbcdrivers.properties which is located in the `<install_root>\bin` directory.
* **Setting up a connection via the WebLogic 6.1 connection pool**
  1. In the Get JDBC Connection Information dialog, check the**Use Connection Pool**checkbox. The string weblogic.jinfonet.pool.Driver will automatically be displayed in the Driver text field.
  2. In the URL text field, specify the URL of the JDBC driver.
  3. Input the user name and password respectively, and then select **OK**.

Via specific JDBC drivers, you can set up connections which connect Logi JReport Designer to different [report databases](https://devnet.logianalytics.com/hc/en-us/articles/1500009568422-Supported-Report-Databases). The following are some examples:

> * [Example 1: Via the Oracle JDBC Driver](https://devnet.logianalytics.com/hc/en-us/articles/1500009585001-Example-1-Via-the-Oracle-JDBC-Driver)
> * [Example 2: Via the MySQL JDBC Driver](https://devnet.logianalytics.com/hc/en-us/articles/1500009584981-Example-2-Via-the-MySQL-JDBC-Driver)
> * [Example 3: Via SQL Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009564142-Example-3-Via-SQL-Server)
> * [Example 4: Via DB2](https://devnet.logianalytics.com/hc/en-us/articles/1500009564102-Example-4-Via-DB2)
> * [Example 5: Via Informix](https://devnet.logianalytics.com/hc/en-us/articles/1500009584961-Example-5-Via-Informix)
> * [Example 6: Via PostgreSQL](https://devnet.logianalytics.com/hc/en-us/articles/1500009585021-Example-6-Via-PostgreSQL)
> * [Example 7: Via WebLogic 6.1 Connection Pool](https://devnet.logianalytics.com/hc/en-us/articles/1500009585061-Example-7-Via-WebLogic-6-1-Connection-Pool)
> * [Example 8: Via Vertica](https://devnet.logianalytics.com/hc/en-us/articles/1500009564162-Example-8-Via-Vertica)
> * [Example 9: Via Amazon RDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009564122-Example-9-Via-Amazon-RDS)
> * [Example 10: Via RedShift](https://devnet.logianalytics.com/hc/en-us/articles/1500009585041-Example-10-Via-RedShift)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584801-Setting-Up-the-JDBC-Driver)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585001-Example-1-Via-the-Oracle-JDBC-Driver)
