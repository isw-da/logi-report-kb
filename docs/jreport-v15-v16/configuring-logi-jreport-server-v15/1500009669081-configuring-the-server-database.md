---
title: "Configuring the Server Database"
id: 1500009669081
section: "Configuring Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009669081-Configuring-the-Server-Database
updated_at: 2021-07-24T20:55:21Z
---

# Configuring the Server Database

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644382-Configuring-Logi-JReport-Server-Guide-v15-Server)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669101-Configuring-in-a-Standalone-Environment)

# Configuring the Server Database

Logi JReport Server needs to read and write to a DBMS system to store information about the server and the reports and report versions. By default the DBMS is the 100% Java Apache Derby DBMS embedded in Logi JReport, which is provided only for testing and evaluation purposes. It can easily be changed to use your preferred DBMS. These databases have been tested as supported for the server database: Apache Derby, HSQLDB, MySQL, Microsoft SQL Server, IBM DB2, Oracle, Sybase, PostgreSQL, and Informix.

There are three logical databases in Logi JReport Server: system, realm, and profiling. The system database holds resources of the global server scope, such as server.properties, global NLS, and so on. The realm database holds information of folders, nodes, versions, the security system, and the completed table. The profiling database holds server runtime related information. The system and realm databases are necessary in order to run Logi JReport Server. The profiling tables are optional. In most cases you can use the same physical database for all 3 sets of tables.

When you install Logi JReport Server, a dbconfig.xml file is automatically created in the directory `<install_root>\bin`. The database configuration information is stored in this configuration file. You can also configure your database by using the dbconfig.xml file.

This section presents the ways of configuring the server database as follows:

* [Configuring in a Standalone Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009669101-Configuring-in-a-Standalone-Environment)
* [Configuring in an Integrated Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009644482-Configuring-in-an-Integrated-Environment)
* [Creating Tables in a Specified Tablespace](https://devnet.logianalytics.com/hc/en-us/articles/1500009669141-Creating-Tables-in-a-Specified-Tablespace)
* [Specifying Schemas](https://devnet.logianalytics.com/hc/en-us/articles/1500009669121-Specifying-Schemas)
* [Initializing the Database System as a Non-Admin Database User](https://devnet.logianalytics.com/hc/en-us/articles/1500009644502-Initializing-the-Database-System-as-a-Non-admin-Database-User)
* [Configuring JdbcDriversConfig.properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009644462-Configuring-JdbcDriversConfig-properties)

See also [Managing Server Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009648722-Managing-Server-Data) for information about working with the data in the server databases.

**Notes:**

* If you are using MySQL, make sure it is of version 5 or above.
* If your server database uses DB2 and the charset is DBK, there will be the exception of encoding not supported.
* When using Microsoft SQL 2000 as the server database, the driver should use jtds.jar, otherwise the scheduling feature cannot work.
* If you are using Sybase, make sure the driver is of version jConnect 7.0.7 or above.
* ODBC is not supported.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644382-Configuring-Logi-JReport-Server-Guide-v15-Server)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669101-Configuring-in-a-Standalone-Environment)
