---
title: "Accessing the Task Information Tables"
id: 1500009648922
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648922-Accessing-the-Task-Information-Tables
updated_at: 2021-07-24T20:54:02Z
---

# Accessing the Task Information Tables

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673681-Managing-Tasks)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648942-Managing-Tasks-in-the-Task-Tables)

# Accessing the Task Information Tables

Logi JReport Server collects task information and manages it in a set of tables.

* Tasks that are [scheduled](https://devnet.logianalytics.com/hc/en-us/articles/1500009674681-Scheduling-Reports)
  + **[Scheduled table](#Scheduled)**  
     Shows the status information of scheduled tasks that are waiting to be performed, such as task ID, whether the task is enabled, previous running time, and next running time.
  + **[Running table](#Running)**  
     Shows the status information of tasks that are currently being performed, such as task ID, time when the task was started, and engine status.
  + **[Completed table](#Completed)**  
     Shows the status information of tasks that have already been performed, such as task ID, time when the task was completed, whether or not the task was successfully performed, result files, and error messages.
* Tasks that are performed in the [Run, Advanced Run or Background Run mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009674661-Running-Reports)
  + **[Background Tasks table](#Background)**  
     Shows the status information of the tasks submitted using the Run, Advanced Run, or Background Run mode, such as report tab names, report path and name, catalog path and name, running format, time when the task was started/completed, time elapsed since the task was performed, and the status of the task.

To access a specific table, on the Logi JReport Console page, select **My Tasks** on the system toolbar, then select the corresponding tab. You can also use [URL commands](https://devnet.logianalytics.com/hc/en-us/articles/1500009650542-Working-with-Logi-JReport-Server-Guide-v15-Server#Schedule) to directly open a task table.

The following shows the columns that are displayed in each table in detail.

**Tips:**

* Some columns in the tables are not shown by default. To have them displayed, switch to the table, select **Preferences** on the task bar of the My Tasks page (for the Scheduled table, select **Tools** > **Preferences** on the task bar), check the corresponding items in the Preferences dialog, then select **OK** to save the settings.
* You can make the records in each of the tables sorted ascending or descending by any column title. To do this, just select on the underlined column title on which you want the records to be sorted, you will then find a sort icon appear right after the title, showing the sort direction.
* You can use the quick search toolbar above each of the tables to search for the desired tasks in this table. Type in the text of the schedule names or report tabs in the text box and the tasks containing the matched text will be listed.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Scheduled Table

The Scheduled table consists of the following columns:

| Column | Description |
| --- | --- |
| Schedule Name | The name of the schedule task. |
| Task ID | The internal ID for this task, which is a unique time stamp. |
| Report | The report path, name and its status. |
| Report Tabs | The names of the report tabs in the report that are included in this task. |
| Next Run Time | The next scheduled time for when this task is to be performed. |
| Last Run Time | The last scheduled time this task was performed. |
| Task Type | The type of task, such as Versioning System, File System, E-mail, or Printer. |
| Is Enabled | Shows whether this task is enabled. Can be Enabled or Disabled. |
| Is Successful | Shows whether or not the last running of this task was successfully performed. The value true means that the last running was performed successfully and false means the task failed. If the column is empty, the task has not been run before. |
| Catalog | The catalog path and name that the report belongs to. |
| Launch Type | The way in which this task is executed, such as Repeatedly or One Time. |
| Requester | The user who submitted this task. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Running Table

The Running table consists of the following columns:

| Column | Description |
| --- | --- |
| Schedule Name | The name of the scheduled task. |
| Task ID | The internal ID for this task (a unique time stamp). |
| Report | The report path and name. |
| Report Tabs | The names of the report tabs in the report that are included in this task. |
| Start Time | The time when this task was started. |
| Task Type | The type of the task, such as Versioning System, File System, E-mail, or Printer. |
| Catalog | The catalog path and name that the report belongs to. |
| Launch Type | The way in which this task is executed, such as Repeatedly, One Time, or Instant. |
| Requester | The user who submitted this task. |
| Parameter File | The parameter file name. You can select the underlined file name to view the parameter values. |
| Parameters | The list of parameter values according to the size specified. To specify the size, select **Preferences** on the task bar, then in the Preferences dialog, set a value for the Parameter Display Size option as required. |
| Engine Status | The current status of the Logi JReport engine, such as record fetching, grouping, memory paging, and engine initializing. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Completed Table

The Completed table consists of the following columns:

| Column | Description |
| --- | --- |
| Schedule Name | The name of the scheduled task. |
| Task ID | The internal ID for this task (a unique time stamp). |
| Is Successful | Shows whether this task was successfully performed. The value true means that the task was performed successfully and false that the task failed. |
| Report | The report path and name. |
| Report Tabs | The names of the report tabs in the report that are included in this task. |
| Completed Time | The time when this task was completed. |
| Task Type | The type of task, such as Versioning System, File System, E-mail, or Printer. |
| Catalog | The catalog path and name that the report belongs to. |
| Launch Type | The way in which this task is executed, such as Repeatedly, One Time, or Instant. |
| Requester | The user who submitted this task. |
| Parameter File | The parameter file name. You can select the underlined file name to view the parameter values. |
| Parameters | The list of parameter values according to the size specified. To specify the size, select **Preferences** on the task bar, then in the Preferences dialog, set a value for the Parameter Display Size option as required. |
| Engine Status | The status of Logi JReport Engine when the task was completed, such as record fetching, grouping, memory paging, and engine initializing. When a task fails to perform, here you can see the status of the engine at the time of the error. |
| Error Message | The error message for when the task failed to complete the task. |
| Result Files | The report result file names and links to the report result files. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Background Tasks Table

Logi JReport Server provides a background running system, which shows the status information of tasks submitted using the Run, Advanced Run, or Background Run mode. Status information includes: report name, report path and name, catalog path and name, running format, time when the task is started/completed, time elapsed since the task is performed, and the status of the task. It allows you to view detailed information in a timely fashion.

The records saved in the background running system are cleared under the following conditions:

* Logi JReport Server is restarted.
* The maximum time limit specified for the report result life has been reached. By default it is 86400 seconds (24 hours).
* The maximum time limit specified for the interval between a user logout and login has been reached. By default it is 300 seconds.
* If the number of records exceeds the number specified for the background task list (by default it is 100 records), the latest 100 records will be retained.

The Background Tasks table consists of the following columns:

| Column | Description |
| --- | --- |
| Report Tabs | The names of the report tabs in the report that are included in this task. |
| Result | The result in the format in which the report ran. |
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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673681-Managing-Tasks)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648942-Managing-Tasks-in-the-Task-Tables)
