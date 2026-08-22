---
title: "General Operations"
id: 1500009673961
section: "Page Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673961-General-Operations
updated_at: 2021-07-24T20:53:55Z
---

# General Operations

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673921-Editing-Page-Reports-in-Page-Report-Studio)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649442-Making-Simple-Modifications-to-Report-Objects)

# General Operations

When a page report is opened in Page Report Studio, you can do the following general operations:

* **Managing report tabs**  
   A page report can include one or more report tabs. The Go To drop-down list on the toolbar panel or the tabs across the top of the report list the display names of all the open report tabs in the current report. Selecting the display name of an inactive report tab will make it active. You can manage report tabs in a page report easily as follows:
  + **Opening and closing a report tab**  
     In a page report, a report tab can be shown or not. To close (hide) the active report tab, select **Menu** > **File** > **Close Report Tab** . If there are one or more report tabs open other than the active report tab, the close action will hide the active report tab; in the case that the active report tab is the only report tab open, the close action will prompt you whether or not to close the report.
  + To open (show) a hidden report tab, select **Menu** > **File** > **Open** or the **Open** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920357783/btn_open.gif) on the toolbar to display the Open Report Tabs dialog, in which the report tabs open in the current report are marked with a check symbol. Check the report tabs you want to open, uncheck the ones you want to close, and then select **OK**.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404926679703/opnrpt.gif)
  + **Renaming a report tab**  
     To rename a report tab, first activate it, then select **Menu** > **File** > **Rename Report Tab**. In the [Rename Report Tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009669921-Rename-Report-Tab) dialog, specify a new display name for the report tab.
  + **Deleting a report tab**   
     To delete a report tab, first activate it, then select **Menu** > **File** > **Delete Report Tab**. The only report tab open cannot be deleted.

    **Note:** A [Logi JReport Live license for Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009648262-Logi-JReport-Licenses#ServerLive) is required in order to delete report tabs. If you do not have the license, contact your Jinfonet Software account manager to obtain it.

  **Tip:** You can configure the [Page Report Studio profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009674101-Customizing-Page-Report-Studio-Profile#Switch) to enable switching report tabs using tabs. With report tabs you can easily activate a report tab in a report by selecting the tab representing the report tab on the report tab bar, and closing, renaming and deleting a report tab can also be accomplished by right-clicking the report tab and choosing the corresponding command from the shortcut menu.
* **Turning the report pages**  
   If a report tab includes more than one page, to turn between the report pages, you can:
  + Select the **First Page** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920441879/btn_firstpg.gif), **Previous Topic** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920442263/btn_prevpg.gif), **Next Topic** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920442647/btn_nxtpg.gif), or **Last Page** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926669463/btn_lastpg.gif) on the View toolbar.
  + Input a number into the page box ![](https://devnet.logianalytics.com/hc/article_attachments/4404926668951/btn_pgrpt_pageno.gif) and press **Enter** to go to that page.
  + Select **Menu** > **View** > **Turn To** and then select the corresponding command on the submenu. When the Page command is selected, the [Turn to Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009645902-Turn-to-Page) dialog appears for you to input the page number.
  + Use the scrollbar or mouse wheel to scroll up/down the report tab.
* **Navigating through the report data**You can use the TOC Browser to navigate through a report tab. To show the TOC Browser, select **Menu** > **View** > **TOC Browser**.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404926679959/pgrpt_edit_genrl_toc.gif)

  In the TOC Browser, expand the Report node, select a component or a node with the group value that you want to browse to. The page that contains the component or the matching data will then be shown.

  The table of contents on the TOC Browser is organized into a tree structure. The root node represents the report tab that you are currently viewing. The component names indicate components in the report tab. The group values show hierarchical groups.

  For report tabs designed in Logi JReport Designer, the nodes displayed on their TOC tree as well as the format of the TOC tree can be customized. For details, refer to "Showing Components in a TOC Tree" in the *Logi JReport Designer User's Guide*.
* **Refreshing the report result**  
   To fetch the data of the current report again, you can select **Menu** > **View** > **Refresh**.
