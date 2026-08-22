---
title: "Using Data Sources via OOJDBC in a Catalog"
id: 1500010095201
section: "Connecting to Your Data Sources - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010095201-Using-Data-Sources-via-OOJDBC-in-a-Catalog
updated_at: 2021-07-23T19:14:54Z
---

# Using Data Sources via OOJDBC in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095181-Using-Imported-SQLs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095241-Connecting-via-JSON-Connections)

# Using Data Sources via OOJDBC in a Catalog

This topic introduces the main frame for OOJDBC in Logi Report and how you can import data sources of different types via OOJDBC into a catalog.

This topic contains the following sections:

* [Main Frame for OOJDBC in Logi Report](#Frame)
* [Using XML File as Data Source via OOJDBC](#XML)
  + [Example 1: Importing the XML File Indirectly](#Example1)
  + [Example 2: Importing the XML File Directly](#Example2)
  + [Example 3: XML File with Dynamic Parameters](#Example3)
* [Using Class File as Data Source via OOJDBC](#Class)
* [Using CSV File as Data Source via OOJDBC](#CSV)

## Main Frame for OOJDBC in Logi Report

OOJDBC (Object Oriented Java Database Connection) is defined to cover an OODS (Object Oriented Data Source) with a JDBC interface. It is similar to a JDBC driver and is based on a Java application, EJB (Enterprise Java Bean), or LDAP (Light Weight Directory Access Protocol), which can be defined as a database. Logi Report provides a tool named Model Wizard, which you can run to import data via an OOJDBC data source.

OOJDBC in Logi Report includes the Model Wizard and OOJDBC Driver.

* **Model Wizard**  
   Opens/Saves model file  
   Defines a Java class as a table  
   Defines a method as a column  
   How to access the instance of the class
* **OOJDBC Driver**  
   Reads the table/column definitions from model file  
   Returns metadata to Logi Report  
   Constructs QUERY data  
   Returns record to Logi Report

![Diagram of the main frame for OOJDBC](https://devnet.logianalytics.com/hc/article_attachments/4404857021463/cnctn_jdbc_oojdbc.gif)

## Using XML File as Data Source via OOJDBC

Designer supports accessing XML data sources via OOJDBC.

You can also use XML directly in Designer which is recommended over using OOJDBC. For more information, see [XML Connections](https://devnet.logianalytics.com/hc/en-us/articles/1500010057882-Connecting-via-XML-Connections).

### Example 1: Importing the XML File Indirectly

This example uses employee.xml in `<install_root>\help\samples\OOJDBC`. Store the file to `<install_root>\Demo\Reports\TutorialReports` first. Then follow the steps below to import the file to a catalog.

**Task 1: Import the XML file using the Model Wizard**

1. Run **ModelWizard.bat** in `<install_root>\bin` to open the Object Source Wizard.
2. Select **File** > **Add Table**.
3. In the Add Table dialog box, specify the class and table name. Here, we type **employee** in the **Table Name** text box and specify **ClassName** as **com.jinfonet.jdbc.RecordResult** (a class of Logi Report). Then select the **Parse** button.

   ![Add Table](https://devnet.logianalytics.com/hc/article_attachments/4404848653079/cnctn_jdbc_oojdbc_xml_exmpl1_1.gif)

   The following table shows the explanations about the other options in the dialog box:

   | Option | Description |
   | --- | --- |
   | Column Name | Methods of the class you have defined. |
   | SQL Type | Returned type of your column name. You can double-click the field and choose the SQL type you want. |
   | Precision | Precision of the current column. You can select on the field and change it manually. |
   | Scale | Scale of the current column. You can also select on the field and change it manually. |
   | Nullable | Current status of the column (null or not). You can double-click the field and choose the current status: Nullable, No Nulls, or Nullable Unknown. |
   | Currency | If your DBField contains "$", you should select it. |
   | Add | Select to add new columns. |
   | Remove | Select to remove the specified column. |
   | Modify Column | Select to modify parameters of the current table. |
   | OK | Select to add the table. |
   | Direct Access Path | Select to edit the path for the table. OOJDBC driver can save and restore the table you have defined through this path. |
   | Cancel | Select to cancel the operation and close the Add Table dialog box. |
4. Select the **Remove** button to get rid of all the existing columns in the Add Table dialog box, and then select the **Add** button to add a new column.
5. In the Access Indirect Columns dialog box, specify the data type of the column.

   In this example, we add a column of String type, so select **java.lang.String** in the **ReturnType** column of the **Methods** box, then select the **Add** button. Select **OK** to return to the Add Table dialog box.

   ![Define Access Indirect Columns](https://devnet.logianalytics.com/hc/article_attachments/4404857021719/cnctn_jdbc_oojdbc_xml_exmpl1_2.gif)
6. In the Add Table dialog box, select **Direct Access Path** to define the accessing path of the table in the Access Method dialog box.
   1. In the **Root Class Name** text box, type **com.jinfonet.jdbc.xml.XMLReader**, select the **Parse** button and select **Show Static Methods Only**.
   2. Select the shown method. In the **Parameters** box, specify the default values for param0 and param1. For example, for param0, type in **`file:///C:/Logi Report/Designer/Demo/Reports/TutorialReports/employee.xml`**, and for param1, **record employee root employee column first\_name 12 path document.employee.first\_name**.

      ![Define Access Method](https://devnet.logianalytics.com/hc/article_attachments/4404857021975/cnctn_jdbc_oojdbc_xml_exmpl1_3.gif)

      The following are explanations about the parameters.

      * param0 is the valid XML file name with its path.
      * param1 is the query sentence for selecting the column to be used for reporting from the XML file. record is the keyword, followed with the XML file name (without the extension .xml). Following this is another keyword column with the actual tag name from the XML file.

        See the following code quoted from employee.xml:

        ```
        <employee>  
        <id>0799</id>  
        <first_name>Jack</first_name>   
        <second_name>Smith</second_name>  
        <birthday>12/28/75</birthday>  
        <title>manager</title>  
        <salary>$7000.00</salary>   
        </employee>
        ```

        Since "first\_name" is required, you should then give the actual tag name here. The number is the SQL type of the column. "12" is for String type. For more information about Java SQL types, refer to the JDK package java.sql.types.java.

        ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

        + In param1, the order of the columns is dependent on the default values you have provided when adding the column.
        + Designer does not the following SQL types BINARY, VARBINARY, and LONGVARBINARY.
   3. Select **OK** to return to the Add Table dialog box.
7. Now you can see that the column is added in the Add Table dialog box. You can rename the default column name by editing in the **Column Name** column. You are recommended to give the name as the actual tag definition in the .xml file, for example, first\_name.

   ![Add Table](https://devnet.logianalytics.com/hc/article_attachments/4404857025431/cnctn_jdbc_oojdbc_xml_exmpl1_4.gif)
8. Select the **OK** button, and the table **employee** is now added to the Object Source Wizard.
9. Select **File** > **Save** in the wizard. You are then prompted to save the ODF file. You should save it to  `<install_root>\lib` or the directory where the catalog is (the same ODF file cannot exist in both `<install_root>\lib` and the directory where the catalog is located). Here we save it as **employee.odf**.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* If you use dynamic parameters, that is, you select the Is Dynamic option in the Access Method dialog box, the syntax of the method is an array of Boolean values which indicates which parameter is dynamic at runtime. If the parameter is dynamic, the value should be prompted and initialized before executing an SQL. In addition, when you choose the option Is Dynamic, this parameter is passed to Designer. After you create a connection in the Catalog Manager, you can find it in the Parameters node. For more information, see [Example 3: XML file with dynamic parameters](#Example3).
* If you have purchased the readable key, you can also save the ODF file (oojdbc data definition file) to XML (with extension .odf.xml). For files which have already been saved with an .xml extension, in order to make them available, you can manually change the extension from .xml to .odf.xml.

**Task 2: Import the ODF file into a catalog**

1. Start Designer.
2. Select **File** > **New Catalog**.
3. In the New Catalog dialog box, specify the catalog name, the data source name, and the path. You should store the catalog in the directory where you saved the ODF file. For example, if you saved the ODF file in `C:\odf`, you should save the new catalog in `C:\odf` too.
4. In the Catalog Manager, right-click the node of a data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog box.
5. In the Get JDBC Connection Information dialog box, type **com.jinfonet.jdbc.obj.ObjectDriver** in the **Driver** text box, type **jdbc:jinfonet:object:@Filename** in the **URL** text box. *@Filename* should be the ODF file name. In the example, it is **jdbc:jinfonet:object:@employee**.

   ![Specify JDBC Connection Information](https://devnet.logianalytics.com/hc/article_attachments/4404848653591/cnctn_jdbc_oojdbc_xml_exmpl1_5.gif)
6. Select **OK** to set up the connection.
7. In the Add Tables/SQL dialog box, select **Add Tables** (if Designer does not display the dialog box, select **Resume** on the Catalog Manager toolbar).
8. In the Add Tables/Views/Synonyms dialog box, select the table **employee** and select **Add**.

   ![Add the Table](https://devnet.logianalytics.com/hc/article_attachments/4404857025687/cnctn_jdbc_oojdbc_xml_exmpl1_6.gif)
9. Select **Done** to close the Add Tables dialog box.

By now, you have added the table "employee" into the catalog. You can use it to create a query or business view and then develop reports as required. When you publish the catalog and reports to Server, whether the ODF file is located in `<install_root>\lib` or in the directory where the catalog is located, Designer publishes it to the path where the catalog is located in the Server side.

### Example 2: Importing the XML File Directly

The process of importing an XML file with the Model Wizard as explained in [Example 1](#Example1) can be simplified with Logi Report's built-in XML file import functionality.

This example uses orgchart\_data.xml in `<install_root>\help\samples\OOJDBC`. Store the file to `<install_root>\Demo\Reports\TutorialReports` first. Then follow the steps below to import the file to a catalog.

**Task 1: Import the XML file directly using the Model Wizard**

1. Run **ModelWizard.bat** in `<install_root>\bin` to open the Object Source Wizard.
2. Select **File** > **Import XML Files**. Designer displays the Import XML dialog box.
3. Select **Open** to browse to the file **orgchart\_data.xml**.
4. You can select **Column** for all elements and change their format and type.

   ![Import XML](https://devnet.logianalytics.com/hc/article_attachments/4404848653847/cnctn_jdbc_oojdbc_xml_exmpl2_1.gif)

   When using certain SQL types, you should specify a standard format. There are some examples:

   * If the time format is like Tue Aug 27 16:04:00 BST 2002, you should select:   
     **Type**: Timestamp  
     **Format**: EEE MMM dd hh:mxm:ss zzz yyyy
   * If the time format is like 2002-11-22 11:09:08, you should select:  
     **Type**: Timestamp  
     **Format**: yyyy-MM-dd hh:mm:ss
   * If the time format is like 11/18/2002 08:20:00, you should select  
     **Type**: Timestamp  
     **Format**: M/d/yyyy hh:mm:ss
   * If the time format is like 1999-12-05, you should select:  
     **Type**: date  
     **Format**: yyyy-MM-dd
   * If the time format is like 08:20:00, you should select:   
     **Type**: time  
     **Format**: hh:mm:ss
   * If the number is like 50,600, you should select:  
     **Type**: integer  
     **Format**: ###,###
   * If the currency is like $50,600, you should select:  
     **Type**: integer  
     **Format**: $###,###
5. Select **OK** and the table **OrgChart** is added to the Object Source Wizard.
6. Select **File** > **Save** in the wizard. You are then prompted to save the ODF file. You should save it to `<install_root>\lib` or to the directory where the catalog is located (the same ODF file cannot exist in both `<install_root>\lib` and the directory where the catalog is located). Here, we save it as **orgchart.odf**.

**Task 2: Import the ODF file into a catalog**

1. Start Designer.
2. Select **File** > **New Catalog**.
3. In the New Catalog dialog box, specify the catalog name, the data source name, and the path. You should store the catalog in the directory where you saved the ODF file. For example, if you saved the ODF file in `C:\odf`, you should save the new catalog in `C:\odf` too.
4. In the Catalog Manager, right-click the data source node and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog box.
5. In the Get JDBC Connection Information dialog box, type **com.jinfonet.jdbc.obj.ObjectDriver** in the **Driver** text box, type **jdbc:jinfonet:object:@Filename** in the **URL** text box. *@Filename* should be the ODF file name. In the example, it is **jdbc:jinfonet:object:@orgchart**.

   ![Specify JDBC Connection Information](https://devnet.logianalytics.com/hc/article_attachments/4404857026071/cnctn_jdbc_oojdbc_xml_exmpl2_2.gif)
6. Select **OK** to set up the connection.
7. In the Add Tables/SQL dialog box, select **Add Tables** (if Designer does not display the dialog box, select **Resume** on the Catalog Manager toolbar).
8. In the Add Tables/Views/Synonyms dialog box, select the table **OrgChart** and select **Add**.
9. Select **Done** to close the Add Tables dialog box.

By now, you have added the table "OrgChart" into the catalog. You can use it to create a query or business view and then develop reports as required. When you publish the catalog and reports to Server, whether the ODF file is located in `<install_root>\lib` or in the directory where the catalog is located, Designer publishes it to the path where the catalog is located in the Server side.

### Example 3: XML File with Dynamic Parameters

When you design a report from the tables imported through OOJDBC, and the tables have the same input parameters, but you don't want to input the same parameters again, Designer provides a way to enable you to bind parameters in a catalog, so they can share the same parameter value.

This example demonstrates how to import tables with dynamic parameters from the ODF file generated by the Model Wizard.

**Task 1: Import the XML file using the Model Wizard**

1. Run **ModelWizard.bat** in `<install_root>\bin` to open the Object Source Wizard.
2. Add two tables as shown in [Example 1](#Example1). The first table named "employee1" has one String type column, and the second table named "employee2" has one Int type column. They have the same input parameter for param0. The default value is `h:\xml\employee.xml`. Make sure to select the option **Is Dynamic**.
3. In the Object Source Wizard, select **File** > **Save**. You are then prompted to save the ODF file. You should save it to `<install_root>\lib` or the directory where the catalog is (the same ODF file cannot exist in `both <install_root>\lib` and the directory where the catalog is located). Here we save it as **xmlparam.odf**.

**Task 2: Import the ODF file into a catalog**

1. Start Designer.
2. Select **File** > **New Catalog**.
3. In the New Catalog dialog box, specify the catalog name, the data source name, and the path. You should store the catalog in the directory where you saved the ODF file. For example, if you saved the ODF file in `C:\odf`, you should save the new catalog in `C:\odf` too.
4. In the Catalog Manager, [create a parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010099761-Creating-Parameters-in-a-Catalog) in an existing catalog data source that is of the String data type and is named "path". This parameter is bound to the parameters in the tables that you import through OOJDBC.

   ![Create a Parameter](https://devnet.logianalytics.com/hc/article_attachments/4404848654103/cnctn_jdbc_oojdbc_xml_exmpl3_1.gif)
5. Right-click the node of the same catalog data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog box.
6. In the Get JDBC Connection Information dialog box, type **com.jinfonet.jdbc.obj.ObjectDriver** in the **Driver** text box, type **jdbc:jinfonet:object:@Filename** in the **URL** text box. *@Filename* should be the ODF file name. In the example, it is **jdbc:jinfonet:object:@xmlparam**.

   ![Specify JDBC Connection Information](https://devnet.logianalytics.com/hc/article_attachments/4404848654359/cnctn_jdbc_oojdbc_xml_exmpl3_2.gif)
7. Select **OK** to set up the connection.
8. In the Add Tables/SQL dialog box, select **Add Tables** (if Designer does not display the dialog box, select **Resume** on the Catalog Manager toolbar).
9. In the Add Tables/Views/Synonyms dialog box, select the table **employee1** and select the **Add** button. Designer display the Dynamic Parameter used in oojdbc tables dialog box. Clear the checkbox in the **New** column and select the parameter **path** from the drop-down list to bind param0 to the parameter path.

   ![Dynamic Parameters Used in Table](https://devnet.logianalytics.com/hc/article_attachments/4404848654743/cnctn_jdbc_oojdbc_xml_exmpl3_3.gif)
10. Repeat the above step to add the **employee2** table and bind its parameter **param0** to the parameter **path**. Now the parameters in the two tables share the same parameter.
11. [Create a query](https://devnet.logianalytics.com/hc/en-us/articles/1500010062582-Creating-Queries-in-a-Catalog) on the newly inserted tables and [create a page report](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#Page) using the query.
12. When you preview the report, Designer displays the Enter Parameter Values dialog box, asking you to specify the parameter. You only need to type in the path of the imported XML file once, since the parameter is shared with the parameters in the two tables.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) You can modify the links between the parameters in OOJDBC and parameters in the catalog. To do this:

1. In the Catalog Manager, select the table with the dynamic parameters that are to be modified.
2. Right-click on the selected table, and select **Parameters** from the shortcut menu.
3. Highlight the parameter in the catalog, and then select the parameter from the drop-down list to bind it to the parameter in OOJDBC.

## Using Class File as Data Source via OOJDBC

This example shows how to generate the ODF file in a different way using the file **demo.zip** in `<install_root>\help\samples\OOJDBC`, which contains all the necessary classes and methods needed for making the OOJDBC data source work with Java objects.

**Preparations**

Before the OOJDBC data source works with Java objects, you should do the preparations:

1. You should define a class that specifies the column name and the method of getting data from this column. In this example, the class **Products.java** in demo.zip takes this role. This class file contains the method *public int getProductID()*, which implies that the column name is **ProductID** and you can get the product ID via this method.
2. You should publish a method to access a group of products. That means OOJDBC needs a result set with multiple rows, and each row is one of the products, so that you should define a class that can retrieve the rows. In this example, the file **SQLReader.java** in demo.zip takes this role. In this file, there is a static\* method *JCollection execSQL(String jdbcDriver, String url, String sql)*, and this method returns a collection that contains the rows of the products. This collection class is **com.jinfonet.jdbc.obj.JCollection**.

Also, you should edit the batch files used to start the Model Wizard, Designer, and Server before you can import the product table and use it to generate reports. To do this:

1. Save demo.zip in `<install_root>\help`.
2. Add it to the class path of the batch file **setenv.bat** in `<install_root>\bin` of both Designer and Server. setenv.bat updates the class path for both the Model Wizard and Designer.

**Task 1 : Import the class file using the Model Wizard**

1. Run **ModelWizard.bat** in `<install_root>\bin` to open the Object Source Wizard.
2. Select **Add Table**.
3. In the **ClassName** field of the Add Table dialog box, type **com.jinfonet.jdbc.demo.Products**, type **demo** in the **Table Name** text box, and then select the **Parse** button.
4. Select **Direct Access Path**.
5. In the Access Method dialog box, type **com.jinfonet.jdbc.demo.SQLReader** in the **Root Class Name** text box, then select the **Parse** button. In the **Methods** box, select the method **execSQL**, and in the **Parameters** box, type in the default values as follows:

   Param0 (the driver of the database): org.hsqldb.jdbcDriver  
   Param1 (the connection URL of the database): `jdbc:hsqldb:C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\Demo\db\JRDemo`  
   Param2 (the user name): sa  
   Param3 (the password): (no value)  
   Param4 (the SQL statement): select \* from products
6. Press the **OK** button and the table **demo** is added to the Object Source Wizard.
7. Select **File** > **Save** in the wizard. You are then prompted to save the ODF file. You should save it to `<install_root>\lib` or the directory where the catalog is (the same ODF file cannot exist in both `<install_root>\lib` and the directory where the catalog is located). Here we save it as **demo.odf**.

**Task 2 : Import the ODF file into a catalog**

1. Start Designer.
2. Select **File** > **New Catalog**.
3. In the Catalog Name dialog box, specify the catalog name, the data source name, and the path. You should store the catalog in the directory where you saved the ODF file. For example, if you saved the ODF file in `C:\odf`, you should save the new catalog in `C:\odf` too.
4. In the Catalog Manager, right-click the node of a data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog box.
5. In the Get JDBC Connection Information dialog box, type **com.jinfonet.jdbc.obj.ObjectDriver** in the **Driver** text box, type **jdbc:jinfonet:object:@Filename** in the **URL** text box. *@Filename* should be the .odf name you have saved but do not include the extension. In the example, it should be **jdbc:jinfonet:object:@demo**.
6. Select **OK** to set up the connection.
7. In the Add Tables/SQL dialog box, select **Add Tables** (if Designer does not display the dialog box, select **Resume** on the Catalog Manager toolbar).
8. In the Add Tables/Views/Synonyms dialog box, select the table **demo** and select **Add**.
9. Select **Done** to close the Add Tables dialog box.

By now, you have added the table "demo" into the catalog. You can use it to create a query or business view and then develop reports as required. When you publish the catalog and reports to Server, whether the ODF file is located in `<install_root>\lib` or in the directory where the catalog is located, Designer publishes it to the path where the catalog is located in the Server side.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) Logi Report provides an interface com.jinfonet.interfaces.query.TableFilter and a simple implementation com.jinfonet.jdbc.obj.TableFilterImpl, which you can use in this example to improve the performance of the select and WHERE clauses in a query. You can extend TableFilterImpl to create your own Reader class. In addition, Logi Report provides the demo FilterSQLReader.java in the file demo.zip for your reference. However if you are using FilterSQLReader.java instead of SQLReader.java, you should type **com.jinfonet.jdbc.demo.FilterSQLReader** in the Root Class Name text box of the Access Method dialog box.

## Using CSV File as Data Source via OOJDBC

Designer supports CSV as data sources which can be accessed via OOJDBC. You can use this method to import Excel files by using Excel to save the report as .csv.

The following example demonstrates how to import a CSV file to an ODF file generated by the Model Wizard. This example uses employee.csv in `<install_root>\help\samples\OOJDBC`. Store it to `<install_root>\Demo\Reports\TutorialReports` first. Then follow the steps below to import the file to a catalog.

**Task 1: Import the CSV file directly using the Model Wizard**

1. Run **ModelWizard.bat** in `<install_root>\bin` to open the Object Source Wizard.
2. Select **File** > **Import Text Files**.
3. In the Open Text Files dialog box, browse to the file **employee.csv** and then select the **First Line Is Column Name** checkbox.

   ![Open Text Files dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404857027223/cnctn_jdbc_oojdbc_csv_open.gif)
4. Select **Open** and the table **Employee** is added to the Object Source Wizard.

   ![Object Source Wizard](https://devnet.logianalytics.com/hc/article_attachments/4404857027479/cnctn_jdbc_oojdbc_csv_wzd.gif)
5. Select **File** > **Save** in the wizard. You are then prompted to save the ODF file. You should save it to `<install_root>\lib` or to the directory where the catalog is (the same ODF file cannot exist in both `<install_root>\lib` and the directory where the catalog is located). Here, we save it as **employee\_csv.odf**.

**Task 2: Import the ODF file into a catalog**

1. Start Designer.
2. Select **File** > **New Catalog**.
3. In the New Catalog dialog box, specify the catalog name, the data source name, and the path. You should store the catalog in the directory where you saved the ODF file. For example, if you saved the ODF file in `C:\odf`, you should save the new catalog in `C:\odf` too.
4. In the Catalog Manager, right-click the node of a data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog box.
5. In the Get JDBC Connection Information dialog box, type **com.jinfonet.jdbc.obj.ObjectDriver** in the **Driver** text box, type **jdbc:jinfonet:object:@Filename** in the **URL** text box. *@Filename* should be the ODF file name. In the example, it is **jdbc:jinfonet:object:@employee\_csv**.

   ![Get JDBC Connection Information dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404857027735/cnctn_jdbc_oojdbc_csv_jdbc.gif)
6. Select **OK** to set up the connection.
7. In the Add Tables/SQL dialog box, select **Add Tables** (if Designer does not display the dialog box, select **Resume** on the Catalog Manager toolbar).
8. In the Add Tables/Views/Synonyms dialog box, select the table **Employee** and select **Add**.
9. Select **Done** to close the Add Tables dialog box.

By now, you have added the table "Employee" into the catalog. You can use it to create a query or business view and then develop reports as required. When you publish the catalog and reports to Server, whether the ODF file is located in `<install_root>\lib` or in the directory where the catalog is located, Designer publishes it to the path where the catalog is located in the Server side.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010095181-Using-Imported-SQLs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095241-Connecting-via-JSON-Connections)
