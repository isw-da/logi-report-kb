---
title: "Save As Dialog Box Properties"
id: 1500009773121
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009773121-Save-As-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:03Z
---

# Save As Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009772961-Report-Tab-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745122-Save-Report-Template-Dialog-Box-Properties)

# Save As Dialog Box Properties

You can use the Save As dialog box to [save a report](https://devnet.logianalytics.com/hc/en-us/articles/1500009777601-Saving-a-Page-Report) as a new file or as a new version. This topic describes the options in the dialog box.

![Save As dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880251543/svas.gif)

**Save In**

Specifies the directory in the server resource tree where you want to save the report. Use the button ![Up Level button](https://devnet.logianalytics.com/hc/article_attachments/4404885385367/btn_dshbrd_up.gif) to go to the parent folder. The root folder cannot save resources.

The resource table shows the resources in the current directory. You can select the column names to change the order of the report in the table list.

* **Name**  
   Displays the file names.
* **Size**  
   Displays the file size.
* **Type**  
   Displays the file type.
* **Last Modified**  
   Displays the last modified time of the file.

**File Name**

Specifies the name for the saved report, without suffix.

**Type**

Specifies the type of the saved report.

By default, page report files contain a .cls suffix. This is the format that provides optimal performance in the Logi Report toolset. You can also store page report files in the following formats:

* **Page Report (\*.cls)**  
  Saves the report as a binary formatting file.
* **Report Template (.rpt)**  
   It is a file in text format, which you can edit in any text editor.
* **Self Contained Page Report (.clx)**  
   It is a binary report file, which contains not only the report's layout but also the catalog with its own resources.
* **Page Report XML Format (.cls.xml)**  
   It follows the XML standard, which you can edit with both Logi Report Designer and external XML editors. You cannot save page reports that contain customized user defined objects (UDO) to XML format. Using the XML format is better for checking into source code control systems than using the binary formats.

**Advanced**/**Simple**

Displays the following settings or hides them.

* **Catalog**  
   Shows the catalog that the report uses.

  Server displays the following two options when you have not selected [Select Catalog Linking Model](https://devnet.logianalytics.com/hc/en-us/articles/1500009777681-Customizing-Page-Report-Studio-Profile#CatalogMode) in the Page Report Studio profile.

  + **Set Original Catalog as Linked Catalog into Saved Report**  
     If you select the option, Server will link the saved report with the catalog and the saved report will run with the catalog no matter whether the two are in the same directory. If later you update the catalog, the saved report will run with the latest version of the catalog.
  + **Set Catalog Copy to Target Folder**   
     If you select the option, Server will copy the catalog to the directory where you save the report and the saved report will run with the copied catalog.
* **Save Sort Criteria**  
   Specifies whether to save the changes made by sorting.
* **Save Filter Criteria**  
   Specifies whether to save the changes made by filtering.
* **Description**Provides a description for the saved report.

**OK**

Saves the report with the specified settings and closes this dialog box.

**Cancel**

Does not save the report as a new file and closes the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009772961-Report-Tab-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745122-Save-Report-Template-Dialog-Box-Properties)
