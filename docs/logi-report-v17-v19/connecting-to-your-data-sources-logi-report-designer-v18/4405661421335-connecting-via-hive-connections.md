---
title: "Connecting via Hive Connections"
id: 4405661421335
section: "Connecting to Your Data Sources - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661421335-Connecting-via-Hive-Connections
updated_at: 2022-01-27T20:34:38Z
---

# Connecting via Hive Connections

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664418583-Using-Imported-APEs)  [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661418007-Connecting-via-Elasticsearch-Connections)

# Connecting via Hive Connections

This topic introduces Hive connections and lists the libraries you need to provide when using Hive connections in Designer.

A Hive connection functions the same as a [JDBC connection](https://devnet.logianalytics.com/hc/en-us/articles/4405664412311-Connecting-via-JDBC-Connections). It supplies the JDBC driver and metadata information which are the same as JDBC. However, it expands many native functions to support non-SQL and huge data that JDBC does not support.

To set up Hive connections in Designer, you need to add the corresponding Hive database drivers to `<designer_install_root>\lib`, or append the archive files of the drivers to the ADDCLASSPATH variable in the file setenv.bat in `<designer_install_root>\bin`. The following lists the libraries that support Hive 0.12.0. If you use higher Hive versions, you can replace them with new jars.

* hadoop-common-2.2.0.jar
* hadoop-core-2.2.0.jar
* hive-exec-0.12.0.jar
* hive-jdbc-0.12.0.jar
* hive-metastore-0.12.0.jar
* hive-service-0.12.0.jar
* libfb303-0.9.0.jar
* libthrift-0.9.0.jar
* slf4j-api-1.7.25.jar
* slf4j-simple-1.6.1.jar

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661433495-Connecting-via-MongoDB-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661418007-Connecting-via-Elasticsearch-Connections)
