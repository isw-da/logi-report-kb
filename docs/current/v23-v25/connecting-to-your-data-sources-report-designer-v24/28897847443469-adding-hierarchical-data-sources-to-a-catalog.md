---
title: "Adding Hierarchical Data Sources to a Catalog"
id: 28897847443469
section: "Connecting to Your Data Sources - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897847443469-Adding-Hierarchical-Data-Sources-to-a-Catalog
updated_at: 2024-09-30T09:11:09Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Adding Hierarchical Data Sources to a Catalog

This topic introduces the two methods for adding hierarchical data sources to a catalog according to how you implement the HDS API: adding general hierarchical data sources and importing hierarchical data sources from XML files. 

This topic contains the following sections:

- 
Adding General HDSs to a Catalog- Example: Adding a General HDS

- 
Importing HDSs from XML Files to a Catalog- The XSD File Used for HDS

## 
Adding General HDSs to a Catalog

To add a general HDS to a catalog, take the following steps:

- 
Create a catalog or open a catalog.

- In the Catalog Manager, do either of the following:
- To add the HDS to  an existing data source in the catalog, right-click the data source node and select New General Hierarchical Data Source from the shortcut menu.

- To add the HDS to a new data source in the catalog, select any of the existing catalog data source, select New Data Source on the Catalog Manager toolbar, then in the New Data source dialog box, specify the name of the data source, select the Hierarchical connection type and select OK.

Designer displays the New General Hierarchical Data Source dialog box.

- Select Browse to specify the HDS class name.

- In the Parameter box, type a number or parameter string. The parameter string must match the format defined in the HDS class. You can reference parameters and constant level formulas predefined in the current catalog data source in the format @FieldName, and the User Name  special field as @username in the PARAMETER string.     

- Select Load Tree. Designer then parses the data source tree.

- Modify the column properties in the Columns box.

- Select OK to add the HDS.

### 
Example: Adding a General HDS

There are three classes used in this example. Their source code files are HierarchicalDataSource.java, HierarchicalDatasetMetaData.java, and HierarchicalDataset.java, which are available in <install_root>\help\samples\APIUDS\hierarchicalUDS. In this example, the HierarchicalDataSource.java returns the result set from the demo HSQL DB.

- Copy the  three files to <install_root>\help. Modify the demo HSQL DB path in both HierarchicalDatasetMetaData.java and HierarchicalDataset.java.

- Compile the Java files to generate HierarchicalDataSource.class, HierarchicalDatasetMetaData.class, and HierarchicalDataset.class.

- Append the path <install_root>\help to the ADDCLASSPATH variable of the setenv.bat batch file in <install_root>\bin, so that at runtime HierarchicalDataSource can be found.

- Start  Designer with the batch file you just modified and open an existing catalog. 

- In the Catalog Manager, right-click the data source to which to add the HDS, then select New General Hierarchical Data Source  from the shortcut menu. 

- In the New General Hierarchical Data Source dialog box, select Browse to find the class HierarchicalDataSource.class.

- In the Parameter box, type a number. Designer only fetches the records whose employee ID is less than this number.

- Select Load Tree. Designer then loads the data source tree.

- In the Columns box, modify the column properties.

- Select OK to add the HDS.

## 
Importing HDSs from XML Files to a Catalog

To import an HDS from an XML file to a catalog, take the following steps:

- 
Create a catalog or open a catalog.

- In the Catalog Manager, do either of the following:
- To import the HDS to  an existing data source in the catalog, right-click the data source node and select New XML Hierarchical Data Source from the shortcut menu.

- To import the HDS to a new data source in the catalog, select any of the existing catalog data source, select New Data Source  on the Catalog Manager toolbar, then in the New Data source dialog box, specify the name of the data source, select the XML connection type, select Hierarchical Data Source and select OK.

Designer displays the New XML Hierarchical Data Source dialog box.

- Select Browse to specify the XML URI and XSD URI. Designer supports all kinds of URI as the XML data source.
- If you want to specify a schema file for the XML data source file, you must first make sure that the schema file path specified in the XML data source file is consistent with the path you provide in the XSD URI text box, and that this file actually exists. Select Load Tree to load the structure of the XML file. Designer then lists the root of the file in the Root Name text box.

- Designer supports static string inline with multiple parameters, for example:
        http://localhost:8888/jrserver%2fSampleReports%2fSampleReports.cat/Key Performance Indicators Report.cls?jrs.cmd=jrs.try_vw&jrs.result_type=7&jrs.param$p_Year=2016&jrs.param$p_Month=2&jrs.param$p_Region=APAC

You can use this URL to run the Key Performance Indicators Report.cls sample report in XML on Server. Type the URL in the XML URI text box and select Load Tree (you should make sure that Server has been started). Designer then loads the structure of the returned XML stream in the Structure box. You can use colon ":" and the "@" symbols to identify Report parameter names. If you use these symbols  in your XML URI but you do not want Report to parse them as parameters, you must add quotation marks to them. For example, when you browse to d:\test\employee.xml, you can quote it either as "d:\test\employee.xml" or d":"\test\employee.xml.

 The Server administrator must select the No Security Checking option in the Administration > Configuration > Advanced page of the Server Console, so that Server can parse the URL successfully. In addition, you can reference the Report parameters in the URL for setting different values dynamically at runtime.

