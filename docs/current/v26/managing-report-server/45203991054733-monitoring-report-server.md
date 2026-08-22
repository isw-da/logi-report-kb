---
title: "Monitoring Report Server"
id: 45203991054733
section: "Managing Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203991054733-Monitoring-Report-Server
updated_at: 2026-04-30T14:10:35Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Monitoring Report Server

Report Server Monitor is a standalone web-based application to monitor the overall performance of Report Server.  This topic describes how you can access Server Monitor from the Server Console.

Server Monitor enables you to inspect the status of Report Server, such as the status of the servers in a Cluster, the status of different reports, and the status of on-line users. Server Monitor can generate and display the performance chart of Server according to its statistics. Thus, you can view the performance of Server in the form of Line Chart Graph and Text. You can also use Server Monitor to maintain Server, such as shutting down Servers, stopping waiting/running tasks, and signing out of a valid user session. By creating profiling reports using Server Monitor, you can inspect server performance in a certain period.

To access Server Monitor from the Server Console:

- Make sure you did not change the web.monitor.link.enable property in the server.properties file in <server_install_root>\bin to false. The default value is true.

- Start Report Server.

- Copy rmi.auth from <server_install_root>\bin to <monitor_install_root>\bin.

- Launch MonitorServer.bat in <monitor_install_root>\bin.

- Sign in to the Server Console as an administrator.

- On the system toolbar, navigate to Administration > Other > Monitor.
  

Select the following links to view the topics:

- 
                    Monitoring the Server Status
                

- 
                    Monitoring the Server Performance
