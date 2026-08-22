---
title: "Supported Report Databases"
id: 1500009568422
section: "Setting Up the Report Designing Environment - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568422-Supported-Report-Databases
updated_at: 2021-07-24T05:54:35Z
---

# Supported Report Databases

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568442-Logi-JReport-Licenses)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568482-Logi-JReport-Designer-on-Windows)

# Supported Report Databases

Logi JReport supports all of the current mainstream databases as well as most databases which support JDBC drivers. In addition to traditional databases, databases in the cloud are also supported, such as Vertica, Amazon RDS, and RedShift.

The following table lists the databases and JDBC drivers that have been tested with Logi JReport. If you are using any of the databases listed below, you are recommended to use the corresponding driver version with Logi JReport although any driver which the DBMS supplier recommends is also fine. If you encounter problems when using a database or driver version that is not listed here, you can contact Jinfonet Support ([support@jinfonet.com](mailto:support@jinfonet.com)) for help.

You can also refer to the page <http://wiki.netbeans.org/DatabasesAndDrivers> for additional information on databases and drivers.

| Database | Version | Driver File Name | JDBC Driver | Example URL |
| --- | --- | --- | --- | --- |
| Amazon RDS |  | mysql-connector-java-5.0.4-bin.jar | com.mysql.jdbc.Driver | jdbc:mysql://jrdbtest.c4fb8hiicidz.us-west-2.rds.amazonaws.com:3306/sampledb1110 (The URL is dynamically generated when you apply an instance.) |
| Cache | Cache 4 | CacheDB.jar | com.intersys.jdbc.CacheDriver | jdbc:Cache://<host>:1972/samples |
| DB2 | 10.5 | db2jcc.jar; db2jcc\_license\_cu.jar; db2jcc4.jar | com.ibm.db2.jcc.DB2Driver | jdbc:db2://<host>:50000/test |
| Derby | 10.10.1 | derbyclient.jar; derby.jar | org.apache.derby.jdbc.ClientDriver | jdbc:derby://<host>:1528/test |
| HIVE | 0.12.0 | hadoop-common-2.2.0.jar; hadoop-core-2.2.0.jar; hive-exec-0.12.0.jar; hive-jdbc-0.12.0.jar; hive-metastore-0.12.0.jar; hive-service-0.12.0.jar; libfb303-0.9.0.jar; libthrift-0.9.0.jar; slf4j-api-1.6.1.jar; slf4j-simple-1.6.1.jar | org.apache.hadoop.hive.jdbc.HiveDriver | jdbc:hive://<host>:10000 |
| Hortonworks | 0.14.0 | hive-jdbc-0.14.0-standalone.jar; hadoop-common-2.6.0.jar | org.apache.hive.jdbc.HiveDriver | jdbc:hive2://<host>:10000/default;auth=noSasl |
| HSQL | 2.3.4 | hsqldb.jar | org.hsqldb.jdbcDriver | jdbc:hsqldb:D:\Logi JReport\Demo\db\SampleDB |
| Informix | 12.10 | ifxjdbc.jar | com.informix.jdbc.IfxDriver | jdbc:informix-sqli://<host>:9088/demo:INFORMIXSERVER=ol\_informix1170 |
| MariaDB | 10.0.2 | mariadb-java-client-1.5.2.jar | org.mariadb.jdbc.Driver | jdbc:mariadb://<host>:3306/database |
| MemSQL | 5.5.8 | mysql-connector-java-5.1.25-bin.jar; mysql-connector-java-5.1.7-bin.jar | com.mysql.jdbc.Driver | jdbc:mysql://<host>:3306/test |
| MongoDB | 3.2.2 | already within Logi JReport | toolkit.db.mongo.MongoDriver | host, port, databaseName:demo |
|  |  |  |  |  |
| MySQL | 5.6.15 | mysql-connector-java-5.1.29-bin.jar | com.mysql.jdbc.Driver | jdbc:mysql://<host>:3306/test |
| Oracle | 12c release1 | ojdbc7.jar | oracle.jdbc.driver.OracleDriver | jdbc:oracle:thin:@<host>:1521:orcl (Oracle JDBC Thin using an SID) |
| PostGreSQL | 9.6 | postgresql-42.0.0.jar | org.postgresql.Driver | jdbc:postgresql://<host>:5432/postgres |
| PSQL | V11 SP3 | jpscs.jar; pvjdbc2.dll; pvjdbc2.jar; pvjdbc2x.jar | com.pervasive.jdbc.v2.Driver | jdbc:pervasive://<host>:1583/test |
| RedBrick warehouse |  | redbrick.jar | redbrick.jdbc.RBWDriver | jdbc:rbw:protocol:<host>:5050/test/ |
| RedShift |  | postgresql-8.4-703.jdbc4.jar | org.postgresql.Driver | jdbc:postgresql://jinfonet-rsdw-demo.cfcn5ogc14yr.us-east-1.redshift.amazonaws.com:5439/sampledb (The URL is dynamically generated when you apply an instance.) |
| ScaleDB | 0.2.3 | mysql-connector-java-5.1.25-bin.jar; mysql-connector-java-5.1.7-bin.jar | com.mysql.jdbc.Driver | jdbc:mysql://<host>:3306/test |
| SQL Server | 2016 | sqljdbc4.jar; sqljdbc41.jar; sqljdbc42.jar | com.microsoft.sqlserver.jdbc.SQLServerDriver | jdbc:sqlserver://<host>:1433;DatabaseName=test |
| Sybase | 15.7 | jconn3.jar | com.sybase.jdbc2.jdbc.SybDriver | jdbc:sybase:Tds:<host>:5000/master |
| Sybase IQ | 15.4.0.3019 | jconn3.jar; jconn4.jar | com.sybase.jdbc3.jdbc.SybDriver | jdbc:sybase:Tds:<host>:2638/iqdemo |
| Vertica | 7.0.1 | vertica-jdbc-7.0.1-0.jar | com.vertica.jdbc.Driver | jdbc:vertica://<host>:5433/vmartdb |

**Notes:**

* If you want to use the DB2 app connection, you need to install the client and configure the net address first.
* The database MySql with the example URL `jdbc:mysql://db06:3306/test?p?useSSL=true?clientCertificateKeyStoreUrl=D:\test\SSL_Client\ca-cert.pem?clientCertificateKeyStorePassword=1234` is connected by SSL. For how to install SSL, refer to <http://www.openssl.org>. For how to configure MySql for SSL, refer to <http://dev.mysql.com/doc/refman/5.1/en/ssl-connections.html>. For more information about JDBC driver, refer to <http://dev.mysql.com/doc/connector-j/en/connector-j-reference-configuration-properties.html>.
* For Oracle JDBC Thin using a TNSName, you need to configure the tnsname first, then add the parameter `-Doracle.net.tns_admin=<designer_install_root>\lib` into the file Logi JReport.bat which is located in `<designer_install_root>\bin`, assuming you have copied the file tnsnames.ora from your Oracle server to `<designer_install_root>\lib`.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568442-Logi-JReport-Licenses)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568482-Logi-JReport-Designer-on-Windows)
