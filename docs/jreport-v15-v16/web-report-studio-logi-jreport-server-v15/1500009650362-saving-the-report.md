---
title: "Saving the Report"
id: 1500009650362
section: "Web Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009650362-Saving-the-Report
updated_at: 2021-07-24T20:53:34Z
---

# Saving the Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675301-Applying-CSS-Styles)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650262-Exporting-Printing-the-Report-Result)

# Saving the Report

To save the changes you made to the current report, select **Menu** > **File** > **Save** or the **Save** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926628119/btn_save.gif) on the toolbar.

If the report is newly created and has not yet been saved, the [Save As](https://devnet.logianalytics.com/hc/en-us/articles/1500009647882-Save-As) dialog appears.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920372631/svas_rpt.gif)

1. In the Save in section, browse to the folder in the server resource tree where you want to save the web report. The folder may be Public Reports or My Reports. You can use the ![](https://devnet.logianalytics.com/hc/article_attachments/4404920372887/btn_wbrpt_up.gif) button to return to the parent folder.

   The resource table shows the resources in the current directory. Select the column names to change the order of the report in the table list if required.
2. In the File Name box, enter the name of the report or use the default name. The default file type is web report.
3. Select the **Advanced** button to set the advanced settings for the report if required.
   1. From the Status drop-down list, specify a status for the report.
   2. Specify the relationship between the saved report and the catalog used to run it:
      * **Set Original Catalog as Linked Catalog into Saved Report**  
         If checked, the saved report will be linked with the catalog and will run with the catalog no matter whether the two are in the same directory. If later the catalog is updated, the saved report will run with the latest version of the catalog.
      * **Set Catalog Copy to Target Folder**   
         If checked, the catalog will be copied to the directory where the report is saved and the saved report will run with the copied catalog. There should be only one catalog per folder so if there is already a catalog in the folder where you are going to save the report, it may cause other reports in the folder not to be able to run as they may try to use the wrong catalog. Also, if there is an existing version of the same catalog in the target folder, it will be overwritten and existing reports that use it may not run with the new catalog version. Therefore, it is always better to link the catalog rather than copy it.
   3. If you want to save the report together with the sort criteria, check **Save Sort Criteria**. With the criteria saved, Web Report Studio will automatically apply them to the report the next time it is opened.
   4. Optionally, input comments in the Description box as a description for the report.
4. Select **Save** to save the report.

To save a copy of a report, select **Menu** > **File** > **Save As** or the **Save As** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920358039/btn_saveas.gif) on the toolbar to show the Save As dialog, and then do as above. If you are saving to an existing file, a Confirm dialog will be displayed asking whether you want to replace the file or [save a new version into the file](https://devnet.logianalytics.com/hc/en-us/articles/1500009649002-Creating-Versions#Save).

**Note:** You will not be able to save the report to some locations if you do not have the required permissions. You need to have Write access to the directory.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675301-Applying-CSS-Styles)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650262-Exporting-Printing-the-Report-Result)
