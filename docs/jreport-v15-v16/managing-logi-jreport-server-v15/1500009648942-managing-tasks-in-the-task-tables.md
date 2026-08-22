---
title: "Managing Tasks in the Task Tables"
id: 1500009648942
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648942-Managing-Tasks-in-the-Task-Tables
updated_at: 2021-07-24T20:54:01Z
---

# Managing Tasks in the Task Tables

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648922-Accessing-the-Task-Information-Tables)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648962-Task-level-Timeout-for-Advanced-Run-and-Schedule-Tasks)

# Managing Tasks in the Task Tables

You can manage tasks in the task tables according to your requirements. For example, you can run a scheduled task immediately, or stop a running task.

Below is a list of the sections covered in this topic:

* [Performing Common Tasks](#Common)
* [Managing Tasks in the Scheduled Table](#Scheduled)
* [Managing Tasks in the Running Table](#Running)
* [Managing Tasks in the Completed Table](#Completed)
* [Managing Tasks in the Background Tasks Table](#Background)

## Performing Common Tasks

Some task management operations are common to the task tables.

| If you want to | Then do |
| --- | --- |
| Select a task | Select in the row that the task is in. |
| Select multiple tasks | Select the rows that the tasks are in while holding the Ctrl button. |
| Remove a task | * Select the task row and select **Edit > Delete** on the task bar of the My Tasks page. * Select the task row, right-click in the row and select **Delete** from the shortcut menu. * Put the mouse pointer over the task row and select the **Delete** button  on the floating toolbar. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Managing Tasks in the Scheduled Table

| If you want to | Then do |
| --- | --- |
| Create a new scheduled task | Select **New Schedule** on the task bar of the My Tasks page, then in the New Schedule dialog, specify how to create the task: [by selecting a report](https://devnet.logianalytics.com/hc/en-us/articles/1500009649902-Scheduling-Tasks-to-Publish-Reports) or [by importing a script file](https://devnet.logianalytics.com/hc/en-us/articles/1500009674801-Importing-and-Exporting-Scheduled-Tasks). |
| Run a task immediately | * Select the task row and select **Run** on the task bar of the My Tasks page. * Select the task row, right-click in the row and select **Run** from the shortcut menu. * Put the mouse pointer over the task row and select the **Run** button  on the floating toolbar. |
| Duplicate a task | * Select the task row and select **Edit > Copy** on the task bar of the My Tasks page. * Select the task row, right-click in the row and select **Copy**  from the shortcut menu. * Put the mouse pointer over the task row and select the **Copy** button  on the floating toolbar. |
| Enable a task | * Select the task row and select **Edit > Enable** on the task bar of the My Tasks page. * Select the task row, right-click in the row and select **Enable** from the shortcut menu. * Put the mouse pointer over the task row and select the **Enable** button  on the floating toolbar. |
| Disable a task | * Select the task row and select **Edit > Disable** on the task bar of the My Tasks page. * Select the task row, right-click in the row and select **Disable** from the shortcut menu. * Put the mouse pointer over the task row and select the **Disable** button  on the floating toolbar.   The disabled task will not be performed until you enable it again. |
| Export a scheduled task to a script on disk | See [Importing and Exporting Scheduled Tasks](https://devnet.logianalytics.com/hc/en-us/articles/1500009674801-Importing-and-Exporting-Scheduled-Tasks) for details. |
| Import a scheduled task from a script saved on disk | See [Importing and Exporting Scheduled Tasks](https://devnet.logianalytics.com/hc/en-us/articles/1500009674801-Importing-and-Exporting-Scheduled-Tasks) for details. |

**Notes:**

* You can perform the Run action on a disabled scheduled task.
* When copying a disabled scheduled task or exporting it to script, the disabled state will not be included since it is not a property of the task.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Managing Tasks in the Running Table

| If you want to | Then do |
| --- | --- |
| Stop a task that is running | * Select the task row and select **Stop** on the task bar of the My Tasks page. * Select the task row, right-click in the row and select **Stop** from the shortcut menu. * Put the mouse pointer over the task row and select the **Stop** button  on the floating toolbar.   **Note:** When you stop a bursting task from running, some sub tasks in the bursting task may have already been finished, so some results may have been sent to some recipients. |
| View parameter information | Refer to the Parameters column of the Running table. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Managing Tasks in the Completed Table

| If you want to | Then do |
| --- | --- |
| View detailed task run information | * Select the schedule name of the task. * Select the task row and select **Edit** > **Details** on the task bar of the My Tasks page. * Select the task row, right-click in the row and select **Details** from the shortcut menu. * Put the mouse pointer over the task row and select the **Details** button  on the floating toolbar.   The Result Details table is then displayed which contains the following information:   |  |  | | --- | --- | | Task ID | Displays the task ID. | | Report | Displays on which report the task is based. | | Publish Type | Displays the publish types of the task. | | Result | Displays the results of the task. For results of the To Version publish type, you can select the links to view the results. To view a page report result, necessary permissions are required. Select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009674841-Viewing-Scheduled-Report-Results#Version) for more information. | | Is Successful | Displays whether or not the task is successful. | | Details | Displays the locations of the results. | |
| View parameter information | Refer to the Parameters column of the Completed table. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Managing Tasks in the Background Tasks Table

| If you want to | Then do |
| --- | --- |
| Stop a running task submitted using Background Run mode | * Select the task row and select **Edit > Stop** on the task bar of the My Tasks page. * Select the task row, right-click in the row and select **Stop** from the shortcut menu. * Put the mouse pointer over the task row and select the **Stop** button  on the floating toolbar. |
| Restart a stopped task | * Select the task row and select **Edit > Restart** on the task bar of the My Tasks page. * Select the task row, right-click in the row and select **Restart** from the shortcut menu. * Put the mouse pointer over the task row and select the **Restart** button  on the floating toolbar. |
| View parameter information | Refer to the Parameters column of the Background Tasks table. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648922-Accessing-the-Task-Information-Tables)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648962-Task-level-Timeout-for-Advanced-Run-and-Schedule-Tasks)
