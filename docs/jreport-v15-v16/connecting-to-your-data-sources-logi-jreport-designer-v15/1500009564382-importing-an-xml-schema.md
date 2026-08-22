---
title: "Importing an XML Schema"
id: 1500009564382
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564382-Importing-an-XML-Schema
updated_at: 2021-07-24T05:55:42Z
---

# Importing an XML Schema

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585421-XML-Connections)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564402-Transforming-an-XML-Schema-to-a-Relational-Schema)

# Importing an XML Schema

Before an XML schema is transformed to relational tables, it must be imported. Logi JReport Designer provides two ways for you to import an XML schema: importing from an XSD file or parsing from an XML instance. After importing, in order to provide a precision schema to be transformed, you can supplement or modify properties of the imported schema according to your requirements.

Below is a list of sections covered in this topic:

> * [Importing from an XSD File](#XSD)
> * [Importing by Parsing an XML Instance](#XMLInstance)
> * [Supplementing Information for the XML Schema](#XMLSchema)

## Importing from an XSD File

In order to transform the imported XML schema to the relational schema, you can choose to import an XML schema by importing the structure of an XML data source and the information of its elements that are recorded in an XSD file.

You should be aware of the following about XSD in order to generate a correctly imported XML schema:

### Data type conversion table

Before the data type defined in the XSD file can function with Logi JReport Designer, it should first be converted into a corresponding data type when the XML schema is imported following the rules in the conversion table below.

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

### XSD syntax supported by Logi JReport Designer

In Logi JReport Designer, not all XSD syntax can be supported. The following diagram shows the XSD syntax that is supported by Logi JReport Designer and syntax is in accordance with the W3C standard:

**XML Schema::=**

![](https://devnet.logianalytics.com/hc/article_attachments/4404893960983/cnctn_xml_imprt_xsd1.gif)

Text description of the XML Schema:

`annotation*, ((element declaration | SimpleType| ComplexType | notation), annotation*)*;`

**Notes:**

* When a ComplexType is being defined, the element cannot be declared as an anonymous ComplexType.
* Neither loop nor network structures can be defined in the ComplexType, so direct or indirect recursion cannot occur when defining a ComplexType. That is, the type of the element declared in the ComplexType cannot be that defined in the current direct or indirect context.
* Only the anonymous attribute definition is supported by Logi JReport Designer.

The following are diagrams showing the detail syntax of elements in the above diagram:

* **Element Declaration::=**

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404889393815/cnctn_xml_imprt_xsd2.gif)

  Text description of the Element Declaration:

  `element declaration:= annotation?, SimpleType | ComplexType;`
* **SimpleType::=**

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404889394071/cnctn_xml_imprt_xsd3.gif)

  Text description of the SimpleType:

  `anonymous simpleType definition | simpleType definition;`

  **Note:** The SimpleType here should be of the schema built-in type, such as xs:string.
* **Anonymous SimpleType Definition::=**

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404889394327/cnctn_xml_imprt_xsd4.gif)

  Text description of the Anonymous SimpleType Definition:

  `annotation?, (restriction | list);`

  **Note:** List type here cannot support some functions, such as minLength, and maxLength.
* **SimpleType Definition::=**

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404893961367/cnctn_xml_imprt_xsd5.gif)

  Text description of the SimpleType Definition:

  `name, annotation?, (restriction | list)`
* **ComplexType::=**

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404893961623/cnctn_xml_imprt_xsd6.gif)

  Text description of the ComplexType:

  `anonymous ComplexType definition | ComplexType definition;`
* **Anonymous ComplexType Definition::=**

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404893961879/cnctn_xml_imprt_xsd7.gif)

  Text description of the Anonymous ComplexType Definition:

  `annotation?, (ComplexContent | ((all | choice | sequence)?, attribute*));`
* **ComplexType Definition::=**

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404889394583/cnctn_xml_imprt_xsd8.gif)

  Text description of the ComplexType Definition:

  `name, annotation?, (ComplexContent | ((all | choice | sequence)?, attribute*));`
* **All::=**

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404893962135/cnctn_xml_imprt_xsd9.gif)

  Text description of the All:

  `annotation?, element*;`
* **Choice::=**

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404889394839/cnctn_xml_imprt_xsd10.gif)

  Text description of the Choice:

  `annotation?, (element | choice | sequence)*;`
