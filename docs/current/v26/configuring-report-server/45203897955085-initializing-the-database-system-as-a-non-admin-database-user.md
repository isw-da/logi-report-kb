---
title: "Initializing the Database System as a Non-admin Database User"
id: 45203897955085
section: "Configuring Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203897955085-Initializing-the-Database-System-as-a-Non-admin-Database-User
updated_at: 2026-04-30T14:08:01Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Initializing the Database System as a Non-admin Database User 

Report Server needs to connect to a server database and fetch and write data from the database tables at runtime. Database initialization is to create the required tables in the database. This topic describes the procedure for a non-admin database user to initialize the database system and the script files for creating and deleting database tables.

Usually, Report Server automatically creates database tables the first time it starts. However, if the user ID you define in the dbconfig.xml file does not have the permission to create tables in the database, Report Server will fail to complete the operation. In this case, you will need another user, such as the database administrator who has the relevant permissions, to create a set of empty tables in the user's schema using the SQL files in <install_root>\script_files. 

When the database administrator (DBA) does not want to assign an admin database user to Report Server for connecting to the database, Report has to use a non-admin database user to initialize the database system. The database initialization will then have to be divided into three phases:

- The DBA creates new database tables using script files in <install_root>\script_files\create_new_tables.
			

If it is a newly installed Report Server connecting to a database that does not already contain the required tables, only the first step is required.

- Customer starts Report Server using a non-admin database user. In this phase, the data in the old version's database tables if they exist will be migrated to the new tables created in the first step. If the data migration happens, you will be able to see a record of it in the debug file.

- The DBA deletes tables of the old version in the database using script files in <install_root>\script_files\delete_old_tables.

The following table lists the script files for different purposes: 

| File Name | Description |
| --- | --- |
| Script files for creating new database tables (in \script_files\create_new_tables): |  |
| cachedb_c.txt | Create new tables for InterSystems Caché database. |
| db2_c.txt | Create new tables for DB2 database. |
| derby_c.txt | Create new tables for Derby database. |
| hsqldb_c.txt | Create new tables for HSQLDB database. |
| informix_c.txt | Create new tables for Informix database. |
| mysql_c.txt | Create new tables for MySQL database (for single-byte charset, like latin1). |
| mysql_mb2_c.txt | Create new tables for MySQL database (for MBCS two-byte charset, for example, gbk). |
| mysql_mb3_c.txt | Create new tables for MySQL database (for MBCS three-byte charset, for example, utf8). |
| oracle_c.txt | Create new tables for Oracle database. |
| postgresql_c.txt | Create new tables for PostgreSQL/EnterpriseDB database. |
| sqlserver_c.txt | Create new tables for Microsoft SQL Server database. |
| sybase_c.txt | Create new tables for Sybase database. |
| Script files for deleting the old version tables (in \script_files\delete_old_tables): |  |
| cachedb_do.txt | Delete old version tables for InterSystems Caché database. |
| db2_do.txt | Delete old version tables for DB2 database. |
| derby_do.txt | Delete old version tables for Derby database. |
| hsqldb_do.txt | Delete old version tables for HSQLDB database. |
| informix_do.txt | Delete old version tables for Informix database. |
| mysql_do.txt | Delete old version tables for MySQL database. |
| oracle_do.txt | Delete old version tables for Oracle database. |
| postgresql_do.txt | Delete old version tables for PostgreSQL/EnterpriseDB database. |
| sqlserver_do.txt | Delete old version tables for Microsoft SQL Server database. |
| sybase_do.txt | Delete old version tables for Sybase database. |
| Script files for deleting the current version tables (in \script_files\delete_current_tables): |  |
| cachedb_dc.txt | Delete current version tables for InterSystems Caché database. |
| db2_dc.txt | Delete current version tables for DB2 database. |
| derby_dc.txt | Delete current version tables for Derby database. |
| hsqldb_dc.txt | Delete current version tables for HSQLDB database. |
| informix_dc.txt | Delete current version tables for Informix database. |
| mysql_dc.txt | Delete current version tables for MySQL database. |
| oracle_dc.txt | Delete current version tables for Oracle database. |
| postgresql_dc.txt | Delete current version tables for PostgreSQL/EnterpriseDB database. |
| sqlserver_dc.txt | Delete current version tables for Microsoft SQL Server database. |
| sybase_dc.txt | Delete current version tables for Sybase database. |
