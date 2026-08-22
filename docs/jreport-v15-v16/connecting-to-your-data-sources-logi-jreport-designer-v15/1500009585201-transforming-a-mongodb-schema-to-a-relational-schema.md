---
title: "Transforming a MongoDB Schema to a Relational Schema"
id: 1500009585201
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585201-Transforming-a-MongoDB-Schema-to-a-Relational-Schema
updated_at: 2023-11-06T10:02:02Z
---

# Transforming a MongoDB Schema to a Relational Schema

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585161-MongoDB-Connections)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564182-Setting-Up-a-MongoDB-Connection)

# Transforming a MongoDB Schema to a Relational Schema

You can transform a MongoDB schema to a relational schema. In the transformation process, elements in the MongoDB schema will be transformed to tables according to the ideographic transformation rules, and the hierarchical logic in the MongoDB schema will be maintained in the transformed relational schema.

Below is a list of sections covered in this topic:

> * [Transformation Rules](#Rule)
> * [MongoDB Hierarchical Logic in Relational Schema](#Logic)

## Transformation Rules

When a MongoDB schema is transformed to a relational schema automatically, tables will be built based on the schema, and the following rules will be applied:

* A database will be a name space for tables. The tables mapped from a collection in a database will belong to this name space.
* A top level document in a collection or an array element which contains documents will be mapped to a table.

After a document is mapped to a table, the following elements in the document will be mapped to the columns in the table:

* A simple element in the document or in the embedded document which does not belong to an array.
* An array element that contains a simple element in the document or in the embedded document which does not belong to an array.

However, as MongoDB databases use dynamic schemas, a heterogeneous set of documents may be stored within a collection, and only when the data in an array is of the same data type, can it be supported by Logi JReport Designer. The metadata must be extracted from the documents of a MongoDB collection. The following [rules](#Rule) and [method](#Method) for a given document will be applied for the extract. And before the data type defined in the MongoDB BSON document can function with Logi JReport Designer, it should first be converted into a corresponding data type when the MongoDB schema is transformed, following the rules in the [data type conversion table](#Conversion).

**Extracting rules**

* The documents are of the same structure.
* Some elements in the documents can be left blank.
* Documents with different structures will not interrupt the data process.

**Extracting method**

1. Merge all documents into a single document:

   :   elementList=new List();
   :   MergeDocument( Document[] ){

       :   for each document in Document[]

           :   for each element in document

               :   if every E in the elementList does not have the same name as an existing element

                   :   then add the element to elementList.
   :   }
   :   If one element in elementList is a document, get all contents of the element in Document[] and merge them.
2. For the merged document, get each element's name, type, and sub type to build an element in the metadata.

**Data type conversion table**

| BSON Data Type ID | BSON Data Type Name | Is Simple Data | SQL Type | SQL Type Name |
| --- | --- | --- | --- | --- |
| "\x01" | Floating point | Y | 8 | Double |
| "\x02" | UTF-8 string | Y | 12 | VARCHAR |
| "\x03" | Embedded document | N | N/A |  |
| "\x04" | Array (containing simple data only) | N | 2003 | ARRAY |
| "\x05" | Binary data | Y | -3 | VARBINARY |
| "\x06" | Undefined — *Deprecated* | N | N/A |  |
| "\x07" | Objectld | Y | 1 | CHAR (hex string presents 12 bytes) |
| "\x08" | Boolean | Y | 16 | BOOLEAN |
| "\x09" | UTC datetime | Y | 93 | TIMESTAMP |
| "\x0A" | Null value | N | N/A |  |
| "\x0B" | Regular expression | Y | 12 | VARCHAR |
| "\x0C" | DBPointer — *Deprecated* | N | N/A |  |
| "\x0D" | JavaScript code | Y | 12 | VARCHAR |
| "\x0E" | Symbol — *Deprecated* | N | N/A |  |
| "\x0F" | JavaScript code w/ scope | Y | 12 | VARCHAR |
| "\x10" | 32-bit Integer | Y | 4 | INTEGER |
| "\x11" | Timestamp | Y | 93 | TIMESTAMP |
| "\x12" | 64-bit integer | Y | -5 | BIGINT |
| "\xFF" | Min key | N | N/A |  |
| "\x7F" | Max key | N | N/A |  |

**Sub types for binary**

| BSON Data Type ID | SQL Data Type Name |
| --- | --- |
| \x00" | Binary / Generic |
| "\x01" | Function |
| "\x02" | Binary (Old) |
| "\x03" | UUID (Old) |
| "\x04" | UUID |
| "\x05" | MD5 |
| "\x80" | User defined |

## MongoDB Hierarchical Logic in Relational Schema

The XML hierarchical logic will be maintained in the transformed relational schema. The parent-child relationship in the MongoDB schema can be maintained by primary key and foreign key in tables, and this relationship can be reproduced by applying the join of the primary key and foreign key. The business view is based on query. The join will be pushed down to MongoDB with Map/Reduce. When building reports base on the business view, if MongoDB contains a huge amount of detail data, it is suggested that you set the [Prefetch](https://devnet.logianalytics.com/hc/en-us/articles/1500009590341-Business-View-Properties) property of the business view to false.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585161-MongoDB-Connections)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564182-Setting-Up-a-MongoDB-Connection)
