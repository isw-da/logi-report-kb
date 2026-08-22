---
title: "Monitoring Logi Report Server"
id: 4405690647063
section: "Managing Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690647063-Monitoring-Logi-Report-Server
updated_at: 2022-01-27T07:59:42Z
---

# Monitoring Logi Report Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683948567-NLS-at-Report-Level)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683945367-Monitoring-the-Server-Status)

# Monitoring Logi Report Server

Logi Report Server Monitor is a standalone web-based application to monitor the overall performance of Logi Report Server. This topic describes how you can access Server Monitor from the Server Console.

Server Monitor enables you to inspect the status of Logi Report Server, such as the status of the servers in a Cluster, the status of different reports, and the status of on-line users. Server Monitor can generate and display the performance chart of Server according to its statistics. Thus, you can view the performance of Server in the form of Line Chart Graph and Text. You can also use Server Monitor to maintain Server, such as shutting down Servers, stopping waiting/running tasks, and signing out of a valid user session. By creating profiling reports using Server Monitor, you can inspect server performance in a certain period.

**To access Server Monitor from the Server Console:**

1. Make sure you did not change the **web.monitor.link.enable** property in the **server.properties** file in `<server_install_root>\bin` to **false**. The default value is **true**.
2. Start Logi Report Server.
3. Copy **rmi.auth** from `<server_install_root>\bin` to `<monitor_install_root>\bin`.
4. Launch **MonitorServer.bat** in `<monitor_install_root>\bin`.
5. Sign in to the Server Console as an administrator.
6. On the system toolbar, navigate to **Administration** > **Other** > **Monitor**.

Select the following links to view the topics:

* [Monitoring the Server Status](https://devnet.logianalytics.com/hc/en-us/articles/4405683945367-Monitoring-the-Server-Status)
* [Monitoring the Server Performance](https://devnet.logianalytics.com/hc/en-us/articles/4405683944343-Monitoring-the-Server-Performance)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683948567-NLS-at-Report-Level)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683945367-Monitoring-the-Server-Status)
