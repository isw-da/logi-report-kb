---
title: "How Designer Gets Data from XML Data Sources"
id: 12480008161165
section: "Connecting to Your Data Sources - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480008161165-How-Designer-Gets-Data-from-XML-Data-Sources
updated_at: 2026-02-25T23:50:11Z
source_host: docs-report.zendesk.com
---
# 
How Designer Gets Data from XML Data Sources

Designer takes the following procedure to get data from an XML data source: importing the XML schemas, supplementing information for the imported XML schemas, and then transforming the XML schemas to relational schemas. This topic introduces this procedure in detail.

This topic contains the following sections:

- 
Importing XML Schemas
- 
Importing from an XSD File
- XSD Syntax Supported by Designer

- Data Type Conversion Rules 

- 
Namespace Limitation in the XSD File

- Importing by Parsing from XML Instances

- 
Supplementing Information for XML Schemas- Format Patterns

- 
Transforming XML Schemas to Relational Schemas
- Transformation Rules

- XML Hierarchical Logic in Relational Schemas

## 
Importing XML Schemas

Designer can import XML schemas either from an XSD file or by parsing from XML instances. 

### 
Importing from an XSD File

You can get the structure of an XML data source and the information of its elements in Designer, by importing an XSD file. You should be aware of the following about XSD in order to generate correctly imported XML schemas.

#### 
XSD Syntax Supported by Designer

Designer does not support all XSD syntax. The following diagram shows the supported XSD syntax. The syntax is in accordance with the W3C standard.

XML Schema::=

Text description of the XML Schema:

annotation*, ((element declaration | SimpleType| ComplexType | notation), annotation*)*;

- If you have defined a ComplexType, you cannot declare the element as an anonymous ComplexType.

- You cannot define loop nor network structures in the ComplexType, so direct or indirect recursion cannot occur when you define a ComplexType. That is, the type of the element declared in the ComplexType cannot be that defined in the current direct or indirect context.

- Designer only supports the anonymous attribute definition.

The following diagrams show the detail syntax of elements in the preceding diagram.

- 
Element Declaration::=

Text description of the Element Declaration:
    

element declaration:= annotation?, SimpleType | ComplexType;

- 
SimpleType::=

Text description of the SimpleType:
    

anonymous simpleType definition | simpleType definition;

The SimpleType here should be of the schema built-in type, such as xs:string.

- 
Anonymous SimpleType Definition::=

Text description of the Anonymous SimpleType Definition:

annotation?, (restriction | list);

 List type here cannot support some functions, such as minLength and maxLength.

- 
SimpleType Definition::=

Text description of the SimpleType Definition:

name, annotation?, (restriction | list)

- 
ComplexType::=

Text description of the ComplexType:
    

anonymous ComplexType definition | ComplexType definition;

- 
Anonymous ComplexType Definition::=

Text description of the Anonymous ComplexType Definition:

annotation?, (ComplexContent | ((all | choice | sequence)?, attribute*));

- 
ComplexType Definition::=

Text description of the ComplexType Definition:

name, annotation?, (ComplexContent | ((all | choice | sequence)?, attribute*));

- 
All::=

Text description of the All:

annotation?, element*;

- 
Choice::=

Text description of the Choice:

annotation?, (element | choice | sequence)*;

- 
Sequence::=

Text description of the Sequence:

annotation?, (element | choice | sequence)*;

#### 
Data Type Conversion Rules 

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

#### 
Namespace Limitation in the XSD File

Designer supports the default namespace (3w) and target namespace. You can define a prefix for the default namespace, such as "xs" or "xsd", but the value of elementFormDefault must be qualified. The value of attributeFormDefault should be unqualified, but Designer does not allow you to add prefixes before the attributes of the elements.

### 
Importing by Parsing from XML Instances

You can also parse an XML data source to get the XML structure in Designer. You should be aware of the following in order to generate a correctly imported XML schema.

- Importing the XML schema from XSD is recommended, because when you import an XML schema by parsing an XML instance, data types in the schema may not be accurate and Designer parses all elements  into one tree.

- Designer parses the XML schema structure into a lot of complex elements which begin with the XML root node. You can specify data types for the imported XML schema if you know data types accurately; otherwise, Designer applies the default.

## 
Supplementing Information for XML Schemas

In order to provide precise schemas to transform, in the process of transforming an XML schema to relational tables, you can modify the properties or supplement some necessary information for the imported XML schemas according to your own requirements, so they can be more useful to you. For information about the properties, see XML Schema Properties. The following describes more about the Format Pattern property.

### 
Format Patterns

