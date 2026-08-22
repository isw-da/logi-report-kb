---
title: "Scheduling to Run Multiple Reports"
id: 1500009778461
section: "Scheduling Tasks to Run Reports"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009778461-Scheduling-to-Run-Multiple-Reports
updated_at: 2021-07-24T00:47:39Z
---

# Scheduling to Run Multiple Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778481-Scheduling-to-Run-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778441-Examples-of-Scheduling-Reports)

# Scheduling to Run Multiple Reports

For page reports and web reports that are in the same folder in the server resource tree and use the same catalog, you can schedule to run them all at a time. This topic describes how you can schedule to run multiple reports.

However, in this case, you can only publish the report results to Logi Report Server's versioning system and by e-mail.

1. In the Resources page of the Server Console, browse to the folder that contains the reports you want to schedule to run.
2. Select the reports to be scheduled, then do either of the following:
   * Select **Run** > **Schedule** on the task bar of the Resources page.
   * Right-click in any of the selected report row and select **Schedule** from the shortcut menu.

   Server displays the
   [Schedule](https://devnet.logianalytics.com/hc/en-us/articles/1500009774581-Schedule-Dialog-Box-Properties) dialog box.
3. In the General tab, type the name for the task in the Schedule Name text box and specify the priority of the task as required. You can expand the top section to view the details about the reports included in the schedule task.

   ![Schedule dialog - General tab for multiple reports](https://devnet.logianalytics.com/hc/article_attachments/4404885371287/wkrpt_sch_dlg_mtpl1.gif)
4. In the Parameter tab, [specify the parameter values](https://devnet.logianalytics.com/hc/en-us/articles/1500009778361-Specifying-Parameter-Values) if the reports have parameters. All the parameters used in the selected reports are listed in the tab.
5. In the Publish tab, specify the types of the task: To Version and To E-mail, then select the result formats for each task type and set the format settings as required. For more information about the task types, see the examples in [Examples of Scheduling Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009778441-Examples-of-Scheduling-Reports).

   ![Schedule dialog - Publish tab for multiple reports](https://devnet.logianalytics.com/hc/article_attachments/4404885371543/wkrpt_sch_dlg_mtpl2.gif)
6. Specify the settings in the Conditions, Notification and Duration tabs as you would do when [scheduling to run a single report](https://devnet.logianalytics.com/hc/en-us/articles/1500009778481-Scheduling-to-Run-a-Report#Condition).
7. Select **Finish**, and Logi Report Server will then perform the task.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778481-Scheduling-to-Run-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778441-Examples-of-Scheduling-Reports)
