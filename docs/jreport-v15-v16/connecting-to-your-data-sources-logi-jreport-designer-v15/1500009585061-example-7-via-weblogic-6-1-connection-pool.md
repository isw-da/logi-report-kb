---
title: "Example 7: Via WebLogic 6.1 Connection Pool"
id: 1500009585061
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585061-Example-7-Via-WebLogic-6-1-Connection-Pool
updated_at: 2021-07-24T05:55:46Z
---

# Example 7: Via WebLogic 6.1 Connection Pool

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585021-Example-6-Via-PostgreSQL)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564162-Example-8-Via-Vertica)

# Example 7: Via WebLogic 6.1 Connection Pool

This topic introduces how to set up a JDBC Connection via WebLogic 6.1 Connection Pool.

Assume that a catalog has been created with a default data source in Logi JReport Designer. Take the following steps to set up a connection which connects Logi JReport Designer to a database via the WebLogic 6.1 Connection Pool:

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
   2. In the Configuration tab, enter the values in the following fields as follows:

      **Name**: jinfonetDS  
      **JNDI Name**: jinfonetDS  
      **Pool Name**: jinfonet
   3. Select **Create**. The new data source will then be added in the Data Sources node in the left panel.
5. Select the **Targets** tab and add **examplesServer** in the Available column to the Chosen column. Then, select **Apply** to save the changes.
6. Add weblogic.jar to setenv.bat.

   To connect via the WebLogic Connection Pool in Logi JReport Designer, you will first need to add weblogic.jar in `<weblogic_install_root>\wlserver6.1\lib` to the ADDCLASSPATH variable of setenv.bat. In this example, supposing that you have installed Logi JReport Designer in `C:\Logi JReport\Designer`, and WebLogic in `C:\bea`, you will have to modify setenv.bat in `C:\Logi JReport\Designer\bin` to add `C:\bea\wlserver6.1\lib\weblogic.jar` to the ADDCLASSPATH variable as follows:

   `set ADDCLASSPATH=%JAVAHOME%\lib\tools.jar;C:\bea\wlserver6.1\lib\weblogic.jar;`
7. Set up the connection.
   1. Start Logi JReport Designer and open the catalog.
   2. In the Catalog Manager, right-click the node of the default data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.
   3. In the Get JDBC Connection Information dialog, check **Use Connection Pool**. The string weblogic.jinfonet.pool.Driver will automatically be displayed in the Driver text field.
   4. Fill in the URL **jdbc:weblogic:jinfonet:@<hostname>:7001:jinfonetDS**, where @<hostname> is the host name or IP address of the WebLogic Server, 7001 is the port on which the WebLogic Server listens, and jinfonetDS is the JNDI Name of the data source. Then, select **OK**.

**Note:** The data types longbarbinary and BigDecimal are not supported when a WebLogic Connection Pool is used.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585021-Example-6-Via-PostgreSQL)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564162-Example-8-Via-Vertica)
