---
title: "Saving a Web Report"
id: 4405684044439
section: "Web Report Studio Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405684044439-Saving-a-Web-Report
updated_at: 2022-01-27T07:59:53Z
---

# Saving a Web Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684045591-Applying-CSS-Styles-in-Web-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690685335-Exporting-Printing-the-Web-Report-Result)

# Saving a Web Report

This topic describes how you can save changes that you made to a web report and save a copy of it.

To save the changes you made to the current report, select the **Save** button ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4420461454871/btn_save.gif) on the toolbar or **Menu** > **File** > **Save**.

* If you created the report just now and has not saved it yet, Server displays the [Save As dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405690607895-Save-As-Dialog-Box-Properties).

  ![Save As dialog](https://devnet.logianalytics.com/hc/article_attachments/4420453403671/svas_rpt.gif)

  1. In the **Save In** section, browse to the folder in the server resource tree where you want to save the web report. You can use the arrow button ![Up Level button](https://devnet.logianalytics.com/hc/article_attachments/4420453403927/btn_wbrpt_up.gif) to return to the parent folder.

     The resource table shows the resources in the current folder. You can select the column names to change the order of the resources in the table.

     **Tip:** You must have the Write permission on a folder to save the report there.
  2. In the **File Name** box, type the name of the report or use the default name.
  3. The default file type is **Web Report** (.wls). You can also save the report in the XML format (.wls.xml).
  4. Optionally, select **Advanced** to set advanced settings for the report.
     1. From the **Status** list, select a status for the report. By default, it is **Active** which means you can run, advanced run, and schedule to run the report. If you want to disable the report for running, choose **Inactive**. If you have not finished editing the report, choose **Incomplete**.
     2. Choose the relationship between the saved report and the catalog used to run it. By default, the saved
        report links to its catalog in which way it can always run with
        the latest version of the catalog. Select **Set Catalog Copy to Target Folder** if you want to copy the catalog to
        the folder where you save the report.

        There should be only one catalog per folder. If there is already a catalog in the folder where you are going to copy the catalog to, it may cause other reports in the folder not to be able to run as they may use the wrong catalog. Also, if there is an existing version of the same catalog in the folder, Server replaces it with the copied catalog, and existing reports that use it are not able to run with the new catalog version. Therefore, it is always better to link the catalog rather than copy it.
     3. By default, Server saves the report together with the sort and filter criteria. The criteria will automatically apply to the report the next time it opens.
     4. Optionally, type comments in the **Description** box as a description for the report.
  5. Select **OK** to save the report.
  6. Select **OK** in the Confirm dialog box.
* If the report is an [editable shared report](https://devnet.logianalytics.com/hc/en-us/articles/4405683936279-Sharing-Web-Reports), Server displays the Confirm dialog box, prompting you to choose whether to save a finished or unfinished version for the report.

  ![Confirm Dialog](https://devnet.logianalytics.com/hc/article_attachments/4420453404183/wbrpt_edt_save.gif)

  By default, Server saves the report as a finished version. If you are not the report owner of the shared report, you should select **Set as Unfinished Version** to save the report as an unfinished version so that you can access your modified version next time you run the shared report. If you save the shared report as a finished version, the next time you run the report you are not able to access this version unless it is the latest finished version of the report.

To save a copy of a report, select **Menu** > **File** > **Save As** or the **Save As** button ![Save As button](https://devnet.logianalytics.com/hc/article_attachments/4420447052311/btn_saveas.gif) on the toolbar. Server displays the Save As dialog box. Then do as above. If you are saving to an existing web report, Server displays the Confirm dialog box asking whether you want to replace it or [save a new version into it](https://devnet.logianalytics.com/hc/en-us/articles/4405683940759-Creating-Versions#Save).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684045591-Applying-CSS-Styles-in-Web-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690685335-Exporting-Printing-the-Web-Report-Result)
