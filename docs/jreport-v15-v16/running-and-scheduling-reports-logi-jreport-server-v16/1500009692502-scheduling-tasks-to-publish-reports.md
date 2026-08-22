---
title: "Scheduling Tasks to Publish Reports"
id: 1500009692502
section: "Running and Scheduling Reports Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009692502-Scheduling-Tasks-to-Publish-Reports
updated_at: 2021-11-03T06:56:35Z
---

# Scheduling Tasks to Publish Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692482-Scheduling-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718701-Scheduling-a-Task-Containing-a-Bursting-Report)

# Scheduling Tasks to Publish Reports

You can schedule tasks for a specified report to publish the report result to various formats as follows:

1. Do either of the following to open the
   [Schedule](https://devnet.logianalytics.com/hc/en-us/articles/1500009715061-Schedule) dialog.
   * In the server resource tree in the Logi JReport Server console, browse to the report you want to schedule to run, then:
     + Put the mouse pointer over the report row and select the  **Schedule** button ![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4412139508887/btn_schdl.gif) on the floating toolbar.
     + Select the report row, right-click in the row and select **Schedule** from the shortcut menu.
     + Select the report row and select **Run** > **Schedule** on the task bar of the Resources page.
   * In the Logi JReport Server console, select **My Tasks**  on the system toolbar, then select the **Scheduled** tab. Select **New Schedule** on the task bar of the My Tasks page, then in the [New Schedule](https://devnet.logianalytics.com/hc/en-us/articles/1500009688862-New-Schedule) dialog, check the **Select Report to Create Schedule** radio button, specify the folder and then the catalog in which the report you want to schedule to run is saved, then select the report and select **OK**.
   * In the [Logi JReport Server Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009717601-Accessing-Logi-Report-Server-via-a-Web-Browser#Start), select **Schedule** in the Manage category, the My Tasks page with the Scheduled tab selected is displayed. Select **New Schedule** on the task bar of the My Tasks page, then in the New Schedule dialog, check the **Select Report to Create Schedule** radio button, specify the folder and then the catalog in which the report you want to schedule to run is saved, then select the report and select **OK**.
2. In the General tab,

   ![Schedule dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4412112528663/sch_gen.gif)

   1. Specify the name for the task in the Schedule Name text box.
   2. For a page report, select the report tabs you want to run from the page report. You can choose multiple normal report tabs or one bursting report at a time (for scheduling a bursting report, see [Scheduling a Task Containing a Bursting Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009718701-Scheduling-a-Task-Containing-a-Bursting-Report)). When multiple normal report tabs are selected, check **Export to One File** if you want to export them to just one result file. The report tabs will be exported in the list order. You can change the order of the report tabs by selecting ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4412112497431/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4412112497687/btn_mvdown.gif).
   3. If there are multiple [dynamic connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009712421-Creating-and-Using-Dynamic-Connections) available, expand the **Select Dynamic Connection** section and select a connection from the drop-down list. Select **Connection Properties** to view the connection information if needed.
   4. Expand the **Report Information** section, select **Select Another Catalog** to specify another catalog for the report if required, and select the report version and catalog version from the corresponding drop-down lists (the catalog and report/catalog version cannot be changed if the report is a [shared report](https://devnet.logianalytics.com/hc/en-us/articles/1500009717901-Sharing-Reports)).

      Assign a priority to the task from the Priority drop-down list. The Priority property is available to administrators only and the priority levels are from 1 to 10 in ascending order of lowest priority to highest priority (by default this property is ignored unless server.properties is modified to set queue.policy not equal to 0).
   5. Expand the **Advanced** section to configure some advanced settings for the report.

      Specify the style group for the report.

      Check the **Enable Converting Encoding** option and specify the encoding before and after converting from the corresponding drop-down lists.

      If the report is defined with NLS, check **Enable NLS** then specify a language to display the report contents in.

      Define the encoding for the report by selecting from the Encoding drop-down list.

      Specify the DB user and password with which to connect to the data source. You can either use the default ones defined in the catalog or specify another DB user and password.

      Check the **Add TaskListener to be Invoked** option to call a Java application before/after the report runs so as to obtain information about the report task (for details, see [Applying TaskListener](https://devnet.logianalytics.com/hc/en-us/articles/1500009712081-Applying-TaskListener)).

      If you are in a [cluster](https://devnet.logianalytics.com/hc/en-us/articles/1500009712281-Logi-JReport-Server-Cluster) environment, you can also directly specify an active server in the cluster to perform the schedule task via the Specify a preferred server to run the task option.

      If you want to enable task recovery, check **Enable Auto Recover Task**, then specify the maximum number of times in which to retry running the task in order to recover it, the time interval between the retries, and whether to recreate all or just the failed results when you publish the task to multiple formats.

      The default on-screen filter values you have saved in the report will be automatically used to run the report. If you do not want to apply the filter conditions, uncheck **Use User-Defined Default On-screen Filter Values**.
3. In the Parameter tab, [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009692442-Specifying-Parameter-Values) if the report has parameters.
4. In the Publish tab, specify the type of the task.

   Six task types are provided by Logi JReport Server: To Version, To Disk (unavailable to [organization users](https://devnet.logianalytics.com/hc/en-us/articles/1500009692742-Multi-tenancy-Supported-via-Organizations)), To E-mail, To Printer, To Fax and To FTP. Choose the types you want to publish, select the report formats for each type and set the other settings as required.
5. In the Conditions tab,
   1. In the Time sub tab, specify the time zone and the time for when the task is to be performed.

      ![Schedule dialog - Conditions - Time](https://devnet.logianalytics.com/hc/article_attachments/4412112529047/sch_cndtn_time.gif)

      * To run the task as soon as you submit it, select **Run this task immediately** from the Time Type drop-down list.
      * To run the task at a specified time, select **Run this task at**, then define the time according to your requirement.
      * If you want to run the task repeatedly, select  **Run this task periodically**, then specify the duration, date and time accordingly. To add an exception date on which you do not want to run the task, select **Show Exception**, then select the **Add** button and in the Select Condition dialog select the date as required. You can add several exception dates as you want. To remove an exception date, check it in the exception date box and select **Remove**.

        ![Exception Date Box](https://devnet.logianalytics.com/hc/article_attachments/4412112529431/sch_cndtn_time_excpt.gif)

      When you select to run the task at a specified time or repeatedly, check **Run missed task upon server restart** so as to run the missed tasks when you restart the server if needed.
   2. If you want to bind a trigger to the task, switch to the **Trigger** sub tab (triggers can only be fired by administrators, for more information, see [Managing Triggers](https://devnet.logianalytics.com/hc/en-us/articles/1500009691402-Managing-Triggers)).

      ![Schedule dialog - Conditions - Trigger](https://devnet.logianalytics.com/hc/article_attachments/4412131413271/sch_cndtn_trgr.gif)

      From the Select a trigger to bind drop-down list, select the required trigger or select the **New Trigger** button to create a new trigger in the [New Trigger](https://devnet.logianalytics.com/hc/en-us/articles/1500009688882-New-Trigger) dialog (the button is not available to [organization users](https://devnet.logianalytics.com/hc/en-us/articles/1500009692742-Multi-tenancy-Supported-via-Organizations)), then specify the trigger logic with time condition.

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
6. In the Notification tab, select an e-mail address from the Mail To box to notify someone via e-mail of when the task is finished successfully or when it fails. If you haven't sent any mail notification before, the Mail To box is empty. Select the **New** button to [create an e-mail address](https://devnet.logianalytics.com/hc/en-us/articles/1500009715061-Schedule#New). To send out mail notification, an [e-mail server](https://devnet.logianalytics.com/hc/en-us/articles/1500009686782-Configuring-the-E-mail-Server) must have been predefined by the administrator.

   ![Schedule dialog - Notification](https://devnet.logianalytics.com/hc/article_attachments/4412112530071/sch_notif.gif)
7. If the Duration tab is available, specify a time duration for the task, and ask Logi JReport Server to cancel the task or to notify you or someone else of the task status via e-mail if the task has not yet finished running when the task duration is up. For detailed information, see [Task-level Timeout for Advanced Run and Schedule Tasks](https://devnet.logianalytics.com/hc/en-us/articles/1500009691382-Managing-Tasks#Timeout).
8. Select **Finish**, and Logi JReport Server will then perform the task.

The following are some specific scheduling examples:

* [Example 1: Publishing a report to the versioning system](#Version)
* [Example 2: Publishing a report to disk](#Disk)
* [Example 3: Publishing a report to e-mail](#Mail)
* [Example 4: Publishing a report to printer](#Printer)
* [Example 5: Publishing a report to fax](#Fax)
* [Example 6: Publishing a report to an FTP site](#FTP)

**Example 1: Publishing a report to the versioning system**

In this example, a task is set up and will be performed immediately. The generated result is asked to be kept for 30 days.

1. In the server resource tree in the Logi JReport Server console, select the report row, right-click in the row and select **Schedule** from the shortcut menu to display the Schedule dialog.
2. In the General tab, specify the general report settings.
3. In the Parameter tab, specify the parameter values as required if the report has parameters.
4. In the Publish tab,
   1. Select the **To Version** sub tab, then check **Publish to Versioning System**.

      ![Schedule dialog - Publish to Version](https://devnet.logianalytics.com/hc/article_attachments/4412131413527/sch_pub_vrsn.gif)
   2. Select the required formats and set the format settings.
   3. Check the **Built-in Version Folder** option in Archive Location to save the report result version in the built-in version folder.
   4. Set **0** for the Maximum Number of Versions.
   5. Check the  **Result Auto-delete** option and define the result to expire in 30 days.
5. In the Conditions tab, select the **Time** sub tab, define the time zone from the Time Zone drop-down list, then from the Time Type drop-down list, choose **Run this task immediately**.
6. If you want to notify someone of when the task is finished by sending an e-mail, go to the Notification tab and then set the settings.
7. Select **Finish** to have the task performed.

Then, select **My Tasks** on the system toolbar. While the task is being performed, you can see a record of it in the Running table. On completion it will be put into the Completed table.

**Notes:**

* When scheduling to publish a page report to the versioning system, the Page Report Result and JReport Result formats are based on the report level, that is the report with all selected report tabs will be output to a single file no matter Export to One File in the General tab is checked or not.
* There is another way to publish the report result to version.
  1. Set the property server.version.from.temp to true in the server.properties file in  `<install_root>\bin`, or select the option Enable "Publish to Versioning System" for Background Tasks View in the Administration > Configuration > Advanced page in the Logi JReport Server console.
  2. [Run a report in the Advanced mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009692462-Running-Reports#Advanced), select a format other than Page Report or Web Report in the Format tab. Specify other settings as required. Then select **Finish**.
  3. In the view page, you will see a link Publish to Versioning System at the upper-left corner. Select the link to publish the report to version in the current format.

**Example 2: Publishing a report to disk**

In this example, you will learn how to set up a task to publish the report result in various file formats to the file system repeatedly at the start of each month.
It is not available to [organization users](https://devnet.logianalytics.com/hc/en-us/articles/1500009692742-Multi-tenancy-Supported-via-Organizations).

1. In the server resource tree in the Logi JReport Server console, select the report row, right-click in the row and select **Schedule** from the shortcut menu to display the Schedule dialog.
2. In the General tab, specify the general report settings.
3. In the Parameter tab, specify the parameter values as required if the report has parameters.
4. In the Publish tab, select the **To Disk** sub tab, check **Publish to Disk**, then select the required formats, specify the result locations, and set the format settings according to your requirements. You can apply [dynamic names](https://devnet.logianalytics.com/hc/en-us/articles/1500009718721-Applying-Dynamic-Names-for-Published-Result-Files) for the result if necessary.

   ![Schedule dialog - Publish to Disk](https://devnet.logianalytics.com/hc/article_attachments/4412139522199/sch_pub_disk.gif)
5. In the Conditions tab,
   1. In the Time sub tab, define the time zone from the Time Zone drop-down list, then from the Time Type drop-down list, choose **Run this task periodically**.

      ![Schedule dialog - Time](https://devnet.logianalytics.com/hc/article_attachments/4412131413783/wkrpt_sch_dlg_disk.gif)
   2. In the Duration box, specify a time period for when the task will be performed.
   3. Select **Monthly** from the Date drop-down list and keep the default to run the first day of every 1 month.
   4. Keep the Time settings as default.
6. If you want to notify someone of when the task is finished by sending an e-mail, go to the Notification tab and set the settings.
7. Select **Finish** to have the task performed.

Then, select **My Tasks** on the system toolbar, you will see that the scheduled task has been recorded in the Scheduled table. Since you have not specified the duration *Run until a time* for this task, it will not stop being performed until you delete or disable it from the Scheduled table.

**Notes:**

* When scheduling to publish a page report to disk, the Page Report Result and JReport Result formats are based on the report level, that is, the report with all selected report tabs will be output to a single file no matter Export to One File in the General tab is checked or not.
* When you specify to publish the report result to the server resource tree, if the specified folder has a [real path](https://devnet.logianalytics.com/hc/en-us/articles/1500009717881-Getting-and-Using-Resources-from-a-Real-Path), the result will be put to the real path. Otherwise it will be put to the default disk location where server resources are.
* If you specify to publish the report result to a non-existent folder on disk, Logi JReport Server will automatically create it.

**Example 3: Publishing a report to e-mail**

Before you can e-mail the report result, an [e-mail server](https://devnet.logianalytics.com/hc/en-us/articles/1500009686782-Configuring-the-E-mail-Server) must have been predefined by the administrator.

In this example, you will learn how to set up a task to publish the report result to e-mail.

1. In the server resource tree in the Logi JReport Server console, select the report row, right-click in the row and select **Schedule** from the shortcut menu to display the Schedule dialog.
2. In the General tab, specify the general report settings.
3. In the Parameter tab, specify the parameter values as required if the report has parameters.
4. In the Publish tab, select the **To E-mail** sub tab, then from the Mail To list, select to whom the report result will be sent. If required, select the **Edit** button to edit the specified e-mail.

   If you want to create another e-mail, select the **New** button, then fill in [every field](https://devnet.logianalytics.com/hc/en-us/articles/1500009715061-Schedule#NewMail), select the format in which you want to export the report result and set the settings according to your requirements. When you choose to specify a report result as an attachment to e-mail, you need to specify a file name for the attachment. You can apply [dynamic names](https://devnet.logianalytics.com/hc/en-us/articles/1500009718721-Applying-Dynamic-Names-for-Published-Result-Files) for the result if necessary.
5. In the Conditions tab, select the **Time** sub tab, define the time zone from the Time Zone drop-down list, then from the Time Type drop-down list, choose **Run this task immediately**.
6. If you want to notify someone of when the task is finished by sending an e-mail, go to the Notification tab and set the settings.
7. If you want to specify a timeout for the task, specify the settings in the Duration tab as required.
8. Select **Finish** to have the task performed.

Then, select **My Tasks** on the system toolbar. When the task is being performed, you can see a record of it in the Running table and on completion it will be put into the Completed table.

**Example 4: Publishing a report to printer**

In this example, you will learn how to set up a task to publish the report result to a printer.

1. In the server resource tree in the Logi JReport Server console, select the report row, right-click in the row and select **Schedule** from the shortcut menu to display the Schedule dialog.
2. In the General tab, specify the general report settings.
3. In the Parameter tab, specify the parameter values as required if the report has parameters.
4. In the Publish tab,
   1. Select the  **To Printer** sub tab and then check **Publish to Printer**.
   2. Select a JDK print method for the report result in the Select Print Method field.
   3. Type a name with the path of the printer in the Printer field.
   4. Specify other [options](https://devnet.logianalytics.com/hc/en-us/articles/1500009715061-Schedule#Printer) according to your requirements.
5. In the Conditions tab, select the **Time** sub tab, define the time zone from the Time Zone drop-down list, then from the Time Type drop-down list of the Time tab, choose **Run this task immediately**.
6. If you want to notify someone of when the task is finished by sending an e-mail, go to the Notification tab and set the settings.
7. If you want to specify a timeout for the task, specify the settings in the Duration tab as required.
8. Select **Finish** to have the task performed.

Then, select **My Tasks** on the system toolbar. When the task is being performed, you can see a record of it in the Running table and on completion it will be put into the Completed table.

**Note:** When there is no printer connected with Logi JReport Server, and you schedule to publish a report to a printer, the server may crash or throw an exception.

**Example 5: Publishing a report to fax**

Before you can fax the report result, the [fax settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009686762-Configuring-Export-Settings#Fax)  must have been predefined by the administrator.

In this example, you will learn how to set up a task to publish the report result to fax.

1. In the server resource tree in the Logi JReport Server console, select the report row, right-click in the row and select **Schedule** from the shortcut menu to display the Schedule dialog.
2. In the General tab, specify the general report settings.
3. In the Parameter tab, specify the parameter values as required if the report has parameters.
4. In the Publish tab, select the **To Fax** sub tab, check the **Publish to Fax** option and then fill in [every field](https://devnet.logianalytics.com/hc/en-us/articles/1500009715061-Schedule#Fax) and set the settings according to your requirements.
5. In the Conditions tab, select the **Time** sub tab, define the time zone from the Time Zone drop-down list, then from the Time Type drop-down list, choose **Run this task immediately**.
6. If you want to notify someone of when the task is finished by sending an e-mail, go to the Notification tab and set the settings.
7. If you want to specify a timeout for the task, specify the settings in the Duration tab as required.
8. Select **Finish** to have the task performed.

Then, select **My Tasks**  on the system toolbar. When the task is being performed, you can see a record of it in the Running table and on completion it will be put into the Completed table.

**Example 6: Publishing a report to an FTP site**

In this example, you will learn how to set up a task to publish the report result to an FTP site.

1. In the server resource tree in the Logi JReport Server console, select the report row, right-click in the row and select **Schedule** from the shortcut menu to display the Schedule dialog.
2. In the General tab, specify the general report settings.
3. In the Parameter tab, specify the parameter values as required if the report has parameters.
4. In the Publish tab,
   1. Select the **To FTP**  sub tab.
   2. Select the **New** button to set up a new FTP site or select the **Edit** button to edit a specified FTP site in the FTP To list.
   3. Fill in [every field](https://devnet.logianalytics.com/hc/en-us/articles/1500009715061-Schedule#FTP), select the format in which you want to send the report result and then set the settings according to your requirements.
5. In the Conditions tab, select the **Time** sub tab, define the time zone from the Time Zone drop-down list, then from the Time Type drop-down list, choose **Run this task immediately**.
6. If you want to notify someone of when the task is finished by sending an e-mail, go to the Notification tab and set the settings.
7. If you want to specify a timeout for the task, specify the settings in the Duration tab as required.
8. Select **Finish** to have the task performed.

Then, select **My Tasks**  on the system toolbar. When the task is being performed, you can see a record of it in the Running table and on completion it will be put into the Completed table.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692482-Scheduling-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718701-Scheduling-a-Task-Containing-a-Bursting-Report)
