---
title: "Using Data Sources via OOJDBC"
id: 1500010064381
section: "Connecting to Your Data Sources - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010064381-Using-Data-Sources-via-OOJDBC
updated_at: 2021-07-24T10:39:15Z
---

# Using Data Sources via OOJDBC

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064341-Imported-SQL-Files) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010029482-JSON-Connections)

# Using Data Sources via OOJDBC

OOJDBC (Object Oriented Java Database Connection) is defined to cover an OODS (Object Oriented Data Source) with a JDBC interface. It is similar to a JDBC driver and is based on a Java application, EJB (Enterprise Java Bean), LDAP (Light Weight Directory Access Protocol), which can be defined as a database. Logi JReport provides a tool named Model Wizard, which you can run to import data via an OOJDBC data source.

Below is a list of the sections covered in this topic:

* [Main Frame for OOJDBC in Logi JReport](#Frame)
* [Using XML File as Data Source via OOJDBC](#XML)
  + [Example 1: Importing the XML File Indirectly](#Example1)
  + [Example 2: Importing the XML File Directly](#Example2)
  + [Example 3: XML File with Dynamic Parameters](#Example3)
* [Using Class File as Data Source via OOJDBC](#Class)
* [Using CSV File as Data Source via OOJDBC](#CSV)

## Main Frame for OOJDBC in Logi JReport

OOJDBC in Logi JReport includes Model Wizard and OOJDBC Driver.

* **Model Wizard**  
   Open/Save model file  
   Define a Java class as a table  
   Define a method as a column  
   How to access the instance of the class
* **OOJDBC Driver**  
   Read the table/column definitions from model file  
   Return meta-data to Logi JReport  
   Construct QUERY data  
   Return record to Logi JReport

![Diagram of the main frame for OOJDBC](https://devnet.logianalytics.com/hc/article_attachments/4404909262999/cnctn_jdbc_oojdbc.gif)

## Using XML File as Data Source via OOJDBC

Logi JReport Designer supports accessing XML data sources via OOJDBC. Logi JReport also supports using XML directly which is recommended over using OOJDBC (see [XML Connections](https://devnet.logianalytics.com/hc/en-us/articles/1500010064581-XML-Connections)).

### Example 1: Importing the XML File Indirectly

In this example, employee.xml in `<install_root>\help\samples\OOJDBC` is used. Store it to `<install_root>\Demo\Reports\TutorialReports` first. Then follow the steps below to import the file to a catalog.

**Task 1: Import the XML file using the Model Wizard**

1. Run ModelWizard.bat in `<install_root>\bin` to open the Object Source Wizard.
2. Select **File** > **Add Table**.
3. In the Add Table dialog, specify the class and table name as required. Here, we fill in the Table Name as **employee** and ClassName as **com.jinfonet.jdbc.RecordResult** (a class of Jinfonet). Then select the **Parse** button.

   ![Add Table](https://devnet.logianalytics.com/hc/article_attachments/4404901306391/cnctn_jdbc_oojdbc_xml_exmpl1_1.gif)

   Below are explantions about the options in the dialog:

   | Options | Description |
   | --- | --- |
   | Column Name | Methods of the class you have defined. |
   | SQL Type | Returned type of your column name. You can double-click the field and choose the SQL type you want. |
   | Precision | Precision of the current column. You can select on the field and change it manually. |
   | Scale | Scale of the current column. You can also select on the field and change it manually. |
   | Nullable | Current status of the column (null or not). You can double-click on the field and choose the current status: Nullable, No Nulls or Nullable Unknown. |
   | Currency | If your DBField contains $, you should check it. |
   | Add | Adds new columns. |
   | Remove | Removes the selected column. |
   | Modify Column | Modifies parameters of the current table. |
   | OK | Adds the table. |
   | Direct Access Path | Specifies the path for the table. OOJDBC driver can save and restore the table you have defined through this path. |
   | Cancel | Cancels the operation and closes the Add Table dialog. |
4. Select the **Remove** button to get rid of all the existing columns in the Add Table dialog, and then select the **Add** button to add a new column.
5. In the Access Indirect Columns dialog, specify the data type of the column.

   In this example, we will add a column of String type, so select **java.lang.String** in the ReturnType column of the Methods box, then select the **Add** button. Select **OK** to return to the Add Table dialog.

   ![Define Access Indirect Columns](https://devnet.logianalytics.com/hc/article_attachments/4404909263255/cnctn_jdbc_oojdbc_xml_exmpl1_2.gif)

   **Note:** If you want to use dynamic parameter, you can choose the option Is Dynamic in the Access Indirect Columns dialog. For details, see [Example 3: XML file with dynamic parameters](#Example3).
6. In the Add Table dialog, select **Direct Access Path** to define the accessing path of the table in the Access Method dialog.
   1. Fill in **com.jinfonet.jdbc.xml.XMLReader** in the Root Class Name text box, select the **Parse** button and check **Show Static Methods Only**.
   2. Select the shown method. In the Parameters box, fill in the default values for param0 and param1 as required. For example, for param0, fill in **`file:///C:/Logi JReport/Designer/Demo/Reports/TutorialReports/employee.xml`**, then for param1, fill in **record employee root employee column first\_name 12 path document.employee.first\_name**.

      ![Define Access Method](https://devnet.logianalytics.com/hc/article_attachments/4404909263639/cnctn_jdbc_oojdbc_xml_exmpl1_3.gif)

      The following are explanations about the parameters.

      * param0 is the valid XML file name with its path.
      * param1 is the query sentence for selecting the column to be used for reporting from the XML file. record is the keyword, followed with the XML file name (without the extension .xml). Following this is another keyword column with the actual tag name from the XML file.

        Below is the part quoted from employee.xml:

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

        Since first\_name is required, you should then give the actual tag name here. The number afterwards is the SQL type of the column. "12" is for String type. For detailed information about Java SQL types, refer to the JDK package java.sql.types.java.

        **Notes:**

        + In param1, the order of the columns is dependent on the default values given when adding the column.
        + The SQL type BINARY, VARBINARY and LONGVARBINARY are not supported.
   3. Select **OK** to return to the Add Table dialog.
7. Now you can see that the column has been added in the Add Table dialog. You can rename the default column name by editing in the Column Name column. You are recommended to give the name as the actual tag definition in the .xml file, for example first\_name.

   ![Add Table](https://devnet.logianalytics.com/hc/article_attachments/4404909263895/cnctn_jdbc_oojdbc_xml_exmpl1_4.gif)
8. Select the **OK** button, and the table employee will now have been added to the Object Source Wizard.
9. Select **File** > **Save** in the wizard. You will then be prompted to save the ODF file. You should save it to `<install_root>\lib` or the directory where the catalog will be. Here we save it as employee.odf.

**Notes:**

* If you use dynamic parameters, that is you check the Is Dynamic option, the syntax of the method is an array of Boolean values which indicates which parameter is dynamic at runtime. If the parameter is dynamic the value should be prompted and initialized before executing an SQL. In addition, when you choose the option Is Dynamic, this parameter will be passed to Logi JReport Designer. After you create a connection in the Catalog Manager, you will find it in the Parameters node.
* The same ODF file cannot exist in both  `<install_root>\lib` and the directory where the catalog is located.
* If you have purchased the readable key, you can also save the ODF file (oojdbc data definition file) to XML format (with extension .odf.xml). For files which have already been saved with an .xml extension, in order to make them available, you can manually change the extension from .xml to .odf.xml.

**Task 2: Import the ODF file into a catalog**

1. Start Logi JReport Designer.
2. Select  **File** > **New Catalog**.
3. In the New Catalog dialog, specify the catalog name, the data source name and the path. The catalog should be located in the directory where you saved the ODF file. For example, if you saved the ODF file in `C:\odf`, the new catalog should be created also in `C:\odf`.
4. In the Catalog Manager, right-click the node of a data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.
5. In the Get JDBC Connection Information dialog, enter **com.jinfonet.jdbc.obj.ObjectDriver** in the Driver text box, type **jdbc:jinfonet:object:@Filename** in the URL text box. @Filename should be the ODF file name. In the example, it is jdbc:jinfonet:object:@employee.

   ![Specify JDBC Connection Information](https://devnet.logianalytics.com/hc/article_attachments/4404909264151/cnctn_jdbc_oojdbc_xml_exmpl1_5.gif)
6. Select **OK** to set up the connection.
7. In the Add Tables/SQL dialog, select **Add Tables** (if the dialog is not displayed, select **Resume** on the Catalog Manager toolbar).
8. In the Add Tables/Views/Synonyms dialog, select the table **employee** and select **Add**.

   ![Add the Table](https://devnet.logianalytics.com/hc/article_attachments/4404901306647/cnctn_jdbc_oojdbc_xml_exmpl1_6.gif)
9. Select **Done** to close the Add Tables dialog.

Now, the table employee will have been added into the catalog. You can use it to develop reports as required.

**Note:** When you publish the catalog and its reports to Logi JReport Server, whether the ODF file is located in `<install_root>\lib` or in the directory where the catalog is located, it will be deployed to the path where the catalog is located in the server side.

### Example 2: Importing the XML File Directly

The process of importing an XML file with Model Wizard (as explained in [Example 1](#Example1)) can be simplified with Logi JReport's built-in XML file import functionality, and is very easy to use.

In this example, orgchart\_data.xml in `<install_root>\help\samples\OOJDBC` is used. Store it to `<install_root>\Demo\Reports\TutorialReports` first. Then follow the steps below to import the file to a catalog.

**Task 1: Import the XML file directly using the Model Wizard**

1. Run ModelWizard.bat in `<install_root>\bin` to open the Object Source Wizard.
2. Select **File** > **Import XML Files** to bring up the Import XML dialog.
3. Select **Open** to browse to the file orgchart\_data.xml.
4. Check **Column** for all elements and change their format and type if necessary.

   ![Import XML](https://devnet.logianalytics.com/hc/article_attachments/4404909264407/cnctn_jdbc_oojdbc_xml_exmpl2_1.gif)

   When using certain SQL types, you should input a standard format. There are some examples:

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
5. Select **OK** and the table OrgChart will now have been added to the Object Source Wizard.
6. Select **File** > **Save** in the wizard. You will then be prompted to save the ODF file. You should save it to `<install_root>\lib` or to the directory where the catalog will be located. Here, we save it as orgchart.odf.

   **Note:** The same ODF file cannot exist in `both <install_root>\lib` and the directory where the catalog will be located.

**Task 2: Import the ODF file into a catalog**

1. Start Logi JReport Designer.
2. Select **File** > **New Catalog**.
3. In the New Catalog dialog, specify the catalog name, the data source name and the path. The catalog should be located in the directory where you saved the ODF file. For example, if you saved the ODF file in `C:\odf`, the new catalog should be created also in `C:\odf`.
4. In the Catalog Manager, right-click the data source node and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.
5. In the Get JDBC Connection Information dialog, enter **com.jinfonet.jdbc.obj.ObjectDriver** in the Driver text box, type **jdbc:jinfonet:object:@Filename** in the URL text box. @Filename should be the ODF file name. In the example, it is jdbc:jinfonet:object:@orgchart.

   ![Specify JDBC Connection Information](https://devnet.logianalytics.com/hc/article_attachments/4404909264663/cnctn_jdbc_oojdbc_xml_exmpl2_2.gif)
6. Select **OK** to set up the connection.
7. In the Add Tables/SQL dialog, select **Add Tables** (if the dialog is not displayed, select **Resume** on the Catalog Manager toolbar).
8. In the Add Tables/Views/Synonyms dialog, select the table **OrgChart** and select **Add**.
9. Select **Done** to close the Add Tables dialog.

Now, the table OrgChart will be added into the catalog. You can use it to develop reports as required.

**Note:** When you publish the catalog and its reports to Logi JReport Server, whether the ODF file is located in `<install_root>\lib` or in the directory where the catalog is located, it will be deployed to the path where the catalog is located on the server side.

### Example 3: XML File with Dynamic Parameters

When you design a report from the tables imported through OOJDBC, and the tables have the same input parameters, but you don't want to input the same parameters again, Logi JReport provides a way to allow you to bind parameters in a catalog, so they can share the same parameter value.

This example demonstrates how to import tables with dynamic parameters from the ODF file generated by the Model Wizard.

**Task 1: Import the XML file using the Model Wizard**

1. Run ModelWizard.bat in `<install_root>\bin` to open the Object Source Wizard.
2. Add two tables as shown in [Example 1](#Example1). The first table named employee1 has one String type column, and the second table named employee2 has one Int type column. They have the same input parameter for param0. The default value is `h:\xml\employee.xml`. Make sure to check the option Is Dynamic.
3. In the Object Source Wizard, select **File** > **Save**. You will then be prompted to save the ODF file. You should save it to `<install_root>\lib` or the directory where the catalog will be. Here we save it as xmlparam.odf.

**Notes:**

* If you choose the option Is Dynamic, this parameter will be passed to Logi JReport Designer. After you create a new connection, you will find this parameter in the node Parameters in the Catalog Manager.
* The same ODF file cannot exist in `both <install_root>\lib` and the directory where the catalog is to be located.

**Task 2: Import the ODF file into a catalog**

1. Start Logi JReport Designer.
2. Select **File** > **New Catalog**.
3. In the New Catalog dialog, specify the catalog name, the data source name and the path. The catalog should be located in the directory where you saved the ODF file. For example, if you saved the ODF file in `C:\odf`, the new catalog should be created also in `C:\odf`.
4. In the Catalog Manager, [create a parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010069001-Creating-Parameters-in-a-Catalog) in an existing catalog data source that is of String data type and is named path. This parameter will be bound to the parameters in the tables that were imported through OOJDBC.

   ![Create a Parameter](https://devnet.logianalytics.com/hc/article_attachments/4404901306903/cnctn_jdbc_oojdbc_xml_exmpl3_1.gif)
5. Right-click the node of the same catalog data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.
6. In the Get JDBC Connection Information dialog, enter **com.jinfonet.jdbc.obj.ObjectDriver** in the Driver text box, type **jdbc:jinfonet:object:@Filename** in the URL text box. @Filename should be the ODF file name. In the example, it is jdbc:jinfonet:object:@xmlparam.

   ![Specify JDBC Connection Information](https://devnet.logianalytics.com/hc/article_attachments/4404909264919/cnctn_jdbc_oojdbc_xml_exmpl3_2.gif)
7. Select **OK** to set up the connection.
8. In the Add Tables/SQL dialog, select **Add Tables** (if the dialog is not displayed, select **Resume** on the Catalog Manager toolbar).
9. The Add Tables/Views/Synonyms dialog appears prompting you to add the listed tables. Select the table **employee1** and select the **Add** button. The Dynamic Parameter used in oojdbc tables dialog will then be displayed. Uncheck the checkbox in the New column and select the parameter path from the drop-down list to bind param0 to the parameter path.

   ![Dynamic Parameters Used in Table](https://devnet.logianalytics.com/hc/article_attachments/4404901307159/cnctn_jdbc_oojdbc_xml_exmpl3_3.gif)
10. Repeat the above step to add the employee2 table and bind its parameter param0 to the parameter path. Now the parameters in the two tables will share the same parameter.
11. [Create a page report](https://devnet.logianalytics.com/hc/en-us/articles/1500010034782-Creating-Reports#Page) on the newly inserted tables.
12. When viewing the report, the Enter Parameter Values dialog will be displayed, asking you to input the parameter. You will only need to input the path of imported XML file once since the parameter is shared with the parameters in the two tables.

**Tip:** You can modify the links between the parameters in OOJDBC and parameters in the Logi JReport catalog.

1. In the Catalog Manager, select the table with the dynamic parameters that are to be modified.
2. Right-click on the selected table, and select **Parameters** from the shortcut menu.
3. Highlight the parameter in the catalog, and then select the parameter from the drop-down list to bind it to the parameter in OOJDBC.

## Using Class File as Data Source via OOJDBC

This topic provides an example about how to generate the ODF file in a different way using the file demo.zip in `<install_root>\help\samples\OOJDBC`, which contains all the necessary classes and methods needed for making the OOJDBC data source work with Java objects.

**Preparations**

Before the OOJDBC data source works with Java objects, you should do the preparations:

1. You should define a class that specifies the column name and the method of getting data from this column. In this example, the class Products.java in demo.zip takes this role. This class file contains the method *public int getProductID()*, which implies that the column name is ProductID and you can get the product ID via this method.
2. You should publish a method to access a group of products. That means OOJDBC needs a result set with multiple rows, and each row is one of the products, so that you should define a class that can retrieve the rows. In this example, the file SQLReader.java in demo.zip takes this role. In this file, there is a static\* method *JCollection execSQL(String jdbcDriver, String url, String sql)*, and this method returns a collection that contains the rows of the products. This collection class is com.jinfonet.jdbc.obj.JCollection.

Also, the batch files used to start the Model Wizard, Logi JReport Designer and Logi JReport Server should be modified before you can import the product table and use it to generate reports. To do this:

1. Save demo.zip in `<install_root>\help`.
2. Add it to the class path of the batch file setenv.bat in `<install_root>\bin` of both Designer and Server. setenv.bat updates the class path for both the Model Wizard and Logi JReport Designer.

**Task 1 : Import the class file using the Model Wizard**

1. Run ModelWizard.bat in `<install_root>\bin` to open the Object Source Wizard.
2. Select **Add Table** and the Add Table dialog will be displayed.
3. In the ClassName field, type **com.jinfonet.jdbc.demo.Products**, input **demo** in the Table Name field, and then select the **Parse** button.
4. Select **Direct Access Path**. In the Access Method dialog, input **com.jinfonet.jdbc.demo.SQLReader** in the Root Class Name field. Then select the **Parse** button. In the Methods box, select the method **execSQL**, and in the Parameters box, fill in the default values as follows:

   Param0 (the driver of the database): org.hsqldb.jdbcDriver  
   Param1 (the connection URL of the database): `jdbc:hsqldb:c:\JReport\Designer\Demo\db\JRDemo`  
   Param2 (the user name): sa  
   Param3 (the password): (no value)  
   Param4 (the SQL statement): select \* from products
5. Press the **OK** button and the table demo will now have been added to the Object Source Wizard.
6. Select **File** > **Save** in the wizard. You will then be prompted to save the ODF file. You should save it to `<install_root>\lib` or the directory where the catalog will be. Here we save it as demo.odf.

**Note:** The same ODF file cannot exist in both `<install_root>\lib` and the directory where the catalog is located.

**Task 2 : Import the ODF file into a catalog**

1. Start Logi JReport Designer.
2. Select **File** > **New Catalog**.
3. In the Catalog Name dialog, specify the catalog name, the data source name and the path. The catalog should be located in the directory where you saved the ODF file. For example, if you saved the ODF file in `C:\odf`, the new catalog should be created also in `C:\odf`.
4. In the Catalog Manager, right-click the node of a data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.
5. In the Get JDBC Connection Information dialog, enter **com.jinfonet.jdbc.obj.ObjectDriver** in the Driver text box, type **jdbc:jinfonet:object:@Filename** in the URL text box. @Filename should be the .odf name you have saved but do not include the extension. So in the example, it should be jdbc:jinfonet:object:@demo.
6. Select **OK** to set up the connection.
7. In the Add Tables/SQL dialog, select **Add Tables** (if the dialog is not displayed, select **Resume** on the Catalog Manager toolbar).
8. In the Add Tables/Views/Synonyms dialog, select the table **demo** and select **Add**.
9. Select **Done** to close the Add Tables dialog.

Now, the table demo has been added into the catalog. You can use it to develop reports as required.

**Note:** When you publish the catalog and its reports to Logi JReport Server, whether the ODF file is located in `<install_root>\lib` or in the directory where the catalog is located, it will be published to the path where the catalog is located on the server side.

**Tip:** Logi JReport provides an interface com.jinfonet.interfaces.query.TableFilter and a simple implementation com.jinfonet.jdbc.obj.TableFilterImpl, which can be used in this example to improve the performance of the select and WHERE clauses in a query. You can extend TableFilterImpl to create your own Reader class. In addition, a demo FilterSQLReader.java in the file demo.zip has been made for your reference. However if you are using FilterSQLReader.java instead of SQLReader.java, you should input com.jinfonet.jdbc.demo.FilterSQLReader in the Root Class Name field of the Access Method dialog.

## Using CSV File as Data Source via OOJDBC

Logi JReport Designer supports CSV as data sources which can be accessed via OOJDBC. You can use this method to import Excel files by using Excel to save the report as .csv.

The following example demonstrates how to import a CSV file to an ODF file generated by the Model Wizard. In this example, employee.csv in `<install_root>\help\samples\OOJDBC` is used. Store it to `<install_root>\Demo\Reports\TutorialReports` first. Then follow the steps below to import the file to a catalog.

**Task 1: Import the CSV file directly using the Model Wizard**

1. Run ModelWizard.bat in `<install_root>\bin` to open the Object Source Wizard.
2. Select **File** > **Import Text Files** to bring up the Open Text Files dialog.
3. Browse to the file employee.csv and then check the **First Line Is Column Name** checkbox.

   ![Open Text Files dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901307415/cnctn_jdbc_oojdbc_csv_open.gif)
4. Select **Open** and the table Employee will now have been added to the Object Source Wizard.

   ![Object Source Wizard](https://devnet.logianalytics.com/hc/article_attachments/4404901307671/cnctn_jdbc_oojdbc_csv_wzd.gif)
5. Select **File** > **Save** in the wizard. You will then be prompted to save the ODF file. You should save it to `<install_root>\lib` or to the directory where the catalog will be located. Here, we save it as employee\_csv.odf.

   **Note:** The same ODF file cannot exist in both `<install_root>\lib` and the directory where the catalog will be located.

**Task 2: Import the ODF file into a catalog**

1. Start Logi JReport Designer.
2. Select **File** > **New Catalog**.
3. In the New Catalog dialog, specify the catalog name, the data source name and the path. The catalog should be located in the directory where you saved the ODF file. For example, if you saved the ODF file in `C:\odf`, the new catalog should be created also in `C:\odf`.
4. In the Catalog Manager, right-click the node of a data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.
5. In the Get JDBC Connection Information dialog, enter **com.jinfonet.jdbc.obj.ObjectDriver** in the Driver text box, type **jdbc:jinfonet:object:@Filename** in the URL text box. @Filename should be the ODF file name. In the example, it is jdbc:jinfonet:object:@employee\_csv.

   ![Get JDBC Connection Information dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909265175/cnctn_jdbc_oojdbc_csv_jdbc.gif)
6. Select **OK** to set up the connection.
7. In the Add Tables/SQL dialog, select **Add Tables** (if the dialog is not displayed, select **Resume** on the Catalog Manager toolbar).
8. In the Add Tables/Views/Synonyms dialog, select the table **Employee** and select **Add**.
9. Select **Done** to close the Add Tables dialog.

Now, the table Employee will be added into the catalog. You can use it to create query or business view and then develop reports as required.

**Note:** When you publish the catalog and its reports to Logi JReport Server, whether the ODF file is located in `<install_root>\lib` or in the directory where the catalog is located, it will be published to the path where the catalog is located on the server side.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064341-Imported-SQL-Files) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010029482-JSON-Connections)
