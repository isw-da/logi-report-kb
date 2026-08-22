---
title: "General Operations in Web Report"
id: 4405690686231
section: "Web Report Studio Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690686231-General-Operations-in-Web-Report
updated_at: 2022-01-27T07:59:52Z
---

# General Operations in Web Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684035223-Editing-Web-Reports-in-Web-Report-Studio)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684040855-Inserting-Components-in-Web-Report)

# General Operations in Web Report

This topic describes how you can perform general operations in Web Report Studio, including undoing and redoing actions, switching between Partial Data and Full Data, quick schedule, configure the report page, exit Web Report Studio, and more.

This topic contains the following sections:

* [Opening Another Web Report](#OpenReport)
* [Undoing/Redoing Actions](#Undo)
* [Turning Component Pages](#TurnPage)
* [Showing/Hiding Editing Marks](#EditingMarks)
* [Switching the Report Data Mode](#DataMode)
* [Setting up the Report Page](#Page)
* [Responsive View](#Responsive)
* [Scheduling Report Tasks](#Schedule)
* [Sharing a Web Report](#Share)
* [Viewing In-memory Cube Status](#CubeStatus)
* [Asking for Help](#Help)
* [Exiting Web Report Studio](#Exit)

## Opening Another Web Report

Select **Menu** > **File** > **Open** or the **Open** button ![Open button](https://devnet.logianalytics.com/hc/article_attachments/4420461454615/btn_open.gif) on the toolbar. Server displays the [Select a Report](https://devnet.logianalytics.com/hc/en-us/articles/4405683880855-Select-a-Report-Dialog-Box-Properties) dialog box and lists the web reports in the same folder as the current open report. Select the web report you want to open from the default folder or from another folder, and then select **OK**.

![Select a Report dialog](https://devnet.logianalytics.com/hc/article_attachments/4420447086359/slctrpt.gif)

## Undoing/Redoing Actions

You can undo or redo some actions. To do this, select **Menu** > **Edit** > **Undo** or **Redo** (or the **Undo** button ![Undo button](https://devnet.logianalytics.com/hc/article_attachments/4420447053079/btn_undo.gif) or **Redo** button ![Redo button](https://devnet.logianalytics.com/hc/article_attachments/4420461455639/btn_redo.gif) on the toolbar).

## Turning Component Pages

When a table or a crosstab contains more than one page, Server displays a navigation bar specific for the component under the component. You can use the navigation bar to view the desired pages: select the corresponding button to go to the first page, the previous page, the next page, or the last page, or type a number in the text box to go to that page.

![Turn Component Page](https://devnet.logianalytics.com/hc/article_attachments/4420461502103/wbrpt_edt_genrl_cmpntpg.gif)

## Showing/Hiding Editing Marks

You can use editing marks (dashed outlines of objects) for purposes such as aligning, moving, and resizing. Server displays the editing marks by default. To switch the status of the editing marks, select **Menu** > **View** > **Editing Marks**.

## Switching the Report Data Mode

If you are making a lot of changes to the report, it may be faster to limit the number of records to one page while you make the changes and then change it back to full data mode to view the final result.

By default, Server enables the [Partial Report Result](https://devnet.logianalytics.com/hc/en-us/articles/4405683590167-Configuring-Server-Profile#Partial) feature in the server profile. You can switch the report data mode to view full data or only a specified number of data in a report. To show a certain number of data, select **Partial Data** from the data mode drop-down list on the toolbar, type a positive integer in the text box that follows, and then press **Enter** or select outside the text box. By default, the number is 5000, which means Server retrieves the first 5000 records. To show all data records, select **Full Data**.

## Setting up the Report Page

1. Select **Menu** > **File** > **Page Setup**. Server displays the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/4405683867543-Page-Setup-Dialog-Box-Properties#Studio) dialog box.

   ![Page Setup dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4420447086871/pgstup_gnrl_prnt.gif)
2. In the **General** tab, select the page type: **Web Report** or **Print Report**, which determines the unit of the page size, pixel or inch.
3. Specify the size, orientation, and margins of the report page. You can select the **Auto Fit** option to calculate the page width/height according to the width/height of the contents within the page dynamically, which is useful when the content width/height is unpredictable and when the report is not huge.
4. In the **Export** tab, specify the page properties for the exported report, which will apply when you [advanced run](https://devnet.logianalytics.com/hc/en-us/articles/4405690675223-Running-Reports) and [schedule to run](https://devnet.logianalytics.com/hc/en-us/articles/4405684005015-Scheduling-Tasks-to-Run-Reports) the report on Logi Report Server as well as [export the report](https://devnet.logianalytics.com/hc/en-us/articles/4405690685335-Exporting-Printing-the-Web-Report-Result) in Web Report Studio.

   ![Page Setup dialog - Export tab](https://devnet.logianalytics.com/hc/article_attachments/4420453434519/pgstup_export.gif)

   By default, the page properties defined for the report in the **General** tab of the dialog box applies to all export formats. You can define the page properties for each format by selecting a format from the **Export To** drop-down list, clearing the **Auto** option, and then defining the properties as you want.
5. Select **OK** to accept the changes and close the dialog box.

## Responsive View

When Web Report Studio is in the [View Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405684031639-Web-Report-Studio-Server-v18#Mode), it can be responsive to any size of browsers on any mobile devices or computers. Report components excluding the report header and footer can automatically scale and fold according to the current browser window size. Information presented is always legible and the layout perfectly adapts to best utilize the available display screen. This is called Responsive View. It always works on mobile devices. When Web Report Studio runs on computers, Server enables Responsive View by default by selecting the profile option [View Web Reports in Responsive Mode,](https://devnet.logianalytics.com/hc/en-us/articles/4405684049047-Customizing-Web-Report-Studio-Profile#View) and you can then open or close it in the View Mode of Web Report Studio as follows:

1. Select the **Customize Toolbar Items** button ![Customize Toolbar Items button](https://devnet.logianalytics.com/hc/article_attachments/4420461502487/btn_wbrpt_cstmz.gif) on the toolbar and then select **Open Responsive Mode** or **Close Responsive Mode** from the menu.

   Server displays the Open Responsive Mode button ![Open Responsive Mode button](https://devnet.logianalytics.com/hc/article_attachments/4420447053591/btn_rspnsvopn.gif) or Close Responsive Mode button ![Close Responsive Mode button](https://devnet.logianalytics.com/hc/article_attachments/4420447053847/btn_rspnsvcls.gif) on the toolbar.
2. Select the button on the toolbar to open or close Responsive View.

## Scheduling Report Tasks

By default, Server enables the [Quick Schedule from Web/Page Studio](https://devnet.logianalytics.com/hc/en-us/articles/4405683590167-Configuring-Server-Profile#Schedule) option in the server profile. Therefore, in Web Report Studio, you can schedule tasks to publish web reports to email, FTP site, or the Logi Report Server versioning system. However, the Quick Schedule feature inside Web Report Studio does not provide the full functionalities. If you want to use the full schedule system of Logi Report Server, go to the [Server Console to submit the schedule tasks](https://devnet.logianalytics.com/hc/en-us/articles/4405690676119-Scheduling-Reports).

1. Make sure you are in the View Mode of Web Report Studio.
2. Select the **Quick Schedule** button ![Quick Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4420447088151/btn_schdl.gif) on the toolbar. Server displays the [Quick Schedule](https://devnet.logianalytics.com/hc/en-us/articles/4405690600215-Quick-Schedule-Dialog-Box-Properties) dialog box.

   ![Quick Schedule dialog](https://devnet.logianalytics.com/hc/article_attachments/4420447088407/qckschdl.gif)

   If you haven't saved the current open report, Server prompts you to save the report.
3. Type the name for the task in the **Schedule Nam**e text box.
4. From the **Time Type** drop-down list, specify when you want to perform the task.
   * To perform the task as soon as you submit it, select **Immediately**.
   * If you want to run the task repeatedly, select  **Periodically**, then specify to run it daily, weekly, or monthly at a specific time of a day.
5. From the **Publish To** drop-down list, select where you want to publish the report and then specify the settings of the publish type.
   * To publish the report to email, select **E-mail**. Then specify the email information such as addresses, subject, and comments, respectively. If you want to send the report in the mail body, select **E-mail Result in** and then select a format for the report: **HTML** or **Text**. If you selected HTML, the report overwrites the comments you input for the email. If you selected Text, Server positions the comments in front of the report. Select **Attachment in** to send the report as an attachment and then specify the format of the attachment file.
   * To publish the report to the Logi Report Server versioning system, select **Version System**. Then choose a format in which you want to send the report.
   * To publish the report to an FTP site, select **FTP**. Then specify the information for the FTP site and select a format in which you want to send the report.
6. Select **OK** to submit the task.

You can then go to the My Tasks page on the Server Console to [view the scheduled report](https://devnet.logianalytics.com/hc/en-us/articles/4405684011031-Viewing-Scheduled-Report-Results).

## Sharing a Web Report

If the current web report is not a shared report and you are the owner of the report, you can use the Share Report feature to share it to others. To share a web report, make sure you have already [saved it](https://devnet.logianalytics.com/hc/en-us/articles/4405684044439-Saving-a-Web-Report), then select **Menu** > **File** > **Share** or select the **Share** button ![Share button](https://devnet.logianalytics.com/hc/article_attachments/4420453393687/btn_share.gif) on the toolbar. Server displays the [Share Report dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683876503-Share-Report-Dialog-Box-Properties). Set the options for sharing the report. For more information, see [Sharing Web Reports](https://devnet.logianalytics.com/hc/en-us/articles/4405683936279-Sharing-Web-Reports).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)After you remove all the components that reference a business view from a shared report and then save the shared report, the business view will no longer be available to the shared report.

## Viewing In-memory Cube Status

If you select [Show Status When Using Cube Data](https://devnet.logianalytics.com/hc/en-us/articles/4405683590167-Configuring-Server-Profile#CubeStatus) in the server profile, you will find the **Cube Status** button ![Cube Status button](https://devnet.logianalytics.com/hc/article_attachments/4420461505175/btn_cbstts.gif) on the toolbar, by selecting which you can view the information about whether the data components in the current report apply [in-memory cubes](https://devnet.logianalytics.com/hc/en-us/articles/4405690641431-Managing-In-Memory-Cubes) and the reasons if not in the [Cube Status](https://devnet.logianalytics.com/hc/en-us/articles/4405683793303-Cube-Status-Dialog-Box-Properties) dialog box.

## Asking for Help

At any time, you can select **Menu** > **Help** > **User's Guide** to open the Web Report Studio user documentation. Furthermore, you can select the Help button in any dialog box to show the help document about the dialog box. You can also use the Help menu to access Logi Report website for more information.

## Exiting Web Report Studio

To close the current web report and release the resources, select **Menu** > **File** > **Exit** (or the button **X** on the far right of the toolbar). Do not use the close button of the browser window as that may not release the resources that the report used.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684035223-Editing-Web-Reports-in-Web-Report-Studio)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684040855-Inserting-Components-in-Web-Report)
