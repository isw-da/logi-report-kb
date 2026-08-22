---
title: "Configuring the Server Database"
id: 1500009686662
section: "Configuring the Server Database"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009686662-Configuring-the-Server-Database
updated_at: 2021-11-03T06:58:26Z
---

# Configuring the Server Database

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686622-Configuring-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686682-Configuring-in-a-Standalone-Environment)

# Configuring the Server Database

Logi JReport Server needs to read and write to a DBMS system to store information about the server and the reports and report versions. By default the DBMS is the 100% Java Apache Derby DBMS embedded in Logi JReport, which is provided only for testing and evaluation purposes. It can be easily changed to your preferred DBMS. These databases have been tested as supported for the server database: Apache Derby, HSQLDB, MySQL, SQL Server, IBM DB2, Oracle, Sybase, PostgreSQL, Informix, MariaDB, InterSystems Caché and EnterpriseDB (EDB).

Logi JReport Server supports connecting a DBMS to access its system data via JDBC. The JDBC configuration information is stored in the file dbconfig.xml located in `<install_root>\bin`, which can be used for configuring a database connection too. When Logi JReport Server runs in an integrated environment, it can also access a DBMS via JNDI.

There are three logical databases in Logi JReport Server: system, realm, and profiling. The system database holds resources of the global server scope, such as server.properties, global NLS, and so on. The realm database holds information of folders, nodes, versions, the security system, and the completed table. The profiling database holds server runtime related information. The system and realm databases are necessary in order to run Logi JReport Server. The profiling tables are optional. In most cases you can use the same physical database for all 3 sets of tables.

Logi JReport also provides completed SQL files to create tables for all databases supported. They reside in `<install_root>\script_files`.

The following topics provide more information about configuration and the server database:

* [Configuring in a Standalone Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009686682-Configuring-in-a-Standalone-Environment)
* [Configuring in an Integrated Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009686702-Configuring-in-an-Integrated-Environment)
* [Creating Tables in a Specified Tablespace](https://devnet.logianalytics.com/hc/en-us/articles/1500009686742-Creating-Tables-in-a-Specified-Tablespace)
* [Initializing the Database System as a Non-admin Database User](https://devnet.logianalytics.com/hc/en-us/articles/1500009686722-Initializing-the-Database-System-as-a-Non-admin-Database-User)
* [Specifying Schemas](https://devnet.logianalytics.com/hc/en-us/articles/1500009712461-Specifying-Schemas)

See also [Managing Server Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009691342-Managing-Server-Data) for information about working with the data in the server databases.

**Notes:**

* ODBC is not supported.
* If you are using MySQL, make sure it is of version 5 or above; for Sybase, the driver should be of version jConnect 7.0.7 or above.
* When using Microsoft SQL Server 2000 as the server database, the driver should be jtds.jar, otherwise the Schedule feature cannot work.
* If your server database uses DB2 and the charset is DBK, there will be the exception of encoding not supported.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686622-Configuring-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686682-Configuring-in-a-Standalone-Environment)
