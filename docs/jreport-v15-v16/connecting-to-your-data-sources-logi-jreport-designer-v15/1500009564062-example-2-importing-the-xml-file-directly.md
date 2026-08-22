---
title: "Example 2: Importing the XML File Directly"
id: 1500009564062
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564062-Example-2-Importing-the-XML-File-Directly
updated_at: 2021-07-24T05:55:48Z
---

# Example 2: Importing the XML File Directly

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584921-Example-1-Importing-the-XML-File-Indirectly)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564082-Example-3-XML-File-with-Dynamic-Parameters)

# Example 2: Importing the XML File Directly

The process of importing an XML file with Model Wizard (as explained in [Example 1](https://devnet.logianalytics.com/hc/en-us/articles/1500009584921-Example-1-Importing-the-XML-File-Indirectly)) can be simplified with Logi JReport's built-in XML file import functionality, and is very easy to use.

In this example, orgchart\_data.xml in `<install_root>\help\samples\OOJDBC` will be used. Store it to `<install_root>\Demo\Reports\TutorialReports` first. Then follow the steps below to import the file to a catalog.

Below is a list of the sections covered in this topic:

> * [Importing the XML File Directly using the Model Wizard](#Wizard)
> * [Importing the ODF file into a Catalog](#Catalog)

## Importing the XML File Directly using the Model Wizard

To import the XML file directly using the Model Wizard, take the following steps:

1. Run ModelWizard.bat in `<install_root>\bin` to open the Object Source Wizard.
2. Select **File** > **Import XML Files** to bring up the Import XML dialog.
3. Select **Open** to browse to the file orgchart\_data.xml.
4. Check **Column** for all elements and change their format and type if necessary (for the details about how to set the format, see [Examples of format](#Examples)).

   ![Import XML dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889397399/cnctn_jdbc_oojdbc_xml_exmpl2.gif)
5. Select **OK** and the table OrgChart will now have been added to the Object Source Wizard.
6. In the Object Source Wizard, select **File** > **Save**. You will then be prompted to save the ODF file. You should save it to `<install_root>\lib` or to the directory where the catalog will be located. Here, we save it as orgchart.odf.

   **Note:** The same ODF file cannot exist in `both <install_root>\lib` and the directory where the catalog will be located.

**Examples of format**

When using certain SQL types, you should input a standard format in the Format cell in the Import XML dialog. There are some examples:

* If the time format is like Tue Aug 27 16:04:00 BST 2002, you should select:   
  **Type**: TimeStamp  
  **Format**: EEE MMM dd hh:mxm:ss zzz yyyy
* If the time format is like 2002-11-22 11:09:08, you should select:  
  **Type**: TimeStamp  
  **Format**: yyyy-MM-dd hh:mm:ss
* If the time format is like 11/18/2002 08:20:00, you should select  
  **Type**: TimeStamp  
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

## Importing the ODF file into a Catalog

To import the generated orgchart.odf file into a Logi JReport catalog, take the following steps:

1. Start Logi JReport Designer.
2. Select **File** > **New Catalog**.
3. In the New Catalog dialog, specify the catalog name, the data source name and the path. The catalog should be located in the directory where you saved the ODF file. For example, if you saved the ODF file in `C:\odf`, the new catalog should be created also in `C:\odf`.
4. In the Catalog Manager, right-click the data source node and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.
5. In the Get JDBC Connection Information dialog, enter **com.jinfonet.jdbc.obj.ObjectDriver** in the Driver text field, type **jdbc:jinfonet:object:@Filename** in the URL text field. @Filename should be the ODF file name. In the example, it is jdbc:jinfonet:object:@orgchart.

   ![Get JDBC Connection Information dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889397655/cnctn_jdbc_oojdbc_xml_exmpl2_impt.gif)
6. Select **OK** to set up the connection.
7. In the prompted guidance dialog, select **Add Tables**.
8. In the Add Tables/Views/Synonyms dialog, select the table **OrgChart** and select **Add**.

   ![Add Table dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893968919/cnctn_jdbc_oojdbc_xml_exmpl2_addtbl.gif)
9. Select **Done** to close the Add Tables dialog.

Now, the table OrgChart will be added into the catalog. You can use it to develop reports as required.

**Note:** When you publish the catalog and its reports to Logi JReport Server, whether the ODF file is located in `<install_root>\lib` or in the directory where the catalog is located, it will be deployed to the path where the catalog is located on the server side.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584921-Example-1-Importing-the-XML-File-Indirectly)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564082-Example-3-XML-File-with-Dynamic-Parameters)
