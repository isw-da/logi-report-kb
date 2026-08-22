---
title: "JSON/Elasticsearch Schema Properties"
id: 5735532649367
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735532649367-JSON-Elasticsearch-Schema-Properties
updated_at: 2022-11-02T08:09:45Z
---

# JSON/Elasticsearch Schema Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735526054167-JSON-Elasticsearch-Connection-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735526093591-MongoDB-Connection-Properties)

# JSON/Elasticsearch Schema Properties

This topic describes the properties of a Schema object in a JSON/Elasticsearch connection.

| Property Name | Description |
| --- | --- |
| Element Type | Shows the type of the element. Read only. |
| Format for Parsing Date/Time | Designer displays this property when you set Mapped SQL Type to DATE, TIME, or TIMESTAMP. You can use it to specify the format to parse the Date/Time data. Select a format from the drop-down list or type an acceptable format pattern of the java.text.SimpleDateFormat class in the value cell. If the property value is blank, Designer applies the rules as described in [How Designer Gets Data from JSON Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/5735512868119-How-Designer-Gets-Data-from-JSON-Data-Sources#ConvertRule).  * **ISO 8601 format** Select to parse the Date/Time data using ISO 8601 format. * **JDBC timestamp escape format** Select to parse the Date/Time data using the JDBC Timestamp format.   Data type: String |
| JSON Data Type | Shows the JSON data type of the element whose element type is attribute or simple data array. Read only. |
| Mapped SQL Type | Specifies the SQL type mapped from JSON data type. You can set this property for attribute and simple data array elements only. Data type: String |
| Name | Shows the name of the element. Read only. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735526054167-JSON-Elasticsearch-Connection-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735526093591-MongoDB-Connection-Properties)
