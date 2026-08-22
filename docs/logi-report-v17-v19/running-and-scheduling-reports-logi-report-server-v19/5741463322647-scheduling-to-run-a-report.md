---
title: "Scheduling to Run a Report"
id: 5741463322647
section: "Running and Scheduling Reports Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741463322647-Scheduling-to-Run-a-Report
updated_at: 2022-10-31T17:18:21Z
---

# Scheduling to Run a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741483442455-Scheduling-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741454859671-Scheduling-to-Run-Multiple-Reports)

# Scheduling to Run a Report

This topic describes how you can create a schedule task to run and publish a specified report to different destinations in various formats.

1. Do either of the following to open the [Schedule](https://devnet.logianalytics.com/hc/en-us/articles/5741433620631-Schedule-Dialog-Box-Properties) dialog box.
   * In the resource tree on the Server Console, browse to the report you want to schedule to run, then:
     + Put the mouse pointer over the report row and select the  **Schedule** button ![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/9905654855063/btn_schdl.gif) on the floating toolbar.
     + Select the report row, right-click in the row and select **Schedule** from the shortcut menu.
     + Select the report row and select **Run** > **Schedule** on the task bar of the Resources page.
   * On the Server Console, select **My Tasks** on the system toolbar, then select the **Scheduled** tab. Select **New Schedule** on the task bar of the My Tasks page, then in the [New Schedule](https://devnet.logianalytics.com/hc/en-us/articles/5741406176919-New-Schedule-Dialog-Box-Properties) dialog box, select the **Select Report to Create Schedule** radio button, specify the folder and then the catalog in which the report you want to schedule to run is saved, then select the report and select **OK**.
   * In the [Logi Report Server Start Page](https://devnet.logianalytics.com/hc/en-us/articles/5741461387031-Accessing-Logi-Report-Server-via-a-Web-Browser#Start), select **Schedule** in the Manage category. Server displays the My Tasks page with the Scheduled tab selected. Select **New Schedule** on the task bar of the My Tasks page, then in the New Schedule dialog box, select the **Select Report to Create Schedule** radio button, specify the folder and then the catalog in which the report you want to schedule to run is saved, then select the report and select **OK**.
2. In the **General** tab,

   ![Schedule dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/9905637353495/sch_gen.gif)

   1. Specify the name for the task in the **Schedule Name** text box.
   2. For a page report, select the report tabs you want to run from the page report. You can choose multiple normal report tabs or one bursting report at a time (for scheduling a bursting report, see [Scheduling Bursting Reports](https://devnet.logianalytics.com/hc/en-us/articles/5741463244055-Scheduling-Bursting-Reports)). When multiple normal report tabs are selected, select **Export to One File** if you want to export them to just one file. The report tabs will be exported in the list order. You can change the order of the report tabs by selecting ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif).
   3. If there are multiple [dynamic connections](https://devnet.logianalytics.com/hc/en-us/articles/5741395796375-Creating-and-Using-Dynamic-Connections) available, expand the **Select Dynamic Connection** section and select a connection from the drop-down list. You can select **Connection Properties** to view the connection information.
   4. Expand the **Report Information** section, you can select **Select Another Catalog** to specify another catalog for the report, and then select the report version and catalog version from the corresponding drop-down lists (the catalog and report/catalog version cannot be changed if the report is a [shared report](https://devnet.logianalytics.com/hc/en-us/articles/5741461964439-Sharing-Web-Reports)).

      Assign a priority to the task from the Priority drop-down list. The Priority property is available to administrators only and the priority levels are from 1 to 10 in ascending order of lowest priority to highest priority (by default this property is ignored unless server.properties is modified to set queue.policy not equal to 0).
   5. Expand **Advanced** to configure some advanced settings for the report.

      Specify the style group for the report.

      Select **Enable Converting Encoding** and specify the encoding before and after converting from the corresponding drop-down lists.

      If the report is defined with NLS, select **Enable NLS** then specify a language to display the report contents in.

      Define the encoding for the report by selecting from the Encoding drop-down list.

      Specify the DB user and password with which to connect to the data source. You can either use the default ones defined in the catalog or specify another DB user and password.

      Select **Add TaskListener to be Invoked** to call a Java application before/after Server runs the report to obtain information about the report task (for more information, see [Applying TaskListener](https://devnet.logianalytics.com/hc/en-us/articles/5741395089175-Applying-TaskListener)).

      If you are in a [cluster](https://devnet.logianalytics.com/hc/en-us/articles/5741415572759-Logi-Report-Server-Cluster-Logi-Report-Server-v19) environment, you can also directly specify an active server in the cluster to perform the schedule task via the Specify a preferred server to run the task option.

      If you want to enable task recovery, select **Enable Auto Recover Task**, then specify the maximum number of times to retry running the task in order to recover it, the time interval between the retries, and whether to recreate all or just the failed results when you publish the task to multiple formats.

      Server automatically uses the default on-screen filter values you have saved in the report to run the report. If you do not want to apply the filter conditions, clear **Use User Defined Default On-screen Filter Values**.

      When you have created bookmarks for the web report, select a bookmark from the **Use Bookmark** drop-down list to run the bookmark of the web report.
3. In the **Parameter** tab, [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/5741454720023-Specifying-Parameter-Values) if the report has parameters.
4. In the **Publish** tab, specify the types of the task.

   Six task types that Server supports: To Version, To Disk (unavailable to [organization users](https://devnet.logianalytics.com/hc/en-us/articles/5741463905047-Multitenancy-Supported-via-Organizations)), To E-mail, To Printer, To Fax and To FTP. Choose the types you want to publish, select the report formats for each task type and set the other settings. For more information about each task type, see the examples in [Examples of Scheduling Reports](https://devnet.logianalytics.com/hc/en-us/articles/5741483494551-Examples-of-Scheduling-Reports).
5. In the **Conditions** tab,
   1. In the **Time** tab, specify the time zone and the time for when the task is to be performed.

      ![Schedule dialog - Conditions - Time](https://devnet.logianalytics.com/hc/article_attachments/9905637382679/sch_cndtn_time.gif)

      * To run the task as soon as you submit it, select **Run this task immediately** from the Time Type drop-down list.
      * To run the task at a specified time, select **Run this task at**, then specify the date and time according to your requirement.
      * If you want to run the task repeatedly, select **Run this task periodically**, then specify the duration, date, and time accordingly. To add an exception date on which you do not want to run the task, select **Show Exception**, then select the **Add** button and in the Select Condition dialog box select the date as required. You can add several exception dates as you want. To remove an exception date, select it in the exception date box and select **Remove**.

        ![Exception Date Box](https://devnet.logianalytics.com/hc/article_attachments/9905637403415/sch_cndtn_time_excpt.gif)

      When you select to run the task at a specified time or repeatedly, you can select **Run missed task upon server restart** so as to run the missed tasks when you restart the server.
   2. If you want to bind a trigger to the task, select **Trigger**. You need to be an administrator to fire triggers. For more information, see [Managing Triggers](https://devnet.logianalytics.com/hc/en-us/articles/5741438280855-Managing-Triggers).

      ![Schedule dialog - Conditions - Trigger](https://devnet.logianalytics.com/hc/article_attachments/9905637420439/sch_cndtn_trgr.gif)

      From the Select a trigger to bind drop-down list, select the required trigger or select the **New Trigger** button to create a new trigger in the [New Trigger](https://devnet.logianalytics.com/hc/en-us/articles/5741406198679-New-Trigger-Dialog-Box-Properties) dialog box (the button is not available to [organization users](https://devnet.logianalytics.com/hc/en-us/articles/5741463905047-Multitenancy-Supported-via-Organizations)), then specify the trigger logic with time condition.

      * **Trigger Only**  
         Performs the task only when the trigger is fired.
      * **Trigger and Time Condition**   
         Performs the task when both time is up and the trigger is fired.

        ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)When you selected this logic:

        + No matter which condition is ready, Server performs the task only when its counterpart is ready.
        + If you specify to perform the task at a specific time, you must select the option **Run missed task upon server restart**, otherwise Server regards the task as expired and deletes it when the time condition is ready before the trigger condition.
      * **Time Condition after Trigger**   
         Performs a task when time is up after the trigger is fired. If the time condition is ready before the trigger condition, the task will be regarded as expired and will be deleted.
      * **Time Condition or Trigger**  
         Performs the task when either time is up or the trigger is fired.
6. In the **Notification** tab, select an email address from the **Mail To** box to notify someone via email of when the task finishes or when it fails. If you have not sent any mail notification before, the **Mail To** box is empty. Select the **New** button to [create an email address](https://devnet.logianalytics.com/hc/en-us/articles/5741433620631-Schedule-Dialog-Box-Properties#New). To send out mail notification, an [email server](https://devnet.logianalytics.com/hc/en-us/articles/5741416139159-Configuring-the-Email-Server) must have been predefined by the administrator.

   ![Schedule dialog - Notification](https://devnet.logianalytics.com/hc/article_attachments/9905671010583/sch_notif.gif)
7. If the **Duration** tab is available, specify a time duration for the task, and ask Server to cancel the task or to notify you or someone else of the task status via email if the task has not yet finished running when the task duration is up. For more information, see [Task-Level Timeout for Advanced Run and Schedule Tasks](https://devnet.logianalytics.com/hc/en-us/articles/5741438263319-Managing-Report-Running-Tasks#Timeout).
8. Select **Finish**. Server starts to perform the task.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741483442455-Scheduling-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741454859671-Scheduling-to-Run-Multiple-Reports)
