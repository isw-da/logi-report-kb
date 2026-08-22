---
title: "Logi Report Server Monitor Guide v18 Overview"
id: 4405683483031
section: "Logi Report Server Monitor Guide v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683483031-Logi-Report-Server-Monitor-Guide-v18-Overview
updated_at: 2022-01-27T07:58:17Z
---

# Logi Report Server Monitor Guide v18 Overview

[Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683527063-Installing-and-Uninstalling-Server-Monitor)

# Logi Report Server Monitor Guide v18 Overview

This guide describes Logi Report Server Monitor, which is a standalone web-based application used to monitor the overall performance of Logi Report Server.

Logi Report Server Monitor has the following main features:

* **Inspects the status of Logi Report Server**  
  Server Monitor enables you to view the status of Servers in a cluster. It also enables you to view the status of different reports and the status of online users, and so on.
* **Shows Logi Report Server performance statistics in Graph/Text mode**  
  Server Monitor is able to generate and display a performance chart of Server according to its statistics. In this way, you can view the performance of Server in the form of Line chart Graph and Text.
* **Maintains Logi Report Server**  
  You can perform maintenance tasks from Server Monitor, such as shutting down Server, stopping waiting/running tasks, and signing out of a valid UserSession.
* **Creates profiling reports: performance reports and statistic reports**  
   By creating profiling reports using Server Monitor, you can inspect the performance of Server in a certain period of time.
* **Provides JMX remote/local monitoring feature**  
  Logi Report has constructed JMX MBeans which correspond to all the monitored objects (including Cluster, Logi Report Server, Report Task, UserSession, and the Database Connection Pool). You can use MBeanServer to find these registered MBeans and perform any operation on them. These JMX MBeans provide the same monitoring functions as with our normal Server Monitor's JSP pages.

If you want to learn about installing and uninstalling the Server Monitor, select this link: [Installing and Uninstalling Server Monitor](https://devnet.logianalytics.com/hc/en-us/articles/4405683527063-Installing-and-Uninstalling-Server-Monitor).

If you want to learn about accessing Server Monitor from the console, select this link: [Launching and Accessing Server Monitor](https://devnet.logianalytics.com/hc/en-us/articles/4405690463255-Launching-and-Accessing-Server-Monitor).

[Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683527063-Installing-and-Uninstalling-Server-Monitor)
