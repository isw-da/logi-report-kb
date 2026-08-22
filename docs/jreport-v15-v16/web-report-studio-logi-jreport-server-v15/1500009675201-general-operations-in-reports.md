---
title: "General Operations in Reports"
id: 1500009675201
section: "Web Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009675201-General-Operations-in-Reports
updated_at: 2021-07-24T20:53:36Z
---

# General Operations in Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675161-Editing-Web-Reports-in-Web-Report-Studio)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675221-Inserting-Components)

# General Operations in Reports

You can perform the following general operations in Web Report Studio:

* **Opening another web report**  
   Select **Menu** > **File** > **Open** or the **Open** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920357783/btn_open.gif) on the toolbar to display the [Select a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009647802-Select-a-Report) dialog, in which the web reports in the same folder as the current open report are listed. Select the web report you want to open from the default folder or from another folder, and then select **OK**.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404926648471/slctrpt.gif)
* **Undoing/Redoing actions**  
   You can undo or redo some actions. To do this, select **Menu** > **Edit** > **Undo** or **Redo** (or the **Undo** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920359447/btn_undo.gif) or **Redo** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926629015/btn_redo.gif) on the toolbar).
* **Turning component pages**  
   When a table or a crosstab contains more than one page, a navigation bar specific for the component will be available right below the component. You can use the navigation bar to view the desired pages: select the corresponding button to go to the first page, the previous page, the next page, or the last page, or input a number in the text box to go to that page.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404926648727/wbrpt_edt_genrl_cmpntpg.gif)
* **Showing/Hiding editing marks**  
   You can use editing marks (dashed outlines of objects) for purposes such as aligning, moving and resizing. The editing marks are shown by default. To switch the status of the editing marks, select **Menu** > **View** > **Editing Marks**.
* **Switching the report data mode** 
  . If you are making a lot of changes to the report, it may be faster to limit the number of records to 1 page while you make the changes and then change it back to full data mode to view the final result.  
  When the[Partial Report Result](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#Partial) feature is enabled in the server profile, you can switch the report data mode to view full data or only a specified number of data in a report. To show a certain number of data, select**Partial Data**from the data mode drop-down list on the toolbar and set a positive integer in the text box that follows, then press**Enter**or select outside the text box. By default, the number is 5000, which means the first 5000 records will retrieved. To show all data records, select**Full Data**

* **Setting up the report page**
  1. Select **Menu** > **File** > **Page Setup**. The [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009672341-Page-Setup#Studio) dialog appears.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920396823/pgstup_gnrl_studio_476x355.gif)
  2. In the General tab, select the page type: Web Report or Print Report, which determines the unit of the page size, pixel or inch, then specify the size, orientation and margins of the report page. You can check the **Auto Fit** option to calculate the page width/height according to the width/height of the contents within the page dynamically, which is useful when the width/height of the contents is unpredictable.
  3. In the Export tab, specify the page properties for the exported result of the report, which will be applied when [advanced running](https://devnet.logianalytics.com/hc/en-us/articles/1500009674661-Running-Reports) and [scheduling to run](https://devnet.logianalytics.com/hc/en-us/articles/1500009649902-Scheduling-Tasks-to-Publish-Reports) the report on Logi JReport Server as well as [exporting the report](https://devnet.logianalytics.com/hc/en-us/articles/1500009650262-Exporting-Printing-the-Report-Result) in Web Report Studio.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920397207/pgstup_export_476x354.gif)

     By default, the page properties defined for the report in the General tab of the dialog will be applied to the exported result of all export formats. You can define the page properties for each exported result by selecting a format from the Type drop-down list, unchecking the **Auto** option and then defining the properties as you want.
  4. Select **OK** to accept the changes and close the dialog.
* **Automatically scaling report components according to browser window**When Web Report Studio is in [View Mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009675101-Web-Report-Studio#Mode), it can be responsive to any size of browsers on any mobile devices or computers. Report components excluding the report header and footer can automatically scale and fold according to the current browser window size. Information presented will always be legible and the layout will perfectly adapt to best utilize the available display screen. This is called responsive view. It is always available to mobile devices. When Web Report Studio runs on computers, you can specify whether to apply repsonsive view by default by setting the profile option [View Web Reports in Responsive Mode,](https://devnet.logianalytics.com/hc/en-us/articles/1500009675361-Customizing-Web-Report-Studio-Profile#View) and open or close it in Web Report Studio as follows:
  1. Select the **Customize Buttons** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920397463/btn_wbrpt_cstmz.gif) on the toolbar and select **Open Responsive Mode** or **Close Responsive Mode** from the menu list.

     The Open Responsive Mode button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920360215/btn_rspnsvopn.gif) or Close Responsive Mode button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920360599/btn_rspnsvcls.gif) is then available on the toolbar.
  2. Select the button on the toolbar to open or close responsive view.
* **Asking for help**  
   At any time, you can select **Menu** > **Help** > **User's Guide** to open the index page of the Web Report Studio User's Guide. Furthermore, you can select the Help button in any dialog to show the help document about the dialog. You can also use the Help menu to access Jinfonet Software website for more information.
* **Exiting Web Report Studio**  
   If you want to close the current web report and release the resources, just select **Menu** > **File** > **Exit** (or the button **X** on the far right of the toolbar). Do not use the close button on the browser window as that may not release the resources used by the report.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675161-Editing-Web-Reports-in-Web-Report-Studio)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675221-Inserting-Components)
