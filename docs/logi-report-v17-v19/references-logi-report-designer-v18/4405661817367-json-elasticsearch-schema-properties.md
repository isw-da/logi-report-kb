---
title: "JSON/Elasticsearch Schema Properties"
id: 4405661817367
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661817367-JSON-Elasticsearch-Schema-Properties
updated_at: 2022-01-27T20:35:39Z
---

# JSON/Elasticsearch Schema Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664630295-JSON-Elasticsearch-Connection-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661818391-MongoDB-Connection-Properties)

# JSON/Elasticsearch Schema Properties

This topic describes the properties of a Schema object in a JSON/Elasticsearch connection.

| Property Name | Description |
| --- | --- |
| Element Type | Shows the type of the element. This property is read only. |
| Format for Parsing Date/Time | Designer displays this property when you set Mapped SQL Type to DATE, TIME, or TIMESTAMP. You can use it to specify the format to parse the Date/Time data. Select a format from the drop-down list or type an acceptable format pattern of the java.text.SimpleDateFormat class in the value cell. If the property value is blank, Designer applies the rules as described in [How Designer Gets Data from JSON Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405661430807-How-Designer-Gets-Data-from-JSON-Data-Sources#ConvertRule).  * **ISO 8601 format** - Select to parse the Date/Time data using ISO 8601 format. * **JDBC timestamp escape format** - Select to parse the Date/Time data using the JDBC Timestamp format.   Data type: String |
| JSON Data Type | Shows the JSON data type of the element whose element type is attribute or simple data array. This property is read only. |
| Mapped SQL Type | Specifies the SQL type mapped from JSON data type. You can set this property for attribute and simple data array elements only. Data type: String |
| Name | Shows the name of the element. This property is read only. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664630295-JSON-Elasticsearch-Connection-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661818391-MongoDB-Connection-Properties)
