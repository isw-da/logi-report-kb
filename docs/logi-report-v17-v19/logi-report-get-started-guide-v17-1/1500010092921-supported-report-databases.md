---
title: "Supported Report Databases"
id: 1500010092921
section: "Logi Report Get Started Guide v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010092921-Supported-Report-Databases
updated_at: 2021-07-23T19:14:13Z
---

# Supported Report Databases

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404848811031/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010055922-Logi-Report-Licenses)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404848811287/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093041-Test-Server-Installation)

# Supported Report Databases

Logi Report supports all of the current mainstream databases as well as most databases which support JDBC drivers. In addition to traditional databases, Logi Report also supports databases in the cloud, such as Vertica, Amazon RDS, and RedShift.

The following table lists the databases and JDBC drivers that have been tested with Logi Report. If you are using any of the databases listed below, you are recommended to use the corresponding driver version with Logi Report although any driver which the DBMS supplier recommends is also fine. If you encounter problems when using a database or driver version that is not listed here, you can contact Logi Analytics Support at [support@logianalytics.com](mailto:support@logianalytics.com) for help.

You can also refer to <http://wiki.netbeans.org/DatabasesAndDrivers> for additional information on databases and drivers.

| Database | Version | JDBC Driver | Driver File Name |
| --- | --- | --- | --- |
| Amazon RDS |  | com.mysql.jdbc.Driver | mysql-connector-java-5.0.4-bin.jar |
| Cache | Cache 4 | com.intersys.jdbc.CacheDriver | CacheDB.jar |
| DB2 | 10.5 | com.ibm.db2.jcc.DB2Driver | db2jcc.jar; db2jcc\_license\_cu.jar; db2jcc4.jar |
| Derby | 10.14.2.0 | org.apache.derby.jdbc.ClientDriver | derby.jar (already contained in Logi Report); derbyclient.jar |
| Hive | 0.12.0 | org.apache.hadoop.hive.jdbc.HiveDriver | hadoop-common-2.2.0.jar; hadoop-core-2.2.0.jar; hive-exec-0.12.0.jar; hive-jdbc-0.12.0.jar; hive-metastore-0.12.0.jar; hive-service-0.12.0.jar; libfb303-0.9.0.jar; libthrift-0.9.0.jar; slf4j-api-1.7.25; slf4j-simple-1.6.1.jar |
| Hortonworks | 0.14.0 | org.apache.hive.jdbc.HiveDriver | hive-jdbc-0.14.0-standalone.jar; hadoop-common-2.6.0.jar |
| HSQL | 2.5.1 | org.hsqldb.jdbcDriver | hsqldb-2.5.1.jar (already contained in Logi Report) |
| Informix | 12.10 | com.informix.jdbc.IfxDriver | ifxjdbc.jar |
| InterSystems IRIS | 2020.1.0.215 | com.intersystems.jdbc.IRISDriver | intersystems-jdbc-3.1.0.jar |
| MariaDB | 10.0.2 | org.mariadb.jdbc.Driver | mariadb-java-client-1.5.2.jar |
| MemSQL | 5.5.8 | com.mysql.jdbc.Driver | mysql-connector-java-5.1.25-bin.jar; mysql-connector-java-5.1.7-bin.jar |
| MongoDB | 3.12.7 | toolkit.db.mongo.MongoDriver | mongo-java-driver-3.12.7.jar (already contained in Logi Report) |
| MySQL | 5.6.15 | com.mysql.jdbc.Driver | mysql-connector-java-5.1.29-bin.jar |
| Oracle | 12c release1 | oracle.jdbc.driver.OracleDriver | ojdbc7.jar |
| PostgreSQL | 9.6 | org.postgresql.Driver | postgresql-42.0.0.jar |
| PSQL | V11 SP3 | com.pervasive.jdbc.v2.Driver | jpscs.jar; pvjdbc2.dll; pvjdbc2.jar; pvjdbc2x.jar |
| RedBrick warehouse |  | redbrick.jdbc.RBWDriver | redbrick.jar |
| RedShift |  | org.postgresql.Driver | postgresql-8.4-703.jdbc4.jar |
| ScaleDB | 0.2.3 | com.mysql.jdbc.Driver | mysql-connector-java-5.1.25-bin.jar; mysql-connector-java-5.1.7-bin.jar |
| SQL Server | 2019 | com.microsoft.sqlserver.jdbc.SQLServerDriver | mssql-jdbc-9.2.1.jre11.jar |
| Sybase | 15.7 | com.sybase.jdbc2.jdbc.SybDriver | jconn3.jar |
| Sybase IQ | 15.4.0.3019 | com.sybase.jdbc3.jdbc.SybDriver | jconn3.jar; jconn4.jar |
| Vertica | 7.0.1 | com.vertica.jdbc.Driver | vertica-jdbc-7.0.1-0.jar |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404848811031/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010055922-Logi-Report-Licenses)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404848811287/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093041-Test-Server-Installation)
