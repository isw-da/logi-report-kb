---
title: "Scheduling Tasks to Publish Reports"
id: 1500009649902
section: "Running and Scheduling Reports Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009649902-Scheduling-Tasks-to-Publish-Reports
updated_at: 2021-07-24T20:53:44Z
---

# Scheduling Tasks to Publish Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674681-Scheduling-Reports)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674781-Example-1-Publishing-a-Report-to-the-Versioning-System)

# Scheduling Tasks to Publish Reports

You can schedule tasks for a specified report to publish the report result to various formats as follows:

1. Do either of the following to open the
   [Schedule](https://devnet.logianalytics.com/hc/en-us/articles/1500009646762-Schedule) dialog.
   * On the Logi JReport Console > Resources page, browse to the report you want to schedule to run, then:
     + Select the report row, then on the task bar of the Resources page, select **Run** > **Schedule**.
     + Select the report row, right-click in the row and select **Schedule** from the shortcut menu.
     + Put the mouse pointer over the report row and select the  **Schedule** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920422295/btn_srv_schdl.gif) on the floating toolbar.
   * On the Logi JReport Console page, select **My Tasks**  on the system toolbar, then select the **Scheduled** tab. Select **New Schedule** on the task bar of the My Tasks page, then in the New Schedule dialog, check the **Select Report to Create Schedule** radio button, specify the folder and then the catalog in which the report you want to schedule to run is saved, then select the report and select **OK**.
   * On the [Logi JReport Server Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009648602-Accessing-Logi-JReport-Server-Guide-v15-Server-via-a-Web-Browser#Local), select **Schedule** in the Manage category, the My Tasks page with the Scheduled tab selected is displayed. Select **New Schedule** on the task bar of the My Tasks page, then in the New Schedule dialog, check the **Select Report to Create Schedule** radio button, specify the folder and then the catalog in which the report you want to schedule to run is saved, then select the report and select **OK**.
2. In the General tab,

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920428183/sch_gen.gif)

   1. Specify the name for the task in the Schedule Name text box.
   2. For a page report, select the report tabs you want to run from the page report. You can choose multiple normal report tabs or one bursting report at a time (for scheduling a bursting report, see [Scheduling a Task Containing a Bursting Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009674701-Scheduling-a-Task-Containing-a-Bursting-Report)). When multiple normal report tabs are selected, check **Export to One File** if you want to export them to just one result file. The report tabs will be exported in the list order. You can change the order of the report tabs by selecting ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif) and ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif).
   3. If there are multiple [dynamic connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009669041-Configuring-Dynamic-Connections) available, expand the **Select Dynamic Connection** section and select a connection from the drop-down list. Select **Connection Properties** to view the connection information if needed.
   4. Expand the **Report Information** section, select **Select Another Catalog** to specify another catalog for the report if required.

      Select the report version and catalog version from the corresponding drop-down lists.

      Assign a priority to the task from the Priority drop-down list. The Priority property is available to administrators only and the priority levels are from 1 to 10 in ascending order of lowest priority to highest priority (by default this property is ignored unless server.properties is modified to set queue.policy not equal to 0).
   5. Expand the **Advanced** section to configure some advanced settings for the report.

      Specify the style group for the report.

      Check the **Enable Converting Encoding** option and specify the encoding before and after converting from the corresponding drop-down lists.

      If the report is defined with NLS, check **Enable NLS** then specify a language to display the report contents in.

      Define the encoding for the report by selecting from the Encoding drop-down list.

      Specify the DB user and password with which to connect to the data source. You can either use the default ones defined in the catalog or specify another DB user and password.

      Check the **Add TaskListener to be Invoked** option to call a Java application when scheduling the report (for details, see [Adding TaskListener When Scheduling Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009668701-Adding-TaskListener-When-Scheduling-Reports)).

      If you are in a [cluster](https://devnet.logianalytics.com/hc/en-us/articles/1500009644262-Logi-JReport-Server-Guide-v15-Server-Cluster) environment, you can also directly specify an active server in the cluster to perform the schedule task via the Specify a preferred server to run the task option.

      If you want to enable task recovery, check **Enable Auto Recover Task**, then specify the maximum number of times in which to retry running the task in order to recover it, the time interval between the retries, and whether to recreate all or just the failed results when you publish the task to multiple formats.

      The default on-screen filter values you have saved in the report will be automatically used to run the report. If you do not want to apply the filter conditions, uncheck **Use User-Defined Default On-screen Filter Values**.
3. In the Parameter tab, [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009649882-Specifying-Parameter-Values) if the report has parameters.
4. In the Publish tab, specify the type of the task.

   Six task types are provided by Logi JReport Server: To Version, To Disk (unavailable to [organization users](https://devnet.logianalytics.com/hc/en-us/articles/1500009675081-Multi-tenancy-Supported-via-Organizations)), To E-mail, To Printer, To Fax and To FTP. Choose the types you want to publish, select the report formats for each type and set the other settings as required.
5. In the Conditions tab,
   1. In the Time sub tab, specify the time zone and the time for when the task is to be performed.

      ![](https://devnet.logianalytics.com/hc/article_attachments/4404926663703/sch_cndtn_time.gif)

      * To perform the task as soon as you submit it, select **Run this task immediately** from the Time Type drop-down list.
      * To run the task at a specified time, select **Run this task at**, then define the time according to your requirement. Check **Run missed task upon server restart** so as to run the missed tasks when you restart the server.
      * If you want to run the task repeatedly, select  **Run this task periodically**, then specify the duration, date and time accordingly. Check **Run missed task upon server restart** so as to run the missed tasks when you restart the server.
   2. If you want to bind a trigger to the task, switch to the **Trigger** sub tab (triggers can only be fired by administrators, for more information, see [Managing Triggers](https://devnet.logianalytics.com/hc/en-us/articles/1500009648982-Managing-Triggers)).

      ![](https://devnet.logianalytics.com/hc/article_attachments/4404926664215/sch_cndtn_trgr.gif)

      From the Select a trigger to bind drop-down list, select the required trigger or select the **Create New** button to create a new trigger (the button is not available to [organization users](https://devnet.logianalytics.com/hc/en-us/articles/1500009675081-Multi-tenancy-Supported-via-Organizations)), then specify the trigger logic with time condition.

      * **Trigger Only**  
         Performs the task only when the trigger is fired.
      * **Trigger and Time Condition**   
         Performs the task when both time is up and the trigger is fired.

        **Note:** When this logic is selected:

        + No matter which condition is ready, the task can only be performed when its counterpart is ready.
        + If you specify the task to be performed at a specific time, you must check the option Run missed task upon server restart, otherwise the task will be regarded as expired and will be deleted when the time condition is ready before the trigger condition.
      * **Time Condition after Trigger**   
         Performs a task when time is up after the trigger is fired. If the time condition is ready before the trigger condition, the task will be regarded as expired and will be deleted.
      * **Time Condition or Trigger**  
         Performs the task when either time is up or the trigger is fired.
6. In the Notification tab, select an e-mail address from the Mail To box to notify someone via e-mail of when the task is finished successfully or when it fails. If you haven't sent any mail notification before, the Mail To box is empty. Select the **New** button to [create an e-mail address](https://devnet.logianalytics.com/hc/en-us/articles/1500009646762-Schedule#New). To send out mail notification, an [e-mail server](https://devnet.logianalytics.com/hc/en-us/articles/1500009669181-Configuring-the-E-Mail-Server) must have been predefined by the administrator.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920428695/sch_notif.gif)
7. If the Duration tab is available, specify a time duration for the task, and ask Logi JReport Server to cancel the task or to notify you or someone else of the task status via e-mail if the task has not yet finished running when the task duration is up. For detailed information, see [Task-level Timeout for Advanced Run and Schedule Tasks](https://devnet.logianalytics.com/hc/en-us/articles/1500009648962-Task-level-Timeout-for-Advanced-Run-and-Schedule-Tasks).
8. Select **Finish**, and Logi JReport Server will then perform the task.

The following are some specific scheduling examples:

* [Example 1: Publishing a Report to the Versioning System](https://devnet.logianalytics.com/hc/en-us/articles/1500009674781-Example-1-Publishing-a-Report-to-the-Versioning-System)
* [Example 2: Publishing a Report to Disk](https://devnet.logianalytics.com/hc/en-us/articles/1500009649922-Example-2-Publishing-a-Report-to-Disk-)
* [Example 3: Publishing a Report to E-Mail](https://devnet.logianalytics.com/hc/en-us/articles/1500009674761-Example-3-Publishing-a-Report-to-E-mail)
* [Example 4: Publishing a Report to Printer](https://devnet.logianalytics.com/hc/en-us/articles/1500009649942-Example-4-Publishing-a-Report-to-Printer)
* [Example 5: Publishing a Report to Fax](https://devnet.logianalytics.com/hc/en-us/articles/1500009674721-Example-5-Publishing-a-Report-to-Fax)
* [Example 6: Publishing a Report to an FTP Site](https://devnet.logianalytics.com/hc/en-us/articles/1500009674741-Example-6-Publishing-a-Report-to-an-FTP-Site)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674681-Scheduling-Reports)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674781-Example-1-Publishing-a-Report-to-the-Versioning-System)
