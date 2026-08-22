---
title: "Configuring Server Databases for Server Metadata"
id: 45203864140301
section: "Configuring Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203864140301-Configuring-Server-Databases-for-Server-Metadata
updated_at: 2026-04-30T14:08:00Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Configuring Server Databases for Server Metadata

Report Server needs to read and write to a DBMS system to store metadata information about the server and the reports and report versions. This topic describes the ways of accessing a DBMS via JDBC and via JNDI and the three logical databases in Report Server: system, realm, and profiling. 

This topic is for metadata. If you want to look for reporting databases, see Supported Report Databases in the Report Designer Guide.

By default, Report embeds the 100% Java Apache Derby DBMS only for testing and evaluation purposes. You can easily change it to your preferred DBMS. We have tested the following databases and you can use them as the server database: Apache Derby, HSQLDB, MySQL, SQL Server, IBM DB2, Oracle, Sybase, PostgreSQL, Informix, MariaDB, InterSystems IRIS, InterSystems Caché, and EnterpriseDB (EDB).

Report Server supports connecting a DBMS to access its system data via JDBC. You can find the JDBC configuration information in the file dbconfig.xml in <install_root>\bin, and use the file to configure a database connection. When Report Server runs in an integrated environment, you can also access a DBMS via JNDI.

There are three logical databases in Report Server: system, realm, and profiling. The system database holds resources of the global server scope, such as server.properties and global NLS. The realm database holds information of folders, nodes, versions, the security system, and the completed table. The profiling database holds server runtime related information. The system and realm databases are necessary in order to run Report Server. The profiling tables are optional. In most cases you can use the same physical database for all three sets of tables.

Report also provides completed SQL files to create tables for all databases supported. They reside in <install_root>\script_files.

Select the following links to view the topics:

- Configuring Server Databases for Server Metadata in a Standalone Environment

- Configuring Server Databases for Server Metadata in an Integrated Environment

- Creating Tables in a Specified Tablespace

- Initializing the Database System as a Non-admin Database User

- Specifying DBMS Schemas

See also Managing Server Data for information about working with the data in the server databases.

- ODBC is not supported.

- If you are using MySQL, make sure it is of version 5 or above; for Sybase, the driver should be of version jConnect 7.0.7 or above.

- When using Microsoft SQL Server 2000 as the server database, the driver should be jtds.jar, otherwise the Schedule feature cannot work.

- If your server database uses DB2 and the charset is DBK, you will get the exception of encoding not supported.
