---
title: "Supported Report Databases"
id: 12480268406029
section: "Introduction to Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480268406029-Supported-Report-Databases
updated_at: 2026-02-25T23:48:22Z
source_host: docs-report.zendesk.com
---
# Supported Report Databases

Report supports all of the current mainstream databases and most databases that support JDBC drivers. In addition to traditional databases, Report also supports databases in the cloud, such as Vertica, Amazon RDS, and RedShift. This topic introduces the databases and JDBC drivers that have been tested with Report.

You should use the corresponding driver version with Report when you are using any of the databases in the following table, although any driver that the database supplier recommends is also fine. You can also go to wiki.netbeans.org/DatabasesAndDrivers for additional information on databases and drivers. If you need more information, contact Customer Service.

 In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: Statement on Log4j and Log4Net Vulnerabilities.
    

| Database | Version | JDBC Driver | Driver File Name |
| --- | --- | --- | --- |
| Amazon RDS |  | com.mysql.jdbc.Driver | mysql-connector-java-5.0.4-bin.jar |
| Cache | Cache 4 or later | com.intersys.jdbc.CacheDriver | CacheDB.jar |
| DB2 | 10.5 or later | com.ibm.db2.jcc.DB2Driver | db2jcc.jar; db2jcc_license_cu.jar; db2jcc4.jar |
| Derby | 10.14.2.0 or later | org.apache.derby.jdbc.ClientDriver | derby.jar (already contained in Report); derbyclient.jar |
| Hive | 0.12.0 or later | org.apache.hadoop.hive.jdbc.HiveDriver | hadoop-common-2.2.0.jar; hadoop-core-2.2.0.jar; hive-exec-0.12.0.jar; hive-jdbc-0.12.0.jar; hive-metastore-0.12.0.jar; hive-service-0.12.0.jar; libfb303-0.9.0.jar; libthrift-0.9.0.jar; slf4j-api-1.7.25.jar; slf4j-simple-1.6.1.jar |
| Hortonworks | 0.14.0 or later | org.apache.hive.jdbc.HiveDriver | hive-jdbc-0.14.0-standalone.jar; hadoop-common-2.6.0.jar |
| HSQL | 2.6.1 or later | org.hsqldb.jdbcDriver | hsqldb-2.6.1.jar (already contained in Report) |
| Informix | 12.10 or later | com.informix.jdbc.IfxDriver | ifxjdbc.jar |
| InterSystems IRIS | 2020.1.0.215 or later | com.intersystems.jdbc.IRISDriver | intersystems-jdbc-3.1.0.jar |
| MariaDB | 10.0.2 or later | org.mariadb.jdbc.Driver | mariadb-java-client-1.5.2.jar |
| MemSQL | 5.5.8 or later | com.mysql.jdbc.Driver | mysql-connector-java-5.1.25-bin.jar; mysql-connector-java-5.1.7-bin.jar |
| MongoDB | 4.5.1 or later | toolkit.db.mongo.MongoDriver | mongodb-driver-sync-4.5.1.jar, mongodb-driver-core-4.5.1.jar, bson-4.5.1.jar, log4j-slf4j-impl-2.17.2.jar, and slf4j-api-1.7.36.jar (already contained in Report) |
| MySQL | 5.6.15 or later | com.mysql.jdbc.Driver | mysql-connector-java-5.1.29-bin.jar |
| Oracle | 12c release1 or later | oracle.jdbc.driver.OracleDriver | ojdbc7.jar |
| PostgreSQL | 12 or later | org.postgresql.Driver | postgresql-42.3.4.jar |
| PSQL | v11 SP3 or later | com.pervasive.jdbc.v2.Driver | jpscs.jar; pvjdbc2.dll; pvjdbc2.jar; pvjdbc2x.jar |
| RedBrick warehouse |  | redbrick.jdbc.RBWDriver | redbrick.jar |
| RedShift |  | org.postgresql.Driver | postgresql-8.4-703.jdbc4.jar |
| ScaleDB | 0.2.3 or later | com.mysql.jdbc.Driver | mysql-connector-java-5.1.25-bin.jar; mysql-connector-java-5.1.7-bin.jar |
| SQL Server | 2019 or later | com.microsoft.sqlserver.jdbc.SQLServerDriver | mssql-jdbc-9.2.1.jre11.jar |
| Sybase | 15.7 or later | com.sybase.jdbc2.jdbc.SybDriver | jconn3.jar |
| Sybase IQ | 15.4.0.3019 or later | com.sybase.jdbc3.jdbc.SybDriver | jconn3.jar; jconn4.jar |
| Vertica | 7.0.1 or later | com.vertica.jdbc.Driver | vertica-jdbc-7.0.1-0.jar |
