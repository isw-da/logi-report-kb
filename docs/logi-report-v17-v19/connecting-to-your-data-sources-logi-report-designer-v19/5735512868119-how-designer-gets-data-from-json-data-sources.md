---
title: "How Designer Gets Data from JSON Data Sources"
id: 5735512868119
section: "Connecting to Your Data Sources - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735512868119-How-Designer-Gets-Data-from-JSON-Data-Sources
updated_at: 2022-11-02T04:29:04Z
---

# How Designer Gets Data from JSON Data Sources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735564733079-Accessing-Data-via-JSON-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735528141079-Working-with-JSON-Connections-in-a-Catalog)

# How Designer Gets Data from JSON Data Sources

Designer can parse JSON data to extract the JSON schema including JSON metadata (JSON objects and the relation between the objects), transform the JSON schema to relational schema and build relational tables during the transformation, namely, map the JSON object classes to tables and table columns, and set up relations between the primary and foreign keys in the tables. This topic introduces the workflow for Designer to get data from JSON data sources.

This topic contains the following sections:

* [Extracting Metadata from JSON Data](#Extract)
* [Transforming JSON Schemas to Relational Schemas](#Transform)

## Extracting Metadata from JSON Data

JSON metadata contains a root element whose element type can be object class or object array. An object class or object array element contains some elements whose element type can be object class, object array, attribute, or simple data array with the data type of String, Number, or Boolean. JSON objects in an array should have the same structure, the members (name/value pairs) in an object cannot be of the same name, and for a nested array, only the first layer is kept.

**Extracting Rules**

Designer uses these rules to extract metadata from JSON data:

* Designer extracts elements from the root value of the JSON data hierarchically.
* When Designer creates the root element, the element name is null, and the root element type is object class or object array if the root value of the JSON data is an object class or an object array, else the root element type is an empty object class.
* If the value of an object member is a simple value, Designer creates an attribute element under current element; if it is a simple value array, Designer creates a simple data array element; if it is an object array, Designer creates an object array element; if it is an object class, Designer creates an object class element. Designer sets the element type according to the conversion rules in the following data type conversion table. The element name is the object member name.
* Designer merges all elements of the same name in object members of an object array into an element.

**Data Type Conversion Rules**

Before the data types defined in the JSON file can function with Designer, Designer needs to convert them into corresponding SQL data types while extracting metadata from the JSON data, based on the rules in the following table.

| JSON Data Type | SQL Data Type |
| --- | --- |
| String (following the format Combined date and time representations in ISO 8601) | TIMESTAMP |
| String (following JDBC Timestamp escape format) | TIMESTAMP |
| String (following the format Calendar dates in ISO 8601) | DATE |
| String (following the format Times with time zone designators in ISO 8601) | TIME |
| String | VARCHAR |
| Number (excluding fraction and exponent) | INTEGER |
| Number (including fraction and exponent) | NUMERIC |
| Boolean | BOOLEAN |

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* If the data type of all values for members of the same name in an object array is Number, including not only integer, but also fraction or exponent, Designer converts the data type of all values to NUMERIC.
* If the values for members of the same name in an object array are of different data types and at least one of them is String, Designer converts the data type of all values to VARCHAR.
* You cannot mix the values for the members of the same name in a JSON schema with simple data array or single value, such as String, Number, Boolean, or Null; otherwise, the extracted schema is incorrect.

## Transforming JSON Schemas to Relational Schemas

When Designer transforms JSON schemas to relational schemas, it transforms elements in the JSON schemas to either tables or columns in tables based on the ideographic transformation rules, and names them according to the naming rules.

**Transformation Rules**

Designer uses these rules when transforming JSON schemas to relational schemas:

* If an object class or object array element has at least one attribute element or simple data array element, or its embedded element can be mapped to tables, Designer maps the object class or object array element to a table, and its attribute or simple data array element to columns in the table.
* When mapping an attribute element to a column, Designer sets the value of its Mapped SQL Type as the value of the SQL Type of the column.
* For an embedded object class or object array element, Designer creates a built-in column called foreign key for the mapped table. If there is no built-in column called primary key in its parent element table, Designer creates the column. The SQL type of the columns primary key and foreign key is SQL type 4 (64 bit Integer).

**Naming Rules**

Designer names the relational tables and columns in tables based on the following rules:

* For the root element, the table name is ROOT. If the name is not unique, Designer adds the character "\_ " before the name one by one until it is unique.
* For elements other than the root element, the table name is the element name. If the table name is not unique, Designer adds the names of the ancestor elements before the table name one by one and separate them by "\_" until it is unique.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735564733079-Accessing-Data-via-JSON-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735528141079-Working-with-JSON-Connections-in-a-Catalog)
