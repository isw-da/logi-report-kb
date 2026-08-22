---
title: "Example 1: Importing the XML File Indirectly"
id: 1500009584921
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584921-Example-1-Importing-the-XML-File-Indirectly
updated_at: 2021-07-24T05:55:48Z
---

# Example 1: Importing the XML File Indirectly

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584901-Using-XML-File-as-a-Data-Source-via-OOJDBC)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564062-Example-2-Importing-the-XML-File-Directly)

# Example 1: Importing the XML File Indirectly

This topic introduces how to import an XML file indirectly.

In this example, employee.xml in `<``install_root>\help\samples\OOJDBC` will be used. Store it to `<install_root>\Demo\Reports\TutorialReports` first, then, follow the steps below to import the file to a catalog.

Below is a list of the sections covered in this topic:

> * [Importing the XML File Using the Model Wizard](#Wizard)
> * [Importing the ODF File into a Catalog](#Catalog)

## Importing the XML File Using the Model Wizard

To import the XML file employee.xml using the Model Wizard, take the following steps:

1. Run ModelWizard.bat in `<install_root>\bin` to open the Object Source Wizard.
2. Select **File** > **Add Table**.
3. In the Add Table dialog, specify the class and table name as required. Here, we fill in the Table Name as **employee** and ClassName as **com.jinfonet.jdbc.RecordResult** (a class of Jinfonet). Then select the **Parse** button.

   ![Add Table dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893969175/cnctn_jdbc_oojdbc_xml_exmpl1_1.gif)

   Where,

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
   | Add Indirect Path |  |
   | Cancel | Cancels the operation and closes the Add Table dialog. |
4. Select the **Remove** button to get rid of all the existing columns in the Add Table dialog, and then select the **Add** button to add a new column.
5. In the Access Indirect Columns dialog, specify the data type of the column.

   In this example, we will add a column of String type, so select **java.lang.String** in the ReturnType column of the Methods box, then select the **Add** button. Select **OK** to return to the Add Table dialog.

   ![Access Indirect Columns dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893969431/cnctn_jdbc_oojdbc_xml_exmpl1_2.gif)

   **Note:** If you want to use dynamic parameter, you can choose the option Is Dynamic in the Access Indirect Columns dialog. For details, see [Example 3: XML file with dynamic parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009564082-Example-3-XML-File-with-Dynamic-Parameters).
6. In the Add Table dialog, select **Direct Access Path** to define the accessing path of the table in the Access Method dialog.
   1. Fill in **com.jinfonet.jdbc.xml.XMLReader** in the Root Class Name text field, select the **Parse** button and check **Show Static Methods Only**.
   2. Select the shown method. In the Parameters box, fill in the default values for param0 and param1 as required. For example, for param0, fill in **`file:///C:/Logi JReport/Designer/Demo/Reports/TutorialReports/employee.xml`**, then for param1, fill in **record employee root employee column first\_name 12 path document.employee.first\_name**.

      ![Access Method dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893969687/cnctn_jdbc_oojdbc_xml_exmpl1_3.gif)

      The following are explanations about the parameters.

      * param0 is the valid XML file name with its path.
      * param1 is the query sentence for selecting the column to be used for reporting from the XML file. record is the keyword, followed with the XML file name (without the extension .xml). Following this is another keyword column with the actual tag name from the XML file.

        Below is the part quoted from employee.xml:

        |  |
        | --- |
        | ``` <employee> <id>0799</id> <first_name>Jack</first_name>  <second_name>Smith</second_name> <birthday>12/28/75</birthday> <title>manager</title> <salary>$7000.00</salary>  </employee> ``` |

        Since first\_name is required, you should then give the actual tag name here. The number afterwards is the SQL type of the column. "12" is for String type. For detailed information about Java SQL types, refer to JDK package java.sql.types.java.

        **Notes:**

        + In param1, the order of the columns is dependent on the default values given when adding the column.
        + The SQL type BINARY, VARBINARY and LONGVARBINARY are not supported.
   3. Select **OK** to return to the Add Table dialog.
7. Now you can see that the column has been added in the Add Table dialog. You can rename the default column name by editing in the Column Name column. You are recommended to give the name as the actual tag definition in the .xml file, for example first\_name.

   ![Add Table dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889397911/cnctn_jdbc_oojdbc_xml_exmpl1_4.gif)
8. Select the **OK** button, and the table employee will now have been added to the Object Source Wizard.
9. In the Object Source Wizard, select **File** > **Save**. You will then be prompted to save the ODF file. You should save it to `<install_root>\lib` or the directory where the catalog will be. Here we save it as employee.odf.

**Notes:**

* If you use dynamic parameters, that is you check the Is Dynamic option, the syntax of the method is an array of Boolean values which indicates which parameter is dynamic at runtime. If the parameter is dynamic the value should be prompted and initialized before executing an SQL. In addition, when you choose the option Is Dynamic, this parameter will be passed to Logi JReport Designer. After you create a connection in the Catalog Manager, you will find it in the Parameters node.
* The same ODF file cannot exist in both  `<install_root>\lib` and the directory where the catalog is located.
* If you have purchased the readable key, you can also save the ODF file (oojdbc data definition file) to XML format (with extension .odf.xml). For files which have already been saved with an .xml extension, in order to make them available, you can manually change the extension from .xml to .odf.xml.

## Importing the ODF File into a Catalog

To import the generated employee.odf into a Logi JReport catalog, take the following steps:

1. Start Logi JReport Designer.
2. Select  **File** > **New Catalog**.
3. In the New Catalog dialog, specify the catalog name, the data source name and the path. The catalog should be located in the directory where you saved the ODF file. For example, if you saved the ODF file in `C:\odf`, the new catalog should be created also in `C:\odf`.
4. In the Catalog Manager, right-click the node of a data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.
5. In the Get JDBC Connection Information dialog, enter **com.jinfonet.jdbc.obj.ObjectDriver** in the Driver text field, type **jdbc:jinfonet:object:@Filename** in the URL text field. @Filename should be the ODF file name. In the example, it is jdbc:jinfonet:object:@employee.

   ![Get JDBC Connection Information dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889398167/cnctn_jdbc_oojdbc_xml_exmpl1_impt.gif)
6. Select **OK** to set up the connection.
7. In the prompted guidance dialog, select **Add Tables**.
8. In the Add Tables dialog, select the table **employee** and select **Add**.

   ![Add Tables dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893970071/cnctn_jdbc_oojdbc_xml_exmpl1_addtbl.gif)
9. Select **Done** to close the Add Tables dialog.

Now, the table employee will have been added into the catalog. You can use it to develop reports as required.

**Note:** When you publish the catalog and its reports to Logi JReport Server, whether the ODF file is located in `<install_root>\lib` or in the directory where the catalog is located, it will be deployed to the path where the catalog is located in the server side.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584901-Using-XML-File-as-a-Data-Source-via-OOJDBC)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564062-Example-2-Importing-the-XML-File-Directly)
