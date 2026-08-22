---
title: "General Operations in Page Report"
id: 5741438977943
section: "Page Report Studio Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741438977943-General-Operations-in-Page-Report
updated_at: 2022-10-31T17:18:16Z
---

# General Operations in Page Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741482707223-Editing-Page-Reports-in-Page-Report-Studio)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741469351191-Making-Simple-Modifications-to-Page-Report-Objects)

# General Operations in Page Report

When you open a page report in Page Report Studio, you can perform general operations such as manage report tab, turn report pages, navigate through report data using TOC, apply a style, change report parameter values, configure Page Report Studio options, Quick schedule report tasks, and more. This topic describes how you can perform the general operations on page report.

This topic contains the following sections:

* [Managing Page Report Tabs](#ReportTab)
* [Turning Page Report Pages](#TurnPage)
* [Navigating Through Page Report Data](#Navigate)
* [Refreshing Page Report Data](#Refresh)
* [Switching Page Report Data Mode](#DataMode)
* [Applying a Style in Page Report](#Style)
* [Changing Page Report Parameter Values](#Param)
* [Opening Links in Page Report](#Link)
* [Customizing Page Report Studio Skin and Toolbars](#Option)
* [Zooming in and out the Page Report Page](#Zoom)
* [Setting up the Report Page for Page Report](#Page)
* [Adding and Removing Page Breaks](#PageBreak)
* [Undoing and Redoing Actions](#Undo)
* [Keeping the Page Report as a Background Task](#Background)
* [Scheduling Page Report Tasks Using Quick Schedule](#Schedule)
* [Showing or Hiding Editing Marks](#EditingMark)
* [Showing or Hiding User Information](#User)
* [Asking for Help](#Help)
* [Exiting the Page Report](#Exit)

## Managing Page Report Tabs

A page report can include one or more report tabs. The Go To drop-down list on the toolbar panel or the tabs on the top of the report list the display names of all the open report tabs in the current report. Selecting the display name of an inactive report tab will make it active. You can manage report tabs in a page report easily:

* **Opening and closing a report tab**  
   In a page report, a report tab can be shown or not. To close (hide) the active report tab, select **Menu** > **File** > **Close Report Tab**. If there are one or more report tabs open other than the active report tab, the close action will hide the active report tab; in the case that the active report tab is the only report tab open, the close action will prompt you whether to close the report.
* To open (show) a hidden report tab, select **Menu** > **File** > **Open** or the **Open** button ![Open button](https://devnet.logianalytics.com/hc/article_attachments/9905577968791/btn_open.gif) on the toolbar to display the Open Report Tabs dialog box, in which the report tabs open in the current report are marked with a check symbol. Select the report tabs you want to open, clear the ones you want to close, and then select **OK**.

  ![Open Report Tabs dialog](https://devnet.logianalytics.com/hc/article_attachments/9905673445015/opnrpt.gif)

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) If the report designer specifies the Work as Subreport property of a report tab to "true", even though you select the report tab in the Open Report Tabs dialog box, you cannot open the report tab from the Go To drop-down list or by switching the tabs on the top of the report.
* **Renaming a report tab**  
   To rename a report tab, first activate it, then select **Menu** > **File** > **Rename Report Tab**. In the [Rename Report Tab](https://devnet.logianalytics.com/hc/en-us/articles/5741440419223-Rename-Report-Tab-Dialog-Box-Properties) dialog box, specify a new display name for the report tab.
* **Deleting a report tab**   
   To delete a report tab, first activate it, then select **Menu** > **File** > **Delete Report Tab**. The only report tab open cannot be deleted.

  ![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/9905614395415/criticalicon.gif) You need a [Logi Report Live license for Server](https://devnet.logianalytics.com/hc/en-us/articles/5741452341143-Logi-Report-Licenses#ServerLive) to delete page report tabs. For more product information, including new purchases and upgrades, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

**Tip:** You can configure the [Page Report Studio profile](https://devnet.logianalytics.com/hc/en-us/articles/5741427459479-Page-Report-Studio-Profile-Properties#Switch) to enable switching report tabs using tabs. With report tabs you can easily activate a report tab in a report by selecting the tab representing the report tab on the report tab bar, and closing, renaming and deleting a report tab can also be accomplished by right-clicking the report tab and choosing the corresponding command from the shortcut menu.

## Turning Page Report Pages

If a report tab includes more than one page, to turn between the report pages, you can:

* Select the **First Page** button ![First Page button](https://devnet.logianalytics.com/hc/article_attachments/9905660274583/btn_firstpg.gif), **Previous Topic** button ![Previous Page button](https://devnet.logianalytics.com/hc/article_attachments/9905672321175/btn_prevpg.gif), **Next Topic** button ![Next Page button](https://devnet.logianalytics.com/hc/article_attachments/9905660312471/btn_nxtpg.gif), or **Last Page** button ![Last Page button](https://devnet.logianalytics.com/hc/article_attachments/9905660342807/btn_lastpg.gif) on the View toolbar.
* Type a number into the page box ![Page box](https://devnet.logianalytics.com/hc/article_attachments/9905660253463/btn_pgrpt_pageno.gif) and press **Enter** to go to that page.
* Select **Menu** > **View** > **Turn To** and then select the corresponding command on the submenu. When the Page command is selected, Server displays the [Turn to Page](https://devnet.logianalytics.com/hc/en-us/articles/5741419052311-Turn-to-Page-Dialog-Box-Properties) dialog box for you to input the page number.
* Use the scroll bar or mouse wheel to scroll up/down the report tab.

## Navigating Through Page Report Data

You can use the TOC Browser to navigate through a report tab. To show the TOC Browser, select **Menu** > **View** > **TOC Browser**.

![TOC Browser](https://devnet.logianalytics.com/hc/article_attachments/9905661525783/pgrpt_edit_genrl_toc.gif)

In the TOC Browser, expand the Report node, select a component or a node with the group value that you want to browse to. Server displays the page that contains the component or the matching data.

Server organizes the table of contents in the TOC Browser into a tree structure. The root node represents the report tab that you are currently viewing. The component names indicate components in the report tab. The group values show hierarchical groups.

For report tabs designed in Logi Report Designer, you can customize the nodes displayed on their TOC tree as well as the format of the TOC tree.

## Refreshing Page Report Data

To fetch the data of the current report again, you can select **Menu** > **View** > **Refresh**.

## Switching the Report Data Mode

If you are making a lot of changes to the report, it may be faster to limit the number of records to one page while you make the changes and then change it back to full data mode to view the final result.

By default, Server enables the [Partial Report Result](https://devnet.logianalytics.com/hc/en-us/articles/7985371543191-Customize-Profile-Dialog-Box-Properties#Partial) feature in the server profile. You can switch the report data mode to view full data or only a specified number of data in a report. To show a certain number of data, select **Partial Data** from the data mode drop-down list on the toolbar, type a positive integer in the text box that follows, and then press **Enter** or select outside the text box. By default, the number is 5000, which means Server retrieves the first 5000 records. To show all data records, select **Full Data**.

## Applying a Style in Page Report

You can apply a style to a report to change its appearance and characteristics. You can create and set up your own styles in Designer. Then when you publish your reports to Server, you can include these custom styles with the published reports. When you run a report, Server enables the style feature, and you can select a style to apply to the report.

* **Applying a style to a report**  
   To apply a style to a report, make sure nothing is selected in the report, then select **Menu** > **Report** > **Style** and select the required one from the submenu, or select the required style from the style drop-down list ![Style Drop-down List](https://devnet.logianalytics.com/hc/article_attachments/9905659942039/btn_pgrpt_style.gif) on the toolbar. When a style is applied to the whole report, all components in the report will take a uniform appearance.
* **Applying a style to a data component**  
   The data component (banded objects, crosstabs, charts, and tables) in a report can take a different style of its own. To apply a style to a data component, select it, and then select the required one from the **Menu** > **Report** > **Style** menu, or select the required style from the style list ![Style Drop-down List](https://devnet.logianalytics.com/hc/article_attachments/9905659942039/btn_pgrpt_style.gif) on the toolbar, or right-click the component and select **Apply Style** from the shortcut menu to select the required style in the [Apply Style](https://devnet.logianalytics.com/hc/en-us/articles/5741409991703-Apply-Style-Dialog-Box-Properties) dialog box. If the data component is contained in a banded object (for a chart, in a table also), you can also select the Inherit Style option to make it inherit the style of its parent data component.

However, if there is only one style available to the report, this style will be applied to the report by default, in which case, you will find that all these style related commands are hidden.

## Changing Page Report Parameter Values

If there are parameters in the current report, you can change the parameter values. To do this, select **Menu** > **Report** > **Change Parameters**, then in the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/5741410399895-Enter-Parameter-Values-Dialog-Box-Properties) dialog box, specify the value for each parameter and select **OK** to run the report with the specified parameter values.

You can also use parameter web controls to dynamically change the parameter values of a report. For more information, see [Applying Web Controls](https://devnet.logianalytics.com/hc/en-us/articles/5741483099159-Applying-Web-Controls-in-Page-Report).

## Opening Links in Page Report

When a page report is developed with links in Designer, which refer to locations specified by URLs, email addresses or other reports, you can select the links' trigger objects in Page Report Studio to open the links. However, if the report designer did not give the Link action the highest Click Priority at report design time, you have to right-click on the trigger objects and select the corresponding link item on the shortcut menu to open the links. For example, if a trigger object is linked with a detail report, you need to right-click the object and select Detail Report from the shortcut menu to open the detail report. Meanwhile, when opening the detail report, Server may prompt the [Encoding](https://devnet.logianalytics.com/hc/en-us/articles/5741388231447-Encoding-Dialog-Box-Properties) dialog box, asking you to provide encoding and DB security information before rendering the report. Select **OK** in the dialog box if you want to run a detail report using the same encoding and DB security settings as that of the master report.

After opening a linked report, you can select the **Back** button ![Back button](https://devnet.logianalytics.com/hc/article_attachments/9905619459095/btn_back.gif) or **Next** button ![Next button](https://devnet.logianalytics.com/hc/article_attachments/9905660473367/btn_next.gif) on the toolbar to return back to the previous report or go forward to the next report, or select the **Visited Reports** button ![Visited Reports button](https://devnet.logianalytics.com/hc/article_attachments/9905631747863/btn_goto.gif) and then select a report to switch to that report directly. When opening a detail report in the current window, you can also select the **Visited Reports** button ![Visited Reports button](https://devnet.logianalytics.com/hc/article_attachments/9905631747863/btn_goto.gif) and then select a report to open that report directly.

## Customizing Page Report Studio Skin and Toolbars

You can set the skin for Page Report Studio and customize toolbars in the Interactive View and Basic View.

**To set the skin for Page Report Studio:**

1. Select **Menu** > **View** > **Options**. Server displays the [Options](https://devnet.logianalytics.com/hc/en-us/articles/5741411515543-Options-Dialog-Box-Properties) dialog box.
2. In the Option tab, select a skin.

   ![Options dialog - Option tab](https://devnet.logianalytics.com/hc/article_attachments/9905661542167/optn_optn.gif)
3. Select **OK**.

**To customize toolbars in the Interactive View:**

1. Select **Menu** > **View** > **Options**. Server displays the [Options](https://devnet.logianalytics.com/hc/en-us/articles/5741411515543-Options-Dialog-Box-Properties) dialog box.
2. Select the **Customize** tab.

   ![Options dialog - Customize tab](https://devnet.logianalytics.com/hc/article_attachments/9905661554071/optn_cstmz.gif)
3. By default, you can customize the items and their order on the three built-in toolbars - Standard, View, and Analysis. To modify a toolbar, select it in the Current Toolbar box, remove unnecessary items from the **Selected Tools** box, and add the items you want from the **Available Tools** box. Select the **Move Up** button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif) or **Move Down** button![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif) to adjust the order of the items on the toolbar.
4. To add a toolbar, select the **Add New Toolbar** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif). Server displays the New Toolbar Name dialog box. Type the toolbar name, select **OK**. Then add items to the new toolbar.
5. To delete a toolbar, select it and select the **Remove Toolbar** button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif).
6. To load the default settings of the skin and the Standard, View, and Analysis toolbars, select **Restore Defaults**.
7. Select **OK** to apply the settings.

You can close the Standard, View, or Analysis toolbar by clearing the corresponding item on the Menu > View > Toolbar menu.

**To customize the toolbar items in the Basic View:**

1. Select the **Customize Toolbar Items** button ![Customize Toolbar Items button](https://devnet.logianalytics.com/hc/article_attachments/9905631747863/btn_goto.gif). Server displays a menu.

   ![Customize Toolbar Items icon drop-down menu](https://devnet.logianalytics.com/hc/article_attachments/9905673531415/pgrpt_edit_genrl_tlbrbv.gif)
2. For an item that does not display on the toolbar, for example, **TOC Browser**, you see the closed eye icon ![Closed Eye icon](https://devnet.logianalytics.com/hc/article_attachments/9905660454295/btn_eyeclosed.gif) on its right. Select the icon if you want to add it on the toolbar.
3. To hide an item from the toolbar, select the item, then select the open eye icon ![Open Eye icon](https://devnet.logianalytics.com/hc/article_attachments/9905661608983/btn_eyeopen.gif).
4. To adjust the order of an item on the toolbar, drag it to another position in the menu.
5. To exit the menu, select outside the menu box.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) The toolbar in the Basic View and **Customize Toolbar Items** menu restores to the default status once you clear browsing data from your browser, discarding any of your changes.

## Zooming in and out the Page Report Page

You can zoom in or out the report page by selecting a magnification from the Zoom list ![Zoom list](https://devnet.logianalytics.com/hc/article_attachments/9905671972631/btn_pgrpt_zoom.gif) on the View toolbar. You can also select **Menu** > **View** > **Zoom** to show the [Zoom](https://devnet.logianalytics.com/hc/en-us/articles/5741404399639-Zoom-Dialog-Box-Properties) dialog box, and then specify the magnification.

## Setting up the Report Page for Page Report

1. Navigate to **Menu** > **File** > **Page Setup**. Server displays the [Page Properties](https://devnet.logianalytics.com/hc/en-us/articles/5741440252183-Page-Properties) dialog box.

   ![Page Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/9905661644055/pgprpty_gnrl.gif)
2. ![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9905577570711/___newv19.2.png "New for version 19.2.")By default, Server applies [pagination mode](https://devnet.logianalytics.com/hc/en-us/articles/5741476487063-General-Operations-in-Web-Report#PageMode) to the report and displays the report in multiple pages. In the **General** tab, clear **Page Layout** if you want to apply continuous mode to the report and displays it in a single page.
3. Specify the page size, orientation, and margin of the report page. You can select **Auto Fit** to calculate the page width/height according to the width/height of the contents within the page dynamically, which is useful when the width/height of the contents is unpredictable and when the report to export is not huge.
4. In the **Export** tab, specify the page properties for different export formats, which will apply when you [advanced run](https://devnet.logianalytics.com/hc/en-us/articles/5741439314455-Running-Reports) and [schedule to run](https://devnet.logianalytics.com/hc/en-us/articles/5741483471255-Scheduling-Tasks-to-Run-Reports) the report on Server as well as [export the report tab](https://devnet.logianalytics.com/hc/en-us/articles/5741462638999-Exporting-Printing-a-Page-Report) in Page Report Studio.

   ![Page Properties dialog box - Export tab](https://devnet.logianalytics.com/hc/article_attachments/9905673597079/pgprpty_export.gif)
5. ![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9905577570711/___newv19.2.png "New for version 19.2.")Select each format from the **Export To** drop-down list, then select or clear **Page Layout** to apply the [pagination mode or continuous mode](https://devnet.logianalytics.com/hc/en-us/articles/5741476487063-General-Operations-in-Web-Report#PageMode) to the corresponding report outputs according to your requirements.
6. By default, the page properties you define for the report in the **General** tab of the dialog box apply to all export formats. You can customize the page properties for each format by clearing **Auto** (you can do this when you do not clear **Page Layout**) and then defining the properties as you want.
7. Select **OK** to accept the changes and close the dialog box.

## Adding and Removing Page Breaks

A new page will be generated in a report tab only when the space in a page has been fully occupied or there exists a break control in this page, for example, a page break that is inserted in the page.

To insert a page break, select **Menu** > **Insert** > **Page Break**, then select the mouse button on the destination where you want the page break to be inserted.

To remove a page break, right-click on the report body, then on the shortcut menu, select **Remove Page Breaks** and then the corresponding page break from the submenu.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* You can insert page breaks into the report body.
* You can insert page breaks into banded objects only when you meet the following conditions:
  + The parent of the banded object is the report body.
  + There is not any existing page panel in the report body.
  + Its Position property of the banded object is static.

## Undoing and Redoing Actions

You can undo or redo some actions by selecting **Menu** > **Edit** > **Undo** or **Redo** (or the **Undo** button ![Undo button](https://devnet.logianalytics.com/hc/article_attachments/9905616106263/btn_undo.gif) or **Redo** button ![Redo button](https://devnet.logianalytics.com/hc/article_attachments/9905616128151/btn_redo.gif) on the toolbar).

## Keeping the Page Report as a Background Task

When you have selected [Enable Background Task for Reports](https://devnet.logianalytics.com/hc/en-us/articles/7985371543191-Customize-Profile-Dialog-Box-Properties#BackgroundTask) in the server profile, you can make the page reports that you have opened in Page Report Studio as background tasks so as to access them the next time directly without running them again.

To keep an opened page report as a background task, select the **Keep as Background Task**  button ![Keep as Background Task button](https://devnet.logianalytics.com/hc/article_attachments/9905672440983/btn_bkgrndtsk.gif) on the toolbar, the report will then be added in the [Background Tasks table](https://devnet.logianalytics.com/hc/en-us/articles/5741438263319-Managing-Report-Running-Tasks#Background) of the My Reports page on the Server Console. You can open it there when needed.

## Scheduling Page Report Tasks Using Quick Schedule

By default, Server enables the [Quick Schedule from Web/Page Studio](https://devnet.logianalytics.com/hc/en-us/articles/7985371543191-Customize-Profile-Dialog-Box-Properties#Schedule) property in the server profile. Therefore, in Page Report Studio, you can schedule tasks to publish page reports to email, FTP site, or the Server versioning system. However, the Quick Schedule feature inside Page Report Studio does not provide the full functionalities. If you want to use the full schedule system of Server, go to the [Server Console to submit the schedule tasks](https://devnet.logianalytics.com/hc/en-us/articles/5741483442455-Scheduling-Reports).

1. Make sure you are in the Basic View of Page Report Studio.
2. Select the page report tab on which the schedule task is based, then select the **Quick Schedule** button ![Quick Schedule button](https://devnet.logianalytics.com/hc/article_attachments/9905654855063/btn_schdl.gif) on the toolbar. Server displays the [Quick Schedule](https://devnet.logianalytics.com/hc/en-us/articles/5741411744023-Quick-Schedule-Dialog-Box-Properties) dialog box.

   ![Quick Schedule dialog](https://devnet.logianalytics.com/hc/article_attachments/9905661684119/qckschdl.gif)

   If the page report has not been saved, you will be prompted to save the report.
3. Specify the name for the task in the Schedule Name text box.
4. From the Time Type drop-down list specify the time for when the task is to be performed.
   * To perform the task as soon as you submit it, select **Immediately**.
   * If you want to run the task repeatedly, select **Periodically**, then specify to run it daily, weekly, or monthly at a specific time of a day.
5. From the Publish To drop-down list, select where you want to publish the report and
   specify the settings of the publish type.
   * To publish the report to email, select **E-mail**. Then specify the email information such as addresses, subject and comments respectively; if you want to send the report in the mail body, select **E-mail Result in** and select a format for the report: HTML or Text (when you select HTML, the report will replace the comments you input for the email; if you select Text, Server will position the comments in front of the report); select **Attachment in** to send the report as an attachment and specify the format of the attachment file.
   * To publish the report to the Logi Report Server versioning system, select **Version System**. Then choose a format in which you want to send the report.
   * To publish the report to an FTP site, select **FTP**. Then specify the information for the FTP site and select a format in which you want to send the report.
6. Select **OK** to submit the task.

When the task is finished, you can go to the My Tasks page on the Server Console to [view the scheduled report](https://devnet.logianalytics.com/hc/en-us/articles/5741469840663-Viewing-Scheduled-Reports).

## Showing or Hiding Editing Marks

In Page Report Studio, you can use editing marks (dashed outlines of objects) for purposes such as aligning, moving, and resizing. By default, the editing marks are shown only when you create a new blank report in Page Report Studio. You can select **Menu** > **View** > **Editing Marks** to switch the status of the editing marks as required.

## Showing or Hiding User Information

The User Information bar shows the current username, catalog path and name, and report path and name. You can select **Menu** > **View** > **User Information Bar** to show or hide the bar.

## Asking for Help

At any time, you can select **Menu** > **Help** > **User's Guide** to open the Page Report Studio user documentation. Furthermore, you can select the **Help** button in any dialog box to show the help about the dialog box. You can also use the Help menu to open the documentation and access Logi Report website for more information.

## Exiting the Page Report

If you want to close the current report and release the resources, just select **Menu** > **File** > **Exit** (or the **Exit** button ![Exit button](https://devnet.logianalytics.com/hc/article_attachments/9905673637271/btn_pgrpt_exit.gif) which is always at the upper right corner of the Page Report Studio window, or the close button of the browser window).

When you close the only report tab in a page report, Server asks whether you want to close the report. In case that you have modified the report without saving it, Server prompts you to [save the report](https://devnet.logianalytics.com/hc/en-us/articles/5741462847767-Saving-a-Page-Report).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741482707223-Editing-Page-Reports-in-Page-Report-Studio)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741469351191-Making-Simple-Modifications-to-Page-Report-Objects)
