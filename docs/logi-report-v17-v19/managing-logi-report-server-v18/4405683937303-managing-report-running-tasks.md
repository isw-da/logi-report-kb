---
title: "Managing Report-Running Tasks"
id: 4405683937303
section: "Managing Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683937303-Managing-Report-Running-Tasks
updated_at: 2022-01-27T07:59:39Z
---

# Managing Report-Running Tasks

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683943191--Advanced-Version-Topics-About-Version-Structure-and-Storage)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683923735-Managing-Server-Data)

# Managing Report-Running Tasks

This topic describes how you can view and manage report-running tasks on Logi Report Server.

You can perform the following fundamental report-running tasks on Server: quickly view a report (Run), view a report using selected options and parameters (Advanced Run), and schedule a report to run unattended at a specific time or periodically (Schedule).

You can view the status of these report-running tasks, such as scheduled tasks that are waiting to be performed by Logi Report Server, the tasks that are currently being performed, and the tasks that have already been performed.

This topic contains the following sections:

* [Accessing the Task Information Tables](#Access)
* [Managing Report-Running Tasks in the Task Tables](#Manage)
* [Task-Level Timeout for Advanced Run and Schedule Tasks](#Timeout)

## Accessing the Task Information Tables

Server collects task information and manages it in a set of tables.

* Server displays the tasks that you [scheduled](https://devnet.logianalytics.com/hc/en-us/articles/4405690676119-Scheduling-Reports) in the following tables:
  + **[Scheduled table](#Scheduled)**  
     Status information of scheduled tasks that are waiting to perform, such as task ID, whether the task is enabled, previous running time, and next running time.
  + **[Running table](#Running)**  
     Status information of tasks that are currently being performed, such as task ID, time when the task was started, and engine status.
  + **[Completed table](#Completed)**  
     Status information of tasks that have already been performed, such as task ID, time when the task was completed, whether the task performed successfully, result files, and error messages.
* Server displays the tasks that you performed using [Run, Advanced Run, or Background Run](https://devnet.logianalytics.com/hc/en-us/articles/4405690675223-Running-Reports) in the Background Tasks table.
  + **[Background Tasks table](#Background)**  
     Status information of the tasks that you Run, Advanced Run, or Background Run reports, such as report path and name, catalog path and name, running format, time when the task was started/completed, time elapsed since the task was performed, and the status of the task.

To access a specific table, on the Server Console select **My Tasks** on the system toolbar, then select the corresponding tab. You can also use [URL commands](https://devnet.logianalytics.com/hc/en-us/articles/4405684055959-Working-with-Server-via-URL#Schedule) to directly open a task table.

![My Tasks Page](https://devnet.logianalytics.com/hc/article_attachments/4420461537687/wkrpt_sch_vwrst1.gif)

The following introduces the task tables.

**Scheduled table**

The Scheduled table consists of the following columns:

| Column | Description |
| --- | --- |
| Schedule Name | The name of the schedule task. |
| Task ID | The internal ID for this task, which is a unique time stamp. |
| Report | The report path, name, and its status. |
| Report Tabs | The names of the report tabs in the report that this task included. |
| Next Run Time | The next scheduled time for when this task is to perform. |
| Last Run Time | The last scheduled time this task was performed. |
| Task Type | The type of task, such as Versioning System, File System, E-mail, or Printer. |
| Is Enabled | Show whether this task is enabled. It can be Enabled or Disabled. |
| Is Successful | Show whether the last running of this task performed successfully. The value **true** means that the last running performed successfully and **false** means the task failed. If the column is empty, the task has not run before. |
| Catalog | The catalog path and name that the report belongs to. |
| Launch Type | The way in which this task is executed, such as Repeatedly or One Time. |
| Requester | The user who submitted this task. |

**Running table**

The Running table consists of the following columns:

| Column | Description |
| --- | --- |
| Schedule Name | The name of the scheduled task. |
| Task ID | The internal ID for this task (a unique time stamp). |
| Report | The report path and name. |
| Report Tabs | The names of the report tabs in the report that this task included. |
| Start Time | The time when this task was started. |
| Task Type | The type of the task, such as Versioning System, File System, E-mail, or Printer. |
| Catalog | The catalog path and name that the report belongs to. |
| Launch Type | The way in which this task is executed, such as Repeatedly, One Time, or Instant. |
| Requester | The user who submitted this task. |
| Parameter File | The parameter file name. You can select the underlined file name to view the parameter values. |
| Parameters | The list of parameter values according to the size you specified. To specify the size, select **Preferences** on the task bar, then in the Preferences dialog box, set a value for the **Parameter Display Size** option. |
| Engine Status | The current status of Logi Report Engine, such as record fetching, grouping, memory paging, and engine initializing. |

**Completed table**

The Completed table consists of the following columns:

| Column | Description |
| --- | --- |
| Schedule Name | The name of the scheduled task. |
| Task ID | The internal ID for this task (a unique time stamp). |
| Is Successful | Show whether this task performed successfully. The value **true** means that the task performed successfully and **false** that the task failed. |
| Report | The report path and name. |
| Report Tabs | The names of the report tabs in the report that this task included. |
| Completed Time | The time when this task was completed. |
| Task Type | The type of task, such as Versioning System, File System, E-mail, or Printer. |
| Catalog | The catalog path and name that the report belongs to. |
| Launch Type | The way in which this task is executed, such as Repeatedly, One Time, or Instant. |
| Requester | The user who submitted this task. |
| Parameter File | The parameter file name. You can select the underlined file name to view the parameter values. |
| Parameters | The list of parameter values according to the size you specified. To specify the size, select **Preferences** on the task bar, then in the Preferences dialog box, set a value for the **Parameter Display Size** option. |
| Engine Status | The status of Logi Report Engine when the task was completed, such as record fetching, grouping, memory paging, and engine initializing. When a task fails to perform, here you can see the status of the engine at the time of the error. |
| Error Message | The error message for when the task failed to complete. |
| Result Files | The report result file names and links to the report result files. |

**Background Tasks table**

Server provides a background running system, which shows the status information of tasks that you submitted using the Run, Advanced Run, or Background Run mode.

Server clears the records that it saved in the background running system under the following conditions:

* Logi Report Server restarts.
* The maximum time limit specified for the report result life is reached. By default, it is 86400 seconds (24 hours).
* The maximum time limit specified for the interval between a user signs out and signs in is reached. By default, it is 300 seconds.
* If the number of records exceeds the number specified for the background task list (by default it is 100 records), Server only retains the latest 100 records.

The Background Tasks table consists of the following columns:

| Column | Description |
| --- | --- |
| Report Tabs | The names of the report tabs in the report that this task included. |
| Result | The result in the format in which the report ran. You can select the format link to open the report result. For a Page Report result, Server removes the task automatically once you opened the result. |
| Report | The path and name of the report that the report tabs belong to. |
| Start Time | The time when this task was started. |
| Finish Time | The time when this task was completed. |
| Status | The status of the task. |
| Catalog | The path and name of the catalog that the report belongs to. |
| Elapse Time | The time elapsed since the start of this task. |
| Catalog Version Number | The version number of the catalog that the report belongs to. |
| Report Version Number | The version number of the report. |
| Parameters | The parameters of the report. |
| Cancelled | Shows whether the task is cancelled or not. |

**Tips:**

* You can customize the columns in the tables: switch to the table, select **Preferences** on the task bar of the My Tasks page (for the **Scheduled** table, select **Tools** > **Preferences** on the task bar), select the corresponding items in the Preferences dialog box, then select **OK** to apply the settings.
* You can sort the records in each table in the ascending or descending order by any column title. To do this, select on the underlined column title on which you want to sort the records. Server displays a sort icon right after the title, showing the sort direction.
* You can use the Search box above each of the tables to search for the desired tasks in this table. Type the text of the schedule names or report tabs in the box and Server lists the tasks that contain the matched text.

## Managing Report-Running Tasks in the Task Tables

You can manage tasks in the task tables, for example, you can run a scheduled task immediately, or stop a running task.

**Management operations that are common to the task tables**

| If you want to | Then do |
| --- | --- |
| Select a task | Select in the row that the task is in. |
| Select multiple tasks | Select the rows that the tasks are in while holding the Ctrl button. |
| Remove a task | Choose one of the following ways:  * Select the task row and select **Edit > Delete** on the task bar of the My Tasks page. * Select the task row, right-click in the row, and select **Delete** from the shortcut menu. * Put the mouse pointer over the task row and select the **Delete** button Delete button on the floating toolbar. |

**Management operations for the Scheduled table**

| If you want to | Then do |
| --- | --- |
| Create a new schedule task | 1. Select **New Schedule** on the task bar of the My Tasks page. Server displays the New Schedule dialog box. 2. Specify how to create the task: [by selecting a report](https://devnet.logianalytics.com/hc/en-us/articles/4405684005015-Scheduling-Tasks-to-Run-Reports) or [by importing a script file](https://devnet.logianalytics.com/hc/en-us/articles/4405684008855-Importing-and-Exporting-Scheduled-Tasks). |
| Run a task immediately | Choose one of the following ways:  * Select the task row and select **Run** on the task bar of the My Tasks page. * Select the task row, right-click in the row, and select **Run** from the shortcut menu. * Put the mouse pointer over the task row and select the **Run** button Run button on the floating toolbar. |
| Duplicate a task | Choose one of the following ways:  * Select the task row and select **Edit** >  **Copy** on the task bar of the My Tasks page. * Select the task row, right-click in the row, and select **Copy** from the shortcut menu. * Put the mouse pointer over the task row and select the **Copy** button Copy button on the floating toolbar. |
| Enable a task | Choose one of the following ways:  * Select the task row and select **Edit** >  **Enable** on the task bar of the My Tasks page. * Select the task row, right-click in the row, and select **Enable** from the shortcut menu. * Put the mouse pointer over the task row and select the **Enable** button Enable button on the floating toolbar. |
| Disable a task | Choose one of the following ways:  * Select the task row and select **Edit** >  **Disable** on the task bar of the My Tasks page. * Select the task row, right-click in the row, and select **Disable** from the shortcut menu. * Put the mouse pointer over the task row and select the **Disable** button Disable button on the floating toolbar.   Server does not perform the disabled task until you enable it again. |
| Export a schedule task to a script file on disk | For more information, see [Importing and Exporting Scheduled Tasks](https://devnet.logianalytics.com/hc/en-us/articles/4405684008855-Importing-and-Exporting-Scheduled-Tasks). |
| Import a script file saved on disk to create a schedule task | For more information, see [Importing and Exporting Scheduled Tasks](https://devnet.logianalytics.com/hc/en-us/articles/4405684008855-Importing-and-Exporting-Scheduled-Tasks). |

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)

* You can perform the Run action on a disabled scheduled task.
* When you copy a disabled scheduled task or export it to script, Server does not include the disabled state since it is not a property of the task.

**Management operations for the Running table:**

| If you want to | Then do |
| --- | --- |
| Stop a task that is running | Choose one of the following ways:  * Select the task row and select **Stop** on the task bar of the My Tasks page. * Select the task row, right-click in the row, and select **Stop** from the shortcut menu. * Put the mouse pointer over the task row and select the **Stop** button Stop button on the floating toolbar.   Note iconWhen you stop a bursting task from running, some sub tasks in the bursting task may have already finished, so Server may have sent some results to some recipients. |
| View parameter information | See the Parameters column of the Running table. |

**Management operations for the Completed table**

| If you want to | Then do |
| --- | --- |
| View detailed task run information | Choose one of the following ways:  * Select the schedule name of the task. * Select the task row and select **Edit** > **Details** on the task bar of the My Tasks page. * Select the task row, right-click in the row, and select **Details** from the shortcut menu. * Put the mouse pointer over the task row and select the **Details** button Details button on the floating toolbar.   Server displays the Result Details table which contains the following columns:   | Column | Description | | --- | --- | | Task ID | The task ID. | | Report | The Report on which the task is based. | | Publish Type | Publish types of the task. | | Result | Results of the task. For results of the **To Version** publish type, you can select the format links to view the results. See [Viewing Results Scheduled to Version](https://devnet.logianalytics.com/hc/en-us/articles/4405684011031-Viewing-Scheduled-Report-Results#Version) for more information. | | Is Successful | Display whether the task is successful. | | Details | Locations of the results. | |
| View parameter information | See the Parameters column of the Completed table. |

**Management operations for the Background Tasks table**

| If you want to | Then do |
| --- | --- |
| Stop a running task that you submitted using Background Run mode | Choose one of the following ways:  * Select the task row and select **Edit > Stop** on the task bar of the My Tasks page. * Select the task row, right-click in the row, and select **Stop** from the shortcut menu. * Put the mouse pointer over the task row and select the **Stop** button Stop button on the floating toolbar. |
| Restart a stopped task | Choose one of the following ways:  * Select the task row and select **Edit > Restart** on the task bar of the My Tasks page. * Select the task row, right-click in the row and select **Restart** from the shortcut menu. * Put the mouse pointer over the task row and select the **Restart** button Restart button on the floating toolbar. |
| View parameter information | See the Parameters column of the Background Tasks table. |

## Task-Level Timeout for Advanced Run and Schedule Tasks

Server introduces the task-level timeout mechanism to avoid the never-finished running tasks consuming server resources and thus decreasing the server performance. With the mechanism, you can specify a time duration for a task, and ask Server to cancel the task or to notify you or someone else of the task status via email if the task has not yet finished running when the task duration is up. To do this:

1. Do either of the following to enable the task-level timeout mechanism.
   * In the **server.properties** file in `<install_root>\bin`, set the **task.duration.enable** property to **true**.
   * On the system toolbar of the Server Console, navigate to **Administration** > **Configuration** > **Advanced**. Server displays the Advanced page. Select **Enable Task Duration**.
2. By default, Server checks task duration every 30 seconds. You can reset the period value by either of the following:
   * In the **server.properties** file, set the **task.duration.check\_cycle** property.
   * In the Administration > Configuration > Advanced page, set the **Status Refresh Interval** option.

   The period value must be an integer greater than 0. Since task duration check frequency affects server performance, you should set the value according to your system environment.
3. Use the **Duration** tab in the Advanced Run or Schedule dialog box to specify task duration.

   ![Duration tab](https://devnet.logianalytics.com/hc/article_attachments/4420461587479/advcdrn_drtn.gif)

   1. In the **Timeout** text box, specify the time limit for when the task can run before notifying of the timeout or canceling the task.
   2. If you want to notify someone of the task status if the task has not yet finished running when the task duration is up, select **Notify by e-mail after the specified time** and specify the email address in the **Mail To** text box.
   3. If you want Server to cancel the task when the task duration is up but the task has not finished yet, select **Cancel the task after the specified time**.
4. Submit the task.

Then, when the specified task duration is up but the task has not finished running,

* **For an Advanced Run task**
  + If you have specified to have server cancel the task when the task duration is up, the task will be cancelled automatically, however, a record for the task will be still remained in the Background Tasks table of the My Tasks page, shown with a sign of cancellation.
  + In the Duration tab, if you have not selected the option Cancel the task after the specified time, the task will be switched to run in background mode when the task duration is up, in which case, you can choose to cancel the task manually. To do this, in the Background Tasks table,
    - Select the task row and click **Edit > Delete** on the task bar of the My Tasks page.
    - Select the task row, right-click in the row and select **Delete** from the shortcut menu.
    - Put the mouse pointer over the task row and select the **Delete** button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420461456151/btn_dltobj.gif) on the floating toolbar.
* **For a Schedule task** 
  + If you have specified to have server cancel the task when the task duration is up, Server cancels the task automatically, and adds a task completed record in the Completed table of the My Tasks page, with the Is Successful status being No.
  + In the **Duration** tab, if you have not selected **Cancel the task after the specified time**, Server still lists the task in the Running table of the My Tasks page when the task duration is up. Then, if you want to cancel the task manually, do one of the following in the Running table,
    - Select the task row and select **Stop** on the task bar of the My Tasks page.
    - Select the task row, right-click in the task row, and select **Stop** from the shortcut menu.
    - Put the mouse pointer over the task row and select the **Stop** button ![Stop button](https://devnet.logianalytics.com/hc/article_attachments/4420447181207/btn_srv_stop.gif) on the floating toolbar.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)

* Server may not cancel a task right after the specified task duration is up due to check frequency.
* You should set the task duration to about five times of the required time for finishing running the task.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683943191--Advanced-Version-Topics-About-Version-Structure-and-Storage)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683923735-Managing-Server-Data)
