---
title: "Adding Hierarchical Data Sources to a Catalog"
id: 5735499355159
section: "Connecting to Your Data Sources - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735499355159-Adding-Hierarchical-Data-Sources-to-a-Catalog
updated_at: 2022-11-02T04:28:55Z
---

# Adding Hierarchical Data Sources to a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735527956503-Hierarchical-Data-Source-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735527967639-Developing-Reports-from-Hierarchical-Data-Sources)

# Adding Hierarchical Data Sources to a Catalog

This topic introduces the two methods for adding hierarchical data sources to a catalog according to how you implement the HDS API: adding general hierarchical data sources and importing hierarchical data sources from XML files.

This topic contains the following sections:

* [Adding General HDSs to a Catalog](#General)
  + [Example: Adding a General HDS](#Example)
* [Importing HDSs from XML Files to a Catalog](#Import)
  + [The XSD File Used for HDS](#XSD)

## Adding General HDSs to a Catalog

To add a general HDS to a catalog, take the following steps:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735563628951-Creating-Opening-and-Saving-Catalogs) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735563628951-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, do either of the following:
   * To add the HDS to an existing data source in the catalog, right-click the data source node and select **New General Hierarchical Data Source** from the shortcut menu.
   * To add the HDS to a new data source in the catalog, select any of the existing catalog data source, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog box, specify the name of the data source, select the **Hierarchical** connection type and select **OK**.

   Designer displays the [New General Hierarchical Data Source dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735543777943-New-General-Hierarchical-Data-Source-Dialog-Box).

   ![New General Hierarchical Data Source dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898478537367/nwhds.gif)
3. Select **Browse** to specify the HDS class name.
4. In the **Parameter** box, type a number or parameter string. The parameter string must match the format defined in the [HDS class](https://devnet.logianalytics.com/hc/en-us/articles/5735527956503-Hierarchical-Data-Source-API#ParamString). You can reference [parameters](https://devnet.logianalytics.com/hc/en-us/articles/5735532413719-Working-with-Parameters) and [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/5735525461399-Formula-Levels#CLF) predefined in the current catalog data source in the format *@FieldName*, and the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/5735564398999-Working-with-Special-Fields#UserName)" as *@username* in the PARAMETER string.
5. Select **Load Tree**. Designer then parses the data source tree.
6. Modify the column properties in the **Columns** box.
7. Select **OK** to add the HDS.

### Example: Adding a General HDS

There are three classes used in this example. Their source code files are HierarchicalDataSource.java, HierarchicalDatasetMetaData.java, and HierarchicalDataset.java, which are available in `<install_root>\help\samples\APIUDS\hierarchicalUDS`. In this example, the HierarchicalDataSource.java returns the result set from the demo HSQL DB.

1. Copy the three files to `<install_root>\help`. Modify the demo HSQL DB path in both HierarchicalDatasetMetaData.java and HierarchicalDataset.java.
2. Compile the Java files to generate HierarchicalDataSource.class, HierarchicalDatasetMetaData.class, and HierarchicalDataset.class.
3. Append the path `<install_root>\help` to the ADDCLASSPATH variable of the **setenv.bat** batch file in `<install_root>\bin`, so that at runtime HierarchicalDataSource can be found.
4. Start Designer with the batch file you just modified and open an existing catalog.
5. In the Catalog Manager, right-click the data source to which to add the HDS, then select **New General Hierarchical Data Source**  from the shortcut menu.
6. In the New General Hierarchical Data Source dialog box, select **Browse** to find the class HierarchicalDataSource.class.
7. In the **Parameter** box, type a number. Designer only fetches the records whose employee ID is less than this number.
8. Select **Load Tree**. Designer then loads the data source tree.
9. In the **Columns** box, modify the column properties.
10. Select **OK** to add the HDS.

## Importing HDSs from XML Files to a Catalog

To import an HDS from an XML file to a catalog, take the following steps:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735563628951-Creating-Opening-and-Saving-Catalogs) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735563628951-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, do either of the following:
   * To import the HDS to an existing data source in the catalog, right-click the data source node and select **New XML Hierarchical Data Source** from the shortcut menu.
   * To import the HDS to a new data source in the catalog, select any of the existing catalog data source, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog box, specify the name of the data source, select the **XML** connection type, select **Hierarchical Data Source** and select **OK**.

   Designer displays the [New XML Hierarchical Data Source dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735515004311-New-XML-Hierarchical-Data-Source-Dialog-Box).

   ![New XML Hierarchical Data Source dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898461435927/nwxmlhds.gif)
3. Select **Browse** to specify the XML URI and XSD URI. Designer supports all kinds of URI as the XML data source.
   * If you want to specify a schema file for the XML data source file, you must first make sure that the schema file path specified in the XML data source file is consistent with the path you provide in the XSD URI text box, and that this file actually exists. Select **Load Tree** to load the structure of the XML file. Designer then lists the root of the file in the **Root Name** text box.
   * Designer supports static string inline with multiple parameters, for example:

     `http://localhost:8888/jrserver%2fSampleReports%2fSampleReports.cat/Key Performance Indicators Report.cls?jrs.cmd=jrs.try_vw&jrs.result_type=7&jrs.param$p_Year=2016&jrs.param$p_Month=2&jrs.param$p_Region=APAC`

     You can use this URL to run the Key Performance Indicators Report.cls sample report in XML on Server. Type the URL in the **XML URI** text box and select **Load Tree** (you should make sure that Server has been started). Designer then loads the structure of the returned XML stream in the **Structure** box. You can use colon ":" and the "@" symbols to identify Logi Report parameter names. If you use these symbols in your XML URI but you do not want Logi Report to parse them as parameters, you must add quotation marks to them. For example, when you browse to `d:\test\employee.xml`, you can quote it either as `"d:\test\employee.xml"` or `d":"\test\employee.xml`.

     ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) The Server administrator must select the No Security Checking option in the Administration > Configuration > Advanced page of the Server Console, so that Server can parse the URL successfully. In addition, you can reference the Logi Report parameters in the URL for setting different values dynamically at runtime.
4. In the **Columns** box, modify the column properties.
   When importing the XML file, you have to define the type of some data in the Format column. For example, when the data is Date type such as 1978-03-12, in the corresponding Format column, type **yyyy-MM-dd**. If the data is $12,345.32, type **$##,###.##** in the Format column. By default, the value of the Scale column is 0, therefore, for decimal type data, you need to specify the scale value in the Scale column, that is, modify this value to the number of digits that you want to display to the right of the decimal point. For example, if the data is 123.23, then in the Scale column, modify this value to **2**. For the Currency and Array columns, select them.
5. Select **OK** to import the HDS into the catalog.

### The XSD File Used for HDS

When you import an XML HDS with an XSD file, the XML file only provides data to reports; while, the structure, data type, and so on of the data from the XML file is defined in the XSD file, meaning, the XSD file determines the structure of the HDS. You should be aware of the following about the XSD file in order to generate a correct report based on an XML HDS with an XSD file.

**Data type conversion**

Before the data type defined in the XSD file can function with Designer, Designer should at first convert the data type into a corresponding data type when you import the XML hierarchical data source based on rules in the following conversion table.

| XML Data Type | Logi Report Data Type |
| --- | --- |
| SchemaSymbols.ATTVAL\_BOOLEAN | java.sql.Types.BIT |
| SchemaSymbols.ATTVAL\_INT | java.sql.Types.INTEGER |
| SchemaSymbols.ATTVAL\_SHORT | java.sql.Types.SMALLINT |
| SchemaSymbols.ATTVAL\_BYTE | java.sql.Types.TINYINT |
| SchemaSymbols.ATTVAL\_INTEGER | java.sql.Types.INTEGER |
| SchemaSymbols.ATTVAL\_NONPOSITIVEINTEGER | java.sql.Types.INTEGER |
| SchemaSymbols.ATTVAL\_NEGATIVEINTEGER | java.sql.Types.INTEGER |
| SchemaSymbols.ATTVAL\_NONNEGATIVEINTEGER | java.sql.Types.INTEGER |
| SchemaSymbols.ATTVAL\_UNSIGNEDLONG | java.sql.Types.BIGINT |
| SchemaSymbols.ATTVAL\_LONG | java.sql.Types.BIGINT |
| SchemaSymbols.ATTVAL\_UNSIGNEDINT, //4294967295 | java.sql.Types.BIGINT |
| SchemaSymbols.ATTVAL\_UNSIGNEDSHORT, //65535 | java.sql.Types.INTEGER |
| SchemaSymbols.ATTVAL\_UNSIGNEDBYTE, //255 | java.sql.Types.SMALLINT |
| SchemaSymbols.ATTVAL\_POSITIVEINTEGER | java.sql.Types.INTEGER |
| SchemaSymbols.ATTVAL\_FLOAT | java.sql.Types.FLOAT |
| SchemaSymbols.ATTVAL\_DOUBLE | java.sql.Types.DOUBLE |
| SchemaSymbols.ATTVAL\_DECIMAL | java.sql.Types.DECIMAL |
| SchemaSymbols.ATTVAL\_STRING | java.sql.Types.VARCHAR |
| SchemaSymbols.ATTVAL\_DATE | java.sql.Types.DATE |
| SchemaSymbols.ATTVAL\_TIME | java.sql.Types.TIME |
| SchemaSymbols.ATTVAL\_DATETIME | java.sql.Types.TIMESTAMP |
| SchemaSymbols.ATTVAL\_HEXBINARY | java.sql.Types.LONGVARBINARY |

**The XSD structure Designer supports**

Designer does not support all XSD structures in HDS. The following diagrams show the supported structures.

* **The ComplexType**

  ![ComplexType diagram](https://devnet.logianalytics.com/hc/article_attachments/9898533961367/cnctn_xml_xsd1.gif)

  The Element type in the diagram can be of simpleType, ref, or complexType (it is different from the ComplexType in the root of this diagram. It can be global complexType but cannot be the anonymous one. If you have defined a complexType named "A", and in this complexType A redefined an element as complexType named "B", then the elements belong to complexType B must be of the simpleType).

  The Attribute type in the diagram should be of the anonymous type or of the schema built-in type, such as xs:string.
* **The SimpleType**

  ![SimpleType diagram](https://devnet.logianalytics.com/hc/article_attachments/9898517564055/cnctn_xml_xsd2.gif)

  SimpleType here should be of the schema built-in type, such as xs:string. List type here cannot support some functions, such as minLength and maxLength.
* **The Element**

  ![Element diagram](https://devnet.logianalytics.com/hc/article_attachments/9898517569687/cnctn_xml_xsd3.gif)

  ComplexType here can include both global and anonymous complexType. The anonymous type means you do not give a name to the type, for example:

  ```
  <xs:element name="aa">  
   
      <xs:simpleType>  
   
          <xs:restriction base="xs:string">  
   
              <xs:enumeration value="Julie P. Adams"/>  
   
          </xs:restriction>  
   
      </xs:simpleType>  
   
  </xs:element>
  ```

  From the code, you can see that the simpleType in the element aa has no name specified.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* Designer does not allow an XML data source file without any schema file. That is, you can leave the XSD URI entry empty. However, Designer uses the data type VARCHAR for all the columns in the data source.
* When you import data of List type from an XSD file, you can define the delimiter via the property List Delimiter in the Report Inspector.
* Designer also supports dynamic XML URI. The XSD file defines the structure of the XML HDS. The XML file in fact only provides the data, so one XSD file can match more than one XML file. That enables you to develop reports with dynamic XML URI. For more information, see [Example 1: Developing a Report from an HDS with Dynamic XML URI](https://devnet.logianalytics.com/hc/en-us/articles/5735527967639-Developing-Reports-from-Hierarchical-Data-Sources#Example1).
* When you specify a schema file for the XML data source file, due to the schema file being complex, there are some limitations:
  + **For Namespace**  
    Designer supports the default namespace (3w) and target namespace. You can define a prefix for the default namespace, such as xs or xsd, but the value of elementFormDefault must be qualified. The value of attributeFormDefault should be unqualified, but Designer does not allow you to add prefixes before the attributes of the elements.
  + **For Type**  
    If you want to use a customized [complexType](#Complex) or [simpleType](#Simple), do not add the prefix to the value of the type, while if you use the built-in simpleType or complexType, you must add the prefix.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735527956503-Hierarchical-Data-Source-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735527967639-Developing-Reports-from-Hierarchical-Data-Sources)
