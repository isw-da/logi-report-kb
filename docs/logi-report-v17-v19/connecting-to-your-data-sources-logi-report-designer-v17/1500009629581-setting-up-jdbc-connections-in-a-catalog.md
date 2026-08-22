---
title: "Setting Up JDBC Connections in a Catalog"
id: 1500009629581
section: "Connecting to Your Data Sources - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009629581-Setting-Up-JDBC-Connections-in-a-Catalog
updated_at: 2021-07-24T16:05:07Z
---

# Setting Up JDBC Connections in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629541-JDBC-Connections) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606862-JDBC-Connection-Plug-ins)

# Setting Up JDBC Connections in a Catalog

Logi Report supports most of the [relational databases](https://devnet.logianalytics.com/hc/en-us/articles/1500009611342-Supported-Report-Databases) which support JDBC drivers. Via specific JDBC drivers, you can create connections which connect Logi Report catalogs to different relational databases.

This topic includes the following sections:

* [Setting Up the JDBC Driver](#Driver)
* [Creating a Connection via the JDBC Driver](#Connection)
  + [Example 1: Connecting to Amazon RDS](#RDS)
  + [Example 2: Connecting to RedShift](#RedShift)
  + [Example 3: Connecting via WebLogic 6.1 Connection Pool](#WebLogic)

## Setting Up the JDBC Driver

Before you can retrieve data from a relational database in Logi Report, you should first set up the JDBC driver as follows:

1. Install the JDBC driver according to the instructions provided by the JDBC driver supplier and understand the URL format required by the driver.
2. Append the class path of the JDBC driver's jar files with full path into Logi Report's environment configuration file by editing setenv.bat for Windows or setenv.sh for Unix/Linux in `<designer_install_root>\bin`.

   For example, if you are using the Oracle JDBC driver ojdbc7.jar, append it as follows:

   `set ADDCLASSPATH=%JAVAHOME%\lib\tools.jar;c:\oracle\lib\ojdbc7.jar;`

   The step for appending the class path is very important. The same changes made to Logi Report Designer’s class path must be made to the class path for Logi Report Server too. A missing JDBC driver in the Logi Report start-up batch file or command line will result in a "ClassNotFoundError message" when you try to run a report. Meanwhile, if you want to use the Preview as Page/Web Report Result feature in Logi Report Designer, you also need to append the class path for the JDBC driver to setenv.bat/setenv.sh in `<designer_install_root>\server\bin.`
3. Add the driver into Logi Report Designer's driver template file jdbcdrivers.properties in `<designer_install_root>\bin` in the following format:

   jdbc.drivers=JDBCDriverName:JDBCDriverName:...

   where, JDBCDriverName is the JDBC driver name that can be auto-loaded when Logi Report starts up and "**:**" is the delimiter between two driver names. See an example below of the jdbcdrivers.properties file which specifies an Oracle thin driver and an Interbase thin driver:

   `jdbc.drivers=oracle.jdbc.driver.OracleDriver:interbase.interclient.Driver`

   Once the drivers are added in jdbcdrivers.properties, later when you set up JDBC connections in Logi Report Designer, you do not need to provide the driver name manually. Logi Report will search from the beginning of the classpath and find one that contains the class specified.

## Creating a Connection via the JDBC Driver

To set up a JDBC connection in a Logi Report catalog to retrieve data via JDBC driver, take the following steps:

1. In Logi Report Designer, [create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, right-click the node of a data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.

   If you want to set up the connection in a new data source in the catalog, select any of the existing catalog data sources, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog, specify the name of the data source, select the **JDBC** connection type and select **OK**.
3. In the [Get JDBC Connection Information](https://devnet.logianalytics.com/hc/en-us/articles/1500009608882-Get-JDBC-Connection-Information-Dialog) dialog, provide the necessary information to connect with the database.

   ![Get JDBC Connection Information dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904262935/jdbccnnctn.gif)

   You have four ways to set up a JDBC connection:

   * **Setting up by adding an existing connection**
     1. From the Connection List drop-down list select the connection. This list contains previously added connection information. The format of the connection information is JDBC URL/(JDBC Driver Name), for example:

        `jdbc:odbc:jinfonet/(sun.jdbc.odbc.JdbcOdbcDriver)`
     2. The JDBC URL and JDBC driver name then appear in the corresponding text boxes.
   * **Setting up a new JDBC connection**
     1. In the Driver text box specify the driver. If you have [added the driver into jdbcdrivers.properties](#AddDriver) when setting up the JDBC driver, you can leave this empty. Logi Report Designer can find the correct driver from the file.
     2. Specify the URL of the JDBC driver in the URL text box.
        The URL format is regulated by the driver itself.
     3. Specify the user name and password used to connect to the database.
   * **Setting up an ODBC connection**
     1. Clear the **Driver** checkbox and select **Use ODBC Data Source**.
     2. Type the ODBC data source name in the DSN Name text box.
     3. Specify the user name and password to enable accessing the database through the ODBC data source.

     **Notes:**

     + The ODBC-JDBC bridge is not included in Java JDKs after version 7. For JDK 8 or later, you will get an error that "No suitable driver found for jdbc:odbc". To resolve this issue, you need to add the path information of the ODBC-JDBC bridge to the class path during installation or by editing the setenv.bat (setenv.sh on Unix/Linux) file in `<designer_install_root>\bin`.
     + The JDK that Logi Report uses must match the ODBC data source that the operating system uses. For example, 32-bit ODBC data source can be connected by 32-bit JDK only.
   * **Setting up a connection via the WebLogic 6.1 connection pool**
     1. Select  **Use Connection Pool**. The string weblogic.jinfonet.pool.Driver is then automatically displayed in the Driver text box.
     2. In the URL text box, specify the URL of the JDBC driver.
     3. Specify the user name and password respectively.
4. If your database has some special requirements, you can select the **More Options** button to modify the options according to your requirements.
5. Select **Test Connection** to test whether the information you provide is available.
6. Select **OK** to set up the connection, and you will be prompted with a message box showing the status of connecting to the database.

   Upon finishing setting up the connection, the Add Tables/Views/Synonyms dialog is displayed, prompting you to [add tables from the database](https://devnet.logianalytics.com/hc/en-us/articles/1500009629561-Tables-Views-Synonyms#Add) to the Logi Report catalog. If you want to add tables at a later date, select **Done**.

You can also use the [connection plug-ins](https://devnet.logianalytics.com/hc/en-us/articles/1500009606862-JDBC-Connection-Plug-ins) provided by Logi Report Designer to connect to the Oracle, MySQL, SQL Server, InterSystems IRIS, and PostgreSQL databases in an easy way.

**Note:** If you want to use the DB2 app connection, you need to install the client and configure the net address first.

The following presents some examples of connecting to specific relational databases:

### Example 1: Connecting to Amazon RDS

Assume that:

* You have already installed the JDBC driver (com.mysql.jdbc.Driver), and have appended the archive files of the driver to the ADDCLASSPATH variable in the file setenv.bat in `<designer_install_root>\bin`.
* The RDS database server has the following information:

  Host name: jrdbtest.c4fb8hiicidz.us-west-2.rds.amazonaws.com  
  Port number: 3306   
  Database name: sampledb1110  
  Database user & password: dbadmin, test1234

Take the following steps to set up a connection which connects Logi Report Designer to a database via Amazon RDS:

1. Open a catalog in Logi Report Designer.
2. In the Catalog Manager, right-click the node of an existing data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.
3. In the Get JDBC Connection Information dialog, type the JDBC driver class name **com.mysql.jdbc.Driver** in the Driver text box.
4. In the URL text box, specify the URL in the format `jdbc:mysql://<hostname>:<port>/<database>`. In this example, type **jdbc:mysql://jrdbtest.c4fb8hiicidz.us-west-2.rds.amazonaws.com:3306/sampledb1110**. The URL is dynamically generated when you apply an instance.
5. Type the user name **dbadmin** and password **test1234** respectively.

   ![Get JDBC Connection Information dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904408855/cnctn_jdbc_set_rds.gif)
6. Select **OK** to set up the connection.

**Notes:**

* It is not recommended to use RDS for small data queries since it takes a long time in the cloud.
* The RDS MySQL database is case sensitive for table names and column names, which may result in that Logi Report sample reports cannot run.

### Example 2: Connecting to RedShift

Assume that:

* You have already installed the PostgreSQL JDBC driver (org.postgresql.Driver), and have appended the archive files of the driver to the ADDCLASSPATH variable in the file setenv.bat in `<designer_install_root>\bin`.
* The RedShift database server has the following information:

  Host name: jinfonet-rsdw-demo.cfcn5ogc14yr.us-east-1.redshift.amazonaws.com  
  Port number: 5439   
  Database name: sampledb  
  Database user & password: dbadmin, test1234

Take the following steps to set up a connection which connects Logi Report Designer to a database via RedShift:

1. Open a catalog in Logi Report Designer.
2. In the Catalog Manager, right-click the node of an existing data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.
3. In the Get JDBC Connection Information dialog, type the JDBC driver class name **org.postgresql.Driver** in the Driver text box.
4. In the URL text box, specify the URL in the format `jdbc:postgresql://<hostname>:<port>/<database>`. In this example, type **jdbc:postgresql://jinfonet-rsdw-demo.cfcn5ogc14yr.us-east-1.redshift.amazonaws.com:5439/sampledb**. The URL is dynamically generated when you apply an instance.
5. Type the user name **dbadmin** and password **test1234** respectively.

   ![Get JDBC Connection Information dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904409239/cnctn_jdbc_set_redshift.gif)
6. Select **OK** to set up the connection.

**Notes:**

* Redshift does not support the "Double" data type and it uses "Decimal" or "Double Precision" instead.
* Redshift does not support "Bytea", "Bit(N)" or "Bit varying (N)" data type, and so far there is no alternative data type for that, therefore Logi Report binary data fields like photos stored in the demo database cannot be imported to Redshift.
* For detailed features, functions, and data types that are not supported in Redshift, see <http://docs.aws.amazon.com/redshift/latest/dg/c_redshift-and-postgres-sql.html>.

### Example 3: Connecting via WebLogic 6.1 Connection Pool

1. Set up the WebLogic Connection Pool.
   1. Assume that the WebLogic Server has been started, access the console through a web browser (`http://host:7001/console`). Then, go to the left panel, and expand the **JDBC** node.
   2. Select the **Connection Pools** node. All the defined connection pools will be displayed in the right panel.
   3. Select the **Configure a New JDBC Connection Pool** link.
   4. In the Configuration tab, define the connection pool as follows. Then, select the **Create** button.

      **Name**: jinfonet  
      **URL**: jdbc:odbc:jinfonet  
      **Driver Classname**: sun.jdbc.odbc.JdbcOdbcDriver
2. Check the Connection Pool.

   In the Monitoring tab, select the link **Monitor all Active Pools** to check if the pool is active. You will see the connection pool that you just created appear in the Monitoring tab.
3. Select the **Targets** tab, and add **examplesServer** to the **Chosen** column (in order to assign the connection pool to the server). Then, select **Apply** to save your changes.
4. Set up the data source.
   1. Select the **Data Sources** node in the JDBC node. In the right panel, select the **Configure a New JDBC Data Source** link.
   2. In the Configuration tab, specify the values in the following text boxes as follows:

      **Name**: jinfonetDS  
      **JNDI Name**: jinfonetDS  
      **Pool Name**: jinfonet
   3. Select **Create**. The new data source will then be added in the Data Sources node in the left panel.
5. Select the **Targets** tab and add **examplesServer** in the Available column to the Chosen column. Then, select **Apply** to save the changes.
6. Add weblogic.jar to setenv.bat.

   To connect via the WebLogic Connection Pool in Logi Report Designer, you will first need to add weblogic.jar in `<weblogic_install_root>\wlserver6.1\lib` to the ADDCLASSPATH variable of setenv.bat. In this example, supposing that you have installed Logi Report Designer in `C:\LogiReport\Designer`, and WebLogic in `C:\bea`, you will have to modify setenv.bat in `C:\LogiReport\Designer\bin` to add `C:\bea\wlserver6.1\lib\weblogic.jar` to the ADDCLASSPATH variable as follows:

   `set ADDCLASSPATH=%JAVAHOME%\lib\tools.jar;C:\bea\wlserver6.1\lib\weblogic.jar;`
7. Set up the connection in Logi Report Designer.
   1. Open a catalog.
   2. In the Catalog Manager, right-click the node of an existing data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.
   3. In the Get JDBC Connection Information dialog, select **Use Connection Pool**. The string weblogic.jinfonet.pool.Driver automatically displays in the Driver text box.
   4. Fill in the URL **jdbc:weblogic:jinfonet:@<hostname>:7001:jinfonetDS**, where <hostname> is the host name or IP address of the WebLogic Server, 7001 is the port on which the WebLogic Server listens, and jinfonetDS is the JNDI Name of the data source. Then, select **OK**.

**Note:** The data types longbarbinary and BigDecimal are not supported when a WebLogic Connection Pool is used.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629541-JDBC-Connections) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606862-JDBC-Connection-Plug-ins)
