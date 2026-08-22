---
title: "Monitoring the Performance of Server"
id: 5741394357271
section: "Logi Report Server Monitor Guide v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741394357271-Monitoring-the-Performance-of-Server
updated_at: 2022-10-31T17:15:41Z
---

# Monitoring the Performance of Server

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741394406423-Monitoring-the-Status-of-Server)   [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741399674519-Maintaining-Server)

# Monitoring the Performance of Server

Server Monitor can show performance counters in graph (Line chart and Bar chart) and text mode. This topic describes how you can monitor the performance of Server.

1. Access the home page of Server Monitor.
2. In the left panel, expand the tree to select any Server node.
3. Select the **Performance** tab. Monitor displays the performance chart of the specified Server.
4. If you want to configure the performance chart, select the **Graph Option** button on the toolbar. Monitor displays the Graph Options dialog box.
5. In the **Keep Last N Records** text box, type how many tick marks you want to display on the X axis.
6. In the **Y Axis Limit** text box, type the maximum value on the left Y axis.
7. In the **Y2 Axis Limit** text box, type the maximum value on the right Y axis.
8. In the **Interval** text box, type the time interval in seconds the performance chart uses to get data and refresh itself.
9. Select the **Clear Display** button if you want to clear the current display of the performance counters in the performance chart.
10. To stop the current display of the performance counters, select the **Stop** button on the toolbar.

The following table describes the available counters:

| Performance Counter | Description |
| --- | --- |
| Waiting Reports | The number of the currently waiting reports. |
| Running Reports | The number of the currently running reports. |
| Finished Reports | The number of the finished reports. |
| Finished Report Pages | The number of pages of the finished reports. |
| Average Submitted Tasks per User | The average number of tasks that each user has submitted since Server started. |
| Valid User Sessions | The number of valid user sessions. |
| Database Connections | The number of database connections. |
| Report Average Waiting Time | The average waiting time of each report. |
| Report Average Processing Time | The average processing time of each report. |

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741394406423-Monitoring-the-Status-of-Server)   [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741399674519-Maintaining-Server)
