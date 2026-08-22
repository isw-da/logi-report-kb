---
title: "Extracting Metadata from JSON Data"
id: 1500009585101
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585101-Extracting-Metadata-from-JSON-Data
updated_at: 2024-02-12T11:11:34Z
---

# Extracting Metadata from JSON Data

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585081-JSON-Connections)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585141-Transforming-a-JSON-Schema-to-a-Relational-Schema)

# Extracting Metadata from JSON Data

A JSON metadata contains a root element whose element type can be object class or object array. An object class or object array element contains some elements whose element type can be object class,  object array, attribute or simple data array with the data type of string, number or Boolean. JSON objects in an array should have the same structure, the members (name/value pairs) in an object cannot be of the same name, and for a nested array, only the first layer will be kept.

Below is a list of the sections covered in this topic:

> * [Extracting Method](#Extract)
> * [Data Type Conversion Table](#Conversion)

## Extracting method

When a JSON schema is transformed to a relational schema automatically, RDBMS tables will be built based on the schema, and the following rules will be applied:

* Elements should be extracted from the root value of JSON data hierarchically.
* When creating the root element, the element name is null, and the root element type is object class or object array if the root value of JSON data is an object class or an object array, else the root element type is an empty object class.
* If the value of an object member is a simple value, an attribute element will be created under current element. If it is a simple value array, a simple data array element will be created. If it is an object array, an object array element will be created. If it is an object class, an object class element will be created. The element type will be set according to the conversion rules in the Data type conversion table below. The element name is the object member name.
* All elements of the same name in object members of an object array will be merged into an element.

## Data Type Conversion Table

Before the JSON data type defined in the JSON file can function with Logi JReport Designer, it should first be converted into a corresponding SQL data type when extracting metadata from JSON data, following the rules below.

| JSON Data Type | SQL Data Type |
| --- | --- |
| String (following the format Combined date and time representations in ISO 8601) | TIMESTAMP |
| String (following JDBC timestamp escape format) | TIMESTAMP |
| String (following the format Calendar dates in ISO 8601) | DATE |
| String (following the format Times with time zone designators in ISO 8601) | TIME |
| String | VARCHAR |
| Number (excluding fraction and exponent) | INTEGER |
| Number (including fraction and exponent) | NUMERIC |
| Boolean | BOOLEAN |

**Notes:**

* If the data type of all values for members of the same name in an object array is Number, including not only integer, but also fraction or exponent, the data type of all values will be converted to NUMERIC.
* If the values for members of the same name in an object array are of different data types and at least one of them is String, the data type of all values will be converted to VARCHAR.
* The values for the members of the same name in a JSON schema cannot be mixed with simple data array and single value, such as string, number,Boolean, or null, otherwise, the extracted schema maybe incorrect.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585081-JSON-Connections)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585141-Transforming-a-JSON-Schema-to-a-Relational-Schema)
