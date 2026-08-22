---
title: "Saving the Report"
id: 1500009751541
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009751541-Saving-the-Report
updated_at: 2021-07-25T07:18:33Z
---

# Saving the Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724882-Applying-CSS-Styles)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724762-Exporting-Printing-the-Report-Result)

# Saving the Report

To save the changes you made to the current report, select the **Save** button ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404942445847/btn_save.gif) on the toolbar or **Menu** > **File** > **Save**.

* If the report is newly created and has not yet been saved, Report Server displays the [Save As](https://devnet.logianalytics.com/hc/en-us/articles/1500009749441-Save-As) dialog box.

  ![Save As dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936723351/svas_rpt.gif)

  1. In the Save In section, browse to the folder in the server resource tree where you want to save the web report. You can use the ![Up Level button](https://devnet.logianalytics.com/hc/article_attachments/4404936723607/btn_wbrpt_up.gif) button to return to the parent folder.

     The resource table shows the resources in the current directory. You can select the column names to change the order of the resources in the table list.

     **Tip:** You will not be able to save the report to some locations if you do not have the required permissions. You need to have the Write access to a directory in order to save report there.
  2. In the File Name box, type the name of the report or use the default name. The default file type is Web Report.
  3. You can select the **Advanced** button to set advanced settings for the report.
     1. From the Status drop-down list, specify a status for the report. By default it is Active which means the report can be run, advanced run and scheduled to run. If you want to disable the report for running, choose **Inactive**; if you haven't finished editing the report, choose **Incomplete**.
     2. Specify the relationship between the saved report and the catalog used to run it. By default the
        report is linked to its catalog in which way it can always run with
        the latest version of the catalog. You can also choose to copy the catalog to
        the directory where the report is saved
        by selecting the **Set Catalog Copy to Target Folder** option.

        There should be only one catalog per folder so if there is already a catalog in the folder where you are going to copy the catalog to, it may cause other reports in the folder not to be able to run as they may use the wrong catalog. Also, if there is a newer version of the same catalog in the target folder, it will be overwritten and existing reports that use it will not be able to run with the newer catalog version. Therefore, it is always better to link the catalog rather than copy it.
     3. If you want to save the report together with the sort and filter criteria, select **Save Sort Criteria** and **Save Filter Criteria** correspondingly. Then Web Report Studio will automatically apply the criteria to the report the next time it is opened.
     4. Optionally, type comments in the Description box as a description for the report.
  4. Select **Save** to save the report. Then select **OK** in the Confirm dialog box.
* If the report is an [editable shared report](https://devnet.logianalytics.com/hc/en-us/articles/1500009723142-Sharing-Reports), Report Server displays the Confirm dialog box, prompting you to choose whether to save a finished or unfinished version for the report.

  ![Confirm Dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942451991/wbrpt_edt_save.gif)

  By default the report will be saved as a finished version. If you are not the report owner of the shared report, it is recommended that you select the **Set as Unfinished Version** option to save the report as an unfinished version so that you can access your modified version next time you run the shared report. If you save the shared report as a finished version, the next time you run the report you will not be able to access the version you save unless it is the latest finished version of the report.

To save a copy of a report, select **Menu** > **File** > **Save As** or the **Save As** button ![Save As button](https://devnet.logianalytics.com/hc/article_attachments/4404936715031/btn_saveas.gif) on the toolbar to show the Save As dialog box, and then do as above. If you are saving to an existing web report, Report Server will display the Confirm dialog box asking whether you want to replace it or [save a new version into it](https://devnet.logianalytics.com/hc/en-us/articles/1500009750221-Creating-Versions#Save).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724882-Applying-CSS-Styles)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724762-Exporting-Printing-the-Report-Result)
