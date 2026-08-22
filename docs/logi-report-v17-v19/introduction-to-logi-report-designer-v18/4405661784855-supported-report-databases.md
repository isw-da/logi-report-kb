---
title: "Supported Report Databases"
id: 4405661784855
section: "Introduction to Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661784855-Supported-Report-Databases
updated_at: 2022-01-27T20:38:23Z
---

# Supported Report Databases

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661785879-System-Requirements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661768087-Installing-and-Running-Designer)

# Supported Report Databases

Logi Report supports all of the current mainstream databases and most databases which support JDBC drivers. In addition to traditional databases, Logi Report also supports databases in the cloud, such as Vertica, Amazon RDS, and RedShift. This topic introduces the databases and JDBC drivers that have been tested with Logi Report.

You should use the corresponding driver version with Logi Report when you are using any of the databases in the following table, although any driver which the DBMS supplier recommends is also fine. You can also select the link: <http://wiki.netbeans.org/DatabasesAndDrivers> for additional information on databases and drivers. If you need more information, contact [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.).

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4420542088087/criticalicon.gif) In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: [Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751).

| Database | Version | JDBC Driver | Driver File Name |
| --- | --- | --- | --- |
| Amazon RDS |  | com.mysql.jdbc.Driver | mysql-connector-java-5.0.4-bin.jar |
| Cache | Cache 4 | com.intersys.jdbc.CacheDriver | CacheDB.jar |
| DB2 | 10.5 | com.ibm.db2.jcc.DB2Driver | db2jcc.jar; db2jcc\_license\_cu.jar; db2jcc4.jar |
| Derby | 10.14.2.0 | org.apache.derby.jdbc.ClientDriver | derby.jar (already contained in Logi Report); derbyclient.jar |
| Hive | 0.12.0 | org.apache.hadoop.hive.jdbc.HiveDriver | hadoop-common-2.2.0.jar; hadoop-core-2.2.0.jar; hive-exec-0.12.0.jar; hive-jdbc-0.12.0.jar; hive-metastore-0.12.0.jar; hive-service-0.12.0.jar; libfb303-0.9.0.jar; libthrift-0.9.0.jar; slf4j-api-1.7.25.jar; slf4j-simple-1.6.1.jar |
| Hortonworks | 0.14.0 | org.apache.hive.jdbc.HiveDriver | hive-jdbc-0.14.0-standalone.jar; hadoop-common-2.6.0.jar |
| HSQL | This image notes any new content for version 18.3 of the product. For more information please see the Release Notes or Enhancements topics.2.6.1 | org.hsqldb.jdbcDriver | hsqldb-2.6.1.jar (already contained in Logi Report) |
| Informix | 12.10 | com.informix.jdbc.IfxDriver | ifxjdbc.jar |
| InterSystems IRIS | 2020.1.0.215 | com.intersystems.jdbc.IRISDriver | intersystems-jdbc-3.1.0.jar |
| MariaDB | 10.0.2 | org.mariadb.jdbc.Driver | mariadb-java-client-1.5.2.jar |
| MemSQL | 5.5.8 | com.mysql.jdbc.Driver | mysql-connector-java-5.1.25-bin.jar; mysql-connector-java-5.1.7-bin.jar |
| MongoDB | This image notes any new content for version 18.3 of the product. For more information please see the Release Notes or Enhancements topics.4.3.0 | toolkit.db.mongo.MongoDriver | mongodb-driver-sync-4.3.0.jar, mongodb-driver-core-4.3.0.jar, bson-4.3.0.jar, log4j-slf4j-impl-2.17.1.jar, and slf4j-api-1.7.32.jar (already contained in Logi Report) |
| MySQL | 5.6.15 | com.mysql.jdbc.Driver | mysql-connector-java-5.1.29-bin.jar |
| Oracle | 12c release1 | oracle.jdbc.driver.OracleDriver | ojdbc7.jar |
| PostgreSQL | This image notes any new content for version 18.3 of the product. For more information please see the Release Notes or Enhancements topics.12 | org.postgresql.Driver | postgresql-42.2.20.jar |
| PSQL | V11 SP3 | com.pervasive.jdbc.v2.Driver | jpscs.jar; pvjdbc2.dll; pvjdbc2.jar; pvjdbc2x.jar |
| RedBrick warehouse |  | redbrick.jdbc.RBWDriver | redbrick.jar |
| RedShift |  | org.postgresql.Driver | postgresql-8.4-703.jdbc4.jar |
| ScaleDB | 0.2.3 | com.mysql.jdbc.Driver | mysql-connector-java-5.1.25-bin.jar; mysql-connector-java-5.1.7-bin.jar |
| SQL Server | 2019 | com.microsoft.sqlserver.jdbc.SQLServerDriver | mssql-jdbc-9.2.1.jre11.jar |
| Sybase | 15.7 | com.sybase.jdbc2.jdbc.SybDriver | jconn3.jar |
| Sybase IQ | 15.4.0.3019 | com.sybase.jdbc3.jdbc.SybDriver | jconn3.jar; jconn4.jar |
| Vertica | 7.0.1 | com.vertica.jdbc.Driver | vertica-jdbc-7.0.1-0.jar |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661785879-System-Requirements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661768087-Installing-and-Running-Designer)
