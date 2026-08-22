---
title: "Supported Report Databases"
id: 1500009690982
section: "Introduction to Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009690982-Supported-Report-Databases
updated_at: 2021-11-03T06:57:02Z
---

# Supported Report Databases

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691022-Logi-JReport-licenses)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009691102-Installing-Using-the-Installation-Wizard)

# Supported Report Databases

Logi JReport supports all of the current mainstream databases as well as most databases which support JDBC drivers. In addition to traditional databases, databases in the cloud are also supported, such as Vertica, Amazon RDS, and RedShift.

The following table lists the databases and JDBC drivers that have been tested with Logi JReport. If you are using any of the databases listed below, you are recommended to use the corresponding driver version with Logi JReport although any driver which the DBMS supplier recommends is also fine. If you encounter problems when using a database or driver version that is not listed here, you can [contact Logi Analytics Support](mailto:support@jinfonet.com) for help.

You can also refer to the page <http://wiki.netbeans.org/DatabasesAndDrivers> for additional information on databases and drivers.

| Database | Version | JDBC Driver | Driver File Name |
| --- | --- | --- | --- |
| Amazon RDS |  | com.mysql.jdbc.Driver | mysql-connector-java-5.0.4-bin.jar |
| Cache | Cache 4 | com.intersys.jdbc.CacheDriver | CacheDB.jar |
| DB2 | 10.5 | com.ibm.db2.jcc.DB2Driver | db2jcc.jar; db2jcc\_license\_cu.jar; db2jcc4.jar |
| Derby | 10.10.1 | org.apache.derby.jdbc.ClientDriver | derby.jar (already contained in Logi JReport); derbyclient.jar |
| HIVE | 0.12.0 | org.apache.hadoop.hive.jdbc.HiveDriver | hadoop-common-2.2.0.jar; hadoop-core-2.2.0.jar; hive-exec-0.12.0.jar; hive-jdbc-0.12.0.jar; hive-metastore-0.12.0.jar; hive-service-0.12.0.jar; libfb303-0.9.0.jar; libthrift-0.9.0.jar; slf4j-api-1.7.25; slf4j-simple-1.6.1.jar |
| Hortonworks | 0.14.0 | org.apache.hive.jdbc.HiveDriver | hive-jdbc-0.14.0-standalone.jar; hadoop-common-2.6.0.jar |
| HSQL | 2.4.0 | org.hsqldb.jdbcDriver | hsqldb-2.4.0.jar (already contained in Logi JReport) |
| Informix | 12.10 | com.informix.jdbc.IfxDriver | ifxjdbc.jar |
| MariaDB | 10.0.2 | org.mariadb.jdbc.Driver | mariadb-java-client-1.5.2.jar |
| MemSQL | 5.5.8 | com.mysql.jdbc.Driver | mysql-connector-java-5.1.25-bin.jar; mysql-connector-java-5.1.7-bin.jar |
| MongoDB | 3.4 | toolkit.db.mongo.MongoDriver | mongo-java-driver-3.4.0.jar (already contained in Logi JReport) |
| SQL Server | 2016 | com.microsoft.sqlserver.jdbc.SQLServerDriver | sqljdbc4.jar; sqljdbc41.jar; sqljdbc42.jar |
| MySQL | 5.6.15 | com.mysql.jdbc.Driver | mysql-connector-java-5.1.29-bin.jar |
| Oracle | 12c release1 | oracle.jdbc.driver.OracleDriver | ojdbc7.jar |
| PostgreSQL | 9.6 | org.postgresql.Driver | postgresql-42.0.0.jar |
| PSQL | V11 SP3 | com.pervasive.jdbc.v2.Driver | jpscs.jar; pvjdbc2.dll; pvjdbc2.jar; pvjdbc2x.jar |
| RedBrick warehouse |  | redbrick.jdbc.RBWDriver | redbrick.jar |
| RedShift |  | org.postgresql.Driver | postgresql-8.4-703.jdbc4.jar |
| ScaleDB | 0.2.3 | com.mysql.jdbc.Driver | mysql-connector-java-5.1.25-bin.jar; mysql-connector-java-5.1.7-bin.jar |
| Sybase | 15.7 | com.sybase.jdbc2.jdbc.SybDriver | jconn3.jar |
| Sybase IQ | 15.4.0.3019 | com.sybase.jdbc3.jdbc.SybDriver | jconn3.jar; jconn4.jar |
| Vertica | 7.0.1 | com.vertica.jdbc.Driver | vertica-jdbc-7.0.1-0.jar |

**Notes:**

* If you want to use the DB2 app connection, you need to install the client and configure the net address first.
* The database MySql with the example URL `jdbc:mysql://db06:3306/test?p?useSSL=true?clientCertificateKeyStoreUrl=D:\test\SSL_Client\ca-cert.pem?clientCertificateKeyStorePassword=1234` is connected by SSL. For how to install SSL, refer to <http://www.openssl.org>. For how to configure MySql for SSL, refer to <https://dev.mysql.com/doc/connector-j/en/connector-j-reference-using-ssl.html>. For more information about JDBC driver, refer to <http://dev.mysql.com/doc/connector-j/en/connector-j-reference-configuration-properties.html>.
* For Oracle JDBC Thin using a TNSName, you need to configure the tnsname first, then add the parameter `-Doracle.net.tns_admin=<designer_install_root>\lib` into the file Logi JReport.bat which is located in `<designer_install_root>\bin`, assuming you have copied the file tnsnames.ora from your Oracle server to `<designer_install_root>\lib`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691022-Logi-JReport-licenses)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009691102-Installing-Using-the-Installation-Wizard)
