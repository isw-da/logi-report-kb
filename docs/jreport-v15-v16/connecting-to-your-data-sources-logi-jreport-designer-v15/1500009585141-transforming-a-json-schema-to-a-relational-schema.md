---
title: "Transforming a JSON Schema to a Relational Schema"
id: 1500009585141
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585141-Transforming-a-JSON-Schema-to-a-Relational-Schema
updated_at: 2021-07-24T05:55:45Z
---

# Transforming a JSON Schema to a Relational Schema

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585101-Extracting-Metadata-from-JSON-Data)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585121-Setting-Up-a-JSON-Connection)

# Transforming a JSON Schema to a Relational Schema

A JSON schema can be transformed to a relational schema. In the transformation process, elements in the JSON schema will be transformed to either tables or columns in tables according to the ideographic transformation rules and be named according to the naming rules.

Below is a list of the sections covered in this topic:

> * [Transformation Rules](#Transformation)
> * [Naming Rules](#Name)

## Transformation Rules

When a JSON schema is transformed to a relational schema automatically, RDBMS tables will be built based on the schema, and the following rules will be applied:

* If an object class or object array element has at least one attribute element or simple data array element, or its embedded element can be mapped to tables, the object class or object array element will be mapped to a table, and its attribute or simple data array element will be mapped to columns in the table.
* When mapping an attribute element to a column, the value of its Mapped SQL Type will be set as the value of the SQL Type of the column.
* For an embedded object class or object array element, a built-in column called foreign key will be created for the mapped table. If there is no built-in column called primary key in its parent element table, the column will be created. The SQL type of the columns primary key and foreign key is SQL type 4 (64 bit Integer).

## Naming Rules

The RDBMS tables and columns in tables are named based on the rules below:

* For the root element, the table name is ROOT. If the name is not unique, the character \_ will be added before the name one by one until it is unique.
* For elements other than the root element, the table name is the element name. If the table name is not unique, the names of the ancestor elements will be added before the table name one by one and be separated by \_ until it is unique.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585101-Extracting-Metadata-from-JSON-Data)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585121-Setting-Up-a-JSON-Connection)
