---
title: "Table/View/Synonym Properties"
id: 4405661825943
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661825943-Table-View-Synonym-Properties
updated_at: 2022-01-27T20:36:01Z
---

# Table/View/Synonym Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664640535-Summary-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661827095-Table-View-Synonym-Column-Properties)

# Table/View/Synonym Properties

This topic describes the properties of a [Table/View/Synonym object](https://devnet.logianalytics.com/hc/en-us/articles/4405664414743-Using-Tables-Views-Synonyms) in a catalog.

| Property Name | Description |
| --- | --- |
| Collection Name | Designer displays this property when the table is in a MongoDB connection. You can use it to specify the name of the collection in the MongoDB database. Data type: String |
| Database Name | Designer displays this property when the table is in a MongoDB connection. You can use it to specify the name of the database in the MongoDB database. If the database you specify exists in the MongoDB database, Designer connects to the database; otherwise, Designer gets no data. Data type: String |
| Description | Specifies the description of the object. Data type: String |
| Element Path | When the table is in a MongoDB connection, you can use this property to specify the element name path from the top level document if the table is mapped to a document array element. The path is the element names separated by ".". The property value is blank if the table is mapped to the top level element. Designer uses "\" as an escaped char. If the element name contains "." and "\", Designer records them as "\." and "\\". When the table is in a JSON/Elasticsearch connection, this property shows the element path from the root element to current element, and is read only.  Data type: String |
| Linked Parameter | Specifies the parameter you want to bind to the parameter in OOJDBC. Data type: String  Note icon Designer does not provide this property when the table is in a JSON/Elasticsearch connection. |
| Name | Specifies the mapped name of the object in the catalog. Data type: String |
| Qualifier | Specifies the name of the database catalog which contains the object. Data type: String  Note icon Designer does not provide this property when the table is in a MongoDB/JSON/Elasticsearch connection. |
| Schema | Specifies the name of the schema which contains the object. Data type: String  Note icon Designer does not provide this property when the table is in a MongoDB/JSON/Elasticsearch connection. |
| Table Name | Specifies the name of the object in the raw database. Data type: String  Note icon Designer does not provide this property when the table is in a MongoDB/JSON/Elasticsearch connection. |
| Type | Specifies the type of the object. Choose an option from the drop-down list. After you edit the type, Designer moves the object to the corresponding resource node automatically. Data type: Enumeration  Note icon Designer does not provide this property when the table is in a JSON/Elasticsearch connection. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664640535-Summary-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661827095-Table-View-Synonym-Column-Properties)
