---
title: "Running Reports"
id: 5741439314455
section: "Running and Scheduling Reports Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741439314455-Running-Reports
updated_at: 2022-10-31T17:18:19Z
---

# Running Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741475379735-Running-and-Scheduling-Reports-Logi-Report-Server-v19)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741483442455-Scheduling-Reports)

# Running Reports

This topic describes how you can run reports directly, in Advanced mode, and in background mode.

If you know the default format for viewing reports and this format is what you expect, see [Running Reports Directly](#Direct). If you would like a different view format or to customize some other information such as the running priority, how to save the report, and the expiration time, use [Running Reports in Advanced Mode](#Advanced).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) To run reports in public folders in the server resource tree, you must have the Execute and/or Edit permissions on the reports, and the Visible/Read permissions on the catalogs that the reports use. For more information about permissions, see [Managing Permissions](https://devnet.logianalytics.com/hc/en-us/articles/5741463668119-Managing-Permissions).

This topic contains the following sections:

* [Running Reports Directly](#Direct)
* [Running Reports in Advanced Mode](#Advanced)
* [Running Web Reports Using Default Bookmark](#Bookmark)
* [Running Page Reports in Background Mode](#Background)

## Running Reports Directly

Direct running reports is to use the default format setting to view the report.

If the reports are created on Server, the default format is controlled by the [Default Format for Viewing Report](https://devnet.logianalytics.com/hc/en-us/articles/5741409420567-Configuring-Server-Profile#Format) option in the server profile. By default, this option is set to Web/Page Studio, which means that page reports (.cls) are opened in [Page Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/5741462429975-Page-Report-Studio-Server-v19) and web reports (.wls) in [Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/5741464180119-Web-Report-Studio-Server-v19).

If the reports are edited using Designer, the default format is controlled by the Default Format for Viewing Report property in the Report Inspector. If this property is set to <Server Setting>, the viewing format will be determined by the preceding setting on server. For page reports this property is available to each report tab in the reports, therefore when a page report contains multiple report tabs and these report tabs have different default format settings, for example, report tab 1 is Page Report, tab 2 HTML and tab 3 Excel, there will be different direct running results, depending on which report tab is the last-time focused tab in the page report when the page report is saved at report design time. If it is report tab 1, all the three tabs in the page report will be opened in Page Report Studio. If it is report tab 2 or 3, only tab 2 or 3 will be displayed in the specified format, and this applies to all the other formats except Page Report.

You can run a report directly from the server resource tree on the Server Console by taking any of the following ways:

* **Selecting the report name**  
   To use this way to run a report saved in the Public Report folder, you need to have the Execute permission on the report so that the report name can be shown with hyperlink when you move the mouse pointer on the report row.

  Selecting the report name runs the report in the default format (if the report contains parameters, you need to [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/5741454720023-Specifying-Parameter-Values)). When the default format for viewing report is Web/Page Studio, which studio mode will be applied to run the report is decided by the [Default View for Page Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/5741409420567-Configuring-Server-Profile#PageMode)/[Default Mode for Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/5741409420567-Configuring-Server-Profile#WebMode) option in the server profile. However, if the default view/mode is Interactive View/Edit Mode but you do not have the Edit permission on the report, you will fail to run the report and instead get an error message.
* **Using the Run option**  
   To use this way to run a report saved in the Public Report folder, you need to have the Execute permission on the report so that the Run option can be available.

  Do any of the following:

  + Put the mouse pointer over the report row and select the  **Run** button ![Run button](https://devnet.logianalytics.com/hc/article_attachments/9905658476183/btn_srv_run.gif) on the floating toolbar.
  + Select the report row, right-click in the report row, and then select **Run** from the shortcut menu.
  + Select the report row and select **Run** > **Run** on the task bar of the Resources page.

  If the report contains parameters, Server will prompt you to specify the parameter values. Then, Server displays the report in the default format. When the default format for viewing report is Web/Page Studio, Server will open the report in the View Mode of Web Report Studio or Basic View of Page Report Studio.

  You can also use the Run option to run multiple reports at a time. To do this, select the required reports and select **Run** > **Run** on the task bar or right-click in any report row and select **Run** from the shortcut menu. If the selected reports contain parameters, the parameter dialog box for each report will appear for you to specify the parameter values. After that, Server displays the reports one by one in the default format.
* **Using the Edit option**  
   To use this way to run a report saved in the Public Report folder, you need to have the Edit permission on the report so that the Edit option can be available. For a [shared report](https://devnet.logianalytics.com/hc/en-us/articles/5741461964439-Sharing-Web-Reports), the Allow Edit property should also be enabled.

  Do any of the following:

  + Put the mouse pointer over the report row and select the  **Edit**  button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9905637127063/btn_srv_edit.gif) on the floating toolbar.
  + Select the report row, right-click in the report row, and then select **Edit** from the shortcut menu.
  + Select the report row and select **Run** > **Edit** on the task bar of the Resources page.

  If the report contains parameters, Server will prompt you to specify the parameter values. Then, Server displays the report in the default format. When the default format for viewing report is Web/Page Studio, Server will open the report in the Edit Mode of Web Report Studio or Interactive View of Page Report Studio.

## Running Reports in Advanced Mode

To run reports saved in a public folder in Advanced mode, you need to have the Execute permission on the reports.

1. In the server resource tree on the Server Console, browse to the report you want to run.
2. Do either of the following to open the [Advanced Run dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741420507799-Advanced-Run-Dialog-Box-Properties).
   * Put the mouse pointer over the report row and select the **Advanced Run** button ![Advanced Run button](https://devnet.logianalytics.com/hc/article_attachments/9905637152919/btn_srv_advrun.gif) on the floating toolbar.
   * Select the report row, right-click in the row and select **Advanced Run** from the shortcut menu.
   * Select the report row and click **Run** > **Advanced Run** on the task bar.
3. In the General tab,

   ![Advanced Run dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/9905659297303/advcdrn_gen.gif)

   1. For a page report, select the report tabs in the page report you want to run. The report tabs will run in the list order. You can change the order of the report tabs by selecting ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif). However, if you choose to run the page report in the Page Report format in the Format tab, the unselected report tabs will also be run.
   2. If there are multiple [dynamic connections](https://devnet.logianalytics.com/hc/en-us/articles/5741395796375-Creating-and-Using-Dynamic-Connections) available, expand the **Select Dynamic Connection** section and select a connection from the drop-down list. You can select **Connection Properties** to view the connection information.
   3. Expand **Report Information**, you can select **Select Another Catalog** to specify another catalog for the report, and then select the report version and catalog version from the corresponding drop-down lists (the catalog and report/catalog version cannot be changed if the report is a [shared report](https://devnet.logianalytics.com/hc/en-us/articles/5741461964439-Sharing-Web-Reports)).
   4. Assign a priority to the task from the Priority drop-down list. The Priority property is available to administrators only and the priority levels are from 1 to 10 in ascending order of lowest priority to highest priority (by default this property is ignored unless server.properties is modified to set queue.policy not equal to 0).
4. In the Parameter tab, [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/5741454720023-Specifying-Parameter-Values) if the report has parameters.
5. In the Format tab,

   ![Advanced Run dialog - Format tab](https://devnet.logianalytics.com/hc/article_attachments/9905659328407/advcdrn_fmt.gif)

   1. Choose a format to view the report and set the [properties](https://devnet.logianalytics.com/hc/en-us/articles/5741420507799-Advanced-Run-Dialog-Box-Properties#Format) of the format. When you select HTML, you can localize the names of page navigation links in the HTML outputs such as First, Previous, Next, and Last. For more information, see [Localizing Page Navigation Links in HTML Report Outputs](https://devnet.logianalytics.com/hc/en-us/articles/5741482629911-NLS-at-Report-Level#Link).
   2. Expand **Advanced**.
   3. Specify the style group for the report.
   4. Select **Enable Converting Encoding** and specify the encoding before and after converting from the corresponding drop-down lists.
   5. If the report is defined with NLS, select **Enable NLS**, then specify a language in which you want to display the report contents.
   6. Define the encoding for the report by selecting from the Encoding drop-down list.
   7. Specify the DB user and password with which to connect with the data source. You can either use the default ones defined in the catalog or specify another DB user and password.
   8. Server will automatically use the default on-screen filter values that you have saved in the report to run the report. If you do not want to apply the filter conditions, clear **Use User Defined Default On-screen Filter Values**.
   9. When you have created bookmarks for the web report, select a bookmark from the **Use Bookmark** drop-down list to run the bookmark of the web report.
   10. When you have selected any format other than Page Report or Web Report, select **Add TaskListener to be Invoked** to call a Java application before/after Server runs the report to obtain information about the report task. For more information, see [Applying TaskListener](https://devnet.logianalytics.com/hc/en-us/articles/5741395089175-Applying-TaskListener).
6. In the Archive tab, select **Auto Archive Properties**, then specify [where you want to generate the report result version](https://devnet.logianalytics.com/hc/en-us/articles/5741462158487-Creating-Versions#Result) and the [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/5741482308887-Applying-an-Archive-Policy).

   ![Advanced Run dialog - Archive tab](https://devnet.logianalytics.com/hc/article_attachments/9905659351191/advcdrn_archv.gif)
7. If the Duration tab is available, specify a time duration for the task, and ask Server to cancel the task or to notify you or someone else of the task status via email if the task has not yet finished running when the task duration is up. For more information, see [Task-level Timeout for Advanced Run and Schedule Tasks](https://devnet.logianalytics.com/hc/en-us/articles/5741438263319-Managing-Report-Running-Tasks#Timeout).
8. Select **Finish** to run the report.

## Running Web Reports Using Default Bookmark

After you [create bookmarks for a web report and set the default bookmark in Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/7985371637143-Bookmarking-a-Web-Report), Server displays the web report with the default bookmark when you [run the web report directly](#Direct) in Web Report Studio.

When you advanced run or schedule to run a web report, you can use the **Use Bookmark** property to specify a bookmark of the web report that you want to run.

When you [run a web report via URL](https://devnet.logianalytics.com/hc/en-us/articles/5741456438167-Running-Reports-via-URL), you can use the property [jrs.bookmark](https://devnet.logianalytics.com/hc/en-us/articles/5741464843927-URL-Properties-for-Running-Scheduling-and-Viewing-Reports-via-URL#jrs.bookmark) or [bookmark (for JSON)](https://devnet.logianalytics.com/hc/en-us/articles/5741456438167-Running-Reports-via-URL#JSON) to specify a bookmark of the web report that you want to run.

You can also update and remove bookmarks and set the default bookmark for a web report on the Server Console. To do this:

1. Do any of the following:
   * Put the mouse pointer over the report row and select the **Bookmark** button ![Save Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/9905574662167/btn_wbrpt_bkmkst.gif) on the floating toolbar.
   * Select the report row, right-click in the report row, and then select **Bookmark** from the shortcut menu.
   * Select the report row and select **Tools** > **Bookmark** on the task bar.

   Server displays the Bookmark dialog box.
2. Server lists all the bookmarks that you have created for the web report. To view or update a bookmark, select **Details**,view the bookmark information or update the name or description of the bookmark, and then select **OK**.
3. To set a bookmark as the default bookmark for the report, select the bookmark, and then select **Set as Default**.
4. To remove a bookmark, select it, and then select **Delete**.
5. Select the close button at top right to close the dialog box.

## Running Page Reports in Background Mode

When you run a page report in Page Report Studio, if the report contains a large amount of data, you need to wait several minutes before the report comes out, and during this period you should make sure the report processing page is not closed. This may bring you some inconvenience, therefore Logi Report provides you the Background and Cancel options on the report processing bar to enable you switch the report to run in background mode or cancel it from running.

By setting [Background Mode Timeout](https://devnet.logianalytics.com/hc/en-us/articles/5741427459479-Page-Report-Studio-Profile-Properties#Background) in the Page Report Studio profile, you can also make page reports run automatically in the background mode after a specified period. Then, when it runs a report in Page Report Studio and has not generated it after the specified time, Server will automatically run the report in the background mode.

When it completes running a page report in the background, Server will list the page report in the [Background Tasks table](https://devnet.logianalytics.com/hc/en-us/articles/5741438263319-Managing-Report-Running-Tasks#Background) of the My Tasks page. You can open the report by selecting **Page Report** in the table.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* When you select a report name, the Run option, or the Edit option more than once within 5 seconds to run a report directly, Server displays a message asking whether you want to run the report only once or multiple times. This is to avoid unwanted submitting of running the same report repeatedly.
* When running a page report containing both normal and [bursting report tabs](https://devnet.logianalytics.com/hc/en-us/articles/5741463244055-Scheduling-Bursting-Reports):
  + **For direct running**  
     When running it in the Page Report format, Server only opens the normal report tabs.

    When running it in other formats, if the last-time focused report tab is a normal report, Server opens it directly; if the last-time focused report tab is a bursting report which cannot run, Server displays a warning message asking you to select a normal report tab to run using advanced run.
  + **For advanced running**  
     You can only choose the normal report tabs to run.
* To be able to run page reports in background mode, you need to select [Enable Background Task for Reports](https://devnet.logianalytics.com/hc/en-us/articles/5741409420567-Configuring-Server-Profile#BackgroundTask) in the server profile.
* When you run reports for the first time after you installed Server, Server might display an error message as follows. It is probably because there are no fonts installed on your computer. To solve this problem, try installing default fonts on your computer.

  ```
  java.lang.InternalError: java.lang.reflect.InvocationTargetException  
  at java.desktop/sun.font.FontManagerFactory$1.run(FontManagerFactory.java:86)  
  at java.base/java.security.AccessController.doPrivileged(Native Method)
  ```

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741475379735-Running-and-Scheduling-Reports-Logi-Report-Server-v19)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741483442455-Scheduling-Reports)
