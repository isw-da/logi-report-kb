---
title: "JSON/Elasticsearch Connection Properties"
id: 1500010061422
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010061422-JSON-Elasticsearch-Connection-Properties
updated_at: 2021-07-23T19:16:22Z
---

# JSON/Elasticsearch Connection Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099961-JDBC-Hive-Connection-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061442-JSON-Elasticsearch-Schema-Properties)

# JSON/Elasticsearch Connection Properties

This topic lists the properties of a JSON/Elasticsearch Connection object in a catalog.

| Property Name | Description |
| --- | --- |
| Default | Specifies whether the connection is the default connection in the current data source. By default, the first added connection in a data source is the default connection of the data source. A data source can have zero or one default connection. Data type: Boolean |
| Description | Specifies the description of the connection. Data type: String |
| Name | Specifies the name of the connection. If the name has already been used, a number starting from 1 will be appended to the name. For example, if aa exists, the new name will be aa1, and if both aa and aa1 exits, it will be aa2, and so on. If you change the name, the imported SQL and stored procedures that reference the connection will be automatically updated to use the new name. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099961-JDBC-Hive-Connection-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061442-JSON-Elasticsearch-Schema-Properties)
