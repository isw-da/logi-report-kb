---
title: "Accessing Data via Hive Connections"
id: 5735499410327
section: "Connecting to Your Data Sources - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735499410327-Accessing-Data-via-Hive-Connections
updated_at: 2022-11-02T04:28:57Z
---

# Accessing Data via Hive Connections

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735512889367-Using-Imported-APEs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735564552471-Accessing-Data-via-Elasticsearch-Connections)

# Accessing Data via Hive Connections

This topic introduces Hive connections and lists the libraries you need to provide when using Hive connections in Designer.

A Hive connection functions the same as a [JDBC connection](https://devnet.logianalytics.com/hc/en-us/articles/5735507700887-Accessing-Data-via-JDBC-Connections). It supplies the JDBC driver and metadata information which are the same as JDBC. However, it expands many native functions to support non-SQL and huge data that JDBC does not support.

To set up Hive connections in Designer, you need to add the corresponding Hive database drivers to `<designer_install_root>\lib`, or append the archive files of the drivers to the ADDCLASSPATH variable of setenv.bat in `<designer_install_root>\bin`. The following lists the libraries that support Hive 0.12.0. When you use later Hive versions, you can replace them with new jars.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735564769943-Accessing-Data-via-MongoDB-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735564552471-Accessing-Data-via-Elasticsearch-Connections)
