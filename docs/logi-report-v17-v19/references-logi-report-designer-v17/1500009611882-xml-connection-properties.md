---
title: "XML Connection Properties"
id: 1500009611882
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009611882-XML-Connection-Properties
updated_at: 2021-07-24T16:03:43Z
---

# XML Connection Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611842-Web-Service-Connection-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611902-XML-Schema-Properties)

# XML Connection Properties

This topic lists the properties of an XML Connection object in a catalog.

| Property Name | Description |
| --- | --- |
| Date Format | Specifies the default format for data of Date type. Data type: String |
| Default | Specifies whether the connection is the default connection in the current data source. By default, the first added connection in a data source is the default connection of the data source. A data source can have zero or one default connection. Data type: Boolean |
| Description | Specifies the description of the XML connection. Data type: String |
| Name | Specifies the full path of the XSD file. Data type: String |
| Name Pattern | Specifies whether or not catalog or schema is used in data manipulation. Choose an option from the drop-down list.  * **unqualified name**  - Neither catalog nor schema is included in data manipulation. Example: SELECT t.c FROM t * **2-part names**  - Uses schema in data manipulation. Example: SELECT schema.t.c FROM schema.t * **3-part names**  - Uses both catalog and schema in data manipulation. Example: SELECT catalog.schema.t.c from catalog.schema.t   Data type: Enumeration |
| Time Format | Specifies the default format for data of Time type. Data type: String |
| Timestamp Format | Specifies the default format for data of Timestamp type. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611842-Web-Service-Connection-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611902-XML-Schema-Properties)
