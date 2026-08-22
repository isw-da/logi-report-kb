---
title: "Monitoring the Status of Reports"
id: 1500009649102
section: "Monitoring Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009649102-Monitoring-the-Status-of-Reports
updated_at: 2021-07-24T20:53:59Z
---

# Monitoring the Status of Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649062-Showing-the-Status-of-Servers-in-a-Cluster)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649122-Monitoring-the-Status-of-Online-Users)

# Monitoring the Status of Reports

Expand any server node in the left panel of the Logi JReport Server Monitor home page, and then select **Reports**, you can see the status of the page reports, web reports and dashboards on the server.

There are five types of report status: all reports, running reports, waiting reports, finished reports, and failed reports. You can select to view the status of different reports from the drop-down list.

Below is a list of the sections covered in this topic:

* [Status of All Reports](#All)
* [Status of the Running Reports](#Running)
* [Status of the Waiting Reports](#Waiting)
* [Status of the Finished Reports](#Finished)
* [Status of the Failed Reports](#Failed)
* [Exporting the Monitoring Data](#Export)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Status of All Reports

The status table of all reports includes:

| Column Heading | Description |
| --- | --- |
| Report | The full path name of the report. |
| User ID | The ID of the user who opened the report. |
| Submit Time | The time when the report was last opened. |
| Pages | The total number of pages the last opened report has. Not available for web reports and dashboards. |
| Number of Runs | The total number of report runs since it is first published to Logi JReport Server. |
| Status | The status of the opened report. |

In addition, when you select the full path name of a report, the Task Statistics dialog will pop up, showing you the detailed task statistics, which includes the following:

**Task ID**

The exact date and time when the report was opened.

**Report**

The path and name of the opened report.

**Catalog**

The catalog where the opened report lists.

**Total Number of Times Run**

The total number of times the opened report has run ever since a specific time.

**Average Number of Times per Day**

The average number of times the opened report has run per day.

**Last Submit Time**

The time when the report was last opened.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Status of the Running Reports

The status table of the running reports includes:

| Column Heading | Description |
| --- | --- |
| Action | Stops the report from running and makes it a failed report. |
| Task ID | The internal ID for this report. |
| Report | The full path name of the report. |
| User ID | The ID of the user who opened the report. |
| Task Status | For running reports, can be one of the following:  * **Running** -   The task is currently being processed. * **Initializing Engine** -   The task is currently in the initializing engine stage. * **Loading Report** -   The task is currently in the loading report stage. * **Exporting** -   The task is currently in the exporting stage. * **Exiting Engine** -   The task is currently in the exiting engine stage. |
| Task Type | The task type. Can be one of the following: Schedule, On-Demand, Page Report Studio, Web Report Studio, Dashboard and Bursting. |
| Start Time | The time when the task was started. |
| Elapsed Time | The elapsed time since the task was started. |
| Submit Time | The time when the report was opened. |
| Run Host | The name of the host on which the task is performed. |
| Run Port | The port number of the host on which the task is performed. |
| Catalog | The catalog that the report belongs to. |

In addition, when you select the task ID of a report, the Task Information dialog will pop up, showing you the detailed task information, which includes the following:

**Task ID**

The exact date and time when the report was opened.

**Task Type**

The task type. There are six task types: Schedule, On-Demand, Page Report Studio, Web Report Studio, Dashboard, and Bursting.

**Report**

The path and name of the opened report.

**Catalog**

The catalog where the opened report lists.

**Report Pages**

The total page number of the report. Not available when task type is Web Report Studio or Dashboard.

**Submit Time**

The time when the report was opened.

**Start Run Time**

The time when the report was started to run.

**Completed Time**

The time when the report was closed.

**Parameters**

The parameters that user uses to run the report. If the report runs with no parameters, this column will be left empty.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Status of the Waiting Reports

The status table of the waiting reports includes:

| Column Heading | Description |
| --- | --- |
| Action | Stops the report from running and makes it a failed report. |
| Task ID | The internal ID for this report. If you select the ID, the [Task Information](#Taskinfo) dialog will pop up showing you the detailed task information. |
| Report | The full path name of the report. |
| User ID | The ID of the user who opened the report. |
| Task Status | For waiting reports, can be one of the following:  * **Submitted** -   The task has been submitted successfully. * **Unlaunch** -   The task is currently in the unlaunch queue waiting to be processed. * **Task Queue** -   The task is currently in the task thread queue waiting to be processed. |
| Task Type | The task type. Can be one of the following: Schedule, On-Demand, Page Report Studio, Web Report Studio, Dashboard, and Bursting. |
| Submit Time | The time when the report was opened. |
| Catalog | The catalog that the report belongs to. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Status of the Finished Reports

The status table of the finished reports includes:

| Column Heading | Description |
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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Status of the Failed Reports

The status table of the failed reports includes:

| Column Heading | Description |
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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Exporting the Monitoring Data

You can export the monitoring data of the reports' status to a CSV file. However, before doing this, you need to make sure the profiling DB on the server node where the monitoring data will be saved has already been configured. For details about how to configure the profiling DB, see the topic [Configuring
the Server Database in a Standalone Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009669101-Configuring-in-a-Standalone-Environment).

**To export the monitoring data of the reports' status:**

1. Select the **Export Data** link on the reports status panel. The Export Data dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920485143/mntr_sts_report_exptdata.gif)
2. Specify the report type, the time period of the monitoring data and the name of the exported file respectively.
3. Select **OK** to export the data.

The following are details about options in the Export Data dialog:

**Report**

The type of reports you want to export the monitoring data.

**From**

The date and time from which the monitoring data starts. You can type it in the text field or select the calendar button to select the date and time.

**To**

The date and time to which the monitoring data ends. You can type it in the text field or select the calendar button to select the date and time.

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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649062-Showing-the-Status-of-Servers-in-a-Cluster)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649122-Monitoring-the-Status-of-Online-Users)
