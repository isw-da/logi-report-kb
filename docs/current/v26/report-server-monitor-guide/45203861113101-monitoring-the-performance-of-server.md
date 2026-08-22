---
title: "Monitoring the Performance of Server"
id: 45203861113101
section: "Report Server Monitor Guide"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203861113101-Monitoring-the-Performance-of-Server
updated_at: 2026-04-30T14:07:38Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Monitoring the Performance of Server

Server Monitor can show performance counters in graph (Line chart and Bar chart) and text mode. This topic describes how you can monitor the performance of Server.

- Access the home page of Server Monitor.

- In the left panel, expand the tree to select any Server node.

- Select the Performance tab. Monitor displays the performance chart of the specified Server.

- If you want to configure the performance chart, select the Graph Option button  on the toolbar. Monitor displays the Graph Options dialog box.

- In the Keep Last N Records text box, type how many tick marks you want to display on the X axis. 

- In the Y Axis Limit text box, type the maximum value on the left Y axis.

- In the Y2 Axis Limit text box, type the maximum value on the right Y axis. 

- In the Interval text box, type the time interval in seconds the performance chart uses to get data and refresh itself.

- Select the Clear Display button  if you want to clear the current display of the performance counters in the performance chart. 

- To stop the current display of the performance counters, select the Stop button  on the toolbar.   

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
