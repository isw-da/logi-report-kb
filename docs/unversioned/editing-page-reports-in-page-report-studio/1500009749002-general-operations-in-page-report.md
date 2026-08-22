---
title: "General Operations in Page Report"
id: 1500009749002
section: "Editing Page Reports in Page Report Studio"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009749002-General-Operations-in-Page-Report
updated_at: 2021-07-24T00:47:52Z
---

# General Operations in Page Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777521-Editing-Page-Reports-in-Page-Report-Studio)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749042-Making-Simple-Modifications-to-Page-Report-Objects)

# General Operations in Page Report

When you open a page report in Page Report Studio, you can perform general operations such as manage report tab, turn report pages, navigate through report data using TOC, apply a style, change report parameter values, **configure Page Report Studio options, Quick schedule report tasks, and more. This topic describes how you can perform the general operations on page report.**

* **Managing report tabs**  
   A page report can include one or more report tabs. The Go To drop-down list on the toolbar panel or the tabs across the top of the report list the display names of all the open report tabs in the current report. Selecting the display name of an inactive report tab will make it active. You can manage report tabs in a page report easily as follows:
  + **Opening and closing a report tab**  
     In a page report, a report tab can be shown or not. To close (hide) the active report tab, select **Menu** > **File** > **Close Report Tab**. If there are one or more report tabs open other than the active report tab, the close action will hide the active report tab; in the case that the active report tab is the only report tab open, the close action will prompt you whether to close the report.
  + To open (show) a hidden report tab, select **Menu** > **File** > **Open** or the **Open** button ![Open button](https://devnet.logianalytics.com/hc/article_attachments/4404880136471/btn_open.gif) on the toolbar to display the Open Report Tabs dialog box, in which the report tabs open in the current report are marked with a check symbol. Select the report tabs you want to open, clear the ones you want to close, and then select **OK**.

    ![Open Report Tabs dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880260631/opnrpt.gif)
  + **Renaming a report tab**  
     To rename a report tab, first activate it, then select **Menu** > **File** > **Rename Report Tab**. In the [Rename Report Tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009745002-Rename-Report-Tab-Dialog-Box-Properties) dialog box, specify a new display name for the report tab.
  + **Deleting a report tab**   
     To delete a report tab, first activate it, then select **Menu** > **File** > **Delete Report Tab**. The only report tab open cannot be deleted.

    ![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404885352855/criticalicon.gif)You need a [Logi Report Live license for Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009776661-Logi-Report-Licenses#ServerLive) to delete report tabs. If you do not have the license, contact your Logi Analytics account manager to obtain it.

  **Tip:** You can configure the [Page Report Studio profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009777681-Customizing-Page-Report-Studio-Profile#Switch) to enable switching report tabs using tabs. With report tabs you can easily activate a report tab in a report by selecting the tab representing the report tab on the report tab bar, and closing, renaming and deleting a report tab can also be accomplished by right-clicking the report tab and choosing the corresponding command from the shortcut menu.
* **Turning the report pages**  
   If a report tab includes more than one page, to turn between the report pages, you can:
  + Select the **First Page** button ![First Page button](https://devnet.logianalytics.com/hc/article_attachments/4404885381143/btn_firstpg.gif), **Previous Topic** button ![Previous Page button](https://devnet.logianalytics.com/hc/article_attachments/4404880246679/btn_prevpg.gif), **Next Topic** button ![Next Page button](https://devnet.logianalytics.com/hc/article_attachments/4404880246935/btn_nxtpg.gif), or **Last Page** button ![Last Page button](https://devnet.logianalytics.com/hc/article_attachments/4404880247319/btn_lastpg.gif) on the View toolbar.
  + Type a number into the page box ![Page box](https://devnet.logianalytics.com/hc/article_attachments/4404885380887/btn_pgrpt_pageno.gif) and press **Enter** to go to that page.
  + Select **Menu** > **View** > **Turn To** and then select the corresponding command on the submenu. When the Page command is selected, Server displays the [Turn to Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009773201-Turn-to-Page-Dialog-Box-Properties) dialog box for you to input the page number.
  + Use the scrollbar or mouse wheel to scroll up/down the report tab.
* **Navigating through the report data**You can use the TOC Browser to navigate through a report tab. To show the TOC Browser, select **Menu** > **View** > **TOC Browser**.

  ![TOC Browser](https://devnet.logianalytics.com/hc/article_attachments/4404880260887/pgrpt_edit_genrl_toc.gif)

  In the TOC Browser, expand the Report node, select a component or a node with the group value that you want to browse to. The page that contains the component or the matching data will then be shown.

  The table of contents in the TOC Browser is organized into a tree structure. The root node represents the report tab that you are currently viewing. The component names indicate components in the report tab. The group values show hierarchical groups.

  For report tabs designed in Logi Report Designer, the nodes displayed on their TOC tree as well as the format of the TOC tree can be customized.
* **Refreshing the report result**  
   To fetch the data of the current report again, you can select **Menu** > **View** > **Refresh**.
* **Switching the report data mode**If you are making a lot of changes to the report, it may be faster to limit the number of records to 1 page while you make the changes and then change it back to full data mode to view the final result.
    
  When the [Partial Report Result](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile#Partial) feature is enabled in the server profile, you can switch the report data mode to view full data or only a specified number of data in a report. To show a certain number of data, select **Partial Data** from the data mode drop-down list on the toolbar and set a positive integer in the text box that follows, then press **Enter** or select outside the text box. By default, the number is 5000, which means the first 5000 records will retrieved. To show all data records, select **Full Data**.
* **Applying a style**  
   You can apply a style to a report to change its appearance and characteristics. You can create and set up your own styles in Logi Report Designer. When you publish your reports to Logi Report Server, you can include these custom styles with the published reports. When you run a report, Server enables the style feature and you can select a style to apply to the report.
  + **Applying a style to a report**  
     To apply a style to a report, make sure nothing is selected in the report, then select **Menu** > **Report** > **Style** and select the required one from the submenu, or select the required style from the style drop-down list ![Style Drop-down List](https://devnet.logianalytics.com/hc/article_attachments/4404885379863/btn_pgrpt_style.gif) on the toolbar. When a style is applied to the whole report, all components in the report will take a uniform appearance.
  + **Applying a style to a data component**  
     The data component (banded objects, crosstabs, charts, and tables) in a report can take a different style of its own. To apply a style to a data component, select it and then select **Menu** > **Report** > **Style** and select the required one from the submenu, or select the required style from the style drop-down list ![Style Drop-down List](https://devnet.logianalytics.com/hc/article_attachments/4404885379863/btn_pgrpt_style.gif) on the toolbar, or right-click the component and select **Apply Style** from the shortcut menu to select the required style in the [Apply Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009771941-Apply-Style-Dialog-Box-Properties) dialog box. If the data component is contained in a banded object (for a chart, in a table also), you can also select the Inherit Style option to make it inherit the style of its parent data component.

  However, if there is only one style available to the report, this style will be applied to the report by default, in which case, you will find that all these style related commands are hidden.
* **Changing the report parameter values**   
   If there are parameters in the current report, you can change the parameter values at runtime. To do this, select **Menu** > **Report** > **Change Parameters**, then in the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009772161-Enter-Parameter-Values-Dialog-Box-Properties) dialog box, specify the value for each parameter and select **OK** to run the report with the specified parameter values.

  You can also use parameter web controls to dynamically change the parameter values of a report at runtime. For more information, see [Applying Web Controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009749062-Applying-Web-Controls-in-Page-Report).
* **Opening links**  
  When a page report is developed with links in Logi Report Designer, which refer to locations specified by URLs, e-mail addresses or other reports, you can select the links' trigger objects in Page Report Studio to open the links. However, if the report designer did not give the Link action the highest Click Priority at report design time, you have to right-click on the trigger objects and select the corresponding link item on the shortcut menu to open the links. For example, if a trigger object is linked with a detail report, you need to right-click the object and select Detail Report from the shortcut menu to open the detail report. Meanwhile, when opening the detail report, you may be prompted with the [Encoding](https://devnet.logianalytics.com/hc/en-us/articles/1500009772141-Encoding-Dialog-Box-Properties) dialog box, asking you to provide encoding and DB security information before the report result is produced. Select OK in the dialog box if you want to run a detail report using the same encoding and DB security settings as that of the master report.

  After opening a linked report, you can select the Back ![Back button](https://devnet.logianalytics.com/hc/article_attachments/4404880165655/btn_back.gif) or Next ![Next button](https://devnet.logianalytics.com/hc/article_attachments/4404885382551/btn_next.gif) button on the toolbar to return back to the previous report or go forward to the next report, or select ![Go To button](https://devnet.logianalytics.com/hc/article_attachments/4404885331991/btn_goto.gif) and select an item from the drop-down list to switch to that report directly. When opening a detail report, if the detail report is opened in the current window, a "link path", which tracks the linking action will be displayed in the Go To drop-down list if the list is available. Selecting the item in the list will switch to the corresponding report.
* **Setting Page Report Studio options**  
   Page Report Studio enables you to set the skin and customize toolbars. To do this:
  1. Select **Menu** > **View** > **Options**, or right-click anywhere on the toolbar area and select **Options** from the shortcut menu to open the [Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009744902-Options-Dialog-Box-Properties) dialog box.
  2. In the Option tab, set the skin of Page Report Studio user interface.

     ![Options dialog - Option tab](https://devnet.logianalytics.com/hc/article_attachments/4404885393175/optn_optn.gif)
  3. In the Customize tab,

     ![Options dialog - Customize tab](https://devnet.logianalytics.com/hc/article_attachments/4404880261527/optn_cstmz.gif)

     + To modify a toolbar, select it in the Current Toolbar box, remove those unnecessary items from the Selected Tools box, and add required tools from the Available Tools box. Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif) to adjust the order of the tools on the toolbar.
     + To add a toolbar, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif) to show the New Toolbar Name dialog box, then specify the toolbar name, select **OK** to return to the Options dialog box, and set the tools for the new toolbar.
     + To delete a toolbar, select it and select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif).
  4. To load the default settings, including the skin, and the three built-in toolbars, namely Standard, View, and Analysis, select the **Restore Defaults** button.
  5. Select **OK** to apply the settings.

  **Tip:** To close a toolbar, right-click anywhere on the toolbar area, then on the shortcut menu, select the item corresponding to the toolbar name. You can also do this to open an invisible toolbar, such as a newly created one. The open/close toolbar operation can also be achieved by selecting the corresponding item on the Toolbar submenu of the View menu.
* **Tuning report page magnification**  
   You can zoom in or out the report page by selecting a magnification from the Zoom list ![Zoom list](https://devnet.logianalytics.com/hc/article_attachments/4404880241815/btn_pgrpt_zoom.gif) on the View toolbar. You can also select **Menu** > **View** > **Zoom** to show the [Zoom](https://devnet.logianalytics.com/hc/en-us/articles/1500009773221-Zoom-Dialog-Box-Properties) dialog box, and then specify the magnification.
* **Setting up the report page**
  1. Select **Menu** > **File** > **Page Setup**. Server displays the [Page Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009772861-Page-Properties) dialog box.

     ![Page Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404880261911/pgprpty_gnrl.gif)
  2. In the General tab, specify the page size, orientation, and margins of the report page. You can select the **Auto Fit** option to calculate the page width/height according to the width/height of the contents within the page dynamically, which is useful when the width/height of the contents is unpredictable and when the report to export is not huge.
  3. In the Export tab, specify the page properties for the exported result of the report tab, which will be applied when [advanced running](https://devnet.logianalytics.com/hc/en-us/articles/1500009778381-Running-Reports) and [scheduling to run](https://devnet.logianalytics.com/hc/en-us/articles/1500009778421-Scheduling-Tasks-to-Run-Reports) the report tab on Logi Report Server as well as [exporting the report tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009777541-Exporting-Printing-Page-Report-Result)  in Page Report Studio.

     ![Page Properties dialog - Export tab](https://devnet.logianalytics.com/hc/article_attachments/4404885393431/pgprpty_export.gif)

     By default, the page properties defined for the report tab in the General tab of the dialog box will be applied to the exported result of all export formats. You can define the page properties for each exported result by selecting a format from the Type drop-down list, clearing the **Auto** option, and then defining the properties as you want.
  4. Select **OK** to accept the changes and close the dialog box
* **Adding/Removing page breaks**  
   A new page will be generated in a report tab only when the space in a page has been fully occupied or there exists a break control in this page, for example, a page break that is inserted in the page.

  To insert a page break, select **Menu** > **Insert** > **Page Break**, then select the mouse button on the destination where you want the page break to be inserted.

  To remove a page break, right-click on the report body, then on the shortcut menu, select **Remove Page Breaks** and then the corresponding page break from the submenu.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)

  + You can insert page breaks into the report body.
  + You can insert page breaks into banded objects only when you meet the following conditions:
    - The parent of the banded object is the report body.
    - There is not any existing page panel in the report body.
    - Its Position property of the banded object is static.
* **Undoing/Redoing actions**  
   You can undo or redo some actions by selecting **Menu** > **Edit** > **Undo** or **Redo** (or the **Undo** button ![Undo button](https://devnet.logianalytics.com/hc/article_attachments/4404880138391/btn_undo.gif) or **Redo** button ![Redo button](https://devnet.logianalytics.com/hc/article_attachments/4404880138647/btn_redo.gif) on the toolbar).
* **Keeping the report as a background task**   
  When you have selected the option [Enable Background Task for Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile#BackgroundTask) in the server profile, you can make the page reports that you have opened in Page Report Studio as background tasks so as to access them the next time directly without running them again.

  To keep an opened page report as a background task, select the **Keep as Background Task**  button ![Keep as Background Task button](https://devnet.logianalytics.com/hc/article_attachments/4404885382167/btn_bkgrndtsk.gif) on the toolbar, the report will then be added in the [Background Tasks table](https://devnet.logianalytics.com/hc/en-us/articles/1500009777301-Managing-Report-Running-Tasks#Background) of the My Reports page in the Server Console. You can open it there when needed.
* **Scheduling report tasks using Quick Schedule**  
   If you have enabled the option [Quick Schedule from Web/Page Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile#Schedule) in the server profile, you can schedule tasks to publish page reports to e-mails, FTP sites, or the Logi Report Server versioning system in Page Report Studio. However, the Quick Schedule feature inside Page Report Studio does not provide the full functionalities. If you want to use the full schedule system of Logi Report Server, go to the [Server Console to submit the schedule tasks](https://devnet.logianalytics.com/hc/en-us/articles/1500009749542-Scheduling-Reports).
  1. Make sure you are in Basic View of Page Report Studio.
  2. Switch to the page report tab on which the schedule task is based, then select the **Quick Schedule** button ![Quick Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4404880187927/btn_schdl.gif) on the toolbar. Server displays the [Quick Schedule](https://devnet.logianalytics.com/hc/en-us/articles/1500009772921-Quick-Schedule-Dialog-Box-Properties) dialog box.

     ![Quick Schedule dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885393687/qckschdl.gif)

     If the page report has not been saved, you will be prompted to save the report.
  3. Specify the name for the task in the Schedule Name text box.
  4. From the Time Type drop-down list specify the time for when the task is to be performed.
     + To perform the task as soon as you submit it, select **Immediately**.
     + If you want to run the task repeatedly, select  **Periodically**, then specify to run it daily, weekly, or monthly at a specific time of a day.
  5. From the Publish To drop-down list, select where to publish the report result and
     specify the settings of the publish type.
     + To publish the report result to e-mail, select **E-mail**. Then specify the e-mail information such as addresses, subject and comments respectively; if you want to send the report result in the mail body, select **E-mail Result in** and select a format for the result: HTML or Text (when HTML is selected the comments you input for the e-mail will be overwritten by the report result; if Text is selected the comments will be positioned in front of the report result); select **Attachment in** to send the report result as an attachment and specify the format of the attachment file.
     + To publish the report result to the Logi Report Server versioning system, select **Version System**. Then choose a format in which to send the report result.
     + To publish the report result to an FTP site, select **FTP**. Then specify the information for the FTP site and select a format in which to send the report result.
  6. Select **OK** to submit the task.

  When the task is finished, you can go to the My Tasks page in the Server Console to [view the scheduled report result](https://devnet.logianalytics.com/hc/en-us/articles/1500009749642-Viewing-Scheduled-Report-Results).
* **Showing/Hiding editing marks**  
  In Page Report Studio, you can use editing marks (dashed outlines of objects) for purposes such as aligning, moving, and resizing. By default, the editing marks are shown only when you create a new blank report in Page Report Studio. You can select **Menu** > **View** > **Editing Marks** to switch the status of the editing marks as required.
* **Showing/Hiding user information**  
   The User Information bar shows the current user name, catalog path and name, and report path and name. You can select **Menu** > **View** > **User Information Bar** to show or hide the bar.
* **Asking for help**  
   At any time, you can select **Menu** > **Help** > **User's Guide** to open the Page Report Studio user documentation. Furthermore, you can select the **Help** button in any dialog box to show the help about the dialog box. You can also use the Help menu to open the documentation and access Logi Report website for more information.
* **Exiting the report**  
   If you want to close the current report and release the resources, just select **Menu** > **File** > **Exit** (or the **Exit** button ![Exit button](https://devnet.logianalytics.com/hc/article_attachments/4404880262807/btn_pgrpt_exit.gif) which is always at the upper right corner of the Page Report Studio window, or the close button of the browser window). Closing the only report tab open will also prompt you whether to close the report. In case that you have modified the report without saving it, Page Report Studio will prompt you to [save the report](https://devnet.logianalytics.com/hc/en-us/articles/1500009777601-Saving-a-Page-Report).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777521-Editing-Page-Reports-in-Page-Report-Studio)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749042-Making-Simple-Modifications-to-Page-Report-Objects)
