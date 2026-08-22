---
title: "HIVE Connections"
id: 1500009584781
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584781-HIVE-Connections
updated_at: 2021-07-24T05:55:50Z
---

# HIVE Connections

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585181-Managing-Schemas-in-a-MongoDB-Connection)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585081-JSON-Connections)

# HIVE Connections

However, it expands many native funThe HIVE connection functions the same as a [JDBC connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009563982-JDBC-Connections). It supplies the JDBC driver and metadata information which are the same as JDBC. ctions to support non SQL and huge data that are not supported by JDBC. The libraries that support HIVE 0.12.0 are listed as below. You can add them in `<install_root>\lib` when needed:

* hadoop-common-2.2.0.jar
* hadoop-core-2.2.0.jar
* hive-exec-0.12.0.jar
* hive-jdbc-0.12.0.jar
* hive-metastore-0.12.0.jar
* hive-service-0.12.0.jar
* libfb303-0.9.0.jar
* libthrift-0.9.0.jar
* slf4j-api-1.6.1.jar
* slf4j-simple-1.6.1.jar

If you use higher HIVE versions, you can replace the libraries with new jars.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585181-Managing-Schemas-in-a-MongoDB-Connection)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585081-JSON-Connections)
