---
title: "Lesson 4: Scheduling Reports"
id: 1500011463561
section: "Logi JReport Tutorial v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011463561-Lesson-4-Scheduling-Reports
updated_at: 2021-07-24T10:39:42Z
---

# Lesson 4: Scheduling Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500011463581-Lesson-3-Running-Reports) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901097111/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011431522-Lesson-5-Administration-of-Logi-JReport-Server)

# Lesson 4: Scheduling Reports

In [Lesson 3](https://devnet.logianalytics.com/hc/en-us/articles/1500011463581-Lesson-3-Running-Reports) of this track we ran published reports by using the Run and Advanced Run commands on the server console. Reports run in this way are on-demand reports. By contrast, Logi JReport Server also allows reports to be scheduled, that is, automatically run at one or more designated dates and times. Scheduled reports can greatly improve the performance of the reporting service in an organization. For example, reports can be run during low network traffic times. Scheduled reports can capture a time period exactly, for example the last day of the quarter.

A scheduled report is not delivered to an end user in the same way an on-demand report is. There are six destinations for scheduled reports:

* Publish to Versioning System
* Publish to File System
* Publish to E-mail
* Publish to Printer
* Publish to Fax
* Publish to FTP

In this lesson, we explore three of these:

* [Example 1: Publishing a Report to the Versioning System](#Example1)
* [Example 2: Publishing a Report to the File System](#Example2)
* [Example 3: Publishing a Report to the Printer](#Example3)

## Example 1: Publishing a Report to the Versioning System

The built-in Logi JReport Server Versioning System is a virtual file system maintained by Logi JReport Server.

In this example, we will set up a schedule to run a report immediately and specify that the generated result be kept for 7 days. Even though we run the task immediately, the report is scheduled to run through the Logi JReport Server scheduling system. This has two advantages, the user does not need to wait for the report to finish to continue using their system and the report is run in the background so does not impact other users who are running interactive reports. Another advantage of scheduling a report is that it can be saved in the versioning system while normally on-demand reports will not be saved unless explicitly saved by the user.

1. In the Resources page of the server console, go to the **Public Reports** > **JinfonetGourmetJava** folder.
2. Put the mouse pointer over the **OrderListbyDate\_Parameter.cls** report row, then select the **Schedule** button ![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4404909107735/btn_schdl.gif) on the floating toolbar.

   The General tab of the Schedule dialog appears. The report tab OrderDetails is selected by default to be scheduled.

   ![Schedule - General](https://devnet.logianalytics.com/hc/article_attachments/4404901104279/admin_lsn4_rpttab.gif)
3. Enter **ToVersion** in the Schedule Name text field. Keep the default settings for other options in the tab.
4. Select **Next** to go to the Parameter tab. If desired, you can enter new parameter values or keep the default values.
5. Select **Next** to go to the Publish tab.
6. In the Publish tab, select **To Version** and then check **Publish to Versioning System**.

   The publishing options appear.

   ![Publish to Version](https://devnet.logianalytics.com/hc/article_attachments/4404901104535/admin_lsn4_2vrsn.gif)
7. Select the **Page Report Result** format, check the **Result Auto-delete** checkbox and set **Result Expires in 7 Days**.
8. Switch to the **Conditions** tab to specify the time when the task is to be performed.
9. In the Time sub tab, keep the default selection Run this task immediately in the Time Type drop-down list. The Time Zone field should represent your current time zone.
10. Select **Finish** to submit the task.

You can monitor the status of the report by viewing the My Tasks page (to access this page, select **My Tasks** on the system toolbar). Reports that are running are listed in the Running table; when complete they will be moved to the Completed table. Reports which are scheduled but have not yet run are listed in the Scheduled table.

In this example the report result is published to the built-in version folder of the report. We can view the report result as follows:

1. Put the mouse pointer over the **OrderListbyDate\_Parameter.cls** report row, then select the **Version** button ![Version button](https://devnet.logianalytics.com/hc/article_attachments/4404901104791/btn_vrsn.gif) on the floating toolbar.
2. In the Report Result Versions table, select the **Page Report Result**  link in the Result column. The full page report result is displayed.

   ![port Result Version](https://devnet.logianalytics.com/hc/article_attachments/4404901105047/admin_lsn4_rst.gif)

## Example 2: Publishing a Report to the File System

In this example, we set up a schedule to output a weekly sales report to the file system. The report is run every Sunday night so it will be available first thing on Monday morning.

1. In the Resources page of the server console, go to the **Public Reports** > **JinfonetGourmetJava** folder.
2. Put the mouse pointer over the **CustomerContactCard.cls** report row, then select the **Schedule** button ![Schedult button](https://devnet.logianalytics.com/hc/article_attachments/4404909107735/btn_schdl.gif) on the floating toolbar.
3. In the General tab, enter **ToPDF** as the schedule name.
4. Select the **Publish** > **To Disk** tab, and then check **Publish to Disk**.
5. Check **PDF**. The PDF options appear.

   ![Publish to Disk](https://devnet.logianalytics.com/hc/article_attachments/4404901105303/admin_lsn4_2pdf.gif)
6. Keep the default location selection Publish to Server Resource Tree and enter **/CustomerContactCard.pdf** in the text box below the location drop-down list. This publishes the report to the server resource tree under the name /CustomerContactCard.pdf.

   The Server Disk Path is set by default to `<install_root>\jreports`, thus if we want to place the output file in this folder the path must start with a "/". Alternatively we can enter a full disk path if we want the file to be created outside of the server resource tree, for example, `C:\temp\CustomerContactCard.pdf`.
7. Select the **Conditions** tab to specify the time when the task is to be performed.
8. In the Time sub tab, choose **Run this task periodically** from the Time Type drop-down list. Select **Weekly** from the Date drop-down list and define to repeat every one week on **Sunday**. Select **At** from the Time drop-down list and specify the time as **8:00 PM**.

   ![Time Condition](https://devnet.logianalytics.com/hc/article_attachments/4404909107991/admin_lsn4_time.gif)

   Although we won't use it in this lesson, the Notification tab allows you to specify e-mail notifications to be sent automatically when the report is finished or if it was unable to complete successfully.
9. Select **Finish** to submit the scheduled report request.

Since it isn't practical to wait until Sunday night to view the report in our lesson, we're going to cheat a bit and request an early version of the report.

1. In the server console, select **My Tasks**  on the system toolbar. The report we requested above should appear as a scheduled task.
2. Put the mouse pointer over the task and select **Run** button ![Run button](https://devnet.logianalytics.com/hc/article_attachments/4404909108247/btn_run.gif) on the floating toolbar to immediately schedule the report.

   ![Scheduled Task Table](https://devnet.logianalytics.com/hc/article_attachments/4404909108503/admin_lsn4_task.gif)

   Now we can find the report using Windows Explorer in `<install_root>\jreports\CustomerContactCard.pdf`.

## Example 3: Publishing a Report to the Printer

In this example, we set up a schedule to output a form letter report to the printer on a monthly basis. The form letter is to be sent to delinquent customers.

1. In the Resources page of the server console, go to the **Public Reports** > **JinfonetGourmetJava** folder.
2. Put the mouse pointer over the **ProductSalesAnalysis.cls** report row, then select the **Schedule** button ![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4404909107735/btn_schdl.gif) on the floating toolbar.
3. In the General tab, enter **ToPrinter** as the schedule name.
4. Select the **Publish** > **To Printer** tab, then check **Publish to Printer**.
5. Fill out the tab according to your requirements and the printer settings.

   ![Publish to Printer](https://devnet.logianalytics.com/hc/article_attachments/4404901105559/admin_lsn4_prntr.gif)
6. Select the **Conditions** tab, and then select the **Time** sub tab to specify the time when the task is to be performed.
7. From the Time Type drop-down list, choose **Run this task periodically**, select **Monthly** from the Date drop-down list and select to run the task on **The 1st day of every 2 months** at **7:00 AM**.

   ![Time Condition](https://devnet.logianalytics.com/hc/article_attachments/4404909108759/admin_lsn4_monthly.gif)
8. Select **Finish** to enter the scheduled report request.
9. Select **My Tasks** on the system toolbar. The task is listed in the Scheduled table. You probably want to delete this entry so Logi JReport Server does not print the report to your printer every month!

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500011463581-Lesson-3-Running-Reports) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901097111/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011431522-Lesson-5-Administration-of-Logi-JReport-Server)
