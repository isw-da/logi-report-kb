---
title: "JSON/Elasticsearch Schema Properties"
id: 45190626890893
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190626890893-JSON-Elasticsearch-Schema-Properties
updated_at: 2026-04-30T15:15:27Z
source_host: logi-report-v26.insightsoftware.com
---
# 
JSON/Elasticsearch Schema Properties

This topic describes the properties of a Schema object in a JSON/Elasticsearch connection.

| Property Name | Description |
| --- | --- |
| Element Type | Shows the type of the element. Read only. |
| Format for Parsing Date/Time | Designer displays this property when you set Mapped SQL Type to DATE, TIME, or TIMESTAMP. You can use it to specify the format to parse the Date/Time data. Select a format from the drop-down list or type an acceptable format pattern of the java.text.SimpleDateFormat class in the value cell. If the property value is blank, Designer applies the rules as described in How Designer Gets Data from JSON Data Sources. ISO 8601 format Select to parse the Date/Time data using ISO 8601 format. JDBC timestamp escape format Select to parse the Date/Time data using the JDBC Timestamp format. Data type: String |
| JSON Data Type | Shows the JSON data type of the element whose element type is attribute or simple data array. Read only. |
| Mapped SQL Type | Specifies the SQL type mapped from JSON data type. You can set this property for attribute and simple data array elements only. Data type: String |
| Name | Shows the name of the element. Read only. |
