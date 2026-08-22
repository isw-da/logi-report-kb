---
title: "JSON Schema Properties"
id: 1500009568842
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568842-JSON-Schema-Properties
updated_at: 2021-07-24T05:54:25Z
---

# JSON Schema Properties

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568822-JSON-Connection-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568862-MongoDB-Connection-Properties)

# JSON Schema Properties

The properties of a JSON schema are as follows:

| Property Name | Description |
| --- | --- |
| Element Type | Displays the type of the element. This property is read only. |
| Format for Parsing Date/Time | Specifies the format to parse Date/Time data. This property is available only when Mapped SQL Type is DATE, TIME or TIMESTAMP. Select a format from the drop-down list or input an acceptable format pattern of java.text.SimpleDateFormat class in the text field. If it is blank, the rules in the Data type conversion table are applied.  * **ISO 8601 format** - For ISO 8601 format, the value is represented by this constant string. * **JDBC timestamp escape format** - For JDBC Timestamp format, the value is represented by this constant string.   Data type: String |
| JSON Data Type | Displays the JSON data type of the element whose element type is attribute or simple data array. This property is read only. |
| Mapped SQL Type | Specifies the SQL Type mapped from JSON data type. Available for attribute and simple data array elements only. Data type: String |
| Name | Displays the name of the element. This property is read only. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568822-JSON-Connection-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568862-MongoDB-Connection-Properties)