* **Sequence::=**

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404889394839/cnctn_xml_imprt_xsd10.gif)

  Text description of the Sequence:

  `annotation?, (element | choice | sequence)*;`

### Namespace limitation in the XSD file

Default namespace (3w) and target namespace are supported by Logi JReport Designer. You can define a prefix for the default namespace, such as xs, or xsd, but the value of elementFormDefault must be qualified. The value of attributeFormDefault should be unqualified, but Logi JReport Designer will not allow you to add prefixes before the attributes of the elements.

## Importing by Parsing an XML Instance

In order to transform the imported XML schema to the relational schema, you can also choose to parse an XML data source to get the XML structure. You should be aware of the following points about XSD in order to generate a correctly imported XML schema.

* Importing the XML schema from XSD is recommended, because when you import an XML schema by parsing an XML instance, data types in the schema may not be accurate and all elements will be parsed in one tree.
* The XML schema structure will be parsed to a lot of complex elements which begin with XML root node. You can specify data types for the imported XML schema if you know data types accurately, otherwise it will be specified as default of Logi JReport Designer.

## Supplementing Information for the XML Schema

When importing an XML schema, you can modify the properties or supplement some necessary information of the XML schema according to your own requirements in order to make it more useful to you.

The following are some special properties and its description for your reference:

**Name**

Displays the name of an element (![](https://devnet.logianalytics.com/hc/article_attachments/4404893844759/btn_elmnt.gif)), attribute (![](https://devnet.logianalytics.com/hc/article_attachments/4404889311383/btn_atrbt.gif)) or a reference of element (![](https://devnet.logianalytics.com/hc/article_attachments/4404889311639/btn_elmntref.gif)) in the XML instance.

**Data Type**

Specifies the data type of an element or attribute. The data type is imported when importing the XML schema from XSD file or given by Logi JReport when parsing from XML source. This property on a reference of element cannot be modified.

**Format Pattern Type**

This property is activated when you modify properties for data of Date, Time or DateTime type in the XML schema. It can be Default or Customized:

* If Default is selected, the lexical formats inspired by [ISO 8601](http://www.w3.org/TR/xmlschema-2/#ISO8601) will be used for Date, Time or DateTime data following the specification [XML Schema Part 2: Datatypes Second Edition](http://www.w3.org/TR/xmlschema-2/#isoformats).
* If Customized is selected, the [Format Pattern](https://devnet.logianalytics.com/hc/en-us/articles/1500009566022-Format-Pattern-Dialog) dialog will appear for you to specify patterns to format the Date, Time or DateTime data in the XML schema. Select [here](#Format) for details about the format patterns.

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

### Format patterns

A format pattern is a string and can be used for specifying patterns to format strings, which are in XML instance. Logi JReport Format Pattern only supports specifying patterns to format time data type strings, such as date, time and datetime. You can customize the format pattern for date, time and datetime formats or use default ones.

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

  |  |
  | --- |
  | ``` GMTOffsetTimeZone:     GMT Sign Hours: Minutes Sign: one of      + - Hours:     Digit     Digit Digit Minutes:     Digit Digit Digit: one of      0 1 2 3 4 5 6 7 8 9 ``` |

  Hours must be between 0 and 23, and Minutes must be between 00 and 59.
* **RFC 822 time zone:**  

  |  |
  | --- |
  | ``` RFC822TimeZone:    Sign TwoDigitHours Minutes TwoDigitHours:    Digit Digit ``` |

  TwoDigitHours must be between 00 and 23.

Format pattern also supports localized date**,** time and datetime pattern strings. In these strings, the text presentation of pattern letters described in the above table may be varied with the locale.

**Date format pattern**

The representation of the format pattern for date data type in XML schema is same as datetime but the pattern strings are less than it. Only the following strings can be used:
G, yyyy, yy, MMMM, MM, dd, D, WW, ww, F, E.

**Time format pattern**

The representation of the format pattern for time data type in XML schema is same as datetime but the pattern strings are less than it. Only the following strings can be used: a, HH, kk, KK, hh, mm, ss, SSS, z, Z.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585421-XML-Connections)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564402-Transforming-an-XML-Schema-to-a-Relational-Schema)
