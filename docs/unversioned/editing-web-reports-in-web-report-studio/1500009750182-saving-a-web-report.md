---
title: "Saving a Web Report"
id: 1500009750182
section: "Editing Web Reports in Web Report Studio"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009750182-Saving-a-Web-Report
updated_at: 2021-07-24T00:47:29Z
---

# Saving a Web Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750202-Applying-CSS-Styles-in-Web-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750102-Exporting-Printing-the-Web-Report-Result)

# Saving a Web Report

This topic describes how you can save changes that you made to a web report and save a copy of it.

To save the changes you made to the current report, select the **Save** button ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404885307671/btn_save.gif) on the toolbar or **Menu** > **File** > **Save**.

* If you created the report just now and has not saved it yet, Server displays the [Save As](https://devnet.logianalytics.com/hc/en-us/articles/1500009776361-Save-As-Dialog-Box-Properties) dialog box.

  ![Save As dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885318167/svas_rpt.gif)

  1. In the **Save In** section, browse to the folder in the server resource tree where you want to save the web report. You can use the up button ![Up Level button](https://devnet.logianalytics.com/hc/article_attachments/4404880146199/btn_wbrpt_up.gif) to return to the parent folder.

     The resource table shows the resources in the current directory. You can select the column names to change the order of the resources in the table list.

     **Tip:** You cannot save the report to some locations if you do not have the required permissions. You need to have the Write access to a directory to save the report there.
  2. In the **File Name** box, type the name of the report or use the default name. The default file type is **Web Report**.
  3. You can select the **Advanced** button to set advanced settings for the report.
     1. From the **Status** drop-down list, select a status for the report. By default, it is **Active** which means you can run, advanced run, and schedule to run the report. If you want to disable the report for running, choose **Inactive**. If you have not finished editing the report, choose **Incomplete**.
     2. Choose the relationship between the saved report and the catalog used to run it. By default, the
        report links to its catalog in which way it can always run with
        the latest version of the catalog. You can also choose to copy the catalog to
        the directory where you save the report by selecting **Set Catalog Copy to Target Folder**.

        There should be only one catalog per folder so if there is already a catalog in the folder where you are going to copy the catalog to, it may cause other reports in the folder not to be able to run as they may use the wrong catalog. Also, if there is a newer version of the same catalog in the target folder, Server overwrites it and existing reports that use it are not able to run with the newer catalog version. Therefore, it is always better to link the catalog rather than copy it.
     3. By default, Server save the report together with the sort and filter criteria. Then Web Report Studio automatically applies the criteria to the report next time you open it.
     4. Optionally, type comments in the Description box as a description for the report.
  4. Select **Save** to save the report.
  5. Select **OK** in the Confirm dialog box.
* If the report is an [editable shared report](https://devnet.logianalytics.com/hc/en-us/articles/1500009777281-Sharing-Web-Reports), Server displays the Confirm dialog box, prompting you to choose whether to save a finished or unfinished version for the report.

  ![Confirm Dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885318551/wbrpt_edt_save.gif)

  By default, Server saves the report as a finished version. If you are not the report owner of the shared report, you should select **Set as Unfinished Version** to save the report as an unfinished version so that you can access your modified version next time you run the shared report. If you save the shared report as a finished version, the next time you run the report you are not able to access the this version unless it is the latest finished version of the report.

To save a copy of a report, select **Menu** > **File** > **Save As** or the **Save As** button ![Save As button](https://devnet.logianalytics.com/hc/article_attachments/4404880136727/btn_saveas.gif) on the toolbar. Server displays the Save As dialog box. Then do as above. If you are saving to an existing web report, Server displays the Confirm dialog box asking whether you want to replace it or [save a new version into it](https://devnet.logianalytics.com/hc/en-us/articles/1500009748782-Creating-Versions#Save).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750202-Applying-CSS-Styles-in-Web-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750102-Exporting-Printing-the-Web-Report-Result)