A format pattern is a string that you can use for specifying patterns to format strings in the XML instance. The Designer Format Pattern only supports specifying patterns to format time data type strings, such as Date, Time, and DateTime. While transforming an XML schema to relational tables, you can customize the format patterns for Date, Time, and DateTime formats in the XML schema, or apply the default ones which comply with the W3C XML Schema 1.1 specification (for more information, go to www.w3.org/TR/2004/REC-xmlschema-2-20041028/datatypes.html#dateTime).

Customized Format Pattern

You can specify the Date, Time, and DateTime formats in XML schema by the Date, Time, and DateTime pattern strings or customize the format pattern by the Format Pattern dialog box. In the dialog box, Designer interprets the pattern string you select from the Pattern Fragments list box, while it does not interpret the delimiter that you specify. Designer accepts any character and quotes some characters automatically.

For the Date, Time, and DateTime pattern strings in the XML schema, Designer interprets unquoted letters from "A" to "Z" and from "a" to "z"  as pattern letters representing the components of a Date, Time, or DateTime string. You can quote text  using single quotes (') to avoid interpretation. '' represents a single quote. Designer does not interpret all other characters; Designer simply copies them into the output string during formatting or matches them against the input string during parsing the XML schema.

DateTime Format Pattern

The DataTime format pattern consists of some pattern strings and delimiters. Designer provides the following pattern strings in the DataTime format pattern: "G", "yyyy", "yy", "MMMM", "MM", "dd", "D", "WW", "ww", "F", "E", "a", "HH", "kk", "KK", "hh", "mm", "ss", "SSS", "z", and "Z".

| Letter | Date Component | Presentation | Examples |
| --- | --- | --- | --- |
| G | Era designator | Text | AD |
| y | Year | Year | 1996; 96 |
| M | Month in year | Month | July; Jul; 07 |
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
| z | Time zone | General time zone | Pacific Standard Time; PST; GMT-08:00 |
| Z | Time zone | RFC 822 time zone | -0800 |

- 
Year
You can format the pattern string of year  as two types: "yyyy" and "yy".
    
- If you use the pattern string "yyyy" to format year, Designer interprets the year  literally, regardless of the number of digits. Therefore, if you use the pattern "MM/dd/yyyy", Designer parses "08/25/22" to "Aug 25, 22 A.D".

- If you use the abbreviated pattern string "yy"  to format year, Designer needs to interpret the abbreviated year relative to some century. To do this, Designer adjusts dates  to be within 80 years before and 20 years after the current time. For example, if you use the pattern of "MM/dd/yy" and the current time is Aug 25, 1998, Designer interprets the string "05/21/15"  as "May 21, 2015", and  "06/02/88"  as "Jun 2, 1988".

When Designer parses the year string of a DateTime data in the XML schema, it only parses strings consisting of exactly two digits  into the default century. Designer interprets any other numeric string literally, such as a one-digit string, a three or more digit string, or a two-digit string but one is a sign (for example, -2). Therefore, Designer parses "03/06/4" or "03/06/004", using the pattern of "MM/dd/yy", as "Mar 6, 4 AD", and  "03/06/-4" as "Mar 6, 5 BC".

- 
Month
If the pattern string is "MMMM", Designer interprets the month  as text; if the pattern string is "MM", Designer interprets the month  as a number.

- 
General time zone
Designer interprets time zones as text if they have names. For time zones representing a GMT offset value, Designer uses the following syntax:
    
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

Hours must be between 0 and 23, and Minutes must be between 00 and 59.

- 
RFC 822 time zoneRFC822TimeZone:

    Sign TwoDigitHours Minutes

TwoDigitHours:

    Digit Digit

TwoDigitHours must be between 00 and 23.

Format pattern also supports localized Date, Time, and DateTime pattern strings. In these strings, the text presentation of pattern letters described in the preceding table may vary by the locale.

Date Format Pattern

The representation of the format pattern for the Date data type in XML schema is the same as DateTime, but the pattern strings are less than it. You can only use the following strings: " G", "yyyy", "yy", "MMMM", "MM", "dd", "D", "WW", "ww", "F", and "E".

Time Format Pattern

The representation of the format pattern for the Time data type in XML schema is the same as DateTime, but the pattern strings are less than it. You can only use  the following strings: "a", "HH", "kk", "KK", "hh", "mm", "ss", "SSS", "z", and "Z".

## 
Transforming XML Schemas to Relational Schemas

After you import the XML schemas, Designer transforms them to relational schemas. In the transformation process, Designer transforms elements in the XML schemas to either tables or columns in tables according to the ideographic transformation rules, and maintains the hierarchical logic in the XML schemas in the transformed relational schemas. You can then access the transformed tables  in the same way as with JDBC supplied tables.

### 
Transformation Rules

When Designer transforms an XML schema to a relational schema automatically, it applies the following transformation rules.

- Designer transforms a simple element in the XML schema  according to the two rules: 
- If the Is Multiple property is "true", Designer transforms the elements  to a relational table. Designer transforms content of the simple element  to records of a column in the table and names the column the same as the element.

- If the Is Multiple property is "false", Designer transforms content of the simple element  to columns in the table that is transformed from the parent element of the simple element, and names the columns the same as the simple element.

 The value of the Is Multiple property of a simple element is defined by the value of its maxOccurs property in the XSD. If you modify it and make it not match with the maxOccurs property in the transformation process, Designer transforms the element according to the Is Multiple property, regardless of the maxOccurs property. The following are the two conditions:

- If the value of the maxOccurs property of a simple element in XSD is greater than 1 or unbounded, but you modify its Is Multiple property to "false" in the transformation process, Designer transforms only the last content of this element in XML instance to a column.

- If the value of the maxOccurs property of a simple element in XSD is less than or equal to 1, but you modify its Is Multiple property to "true" in the transformation process, Designer transforms the element  to a table with only one column and one record.

- Designer transforms attributes of an element in the XML schema to columns in the table, which is transformed from the element.

- Designer transforms a complex element in the XML schema  to a relational table. Content of complex elements may contain three kinds of subnodes: text, simple element, and subcomplex element.
    
- Designer ignored text in the XML in the transformation process.

- Designer transforms each simple element  to a column in the table according to the preceding rules.

- Designer transforms each subcomplex element to a table according to the preceding rules.

The following examples can help you better understand the transformation rules.

Example 1: Transforming a simple element occurring more than once to a table

In the example, Employee is a simple element and its Is Multiple property is "true" according to the value of maxOccurs in the XSD which is 10, so Designer transforms it  to the Employee table and content of the simple element  to records of a column with the same name as the Employee table.

The following is a segment of the XSD file.

...

<xs:element name="Employee" maxOccurs="10" type="xs:string"/>

...

The following is a segment of the corresponding XML instance.

...

<Employee>John</Employee>

<Employee>Sally</Employee>

...

The following table, named "Employee", is the result that Designer transforms from the simple element occurring more than once in the XML instance. Designer generates the two columns NodePrimaryKey and NodeForeignKey  automatically in the transformation process, and transforms content of the simple element to the  Employee column.

 If the value of the maxOccurs property in the XSD is greater than 1 or unbounded, the simple element occurs more than once in the XML, and the Is Multiple property is "true" by default. However, if you set Is Multiple to "false" in the transformation process, Designer transforms only the last element of the simple element in the XML  to a column of a table, which Designer transforms from the parent element of the simple element.

Example 2: Transforming a simple element occurring once to a column

In the example, Employee is a simple element and its Is Multiple property is "false" according to the value of maxOccurs in the XSD which is less than or equal to 1, so Designer transforms the simple element Employee to the Employee column in the Employees table, which Designer transforms from the parent element.

The following is a segment of the XSD file.

...

<xs:element name="Employee" type="xs:string" maxOccurs="1"/>

...

The following is a segment of the corresponding XML instance.

...

<Employees>

    <Employee>John</Employee>

</Employees>

...

The following table, named "Employees", is the result that Designer transforms from the parent element of the simple element. Designer generates the two columns NodePrimaryKey and NodeForeignKey automatically in the transformation process, and transforms the simple element to the Employee column.

Example 3: Transforming an attribute of an element to a column

In the example, Designer transforms the complex element Employees to the Employees table, the subelements Employee  to another table Employee, and attributes of these subelements to columns in the Employee table. 

The following is a segment of the XSD file.

...

<xsd:attribute name="id" type="xsd:long"/>

<xsd:attribute name="name" type="xsd string"/>

<xsd:attribute name="age" type="xsd:int"/>

...

The following is a segment of the XML file.

...

<Employees groupId="1";>

<Employee id="1", name="John", age="23"/>

<Employee id="9" name="Sally" age="22"/>

...

</Employees>

...

The following table, named "Employees", is the result Designer transforms from the parent element Employees. Designer generates the two columns NodePrimaryKey and NodeForeignKey  automatically in the transformation process. 

The following table, named "Employee",  is the result Designer transforms from the subelement Employee. Designer generates the two columns NodePrimaryKey and NodeForeignKey automatically in the transformation process. Designer maps the foreign key in Employee to the primary key in the Employees table. 

Example 4: Transforming a complex element to a table

In the example, the element StockMarket is of complex type and its Is Multiple property is "true" according to the value of maxOccurs in the XSD file which is 10, so Designer transforms StockMarket to the StockMarket table and its subelements such as Date, Open, High, Low, Close, Volume, and ID  to columns of the table automatically.

The following is a segment of the XSD file.

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

The following is a segment of the corresponding XML file.

<StockMarket>

    <Date>1999-02-11</Date>

    <Open>11.5</Open>

    <High>12.4375</High>

    <Low>11.5</Low>

    <Close>12.4375</Close>

    <Volume>26600</Volume>

    <id>284</id>

</StockMarket>

The following table, named "StockMarket", is the transformed result. Designer generates the two columns NodePrimaryKey and NodeForeignKey automatically in the transformation process, and transforms subelements of the complex element StockMarket to the columns: id, Date, Open, Low, Close, and Volume.

### 
XML Hierarchical Logic in Relational Schemas

During the transformation, Designer maintains the XML hierarchical logic in the transformed relational schemas. Designer maintains the parent-child relationship in the XML schemas by the following two ways:

- If Designer transforms the parent and child nodes to different tables, it maintains the parent-child relationship by primary key and foreign key in tables, and you can reproduce this relationship by applying join between the primary key and foreign key. When you build a query using the tables, the query automatically adds the appropriate join. 

- If Designer can transform the child nodes to columns, it maintains the parent-child relationship in the XML hierarchical logic in the relationship of table-column.
