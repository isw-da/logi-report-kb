---
title: "General Operations in Web Report"
id: 5741476487063
section: "Web Report Studio Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741476487063-General-Operations-in-Web-Report
updated_at: 2022-10-31T17:18:32Z
---

# General Operations in Web Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741490579607-Editing-Web-Reports-in-Web-Report-Studio)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741476545943-Inserting-Components-in-Web-Report)

# General Operations in Web Report

This topic describes how you can perform general operations in Web Report Studio, including undoing and redoing actions, switching between Partial Data and Full Data, quick schedule, configure the report page, exit Web Report Studio, and more.

This topic contains the following sections:

* [Opening Another Web Report](#OpenReport)
* [Undoing/Redoing Actions](#Undo)
* [Turning Component Pages](#TurnPage)
* [Showing/Hiding Editing Marks](#EditingMarks)
* [Switching the Report Data Mode](#DataMode)
* [Setting up the Report Page for Web Report](#Page)
* [Responsive View](#Responsive)
* [Scheduling Report Tasks](#Schedule)
* [Sharing a Web Report](#Share)
* [Viewing In-memory Cube Status](#CubeStatus)
* [Asking for Help](#Help)
* [Exiting Web Report Studio](#Exit)

## Opening Another Web Report

Select **Menu** > **File** > **Open** or the **Open** button ![Open button](https://devnet.logianalytics.com/hc/article_attachments/9905577968791/btn_open.gif) on the toolbar. Server displays the [Select a Report dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741466701463-Select-a-Report-Dialog-Box-Properties) and lists the web reports in the same folder as the current open report. Select the web report you want to open from the default folder or from another folder, and then select **OK**.

![Select a Report dialog](https://devnet.logianalytics.com/hc/article_attachments/9905654714903/slctrpt.gif)

## Undoing/Redoing Actions

You can undo or redo some actions. To do this, select **Menu** > **Edit** > **Undo** or **Redo** (or the **Undo** button ![Undo button](https://devnet.logianalytics.com/hc/article_attachments/9905616106263/btn_undo.gif) or **Redo** button ![Redo button](https://devnet.logianalytics.com/hc/article_attachments/9905616128151/btn_redo.gif) on the toolbar).

## Turning Component Pages

When a table or a crosstab contains more than one page, Server displays a navigation bar specific for the component under the component. You can use the navigation bar to view the pages you want: select the corresponding button to go to the first page, the previous page, the next page, or the last page, or type a number in the text box to go to that page.

![Turn Component Page](https://devnet.logianalytics.com/hc/article_attachments/9905633465367/wbrpt_edt_genrl_cmpntpg.gif)

## Showing/Hiding Editing Marks

You can use editing marks (dashed outlines of objects) for purposes such as aligning, moving, and resizing. Server displays the editing marks by default. To switch the status of the editing marks, select **Menu** > **View** > **Editing Marks**.

## Switching the Report Data Mode

If you are making a lot of changes to the report, it may be faster to limit the number of records to one page while you make the changes and then change it back to full data mode to view the final result.

By default, Server enables the [Partial Report Result](https://devnet.logianalytics.com/hc/en-us/articles/7985371543191-Customize-Profile-Dialog-Box-Properties#Partial) feature in the server profile. You can switch the report data mode to view full data or only a specified number of data in a report. To show a certain number of data, select **Partial Data** from the data mode drop-down list on the toolbar, type a positive integer in the text box that follows, and then press **Enter** or select outside the text box. By default, the number is 5000, which means Server retrieves the first 5000 records. To show all data records, select **Full Data**.

## Setting up the Report Page for Web Report

This section describes the two Logi Report page layout modes - pagination mode and continuous mode and how you can customize page settings for report display and output.

### Page Mode

Each report applies a page mode to determine the layout of the report pages, which can be either pagination mode or continuous mode. By default, Server applies pagination mode to the reports.

* **Pagination Mode**  
  Pagination mode displays the page margins and enables multiple pages. In this mode, you can specify the page shape and size in the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741459540631-Page-Setup-Dialog-Box-Properties#Studio).
  Once defined, Logi Report lays out report content according to these specifications. If the content exceeds the specified size, the page break control starts a new page with the same size. The report's total page size in pagination mode is determined by both the content's size and the page break controls, such as Fill Whole Page, On New Page, and Page Break.
* **Continuous Mode**  
  In continuous mode, the whole report displays in a single page that has no specific shape and size (the size of the page depends on the size of the content), which is useful for dashboard style reports where you don't want multiple pages. However, if the report is very large, it may run out of memory and be very unresponsive. In continuous page mode, Logi Report skips all properties that you specify in pagination mode, including the [page breaks](https://devnet.logianalytics.com/hc/en-us/articles/5741438977943-General-Operations-in-Page-Report#PageBreak) in page panel. In this way, when there is more than one page panel in a report, Logi Report displays all content contained in different page panels in the same page, and only displays the first page panel's page header and footer.

When editing a page report tab or web report on Server, ![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9905577570711/___newv19.2.png "New for version 19.2.")you can customize the page mode of the report to display it in either of the two modes in different scenarios, by setting the **Page Layout** property in the [Page Setup dialog box](../dialog/dlg_pgstup.htm). For example, you can display a web report in multiple pages when you open it in Web Report Studio, but in a single page in the HTML output.

### Customizing Page Settings for Report Display and Output

1. Navigate to **Menu** > **File** > **Page Setup**. Server displays the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741459540631-Page-Setup-Dialog-Box-Properties#Studio).

   ![Page Setup dialog - General - Web Report](https://devnet.logianalytics.com/hc/article_attachments/9905633489303/pgstup_gnrl_prnt.gif)
2. In the **General** tab, select the page type: **Web Report** or **Print Report**, which determines the unit of the page size, pixel or inch.
3. ![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9905577570711/___newv19.2.png "New for version 19.2.")By default, Server applies [pagination mode](#PageMode) to the report and displays the report in multiple pages. Clear **Page Layout** if you want to apply continuous mode to the report and displays it in a single page.
4. Specify the size, orientation, and margins of the report page. You can select **Auto Fit** to calculate the page width/height according to the width/height of the contents within the page dynamically, which is useful when the content width/height is unpredictable and when the report is not huge.
5. In the **Export** tab, specify the page properties for different export formats, which will apply when you [advanced run](https://devnet.logianalytics.com/hc/en-us/articles/5741439314455-Running-Reports) and [schedule to run](https://devnet.logianalytics.com/hc/en-us/articles/5741483471255-Scheduling-Tasks-to-Run-Reports) the report on Server as well as [export the report](https://devnet.logianalytics.com/hc/en-us/articles/5741470801175-Exporting-Printing-a-Web-Report) in Web Report Studio.

   ![Page Setup dialog - Export tab](https://devnet.logianalytics.com/hc/article_attachments/9905654801687/pgstup_export.gif)
6. ![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9905577570711/___newv19.2.png "New for version 19.2.")Select each format from the **Export To** drop-down list, then select or clear **Page Layout** to apply the [pagination mode or continuous mode](#PageMode) to the corresponding report outputs according to your requirements.
7. By default, the page properties you define for the report in the **General** tab of the dialog box apply to all export formats. You can customize the page properties for each format by clearing **Auto** (you can do this when you do not clear **Page Layout**) and then defining the properties as you want.
8. Select **OK** to accept the changes and close the dialog box.

## Responsive View

When Web Report Studio is in the [View Mode](https://devnet.logianalytics.com/hc/en-us/articles/5741464180119-Web-Report-Studio-Server-v19#Mode), it can be responsive to any size of browsers on any mobile devices or computers. Report components excluding the report header and footer can automatically scale and fold according to the current browser window size. Information presented is always legible and the layout perfectly adapts to best utilize the available display screen. This is called Responsive View. It always works on mobile devices. When Web Report Studio runs on computers, Server enables Responsive View by default by selecting the profile option [View Web Reports in Responsive Mode,](https://devnet.logianalytics.com/hc/en-us/articles/5741456214039-Customizing-Web-Report-Studio-Profile#View) and you can then open or close it in the View Mode of Web Report Studio as follows:

1. Select the **Customize Toolbar Items** button ![Customize Toolbar Items button](https://devnet.logianalytics.com/hc/article_attachments/9905654831767/btn_wbrpt_cstmz.gif) on the toolbar and then select **Open Responsive Mode** or **Close Responsive Mode** from the menu.

   Server displays the Open Responsive Mode button ![Open Responsive Mode button](https://devnet.logianalytics.com/hc/article_attachments/9905616210327/btn_rspnsvopn.gif) or Close Responsive Mode button ![Close Responsive Mode button](https://devnet.logianalytics.com/hc/article_attachments/9905616238231/btn_rspnsvcls.gif) on the toolbar.
2. Select the button on the toolbar to open or close Responsive View.

## Scheduling Report Tasks

By default, Server enables the [Quick Schedule from Web/Page Studio](https://devnet.logianalytics.com/hc/en-us/articles/7985371543191-Customize-Profile-Dialog-Box-Properties#Schedule) property in the server profile. Therefore, in Web Report Studio, you can schedule tasks to publish web reports to email, FTP site, or the Server versioning system. However, the Quick Schedule feature inside Web Report Studio does not provide the full functionalities. If you want to use the full schedule system of Server, go to the [Server Console to submit the schedule tasks](https://devnet.logianalytics.com/hc/en-us/articles/5741483442455-Scheduling-Reports).

1. Make sure you are in the View Mode of Web Report Studio.
2. Select the **Quick Schedule** button ![Quick Schedule button](https://devnet.logianalytics.com/hc/article_attachments/9905654855063/btn_schdl.gif) on the toolbar. Server displays the [Quick Schedule dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741436360471-Quick-Schedule-Dialog-Box-Properties).

   ![Quick Schedule dialog](https://devnet.logianalytics.com/hc/article_attachments/9905654880151/qckschdl.gif)

   If you haven't saved the current open report, Server prompts you to save the report.
3. Type the name for the task in the **Schedule Name** text box.
4. From the **Time Type** drop-down list, specify when you want to perform the task.
   * To perform the task as soon as you submit it, select **Immediately**.
   * If you want to run the task repeatedly, select  **Periodically**, then specify to run it daily, weekly, or monthly at a specific time of a day.
5. From the **Publish To** drop-down list, select where you want to publish the report and then specify the settings of the publish type.
   * To publish the report to email, select **E-mail**. Then specify the email information such as addresses, subject, and comments, respectively. If you want to send the report in the mail body, select **E-mail Result in** and then select a format for the report: **HTML** or **Text**. If you select HTML, the report will overwrite the comments you input for the email. If you select Text, Server will position the comments in front of the report. Select **Attachment in** to send the report as an attachment and then specify the format of the attachment file.
   * To publish the report to the Server versioning system, select **Version System**. Then choose a format in which you want to send the report.
   * To publish the report to an FTP site, select **FTP**. Then specify the information for the FTP site and select a format in which you want to send the report.
6. Select **OK** to submit the task.

You can then go to the My Tasks page on the Server Console to [view the scheduled report](https://devnet.logianalytics.com/hc/en-us/articles/5741469840663-Viewing-Scheduled-Reports).

## Sharing a Web Report

If the current web report is not a shared report and you are the owner of the report, you can use the Share Report feature to share it to others. To share a web report, make sure you have already [saved it](https://devnet.logianalytics.com/hc/en-us/articles/5741464615703-Saving-a-Web-Report), then select **Menu** > **File** > **Share** or select the **Share** button ![Share button](https://devnet.logianalytics.com/hc/article_attachments/9905616075543/btn_share.gif) on the toolbar. Server displays the [Share Report dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741446516119-Share-Report-Dialog-Box-Properties). Set the options for sharing the report. For more information, see [Sharing Web Reports](https://devnet.logianalytics.com/hc/en-us/articles/5741461964439-Sharing-Web-Reports).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)After you remove all the components that reference a business view from a shared report and then save the shared report, the business view will no longer be available to the shared report.

## Viewing In-memory Cube Status

If you have selected [Show Status When Using Cube Data](https://devnet.logianalytics.com/hc/en-us/articles/7985371543191-Customize-Profile-Dialog-Box-Properties#CubeStatus) in the server profile, you can find the **Cube Status** button ![Cube Status button](https://devnet.logianalytics.com/hc/article_attachments/9905654904343/btn_cbstts.gif) on the toolbar. By selecting this button you can view the information about whether the data components in the current report apply [in-memory cubes](https://devnet.logianalytics.com/hc/en-us/articles/5741437977495-Managing-In-Memory-Cubes) and the reasons if not in the [Cube Status dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741422256407-Cube-Status-Dialog-Box-Properties).

## Asking for Help

At any time, you can select **Menu** > **Help** > **User's Guide** to open the Web Report Studio user documentation. Furthermore, you can select the Help button in any dialog box to show the help document about the dialog box. You can also use the Help menu to access Logi Report website for more information.

## Exiting Web Report Studio

To close the current web report and release the resources, select **Menu** > **File** > **Exit** (or the button **X** on the far right of the toolbar). Do not use the close button of the browser window as that may not release the resources that the report used.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741490579607-Editing-Web-Reports-in-Web-Report-Studio)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741476545943-Inserting-Components-in-Web-Report)
