---
title: "Monitoring the Performance of Logi JReport Server"
id: 1500009711761
section: "Using JReport Server Monitor"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009711761-Monitoring-the-Performance-of-Logi-JReport-Server
updated_at: 2021-11-03T06:58:41Z
---

# Monitoring the Performance of Logi JReport Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412139637143/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009711781-Monitoring-the-Status-of-Logi-JReport-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139637399/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686002-Maintaining-Logi-JReport-Server)

# Monitoring the Performance of Logi JReport Server

Logi JReport Server Monitor can show performance counters in graph (Line chart and Bar chart) and text mode.

**To monitor the performance of Logi JReport Server:**

1. Access the home page of Logi JReport Server Monitor.
2. In the left panel, expand the tree to select any server node.
3. Select the **Performance** tab and the performance chart of the specified server will be displayed.
4. If you want to configure the performance chart, select the **Graph Options** button ![Graph Options button](https://devnet.logianalytics.com/hc/article_attachments/4412139637911/btn_graphoptn.gif) on the toolbar. In the Graph Options dialog, set how many tick marks you need to display on the X axis in the Keep Last N Records text field. In the Y Axis Limit and Y2 Axis Limit text fields, set respectively the maximum value on the left Y axis and the right Y axis. In the Interval text field, set the time interval (in seconds) the performance chart will use to get data and refresh itself.

   Select the **Clear Display** button ![Clear Display button](https://devnet.logianalytics.com/hc/article_attachments/4412139638167/btn_clrdspy.gif) if you want to clear the current display of the performance counters in the performance chart.

   To stop the current display of the performance counters, select the **Stop** button ![Stop button](https://devnet.logianalytics.com/hc/article_attachments/4412112646295/btn_stop.gif) on the toolbar.

The following are the available counters:

| Performance Counter | Description |
| --- | --- |
| Waiting Reports | The number of the currently waiting reports. |
| Running Reports | The number of the currently running reports. |
| Finished Reports | The number of the finished reports. |
| Finished Report Pages | The number of pages of the finished reports. |
| Report Average Processing Time | The average processing time of each report. |
| Report Average Waiting Time | The average waiting time of each report. |
| Valid User Sessions | The number of valid user sessions. |
| Average Submitted Tasks per User | The average number of tasks that each user has submitted since Logi JReport Server started. |
| Database Connections | The number of database connections. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412139637143/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009711781-Monitoring-the-Status-of-Logi-JReport-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139637399/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686002-Maintaining-Logi-JReport-Server)