- In the Columns box, modify the column properties.
   When importing the XML file, you have to define the type of some data in the Format column. For example, when the data is Date type such as 1978-03-12, in the corresponding Format column, type yyyy-MM-dd. If the data is $12,345.32, type $##,###.##  in the Format column. By default, the value of the Scale column is 0, therefore, for decimal type data, you need to specify the scale value in the Scale column, that is, modify this value to the number of digits that you want to display to the right of the decimal point. For example, if the data is 123.23, then in the Scale column, modify this value to 2. For the Currency and Array columns, select them.

- Select OK to import the HDS into the catalog.

### 
The XSD File Used for HDS 

When you import an XML HDS with an XSD file, the XML file only provides data to reports; while, the structure, data type, and so on of the data from the XML file is defined in the XSD file, meaning, the XSD file determines the structure of the HDS. You should be aware of the following about the XSD file in order to generate a correct report based on an XML HDS with an XSD file.

Data type conversion

Before the data type defined in the XSD file can function with Designer, Designer should at first convert the data type into a corresponding data type when you import the XML hierarchical data source based on rules in the following conversion table.

| XML Data Type | Report Data Type |
| --- | --- |
| SchemaSymbols.ATTVAL_BOOLEAN | java.sql.Types.BIT |
| SchemaSymbols.ATTVAL_INT | java.sql.Types.INTEGER |
| SchemaSymbols.ATTVAL_SHORT | java.sql.Types.SMALLINT |
| SchemaSymbols.ATTVAL_BYTE | java.sql.Types.TINYINT |
| SchemaSymbols.ATTVAL_INTEGER | java.sql.Types.INTEGER |
| SchemaSymbols.ATTVAL_NONPOSITIVEINTEGER | java.sql.Types.INTEGER |
| SchemaSymbols.ATTVAL_NEGATIVEINTEGER | java.sql.Types.INTEGER |
| SchemaSymbols.ATTVAL_NONNEGATIVEINTEGER | java.sql.Types.INTEGER |
| SchemaSymbols.ATTVAL_UNSIGNEDLONG | java.sql.Types.BIGINT |
| SchemaSymbols.ATTVAL_LONG | java.sql.Types.BIGINT |
| SchemaSymbols.ATTVAL_UNSIGNEDINT, //4294967295 | java.sql.Types.BIGINT |
| SchemaSymbols.ATTVAL_UNSIGNEDSHORT, //65535 | java.sql.Types.INTEGER |
| SchemaSymbols.ATTVAL_UNSIGNEDBYTE, //255 | java.sql.Types.SMALLINT |
| SchemaSymbols.ATTVAL_POSITIVEINTEGER | java.sql.Types.INTEGER |
| SchemaSymbols.ATTVAL_FLOAT | java.sql.Types.FLOAT |
| SchemaSymbols.ATTVAL_DOUBLE | java.sql.Types.DOUBLE |
| SchemaSymbols.ATTVAL_DECIMAL | java.sql.Types.DECIMAL |
| SchemaSymbols.ATTVAL_STRING | java.sql.Types.VARCHAR |
| SchemaSymbols.ATTVAL_DATE | java.sql.Types.DATE |
| SchemaSymbols.ATTVAL_TIME | java.sql.Types.TIME |
| SchemaSymbols.ATTVAL_DATETIME | java.sql.Types.TIMESTAMP |
| SchemaSymbols.ATTVAL_HEXBINARY | java.sql.Types.LONGVARBINARY |

The XSD structure Designer supports

Designer does not support all XSD structures in HDS. The following diagrams show the supported structures.

- 
The ComplexType

The Element type in the diagram can be of simpleType, ref, or complexType (it is different from the ComplexType in the root of this diagram. It can be global complexType but cannot be the anonymous one. If you have defined a complexType named "A", and in this complexType A redefined an element as complexType named "B", then the elements belong to complexType B must be of the simpleType).

The Attribute type in the diagram should be of the anonymous type or of the schema built-in type, such as xs:string.

- 
The SimpleType

SimpleType here should be of the schema built-in type, such as xs:string. List type here cannot support some functions, such as minLength and maxLength.

- 
The Element

ComplexType here can include both global and anonymous complexType. The anonymous type means you do not give a name to the type, for example:

<xs:element name="aa">

    <xs:simpleType>

        <xs:restriction base="xs:string">

            <xs:enumeration value="Julie P. Adams"/>

        </xs:restriction>

    </xs:simpleType>

</xs:element>

From the code, you can see that the simpleType in the element aa has no name specified.

- Designer does not allow an XML data source file without any schema file. That is, you can leave the XSD URI entry empty. However, Designer uses the data type VARCHAR  for all the columns in the data source.

- When you import data of List type from an XSD file, you can define the delimiter via the property List Delimiter in the Report Inspector.

- Designer also supports dynamic XML URI. The XSD file defines the structure of the XML HDS. The XML file in fact only provides the data, so one XSD file can match more than one XML file. That enables you to develop reports with dynamic XML URI. For more information, see Example 1: Developing a Report from an HDS with Dynamic XML URI.

- When you specify a schema file for the XML data source file, due to the schema file being complex, there are some limitations:
      
- 
For Namespace
Designer supports the default namespace (3w) and target namespace. You can define a prefix for the default namespace, such as xs or xsd, but the value of elementFormDefault must be qualified. The value of attributeFormDefault should be unqualified, but Designer does not allow you to add prefixes before the attributes of the elements.

- 
For Type
If you want to use a customized complexType or simpleType, do not add the prefix to the value of the type, while if you use the built-in simpleType or complexType, you must add the prefix.

Previous Topic  Next Topic
