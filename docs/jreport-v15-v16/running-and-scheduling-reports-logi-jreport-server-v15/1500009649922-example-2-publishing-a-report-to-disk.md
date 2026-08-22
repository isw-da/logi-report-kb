---
title: "Example 2: Publishing a Report to Disk "
id: 1500009649922
section: "Running and Scheduling Reports Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009649922-Example-2-Publishing-a-Report-to-Disk
updated_at: 2021-07-24T20:53:43Z
---

# Example 2: Publishing a Report to Disk 

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674781-Example-1-Publishing-a-Report-to-the-Versioning-System)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674761-Example-3-Publishing-a-Report-to-E-mail)

# Example 2: Publishing a Report to Disk

In this example, you will learn how to set up a task to publish the report result in various file formats to the file system repeatedly at the start of each month.
It is not available to [organization users](https://devnet.logianalytics.com/hc/en-us/articles/1500009675081-Multi-tenancy-Supported-via-Organizations).

1. On the Logi JReport Console > Resources page, select the report row, right-click in the row and select **Schedule** from the shortcut menu to display the Schedule dialog.
2. In the General tab, specify the general report settings.
3. In the Parameter tab, specify the parameter values as required if the report has parameters.
4. In the Publish tab, select the **To Disk** sub tab, check **Publish to Disk**, then select the required formats, specify the result locations, and set the format settings according to your requirements. You can apply [dynamic names](https://devnet.logianalytics.com/hc/en-us/articles/1500009674821-Applying-Dynamic-Names-for-Published-Result-Files) for the result if necessary.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920423831/sch_pub_disk.gif)
5. In the Conditions tab,
   1. In the Time sub tab, define the time zone from the Time Zone drop-down list, then from the Time Type drop-down list, choose **Run this task periodically**.

      ![](https://devnet.logianalytics.com/hc/article_attachments/4404920424343/wkrpt_sch_dlg_file.gif)
   2. In the Duration box, specify a time period for when the task will be performed.
   3. Select **Monthly** from the Date drop-down list and keep the default to run the first day of every 1 month.
   4. Keep the Time settings as default.
6. If you want to notify someone of when the task is finished by sending an e-mail, go to the Notification tab and set the settings.
7. Select **Finish** to have the task performed.

Then, select **My Tasks** on the system toolbar, you will see that the scheduled task has been recorded in the Scheduled table. Since you have not specified the duration *Run until a time* for this task, it will not stop being performed until you delete or disable it from the Scheduled table.

**Notes:**

* When scheduling to publish a page report to disk, the Page Report Result and Logi JReport Result formats are based on the report level, that is, the report with all selected report tabs will be output to a single file no matter Export to One File in the General tab is checked or not.
* When you specify to publish the report result to the server resource tree, if the specified folder has a [real path](https://devnet.logianalytics.com/hc/en-us/articles/1500009648902-Getting-and-Using-Resources-from-a-Real-Path), the result will be put to the real path. Otherwise it will be put to the default disk location where server resources are.
* If you specify to publish the report result to a non-existent folder on disk, Logi JReport Server will automatically create it.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674781-Example-1-Publishing-a-Report-to-the-Versioning-System)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674761-Example-3-Publishing-a-Report-to-E-mail)
