---
title: "Saving a Page Report"
id: 4405690651415
section: "Page Report Studio Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690651415-Saving-a-Page-Report
updated_at: 2022-01-27T07:59:44Z
---

# Saving a Page Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683961623-Searching-for-Text-in-Page-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683955223-Exporting-Printing-Page-Report-Result)

# Saving a Page Report

You can save the changes that you made to your page report or save a copy of your page report in Page Report Studio. This topic describes how you can save a page report.

To save your page report, select **Menu** > **File** > **Save** or the **Save** button ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4420461454871/btn_save.gif) on the toolbar.

If you have saved the report before, Server displays the [Save Report Template dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683686295-Save-Report-Template-Dialog-Box-Properties). Specify whether to save the sort and filter criteria you have made in the report, then select **Yes**. Server saves the report as a report version to the original location. If you do not want to display the dialog box, you can use the [Pop Up Save Criteria Dialog](https://devnet.logianalytics.com/hc/en-us/articles/4405683964951-Customizing-Page-Report-Studio-Profile#Criteria) option in the Page Report Studio profile to disable the dialog box from popping up when saving reports.

If you have newly created the report and has not yet saved it, Server displays the [Save As dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405690526359-Save-As-Dialog-Box-Properties).

![Save As dialog](https://devnet.logianalytics.com/hc/article_attachments/4420461558295/svas.gif)

1. In the **Save in** section, browse to the folder in the server resource tree where you want to save the report. You can use the arrow button ![Up Level button](https://devnet.logianalytics.com/hc/article_attachments/4420453485079/btn_dshbrd_up.gif) to go to the parent folder.

   The resource table lists the resources in the selected folder. You can select the column names to change the order of the resources in the table.
2. In the **File Name** box, type the name of the report or use the default name.
3. From the **Type** list, select the [file type](https://devnet.logianalytics.com/hc/en-us/articles/4405690526359-Save-As-Dialog-Box-Properties#Type) of the saved report. Normally you want to use the default page report format (.cls).
4. Select **Advanced** to set the advanced settings for the report if you want.
   1. When you did not clear [Select Catalog Linking Model](https://devnet.logianalytics.com/hc/en-us/articles/4405683964951-Customizing-Page-Report-Studio-Profile#CatalogMode) in the Page Report Studio profile, you can specify the relationship between the saved report and the catalog used to run it. By default, the saved
      report links to its catalog in which way it can always run with
      the latest version of the catalog. Select **Set Catalog Copy to Target Folder** if you want to copy the catalog to
      the folder where you save the report.

      There should be only one catalog per folder. If there is already a catalog in the folder where you are going to copy the catalog to, it may cause other reports in the folder not to be able to run as they may use the wrong catalog. Also, if there is an existing version of the same catalog in the folder, Server replaces it with the copied catalog, and existing reports that use it are not able to run with the new catalog version. Therefore, it is always better to link the catalog rather than copy it.
   2. If you want to save the report together with the sort and filter criteria, select **Save Sort Criteria** and **Save Filter Criteria** correspondingly. The criteria will automatically apply to the report the next time it opens.
   3. Optionally, type comments in the **Description** box as a description for the report.
5. Select **OK** to save the report.

To save a copy of a report, select **Menu** > **File** > **Save As**, or the **Save As** button ![Save As button](https://devnet.logianalytics.com/hc/article_attachments/4420447052311/btn_saveas.gif) on the toolbar to display the Save As dialog box, and then do as above. If you are saving to an existing file, Server will display a Confirm dialog box asking whether you want to replace the file or [save a new version into the file](https://devnet.logianalytics.com/hc/en-us/articles/4405683940759-Creating-Versions#Save).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)

* You must have the Write permission on a folder to save the report there.
* If one of the report tabs in a report contains subreports, when you save the report, Server does not save the changes that you have made on the subreports.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683961623-Searching-for-Text-in-Page-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683955223-Exporting-Printing-Page-Report-Result)
