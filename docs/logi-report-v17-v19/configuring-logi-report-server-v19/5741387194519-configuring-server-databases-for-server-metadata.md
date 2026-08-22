---
title: "Configuring Server Databases for Server Metadata"
id: 5741387194519
section: "Configuring Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741387194519-Configuring-Server-Databases-for-Server-Metadata
updated_at: 2022-10-31T17:18:48Z
---

# Configuring Server Databases for Server Metadata

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741364328215-Configuring-Server-v19)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741415979543-Configuring-Server-Databases-for-Server-Metadata-in-a-Standalone-Environment)

# Configuring Server Databases for Server Metadata

Logi Report Server needs to read and write to a DBMS system to store metadata information about the server and the reports and report versions. This topic describes the ways of accessing a DBMS via JDBC and via JNDI and the three logical databases in Logi Report Server: system, realm, and profiling.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)This topic is for metadata. If you want to look for reporting databases, see [Supported Report Databases](https://devnet.logianalytics.com/hc/en-us/articles/5735568258711-Supported-Report-Databases) in the *Logi Report Designer Guide*.

By default, Logi Report embeds the 100% Java Apache Derby DBMS only for testing and evaluation purposes. You can easily change it to your preferred DBMS. We have tested the following databases and you can use them as the server database: Apache Derby, HSQLDB, MySQL, SQL Server, IBM DB2, Oracle, Sybase, PostgreSQL, Informix, MariaDB, InterSystems IRIS, InterSystems Caché, and EnterpriseDB (EDB).

Logi Report Server supports connecting a DBMS to access its system data via JDBC. You can find the JDBC configuration information in the file **dbconfig.xml** in `<install_root>\bin`, and use the file to configure a database connection. When Logi Report Server runs in an integrated environment, you can also access a DBMS via JNDI.

There are three logical databases in Logi Report Server: system, realm, and profiling. The system database holds resources of the global server scope, such as server.properties and global NLS. The realm database holds information of folders, nodes, versions, the security system, and the completed table. The profiling database holds server runtime related information. The system and realm databases are necessary in order to run Logi Report Server. The profiling tables are optional. In most cases you can use the same physical database for all three sets of tables.

Logi Report also provides completed SQL files to create tables for all databases supported. They reside in `<install_root>\script_files`.

Select the following links to view the topics:

* [Configuring Server Databases for Server Metadata in a Standalone Environment](https://devnet.logianalytics.com/hc/en-us/articles/5741415979543-Configuring-Server-Databases-for-Server-Metadata-in-a-Standalone-Environment)
* [Configuring Server Databases for Server Metadata in an Integrated Environment](https://devnet.logianalytics.com/hc/en-us/articles/5741395898263-Configuring-Server-Databases-for-Server-Metadata-in-an-Integrated-Environment)
* [Creating Tables in a Specified Tablespace](https://devnet.logianalytics.com/hc/en-us/articles/5741387307799-Creating-Tables-in-a-Specified-Tablespace)
* [Initializing the Database System as a Non-admin Database User](https://devnet.logianalytics.com/hc/en-us/articles/5741387264663-Initializing-the-Database-System-as-a-Non-admin-Database-User)
* [Specifying DBMS Schemas](https://devnet.logianalytics.com/hc/en-us/articles/5741395949719-Specifying-DBMS-Schemas)

See also [Managing Server Data](https://devnet.logianalytics.com/hc/en-us/articles/5741448346007-Managing-Server-Data) for information about working with the data in the server databases.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* ODBC is not supported.
* If you are using MySQL, make sure it is of version 5 or above; for Sybase, the driver should be of version jConnect 7.0.7 or above.
* When using Microsoft SQL Server 2000 as the server database, the driver should be jtds.jar, otherwise the Schedule feature cannot work.
* If your server database uses DB2 and the charset is DBK, you will get the exception of encoding not supported.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741364328215-Configuring-Server-v19)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741415979543-Configuring-Server-Databases-for-Server-Metadata-in-a-Standalone-Environment)
