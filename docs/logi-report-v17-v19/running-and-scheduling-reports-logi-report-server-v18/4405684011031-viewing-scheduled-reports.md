---
title: "Viewing Scheduled Reports"
id: 4405684011031
section: "Running and Scheduling Reports Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405684011031-Viewing-Scheduled-Reports
updated_at: 2022-01-27T07:59:47Z
---

# Viewing Scheduled Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684009879-Applying-Dynamic-Names-for-Published-Result-Files)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684008855-Importing-and-Exporting-Scheduled-Tasks)

# Viewing Scheduled Reports

When finishing a report schedule task, you can view the reports included in the task at any time. This topic describes how you can view scheduled reports that you published to different destinations.

This topic contains the following sections:

* [Viewing Reports Scheduled to Version](#Version)
  + [Via the Schedule Task Details](#TaskDetail)
  + [Via the Version Table](#VersionTable)
* [Viewing Reports Scheduled to Disk](#Disk)
* [Viewing Reports Scheduled to Email/Printer/Fax/FTP](#Other)

## Viewing Reports Scheduled to Version

There are two ways you can take to view the reports you published to the versioning system: via the schedule task details and via the version table.

### Via the Schedule Task Details

1. On the Server Console, select **My Tasks** on the system toolbar.
2. Select the **Completed** tab, where Server displays all the successfully scheduled tasks.

   ![Completed Task List](https://devnet.logianalytics.com/hc/article_attachments/4420461537687/wkrpt_sch_vwrst1.gif)
3. Locate the required task and do any of the following:
   * Select the name of the task in the **Schedule Name** column.
   * Select the **Details** button ![Detail button](https://devnet.logianalytics.com/hc/article_attachments/4420461538071/btn_srv_details.gif) on the floating toolbar of the task row.
   * Select the task row and select **Edit** > **Details** on the task bar of the My Tasks page.
4. In the Result Details list, the links to different report formats are available in the To Version section. Select the format links to view the reports.

   ![Result Details](https://devnet.logianalytics.com/hc/article_attachments/4420453470359/wkrpt_sch_vwrst2.gif)

   You can further export Logi Report Result and Web Report Result to the HTML, PDF, Text, Excel, XML, RTF, and Postscript formats via Server. When you view a Logi Report Result or Web Report Result, Server displays the following dialog box for you to specify the export format and configure the [format settings](https://devnet.logianalytics.com/hc/en-us/articles/4405683737751-Advanced-Run-Dialog-Box-Properties#HTML). For a Logi Report Result, you also need to select the report tabs in the page report you want to export.

   ![Result Export Settings](https://devnet.logianalytics.com/hc/article_attachments/4420447129751/wkrpt_sch_vwrst3.gif)

   Server opens page report results in Page Report Studio which has permission control, so to view page report results successfully you need to have the [Execute and/or Edit permissions](https://devnet.logianalytics.com/hc/en-us/articles/4405684023831-Managing-Permissions) on the results. To view a page report result, you can choose one of the following ways:

   * Select **Page Report Result** which is available when you have the Execute permission on the page report result. Server then opens the result in Page Report Studio in the mode specified by the [Default View for Page Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/4405683590167-Configuring-Server-Profile#PageMode) option in the server profile. If Default View is Interactive View but you do not have the Edit permission, you will get an error message.
   * Select the **Run** button ![Run button](https://devnet.logianalytics.com/hc/article_attachments/4420461539479/btn_srv_run.gif) on the result row to access Basic View of Page Report Studio. You need the execute permission.
   * Select the **Edit** button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420453471767/btn_srv_edit.gif) on the result row to access Interactive View of Page Report Studio. You need the edit permission.
   * Select the **Advanced Run** button ![Advanced Run button](https://devnet.logianalytics.com/hc/article_attachments/4420461540503/btn_srv_advrun.gif) on the result row. In this way, you can customize the result resolution and the view mode of Page Report Studio: Basic View, Basic View Only, or Interactive View. You need the execute permission.

### Via the Version Table

Based on the different archive location that you have specified when creating the report schedule task, you will need to access the [version table](https://devnet.logianalytics.com/hc/en-us/articles/4405683939607-Browsing-Versions) of a report in different ways.

* If the archive location is Built-in Version Folder:
  1. In the server resource tree, browse to the row that the original report is in.
  2. Do any of the following to open the Report Result Versions table:
     + Select the report row and select **Tools** > **Version** on the task bar of the Resources page.
     + Select the report row, right-click in the row and select **Version** from the shortcut menu.
     + Put the mouse pointer over the report row and select the **Version** button ![Version button](https://devnet.logianalytics.com/hc/article_attachments/4420447130135/btn_srv_vrsn.gif) on the floating toolbar.
  3. In the Results column of the version table, Server lists the reports of different formats. Select the format links to view the reports.

     ![Report Result Versions](https://devnet.logianalytics.com/hc/article_attachments/4420447130391/wkrpt_sch_vwrst4.gif)
* If the archive location is the My Reports Folder or Public Reports Folder, which requires providing the path and name for the scheduled report in the server resource tree:
  1. In the server resource tree, browse to the row that the report is in based on the specified path and name information.
  2. Do any of the following to open the Result Versions table:
     + Select the name of the report directly.
     + Hover over the report row and select the **Version** button ![Version button](https://devnet.logianalytics.com/hc/article_attachments/4420447130135/btn_srv_vrsn.gif) on the floating toolbar.
     + Select the report row, right-click in the row and select **Version** from the shortcut menu.
     + Select the report row and select **Tools** > **Version** on the task bar of the Resources page.
  3. In the Results column of the version table, Server lists the reports of different formats. If the schedule task is based on multiple reports, Server lists the reports of different formats for each report tab in a page report and each web report. Select the format links to view the reports.

     ![Multiple Result Versions](https://devnet.logianalytics.com/hc/article_attachments/4420447130647/wkrpt_sch_vwrst5.gif)

You can also use [URL commands](https://devnet.logianalytics.com/hc/en-us/articles/4405684055959-Working-with-Server-via-URL#ViewResult) to view the reports that are published to version.

## Viewing Reports Scheduled to Disk

When you schedule to publish a report to disk, you can choose to publish the report to either the server resource tree or a server disk path, then after Server completes the schedule task:

* If you are to publish the report to the server resource tree, you can view the report files from the specified server resource tree folder.
* If you are to publish the report to a server disk path, you can find the report files in the specified location on the computer where you installed Logi Report Server.

## Viewing Reports Scheduled to Email/Printer/Fax/FTP

When you schedule to publish a report to email, printer, fax, or FTP, you can view the scheduled report if the specified address or location is available to you.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684009879-Applying-Dynamic-Names-for-Published-Result-Files)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684008855-Importing-and-Exporting-Scheduled-Tasks)
