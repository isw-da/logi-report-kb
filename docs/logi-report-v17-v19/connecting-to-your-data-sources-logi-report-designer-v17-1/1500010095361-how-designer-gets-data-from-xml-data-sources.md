---
title: "How Designer Gets Data from XML Data Sources"
id: 1500010095361
section: "Connecting to Your Data Sources - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010095361-How-Designer-Gets-Data-from-XML-Data-Sources
updated_at: 2021-07-23T19:14:58Z
---

# How Designer Gets Data from XML Data Sources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057882-Connecting-via-XML-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095381-Working-with-XML-Connections-in-a-Catalog)

# How Designer Gets Data from XML Data Sources

Designer takes the following procedure to get data from an XML data source: import the XML schemas, supplement information for the imported XML schemas, and then transform the XML schemas to relational schemas. This topic introduces this procedure in detail.

This topic contains the following sections:

* [Importing XML Schemas](#Import)
  + [Importing from an XSD File](#XSD)
    - [XSD Syntax Supported by Designer](#Syntax)
    - [Data Type Conversion Rules](#Conversion)
    - [Namespace Limitation in the XS](#Conversion)[D File](#Namespace)
  + [Importing by Parsing from XML Instances](#XMLInstance)
* [Supplementing Information for XML Schemas](#SupplementInfo)
  + [Format Patterns](#Format)
* [Transforming XML Schemas to Relational Schemas](#Transform)
  + [Transformation Rules](#Rules)
  + [XML Hierarchical Logic in Relational Schemas](#Logic)

## Importing XML Schemas

Using Designer, you can import XML schemas by either of the two methods: [importing from an XSD file](#XSD) or [parsing from XML instances](#XMLInstance).

### Importing from an XSD File

You can get the structure of an XML data source and the information of its elements by importing an XSD file. While you should be aware of the following about XSD in order to generate correctly imported XML schemas.

#### XSD Syntax Supported by Designer

Designer does not support all XSD syntax. The following diagram shows the supported XSD syntax. The syntax is in accordance with the W3C standard.

**XML Schema::=**

![XSD syntax diagram](https://devnet.logianalytics.com/hc/article_attachments/4404857015447/cnctn_xml_imprt_xsd1.gif)

Text description of the XML Schema:

`annotation*, ((element declaration | SimpleType| ComplexType | notation), annotation*)*;`

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* If you have defined a ComplexType, you cannot declare the element as an anonymous ComplexType.
* You cannot define loop nor network structures in the ComplexType, so direct or indirect recursion cannot occur when you define a ComplexType. That is, the type of the element declared in the ComplexType cannot be that defined in the current direct or indirect context.
* Designer only supports the anonymous attribute definition.

The following diagrams show the detail syntax of elements in the above diagram:

* **Element Declaration::=**

  ![Element Declaration diagram](https://devnet.logianalytics.com/hc/article_attachments/4404857015703/cnctn_xml_imprt_xsd2.gif)

  Text description of the Element Declaration:

  `element declaration:= annotation?, SimpleType | ComplexType;`
* **SimpleType::=**

  ![SimpleType diagram](https://devnet.logianalytics.com/hc/article_attachments/4404857016087/cnctn_xml_imprt_xsd3.gif)

  Text description of the SimpleType:

  `anonymous simpleType definition | simpleType definition;`

  The SimpleType here should be of the schema built-in type, such as xs:string.
* **Anonymous SimpleType Definition::=**

  ![Anonymous SimpleType Definition diagram](https://devnet.logianalytics.com/hc/article_attachments/4404848646039/cnctn_xml_imprt_xsd4.gif)

  Text description of the Anonymous SimpleType Definition:

  `annotation?, (restriction | list);`

  List type here cannot support some functions, such as minLength and maxLength.
* **SimpleType Definition::=**

  ![SimpleType Definition diagram](https://devnet.logianalytics.com/hc/article_attachments/4404857016343/cnctn_xml_imprt_xsd5.gif)

  Text description of the SimpleType Definition:

  `name, annotation?, (restriction | list)`
* **ComplexType::=**

  ![ComplexType diagram](https://devnet.logianalytics.com/hc/article_attachments/4404857016727/cnctn_xml_imprt_xsd6.gif)

  Text description of the ComplexType:

  `anonymous ComplexType definition | ComplexType definition;`
* **Anonymous ComplexType Definition::=**

  ![Anonymous ComplexType Definition diagram](https://devnet.logianalytics.com/hc/article_attachments/4404857016983/cnctn_xml_imprt_xsd7.gif)

  Text description of the Anonymous ComplexType Definition:

  `annotation?, (ComplexContent | ((all | choice | sequence)?, attribute*));`
* **ComplexType Definition::=**

  ![ComplexType Definition diagram](https://devnet.logianalytics.com/hc/article_attachments/4404857017239/cnctn_xml_imprt_xsd8.gif)

  Text description of the ComplexType Definition:

  `name, annotation?, (ComplexContent | ((all | choice | sequence)?, attribute*));`
* **All::=**

  ![All diagram](https://devnet.logianalytics.com/hc/article_attachments/4404857017495/cnctn_xml_imprt_xsd9.gif)

  Text description of the All:

  `annotation?, element*;`
* **Choice::=**

  ![Choice diagram](https://devnet.logianalytics.com/hc/article_attachments/4404848647063/cnctn_xml_imprt_xsd10.gif)

  Text description of the Choice:

  `annotation?, (element | choice | sequence)*;`
* **Sequence::=**

  ![Sequence diagram](https://devnet.logianalytics.com/hc/article_attachments/4404848647063/cnctn_xml_imprt_xsd10.gif)

  Text description of the Sequence:

  `annotation?, (element | choice | sequence)*;`

#### Data Type Conversion Rules

Before the data types defined in the XSD file can function in Designer, Designer needs to convert them to the corresponding SQL data types when you import the XML schemas, based on the rules in the following table.

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

Designer supports the default namespace (3w) and target namespace. You can define a prefix for the default namespace, such as "xs" or "xsd", but the value of elementFormDefault must be qualified. The value of attributeFormDefault should be unqualified, but Designer does not allow you to add prefixes before the attributes of the elements.

### Importing by Parsing from XML Instances

You can also parse an XML data source to get the XML structure. You should be aware of the following about XSD in order to generate a correctly imported XML schema.

* Importing the XML schema from XSD is recommended, because when you import an XML schema by parsing an XML instance, data types in the schema may not be accurate and Designer parses all elements into one tree.
* Designer parses the XML schema structure into a lot of complex elements which begin with the XML root node. You can specify data types for the imported XML schema if you know data types accurately; otherwise, Designer applies its defaults to them.

## Supplementing Information for XML Schemas

In order to provide precision schemas to transform, you can modify the properties or supplement some necessary information for the imported XML schemas according to your own requirements so that they can be more useful to you.

The following are some special properties and their descriptions for your reference:

**Name**

The property shows the name of an element (![](https://devnet.logianalytics.com/hc/article_attachments/4404856879895/btn_elmnt.gif)), attribute (![](https://devnet.logianalytics.com/hc/article_attachments/4404848477463/btn_atrbt.gif)), or a reference of element (![](https://devnet.logianalytics.com/hc/article_attachments/4404848477719/btn_elmntref.gif)) in the XML instance.

**Data Type**

The property specifies the data type of an element or attribute. Designer imports the data type when importing the XML schema from XSD file or provides it when parsing from XML source. You cannot modify this property on a reference of element.

**Format Pattern Type**

The property is available for data of Date, Time, or DateTime type in the XML schema. It can be Default or Customized.

* If you specify the property value as Default, Designer uses the lexical formats inspired by [ISO 8601](http://www.w3.org/TR/xmlschema-2/#ISO8601) for Date, Time, or DateTime data following the specification [XML Schema Part 2: Datatypes Second Edition](http://www.w3.org/TR/xmlschema-2/#isoformats).
* If you specify the property value as Customized, Designer displays the [Format Pattern dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097161-Format-Pattern-Dialog-Box) for you to specify the [pattern](#Format) to format the Date, Time, or DateTime data in the XML schema.

**Format Pattern**

The property is available when you specify to parse data from the XML instance at runtime.

**Is Multiple**

The property indicates whether or not an element occurs more than once in the XML instance. By default, the value of the Is Multiple property is affected by the value of its maxOccurs property in the XSD: if the value of maxOccurs is greater than 1 or unbounded, it is true; otherwise, it is false. You can modify this property according to your own requirements.

**List**

The property specifies whether or not to set the data type of an element or attribute as List. You cannot edit this property on a reference of element.

* **List Delimiter**  
  Specify the delimiter to separate items in the list. Designer only supports the following delimiters at present : ",", ".", ";", "!", "/", "\", "|", and space. By default, Designer uses space.

The following two properties are alternative:

**Default Value**

The property specifies the default value for an element or attribute. If there is no specific value of an element or attribute in the XML schema, Designer applies the default value you specify here; otherwise, Designer applies the value in the XML schema for this element or attribute.

**Fixed Value**

The property specifies the fixed value for an element or attribute, which Designer applies no matter there is a value for the element or attribute.

### Format Patterns

A format pattern is a string that you can use for specifying patterns to format strings in the XML instance. The Designer Format Pattern only supports specifying patterns to format time data type strings, such as Date, Time, and DateTime. You can customize the format pattern for Date, Time, and DateTime formats or use default ones.

In the process of transforming an XML schema to relational tables, you can customize the format patterns for Date, Time, and DateTime formats in the XML schema, or apply the default ones which comply with the W3C XML Schema 1.1 specification (for more information, see <http://www.w3.org/TR/2004/REC-xmlschema-2-20041028/datatypes.html#dateTime>).

**Customized format pattern**

You can specify the Date, Time, and DateTime formats in XML schema by the Date, Time, and DateTime pattern strings or customize the format pattern by the Format Pattern dialog box. In the dialog box, Designer interprets the pattern string you select from the Pattern Fragments list box, while it does not interpret the delimiter that you specify. Designer accepts any character and quotes some characters automatically.

For the Date, Time, and DateTime pattern strings in the XML schema, Designer interprets unquoted letters from "A" to "Z" and from "a" to "z" as pattern letters representing the components of a Date, Time, or DateTime string. You can quote text using single quotes (') to avoid interpretation. '' represents a single quote. Designer does not interpret all other characters; Designer simply copies them into the output string during formatting or matches them against the input string during parsing the XML schema.

**DateTime format pattern**

The DataTime format pattern consists of some pattern strings and delimiters. Designer provides the following pattern strings in the DataTime format pattern: "G", "yyyy", "yy", "MMMM", "MM", "dd", "D", "WW", "ww", "F", "E", "a", "HH", "kk", "KK", "hh", "mm", "ss", "SSS", "z", and "Z".

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
  You can format the pattern string of year as two types: "yyyy" and "yy".
  + If you use the pattern string "yyyy" to format year, Designer interprets the year literally, regardless of the number of digits. Therefore, if you use the pattern "MM/dd/yyyy", Designer parses "08/25/22" to "Aug 25, 22 A.D".
  + If you use the abbreviated pattern string "yy" to format year, Designer needs to interpret the abbreviated year relative to some century. To do this, Designer adjusts dates to be within 80 years before and 20 years after the current time. For example, if you use the pattern of "MM/dd/yy" and the current time is Aug 25, 1998, Designer interprets the string "05/21/15" as "May 21, 2015", and "06/02/88" as "Jun 2, 1988".

  When Designer parses the year string of a DateTime data in the XML schema, it only parses strings consisting of exactly two digits into the default century. Designer interprets any other numeric string literally, such as a one-digit string, a three or more digit string, or a two-digit string but one is a sign (for example, -2). Therefore, Designer parses "03/06/4" or "03/06/004", using the pattern of "MM/dd/yy", as "Mar 6, 4 AD", and "03/06/-4" as "Mar 6, 5 BC".

* **Month**  
  If the pattern string is "MMMM", Designer interprets the month as text; if the pattern string is "MM", Designer interprets the month as a number.
* **General time zone**  
  Designer interprets time zones as text if they have names. For time zones representing a GMT offset value, Designer uses the following syntax:

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

Format pattern also supports localized Date, Time, and DateTime pattern strings. In these strings, the text presentation of pattern letters described in the above table may vary with the locale.

**Date format pattern**

The representation of the format pattern for the Date data type in XML schema is the same as DateTime, but the pattern strings are less than it. You can only use the following strings: " G", "yyyy", "yy", "MMMM", "MM", "dd", "D", "WW", "ww", "F", and "E".

**Time format pattern**

The representation of the format pattern for the Time data type in XML schema is the same as DateTime, but the pattern strings are less than it. You can only use the following strings: "a", "HH", "kk", "KK", "hh", "mm", "ss", "SSS", "z", and "Z".

## Transforming XML Schemas to Relational Schemas

After you import the XML schemas, Designer transforms them to relational schemas. In the transformation process, Designer transforms elements in the XML schemas to either tables or columns in tables according to the ideographic transformation rules, and maintains the hierarchical logic in the XML schemas in the transformed relational schemas. You can then access the transformed tables in the same way as with JDBC supplied tables.

### Transformation Rules

When Designer transforms an XML schema to a relational schema automatically, it applies the following transformation rules:

* Designer transforms a simple element in the XML schema according to the following two rules:
  + If the Is Multiple property is true, Designer transforms the elements to a relational table. Designer transforms contents of the simple element to records of a column in the table and names the column the same as the element.
  + If the Is Multiple property is false, Designer transforms contents of the simple element to columns in the table that is transformed from the parent element of the simple element, and names the columns the same as the simple element.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) The value of the Is Multiple property of a simple element is defined by the value of its maxOccurs property in the XSD. If you modify it and make it not match with the maxOccurs property in the transformation process, Designer transforms the element according to the Is Multiple property, regardless of the maxOccurs property. The following are the two conditions:

  + If the value of the maxOccurs property of a simple element in XSD is greater than 1 or unbounded, but you modify its Is Multiple property to false in the transformation process, Designer transforms only the last content of this element in XML instance to a column.
  + If the value of the maxOccurs property of a simple element in XSD is less than or equal to 1, but you modify its Is Multiple property to true in the transformation process, Designer transforms the element to a table with only one column and one record.
* Designer transforms attributes of an element in the XML schema to columns in the table, which is transformed from the element.
* Designer transforms a complex element in the XML schema to a relational table. Contents of complex elements may contain three kinds of sub-nodes: text, simple element, and sub-complex element.
  + Designer ignored text in the XML in the transformation process.
  + Designer transforms each simple element to a column in the table according to the rules above.
  + Designer transforms each sub-complex element to a table according to the rules above.

The following examples can help you better understand the transformation rules.

**Example 1: Transforming a simple element occurring more than once to a table**

In the example, Employee is a simple element and its Is Multiple property is true according to the value of maxOccurs in the XSD which is 10, so Designer transforms it to a table, named "Employee". Designer transforms contents of the simple element to records of a column with the same name as the Employee table.

The following is a segment of the XSD file:

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

The following table, named "Employee", is the result that Designer transforms from the simple element occurring more than once in the XML instance:

![Table transformed from a simple element in the XML instance](https://devnet.logianalytics.com/hc/article_attachments/4404848647447/cnctn_xml_trnsfrm_rule2.gif)

In the result, the two columns, NodePrimaryKey and NodeForeignKey, are generated by Designer automatically in the transformation process, and the column Employee is transformed from contents of the simple element.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) If the value of the maxOccurs property in the XSD is greater than 1 or unbounded, the simple element occurs more than once in the XML, and the Is Multiple property is true by default. However, if you set Is Multiple to false in the transformation process, Designer transforms only the last element of the simple element in the XML to a column of a table, which is transformed from the parent element of the simple element.

**Example 2: Transforming a simple element occurring once to a column**

In the example, Employee is a simple element and its property Is Multiple is false according to the value of maxOccurs in the XSD which is less than or equal to 1, so Designer transforms the simple element Employee to a column, named "Employee" in the Employees table which is transformed from the parent element.

The following is a segment of the XSD file:

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

The following table, named "Employees", is the result that Designer transforms from the parent element of the simple element:

![Table transformed from the parent element of the simple element in XML instance](https://devnet.logianalytics.com/hc/article_attachments/4404848647447/cnctn_xml_trnsfrm_rule2.gif)

In the result table, the two columns, NodePrimaryKey and NodeForeignKey, are generated by Designer automatically in the transformation process, and the column Employee is transformed from the simple element.

**Example 3: Transforming an attribute of an element to a column**

In the example, Designer transforms the complex element - Employees to a table, named "Employees", the sub-elements Employee to another table, named "Employee", and attributes of these sub-elements to columns in the Employee table.

The following is a segment of the XSD file:

```
...  
<xsd:attribute name="id" type="xsd:long"/>  
<xsd:attribute name="name" type="xsd string"/>  
<xsd:attribute name="age" type="xsd:int"/>  
...
```

The following is a segment of the XML file:

```
...  
<Employees groupId="1";>  
<Employee id="1", name="John", age="23"/>  
<Employee id="9" name="Sally" age="22"/>  
...  
</Employees>  
...
```

The following table named "Employees" is transformed from the parent element - Employees:

![Table transformed from the parent element/](https://devnet.logianalytics.com/hc/article_attachments/4404857017879/cnctn_xml_trnsfrm_rule3.gif)

In the result table, the two columns, NodePrimaryKey and NodeForeignKey, are generated by Designer automatically in the transformation process.

The following table named "Employee" is transformed from the sub-elements - Employee:

![Table transformed from sub-elements](https://devnet.logianalytics.com/hc/article_attachments/4404848648087/cnctn_xml_trnsfrm_rule4.gif)

In the result table, the two columns, NodePrimaryKey and NodeForeignKey, are generated by Designer automatically in the transformation process. Designer maps the foreign key in Employee to the primary key in the Employees table.

**Example 4: Transforming a complex element to a table**

In the example, the element StockMarket is of complex type and its property Is Multiple is true according to the value of maxOccurs in the XSD file which is 10, so Designer transforms StockMarket to a table, named "StockMarket", and its sub-elements such as Date, Open, High, Low, Close, Volume, and ID to columns of the table automatically.

The following is a segment of the XSD file:

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

The following is a segment of the corresponding XML file:

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

The following table named "StockMarket" is the transformed result:

![Table transformed from a complex element](https://devnet.logianalytics.com/hc/article_attachments/4404857018135/cnctn_xml_trnsfrm_rule1.gif)

In the result table, the two columns, NodePrimaryKey and NodeForeignKey, are generated by Designer automatically in the transformation process. The columns: id, Date, Open, Low, Close, and Volume are transformed from sub-elements of the complex element StockMarket.

### XML Hierarchical Logic in Relational Schemas

During the transformation, Designer maintains the XML hierarchical logic in the transformed relational schemas. Designer maintains the parent-child relationship in the XML schemas by the following two ways:

* If Designer transforms the parent and child nodes to different tables, it maintains the parent-child relationship by primary key and foreign key in tables, and you can reproduce this relationship by applying join between the primary key and foreign key. When you build a query using the tables, the query automatically adds the appropriate join.
* If Designer can transform the child nodes to columns, it maintains the parent-child relationship in the XML hierarchical logic in the relationship of table-column.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057882-Connecting-via-XML-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095381-Working-with-XML-Connections-in-a-Catalog)