* **Switching the report data mode** 
  . If you are making a lot of changes to the report, it may be faster to limit the number of records to 1 page while you make the changes and then change it back to full data mode to view the final result.  
  When the[Partial Report Result](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#Partial) feature is enabled in the server profile, you can switch the report data mode to view full data or only a specified number of data in a report. To show a certain number of data, select**Partial Data**from the data mode drop-down list on the toolbar and set a positive integer in the text box that follows, then press**Enter**or select outside the text box. By default, the number is 5000, which means the first 5000 records will retrieved. To show all data records, select**Full Data**
* **Applying a style**  
   A style can be applied to a report in order to change its appearance and characteristics. You can create and set up your own styles in Logi JReport Designer. When you publish your reports to Logi JReport Server, you can include these custom styles with the published reports. When you run a report, the style feature will be enabled and you can select a style to apply to the report.
  + **Applying a style to a report**  
     To apply a style to a report, make sure nothing is selected in the report, then select **Menu** > **Report** > **Style** and select the required one from the submenu, or select the required style from the style drop-down list ![](https://devnet.logianalytics.com/hc/article_attachments/4404920436119/btn_pgrpt_style.gif) on the toolbar. When a style is applied to the whole report, all components in the report will take a uniform appearance.
  + **Applying a style to a data component**  
     The data component (banded objects, crosstabs, charts, and tables) in a report can take a different style of its own. To apply a style to a data component, select it and then select **Menu** > **Report** > **Style** and select the required one from the submenu, or select the required style from the style drop-down list ![](https://devnet.logianalytics.com/hc/article_attachments/4404920436119/btn_pgrpt_style.gif) on the toolbar, or right-click the component and select **Apply Style** from the shortcut menu to select the required style in the [Apply Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009644922-Apply-Style) dialog. If the data component is contained in a banded object (for a chart, in a table also), you can also select the Inherit Style option to make it inherit the style of its parent data component.

  However, if there is only one style available to the report, this style will be applied to the report by default, in which case, you will find that all these style related commands are hidden.
* **Changing the report parameter values**   
   If there are parameters in the current report, you can change the parameter values at runtime. To do this, select **Menu** > **Report** > **Change Parameters**, then in the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009669621-Enter-Parameter-Values) dialog, specify the value for each parameter and select **OK** to run the report with the specified parameter values.

  You can also use parameter web controls to dynamically change the parameter values of a report at runtime. For details, see [Applying Web Controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009674041-Applying-Web-Controls).
* **Opening links**  
   When a page report is developed with links in Logi JReport Designer, which refer to locations specified by URLs, e-mail addresses or other reports, you can select the links' trigger objects in Page Report Studio to open the links. However, if the select priority of the link action is not specified to be the highest at report design time, you have to right-click on the trigger objects and select the corresponding link item on the shortcut menu to open the links. For example, if a trigger object is linked with a detail report, you need to right-click the object and select Detail Report from the shortcut menu to open the detail report. Meanwhile, when opening the detail report, you may be prompted with the [Encoding](https://devnet.logianalytics.com/hc/en-us/articles/1500009669601-Encoding) dialog, asking you to provide encoding and DB security information before the report result is produced. Select OK in the dialog if you want to run a detail report using the same encoding and DB security settings as that of the master report.

  After opening a linked report, you can select the Back ![](https://devnet.logianalytics.com/hc/article_attachments/4404920386327/btn_back.gif) or Next ![](https://devnet.logianalytics.com/hc/article_attachments/4404920446871/btn_next.gif) button on the toolbar to return back to the previous report or go forward to the next report, or select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920386711/btn_goto.gif) and select an item from the drop-down list to switch to that report directly. When opening a detail report, if the detail report is opened in the current window, a "link path", which tracks the linking action will be displayed in the Go To drop-down list if the list is available. Selecting the item in the list will switch to the corresponding report.
* **Setting Page Report Studio options**  
   Page Report Studio allows you to set the skin and customize toolbars. To do this:
  1. Select **Menu** > **View** > **Options**, or right-click anywhere on the toolbar area and select **Options** from the shortcut menu to open the [Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009669881-Options) dialog.
  2. In the Option tab, set the skin of Page Report Studio user interface.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920463767/optn_optn.gif)
  3. In the Customize tab,

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920464023/optn_cstmz.gif)

     + To modify a toolbar, select it in the Current Toolbar box, remove those unnecessary items from the Selected Tools box, and add required tools from the Available Tools box. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif) to adjust the order of the tools on the toolbar.
     + To add a toolbar, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) to show the New Toolbar Name dialog, then specify the toolbar name, select **OK** to return to the Options dialog, and set the tools for the new toolbar.
     + To delete a toolbar, select it and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif).
  4. To load the default settings, including the skin, and the three built-in toolbars, namely Standard, View, and Analysis, select the **Restore Defaults** button.
  5. Select **OK** to apply the settings.

  **Tip:** To close a toolbar, right-click anywhere on the toolbar area, then on the shortcut menu, select the item corresponding to the toolbar name. You can also do this to open an invisible toolbar, such as a newly-created one. The open/close toolbar operation can also be achieved by selecting the corresponding item on the Toolbar submenu of the View menu.
