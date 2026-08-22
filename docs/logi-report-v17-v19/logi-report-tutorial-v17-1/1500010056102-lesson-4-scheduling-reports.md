---
title: "Lesson 4: Scheduling Reports"
id: 1500010056102
section: "Logi Report Tutorial v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010056102-Lesson-4-Scheduling-Reports
updated_at: 2021-07-23T19:14:17Z
---

# Lesson 4: Scheduling Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856777623/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056082-Lesson-3-Running-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404848352023/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093121-Lesson-5-Administration-of-Logi-Report-Server)

# Lesson 4: Scheduling Reports

In [Lesson 3](https://devnet.logianalytics.com/hc/en-us/articles/1500010056082-Lesson-3-Running-Reports) of this track, we ran published reports by using the Run and Advanced Run commands in the Server Console. Reports run in this way are on-demand reports. By contrast, Server also enables reports to be scheduled, that is, automatically run at one or more designated dates and times. Scheduled reports can greatly improve the performance of the reporting service in an organization. For example, you can run reports during low network traffic times. Scheduled reports can also capture a time period exactly, for example, the last day of the quarter.

Server does not deliver a scheduled report to an end user in the same way as it delivers an on-demand report. There are six destinations for scheduled reports:

* Versioning System
* File System
* E-mail
* Printer
* Fax
* FTP

In this lesson, we explore three of these:

* [Example 1: Publish a Report to the Versioning System](#Example1)
* [Example 2: Publish a Report to the File System](#Example2)
* [Example 3: Publish a Report to the Printer](#Example3)

## Example 1: Publish a Report to the Versioning System

The built-in versioning system is a virtual file system that Server maintains.

In this example, we set up a schedule to run a report immediately and ask Server to keep the generated result for 7 days. Even though we run the task immediately, we schedule to run the report through the Server scheduling system. This has two advantages, the user does not need to wait for the report to finish to continue using their system and Server runs the report in the background so does not impact other users who are running interactive reports. Another advantage of scheduling a report is that Server saves it in the versioning system; while normally Server does not save on-demand reports in the versioning system unless explicitly saved by the user.

1. In the Resources page of the Server Console, go to the **Public Reports** > **JinfonetGourmetJava** folder.
2. Put the mouse pointer over the **OrderListbyDate\_Parameter.cls** report row, then select the **Schedule** button ![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4404857175703/btn_schdl.gif) on the floating toolbar.

   Server displays the **General** tab of the Schedule dialog box. It selects the report tab OrderDetails by default.

   ![Schedule - General](https://devnet.logianalytics.com/hc/article_attachments/4404857176215/admin_lsn4_rpttab.gif)
3. Type **ToVersion** in the **Schedule Name** text box. Keep the default settings for other options in the tab.
4. Select **Next** to go to the **Parameter** tab. You can specify new parameter values or keep the default values.
5. Select **Next**.
6. In the **Publish** tab, select **To Version** and then select **Publish to Versioning System**.

   Server displays the publishing options:

   ![Publish to Version](https://devnet.logianalytics.com/hc/article_attachments/4404848802071/admin_lsn4_2vrsn.gif)
7. Select the **Page Report Result** format, select the **Result Auto-delete** checkbox and set **Result Expires in 7 Days**.
8. Switch to the **Conditions** tab to specify the time when the task is to be performed.
9. In the **Time** sub tab, keep the default selection, **Run this task immediately**, in the **Time Type** drop-down list. The **Time Zone** option should represent your current time zone.
10. Select **Finish** to submit the task.

You can monitor the status of the report by viewing the My Tasks page (to access this page, select **My Tasks** on the system toolbar). Server lists the reports that are running in the Running table; when they complete running, Server moves them to the Completed table. Server lists the reports which are scheduled but have not yet run in the Scheduled table.

In this example, we publish the report result to the built-in version folder of the report. We can view the report result as follows:

1. Put the mouse pointer over the **OrderListbyDate\_Parameter.cls** report row, then select the **Version** button ![Version button](https://devnet.logianalytics.com/hc/article_attachments/4404848802327/btn_vrsn.gif) on the floating toolbar.
2. In the **Report Result Versions** table, select the **Page Report Result** link in the **Result** column. Server displays the full page report result.

   ![port Result Version](https://devnet.logianalytics.com/hc/article_attachments/4404857176599/admin_lsn4_rst.gif)

## Example 2: Publish a Report to the File System

In this example, we set up a schedule to output a weekly sales report to the file system. We specify to run the report every Sunday night so it is available first thing on Monday morning.

1. In the Resources page of the Server Console, go to the **Public Reports** > **JinfonetGourmetJava** folder.
2. Put the mouse pointer over the **CustomerContactCard.cls** report row, then select the **Schedule** button ![Schedult button](https://devnet.logianalytics.com/hc/article_attachments/4404857175703/btn_schdl.gif) on the floating toolbar.
3. In the **General** tab, type **ToPDF** as the schedule name.
4. Select the **Publish** > **To Disk** tab, and then select **Publish to Disk**.
5. Select **PDF**. Server displays the PDF options.

   ![Publish to Disk](https://devnet.logianalytics.com/hc/article_attachments/4404848802711/admin_lsn4_2pdf.gif)
6. Keep the default location selection, **Publish to Server Resource Tree**, then type **/CustomerContactCard.pdf** in the text box below the location drop-down list. This publishes the report to the disk path of the server resource tree under the name CustomerContactCard.pdf.

   The server disk path is `<install_root>\jreports` by default, thus if we want to place the output file in this folder, the path must start with a "/". Alternatively, we can type a full disk path if we want to create the file outside of the server resource tree, for example, `C:\temp\CustomerContactCard.pdf`.
7. Select the **Conditions** tab to specify the time when to perform the task.
8. In the **Time** sub tab, choose **Run this task periodically** from the **Time Type** drop-down list. Select **Weekly** from the **Date** drop-down list and define to repeat every one week on **Sunday**. Select **At** from the **Time** drop-down list and specify the time as **8:00 PM**.

   ![Time Condition](https://devnet.logianalytics.com/hc/article_attachments/4404857177751/admin_lsn4_time.gif)

   Although we do not use it in this lesson, the Notification tab enables you to specify e-mail notifications to be sent automatically when the report finishes running or if it is unable to complete successfully.
9. Select **Finish** to submit the scheduled report request.

Since it isn't practical to wait until Sunday night to view the report in our lesson, we cheat a bit and request an early version of the report.

1. In the Server Console, select **My Tasks** on the system toolbar. Server should display the report we requested above as a scheduled task.
2. Put the mouse pointer over the task and select **Run** button ![Run button](https://devnet.logianalytics.com/hc/article_attachments/4404848802967/btn_run.gif) on the floating toolbar to immediately schedule the report.

   ![Scheduled Task Table](https://devnet.logianalytics.com/hc/article_attachments/4404848803479/admin_lsn4_task.gif)

   Now we can find the report result file "CustomerContactCard.pdf" using Windows Explorer in `<install_root>\jreports\`.

## Example 3: Publish a Report to the Printer

In this example, we set up a schedule to output a form letter report to the printer on a monthly basis. We specify to send the form letter to delinquent customers.

1. In the Resources page of the Server Console, go to the **Public Reports** > **JinfonetGourmetJava** folder.
2. Put the mouse pointer over the **ProductSalesAnalysis.cls** report row, then select the **Schedule** button ![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4404857175703/btn_schdl.gif) on the floating toolbar.
3. In the **General** tab, type **ToPrinter** as the schedule name.
4. Select the **Publish** > **To Printer** tab, then select **Publish to Printer**.
5. Fill out the tab according to your requirements and the printer settings.

   ![Publish to Printer](https://devnet.logianalytics.com/hc/article_attachments/4404848803991/admin_lsn4_prntr.gif)
6. Select the **Conditions** tab, and then select the **Time** sub tab to specify the time when the task is to be performed.
7. From the **Time Type** drop-down list, choose **Run this task periodically**, select **Monthly** from the **Date** drop-down list and select to run the task on **The 1st day of every 2 months** at **7:00 AM**.

   ![Time Condition](https://devnet.logianalytics.com/hc/article_attachments/4404857178391/admin_lsn4_monthly.gif)
8. Select **Finish** to submit the scheduled report request.
9. Select **My Tasks** on the system toolbar. Server lists the task in the **Scheduled** table. You probably want to delete this entry so Server does not print the report to your printer every month!

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856777623/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056082-Lesson-3-Running-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404848352023/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093121-Lesson-5-Administration-of-Logi-Report-Server)
