---
title: "Monitoring the Server Status"
id: 1500009691462
section: "Monitoring Logi JReport Server Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009691462-Monitoring-the-Server-Status
updated_at: 2021-11-03T06:56:52Z
---

# Monitoring the Server Status

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691442-Monitoring-Logi-JReport-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718041-Monitoring-the-Server-Performance)

# Monitoring the Server Status

Logi JReport Server Monitor allows you to inspect the status of Logi JReport Server. You can list the servers and their status from a cluster. You can also list the reports by drilling down into the servers, for example, running reports, waiting reports, finished reports, and failed reports. Tracking further down, you can even view the status of these reports. However, Logi JReport Server Monitor is not able to monitor the information of a report that is running in Page Report Studio.

Below is a list of the sections covered in this topic:

* [Showing the Status of Servers in a Cluster](#Cluster)
* [Monitoring the Status of Reports](#Report)
  + [Exporting the Monitoring Data](#Export)
* [Monitoring the Status of Online Users](#User)
* [Monitoring the Status of the Database Connection Pool](#Pool)

## Showing the Status of Servers in a Cluster

By accessing the home page of Logi JReport Server Monitor, you can see the status of each server in a cluster, including the cluster member ID, host IP, port, and its status.

The Status table of the servers includes:

| Column | Description |
| --- | --- |
| Cluster Member ID | The ID of the server as a cluster member. |
| Host | The host IP address of the server. |
| Port | The RMI port number of the server. |
| Status | The status of the server:  * **Active** - The server has been started and is ready for service. * **Inactive** - The server is inactive and cannot be available for service. |

## Monitoring the Status of Reports

Expand any server node in the left panel of the Logi JReport Server Monitor home page, and then select **Reports**, you can see the status of the page reports, web reports and dashboards on the server.

There are five types of report status: [all reports](#All), [running reports](#Running), [waiting reports](#Waiting), [finished reports](#Finished), and [failed reports](#Failed). You can select to view the status of different reports from the drop-down list.

**Status of all reports**

The status table of all reports includes:

| Column | Description |
| --- | --- |
| Report | The full path name of the report. |
| User ID | The ID of the user who opened the report. |
| Submit Time | The time when the report was last opened. |
| Pages | The total number of pages the last opened report has. Not available for web reports and dashboards. |
| Number of Runs | The total number of report runs since it is first published to Logi JReport Server. |
| Status | The status of the opened report. |

When you select the full path name of a report, the Task Statistics dialog will pop up, showing you the detailed task statistics, which includes the following:

* **Task ID**  
   The exact date and time when the report was opened.
* **Report**The path and name of the opened report.
* **Catalog**  
   The catalog where the opened report lists.
* **Total Number of Times Run**  
   The total number of times the opened report has run ever since a specific time.
* **Average Number of Times per Day**  
   The average number of times the opened report has run per day.
* **Last Submit Time**  
   The time when the report was last opened.

**Status of the running reports**

The status table of the running reports includes:

| Column | Description |
| --- | --- |
| Action | Stops the report from running and makes it a failed report. |
| Task ID | The internal ID for this report. |
| Report | The full path name of the report. |
| User ID | The ID of the user who opened the report. |
| Task Status | Can be one of the following:  * **Running** - The task is currently being processed. * **Initializing Engine** - The task is currently in the initializing engine stage. * **Loading Report** - The task is currently in the loading report stage. * **Exporting** - The task is currently in the exporting stage. * **Exiting Engine** - The task is currently in the exiting engine stage. |
| Task Type | The task type. Can be one of the following: Schedule, On-Demand, Page Report Studio, Web Report Studio, Dashboard and Bursting. |
| Start Time | The time when the task was started. |
| Elapsed Time | The elapsed time since the task was started. |
| Submit Time | The time when the report was opened. |
| Run Host | The name of the host on which the task is performed. |
| Run Port | The port number of the host on which the task is performed. |
| Catalog | The catalog that the report belongs to. |

When you select the task ID of a report, the Task Information dialog will pop up, showing you the detailed task information, which includes the following:

* **Task ID**  
   The exact date and time when the report was opened.
* **Task Type**  
   The task type. There are six task types: Schedule, On-Demand, Page Report Studio, Web Report Studio, Dashboard, and Bursting.
* **Report**   
   The path and name of the opened report.
* **Catalog**  
   The catalog where the opened report lists.
* **Report Pages**  
   The total page number of the report. Not available when task type is Web Report Studio or Dashboard.
* **Submit Time**  
   The time when the report was opened.
* **Start Run Time**  
   The time when the report was started to run.
* **Completed Time**The time when the report was closed.
* **Parameters**  
   The parameters that user uses to run the report. If the report runs with no parameters, this column will be left empty.

**Status of the waiting reports**

The status table of the waiting reports includes:

| Column | Description |
| --- | --- |
| Action | Stops the report from running and makes it a failed report. |
| Task ID | The internal ID for this report. If you select the ID, the [Task Information](#Taskinfo) dialog will pop up showing you the detailed task information. |
| Report | The full path name of the report. |
| User ID | The ID of the user who opened the report. |
| Task Status | Can be one of the following:  * **Submitted** - The task has been submitted successfully. * **Unlaunch** - The task is currently in the unlaunch queue waiting to be processed. * **Task Queue** - The task is currently in the task thread queue waiting to be processed. |
| Task Type | The task type. Can be one of the following: Schedule, On-Demand, Page Report Studio, Web Report Studio, Dashboard, and Bursting. |
| Submit Time | The time when the report was opened. |
| Catalog | The catalog that the report belongs to. |

**Status of the finished reports**

The status table of the finished reports includes:

| Column | Description |
| --- | --- |
| Task ID | The internal ID for this report. If you select the ID, the [Task Information](#Taskinfo) dialog will pop up showing you the detailed task information. |
| Report | The full path name of the report. |
| User ID | The ID of the user who opened the report. |
| Task Status | Completed. The task has been processed successfully, and has accomplished all the requirements. |
| Task Type | The task type. Can be one of the following: Schedule, On-Demand, Page Report Studio, Web Report Studio, Dashboard and Bursting. |
| Run Host | The name of the host on which the task is performed. |
| Run Port | The port number of the host on which the task is performed. |
| Catalog | The catalog that the report belongs to. |
| Result Files | The path of the result files. |
| Report Pages | The total page number of the report. Not available when task type is Web Report Studio or Dashboard. |
| Reason | The reason why the task failed. Can be an exception or a meaningful description. |
| Submit Time | The time when the report was opened. |
| Start Run Time | The time when the report was started to run. |
| Completed Time | The time when the report was closed. |

**Status of the failed reports**

The status table of the failed reports includes:

| Column | Description |
| --- | --- |
| Task ID | The internal ID for this report. If you select the ID, the [Task Information](#Taskinfo) dialog will pop up showing you the detailed task information. |
| Report | The full path name of the report. |
| User ID | The ID of the user who opened the report. |
| Task Status | Failed. The task has encountered errors, and has failed to accomplish all the requirements. |
| Task Type | The task type. Can be one of the following: Schedule, On-Demand, Page Report Studio, Web Report Studio, Dashboard, and Bursting. |
| Run Host | The name of the host on which the task is performed. |
| Run Port | The port number of the host on which the task is performed. |
| Catalog | The catalog that the report belongs to. |
| Result Files | The path of the result files. |
| Report Pages | The total page number of the report. Not available when task type is Web Report Studio or Dashboard. |
| Reason | The reason why the task fails. Can be an exception or a meaningful description. |
| Failed Info | The information about the report's failure. |
| Submit Time | The time when the report was opened. |
| Start Run Time | The time when the report was started to run. |
| Completed Time | The time when the report was closed. |

### Exporting the Monitoring Data

You can export the monitoring data of the reports' status to a CSV file. However, before doing this, you need to make sure the profiling DB on the server node where the monitoring data will be saved has already been configured. For details about how to configure the profiling DB, see the topic [Configuring in a Standalone Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009686682-Configuring-in-a-Standalone-Environment).

**To export the monitoring data of the reports' status:**

1. Select the **Export Data** link in the report status panel. The Export Data dialog appears.

   ![Export Data dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112559639/mntr_sts_report_exptdata.gif)
2. Specify the report type, the time period of the monitoring data and the name of the exported file respectively.
3. Select **OK** to export the data.

The following are details about options in the Export Data dialog:

**Report**

The type of reports you want to export the monitoring data.

**From**

The date and time from which the monitoring data starts. You can type it in the text box or select the calendar button to select the date and time.

**To**

The date and time to which the monitoring data ends. You can type it in the text box or select the calendar button to select the date and time.

**File Name**

The name of the exported file.

**OK**

Exports the data to a CSV file and opens the File Download panel. You can choose to open the file or save it elsewhere.

**Cancel**

Does not retain any changes and closes the dialog.

**Note:** The exported monitoring data in the CSV file are encoded with UTF-8. If you open an exported CSV file which contains Chinese strings by a double-click, the Chinese strings would be displayed as random code in the file. To solve this problem, you need to open the file in the following way:

1. Start Microsoft Excel first.
2. Select **From Text** in the Data tab, then select the exported CSV file and select **Import**.
3. Select **65001: Unicode (UTF-8)** in the File Origin selector, then keep selecting **Next** and at last select **Finish** and **OK**.

## Monitoring the Status of Online Users

To see the status of the online users, expand any server node in the left panel of the Logi JReport Server Monitor home page, and then select **Users**. You can also select and remove specific users.

The status table of the online users includes:

| Column | Description |
| --- | --- |
| Session ID | The internal ID of the user session. |
| User ID | The ID of the user logged onto the server. |
| Create Time | The time when the user session was created. |
| Last Access Time | The time when the user last accessed the server. |
| HTTP Session ID | The session ID in the HTTP service. |
| Authentication | The authentication type. It can be Internal or External. |

## Monitoring the Status of the Database Connection Pool

To see the status of the database connection pool, expand any server node in the left panel of the Logi JReport Server Monitor home page, and then select **Databases**. You can also select and remove specific connections.

The status table of the connection pool includes:

| Column | Value | Description |
| --- | --- | --- |
| User | String | The user who is currently using the connection. |
| URL | A URL connecting to a database. | It specifies the connections that are based on a URL which will be caught in the pool. |
| Expiring Time(s) | 0 (default) or expiring time. The unit is second. If the value is zero then the connection will never expire. | Shows the time during which a connection can be alive. If a connection has expired, the connection pool will close it. |
| Idle Expiring Time(s) | 1 (default) or expiring time. The unit is second. Its value must be larger than or equals to 1. | Shows the time during which a connection is kept after it starts idling. If a connection is not used, it will stay open until the idle expiry time has been reached. |
| Maximal Connection Count | 0 (default) or a positive integer. | Shows the pool size, which limits the number of connections under a single URL |
| Maximal Share Count | 0 (default) or a positive integer. | Shows the number of users who can share a connection simultaneously. |
| Attempt | A positive integer, the default value is 1. | Shows whether to re-create a connection when the connection pool has failed to create one and the number of attempts for creating the connection. If the user sets this value to a non-positive integer, the default value (1) will be used. |
| Interval(ms) | 0 (default) or a positive integer. The unit is millisecond (ms). | If property ‘Attempt' is larger than 1, then before the connection pool retries to create a connection it will wait for an interval time. This property defines the interval time. |
| Last User Connecting Time(s) | 0 (default) or a positive integer. The unit is second. | It shows the time elapsed since the last user has taken this connection. |
| Current Idle Time(s) | 0 (default) or a positive integer.The unit is second. | Shows the time elapsed since the connection started to idle. |
| Current Share Count | 0 (default) or a positive integer. | Shows the number of users who are currently sharing this connection. |

**Note:** The properties numbered 2 to 8 can be set in the ConnectionPoolConfig.properties file in `<server_install_root>\bin` and the last three properties will be shown according to the real time status.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691442-Monitoring-Logi-JReport-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718041-Monitoring-the-Server-Performance)
