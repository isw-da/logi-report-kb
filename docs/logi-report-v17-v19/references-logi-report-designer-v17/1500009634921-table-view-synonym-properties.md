---
title: "Table/View/Synonym Properties"
id: 1500009634921
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009634921-Table-View-Synonym-Properties
updated_at: 2021-07-24T16:03:43Z
---

# Table/View/Synonym Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634901-Summary-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611782-Table-View-Synonym-Column-Properties)

# Table/View/Synonym Properties

This topic lists the properties of a Table/View/Synonym object in a catalog.

| Property Name | Description |
| --- | --- |
| Collection Name | Specifies the name of the collection in the MongoDB database. Available for tables in MongoDB connection only. Data type: String |
| Database Name | Specifies the name of the database in the MongoDB connection. Available for tables in MongoDB connection only.  * If the database you specify exists in the MongoDB database, it will connect to the new database. * If the database you specify does not exist in the MongoDB database, no data will be got.   Data type: String |
| Description | Specifies the description of the table/view/synonym. Data type: String |
| Element Path | * For tables in MongoDB connection: Specifies the element name path from the top level document if the table is mapped to a document array element. The path are the element names separated by ".". It will be blank if the table is mapped to the top level element.  '\' is used as an escaped char. If the '.' and '\' are used in the element name, it will be recorded as '\.' and '\\'. * For tables in JSON/Elasticsearch connection: Displays the element path from the root element to current element. This property is read only.   Data type: String |
| Linked Parameter | Specifies the parameter to bind it to the parameter in OOJDBC. Not available for tables in JSON/Elasticsearch connection. Data type: String |
| Name | Specifies the mapped table/view/synonym name in the Logi Report catalog. Data type: String |
| Qualifier | Specifies the name of the catalog which contains the table/view/synonym. Not available for tables in MongoDB/JSON/Elasticsearch connection. Data type: String |
| Schema | Specifies the name of the schema which contains the table/view/synonym. Not available for tables in MongoDB/JSON/Elasticsearch connection. Data type: String |
| Table Name | Specifies the name of the table/view/synonym in the raw database. Not available for tables in MongoDB/JSON/Elasticsearch connection. Data type: String |
| Type | Specifies the type of the table/view/synonym. The table type can be Table or Alias Table, the view type can be View or Alias View, and the synonym type can be Alias, Synonym or Alias Synonym. You can define whether an object is a table, a view or a synonym by selecting a type from the drop-down list, then the object will be put under the corresponding node automatically. Not available for tables in JSON/Elasticsearch connection.  * **Table** - Indicates the type is Table in the database. * **View** - Indicates the type is View in the database. * **Alias** - Indicates the type is Alias in the database. * **Alias Table** - Indicates the type is Alias Table in the database. It will be created when a table is imported more than one time. * **Alias View** - Indicates the type is Alias View in the database. It will be created when a view is imported more than one time. * **Synonym** - Indicates the type is Synonym in the database. * **Alias Synonym** - Indicates the type is Alias Synonym in the database. It will be created when a synonym is imported more than one time.   Data type: Enumeration |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634901-Summary-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611782-Table-View-Synonym-Column-Properties)
