---
title: "Hive Connections"
id: 1500009606762
section: "Connecting to Your Data Sources - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009606762-Hive-Connections
updated_at: 2021-07-24T16:05:08Z
---

# Hive Connections

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606942-Imported-APEs) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629481-Elasticsearch-Connections-)

# Hive Connections

A Hive connection functions the same as a [JDBC connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009629541-JDBC-Connections). It supplies the JDBC driver and metadata information which are the same as JDBC. However, it expands many native functions to support non SQL and huge data that are not supported by JDBC.

To set up Hive connections in Logi Report Designer, you need to add the corresponding Hive database drivers to `<designer_install_root>\lib`, or append the archive files of the drivers to the ADDCLASSPATH variable in the file setenv.bat in `<designer_install_root>\bin`. The libraries that support Hive 0.12.0 are listed as below. If you use higher Hive versions, you can replace them with new jars.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629601-MongoDB-Connections) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629481-Elasticsearch-Connections-)
