---
title: "General Operations in a Report"
id: 1500009719161
section: "Editing Web Reports in Web Report Studio"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009719161-General-Operations-in-a-Report
updated_at: 2021-11-03T06:56:28Z
---

# General Operations in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719081-Editing-Web-Reports-in-Web-Report-Studio)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009719181-Inserting-Components)

# General Operations in a Report

You can perform the following general operations in Web Report Studio:

* **Opening another web report**  
   Select **Menu** > **File** > **Open** or the **Open** button ![Open button](https://devnet.logianalytics.com/hc/article_attachments/4412139483415/btn_open.gif) on the toolbar to display the [Select a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009690682-Select-a-Report) dialog, in which the web reports in the same folder as the current open report are listed. Select the web report you want to open from the default folder or from another folder, and then select **OK**.

  ![Select a Report dialog](https://devnet.logianalytics.com/hc/article_attachments/4412139507607/slctrpt.gif)
* **Undoing/Redoing actions**  
   You can undo or redo some actions. To do this, select **Menu** > **Edit** > **Undo** or **Redo** (or the **Undo** button ![Undo button](https://devnet.logianalytics.com/hc/article_attachments/4412139484183/btn_undo.gif) or **Redo** button ![Redo button](https://devnet.logianalytics.com/hc/article_attachments/4412139484439/btn_redo.gif) on the toolbar).
* **Turning component pages**  
   When a table or a crosstab contains more than one page, a navigation bar specific for the component will be available right below the component. You can use the navigation bar to view the desired pages: select the corresponding button to go to the first page, the previous page, the next page, or the last page, or input a number in the text box to go to that page.

  ![Turn Component Page](https://devnet.logianalytics.com/hc/article_attachments/4412112511383/wbrpt_edt_genrl_cmpntpg.gif)
* **Showing/Hiding editing marks**  
   You can use editing marks (dashed outlines of objects) for purposes such as aligning, moving and resizing. The editing marks are shown by default. To switch the status of the editing marks, select **Menu** > **View** > **Editing Marks**.
* **Switching the report data mode** 
  . If you are making a lot of changes to the report, it may be faster to limit the number of records to 1 page while you make the changes and then change it back to full data mode to view the final result.  
  When the[Partial Report Result](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#Partial) feature is enabled in the server profile, you can switch the report data mode to view full data or only a specified number of data in a report. To show a certain number of data, select**Partial Data**from the data mode drop-down list on the toolbar and set a positive integer in the text box that follows, then press**Enter**or select outside the text box. By default, the number is 5000, which means the first 5000 records will retrieved. To show all data records, select**Full Data**

* **Setting up the report page**
  1. Select **Menu** > **File** > **Page Setup**. The [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009716761-Page-Setup#Studio) dialog appears.

     ![Page Setup dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4412139507863/pgstup_gnrl_prnt.gif)
  2. In the General tab, select the page type: Web Report or Print Report, which determines the unit of the page size, pixel or inch, then specify the size, orientation and margins of the report page. You can check the **Auto Fit** option to calculate the page width/height according to the width/height of the contents within the page dynamically, which is useful when the width/height of the contents is unpredictable.
  3. In the Export tab, specify the page properties for the exported result of the report, which will be applied when [advanced running](https://devnet.logianalytics.com/hc/en-us/articles/1500009692462-Running-Reports) and [scheduling to run](https://devnet.logianalytics.com/hc/en-us/articles/1500009692502-Scheduling-Tasks-to-Publish-Reports) the report on Logi JReport Server as well as [exporting the report](https://devnet.logianalytics.com/hc/en-us/articles/1500009692782-Exporting-Printing-the-Report-Result) in Web Report Studio.

     ![Page Setup dialog - Export tab](https://devnet.logianalytics.com/hc/article_attachments/4412131397143/pgstup_export.gif)

     By default, the page properties defined for the report in the General tab of the dialog will be applied to the exported result of all export formats. You can define the page properties for each exported result by selecting a format from the Type drop-down list, unchecking the **Auto** option and then defining the properties as you want.
  4. Select **OK** to accept the changes and close the dialog.
* **Automatically scaling report components according to browser window**When Web Report Studio is in [View Mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009719001-Web-Report-Studio#Mode), it can be responsive to any size of browsers on any mobile devices or computers. Report components excluding the report header and footer can automatically scale and fold according to the current browser window size. Information presented will always be legible and the layout will perfectly adapt to best utilize the available display screen. This is called responsive view. It is always available to mobile devices. When Web Report Studio runs on computers, you can specify whether to apply repsonsive view by default by setting the profile option [View Web Reports in Responsive Mode,](https://devnet.logianalytics.com/hc/en-us/articles/1500009719321-Customizing-Web-Report-Studio-Profile#View) and open or close it in Web Report Studio as follows:
  1. Select the **Customize Buttons** button ![Customize Buttons button](https://devnet.logianalytics.com/hc/article_attachments/4412139508631/btn_wbrpt_cstmz.gif) on the toolbar and select **Open Responsive Mode** or **Close Responsive Mode** from the menu list.

     The Open Responsive Mode button ![Open Responsive Mode button](https://devnet.logianalytics.com/hc/article_attachments/4412112483735/btn_rspnsvopn.gif) or Close Responsive Mode button ![Close Responsive Mode button](https://devnet.logianalytics.com/hc/article_attachments/4412139485079/btn_rspnsvcls.gif) is then available on the toolbar.
  2. Select the button on the toolbar to open or close responsive view.
* **Scheduling report tasks**  
   If the [Quick Schedule from Web/Page Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#Schedule) option is enabled in the server profile, you can schedule tasks to publish web reports to e-mails, FTP sites, or the Logi JReport Server versioning system in Web Report Studio. However the Quick Schedule feature inside Web Report Studio does not provide the full functionalities. If you want to use the full schedule system of Logi JReport Server, go to the [server console to submit the schedule tasks](https://devnet.logianalytics.com/hc/en-us/articles/1500009692482-Scheduling-Reports).
  1. Make sure you are in View Mode of Web Report Studio.
  2. Select the **Quick Schedule** button ![Quick Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4412139508887/btn_schdl.gif) on the toolbar and the [Quick Schedule](https://devnet.logianalytics.com/hc/en-us/articles/1500009716821-Quick-Schedule) dialog is displayed.

     ![Quick Schedule dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112513047/qckschdl.gif)

     If the current open report has not been saved, you will be prompted to save the report.
  3. Specify the name for the task in the Schedule Name text box.
  4. From the Time Type drop-down list specify the time for when the task is to be performed.
     + To perform the task as soon as you submit it, select **Immediately**.
     + If you want to run the task repeatedly, select  **Periodically**, then specify to run it daily, weekly or monthly at a specific time of a day.
  5. From the Publish To drop-down list, select where to publish the report result and specify the settings of the publish type.
     + To publish the report result to e-mail, select **E-mail**. Then specify the e-mail information such as addresses, subject and comments respectively; if you want to send the report result in the mail body, check **E-mail Result in** and select a format for the result: HTML or Text (when HTML is selected the comments you input for the e-mail will be overwritten by the report result; if Text is selected the comments will be positioned in front of the report result); check **Attachment in** to send the report result as an attachment and specify the format of the attachment file.
     + To publish the report result to the Logi JReport Server versioning system, select **Version System**. Then choose a format in which to send the report result.
     + To publish the report result to an FTP site, select **FTP**. Then specify the information for the FTP site and select a format in which to send the report result.
  6. Select **OK** to submit the task.

  When the task is finished, you can go to the My Tasks page in the server console to [view the scheduled report result](https://devnet.logianalytics.com/hc/en-us/articles/1500009718741-Viewing-Scheduled-Report-Results).
* **Sharing a web report**  
   If the current web report is not a shared report and you are the owner of the report, you can use the Share Report feature to share it to others. To share a web report, make sure you have already [saved it](https://devnet.logianalytics.com/hc/en-us/articles/1500009719241-Saving-the-Report), then select **Menu** > **File** > **Share** or select the **Share** button ![Share button](https://devnet.logianalytics.com/hc/article_attachments/4412112483223/btn_share.gif) on the toolbar. In the [Share Report dialog](https://devnet.logianalytics.com/hc/en-us/articles/1500009716901-Share-Report), set the options for sharing the report. For detailed information about sharing report, see [Sharing Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009717901-Sharing-Reports).

  **Note:** After all the components that reference a business view are removed from a shared report, the business view will not be available after the shared report is saved.
* **Viewing in-memory cube status**  
   If the [Show Status When Using Cube Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile#CubeStatus) option is enabled in the server profile, you will find the Cube Status button ![Cube Status button](https://devnet.logianalytics.com/hc/article_attachments/4412139509399/btn_cbstts.gif) on the toolbar, by selecting which you can view the information about whether the data components in the current report apply [in-memory cubes](https://devnet.logianalytics.com/hc/en-us/articles/1500009691322-Managing-In-memory-Cubes) and the reasons if not in the [Cube Status](https://devnet.logianalytics.com/hc/en-us/articles/1500009715661-Cube-Status) dialog.
* **Asking for help**  
   At any time, you can select **Menu** > **Help** > **User's Guide** to open the index page of the Web Report Studio User's Guide. Furthermore, you can select the Help button in any dialog to show the help document about the dialog. You can also use the Help menu to access Logi JReport website for more information.
* **Exiting Web Report Studio**  
   To close the current web report and release the resources, select **Menu** > **File** > **Exit** (or the button **X** on the far right of the toolbar). Do not use the close button of the browser window as that may not release the resources used by the report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719081-Editing-Web-Reports-in-Web-Report-Studio)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009719181-Inserting-Components)
