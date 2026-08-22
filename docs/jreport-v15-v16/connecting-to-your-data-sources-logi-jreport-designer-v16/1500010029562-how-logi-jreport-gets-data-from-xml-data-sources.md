---
title: "How Logi JReport Gets Data from XML Data Sources"
id: 1500010029562
section: "Connecting to Your Data Sources - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010029562-How-Logi-JReport-Gets-Data-from-XML-Data-Sources
updated_at: 2021-07-24T10:39:12Z
---

# How Logi JReport Gets Data from XML Data Sources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064581-XML-Connections) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064601-Working-with-XML-Connections-in-a-Catalog)

# How Logi JReport Gets Data from XML Data Sources

Logi JReport Designer takes the following procedure to get data from an XML data source: import the XML schemas, supplement information for the imported XML schemas if necessary, then transform the XML schemas to relational schemas and during the transformation process, elements in the XML schemas will be transformed to either tables or columns in tables. The transformed tables can then be accessed in the same way as [JDBC supplied tables](https://devnet.logianalytics.com/hc/en-us/articles/1500010064361-Tables-Views-Synonyms).

Below is a list of the sections covered in this topic:

* [Importing XML Schemas](#Import)
  + [Importing from an XSD File](#XSD)
    - [XSD Syntax Supported by Logi JReport Designer](#Syntax)
    - [Data Type Conversion Rules](#Conversion)
    - [Namespace Limitation in the XS](#Conversion)[D File](#Namespace)
  + [Importing by Parsing from XML Instances](#XMLInstance)
* [Supplementing Information for XML Schemas](#SupplementInfo)
  + [Format Patterns](#Format)
* [Transforming XML Schemas to Relational Schemas](#Transform)
  + [Transformation Rules](#Rules)
  + [XML Hierarchical Logic in Relational Schemas](#Logic)

## Importing XML Schemas

Logi JReport Designer provides two ways to import XML schemas: [importing from an XSD file](#XSD) or [parsing from XML instances](#XMLInstance).

### Importing from an XSD File

You can get the structure of an XML data source and the information of its elements by importing an XSD file. While you should be aware of the following about XSD in order to generate correctly imported XML schemas.

#### XSD Syntax Supported by Logi JReport Designer

In Logi JReport Designer, not all XSD syntax can be supported. The following diagram shows the XSD syntax Logi JReport supports and the syntax is in accordance with the W3C standard:

**XML Schema::=**

![XSD syntax diagram](https://devnet.logianalytics.com/hc/article_attachments/4404901301015/cnctn_xml_imprt_xsd1.gif)

Text description of the XML Schema:

`annotation*, ((element declaration | SimpleType| ComplexType | notation), annotation*)*;`

**Notes:**

* When a ComplexType is being defined, the element cannot be declared as an anonymous ComplexType.
* Neither loop nor network structures can be defined in the ComplexType, so direct or indirect recursion cannot occur when defining a ComplexType. That is, the type of the element declared in the ComplexType cannot be that defined in the current direct or indirect context.
* Only the anonymous attribute definition is supported by Logi JReport Designer.

The following diagrams show the detail syntax of elements in the above diagram:

* **Element Declaration::=**

  ![Element Declaration diagram](https://devnet.logianalytics.com/hc/article_attachments/4404909256727/cnctn_xml_imprt_xsd2.gif)

  Text description of the Element Declaration:

  `element declaration:= annotation?, SimpleType | ComplexType;`
* **SimpleType::=**

  ![SimpleType diagram](https://devnet.logianalytics.com/hc/article_attachments/4404901301271/cnctn_xml_imprt_xsd3.gif)

  Text description of the SimpleType:

  `anonymous simpleType definition | simpleType definition;`

  **Note:** The SimpleType here should be of the schema built-in type, such as xs:string.
* **Anonymous SimpleType Definition::=**

  ![Anonymous SimpleType Definition diagram](https://devnet.logianalytics.com/hc/article_attachments/4404901301527/cnctn_xml_imprt_xsd4.gif)

  Text description of the Anonymous SimpleType Definition:

  `annotation?, (restriction | list);`

  **Note:** List type here cannot support some functions, such as minLength, and maxLength.
* **SimpleType Definition::=**

  ![SimpleType Definition diagram](https://devnet.logianalytics.com/hc/article_attachments/4404909256983/cnctn_xml_imprt_xsd5.gif)

  Text description of the SimpleType Definition:

  `name, annotation?, (restriction | list)`
* **ComplexType::=**

  ![ComplexType diagram](https://devnet.logianalytics.com/hc/article_attachments/4404901301783/cnctn_xml_imprt_xsd6.gif)

  Text description of the ComplexType:

  `anonymous ComplexType definition | ComplexType definition;`
* **Anonymous ComplexType Definition::=**

  ![Anonymous ComplexType Definition diagram](https://devnet.logianalytics.com/hc/article_attachments/4404909257239/cnctn_xml_imprt_xsd7.gif)

  Text description of the Anonymous ComplexType Definition:

  `annotation?, (ComplexContent | ((all | choice | sequence)?, attribute*));`
* **ComplexType Definition::=**

  ![ComplexType Definition diagram](https://devnet.logianalytics.com/hc/article_attachments/4404901302039/cnctn_xml_imprt_xsd8.gif)

  Text description of the ComplexType Definition:

  `name, annotation?, (ComplexContent | ((all | choice | sequence)?, attribute*));`
* **All::=**

  ![All diagram](https://devnet.logianalytics.com/hc/article_attachments/4404909257495/cnctn_xml_imprt_xsd9.gif)

  Text description of the All:

  `annotation?, element*;`
* **Choice::=**

  ![Choice diagram](https://devnet.logianalytics.com/hc/article_attachments/4404909257751/cnctn_xml_imprt_xsd10.gif)

  Text description of the Choice:

  `annotation?, (element | choice | sequence)*;`
* **Sequence::=**

  ![Sequence diagram](https://devnet.logianalytics.com/hc/article_attachments/4404909257751/cnctn_xml_imprt_xsd10.gif)

  Text description of the Sequence:

  `annotation?, (element | choice | sequence)*;`

#### Data Type Conversion Rules

Before the data types defined in the XSD file can function in Logi JReport Designer, they should be converted into corresponding SQL data types when the XML schemas are imported, following the rules in the table below.

| XSD Data Type | SQL Data Type |
| --- | --- |
| BOOLEAN | BIT |
| BYTE | TINYINT |
| UNSIGNEDBYTE | SMALLINT |
| SHORT | SMALLINT |
| UNSIGNEDSHORT | INTEGER |
| INT | INTEGER |
| UNSIGNEDINT | BIGINT |
| LONG | BIGINT |
| UNSIGNEDLONG | DECIMAL |
| NEGATIVEINTEGER | DECIMAL |
| NONPOSITIVEINGEGER | DECIMAL |
| POSITIVEINTEGER | DECIMAL |
| NONNEGATIVEINTEGER | DECIMAL |
| INTEGER | DECIMAL |
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |
| DECIMAL | DECIMAL |
| STRING | VARCHAR |
| NORMALIZEDSTRING | VARCHAR |
| TOKEN | VARCHAR |
| LANGUAGE | VARCHAR |
| NAME | VARCHAR |
| NMTOKEN | VARCHAR |
| NMTOKENS | VARCHAR |
| NCNAME | VARCHAR |
| ID | VARCHAR |
| IDREF | VARCHAR |
| ENTITY | VARCHAR |
| IDREFS | VARCHAR |
| ENTITIES | VARCHAR |
| ANYSIMPLETYPE | VARCHAR |
| GYEAR | VARCHAR |
| GYEARMONTH | VARCHAR |
| GMONTH | VARCHAR |
| GMONTHDAY | VARCHAR |
| GDAY | VARCHAR |
| DATE | DATE |
| TIME | TIME |
| DATETIME | TIMESTAMP |
| HEXBINARY | BLOB |
| BASE64BINARY | BLOB |

#### Namespace Limitation in the XSD File

Default namespace (3w) and target namespace are supported by Logi JReport Designer. You can define a prefix for the default namespace, such as xs, or xsd, but the value of elementFormDefault must be qualified. The value of attributeFormDefault should be unqualified, but Logi JReport Designer will not allow you to add prefixes before the attributes of the elements.

### Importing by Parsing from XML Instances

You can also parse an XML data source to get the XML structure. You should be aware of the following about XSD in order to generate a correctly imported XML schema.

* Importing the XML schema from XSD is recommended, because when you import an XML schema by parsing an XML instance, data types in the schema may not be accurate and all elements will be parsed in one tree.
* The XML schema structure will be parsed to a lot of complex elements which begin with the XML root node. You can specify data types for the imported XML schema if you know data types accurately, otherwise it will be specified as default of Logi JReport Designer.

## Supplementing Information for XML Schemas

In order to provide precision schemas to transform, you can modify the properties or supplement some necessary information for the imported XML schemas according to your own requirements so as to make them more useful to you.

The following are some special properties and their descriptions for your reference:

**Name**

Displays the name of an element (![](https://devnet.logianalytics.com/hc/article_attachments/4404901167639/btn_elmnt.gif)), attribute (![](https://devnet.logianalytics.com/hc/article_attachments/4404909149591/btn_atrbt.gif)) or a reference of element (![](https://devnet.logianalytics.com/hc/article_attachments/4404909149847/btn_elmntref.gif)) in the XML instance.

**Data Type**

Specifies the data type of an element or attribute. The data type is imported when importing the XML schema from XSD file or given by Logi JReport when parsing from XML source. This property on a reference of element cannot be modified.

**Format Pattern Type**

This property is activated when you modify properties for data of Date, Time or DateTime type in the XML schema. It can be Default or Customized:

* If Default is selected, the lexical formats inspired by [ISO 8601](http://www.w3.org/TR/xmlschema-2/#ISO8601) will be used for Date, Time or DateTime data following the specification [XML Schema Part 2: Datatypes Second Edition](http://www.w3.org/TR/xmlschema-2/#isoformats).
* If Customized is selected, the [Format Pattern](https://devnet.logianalytics.com/hc/en-us/articles/1500010066501-Format-Pattern-Dialog) dialog will appear for you to specify patterns to format the Date, Time or DateTime data in the XML schema. [Select here](#Format) for details about the format patterns.

**Format Pattern**

This property is available when you specify to parse data from the XML instance at runtime.

**Is Multiple**

Indicates whether or not an element occurs more than once in the XML instance. By default, the value of the Is Multiple property is affected by the value of its maxOccurs property in the XSD: if the value of maxOccurs property is greater than 1 or unbounded, it is true; otherwise, it is false. You can modify this property according to your own requirements.

**List**

Specifies whether or not to set the data type of an element or attribute as List. This property on a reference of element cannot be modified.

* **List Delimiter**  
   Specifies the delimiter to separate items in the list. Now only the following delimiters are supported: , . ; ! / \ | and space. Space will be specified by default.

The following two properties are alternative:

**Default Value**

Specifies the default value for an element or attribute. If there is no specific value of an element or attribute in the XML schema, the default value you specify here will be applied; otherwise, the value in the XML schema for this element or attribute will be applied.

**Fixed Value**

Specifies the fixed value for an element or attribute, which will be applied no matter there is a value for the element or attribute.

### Format Patterns

A format pattern is a string and can be used for specifying patterns to format strings, which are in XML instance. Logi JReport format Pattern only supports specifying patterns to format time data type strings, such as date, time and datetime. You can customize the format pattern for date, time and datetime formats or use default ones.

In the process of transforming an XML schema to relational tables, you can choose to customize the format patterns for date, time and datetime formats in the XML schema or apply the default ones, which will comply with the W3C XML Schema 1.1 specification (for details, refer to the page <http://www.w3.org/TR/2004/REC-xmlschema-2-20041028/datatypes.html#dateTime>).

**Customized format pattern**

You can specify the date, time and datetime formats in XML schema by the date, time and datetime pattern strings or customize the format pattern by the Format Pattern dialog. In the dialog, the pattern string you select from the Pattern Fragments list box will be interpreted, and the delimiter that you input will not be interpreted. Any character is acceptable and it will be quoted if necessary.

Within date, time and datetime pattern strings in the XML schema, unquoted letters from A to Z and from a to z are interpreted as pattern letters representing the components of a date, time or datetime string. Text can be quoted using single quotes (') to avoid interpretation. '' represents a single quote. All other characters are not interpreted; they're simply copied into the output string during formatting or matched against the input string during parsing the XML schema.

**DateTime format pattern**

The DataTime format pattern consists of some pattern strings and delimiters. Logi JReport provides the following pattern strings in the DataTime format pattern: G, yyyy, yy, MMMM, MM, dd, D, WW, ww, F, E, a, HH, kk, KK, hh, mm, ss, SSS, z, Z.

| Letter | Date Component | Presentation | Examples |
| --- | --- | --- | --- |
| G | Era designator | Text | AD |
| y | Year | [Year](#year) | 1996; 96 |
| M | Month in year | [Month](#month) | July; Jul; 07 |
| w | Week in year | Number | 27 |
| D | Day in year | Number | 189 |
| d | Day in month | Number | 10 |
| F | Day of week in month | Number | 2 |
| E | Day in Week | Text | Tuesday; Tue |
| a | Am/pm marker | Text | PM |
| H | Hour in day (0-23) | Number | 0 |
| k | Hour in day (1-24) | Number | 24 |
| K | Hour in am/pm (0-11) | Number | 0 |
| h | Hour in am/pm (1-12) | Number | 12 |
| m | Minute in hour | Number | 30 |
| s | Second in minute | Number | 55 |
| S | Millisecond | Number | 978 |
| z | Time zone | [General time zone](#timezone) | Pacific Standard Time; PST; GMT-08:00 |
| Z | Time zone | [RFC 822 time zone](#rfc822timezone) | -0800 |

* **Year**  
   The pattern string of year can be formatted as two types - yyyy and yy:
  + If the pattern string - yyyy is used to format year, the year will be interpreted literally, regardless of the number of digits. Therefore, if the pattern MM/dd/yyyy is used, 08/25/22 will be parsed to Aug 25, 22 A.D.
  + If the abbreviated pattern string - yy is used to format year, the abbreviated year relative to some century must be interpreted. To do this, dates will be adjusted to be within 80 years before and 20 years after the current time. For example, a pattern of MM/dd/yy and the current time is Aug 25, 1998, the string 05/21/15 would be interpreted as May 21, 2015 while the string 06/02/88 would be interpreted as Jun 2, 1988.

  When the year string of a datetime data in the XML schema is parsing, only strings consisting of exactly two digits will be parsed into the default century. Any other numeric string, such as a one-digit string, a three or more digit string, or a two-digit string but one is a sign (for example, -2), is interpreted literally. So 03/06/4 or 03/06/004 is parsed, using the pattern of MM/dd/yy, as Mar 6, 4 AD. Also, 03/06/-4 is parsed as Mar 6, 5 BC.

* **Month**  
   If the pattern string is MMMM, the month is interpreted as text; if the pattern string is MM, the month will be interpreted as a number.
* **General time zone**  
   Time zones are interpreted as text if they have names. For time zones representing a GMT offset value, the following syntax is used:

  ```
  GMTOffsetTimeZone:  
      GMT Sign Hours: Minutes  
  Sign: one of   
      + -  
  Hours:  
      Digit  
      Digit Digit  
  Minutes:  
      Digit Digit  
  Digit: one of   
      0 1 2 3 4 5 6 7 8 9
  ```

  Hours must be between 0 and 23, and Minutes must be between 00 and 59.
* **RFC 822 time zone:**

  ```
  RFC822TimeZone:  
      Sign TwoDigitHours Minutes  
  TwoDigitHours:  
      Digit Digit
  ```

  TwoDigitHours must be between 00 and 23.

Format pattern also supports localized date**,** time and datetime pattern strings. In these strings, the text presentation of pattern letters described in the above table may be varied with the locale.

**Date format pattern**

The representation of the format pattern for date data type in XML schema is same as datetime but the pattern strings are less than it. Only the following strings can be used:
G, yyyy, yy, MMMM, MM, dd, D, WW, ww, F, E.

**Time format pattern**

The representation of the format pattern for time data type in XML schema is same as datetime but the pattern strings are less than it. Only the following strings can be used: a, HH, kk, KK, hh, mm, ss, SSS, z, Z.

## Transforming XML Schemas to Relational Schemas

After the XML schemas are imported, Logi JReport will transform them to relational schemas. In the transformation process, elements in the XML schemas are transformed to either tables or columns in tables according to the ideographic transformation rules, and the hierarchical logic in the XML schemas is maintained in the transformed relational schemas.

### Transformation Rules

When an XML schema is transformed to a relational schema automatically, the following transformation rules are applied:

* A simple element in the XML schema is transformed according to the following two rules:
  + If the Is Multiple property is to true, elements will be transformed to a relational table. Contents of the simple element will be transformed to records of a column in the table and the column is named the same as the element.
  + If the Is Multiple property is to false, contents of the simple element will be transformed to columns in the table transformed from the parent element of the simple element, and columns are named the same as the simple element.

  **Note:** The value of the Is Multiple property of a simple element is defined by the value of its maxOccurs property in the XSD. If you modify it and make it not match with the maxOccurs property in the transformation process, the element will be transformed according to the Is Multiple property regardless of the maxOccurs property. The following are the two conditions:

  + If the value of maxOccurs property of a simple element in XSD is greater than 1 or unbounded, but its Is Multiple property is modified to False in the transformation process, then only the last content of this element in XML instance can be transformed to a column.
  + If the value of maxOccurs property of a simple element in XSD is less than or equal to 1, but its Is Multiple property is modified to True in the transformation process, then the element will be transformed to a table with only one column and one record.
* Attributes of an element in the XML schema will be transformed to columns in the table, which is transformed from the element.
* A complex element in the XML schema will be transformed to a relational table. Contents of complex elements may contain three kinds of sub-nodes: text, simple element and sub-complex element.
  + Text in the XML will be ignored in the transformation process.
  + Each simple element will be transformed to a column in the table according to the rules above.
  + Each sub-complex element will be transformed to a table according to the rules above.

Below examples can help you better understand the transformation rules.

**Example 1: Transforming a simple element occurring more than once to a table**

In the example, Employee is a simple element and its Is Multiple property is true according to the value of maxOccurs in the XSD which is 10, so it will be transformed to a table, named Employee. Contents of the simple element will be transformed to records of a column with the same name as the Employee table.

The following is a segment of an XSD file:

```
...  
<xs:element name="Employee" maxOccurs="10" type="xs:string"/>
...
```

The following is a segment of the corresponding XML instance:

```
...  
<Employee>John</Employee>  
<Employee>Sally</Employee>  
...
```

The following table, named Employee, is the result which is transformed from the simple element occurring more than once in the XML instance:

![Table transformed from a simple element in the XML instance](https://devnet.logianalytics.com/hc/article_attachments/4404901303319/cnctn_xml_trnsfrm_rule2.gif)

In the result, these two columns - NodePrimaryKey and NodeForeignKey are generated by the system automatically in the transformation process, and the column Employee is transformed from contents of the simple element.

**Note:** If the value of the maxOccurs property in the XSD is greater than 1 or unbounded, the simple element will occur more than once in the XML, and the Is Multiple property is true by default, but if you set Is Multiple to false in the transformation process, only the last element of the simple element in the XML will be transformed to a column of a table, which is transformed from the parent element of the simple element.

**Example 2: Transforming a simple element occurring once to a column**

In the example, Employee is a simple element and its property Is Multiple is false according to the value of maxOccurs in the XSD which is less than or equal to 1, so the simple element Employee will be transformed to a column, named Employee in the Employees table which is transformed from the parent element.

The following is a segment of an XSD file:

```
...  
<xs:element name="Employee" type="xs:string" maxOccurs="1"/>  
...
```

The following is a segment of the corresponding XML instance:

```
...  
<Employees>  
    <Employee>John</Employee>  
</Employees>  
...
```

The following table, named Employees, is the transformed result which is transformed from the parent element of the simple element:

![Table transformed from the parent element of the simple element in XML instance](https://devnet.logianalytics.com/hc/article_attachments/4404901303319/cnctn_xml_trnsfrm_rule2.gif)

In the result table, these two columns - NodePrimaryKey and NodeForeignKey are generated by the system automatically in the transformation process, and the column Employee is transformed from the simple element.

**Example 3: Transforming an attribute of an element to a column**

In the example, the complex element - Employees will be transformed to a table, named Employees, the sub-elements Employee will be transformed to another table, named Employee, and attributes of these sub-elements will be transformed to columns in the Employee table.

The following is a segment of an XSD file:

```
...  
<xsd:attribute name="id" type="xsd:long"/>  
<xsd:attribute name="name" type="xsd string"/>  
<xsd:attribute name="age" type="xsd:int"/>  
...
```

The following is a segment of an XML file:

```
...  
<Employees groupId="1";>  
<Employee id="1", name="John", age="23"/>  
<Employee id="9" name="Sally" age="22"/>  
...  
</Employees>  
...
```

The following table named Employees is transformed from the parent element - Employees:

![Table transformed from the parent element/](https://devnet.logianalytics.com/hc/article_attachments/4404901303575/cnctn_xml_trnsfrm_rule3.gif)

In the result table, these two columns NodePrimaryKey and NodeForeignKey are generated by the system automatically in the transformation process.

The following table named Employee is transformed from sub-elements - Employee:

![Table transformed from sub-elements](https://devnet.logianalytics.com/hc/article_attachments/4404901303831/cnctn_xml_trnsfrm_rule4.gif)

In the result table, these two columns NodePrimaryKey and NodeForeignKey are generated by the system automatically in the transformation process and the foreign key in the Employee is mapped to the primary key in the Employees table.

**Example 4: Transforming a complex element to a table**

In the example, the element StockMarket is of complex type and its property Is Multiple is true according to the value of maxOccurs in the XSD file which is 10, so StockMarket will be transformed to a table, named StockMarket and its sub-elements such as: Date, Open, High, Low, Close, Volume and ID will all be transformed to columns of the table automatically.

The following is a segment of an XSD file:

```
<xs:element name="StockMarket">  
    <xs:complexType>   
        <xs:choice maxOccurs="10">  
            <xs:element name="Date" type="xs:date" />  
            <xs:element name="Open" type="xs:double" />  
            <xs:element name="High" type="xs:double" />  
            <xs:element name="Low" type="xs:double" />  
            <xs:element name="Close" type="xs:double" />  
            <xs:element name="Volume" type="xs:double" />  
            <xs:element name="ID" type="xs:long" />  
        </xs:choice>  
    </xs:complexType>  
</xs:element>
```

The following is a segment of a corresponding XML file:

```
<StockMarket>  
    <Date>1999-02-11</Date>  
    <Open>11.5</Open>  
    <High>12.4375</High>  
    <Low>11.5</Low>  
    <Close>12.4375</Close>  
    <Volume>26600</Volume>  
    <id>284</id>  
</StockMarket>
```

The following table named StockMarket is the transformed result:

![Table transformed from a complex element](https://devnet.logianalytics.com/hc/article_attachments/4404909259799/cnctn_xml_trnsfrm_rule1.gif)

In the result table, these two columns NodePrimaryKey and NodeForeignKey are generated by the system automatically in the transformation process and the columns- id, Date, Open, Low, Close, Volume are transformed from sub-elements of the complex element StockMarket.

### XML Hierarchical Logic in Relational Schemas

During the transformation, the XML hierarchical logic is maintained in the transformed relational schemas. The parent-child relationship in the XML schemas can be maintained by the following two ways:

* If the parent and child nodes are transformed to different tables, the parent-child relationship will be maintained by primary key and foreign key in tables, and this relationship can be reproduced by applying join between the primary key and foreign key. When you build a query using the tables the query will automatically add the appropriate join.
* If the child nodes can be transformed to columns, the parent-child relationship in the XML hierarchical logic will be maintained in the relationship of table-column.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064581-XML-Connections) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064601-Working-with-XML-Connections-in-a-Catalog)
