---
title: "Report Server Monitor Guide v24 Overview"
id: 28891395501837
section: "Report Server Monitor Guide v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891395501837-Report-Server-Monitor-Guide-v24-Overview
updated_at: 2025-01-27T20:57:09Z
source_host: docs-report.zendesk.com
---
Next Topic

# 
Report Server Monitor Guide v24 Overview 

This guide describes Report Server Monitor, which is a standalone web-based application used to monitor the overall performance of Report Server.

Report Server Monitor has the following main features:

- 
Inspects the status of Report Server
Server Monitor enables you to view the status of Servers in a cluster. It also enables you to view the status of different reports and the status of online users, and so on.

- 
Shows Report Server performance statistics in Graph/Text mode
Server Monitor is able to generate and display a performance chart of Server according to its statistics. In this way, you can view the performance of Server in the form of Line chart Graph and Text.

- 
Maintains Report Server
You can perform maintenance tasks from Server Monitor, such as shutting down Server, stopping waiting/running tasks, and signing out of a valid UserSession.

- 
Creates profiling reports: performance reports and statistic reports
  By creating profiling reports using Server Monitor, you can inspect the performance of Server in a certain period of time.

- 
Provides JMX remote/local monitoring feature
Report has constructed JMX MBeans which correspond to all the monitored objects (including Cluster, Report Server, Report Task, UserSession, and the Database Connection Pool). You can use MBeanServer to find these registered MBeans and perform any operation on them. These JMX MBeans provide the same monitoring functions as with our normal Server Monitor's JSP pages.

If you want to learn about installing and uninstalling the Server Monitor, select this link: Installing and Uninstalling Server Monitor.

If you want to learn about accessing Server Monitor from the console, select this link: Launching and Accessing Server Monitor.

Next Topic