* **Tuning report page magnification**  
   You can zoom in or out the report page by selecting a magnification from the Zoom list ![](https://devnet.logianalytics.com/hc/article_attachments/4404920435479/btn_pgrpt_zoom.gif) on the View toolbar. You can also select **Menu** > **View** > **Zoom** to show the [Zoom](https://devnet.logianalytics.com/hc/en-us/articles/1500009670181-Zoom) dialog, and then specify the magnification.
* **Setting up the report page**
  1. Select **Menu** > **File** > **Page Setup**. The [Page Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009645562-Page-Properties) dialog appears.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920464279/pgprpty_gnrl.gif)
  2. In the General tab, specify the page size, orientation, and margins of the report page. You can check the **Auto Fit** option to calculate the page width/height according to the width/height of the contents within the page dynamically, which is useful when the width/height of the contents is unpredictable.
  3. In the Export tab, specify the page properties for the exported result of the report tab, which will be applied when [advanced running](https://devnet.logianalytics.com/hc/en-us/articles/1500009674661-Running-Reports) and [scheduling to run](https://devnet.logianalytics.com/hc/en-us/articles/1500009649902-Scheduling-Tasks-to-Publish-Reports) the report tab on Logi JReport Server as well as [exporting the report tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009649382-Exporting-the-Report-Result)  in Page Report Studio.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404926680215/pgprpty_export.gif)

     By default, the page properties defined for the report tab in the General tab of the dialog will be applied to the exported result of all export formats. You can define the page properties for each exported result by selecting a format from the Type drop-down list, unchecking the **Auto** option and then defining the properties as you want.
  4. Select **OK** to accept the changes and close the dialog
* **Adding/Removing page breaks**  
   A new page will be generated in a report tab only when the space in a page has been fully occupied or there exists a break control in this page, for example, a page break that is inserted in the page.

  To insert a page break, select **Menu** > **Insert** > **Page Break**, then select the mouse button on the destination where you want the page break to be inserted.

  To remove a page break, right-click on the report body, then on the shortcut menu, select **Remove Page Breaks** and then the corresponding page break from the submenu.

  **Notes:**

  + Page breaks can be inserted into the report body level.
  + Page breaks can be inserted into banded objects only when the following conditions have been met:
    - The parent of the banded object is the report body.
    - There isn't any existing page panel in the report body.
    - Its Position property of the banded object is set to static.
* **Undoing/Redoing actions**  
   You can undo or redo some actions by selecting **Menu** > **Edit** > **Undo** or **Redo** (or the **Undo** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920359447/btn_undo.gif) or **Redo** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926629015/btn_redo.gif) on the toolbar).
* **Showing/Hiding user information**  
   The User Information bar shows the current user name, catalog path and name, and report path and name. You can select **Menu** > **View** > **User Information Bar** to show or hide the bar.
* **Showing/Hiding editing marks**  
   In Page Report Studio, you can use editing marks (dashed outlines of objects) for purposes such as aligning, moving and resizing. By default, the editing marks are shown only when you create a new blank report in Page Report Studio. You can select **Menu** > **View** > **Editing Marks** to switch the status of the editing marks as required.
* **Asking for help**  
   At any time, you can select **Menu** > **Help** > **User's Guide** to open the index page of Page Report Studio User's Guide. Furthermore, you can select the **Help** button in any dialog to show the help about the dialog. You can also use the Help menu to open the User's Guide and access Jinfonet Software website for more information.
* **Exiting the report**  
   If you want to close the current report and release the resources, just select **Menu** > **File** > **Exit** (or the **Exit** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920464535/btn_pgrpt_exit.gif) which is always on the upper right corner of the Page Report Studio window, or the close button of the browser window). Closing the only report tab open will also prompt you whether or not to close the report. In case that you have modified the report without saving it, Page Report Studio will prompt you to [save the report](https://devnet.logianalytics.com/hc/en-us/articles/1500009673981-Saving-the-Report).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673921-Editing-Page-Reports-in-Page-Report-Studio)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649442-Making-Simple-Modifications-to-Report-Objects)
