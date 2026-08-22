---
title: "Viewing Scheduled Report Results"
id: 1500009674841
section: "Running and Scheduling Reports Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009674841-Viewing-Scheduled-Report-Results
updated_at: 2021-07-24T20:53:42Z
---

# Viewing Scheduled Report Results

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674821-Applying-Dynamic-Names-for-Published-Result-Files)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674801-Importing-and-Exporting-Scheduled-Tasks)

# Viewing Scheduled Report Results

When a scheduled task is finished, you can view the result of the scheduled report as required. To view the result, first of all you need to know the corresponding result's location. To get the location information:

1. On the Logi JReport Console page, select **My Tasks**  on the system toolbar, then select the **Completed** tab, where all the successfully scheduled tasks are recorded.
2. Locate the task in the tab and select the name of the task in the Schedule Name column.
3. In the Result Details table, the location information of the scheduled result is available in the Details column.

Below is a list of the sections covered in this topic:

* [Viewing Results Scheduled to Version](#Version)
* [Viewing Results Scheduled to Disk](#Disk)
* [Viewing Results Scheduled to E-Mail/Printer/Fax/FTP](#Other)

## Viewing Results Scheduled to Version

One way to view results that are scheduled to version on the Logi JReport Console page is via the scheduled task records. To do this:

1. Select **My Tasks**  on the system toolbar, then select the **Completed** tab.
2. In the tab, locate the right task and select the name of the task in the Schedule Name column.
3. In the Result Details table, the links to different result formats are available for viewing in the To Version row. Select the format links to view the results.

   Page report results are opened in Page Report Studio which has permission control, so to view page report results successfully you need to have the [Execute and/or Edit permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009674981-Managing-Permissions) on the results. To view a page report result, you can choose one of the following ways:

   * Select the **Page Report Result** link which is available when you have the Execute permission on the page report result. It will then be opened in Page Report Studio in the mode specified by the [Default View for Page Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#PageMode) option in the server profile. If Default View is Interactive View but you do not have the Edit permission, you will get an error message.
   * Select the  **Run** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920422807/btn_srv_run.gif) on the result row to access Basic View of Page Report Studio. Execute permission is required.
   * Select the **Edit** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926643991/btn_srv_edit.gif) on the result row to access Interactive View of Page Report Studio. Edit permission is required.
   * Select the **Advanced Run** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920423319/btn_srv_advrun.gif) on the result row. In this way, you can customize the result resolution and the view mode of Page Report Studio: Basic View, Basic View Only or Interactive View. Execute permission is required.

Another way to achieve the same purpose is via the [version table](https://devnet.logianalytics.com/hc/en-us/articles/1500009673741-Browsing-Versions) which to some extent varies with the archive location type specified in the Publish > To Version tab:

* If the archive location is Built-in Version Folder:
  1. On the Logi JReport Console > Resources page, browse to the row that the original report is in.
  2. Do either of the following:
     + Select the report row and select **Tools** > **Version** on the task bar of the Resources page.
     + Select the report row, right-click in the row and select **Version** from the shortcut menu.
     + Put the mouse pointer over the report row and select the **Version** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926662807/btn_srv_vrsn.gif) on the floating toolbar.
  3. In the Report Result Versions table, the scheduled results of different format types are listed in the Result column. Select the format links to view the results. For a page report result, you can also make use of the action buttons.
* If the archive location is the My Reports or Public Reports folder, which requires providing a path and a name for the scheduled result in the server resource tree:
  1. On the Logi JReport Console > Resources page, browse to the row that the result is in.
  2. Put the mouse pointer over the result row and select the **Version** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926662807/btn_srv_vrsn.gif) on the floating toolbar (or you can use one of the other two methods shown in the above procedure to display the version table).
  3. In the Result Versions table, the scheduled results of different format types are listed in the Result column. Select the format links to view the results. For a page report result, you can also make use of the action buttons.

You can also use [URL commands](https://devnet.logianalytics.com/hc/en-us/articles/1500009650542-Working-with-Logi-JReport-Server-Guide-v15-Server#ViewResult) to view the report results that are scheduled to version.

**Tip:** In the version table, the unviewed version results are highlighted in bold. You can cancel the highlighting by setting the property web.version.mark\_unviewed to false in the server.properties file in `<install_root>\bin`.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Viewing Results Scheduled to Disk

When scheduling a report to disk,

* If you choose Publish to Server Disk Path, you are required to provide a disk file path and file name with correct format type as the suffix for each report tab in the report. After scheduling succeeds, you can find the corresponding result files available at the specified location on the computer where Logi JReport Server is installed.
* If you choose Publish to Server Resource Tree, you are required to provide a path following the server resource tree and file name with correct format type as the suffix for each report tab in the report. For example,
  + To follow the My Reports folder path, start with "/USERFOLDERPATH/admin/".

    Example: /USERFOLDERPATH/admin/report1.pdf
  + To follow the Public Reports folder, start with "/".

    Example: /report2.html.

  If the specified folder which is the parent folder of the result file has a real path, the generated result file will be saved to the real path; if the folder doesn't have a real path, the generated result will be saved to `<server_install_root>/Logi JReports/`, which is the mapped disk path of the root node "/" in the specified path.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Viewing Results Scheduled to E-Mail/Printer/Fax/FTP

When a report is scheduled to e-mail, printer, fax, or FTP, you can view the scheduled result if the specified address or location is available to you.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674821-Applying-Dynamic-Names-for-Published-Result-Files)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674801-Importing-and-Exporting-Scheduled-Tasks)
