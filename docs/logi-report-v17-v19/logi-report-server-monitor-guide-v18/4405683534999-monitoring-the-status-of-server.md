---
title: "Monitoring the Status of Server"
id: 4405683534999
section: "Logi Report Server Monitor Guide v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683534999-Monitoring-the-Status-of-Server
updated_at: 2022-01-27T07:58:27Z
---

# Monitoring the Status of Server

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683533975-Configuring-Server-Monitor)   [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683532951-Monitoring-the-Performance-of-Server)

# Monitoring the Status of Server

This topic introduces how you can use Server Monitor to inspect the status of Logi Report Server, including Servers in a cluster, reports, online users, and the database connection pool.

In Server Monitor, you can list the Servers and their status from a cluster. You can also list the reports by drilling down into the Servers. For example, running reports, waiting reports, finished reports, and failed reports. Tracking further down, you can view the status of these reports.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)Server Monitor is not able to monitor the information of a report that is running in Page Report Studio.

This topic contains the following sections:

* [Showing the Status of Servers in a Cluster](#Cluster)
* [Monitoring the Status of Reports](#Report)

+ [Exporting the Monitoring Data](#Export)

* [Monitoring the Status of Online Users](#User)
* [Monitoring the Status of the Database Connection Pool](#Pool)

## Showing the Status of Servers in a Cluster

By accessing the home page of Server Monitor, you can see the status of each Server in a cluster, including the cluster member ID, host IP, port, and its status.

The Status table includes:

| Column | Description |
| --- | --- |
| Cluster Member ID | The ID of the Server as a cluster member. |
| Host | The host IP address of the Server. |
| Port | The RMI port number of the Server. |
| Status | The status of the Server. Can be either Active or Inactive.  * **Active** - The Server has started and is ready for service. * **Inactive** - The Server is inactive and cannot be available for service. |

## Monitoring the Status of Reports

Expand any Server node in the left panel of the Server Monitor home page, and then select **Reports**, you can see the status of the page reports, web reports, and dashboards on the Server.

There are five types of report status: [all reports](#All), [running reports](#Running), [waiting reports](#Waiting), [finished reports](#Finished), and [failed reports](#Failed). You can select to view the status of different reports from the drop-down list.

**Status of all reports**

The status table of all reports includes:

| Column | Description |
| --- | --- |
| Report | The full path name of the report. |
| User ID | The ID of the user who opened the report. |
| Submit Time | The time when the report was last opened. |
| Pages | The total number of pages the last opened report has. Not available for web reports and dashboards. |
| Number of Runs | The total number of report runs since it is first published to Server. |
| Status | The status of the report. |

In addition, when you select the full path name of a report, Server Monitor displays the Report dialog box, showing you the report statistics, which includes the following:

* **Task ID**  
  The exact date and time when the report was opened.
* **Report**  
  The path and name of the report.
* **Catalog**  
  The catalog where the report lists.
* **Total Number of Times Run**  
  The total number of times the report has run ever since a specific time.
* **Average Number of Times per Day**  
  The average number of times the report has run per day.
* **Last Submit Time**  
  The time when the report was last opened.

**Status of the running reports**

The status table of the running reports includes:

| Column | Description |
| --- | --- |
| Action | You can stop the report from running and make it a failed report. |
| Task ID | The internal ID for this task. |
| Report | The full path name of the report. |
| User ID | The ID of the user who opened the report. |
| Task Status | Can be one of the following:  * **Running** -   The task is currently being processed. * **Initializing Engine** -   The task is currently in the initializing engine stage. * **Loading Report** -   The task is currently in the loading report stage. * **Exporting** -   The task is currently in the exporting stage. * **Exiting Engine** -   The task is currently in the exiting engine stage. |
| Task Type | The task type. Can be one of the following: Schedule, On-Demand, Page Report Studio, Web Report Studio, Dashboard, and Bursting. |
| Start Time | The time when the task started. |
| Elapsed Time | The elapsed time since the task started. |
| Submit Time | The time when the report was opened. |
| Run Host | The name of the host on which the task is performed. |
| Run Port | The port number of the host on which the task is performed. |
| Catalog | The catalog that the report belongs to. |

In addition, when you select the task ID of a report, Monitor displays the Task dialog box, showing the task information, which includes the following:

* **Task ID**  
  The exact date and time when the report was opened.
* **Task Type**  
   The task type. There are six task types: Schedule, On-Demand, Page Report Studio, Web Report Studio, Dashboard, and Bursting.
* **Report**  
  The path and name of the report.
* **Catalog**  
   The catalog that the report belongs to.
* **Report Pages**  
  The total page number of the report. Not available when task type is Web Report Studio or Dashboard.
* **Submit Time**  
  The time when the report was opened.
* **Start Run Time**  
  The time when the report started to run.
* **Completed Time**   
  The time when the report was closed.
* **Parameters**  
  The parameters used to run the report. If the report runs with no parameters, this column will be left blank.

**Status of the waiting reports**

The status table of the waiting reports includes:

| Column | Description |
| --- | --- |
| Action | Stops the report from running and makes it a failed report. |
| Task ID | The internal ID for this task. If you select the ID, the [Task Information dialog box](#Taskinfo) will pop up showing you the detailed task information. |
| Report | The full path name of the report. |
| User ID | The ID of the user who opened the report. |
| Task Status | For waiting reports, can be one of the following:  * **Submitted** -   The task has been submitted successfully. * **Unlaunch** -   The task is currently in the unlaunch queue waiting to be processed. * **Task Queue** -   The task is currently in the task thread queue waiting to be processed. |
| Task Type | The task type. Can be one of the following: Schedule, On-Demand, Page Report Studio, Web Report Studio, Dashboard, and Bursting. |
| Submit Time | The time when the report was opened. |
| Catalog | The catalog that the report belongs to. |

**Status of the finished reports**

The Status table of the finished reports includes:

| Column | Description |
| --- | --- |
| Task ID | The internal ID for this task. If you select the ID, Server Monitor displays the [Task dialog box](#Taskinfo), showing the task information. |
| Report | The full path name of the report. |
| User ID | The ID of the user who opened the report. |
| Task Status | Monitor displays Completed. It means the task has processed successfully and has accomplished all the requirements. |
| Task Type | The task type. Can be one of the following: Schedule, On-Demand, Page Report Studio, Web Report Studio, Dashboard, and Bursting. |
| Run Host | The name of the host on which the task was performed. |
| Run Port | The port number of the host on which the task was performed. |
| Catalog | The catalog that the report belongs to. |
| Result Files | The path of the result files. |
| Report Pages | The total page number of the report. Not available when task type is Web Report Studio or Dashboard. |
| Reason | The reason why the task failed. Can be an exception or a meaningful description. |
| Submit Time | The time when the report was opened. |
| Start Run Time | The time when the report started to run. |
| Completed Time | The time when the report was closed. |

**Status of the failed reports**

The Status table of the failed reports includes:

| Column | Description |
| --- | --- |
| Task ID | The internal ID for this task. If you select the ID, Monitor displays the [Task dialog box](#Taskinfo), showing the task information. |
| Report | The full path name of the report. |
| User ID | The ID of the user who opened the report. |
| Task Status | Monitor displays Failed. It means that the task encountered errors and failed to accomplish all the requirements. |
| Task Type | The task type. Can be one of the following: Schedule, On-Demand, Page Report Studio, Web Report Studio, Dashboard, and Bursting. |
| Run Host | The name of the host on which the task was performed. |
| Run Port | The port number of the host on which the task was performed. |
| Catalog | The catalog that the report belongs to. |
| Result Files | The path of the result files. |
| Report Pages | The total page number of the report. Not available when task type is Web Report Studio or Dashboard. |
| Reason | The reason why the task failed. Can be an exception or a meaningful description. |
| Failed Info | The information about the report's failure. |
| Submit Time | The time when the report was opened. |
| Start Run Time | The time when the report started to run. |
| Completed Time | The time when the report was closed. |

### Exporting the Monitoring Data

You can export the monitoring data of the reports' status to a CSV file. However, before doing this, you must configure the profiling DB on the server node where you are going to save the monitoring data.

**To export the monitoring data of the reports' status:**

1. Select the **Export Data** link on the reports status panel. Monitor displays the Export Data dialog box.
2. From the **Report** drop-down list, select he type of reports you want to export the monitoring data.
3. Select the **Calendar** icon on the right of the **From** text box to select the date and time from which the monitoring data starts. You can also type the value in the text box.
4. Select the **Calendar** icon on the right of the **To** text box to select the date and time to which the monitoring data ends. You can also type the value in the text box.
5. In the **File Name** text box, type the name of the exported file.
6. Select **OK** to export the data to a CSV file. Monitor displays the File Download panel. You can choose to open the file or save it elsewhere.

**![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)**Logi Report encodes the exported monitoring data in the CSV file with UTF-8. If you open an exported CSV file that contains Chinese strings by a double-click, the Chinese strings display as random code in the file. To solve this problem, open the file in the following way:

1. Start **Microsoft Excel** first.
2. Select **From Text** in the **Data** tab.
3. Select the exported CSV file.
4. Select **Import**.
5. Select **65001: Unicode (UTF-8)** in the **File Origin** selector.
6. Keep selecting **Next**.
7. Select **Finish**.
8. Select **OK**.

## Monitoring the Status of Online Users

Expand any Server node in the left panel of the Server Monitor home page, then select **Users**, and you can see the status of the online users on the Server. You can also select and remove specific users.

The Status table of the online users includes:

| Column | Description |
| --- | --- |
| Session ID | The internal ID of the user session. |
| User ID | The ID of the user who signed in to the Server. |
| Create Time | The time when the user session was created. |
| Last Access Time | The time when the user last accessed the Server. |
| HTTP Session ID | The session ID in the HTTP service. |
| Authentication | The authentication type. It can be Internal or External. |

## Monitoring the Status of the Database Connection Pool

Expand any Server node in the left panel of the Server Monitor home page, then select **Databases**, and you can see the status of the Server's database connection pool. You can also select and remove specific connections.

The Status table of the connection pool includes:

| Column | Value | Description |
| --- | --- | --- |
| User | String | The user who is currently using the connection. |
| URL | The URL connecting to a database. | The connections that are based on the URL to catch in the pool. |
| Expiring Time(s) | 0 (the default value) or expiring time in seconds. If the value is zero, then the connection never expires. | The time during which a connection can be alive. If a connection has expired, the connection pool closes it. |
| Idle Expiring Time(s) | 1 (the default value) or expiring time in seconds. Its value must be larger than or equals to 1. | The time during which a connection is kept after it starts idling. If a connection is not used, it stays open until the idle expiry time has reached. |
| Maximal Connection Count | 0 (the default value) or a positive integer. | The pool size which limits the number of connections under a single URL. |
| Maximal Share Count | 0 (the default value) or a positive integer. | The number of users who can share a connection simultaneously. |
| Attempt | A positive integer. The default value is 1. | The number of attempts for recreating a connection when the connection pool has failed to create one. |
| Interval(ms) | 0 (the default value) or a positive integer in milliseconds. | If the property **Attempt** is larger than 1, then the connection pool waits for an interval time before it retries to create a connection. This property defines the interval time. |
| Last User Connecting Time(s) | 0 (the default value) or a positive integer in seconds. | The time elapsed since the last user took this connection. |
| Current Idle Time(s) | 0 (the default value) or a positive integer in seconds. | The time elapsed since the connection started to idle. |
| Current Share Count | 0 (the default value) or a positive integer. | The number of users who are currently sharing this connection. |

**![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)**You can set the properties numbered 2 to 8 in the **ConnectionPoolConfig.properties** file in `<server_install_root>\bin`, and Server displays the last three properties according to the real time status.

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683533975-Configuring-Server-Monitor)   [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683532951-Monitoring-the-Performance-of-Server)
