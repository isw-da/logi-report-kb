---
title: "Adding Tables to a Web Service Connection"
id: 1500009585361
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585361-Adding-Tables-to-a-Web-Service-Connection
updated_at: 2021-07-24T05:55:43Z
---

# Adding Tables to a Web Service Connection

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585401-Setting-Up-a-Web-Service-Connection)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564362-Editing-the-Operation-Used-to-Create-Tables)

# Adding Tables to a Web Service Connection

After setting up the web service connection, all the information of the web service defined in the WSDL file will be stored in the catalog, including information of service, operation, and the input message and output message in each operation. You can then add tables into the Logi JReport catalog via the connection based on this information. However, you can only define tables based on operations which support SOAP binding.

**To add tables to a web service connection:**

1. Do any of the following:
   * Right-click the web service connection and select **Add Tables** from the shortcut menu.
   * Right-click the **Tables** node of the web service connection and select **Add Tables** from the shortcut menu.
   * Right-click an existing table in the web service connection if there is and select **Add Tables** from the shortcut menu.
   * Right-click any folder in the Tables node of the web service connection if you have already created some and select **Add Tables** from the shortcut menu.
   * Select the **Tables** node of the web service connection, or any existing table or folder in the connection any and select **Add Tables** on the Catalog Manager toolbar.

   The [Add Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009564482-Add-Tables-Dialog) dialog appears.

   ![Add Tables dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893958167/addtbl_wbsvc.gif)
2. Specify a service from the Service Name drop-down list.
3. If you use WSDL 1.1 to define the web service, you also need to specify the port type for the selected service from the Port Type drop-down list.
4. All the operations with SOAP binding that are included in the selected service will be listed in the Operation Name drop-down list. Select one as required, then the input message of the operation will be displayed. You can define the value for the input message if necessary by either typing in the value in the text field in the Value column, or selecting ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif) in the text field to select or define a [constant level formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009589701-Formula-Levels#CLF) or [parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009590021-Parameters) in the current catalog data source to return the value.

   If the Input Message column is empty, that is to say, the input message has its own defined values, so there is no need for you to provide it the value.
5. Type the number of seconds in the Time Out text field to specify how long to wait to get the specified service and operation information defined in the WSDL file.
6. If you use WSDL 1.1, you may sometimes find that the XML schema described by the output message does not match the concrete XML instance in the SOAP responded from the web service, as a result, Logi JReport will be unable to read data properly from that XML instance. In this case, you can check the option **Use Schema from Response**, so as to ignore the XML schema in the output message and directly parse the XML schema from the specific XML instance included in the SOAP responded from the web service.
7. When done, select the **OK** button to accept the changes and exit the dialog.

When the tables are added in the Logi JReport catalog, you can manage them the same as you do with tables from an XML data source. For example, you can add more tables via the web service connection into the catalog, remove undesired table columns, organizing the tables into folder and refreshing the tables. For details, see [Managing Tables in an XML Connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009585461-Managing-Tables-in-an-XML-Connection).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585401-Setting-Up-a-Web-Service-Connection)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564362-Editing-the-Operation-Used-to-Create-Tables)
