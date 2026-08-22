---
title: "Running Reports"
id: 1500009724222
section: "Run and Schedule Reports Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009724222-Running-Reports
updated_at: 2021-12-13T03:43:23Z
---

# Running Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724182-Running-and-Scheduling-Reports-Logi-Report-Server-v17)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009751081-Scheduling-Reports)

# Running Reports

This topic introduces how to run reports directly, in Advanced mode, and in background mode. If you know the default format for viewing reports and this format is what you expect, use [direct running](#Direct). If you would like a different view format or to customize some other information such as the running priority, how to save the result, the expiration time, and so on, use [advanced running](#Advanced).

**Note:** To run reports in public folders in the server resource tree, you must have the Execute and/or Edit permissions on the reports and the Visible and Read permissions on the catalogs that the reports use. For more information about permissions, see [Managing Permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009751241-Managing-Permissions).

Select the following links to view the topics:

* [Running Reports Directly](#Direct)
* [Running Reports in Advanced Mode](#Advanced)
* [Running Page Reports in Background Mode](#Background)

## Running Reports Directly

Direct running reports is to use the default format setting to view the report result.

If the reports are created on Logi Report Server, the default format is controlled by the [Default Format for Viewing Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#Format) option in the server profile. By default, this option is set to Web/Page Studio, which means that page reports (.cls) are opened in [Page Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009723302-Page-Report-Studio) and web reports (.wls) in [Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009724642-Web-Report-Studio).

If the reports are edited using Logi Report Designer, the default format is controlled by the Default Format for Viewing Report property in the Report Inspector. If this property is set to <Server Setting>, the viewing format will be determined by the above setting on server. For page reports this property is available to each report tab in the reports, therefore when a page report contains multiple report tabs and these report tabs have different default format settings, for example, report tab 1 is Page Report, tab 2 HTML and tab 3 Excel, there will be different direct running results, depending on which report tab is the last-time focused tab in the page report when the page report is saved at report design time. If it is report tab 1, all the three tabs in the page report will be opened in Page Report Studio. If it is report tab 2 or 3, only tab 2 or 3 will be displayed in the specified format, and this applies to all the other formats except Page Report.

You can run a report directly from the server resource tree in the Logi Report Server console by taking any of the following ways:

* **Selecting the report name**  
  To use this way to run a report saved in the Public Report folder, you need to have the Execute permission on the report so that the report name can be shown with hyperlink when you move the mouse pointer on the report row.

  Selecting the report name runs the report in the default format (if the report contains parameters, you need to [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009724202-Specifying-Parameter-Values)). When the default format for viewing report is Web/Page Studio, which studio mode will be applied to run the report is decided by the [Default View for Page Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#PageMode)/[Default Mode for Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#WebMode) option in the server profile. However if the default view/mode is Interactive View/Edit Mode but you do not have the Edit permission on the report, you will fail to run the report and instead get an error message.
* **Using the Run option**  
  To use this way to run a report saved in the Public Report folder, you need to have the Execute permission on the report so that the Run option can be available.

  Do any of the following:

  + Put the mouse pointer over the report row and select the  **Run** button ![Run button](https://devnet.logianalytics.com/hc/article_attachments/4404942480023/btn_srv_run.gif) on the floating toolbar.
  + Select the report row, right-click in the report row and select **Run** from the shortcut menu.
  + Select the report row and select **Run** > **Run** on the task bar of the Resources page.

  If the report contains parameters, you will be prompted to specify the parameter values. Then Logi Report Server will display the report in its default format. When the default format for viewing report is Web/Page Studio, the Server will open page report in the Basic View of Page Report Studio and web report in the View Mode of Web Report Studio.

  You can also use the Run option to run multiple reports at a time. To do this, select the check boxes ahead of the required reports and select **Run** > **Run** on the task bar or right-click in any report row and select **Run** from the shortcut menu. If the selected reports contain parameters, the parameter dialog box for each report will appear for you to specify the parameter values. After that the reports will be displayed one by one in the default format.
* **Using the Edit option**  
  To use this way to run a report saved in the Public Report folder, you need to have the Edit permission on the report so that the Edit option can be available. For a [shared report](https://devnet.logianalytics.com/hc/en-us/articles/1500009723142-Sharing-Reports), the Allow Edit property should also be enabled.

  Do any of the following:

  + Put the mouse pointer over the report row and select the  **Edit**  button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404936766231/btn_srv_edit.gif) on the floating toolbar.
  + Select the report row, right-click in the report row and select **Edit** from the shortcut menu.
  + Select the report row and select **Run** > **Edit**  on the task bar of the Resources page.

  If the report contains parameters, you will be prompted to specify the parameter values. Then the report will be displayed in the default format. When the default format for viewing report is Web/Page Studio, the report will be opened in Interactive View of Page Report Studio or Edit Mode of Web Report Studio.

## Running Reports in Advanced Mode

To run reports saved in a public folder in Advanced mode, you need to have the Execute permission on the reports.

1. In the server resource tree in the Logi Report Server console, browse to the report you want to run.
2. Do either of the following to open the [Advanced Run](https://devnet.logianalytics.com/hc/en-us/articles/1500009747301-Advanced-Run) dialog box.
   * Put the mouse pointer over the report row and select the **Advanced Run** button ![Advanced Run button](https://devnet.logianalytics.com/hc/article_attachments/4404936766487/btn_srv_advrun.gif) on the floating toolbar.
   * Select the report row, right-click in the row and select **Advanced Run** from the shortcut menu.
   * Select the report row and click **Run** > **Advanced Run** on the task bar of the Resources page.
3. In the General tab,

   ![Advanced Run dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404936769943/advcdrn_gen.gif)

   1. For a page report, select the report tabs in the page report you want to run. The report tabs will run in the list order. You can change the order of the report tabs by selecting ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif). However if you choose to run the page report in the Page Report format in the Format tab, the unselected report tabs will also be run.
   2. If there are multiple [dynamic connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009718782-Creating-and-Using-Dynamic-Connections) available, expand the **Select Dynamic Connection** section and select a connection from the drop-down list. You can select **Connection Properties** to view the connection information.
   3. Expand the **Report Information** section, you can select **Select Another Catalog** to specify another catalog for the report, and then select the report version and catalog version from the corresponding drop-down lists (the catalog and report/catalog version cannot be changed if the report is a [shared report](https://devnet.logianalytics.com/hc/en-us/articles/1500009723142-Sharing-Reports)).
   4. Assign a priority to the task from the Priority drop-down list. The Priority property is available to administrators only and the priority levels are from 1 to 10 in ascending order of lowest priority to highest priority (by default this property is ignored unless server.properties is modified to set queue.policy not equal to 0).
4. In the Parameter tab, [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009724202-Specifying-Parameter-Values) if the report has parameters.
5. In the Format tab,

   ![Advanced Run dialog - Format tab](https://devnet.logianalytics.com/hc/article_attachments/4404936770199/advcdrn_fmt.gif)

   1. Choose a format to view the report result and set the [properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009747301-Advanced-Run#Format) of the selected format. When HTML is selected, the names of page navigation links in the HTML results such as First, Previous, Next, and Last can be localized according to your requirements. For details, refer to [Localizing Page Navigation Links in HTML Report Outputs](https://devnet.logianalytics.com/hc/en-us/articles/1500009750321-NLS-at-Report-Level#Link).
   2. Expand the **Advanced** section.
   3. Specify the style group for the report.
   4. Select the **Enable Converting Encoding** option and specify the encoding before and after converting from the corresponding drop-down lists.
   5. If the report is defined with NLS, select **Enable NLS** then specify a language to display the report contents in.
   6. Define the encoding for the report by selecting from the Encoding drop-down list.
   7. Specify the DB user and password with which to connect with the data source. You can either use the default ones defined in the catalog or specify another DB user and password.
   8. The default on-screen filter values you have saved in the report will be automatically used to run the report. If you do not want to apply the filter conditions, clear **Use User Defined Default On-screen Filter Values**.
   9. When the selected format is any format other than Page Report or Web Report, select the **Add TaskListener to be Invoked** option to call a Java application before/after the report runs so as to obtain information about the report task (for details, see [Applying TaskListener](https://devnet.logianalytics.com/hc/en-us/articles/1500009718522-Applying-TaskListener)).
6. In the Archive tab, select the **Auto Archive Properties** check box, then specify [where to generate the report result version](https://devnet.logianalytics.com/hc/en-us/articles/1500009750221-Creating-Versions#Result) and the [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009723202-Applying-an-Archive-Policy).

   ![Advanced Run dialog - Archive tab](https://devnet.logianalytics.com/hc/article_attachments/4404936770455/advcdrn_archv.gif)
7. If the Duration tab is available, specify a time duration for the task, and ask Logi Report Server to cancel the task or to notify you or someone else of the task status via e-mail if the task has not yet finished running when the task duration is up. For detailed information, see [Task-level Timeout for Advanced Run and Schedule Tasks](https://devnet.logianalytics.com/hc/en-us/articles/1500009750161-Managing-Tasks#Timeout).
8. Select **Finish** to run the report.

## Running Page Reports in Background Mode

When you run a page report in Page Report Studio, if the report contains a large amount of data, you need to wait several minutes before the report result comes out, and during this period you should make sure the report processing page is not closed. This may bring you some inconvenience, therefore Logi Report provides you the Background and Cancel options on the report processing bar to allow you switch the report to run in background mode or cancel it from running.

By setting the [Background Mode Timeout](https://devnet.logianalytics.com/hc/en-us/articles/1500009750581-Customizing-Page-Report-Studio-Profile#Background) option in the Page Report Studio profile, you can also make page reports run automatically in background mode after a specified time period. Then when a report runs in Page Report Studio and the result has not yet been generated after the specified time, it will be automatically switched to run in background mode.

When a page report completes running in background, it will be listed in the [Background Tasks table](https://devnet.logianalytics.com/hc/en-us/articles/1500009750161-Managing-Tasks#Background) of the My Tasks page. You can open the report result by selecting the Page Report link in the table.

**Notes:**

* ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")When you click a report name, the Run option or the Edit option more than once within 5 seconds to run a report directly, a message will ask whether you want to run the report only once or multiple times. This is to avoid unwanted submitting of running the same report repeatedly.
* When running a page report containing both normal and [bursting report tabs](https://devnet.logianalytics.com/hc/en-us/articles/1500009724242-Scheduling-Bursting-Reports):
  + **For direct running**  
    When running it in the Page Report format, only the normal report tabs are opened.

    When running it in other formats, if the last-time focused report tab is a normal report, it will be opened directly; if the last-time focused report tab is a bursting report which cannot be run, a warning message will be displayed asking you to select a normal report tab to run using advanced run.
  + **For advanced running**  
    You can only choose the normal report tabs to run.
* To be able to run page reports in background mode, you need to make sure the option [Enable Background Task for Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#BackgroundTask) in the server profile is selected.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724182-Running-and-Scheduling-Reports-Logi-Report-Server-v17)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009751081-Scheduling-Reports)
