---
title: "JSON Connection Properties"
id: 1500009568822
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568822-JSON-Connection-Properties
updated_at: 2021-07-24T05:54:25Z
---

# JSON Connection Properties

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590441-JDBC-HIVE-Connection-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568842-JSON-Schema-Properties)

# JSON Connection Properties

A JSON connection has the following child object: [JSON Schema](https://devnet.logianalytics.com/hc/en-us/articles/1500009568842-JSON-Schema-Properties).

The properties of a JSON connection are as follows:

| Property Name | Description |
| --- | --- |
| Default | Specifies whether the connection is the default connection in the current data source. By default, the first added connection in a data source is the default connection of the data source. A data source can have zero or one default connection. Data type: Boolean |
| Description | Specifies the description of the connection. Data type: String |
| Name | Specifies the name of the connection. If the name has already been used, a number starting from 1 will be appended to the name. For example, if aa exists, the new name will be aa1, and if both aa and aa1 exits, it will be aa2, and so on. If you change the name, the imported SQL and stored procedures that reference the connection will be automatically updated to use the new name. Data type: String |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590441-JDBC-HIVE-Connection-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568842-JSON-Schema-Properties)
