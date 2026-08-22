---
title: "Monitoring Logi Report Server"
id: 1500009777401
section: "Monitoring Logi Report Server"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009777401-Monitoring-Logi-Report-Server
updated_at: 2021-07-24T00:47:55Z
---

# Monitoring Logi Report Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777481-NLS-at-Report-Level)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748822-Monitoring-the-Server-Status)

# Monitoring Logi Report Server

Logi Report Server Monitor is a standalone web-based application to monitor the overall performance of Logi Report Server. This topic describes how you can access Server Monitor from the Server Console.

Server Monitor enables you to inspect the status of Logi Report Server, including the status of the servers in a Cluster, the status of different reports, the status of on-line users, and so on. Server Monitor can generate and display the performance chart of Server according to its statistics. Thus, you can view the performance of Server in the form of Line Chart Graph and Text. You can also use Server Monitor to maintain Server, such as shutting down Servers, stopping waiting/running tasks, and logging out a valid user session. By creating profiling reports using Server Monitor, you can inspect server performance in a certain period.

**To access Server Monitor from the Server Console:**

1. Make sure you did not change the **web.monitor.link.enable** property in the **server.properties** file in `<server_install_root>\bin` to **false**. The default value is **true**.
2. Start Logi Report Server.
3. Copy **rmi.auth** from `<server_install_root>\bin` to `<monitor_install_root>\bin`.
4. Launch **MonitorServer.bat** in `<monitor_install_root>\bin`.
5. Log onto the Server Console as an administrator.
6. Point to **Administration** on the system toolbar, and then select **Other** > **Monitor** from the drop-down menu.

Select the following links to view the topics:

* [Monitoring the Server Status](https://devnet.logianalytics.com/hc/en-us/articles/1500009748822-Monitoring-the-Server-Status)
* [Monitoring the Server Performance](https://devnet.logianalytics.com/hc/en-us/articles/1500009777421-Monitoring-the-Server-Performance)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777481-NLS-at-Report-Level)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748822-Monitoring-the-Server-Status)
