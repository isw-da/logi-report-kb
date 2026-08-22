---
title: "Running Reports"
id: 1500009674661
section: "Running and Scheduling Reports Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009674661-Running-Reports
updated_at: 2021-12-13T03:45:39Z
---

# Running Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649862-Running-and-Scheduling-Reports)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674681-Scheduling-Reports)

# Running Reports

If you know the default format for viewing reports and this format is what you expect, use [direct running](#Direct). If you would like a different view format or to customize some other information such as the running priority, how to save the result, the expiration time and so on, use [advanced running](#Advanced).

**Note:** To run reports in public folders in the server resource tree, you must have the Execute and/or Edit permissions on the reports and the Visible and Read permissions on the catalogs that the reports use. For more information about permissions, see [Managing Permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009674981-Managing-Permissions).

Below is a list of the sections covered in this topic:

* [Running Reports Directly](#Direct)
* [Running Reports in Advanced Mode](#Advanced)
* [Running Page Reports in Background Mode](#Background)

## Running Reports Directly

Direct running reports is to use the default format setting to view the report result.

If the reports are created on Logi JReport Server, the default format is controlled by the [Default Format for Viewing Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#Format) option in the server profile. By default, this option is set to Report Studio, which means that page reports (.cls) are opened in [Page Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009649242-Page-Report-Studio) and web reports (.wls) in [Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009675101-Web-Report-Studio).

If the reports are edited using Logi JReport Designer, the default format is controlled by the Default Format for Viewing Report property in the Report Inspector. If this property is set to <Server Setting>, the viewing format will be determined by the above setting on server. For page reports this property is available to each report tab in the reports, therefore when a page report contains multiple report tabs and these report tabs have different default format settings, for example, report tab 1 is Page Report, tab 2 HTML and tab 3 Excel, there will be different direct running results, depending on which report tab is the last-time focused tab in the page report when the page report is saved at report design time. If it is report tab 1, all the three tabs in the page report will be opened in Page Report Studio. If it is report tab 2 or 3, only tab 2 or 3 will be displayed in the specified format, and this applies to all the other formats except Page Report.

You have the following ways to run a report directly:

* **Selecting the report name**  
  To use this way to run a report saved in the Public Report folder, you need to have the Execute permission on the report so that the report name can be shown with hyperlink when you move the mouse pointer on the report row.

  Selecting the report name runs the report in the default format (if the report contains parameters, you need to [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009649882-Specifying-Parameter-Values)). When the default format for viewing report is Report Studio, which studio mode will be applied to run the report is decided by the [Default View for Page Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#PageMode)/[Default Mode for Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#WebMode) option in the server profile. However if the default view/mode is Interactive View/Edit Mode but you do not have the Edit permission on the report, you will fail to run the report and instead get an error message.
* **Using the Run option**  
  To use this way to run a report saved in the Public Report folder, you need to have the Execute permission on the report so that the Run option can be available.

  Do any of the following:

  + Put the mouse pointer over the report row and select the  **Run** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920422807/btn_srv_run.gif) on the floating toolbar.
  + Select the report row, right-click in the report row and select **Run** from the shortcut menu.
  + Select the report row and select **Run** > **Run** on the task bar.

  If the report contains parameters, you will be prompted to specify the parameter values. Then the report will be displayed in the default format. When the default format for viewing report is Report Studio, page report will be opened in Basic View of Page Report Studio and web report in View Mode of Web Report Studio.

  You can also use the Run option to run multiple reports at a time. To do this, check the checkboxes ahead of the required reports and select **Run** > **Run** on the task bar or right-click in any report row and select **Run** from the shortcut menu. If the selected reports contain parameters, the parameter dialog for each report will appear for you to specify the parameter values. After that the reports will be displayed one by one in the default format.
* **Using the Edit option**  
  To use this way to run a report saved in the Public Report folder, you need to have the Edit permission on the report so that the Edit option can be available.

  Do any of the following:

  + Put the mouse pointer over the report row and select the  **Edit**  button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926643991/btn_srv_edit.gif) on the floating toolbar.
  + Select the report row, right-click in the report row and select **Edit** from the shortcut menu.
  + Select the report row and select **Run** > **Edit**  on the task bar.

  If the report contains parameters, you will be prompted to specify the parameter values. Then the report will be displayed in the default format. When the default format for viewing report is Report Studio, the report will be opened in Interactive View of Page Report Studio or Edit Mode of Web Report Studio.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Running Reports in Advanced Mode

To run reports saved in the Public Reports folder in Advanced mode, you need to have the Execute permission on the reports.

1. On the Logi JReport Console > Resources page, browse to the report you want to run.
2. Do either of the following to open the [Advanced Run](https://devnet.logianalytics.com/hc/en-us/articles/1500009670701-Advanced-Run) dialog.
   * Select the report row, then on the task bar of the Resources page, select **Run** > **Advanced Run**.
   * Select the report row, right-click in the row and select **Advanced Run** from the shortcut menu.
   * Put the mouse pointer over the report row and select the **Advanced Run** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920423319/btn_srv_advrun.gif) on the floating toolbar.
3. In the General tab,

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926664599/advcdrn_gen.gif)

   1. For a page report, select the report tabs in the page report you want to run. The report tabs will run in the list order. You can change the order of the report tabs by selecting ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif) and ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif).
   2. If there are multiple [dynamic connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009669041-Configuring-Dynamic-Connections) available, expand the **Select Dynamic Connection** section and select a connection from the drop-down list. Select **Connection Properties** to view the connection information if needed.
   3. Expand the **Report Information** section, select **Select Another Catalog** to specify another catalog for the report if required.

      Select the report version and catalog version from the corresponding drop-down lists.

      Assign a priority to the task from the Priority drop-down list. The Priority property is available to administrators only and the priority levels are from 1 to 10 in ascending order of lowest priority to highest priority (by default this property is ignored unless server.properties is modified to set queue.policy not equal to 0).
4. In the Parameter tab, [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009649882-Specifying-Parameter-Values) if the report has parameters.
5. In the Format tab,

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920429463/advcdrn_fmt.gif)

   1. Choose a format to view the report result and set the [properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009670701-Advanced-Run#Format) of the selected format. When HTML is selected, the names of page navigation links in the report such as First, Previous, Next, and Last can be localized according to your requirements. For details, refer to [Localizing Page Navigation Links in HTML Report Outputs](https://devnet.logianalytics.com/hc/en-us/articles/1500009649202-Localizing-Page-Navigation-Links-in-HTML-Report-Outputs).
   2. Expand the **Advanced** section.
   3. Specify the style group for the report.
   4. Check the **Enable Converting Encoding** option and specify the encoding before and after converting from the corresponding drop-down lists.
   5. If the report is defined with NLS, check **Enable NLS** then specify a language to display the report contents in.
   6. Define the encoding for the report by selecting from the Encoding drop-down list.
   7. Specify the DB user and password with which to connect with the data source. You can either use the default ones defined in the catalog or specify another DB user and password.
   8. The default on-screen filter values you have saved in the report will be automatically used to run the report. If you do not want to apply the filter conditions, uncheck **Use User-Defined Default On-screen Filter Values**.
   9. Check the **Add TaskListener to be Invoked** option to call a Java application when scheduling the report (for details, see [Adding TaskListener When Scheduling Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009668701-Adding-TaskListener-When-Scheduling-Reports)).
6. In the Archive tab, check the **Auto Archive Properties** checkbox, then specify [where to generate the report result version](https://devnet.logianalytics.com/hc/en-us/articles/1500009649002-Creating-Versions#Result) and the [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009673721-Applying-an-Archive-Policy).

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920429719/advcdrn_archv.gif)
7. If the Duration tab is available, specify a time duration for the task, and ask Logi JReport Server to cancel the task or to notify you or someone else of the task status via e-mail if the task has not yet finished running when the task duration is up. For detailed information, see [Task-level Timeout for Advanced Run and Schedule Tasks](https://devnet.logianalytics.com/hc/en-us/articles/1500009648962-Task-level-Timeout-for-Advanced-Run-and-Schedule-Tasks).
8. Select **Finish** to view the report in the format you specified.

   When running a page report in Page Report Studio, the report processing page will appear, on which you can choose to cancel the running of the report, or to make the report run in background mode. Select **Cancel** on this page if you decide to cancel, **Background** if you want the report to run in background mode, or just wait for processing to complete. If you cancel the report from running, you can choose whether to cancel the running query used by the report in the database at the same time by configuring the JdbcDriversConfig.properties file. For details, refer to [Canceling Running Query](https://devnet.logianalytics.com/hc/en-us/articles/1500009644462-Configuring-JdbcDriversConfig-properties#Cancel).

**Notes:**

* If you choose to view a page report in Page Report format, besides the selected report tab, all the other tabs in the report will also be run.
* When you run a report in Advanced mode in Applet format or in HTML format with Applet Chart is checked for it using Google Chrome, the report can run correctly only when NPAPI is enabled for the web browser. To do this, you need to type **chrome://flags/** in the address bar of the web browser, then scroll down and set Enable NPAPI Mac, Windows to **Enable**.
* When running a page report containing both normal and [bursting report tabs](https://devnet.logianalytics.com/hc/en-us/articles/1500009674701-Scheduling-a-Task-Containing-a-Bursting-Report):
  + **For direct running**  
    When running it to Page Report format, only the normal report tabs are opened.

    When running it to other formats, if the last-time focused report tab is a normal report, it will be opened directly; if the last-time focused report tab is a bursting report which cannot be run, a warning message will be displayed asking you to select a normal report tab to run using advanced run.
  + **For advanced running**  
    You can only choose the normal report tabs to run.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Running Page Reports in Background Mode

When you run a page report in Page Report Studio, if the report contains a large amount of data, you need to wait several minutes before the report result is displayed, and during this period you have to remain on the report processing page. Therefore Logi JReport provides you the option to switch running page reports to background mode.

To make a report running in Page Report Studio to run in background mode, on the report processing page select the **Background** button.

You can also configure the Page Report Studio profile to run page reports automatically in background mode after a specified time period by setting the [Background Mode Timeout](https://devnet.logianalytics.com/hc/en-us/articles/1500009674101-Customizing-Page-Report-Studio-Profile#Background) option. Then when a report runs in Page Report Studio and the results have not yet been generated after the specified time, it will be automatically switched to run in background mode.

When a page report completes running in background, it will be listed in the [Background Tasks table](https://devnet.logianalytics.com/hc/en-us/articles/1500009648922-Accessing-the-Task-Information-Tables#Background) of the My Tasks page. You can open the report by selecting its Page Report Result link in the table, and once the report is opened the task will automatically be removed from the table.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649862-Running-and-Scheduling-Reports)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674681-Scheduling-Reports)
