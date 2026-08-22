---
title: "Managing Scheduled CRD Tasks"
id: 1500009648662
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648662-Managing-Scheduled-CRD-Tasks
updated_at: 2021-07-24T20:54:06Z
---

# Managing Scheduled CRD Tasks

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673421-Scheduling-Cached-Report-Data-Results)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648682-Managing-In-memory-Cubes)

# Managing Scheduled CRD Tasks

The tasks that have been submitted for generating scheduled CRD are listed in the [Cached Report Data](#Cached), [Scheduled](#Scheduled), [Running](#Running), and [Completed](#Completed) tables on the Logi JReport Administration > Cache > Data Cache page according to their status. For each table you can customize the columns to be displayed as follows:

1. On the Cache - Data Cache page, switch to the tab for the table, then select **Preferences** on the task bar.
2. In the Preferences dialog, check the checkbox ahead of the column names which you want to display in the table.
3. For the Running table, in the Preferences dialog, you can also use the Parameter Display Size option to specify the display length in characters of the parameters listed in its Parameters column. For the Completed table, you can specify the number of days for keeping completed tasks and the display length of the parameters listed in its Parameters column.
4. Select **OK** to apply the settings.

The following lists the columns each table contains in details. The records in the tables can be sorted by selecting the underlined column headers.

**Cached Report Data table**

This table displays the scheduled data cache tasks and consists of the following columns:

| Column | Description |
| --- | --- |
| Name | The name of the scheduled data cache. |
| Path | The path of the scheduled data cache in the server resource tree. |
| Catalog Name | The catalog that the scheduled data cache belongs to. |
| Data Source | The data source that the scheduled data cache belongs to. |
| Data Type | The type of the query resource that the scheduled data cache is based on. |
| Last Modified | The last time when the scheduled data cache was modified. |

You can further edit the scheduling information of the tasks in the table or remove the tasks.

* To edit a task, select the row in which the task is, then select **Edit > Properties** on the task bar or right-click on the row and select **Properties** from the shortcut menu. If parameters or schedule policy is changed, they will only take effect after the next CRD update time; before that, all reports using the CRD will still get the old data.
* To remove a task, select the row where the task is, then selecting **Edit > Delete** on the task bar; or right-click in the row and select **Delete** from the shortcut menu.

**Scheduled table**

This table displays the data cache tasks that are waiting to be performed. It consists of the following columns:

| Column | Description |
| --- | --- |
| Name | The name of the scheduled data cache. |
| Path | The path of the scheduled data cache in the server resource tree. |
| Catalog Name | The catalog that the scheduled data cache belongs to. |
| Data Source | The data source that the scheduled data cache belongs to. |
| Data Type | The type of the query resource that the scheduled data cache is based on. |
| Last Modified | The latest time when the task was modified. |
| Next Run Time | The next scheduled time this task is to be performed. |
| Last Run Time | The last scheduled time this task was performed. |
| Is Successful | Shows whether or not the last running of this task was successfully performed. The value true means that the last running was performed successfully and false means the task failed. If the column is empty, the task has not been run before. |

**Running table**

This table displays the data cache tasks that are currently being performed. It consists of the following columns:

| Column | Description |
| --- | --- |
| Name | The name of the scheduled data cache. |
| Path | The path of the scheduled data cache in the server resource tree. |
| Catalog Name | The catalog that the scheduled data cache belongs to. |
| Data Source | The data source that the scheduled data cache belongs to. |
| Data Type | The type of the query resource that the scheduled data cache is based on. |
| Start Time | The time when this task was started. |
| Parameters | The parameters of the query. |

**Completed table**

This table displays the data cache tasks that have already been finished and consists of the following columns.

| Column | Description |
| --- | --- |
| Name | The name of the scheduled data cache. |
| Path | The path of the scheduled data cache in the server resource tree. |
| Catalog Name | The catalog that the scheduled data cache belongs to. |
| Data Source | The data source that the scheduled data cache belongs to. |
| Data Type | The type of the query resource that the scheduled data cache is based on. |
| Is Successful | Shows whether this task was successfully performed. The value true means that the task was performed successfully and false that the task failed. |
| Completed Time | The time when this task was completed. |
| Parameters | The parameters of the query. |

When a task is listed in the table, the cached report data generated from the schedule task will be ready for use.

You can remove the record of a completed CRD task from the tab if required. To do this, select the row where the record is located and then select **Delete** on the task bar, or right-click on the row and select **Delete** from the shortcut menu.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673421-Scheduling-Cached-Report-Data-Results)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648682-Managing-In-memory-Cubes)
