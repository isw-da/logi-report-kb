---
title: "How To Add a DB2 JDBC Driver"
id: 360049960033
section: "Tactics"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360049960033-How-To-Add-a-DB2-JDBC-Driver
updated_at: 2022-11-01T15:25:31Z
---

# How To Add a DB2 JDBC Driver

**Question:**

How do I add a JDBC driver for DB2 in Logi Report?

**Answer:**

Follow these steps to add a new DB2 driver to the Logi Report environment:

1. Download a DB2 driver from IBM. Go to <http://www-01.ibm.com/support/docview.wss?uid=swg21363866>, select a driver version, and then download and install the driver.
2. Follow the standard DB2 configuration instructions to configure the driver: <https://www.ibm.com/support/knowledgecenter/SSEPGG_11.1.0/com.ibm.db2.luw.apdv.java.doc/src/tpc/imjcc_t0010264.html>.
3. Add the driver to Logi Report Designer and Logi Report Server installations. Locate the JDBC library (for example, **db2jcc4.jar)** in your DB2 JDBC driver installation directories and copy it to the **lib** folder in the installation root directory of Logi Report Designer or Logi Report Server.
4. Update the startup file **<install\_root>\bin\Logi Report.bat**for Logi Report Designer or **<install\_root>\bin\JRserver.bat**for Logi Report Server, by adding the following path as the first item in the classpath:  **%REPORTHOME%\lib\db2jcc4.jar;**
5. Restart Logi Report Designer.
6. Add a new data source to Logi Report Designer (see steps below) and Server using the newly installed JDBC driver. Publishing the catalog to the server will provide the necessary information for Logi Report Server to connect to the DB2 database.

Follow these steps to add a new data source in Logi Report Designer:

1. Click **New > Data Source**.
2. In the New Data Source dialog, select **JDBC** as the connection type and click **OK**.
3. In the Get JDBC Connection Information dialog, enter connection parameters as follows:

   ![JDBC Connection Information](https://devnet.logianalytics.com/hc/article_attachments/9932698884247)
4. Click **OK**. You can then access the DB2 database to add tables, views and synonyms to the new data source.
