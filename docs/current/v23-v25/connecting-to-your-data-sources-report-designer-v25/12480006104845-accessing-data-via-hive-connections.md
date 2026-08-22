---
title: "Accessing Data via Hive Connections"
id: 12480006104845
section: "Connecting to Your Data Sources - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480006104845-Accessing-Data-via-Hive-Connections
updated_at: 2026-02-25T23:50:17Z
source_host: docs-report.zendesk.com
---
# Accessing Data via Hive Connections

This topic introduces Hive connections and lists the libraries you need to provide when using Hive connections in Designer.

A Hive connection functions the same as a JDBC connection. It supplies the JDBC driver and metadata information which are the same as JDBC. However, it expands many native functions to support non-SQL and huge data that JDBC does not support.

To set up Hive connections in Designer, you need to add the corresponding Hive database drivers to <designer_install_root>\lib, or append the archive files of the drivers to the ADDCLASSPATH variable of  setenv.bat in <designer_install_root>\bin. The following lists the libraries that support Hive 0.12.0. When you use later Hive versions, you can replace them with new jars.

- hadoop-common-2.2.0.jar 

- hadoop-core-2.2.0.jar

- hive-exec-0.12.0.jar

- hive-jdbc-0.12.0.jar

- hive-metastore-0.12.0.jar

- hive-service-0.12.0.jar

- libfb303-0.9.0.jar

- libthrift-0.9.0.jar

- slf4j-api-1.7.25.jar

- slf4j-simple-1.6.1.jar
