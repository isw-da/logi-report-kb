---
title: "Table/View/Synonym Properties"
id: 1500009590601
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009590601-Table-View-Synonym-Properties
updated_at: 2021-07-24T05:54:23Z
---

# Table/View/Synonym Properties

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590581-Summary-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009569002-Table-View-Synonym-Column-Properties)

# Table/View/Synonym Properties

The properties of a table/view/synonym are as follows:

| Property Name | Description |
| --- | --- |
| Collection Name | Specifies the name of the collection in the MongoDB database. Available for tables in MongoDB connection only. Data type: String |
| Database Name | Specifies the name of the database in the MongoDB connection. Available for tables in MongoDB connection only.  * If the database you specify exists in the MongoDB data source, it will connect to the new database. * If the database you specify does not exist in the MongoDB data source, no data will be got.   Data type: String |
| Description | Specifies the description of the table/view/synonym. Data type: String |
| Element Path | * For tables in MongoDB connection: Specifies the element name path from the top level document if the table is mapped to a document array element. The path are the element names separated by ".". It will be blank if the table is mapped to the top level element.  '\' is used as an escaped char. If the '.' and '\' are used in the element name, it will be recorded as '\.' and '\\'. * For tables in JSON connection: Displays the element path from the root element to current element. This property is read only.   Data type: String |
| Linked Parameter | Specifies the parameter to bind it to the parameter in OOJDBC. Not available for tables in JSON connection. Data type: String |
| Name | Specifies the mapped table/view/synonym name in the Logi JReport catalog. Data type: String |
| Qualifier | Specifies the name of the catalog which contains the table/view/synonym. Not available for tables in MongoDB connection and JSON connection. Data type: String |
| Schema | Specifies the name of the schema which contains the table/view/synonym. Not available for tables in MongoDB connection and JSON connection. Data type: String |
| Table Name | Specifies the name of the table/view/synonym in the raw database. Not available for tables in MongoDB connection and JSON connection. Data type: String |
| Type | Specifies the type of the table/view/synonym. The table type can be Table or Alias Table, the view type can be View or Alias View, and the synonym type can be Alias, Synonym or Alias Synonym. You can define whether an object is a table, a view or a synonym by selecting a type from the drop-down list, then the object will be put under the corresponding node automatically. Not available for tables in JSON connection.  * **Table**  Indicates the type is Table in the database. * **View**  Indicates the type is View in the database. * **Alias**  Indicates the type is Alias in the database. * **Alias Table**  Indicates the type is Alias Table in the database. It will be created when a table is imported more than one time. * **Alias View**  Indicates the type is Alias View in the database. It will be created when a view is imported more than one time. * **Synonym**  Indicates the type is Synonym in the database. * **Alias Synonym** Indicates the type is Alias Synonym in the database. It will be created when a synonym is imported more than one time.   Data type: Enumeration |

A table/view/synonym contains several columns, the properties of which are shown in the following topic: [Table/View/Synonym Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009569002-Table-View-Synonym-Column-Properties).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590581-Summary-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009569002-Table-View-Synonym-Column-Properties)
