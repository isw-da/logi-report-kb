---
title: "Editing the Operation Used to Create Tables"
id: 1500009564362
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564362-Editing-the-Operation-Used-to-Create-Tables
updated_at: 2021-07-24T05:55:41Z
---

# Editing the Operation Used to Create Tables

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585361-Adding-Tables-to-a-Web-Service-Connection)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585381-Example-Developing-Reports-from-a-Web-Service-Data-Source)

# Editing the Operation Used to Create Tables

After creating the table, the service and operation you have selected to create the table will be displayed under the Tables node of the web service connection in the Catalog Manager. If you use WSDL 1.1 to define the web service, the defined port type will also be included. You can edit the information of the operation if necessary. To do this, follow the steps below:

1. Select the operation node, right-click it and then select **Edit** from the shortcut menu. The [Edit Operation Calling Property](https://devnet.logianalytics.com/hc/en-us/articles/1500009586521-Edit-Operating-Calling-Property-Dialog) dialog appears.

   ![Edit Operation Calling Property dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889367191/edtoprtn.gif)
2. In the Input Message column, select the input message you want to edit, then modify its value in the text field of the Value column as required. You can either input the value, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif) in the text field to select or define a [constant level formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009589701-Formula-Levels#CLF) or [parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009590021-Parameters) in the current catalog data source to return the value of the input message.
3. Type the number of seconds in the Time Out text field to specify how long to wait for the operation to complete.
4. If you use WSDL 1.1 to define the web service, the option Use Schema from Response will be available, using which you can decide whether to ignore the XML schema described in the output message and parse the XML schema directly from the specific XML instance in the SOAP responded from web service.
5. When done, select **OK** to accept the changes and exit the dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585361-Adding-Tables-to-a-Web-Service-Connection)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585381-Example-Developing-Reports-from-a-Web-Service-Data-Source)
