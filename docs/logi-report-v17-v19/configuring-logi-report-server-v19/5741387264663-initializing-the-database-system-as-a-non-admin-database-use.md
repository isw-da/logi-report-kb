---
title: "Initializing the Database System as a Non-admin Database User"
id: 5741387264663
section: "Configuring Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741387264663-Initializing-the-Database-System-as-a-Non-admin-Database-User
updated_at: 2022-10-31T17:15:58Z
---

# Initializing the Database System as a Non-admin Database User

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741395949719-Specifying-DBMS-Schemas)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741409467031-Configuring-the-Server-Service)

# Initializing the Database System as a Non-admin Database User

Logi Report Server needs to connect to a server database and fetch and write data from the database tables at runtime. Database initialization is to create the required tables in the database. This topic describes the procedure for a non-admin database user to initialize the database system and the script files for creating and deleting database tables.

Usually, Logi Report Server automatically creates database tables the first time it starts. However, if the user ID you define in the **dbconfig.xml** file does not have the permission to create tables in the database, Logi Report Server will fail to complete the operation. In this case, you will need another user, such as the database administrator who has the relevant permissions, to create a set of empty tables in the user's schema using the SQL files in `<install_root>\script_files`.

When the database administrator (DBA) does not want to assign an admin database user to Logi Report Server for connecting to the database, Logi Report has to use a non-admin database user to initialize the database system. The database initialization will then have to be divided into three phases:

1. The DBA creates new database tables using script files in `<install_root>\script_files\create_new_tables`.

   If it is a newly installed Logi Report Server connecting to a database that does not already contain the required tables, only the first step is required.
2. Customer starts Logi Report Server using a non-admin database user. In this phase, the data in the old version's database tables if they exist will be migrated to the new tables created in the first step. If the data migration happens, you will be able to see a record of it in the debug file.
3. The DBA deletes tables of the old version in the database using script files in `<install_root>\script_files\delete_old_tables`.

The following table lists the script files for different purposes:

| **File Name** | **Description** |
| --- | --- |
| **Script files for creating new database tables** (in `<install_root>\script_files\create_new_tables`): | |
| cachedb\_c.txt | Create new tables for InterSystems Caché database. |
| db2\_c.txt | Create new tables for DB2 database. |
| derby\_c.txt | Create new tables for Derby database. |
| hsqldb\_c.txt | Create new tables for HSQLDB database. |
| informix\_c.txt | Create new tables for Informix database. |
| mysql\_c.txt | Create new tables for MySQL database (for single-byte charset, like latin1). |
| mysql\_mb2\_c.txt | Create new tables for MySQL database (for MBCS two-byte charset, for example, gbk). |
| mysql\_mb3\_c.txt | Create new tables for MySQL database (for MBCS three-byte charset, for example, utf8). |
| oracle\_c.txt | Create new tables for Oracle database. |
| postgresql\_c.txt | Create new tables for PostgreSQL/EnterpriseDB database. |
| sqlserver\_c.txt | Create new tables for Microsoft SQL Server database. |
| sybase\_c.txt | Create new tables for Sybase database. |
| **Script files for deleting the old version tables** (in `<install_root>\script_files\delete_old_tables`): | |
| cachedb\_do.txt | Delete old version tables for InterSystems Caché database. |
| db2\_do.txt | Delete old version tables for DB2 database. |
| derby\_do.txt | Delete old version tables for Derby database. |
| hsqldb\_do.txt | Delete old version tables for HSQLDB database. |
| informix\_do.txt | Delete old version tables for Informix database. |
| mysql\_do.txt | Delete old version tables for MySQL database. |
| oracle\_do.txt | Delete old version tables for Oracle database. |
| postgresql\_do.txt | Delete old version tables for PostgreSQL/EnterpriseDB database. |
| sqlserver\_do.txt | Delete old version tables for Microsoft SQL Server database. |
| sybase\_do.txt | Delete old version tables for Sybase database. |
| **Script files for deleting the current version tables** (in `<install_root>\script_files\delete_current_tables`): | |
| cachedb\_dc.txt | Delete current version tables for InterSystems Caché database. |
| db2\_dc.txt | Delete current version tables for DB2 database. |
| derby\_dc.txt | Delete current version tables for Derby database. |
| hsqldb\_dc.txt | Delete current version tables for HSQLDB database. |
| informix\_dc.txt | Delete current version tables for Informix database. |
| mysql\_dc.txt | Delete current version tables for MySQL database. |
| oracle\_dc.txt | Delete current version tables for Oracle database. |
| postgresql\_dc.txt | Delete current version tables for PostgreSQL/EnterpriseDB database. |
| sqlserver\_dc.txt | Delete current version tables for Microsoft SQL Server database. |
| sybase\_dc.txt | Delete current version tables for Sybase database. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741395949719-Specifying-DBMS-Schemas)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741409467031-Configuring-the-Server-Service)
