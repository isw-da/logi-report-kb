---
title: "Saving the Report"
id: 1500009673981
section: "Page Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673981-Saving-the-Report
updated_at: 2021-07-24T20:53:54Z
---

# Saving the Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674021-Searching-for-Text-in-a-Report)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649462-Printing-the-Report-Result)

# Saving the Report

You can save your report in Page Report Studio. To do this, select **Menu** > **File** > **Save**, or the **Save** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926628119/btn_save.gif) on the toolbar.

If the report has been saved before, the [Save Report Template](https://devnet.logianalytics.com/hc/en-us/articles/1500009670041-Save-Report-Template) dialog appears. Specify whether or not to save the sort and filter criteria you have made on the report, then select **OK**. The report will be saved as a report version to the original location. If you do not want to display the dialog, you can use the option [Pop Up Save Criteria Dialog](https://devnet.logianalytics.com/hc/en-us/articles/1500009674101-Customizing-Page-Report-Studio-Profile#Criteria) in the Page Report Studio profile to disable it from popping up when saving reports.

If the report is newly created and has not yet been saved, the [Save As](https://devnet.logianalytics.com/hc/en-us/articles/1500009670021-Save-As) dialog appears.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920451735/svas.gif)

1. In the Save in section, browse to the folder in the server resource tree where you want to save the report. The folder may be Public Reports or My Reports. You can use the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926673687/btn_dshbrd_up.gif) to go to the parent folder.

   The resource table shows the resources in the current directory. Select the column names to change the order of the report in the table list if required.
2. In the File Name box, enter the name of the report or use the default name.
3. From the File Type drop-down list, specify the type of the saved report. Normally you want to use the default (.cls).
   * **Page Report (\*.cls)**  
      Saves the report as a binary formatting file.
   * **Report Template (.rpt)**  
      It is a file saved in text format, which can be edited in any text editor.
   * **Self Contained Page Report (.clx)**  
      It is a binary report file, which contains not only the report's layout but also the catalog with its own resources.
   * **Page Report XML Format (.cls.xml)**  
      It follows the XML standard, which can be edited with both Logi JReport Designer and external XML editors. Page reports that contain customized user-defined objects (UDO) cannot be saved to XML format. Using the XML format is better for checking into source code control systems than using the binary formats. The XML feature for page reports is under license control. To obtain the special key, contact Jinfonet Support ([support@jinfonet.com](mailto:support@jinfonet.com)).
4. Select the **Advanced** button to set the advanced settings for the report if required.
   1. When [Select Catalog Linked Model](https://devnet.logianalytics.com/hc/en-us/articles/1500009674101-Customizing-Page-Report-Studio-Profile#CatalogMode) is enabled in the Page Report Studio profile, specify the relationship between the saved report and the catalog used to run it:
      * **Set Original Catalog as Linked Catalog into Saved Report**  
         If checked, the saved report will be linked with the catalog and the saved report will run with the catalog no matter whether the two are in the same directory. If later the catalog is updated, the saved report will run with the latest version of the catalog.
      * **Set Catalog Copy to Target Folder**   
         If checked, the catalog will be copied to the directory where the report is saved and the saved report will run with the copied catalog. There should be only one catalog per folder so if there is already a catalog in the folder where you are going to save the report, it may cause other reports in the folder not to be able to run as they may try to use the wrong catalog. Also, if there is an existing version of the same catalog in the target folder, it will be overwritten and existing reports that use it may not run with the new catalog version. Therefore, it is always better to link the catalog rather than copy it.
   2. If you want to save the report together with the sort and filter criteria, check **Save Sort Criteria** and **Save Filter Criteria** correspondingly. With the criteria saved, Page Report Studio will automatically apply them to the report the next time it is opened.
   3. Optionally, input comments in the Description box as a description for the report.
5. Select **OK** to save the report.

To save a copy of a report, select **Menu** > **File** > **Save As**, or the **Save As** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920358039/btn_saveas.gif) on the toolbar to show the Save As dialog, and then do as above. If you are saving to an existing file, a Confirm dialog will be displayed asking whether you want to replace the file or [save a new version into the file](https://devnet.logianalytics.com/hc/en-us/articles/1500009649002-Creating-Versions#Save).

**Notes:**

* You will not be able to save the report to some locations if you do not have the required permissions. You need to have Write access to the directory.
* If one of the report tabs in a report contains subreports, when you save the report, changes you have made on the subreports will not be saved along with the primary report.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674021-Searching-for-Text-in-a-Report)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649462-Printing-the-Report-Result)
