---
title: "Adding Hierarchical Data Sources to a Catalog"
id: 1500009629501
section: "Connecting to Your Data Sources - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009629501-Adding-Hierarchical-Data-Sources-to-a-Catalog
updated_at: 2021-07-24T16:05:09Z
---

# Adding Hierarchical Data Sources to a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606742-Hierarchical-Data-Source-API) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629521-Developing-Reports-from-Hierarchical-Data-Sources)

# Adding Hierarchical Data Sources to a Catalog

There are two ways to add an HDS to a Logi Report catalog: adding a general HDS or importing from an XML file.

This topic includes the following sections:

* [Adding a General HDS to a Catalog](#General)
  + [Example of Adding a General HDS](#Example)
* [Importing an HDS from an XML File to a Catalog](#Import)
  + [The XSD File Used for HDS](#XSD)

## Adding a General HDS to a Catalog

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, right-click the node of a data source and choose **New General Hierarchical Data Source** from the shortcut menu.

   If you want to add the HDS to a new data source in the catalog, select any of the existing catalog data source, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog, specify the name of the data source, select the **Hierarchical**connection type and select **OK**.
3. In the [New General Hierarchical Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009609282-New-General-Hierarchical-Data-Source-Dialog) dialog, select the **Browse** button to specify the HDS class name.

   ![New General Hierarchical Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904250519/nwhds.gif)
4. Type a number or parameter string in the Parameter box. The parameter string must match the format defined in the [HDS class](https://devnet.logianalytics.com/hc/en-us/articles/1500009606742-Hierarchical-Data-Source-API#ParamString).

   You can reference [parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009611462-Parameters) and [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009611142-Formula-Levels#CLF) predefined in the current catalog data source in the format *@FieldName* and the special field [User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500009606442-Special-Fields#UserName) as *@username* in the PARAMETER string.
5. Select **Load Tree**. The data source tree will then be parsed. Modify the column properties in the Columns box as required.
6. Select **OK** to add the HDS.

### Example of Adding a General HDS

There are three classes used in this example. Their source code files are HierarchicalDataSource.java, HierarchicalDatasetMetaData.java, and HierarchicalDataset.java, which are available in `<install_root>\help\samples\APIUDS\hierarchicalUDS`. In this example, the HierarchicalDataSource.java will return the result set from the demo HSQL DB.

1. Copy the above three files to `<install_root>\help`. Modify the demo HSQL DB path in both HierarchicalDatasetMetaData.java and HierarchicalDataset.java.
2. Compile the Java files to generate HierarchicalDataSource.class, HierarchicalDatasetMetaData.class, and HierarchicalDataset.class.
3. Append the path `<install_root>\help` into the ADDCLASSPATH variable of the batch file setenv.bat in `<install_root>\bin`, so that at runtime HierarchicalDataSource can be found.
4. Start Logi Report Designer with the batch file you just modified and open an existing catalog.
5. In the Catalog Manager, right-click the data source to which to add the HDS, then select **New General Hierarchical Data Source**  from the shortcut menu. The appears.
6. In the New General Hierarchical Data Source dialog, select the **Browse** button to find the class HierarchicalDataSource.class.
7. Type a number in the Parameter box. Then, only the records whose employee ID is less than this number will be fetched.
8. Select **Load Tree**. The data source tree will then be parsed.
9. Modify the column properties in the Columns box as required.
10. Select **OK** to add the HDS.

## Importing an HDS from an XML File to a Catalog

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, right-click the node of a data source and choose **New XML Hierarchical Data Source** from the shortcut menu.

   If you want to add the HDS to a new data source in the catalog, select any of the existing catalog data source, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog, specify the name of the data source, select the **XML**connection type, select the **Hierarchical Data Source** radio button and select **OK**.
3. In the [New XML Hierarchical Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009609442-New-XML-Hierarchical-Data-Source-Dialog) dialog, select the **Browse** buttons to specify the XML URI and XSD URI as required. Select the **Load Tree**button to load the structure of the XML file, the root of the file is then be listed in the Root Name text box.

   ![New XML Hierarchical Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904249879/nwxmlhds.gif)

   Logi Report Designer supports all kinds of URI as the XML data source.

   * If you want to specify a schema file for the XML data source file, you must first make sure that the schema file path specified in the XML data source file is consistent with the path you specified in the XSD URI field, and that this file actually exists. Select the **Load Tree** button to load the structure of the XML file. The root of the file will then be listed in the Root Name field. Modify the column properties in the Columns box as required.
   * Logi Report Designer supports static string inline with multiple parameters, for example:

     `http://localhost:8888/jrserver%2fSampleReports%2fSampleReports.cat/Key Performance Indicators Report.cls?jrs.cmd=jrs.try_vw&jrs.result_type=7&jrs.param$p_Year=2016&jrs.param$p_Month=2&jrs.param$p_Region=APAC`

     It is the URL used to run the sample report Key Performance Indicators Report.cls to the XML format in Logi Report Server. Type the URL into the XML URI text box, and select the **Load Tree**  button, the structure of the returned XML stream will be loaded in the Structure box (before doing so, make sure that Logi Report Server is started). Modify the column properties in the Columns box as required.

     The colon ':' and '@' symbols are used to identify Logi Report parameter names. If these symbols are used in your XML URI and you do not want Logi Report to parse them as parameters, you must add quotation marks to them. For example, when you browse to `d:\test\employee.xml`, you can quote it either as `"d:\test\employee.xml"` or `d":"\test\employee.xml`.

     Note that you should select the No Security Checking option on the Logi Report Server console > Administration > Configuration > Advanced page before parsing this URL. In addition, Logi Report parameters can be dynamically referenced in the URL for setting different values at runtime.
4. Modify the column properties in the Columns box.

   When importing the XML file, you have to define the types of some data in the Format column. For example, if it is Date type, such as 1978-03-12, in the corresponding Format column, type in yyyy-MM-dd. If the data is $12,345.32, in the corresponding Format column, type in $##,###.##. By default, the value of the Scale column is 0, therefore, for decimal type data, you will have to specify the scale value in its corresponding Scale column, that is, modify this value to the number of digits that you want to appear to the right of the decimal point, for example, if the data is 123.23, then in the Scale column, modify this value to 2. For the Currency and Array columns, select them.
5. Select **OK** to import the HDS into the catalog.

### The XSD File Used for HDS

When you import an XML format HDS with an XSD file, the XML file only provides the data to the Logi Report Designer reports, while the structure, data type, and so on of the data from the XML file is defined in the XSD file. That is, the structure of the HDS is determined by the XSD file. You should be aware of the following points about the XSD file in order to generate a correct report based on an XML format HDS with an XSD file.

**Data type conversion**

Before the data type defined in the XSD file can function with Logi Report Designer, it should first be converted into a corresponding data type when the XML format hierarchical data source is imported, following the rules in the conversion table below.

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

**XSD structure supported by Logi Report**

In Logi Report Designer, not all XSD structures can be supported in HDS. The following diagrams show the supported structures.

* **The ComplexType**

  ![ComplexType diagram](https://devnet.logianalytics.com/hc/article_attachments/4404904416791/cnctn_xml_xsd1.gif)

  The Element type in the diagram can be of simpleType, ref, or complexType (it is different from the ComplexType in the root of this diagram. It can be global complexType but cannot be the anonymous one. If you have defined a complexType named A, and in this complexType A redefined an element as complexType named B, then the elements belong to complexType B must be of the simpleType).

  The Attribute type in the diagram should be of the anonymous type or of the schema built-in type, such as xs:string.
* **The SimpleType**

  ![SimpleType diagram](https://devnet.logianalytics.com/hc/article_attachments/4404916825367/cnctn_xml_xsd2.gif)

  SimpleType here should be of the schema built-in type, such as xs:string. List type here cannot support some functions, such as minLength, and maxLength.
* **The Element**

  ![Element diagram](https://devnet.logianalytics.com/hc/article_attachments/4404904417175/cnctn_xml_xsd3.gif)

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

  From the code above, you can see that the simpleType in the element aa has no name specified.

**Notes:**

* An XML data source file without any schema file is also allowed. That is, you can leave the XSD URI entry empty. However, the data type VARCHAR will be used for all the columns in the data source.
* When you import data of List type from an XSD file, you can define the delimiter through the property List Delimiter in the Report Inspector.
* Logi Report Designer also supports dynamic XML URI. The XSD file defines the structure of the XML format HDS and the XML file in fact only provides the data, so one XSD file can match more than one XML file. That enables you to develop reports with dynamic XML URI. For details, see [Example 1: Developing a Report from an HDS with Dynamic XML URI](https://devnet.logianalytics.com/hc/en-us/articles/1500009629521-Developing-Reports-from-Hierarchical-Data-Sources#Example1).
* When specifying a schema file for the XML data source file, due to the schema file being complex, there are some limitations:
  + **Namespace**: Now, default namespace (3w) and target namespace are supported by Logi Report Designer. You can define a prefix for the default namespace, such as xs, or xsd, but the value of elementFormDefault must be qualified. The value of attributeFormDefault should be unqualified, but Logi Report Designer will not allow you to add prefixes before the attributes of the elements.
  + **Type**: If a customized [complexType](#Complex) or [simpleType](#Simple) is used, do not add the prefix to the value of the type, while if the built-in simpleType or complexType is used, the prefix must be added.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606742-Hierarchical-Data-Source-API) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629521-Developing-Reports-from-Hierarchical-Data-Sources)
