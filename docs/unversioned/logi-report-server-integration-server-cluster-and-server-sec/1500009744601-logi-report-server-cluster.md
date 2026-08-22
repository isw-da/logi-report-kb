---
title: "Logi Report Server Cluster"
id: 1500009744601
section: "Logi Report Server Integration, Server Cluster, and Server Security Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744601-Logi-Report-Server-Cluster
updated_at: 2021-07-25T07:20:19Z
---

# Logi Report Server Cluster

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722882-Seamless-Integrated-Security-Solution)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718662-Logi-Report-Server-Cluster-Main-Features)

# Logi Report Server Cluster

A Logi Report Server Cluster is a distributed cluster in which a group of servers work together to provide cluster-wide shared resources, security, schedule, and version services that manage multiple versions of resources. In a Logi Report Server Cluster, all clustered servers play the same role. Dynamic load balancing ensures that a cluster utilizes all the servers in the cluster efficiently. You can use Logi Report Server Monitor to monitor the entire cluster and add and remove resources. You can also set up notifications to notify administrators if any servers encounter problems. This topic describes the major benefits and infrastructure of a Logi Report Server Cluster and describes tasks that a clustered server can accomplish.

The Logi Report Server Cluster provides the following major benefits:

* **Manageability**: You can control all users and resources from a clustered server, remotely.
* **High-Availability**: When one server fails, the cluster will re-allocate the tasks running on it to other servers. When a server has already been fully utilized, the cluster will allocate the following tasks to the other servers.
* **Scalability**: You can add or remove servers at any time according to your needs.

The following diagram illustrates the Logi Report Server Cluster infrastructure:

![Logi Report Server Cluster Infrastructure](https://devnet.logianalytics.com/hc/article_attachments/4404936965015/clstr.gif)

Every server in a distributed cluster has the same responsibility. You can set each server in a Logi Report Server Cluster by configuring its properties. The following table shows the tasks each clustered server in a server cluster can complete.

|  | Business Task | | | **Administrative Task** | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Run Reports | Submit Scheduled Tasks | Load-Balancing | Fail-over | Load-Balancing Administration | Security Administration | Resource Administration |
| **Clustered Server** | **Y** | **Y** | **Y** | **Y** | **Y** | **Y** | **Y** |

Select the following links to view the topics:

* [Logi Report Server Cluster Main Features](https://devnet.logianalytics.com/hc/en-us/articles/1500009718662-Logi-Report-Server-Cluster-Main-Features)
* [Setting Up and Starting a Logi Report Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/1500009744621-Setting-Up-and-Starting-a-Logi-Report-Server-Cluster)
* [Managing a Logi Report Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/1500009718682-Managing-a-Logi-Report-Server-Cluster)
* [Clustering Logi Report Server with Oracle WebLogic Server 12c (12.1.3)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718742-Clustering-Logi-Report-Server-with-Oracle-WebLogic-Server-12c-12-1-3-)
* [Dispatching RMI Server Pages Requests in Multiple Server Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009744681-Dispatching-RMI-Server-Pages-Requests-in-Multiple-Server-Environment)

**Note:** A [Logi Report Server Cluster license](https://devnet.logianalytics.com/hc/en-us/articles/1500009749561-Logi-Report-licenses#Cluster) is required in order to use this feature. If you do not have the license, contact your Logi Analytics account manager to obtain it.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722882-Seamless-Integrated-Security-Solution)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718662-Logi-Report-Server-Cluster-Main-Features)
