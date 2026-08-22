---
title: "Managing a Logi Report Server Cluster"
id: 1500009771321
section: "Logi Report Server Cluster Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009771321-Managing-a-Logi-Report-Server-Cluster
updated_at: 2021-07-24T00:49:32Z
---

# Managing a Logi Report Server Cluster

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743442-Example-2-Setting-Up-a-Logi-Report-Server-Cluster-for-a-Production-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771441-Clustering-Logi-Report-Server-with-Oracle-WebLogic-Server-12c-12-1-3-)

# Managing a Logi Report Server Cluster

You can manage the servers in a Logi Report Server cluster if you are an administrator, using the Server Console. This topic describes how to manage your server clusters using the Server Console.

You can configure the performance weight for the clustered servers, balance the server load to make the servers work more effectively, and use Logi Report Server Monitor to monitor the status of each clustered server.

This topic contains the following sections:

* [Configuring Performance Weight](#Weight)
* [Balancing the Server Load](#Load)
* [Monitoring Clustered Servers](#Monitor)

## Configuring Performance Weight

If you have chosen the [Weighted Min-load](https://devnet.logianalytics.com/hc/en-us/articles/1500009771301-Logi-Report-Server-Cluster-Main-Features#Weight) (loadbalance.type=2) algorithm for load balancing when creating a cluster, you will have to configure a performance weight for each clustered server in the cluster. The higher performance weight you set to a clustered server, the higher chance it may get selected by the server that has the active scheduler during load balancing.

**To configure performance weight**:

1. Start a clustered server in the cluster and [log onto the Server Console](https://devnet.logianalytics.com/hc/en-us/articles/1500009777061-Accessing-Logi-Report-Server-via-a-Web-Browser).
2. Point to **Administration** on the system toolbar, select **Configuration** > **Cluster** > **Weight** from the drop-down menu to display the Weight page.

   ![Cluster - Weight page](https://devnet.logianalytics.com/hc/article_attachments/4404885616791/clstr_mng_weight.gif)
3. In the weight table, specify a weight value for each clustered server manually.
   Performance weight is a positive float number.
4. Select **OK** to save the weight values.
5. If you want to test each clustered server's performance weight value at current time, specify a catalog and a report that will be used for the testing in the Catalog and Report text boxes and then select **Test**.

The following two examples show how Least Weighted Current Reports algorithm works:

**Example 1 - when there are free servers:**

| Active Servers | ServerA | ServerB | ServerC | Comments |
| --- | --- | --- | --- | --- |
| Is local server | TRUE | FALSE | FALSE |  |
| Maximum concurrent reports | 8 | Unlimited | 5 |  |
| Number of currently running reports | 6 | 6 | 5 |  |
| Performance weight | 10 | 10 | 10 |  |
| Calculation | | | | |
| Weighted current reports | 0.6 | 0.6 | 0.5 |  |
| Is free | TRUE | TRUE | FALSE | Current < MaxConcurrent, or MaxConcurrent is unlimited |
| Candidate servers | YES | YES |  | Select from free servers |
| Candidate servers | YES | YES |  | Select servers which have the least Weighted current reports |
| Selected server | YES |  |  | Local server has higher priority |

**Example 2 - when there are no free servers:**

| Active Servers | ServerA | ServerB | ServerC | Comments |
| --- | --- | --- | --- | --- |
| Is local server | TRUE | FALSE | FALSE |  |
| Maximum concurrent reports | 10 | 10 | 10 |  |
| Number of currently running reports | 10 | 10 | 10 |  |
| Performance weight | 4 | 5 | 8 |  |
| Calculation | | | | |
| Weighted current reports | 2.5 | 2 | 1.25 |  |
| Is free | FALSE | FALSE | FALSE | Current < MaxConcurrent, or MaxConcurrent is unlimited |
| Candidate servers | YES | YES | YES | Selects from all servers when all servers are full |
| Candidate servers |  |  | YES | Select servers which have the least Weighted current reports |
| Selected server |  |  | YES | Select ServerC |

## Balancing the Server Load

In a cluster environment, Logi Report Server provides a [load balancing mechanism](https://devnet.logianalytics.com/hc/en-us/articles/1500009771301-Logi-Report-Server-Cluster-Main-Features#LoadBalance) which enables the server to work more effectively.

**Load balancing process**

1. When the time of a scheduled task arrives, active schedulers compete, and the winner gets to trigger the schedule.
2. The server that has the active scheduler selects a server in the cluster according to the load balancing algorithm specified which can either be a built-in one or a customized one, and then sends the task to the selected server.

**Tip:** You can also directly specify a server in a cluster to perform a scheduled task instead of using load balancing. To do this, first make sure that you have enabled the [Identify Server Preference](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile#Identify) option in the server profile, and then use the Specify a preferred server to run the task option in the General tab of the Schedule dialog box to specify a server manually.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)For the load balancing algorithms: the server that holds the active scheduler selects from the servers with the number of concurrently running reports less than maximum number first. However, if all servers are full, it will select from all of them.

You can also write your own load balancing algorithm based on the API included in Logi Report Server. For more information, see [Writing Customized Load Balancing Algorithm via API](https://devnet.logianalytics.com/hc/en-us/articles/1500009770981-Writing-Customized-Load-Balancing-Algorithm).

## Monitoring Clustered Servers

If you have [Logi Report Server Monitor](https://devnet.logianalytics.com/hc/en-us/articles/1500009777401-Monitoring-Logi-Report-Server) installed, you can use it to monitor the status of each clustered server. First, you should do the following:

1. Modify the server.properties file in `<monitor_install_root>\bin` to configure the IP address and port information of one clustered server.
2. Copy rmi.auth from `<server_install_root>\bin` of the clustered server whose IP address and port information you modified in the last step to `<monitor_install_root>\bin`, or remove rmi.auth from `<server_install_root>\bin` of this clustered server.
3. Start Logi Report Server.
4. Copy **rmi.auth** from `<server_install_root>\bin` to `<monitor_install_root>\bin`.
5. Launch MonitorServer.bat in `<monitor_install_root>\bin` to start Logi Report Server Monitor.
6. Access Logi Report Server Monitor using `http://monitorhost:monitorport` (default port is 8848), or by selecting **Monitor** on the Administration > Other drop-down menu in the Server Console.

   You can specify the monitor port by setting **monitor.jmx.htmladaptor.port** in the server.properties file in `<server_install_root>\bin`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743442-Example-2-Setting-Up-a-Logi-Report-Server-Cluster-for-a-Production-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771441-Clustering-Logi-Report-Server-with-Oracle-WebLogic-Server-12c-12-1-3-)
