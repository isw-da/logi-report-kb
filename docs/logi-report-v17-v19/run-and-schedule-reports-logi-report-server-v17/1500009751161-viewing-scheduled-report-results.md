---
title: "Viewing Scheduled Report Results"
id: 1500009751161
section: "Run and Schedule Reports Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009751161-Viewing-Scheduled-Report-Results
updated_at: 2021-07-25T07:18:40Z
---

# Viewing Scheduled Report Results

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724322-Applying-Dynamic-Names-for-Published-Result-Files)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009751141-Importing-and-Exporting-Scheduled-Tasks)

# Viewing Scheduled Report Results

When a report schedule task is finished, you can view the results of the reports included in the task at any time. Depending on the destinations where the report results are published, the ways to view the results vary.

Select the following links to view the topics:

* [Viewing Results Scheduled to Version](#Version)
  + [Via the Schedule Task Details](#TaskDetail)
  + [Via the Version Table](#VersionTable)
* [Viewing Results Scheduled to Disk](#Disk)
* [Viewing Results Scheduled to E-mail/Printer/Fax/FTP](#Other)

## Viewing Results Scheduled to Version

There are two ways you can take to view the report results that are published to the versioning system: via the schedule task details and via the version table.

### Via the Schedule Task Details

1. In the Logi Report Server console, select **My Tasks** on the system toolbar, then select the **Completed** tab, where all the successfully scheduled tasks are recorded.

   ![Completed Task List](https://devnet.logianalytics.com/hc/article_attachments/4404936765463/wkrpt_sch_vwrst1.gif)
2. Locate the required task and do any of the following:
   * Select the name of the task in the Schedule Name column.
   * Select the **Details** button ![Detail button](https://devnet.logianalytics.com/hc/article_attachments/4404936765719/btn_srv_details.gif) on the floating toolbar of the task row.
   * Select the task row and select **Edit** > **Details** on the task bar of the My Tasks page.
3. In the Result Details list, the links to different result formats are available in the To Version section. Select the format links to view the results.

   ![Result Details](https://devnet.logianalytics.com/hc/article_attachments/4404942479767/wkrpt_sch_vwrst2.gif)

   Logi Report results and web report results can be further exported to the HTML, PDF, Text, Excel, XML, RTF, and Postscript formats via Logi Report Server. When you view a Logi Report result or web report result, Report Server displays the below dialog box for you to specify the export format and configure the [format settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009747301-Advanced-Run#HTML). For a Logi Report result, you also need to select the report tabs in the page report you want to export.

   ![Result Export Settings](https://devnet.logianalytics.com/hc/article_attachments/4404936765975/wkrpt_sch_vwrst3.gif)

   Page report results are opened in Page Report Studio which has permission control, so to view page report results successfully you need to have the [Execute and/or Edit permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009751241-Managing-Permissions) on the results. To view a page report result, you can choose one of the following ways:

   * Select the **Page Report Result** link which is available when you have the Execute permission on the page report result. The result is then opened in Page Report Studio in the mode specified by the [Default View for Page Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#PageMode) option in the server profile. If Default View is Interactive View but you do not have the Edit permission, you will get an error message.
   * Select the **Run** button ![Run button](https://devnet.logianalytics.com/hc/article_attachments/4404942480023/btn_srv_run.gif) on the result row to access Basic View of Page Report Studio. Execute permission is required.
   * Select the **Edit** button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404936766231/btn_srv_edit.gif) on the result row to access Interactive View of Page Report Studio. Edit permission is required.
   * Select the **Advanced Run** button ![Advanced Run button](https://devnet.logianalytics.com/hc/article_attachments/4404936766487/btn_srv_advrun.gif) on the result row. In this way, you can customize the result resolution and the view mode of Page Report Studio: Basic View, Basic View Only or Interactive View. Execute permission is required.

### Via the Version Table

Based on the different archive location that has been specified when creating the report schedule task, you will need to access the [version table](https://devnet.logianalytics.com/hc/en-us/articles/1500009750201-Browsing-Versions) of a result in different way.

* If the archive location of the result is Built-in Version Folder:
  1. In the server resource tree, browse to the row that the original report is in.
  2. Do any of the following to open the Report Result Versions table:
     + Select the report row and select **Tools** > **Version** on the task bar of the Resources page.
     + Select the report row, right-click in the row and select **Version** from the shortcut menu.
     + Put the mouse pointer over the report row and select the **Version** button ![Version button](https://devnet.logianalytics.com/hc/article_attachments/4404942480279/btn_srv_vrsn.gif) on the floating toolbar.
  3. In the Results column of the version table, the results of different formats are listed. Select the format links to view the results.

     ![Report Result Versions](https://devnet.logianalytics.com/hc/article_attachments/4404936766743/wkrpt_sch_vwrst4.gif)
* If the archive location of the result is the My Reports Folder or Public Reports Folder, which requires providing the path and name for the result in the server resource tree:
  1. In the server resource tree, browse to the row that the result is in based on the specified path and name information.
  2. Do any of the following to open the Result Versions table:
     + Select the name of the result directly.
     + Put the mouse pointer over the result row and select the **Version** button ![Version button](https://devnet.logianalytics.com/hc/article_attachments/4404942480279/btn_srv_vrsn.gif) on the floating toolbar.
     + Select the result row, right-click in the row and select **Version** from the shortcut menu.
     + Select the result row and select **Tools** > **Version** on the task bar of the Resources page.
  3. In the Results column of the version table, the results of different formats are listed. If the schedule task is based on multiple reports, the results of different formats for each report tab in a page report and each web report are listed. Select the format links to view the results.

     ![Multiple Result Versions](https://devnet.logianalytics.com/hc/article_attachments/4404936766999/wkrpt_sch_vwrst5.gif)

You can also use [URL commands](https://devnet.logianalytics.com/hc/en-us/articles/1500009725002-Working-with-Logi-Report-Server#ViewResult) to view the report results that are published to version.

## Viewing Results Scheduled to Disk

When you schedule a report to publish its result to disk, the result can either be published to the server resource tree or to a server disk path, then after the schedule task is completed successfully:

* If the result is published to the server resource tree, you can view the result files from the specified server resource tree folder.
* If the result is published to a server disk path, you can find the result files available at the specified location on the computer where Logi Report Server is installed.

## Viewing Results Scheduled to E-mail/Printer/Fax/FTP

When you schedule a report to publish its result to e-mail, printer, fax, or FTP, you can view the scheduled result if the specified address or location is available to you.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724322-Applying-Dynamic-Names-for-Published-Result-Files)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009751141-Importing-and-Exporting-Scheduled-Tasks)
