---
title: "Initializing the Database System as a Non-admin Database User"
id: 1500009644502
section: "Configuring Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644502-Initializing-the-Database-System-as-a-Non-admin-Database-User
updated_at: 2021-07-24T20:55:20Z
---

# Initializing the Database System as a Non-admin Database User

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669121-Specifying-Schemas)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644462-Configuring-JdbcDriversConfig-properties)

# Initializing the Database System as a Non-Admin Database User

Logi JReport Server needs to connect to a server database and fetch and write data from the database tables at runtime. Database initialization is to create the required tables in the database. Usually, Logi JReport Server automatically creates database tables the first time it is started. The database information that Logi JReport Server uses is defined in the dbconfig.xml file. However, if the user ID defined in this file does not have the permission to create tables in the database, Logi JReport Server will fail to complete the operation. In this case, you will need another user, such as the database administrator (who holds the relevant permissions), to create a set of empty tables in the user's schema using the provided SQL files in `<install_root>\script_files`.

In the case when a database administrator (DBA) does not want to assign an admin database user to Logi JReport Server for connecting to the server database, Logi JReport has to use a non-admin database user to initialize the database system. The database initialization will then have to be divided into three phases:

1. The DBA creates new database tables using script files stored in `<install_root>\script_files\create_new_tables`.
2. Customer starts Logi JReport Server by using non-admin database user. In this phase, the data in the old version's database tables if they exist will be migrated to the new tables created in the first step. If the data migration happens, you will be able to see a record of it in the debug file.
3. The DBA deletes the old version' tables in the database using script files stored in `<install_root>\script_files\delete_old_tables`.

If it is a newly installed Logi JReport Server connecting to a database that does not already contain the required tables, only the first step is required.

The following table lists the script files used for different purposes:

|  |  |
| --- | --- |
| **File** | **Description** |
| **Script files used for creating new database tables**  (stored in `<install_root>\script_files\create_new_tables`): | |
| db2\_c.txt | Creates new tables for DB2 database. |
| derby\_c.txt | Creates new tables for Derby database. |
| hsqldb\_c.txt | Creates new tables for HSQLDB database. |
| informix\_c.txt | Creates new tables for Informix database. |
| mysql\_c.txt | Creates new tables for MySQL database (for single-byte charset, e.g. latin1). |
| sybase\_dc.txt | Deletes current version tables for Sybase database. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669121-Specifying-Schemas)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644462-Configuring-JdbcDriversConfig-properties)
