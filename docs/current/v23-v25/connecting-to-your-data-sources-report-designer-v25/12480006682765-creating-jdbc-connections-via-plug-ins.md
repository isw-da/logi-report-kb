---
title: "Creating JDBC Connections via Plug-ins"
id: 12480006682765
section: "Connecting to Your Data Sources - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480006682765-Creating-JDBC-Connections-via-Plug-ins
updated_at: 2026-02-25T23:50:15Z
source_host: docs-report.zendesk.com
---
# 
Creating JDBC Connections via Plug-ins

Designer provides connection plug-ins  for the most commonly used relational databases in the <install_root>\plugin directory: Oracle, MySQL, SQL Server, InterSystems IRIS, and PostgreSQL, to include the JDBC drivers required for these databases for an easy connection setup procedure (by default, Designer does not include the MySQL driver in the MySQL connection plug-in for license concern so you need to add it by yourself). This topic introduces connecting to these databases using the connection plug-ins. It also describes the configurations you need to make before you can connect to an Oracle database via Wallet.

A connection plug-in can have its own driver, configuration dialog box, and logo. The configuration dialog box can get the driver from the plug-in, and you can use the dialog box to create a connection to the database.

The following shows the procedure to set up a JDBC connection to connect to an Oracle, MySQL, SQL Server, InterSystems IRIS, or PostgreSQL database via the corresponding connection plug-in.

- Do one of the following:
    
- In the Start Page, select Oracle, MySQL, SQL Server, InterSystems IRIS, or PostgreSQL in the Connect category. In the Create Connection dialog box, specify an existing catalog or create a new one and select OK. 

- In the Catalog Manager, right-click a data source and select New JDBC Connection from the shortcut menu. In the Select Connection Type dialog box, select Oracle,  MySQL, SQL Server,  InterSystems IRIS, or PostgreSQL.

- In the Catalog Manager, select a data source and select New Data Source on the toolbar. In the New Data Source dialog box, specify the name of the data source, then select the Oracle, MySQL, SQL Server, InterSystems IRIS, or PostgreSQL connection type and select OK. 

- Designer displays the Connect to Oracle dialog box, Connect to MySQL dialog box, Connect to SQL Server dialog box, Connect to InterSystems IRIS dialog box, or Connect to PostgreSQL dialog box.
    For MySQL, if Designer cannot find its driver, it displays the Add Driver dialog box first. Select Add to select the MySQL driver JAR file from your local disk, then select OK and Designer loads the driver into the MySQL connection plug-in.

The following shows a sample dialog box.

- The Driver drop-down list displays the driver included in the connection plug-in by default. 

- For Oracle, choose whether to use Service Name, SID, or TNS to connect to the database from the Connection Type drop-down list.

-  In the Server text box, type the host name or IP address of the database server.

- In the Port text box, type the port of the database server. Then,
- For Oracle, specify the database instance in the  text box that corresponds to the connection type. Designer connects with the specified database instance by default. If you select to connect to the Oracle database server using the TNS connection type, you can specify the TNS  either by typing the definition of the TNS entry, or  the alias of the TNS entry if you have defined the alias  in a tnsnames.ora file.

- For MySQL, specify the name of the database or schema in the Database text box that you want  Designer to connect with by default.

- For SQL Server or PostgreSQL, specify the name of the database in the Database text box that you want  Designer to connect with by default.

- For  InterSystems IRIS, specify  the namespace  in the Namespace text box  that you want  Designer to connect with by default.

- In the User and Password text boxes, specify the user ID and password used for accessing the database.

- Select Show URL if you want to view the URL that is formulated by the information you have provided. You can see the URL in the URL text box. You can also  specify the valid JDBC URL in the URL text box to establish the connection to the database server.  The URL format is regulated by the driver itself.

- Select Test Connection to test whether the specified information is correct for setting up the connection.

- Select More Options if your database has special requirements  to modify the options accordingly. 

- Select OK and Designer adds the connection in the specified catalog data source in the Catalog Manager. You can then add  objects from the database into the catalog via the connection.

- If your MySQL database server is configured to use SSL, you need to make sure the URL you provide contains SSL information, for example, jdbc:mysql://<host>:<port>/test_db?useSSL=true&clientCertificateKeyStoreUrl=C:\SSL_Client\ca-cert.pem&clientCertificateKeyStorePassword=1234

- If you want to use alias to specify TNS, you need to add the -Doracle.net.tns_admin=<directory_containing_tnsnames.org> option to the CLASSPATH environment variable of Designer's startup file JReport.bat  in <designer_install_root>\bin before starting Designer.

## 
Connecting to Oracle Databases via Wallets

Oracle Wallet provides an simple and easy method to manage database credentials across multiple domains. However, Designer does not support connecting to Oracle databases via Wallet by default. If you want to set up an Oracle connection using Wallet, you need to first make some configurations.

- Create the wallet and define the properties of the database connection identifier in the file tnsnames.ora as described in the Oracle documentation.

- Add the three Oracle JAR files: oraclepki.jar, osdt_core.jar, and osdt_cert.jar to the <designer_install_root>\lib directory.

- Use the -Doracle.net.tns_admin and -Doracle.net.wallet_location options to add the locations of tnsnames.ora and the wallet file to the CLASSPATH environment variable of Designer's startup file JReport.bat in the <designer_install_root>\bin folder.-Doracle.net.tns_admin=<directory_containing_tnsnames.ora>
-Doracle.net.wallet_location= "(SOURCE=(METHOD=FILE)(METHOD_DATA=(DIRECTORY=<directory_containing_wallet>)))

For example:

- Start Designer and connect to the Oracle database via the Oracle connection plug-in.

- Add the connection identifier name in the URL used for connecting to the Oracle database. You can then connect to the database without having to provide the user name and password.
