---
title: "JDBC Connection Plug-ins"
id: 1500009606862
section: "Connecting to Your Data Sources - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009606862-JDBC-Connection-Plug-ins
updated_at: 2021-07-24T16:05:07Z
---

# JDBC Connection Plug-ins

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629581-Setting-Up-JDBC-Connections-in-a-Catalog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606782-DBMS-Objects-in-JDBC-Connections)

# JDBC Connection Plug-ins

Logi Report Designer provides connection plug-ins for the most commonly used relational databases: Oracle, MySQL, SQL Server, InterSystems IRIS, and PostgreSQL, to include the JDBC drivers required for these databases for an easy connection setup procedure (by default Logi Report does not include the MySQL driver in the MySQL connection plug-in for license concern so you will need to provide it by yourself). This topic describes connecting to these databases using the connection plug-ins.

A connection plug-in can have its own driver, configuration dialog, and logo. The configuration dialog defined in a plug-in can be used to create a connection to the database and can get driver from the plug-in.

The following shows the procedure to set up a JDBC connection to connect to an Oracle, MySQL, SQL Server, InterSystems IRIS, or PostgreSQL database via the corresponding connection plug-in:

1. Do one of the following:
   * On the Start Page, select **Oracle**, **MySQL**, **SQL Server**, **InterSystems IRIS**, or **PostgreSQL** in the Connect category. In the [Create Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009630221-Create-Connection-Dialog) dialog, specify an existing catalog or create a new one and select **OK**.
   * In the Catalog Manager, right-click a data source and select **New JDBC Connection** from the shortcut menu, then select **Oracle**,  **MySQL**, **SQL Server**, **InterSystems IRIS**, or **PostgreSQL** in the Select Connection Type dialog.
   * In the Catalog Manager, select a data source and select **New Data Source** on the toolbar. In the [New Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009609222-New-Data-Source-Dialog) dialog, specify the name of the data source, then select the **Oracle**, **MySQL**, **SQL Server**, **InterSystems IRIS**, or **PostgreSQL** connection type and select **OK**.
2. For MySQL, if its driver cannot be found, the [Add Driver](https://devnet.logianalytics.com/hc/en-us/articles/1500009607102-Add-Driver-Dialog) dialog is displayed. Select **Add** to select the MySQL driver jar file from your local disk. Then select **OK** and the driver will be loaded into the MySQL connection plug-in.
3. The [Connect to Oracle](https://devnet.logianalytics.com/hc/en-us/articles/1500009630121-Connect-to-Oracle-Dialog), [Connect to MySQL](https://devnet.logianalytics.com/hc/en-us/articles/1500009630101-Connect-to-MySQL-Dialog), [Connect to SQL Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009630141-Connect-to-SQL-Server-Dialog), [Connect to InterSystems IRIS](https://devnet.logianalytics.com/hc/en-us/articles/1500009630081-Connect-to-InterSystems-IRIS-Dialog), or [Connect to PostgreSQL](https://devnet.logianalytics.com/hc/en-us/articles/1500009607462-Connect-to-PostgreSQL-Dialog) dialog appears (below shows a sample dialog).

   ![Connect to Oracle dialog](https://devnet.logianalytics.com/hc/article_attachments/4404916815511/cnnct2orcl.gif)
4. The Driver drop-down list displays the driver included in the connection plug-in by default.
5. For Oracle, choose whether to use **Service Name**, **SID**, or **TNS** to connect to the database from the Connection Type drop-down list.
6. Type the host name or IP address of the database server in the Server text box.
7. Type the port of the database server in the Port text box.
8. For Oracle, specify the database instance in the text box that corresponds to the connection type. Logi Report Designer will connect with the specified database instance by default. If you select to connect to the Oracle database server using the TNS connection type, you can specify the TNS either by inputting the definition of the TNS entry, or the alias of the TNS entry if you have defined the alias in a tnsnames.ora file.

   For MySQL, specify the name of the database or schema in the Database text box that you want Designer to connect with by default.

   For SQL Server or PostgreSQL, specify the name of the database in the Database text box that you want Designer to connect with by default.

   For InterSystems IRIS, specify the namespace in the Namespace text box that you want Designer to connect with by default.
9. Specify
   the user ID and password used for accessing the database in the User and Password text boxes.
10. Select **Show URL** if you want to view the URL that is formulated by the information you have provided. You can see the URL in the URL text box. You can also specify the valid JDBC URL in the URL text box to establish the connection to the database server. The URL format is regulated by the driver itself.
11. Select the **Test Connection** button to test whether the specified information is correct for setting up the connection.
12. Select the **More Options** button if your database has special requirements to modify the [options](https://devnet.logianalytics.com/hc/en-us/articles/1500009608882-Get-JDBC-Connection-Information-Dialog#Options) accordingly.
13. Select **OK** and Logi Report Designer adds the connection in the specified catalog data source in the Catalog Manager.

    You can then [add DBMS objects](https://devnet.logianalytics.com/hc/en-us/articles/1500009606782-DBMS-Objects-in-JDBC-Connections) from the database into the Logi Report catalog via the connection.

**Notes:**

* If your MySQL database server is configured to use SSL, you need to make sure the URL you provide contains SSL information, for example, `jdbc:mysql://<host>:<port>/test_db?useSSL=true&clientCertificateKeyStoreUrl=C:\SSL_Client\ca-cert.pem&clientCertificateKeyStorePassword=1234`
* If you want to use alias to specify TNS, you need to add the `-Doracle.net.tns_admin=<folder-containing-tnsnames.org-file>` Java VM property in the file JReport.bat which is located in `<designer_install_root>\bin` before starting Designer.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629581-Setting-Up-JDBC-Connections-in-a-Catalog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606782-DBMS-Objects-in-JDBC-Connections)
