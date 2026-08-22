---
title: "XML Connection Properties"
id: 5735532825111
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735532825111-XML-Connection-Properties
updated_at: 2022-11-02T08:09:57Z
---

# XML Connection Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735532819095-Web-Service-Connection-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735568669079-XML-Schema-Properties)

# XML Connection Properties

This topic describes the properties of an [XML Connection object](https://devnet.logianalytics.com/hc/en-us/articles/5735521660439-Accessing-Data-via-XML-Connections) in a catalog.

| Property Name | Description |
| --- | --- |
| Date Format | Specifies the default format for Date type data. Data type: String |
| Default | Specifies whether the connection is the default connection in the current catalog data source. By default, the first connection you create in a data source is the default connection of the data source. A data source can have zero or one default connection. Data type: Boolean |
| Description | Specifies the description of the connection. Data type: String |
| Name | Specifies the mapped name of the connection in the catalog. Data type: String |
| Name Pattern | Specifies whether to use catalog or schema in data manipulation. Choose an option from the drop-down list.  * **unqualified name** Select to include neither catalog nor schema in data manipulation. Example: SELECT t.c FROM t * **2-part names** Select to use schema in data manipulation. Example: SELECT schema.t.c FROM schema.t * **3-part names** Select to use both catalog and schema in data manipulation. Example: SELECT catalog.schema.t.c from catalog.schema.t   Data type: Enumeration |
| Time Format | Specifies the default format for Time type data. Data type: String |
| Timestamp Format | Specifies the default format for Timestamp type data. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735532819095-Web-Service-Connection-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735568669079-XML-Schema-Properties)
