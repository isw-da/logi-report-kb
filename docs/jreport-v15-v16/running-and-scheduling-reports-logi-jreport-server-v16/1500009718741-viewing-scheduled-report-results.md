---
title: "Viewing Scheduled Report Results"
id: 1500009718741
section: "Running and Scheduling Reports Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718741-Viewing-Scheduled-Report-Results
updated_at: 2021-11-03T06:56:34Z
---

# Viewing Scheduled Report Results

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718721-Applying-Dynamic-Names-for-Published-Result-Files)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692522-Importing-and-Exporting-Scheduled-Tasks)

# Viewing Scheduled Report Results

When a scheduled task is finished, you can view the result of the scheduled report as required. To view the result, first of all you need to know the corresponding result's location. To get the location information:

1. In the Logi JReport Server console, select **My Tasks**  on the system toolbar, then select the **Completed** tab, where all the successfully scheduled tasks are recorded.

   ![My Tasks - Completed tab](https://devnet.logianalytics.com/hc/article_attachments/4412131411991/wkrpt_sch_vwrst1.gif)
2. Locate the task in the tab and select the name of the task in the Schedule Name column.
3. In the Result Details table, the location information of the scheduled result is available in the Details column.

   ![Task Details](https://devnet.logianalytics.com/hc/article_attachments/4412139520535/wkrpt_sch_vwrst2.gif)

Below is a list of the sections covered in this topic:

* [Viewing Results Scheduled to Version](#Version)
* [Viewing Results Scheduled to Disk](#Disk)
* [Viewing Results Scheduled to E-mail/Printer/Fax/FTP](#Other)

## Viewing Results Scheduled to Version

One way to view results that are scheduled to version from the Logi JReport Server console is via the scheduled task records. To do this:

1. Select **My Tasks** on the system toolbar, then select the **Completed** tab.
2. In the tab, locate the right task and select the name of the task in the Schedule Name column.
3. In the Result Details table, the links to different result formats are available for viewing in the To Version row. Select the format links to view the results.

   Page report results are opened in Page Report Studio which has permission control, so to view page report results successfully you need to have the [Execute and/or Edit permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009718881-Managing-Permissions) on the results. To view a page report result, you can choose one of the following ways:

   * Select the **Page Report Result** link which is available when you have the Execute permission on the page report result. It will then be opened in Page Report Studio in the mode specified by the [Default View for Page Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#PageMode) option in the server profile. If Default View is Interactive View but you do not have the Edit permission, you will get an error message.
   * Select the  **Run** button ![Run button](https://devnet.logianalytics.com/hc/article_attachments/4412139520791/btn_srv_run.gif) on the result row to access Basic View of Page Report Studio. Execute permission is required.
   * Select the **Edit** button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4412131412247/btn_srv_edit.gif) on the result row to access Interactive View of Page Report Studio. Edit permission is required.
   * Select the **Advanced Run** button ![Advanced Run button](https://devnet.logianalytics.com/hc/article_attachments/4412139521047/btn_srv_advrun.gif) on the result row. In this way, you can customize the result resolution and the view mode of Page Report Studio: Basic View, Basic View Only or Interactive View. Execute permission is required.

Another way to achieve the same purpose is via the [version table](https://devnet.logianalytics.com/hc/en-us/articles/1500009717961-Browsing-Versions) which to some extent varies with the archive location type specified in the Publish > To Version tab:

* If the archive location is Built-in Version Folder:
  1. In the server resource tree, browse to the row that the original report is in.
  2. Do either of the following:
     + Select the report row and select **Tools** > **Version** on the task bar of the Resources page.
     + Select the report row, right-click in the row and select **Version** from the shortcut menu.
     + Put the mouse pointer over the report row and select the **Version** button ![Version button](https://devnet.logianalytics.com/hc/article_attachments/4412131412631/btn_srv_vrsn.gif) on the floating toolbar.
  3. In the Report Result Versions table, the scheduled results of different format types are listed in the Result column. Select the format links to view the results. For a page report result, you can also make use of the action buttons.
* If the archive location is the My Reports or Public Reports folder, which requires providing a path and a name for the scheduled result in the server resource tree:
  1. In the server resource tree, browse to the row that the result is in.
  2. Put the mouse pointer over the result row and select the **Version** button ![Version button](https://devnet.logianalytics.com/hc/article_attachments/4412131412631/btn_srv_vrsn.gif) on the floating toolbar (or you can use one of the other two methods shown in the above procedure to display the version table).
  3. In the Result Versions table, the scheduled results of different format types are listed in the Result column. Select the format links to view the results. For a page report result, you can also make use of the action buttons.

You can also use [URL commands](https://devnet.logianalytics.com/hc/en-us/articles/1500009719381-Working-with-Logi-Report-Server#ViewResult) to view the report results that are scheduled to version.

**Tip:** In the version table, the unviewed version results are highlighted in bold. You can cancel the highlighting by setting the property web.version.mark\_unviewed to false in the server.properties file in `<install_root>\bin`.

## Viewing Results Scheduled to Disk

When scheduling a report to disk,

* If you choose Publish to Server Disk Path, you are required to provide a disk file path and file name with correct format type as the suffix for each report tab in the report. After scheduling succeeds, you can find the corresponding result files available at the specified location on the computer where Logi JReport Server is installed.
* If you choose Publish to Server Resource Tree, you are required to provide a path following the server resource tree and file name with correct format type as the suffix for each report tab in the report. For example,
  + To follow the My Reports folder path, start with "/USERFOLDERPATH/*username*/" (change *username* to the real user name with which you log onto Logi JReport Server).

    Example: /USERFOLDERPATH/admin/report1.pdf
  + To follow the Public Reports folder, start with "/".

    Example: /report2.html.

  If the specified folder which is the parent folder of the result file has a real path, the generated result file will be saved to the real path; if the folder doesn't have a real path, the generated result will be saved to `<install_root>\jreports`, which is the mapped disk path of the root node "/" in the specified path.

## Viewing Results Scheduled to E-mail/Printer/Fax/FTP

When a report is scheduled to e-mail, printer, fax, or FTP, you can view the scheduled result if the specified address or location is available to you.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718721-Applying-Dynamic-Names-for-Published-Result-Files)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692522-Importing-and-Exporting-Scheduled-Tasks)
