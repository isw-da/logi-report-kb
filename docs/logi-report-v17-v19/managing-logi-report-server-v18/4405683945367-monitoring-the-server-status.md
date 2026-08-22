---
title: "Monitoring the Server Status"
id: 4405683945367
section: "Managing Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683945367-Monitoring-the-Server-Status
updated_at: 2022-01-27T07:59:40Z
---

# Monitoring the Server Status

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690647063-Monitoring-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683944343-Monitoring-the-Server-Performance)

# Monitoring the Server Status

Logi Report Server Monitor enables you to inspect the status of Logi Report Server. This topic describes how you can monitor the status of reports, servers in a Cluster, users, and the database connection pool.

You can list the servers and their status from a Cluster. You can also list the reports by drilling down into the servers, for example, running reports, waiting reports, finished reports, and failed reports. Tracking further down, you can even view the status of these reports. However, Server Monitor is not able to monitor the information of a report that is running in Page Report Studio.

This topic contains the following sections:

* [Showing the Status of Servers in a Cluster](#Cluster)
* [Monitoring the Status of Reports](#Report)
  + [Exporting the Monitoring Data](#Export)
* [Monitoring the Status of Online Users](#User)
* [Monitoring the Status of the Database Connection Pool](#Pool)

## Showing the Status of Servers in a Cluster

By accessing the home page of Server Monitor, you can see the status of each server in a cluster, including the cluster member ID, host IP, port, and its status.

The Status table of the servers includes:

| Column | Description |
| --- | --- |
| Cluster Member ID | The ID of the server as a cluster member. |
| Host | The host IP address of the server. |
| Port | The RMI port number of the server. |
| Status | The status of the server:  * **Active** - The server has started and is ready for service. * **Inactive** - The server is inactive and cannot be available for service. |

## Monitoring the Status of Reports

Expand any server node in the left panel of the Server Monitor home page, and then select **Reports**, you can see the status of the page reports, web reports, and dashboards on the server.

There are five types of report status: [all reports](#All), [running reports](#Running), [waiting reports](#Waiting), [finished reports](#Finished), and [failed reports](#Failed). You can select to view the status of different reports from the drop-down list.

**Status of all reports**

The status table of all reports includes:

| Column | Description |
| --- | --- |
| Report | The full path name of the report. |
| User ID | The ID of the user who opened the report. |
| Submit Time | The time when the report was last opened. |
| Pages | The total number of pages the last opened report has. Not available for web reports or dashboards. |
| Number of Runs | The total times of running the report since you first publish it to Server. |
| Status | The status of the opened report. |

When you select the full path name of a report, Server Monitor displays the Task Statistics dialog box, showing you the task statistics, which includes the following:

* **Task ID**  
   The exact date and time when the report opened.
* **Report**The path and name of the opened report.
* **Catalog**  
   The catalog that the opened report belongs to.
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
| Action | Stop the report from running and make it a failed report. |
| Task ID | The internal ID for the report running task. |
| Report | The full path name of the report. |
| User ID | The ID of the user who opened the report. |
| Task Status | Can be one of the following:  * **Running** - The task is currently processing. * **Initializing Engine** - The task is currently in the initializing engine stage. * **Loading Report** - The task is currently in the loading report stage. * **Exporting** - The task is currently in the exporting stage. * **Exiting Engine** - The task is currently in the exiting engine stage. |
| Task Type | The task type. Can be one of the following: Schedule, On-Demand, Page Report Studio, Web Report Studio, Dashboard, and Bursting. |
| Start Time | The time when the task started. |
| Elapsed Time | The elapsed time since the task started. |
| Submit Time | The time when the report opened. |
| Run Host | The name of the host on which the task is performed. |
| Run Port | The port number of the host on which the task is performed. |
| Catalog | The catalog that the report belongs to. |

When you select the task ID of a report, Server Monitor displays the Task Information dialog box, showing you the task information, which includes the following:

* **Task ID**  
   The exact date and time when the report opened.
* **Task Type**  
   The task type. There are six task types: Schedule, On-Demand, Page Report Studio, Web Report Studio, Dashboard, and Bursting.
* **Report**   
   The path and name of the opened report.
* **Catalog**  
   The catalog that the opened report belongs to.
* **Report Pages**  
   The total page number of the report. Not available when task type is Web Report Studio or Dashboard.
* **Submit Time**  
   The time when the report opened.
* **Start Run Time**  
   The time when the report started to run.
* **Completed Time**The time when the report closed.
* **Parameters**  
   The parameters that the report used to run. If the report ran with no parameters, this column is left blank.

**Status of the waiting reports**

The status table of the waiting reports includes:

| Column | Description |
| --- | --- |
| Action | Stop the report from running and make it a failed report. |
| Task ID | The internal ID for this task. If you select the ID, Server Monitor displays the [Task Information](#Taskinfo) dialog box showing you the task information. |
| Report | The full path name of the report. |
| User ID | The ID of the user who opened the report. |
| Task Status | Can be one of the following:  * **Submitted** - The task has submitted successfully. * **Unlaunch** - The task is currently in the unlaunch queue waiting to process. * **Task Queue** - The task is currently in the task thread queue waiting to process. |
| Task Type | The task type. Can be one of the following: Schedule, On-Demand, Page Report Studio, Web Report Studio, Dashboard, and Bursting. |
| Submit Time | The time when the report opened. |
| Catalog | The catalog that the report belongs to. |

**Status of the finished reports**

The status table of the finished reports includes:

| Column | Description |
| --- | --- |
| Task ID | The internal ID for this task. If you select the ID, Server Monitor displays the [Task Information](#Taskinfo) dialog box showing you the task information. |
| Report | The full path name of the report. |
| User ID | The ID of the user who opened the report. |
| Task Status | Completed. The task has processed successfully and has accomplished all the requirements. |
| Task Type | The task type. Can be one of the following: Schedule, On-Demand, Page Report Studio, Web Report Studio, Dashboard, and Bursting. |
| Run Host | The name of the host on which the task is performed. |
| Run Port | The port number of the host on which the task is performed. |
| Catalog | The catalog that the report belongs to. |
| Result Files | The path of the result files. |
| Report Pages | The total page number of the report. Not available when task type is Web Report Studio or Dashboard. |
| Reason | The reason why the task failed. Can be an exception or a meaningful description. |
| Submit Time | The time when the report opened. |
| Start Run Time | The time when the report started to run. |
| Completed Time | The time when the report closed. |

**Status of the failed reports**

The status table of the failed reports includes:

| Column | Description |
| --- | --- |
| Task ID | The internal ID for this task. If you select the ID, Server Monitor displays the [Task Information](#Taskinfo) dialog box showing you the task information. |
| Report | The full path name of the report. |
| User ID | The ID of the user who opened the report. |
| Task Status | Failed. The task has encountered errors and has failed to accomplish all the requirements. |
| Task Type | The task type. Can be one of the following: Schedule, On-Demand, Page Report Studio, Web Report Studio, Dashboard, and Bursting. |
| Run Host | The name of the host on which the task is performed. |
| Run Port | The port number of the host on which the task is performed. |
| Catalog | The catalog that the report belongs to. |
| Result Files | The path of the result files. |
| Report Pages | The total page number of the report. Not available when task type is Web Report Studio or Dashboard. |
| Reason | The reason why the task failed. Can be an exception or a meaningful description. |
| Failed Info | The information about the report's failure. |
| Submit Time | The time when the report opened. |
| Start Run Time | The time when the report started to run. |
| Completed Time | The time when the report closed. |

### Exporting the Monitoring Data

You can export the monitoring data of the reports' status to a CSV file. However, before doing this, you must configure the profiling DB on the server node where you are going to save the monitoring data. For more information, see [Configuring the Server Database in a Standalone Environment](https://devnet.logianalytics.com/hc/en-us/articles/4405683583383-Configuring-the-Server-Database-in-a-Standalone-Environment).

**To export the monitoring data of the reports' status:**

1. Select **Export Data** in the report status panel. Server Monitor displays the Export Data dialog box.

   ![Export Data dialog](https://devnet.logianalytics.com/hc/article_attachments/4420461579287/mntr_sts_report_exptdata.gif)
2. From the **Report** drop-down list, select he type of reports you want to export the monitoring data.
3. Select the **Calendar** icon on the right of the **From** text box to select the date and time from which the monitoring data starts. You can also type the value in the text box.
4. Select the **Calendar** icon on the right of the **To** text box to select the date and time to which the monitoring data ends. You can also type the value in the text box.
5. In the **File Name** text box, type the name of the exported file.
6. Select **OK** to export the data to a CSV file. Server Monitor displays the File Download panel. You can choose to open the file or save it elsewhere.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)Logi Report encodes the exported monitoring data in the CSV file with UTF-8. If you open an exported CSV file that contains Chinese strings by a double-click, the Chinese strings display as random code in the file. To solve this problem, you need to open the file in the following way:

1. Start **Microsoft Excel** first.
2. Select **From Text** in the **Data** tab.
3. Select the exported CSV file.
4. Select **Import**.
5. Select **65001: Unicode (UTF-8)** in the **File Origin** selector.
6. Keep selecting **Next**.
7. Select **Finish**.
8. Select **OK**.

## Monitoring the Status of Online Users

To see the status of the online users, expand any server node in the left panel of the Server Monitor home page, and then select **Users**. You can also select and remove specific users.

The status table of the online users includes:

| Column | Description |
| --- | --- |
| Session ID | The internal ID of the user session. |
| User ID | The ID of the user who signed in to the server. |
| Create Time | The time when Server created the user session. |
| Last Access Time | The time when the user last accessed the server. |
| HTTP Session ID | The session ID in the HTTP service. |
| Authentication | The authentication type. It can be Internal or External. |

## Monitoring the Status of the Database Connection Pool

To see the status of the database connection pool, expand any server node in the left panel of the Server Monitor home page, and then select **Databases**. You can also select and remove specific connections.

The status table of the connection pool includes:

| Column | Value | Description |
| --- | --- | --- |
| User | String | The user who is currently using the connection. |
| URL | A URL for connecting to a database. | The connection based on a URL that the pool will catch. |
| Expiring Time(s) | 0 (the default value) or expiring time in seconds. If the value is zero, then the connection will never expire. | The time during which a connection can be alive. If a connection expired, the connection pool closes it. |
| Idle Expiring Time(s) | 1 (the default value) or expiring time in seconds. Its value must be larger than or equal to 1. | The time during which a connection is kept after it starts idling. If a connection is not used, it will stay open until the idle expiry time is up. |
| Maximal Connection Count | 0 (the default value) or a positive integer. | The pool size, which limits the number of connections under a single URL. |
| Maximal Share Count | 0 (the default value) or a positive integer. | The number of users who can share a connection simultaneously. |
| Attempt | A positive integer. The default value is 1. | Show whether to re-create a connection when the connection pool failed to create one and the number of attempts for creating the connection. If you set the value to a non-positive integer, Server Monitor uses the default value 1. |
| Interval(ms) | 0 (the default value) or a positive integer in milliseconds (ms). | If the property **Attempt** is larger than 1, then the connection pool will wait for an interval time before it retries to create a connection. This property defines the interval time. |
| Last User Connecting Time(s) | 0 (the default value) or a positive integer in seconds. | The time elapsed since the last user has taken this connection. |
| Current Idle Time(s) | 0 (the default value) or a positive integer in seconds. | The time elapsed since the connection started to idle. |
| Current Share Count | 0 (the default value) or a positive integer. | The number of users who are currently sharing this connection. |

You can also set the properties numbered 2 to 8 in the **ConnectionPoolConfig.properties** file in `<server_install_root>\bin` and Server displays the last three properties according to the real time status.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690647063-Monitoring-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683944343-Monitoring-the-Server-Performance)
