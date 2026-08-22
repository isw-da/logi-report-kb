---
title: "How Designer Gets Data from MongoDB Databases"
id: 4405664419479
section: "Connecting to Your Data Sources - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664419479-How-Designer-Gets-Data-from-MongoDB-Databases
updated_at: 2022-01-27T20:34:42Z
---

# How Designer Gets Data from MongoDB Databases

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661433495-Connecting-via-MongoDB-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664420375-Working-with-MongoDB-Connections-in-a-Catalog)

# How Designer Gets Data from MongoDB Databases

Designer supports extracting the metadata from the documents of a collection in a MongoDB database, and transforming schemas to relational tables. In the transformation process, Designer transforms elements in a MongoDB collection to tables according to the ideographic transformation rules. Designer maintains the hierarchical logic in the MongoDB collection in the transformed relational schema by joins between the primary key and foreign key in the tables. This topic introduces the workflow for Designer to get data from MongoDB databases.

This topic contains the following sections:

* [Extracting Metadata](#Extract)
* [Transforming MongoDB Collections to Relational Schemas](#Transform)

## Extracting Metadata

To use the data in a MongoDB collection, Designer first needs to extract the metadata from the documents of the collection. Designer applies the following rules and method for extracting.

**Extracting rules**

* The documents are of the same structure.
* Some elements in the documents can be left blank.
* Documents with different structures do not interrupt the data process.

**Extracting method**

1. Merge all documents into a single document.

   :   elementList=new List();
   :   MergeDocument( Document[] ){

       :   for each document in Document[]

           :   for each element in document

               :   if every E in the elementList does not have the same name as an existing element

                   :   then add the element to elementList.
   :   }
   :   If one element in elementList is a document, get all contents of the element in Document[] and merge them.
2. For the merged document, get each element's name, type, and subtype to build an element in the metadata.

## Transforming MongoDB Collections to Relational Schemas

While transforming a MongoDB collection to a relational schema, Designer builds tables based on the schema.

**Transformation rules**

Designer takes the following rules during the transformation:

* A database is a name space for tables. The tables mapped from a collection in a database belong to this name space.
* A top level document in a collection or an array element which contains documents is mapped to a table.

After mapping a document to a table, Designer maps the following elements in the document to columns in the table.

* A simple element in the document or in the embedded document which does not belong to an array.
* An array element that contains a simple element in the document or in the embedded document which does not belong to an array.

However, as MongoDB databases use dynamic collections, a heterogeneous set of documents may be stored within a collection. Only when the data in an array is of the same data type, can it be supported by Designer.

**Data type conversion rules**

Before the data types defined in the MongoDB documents can function with Designer, Designer needs to convert them into corresponding SQL data types while transforming the MongoDB collections, based on the rules in the following tables.

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

**Subtypes for binary**

| BSON Data Type ID | SQL Data Type Name |
| --- | --- |
| \x00" | Binary / Generic |
| "\x01" | Function |
| "\x02" | Binary (Old) |
| "\x03" | UUID (Old) |
| "\x04" | UUID |
| "\x05" | MD5 |
| "\x80" | User defined |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661433495-Connecting-via-MongoDB-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664420375-Working-with-MongoDB-Connections-in-a-Catalog)
