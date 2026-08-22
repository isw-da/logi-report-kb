---
title: "Logi JReport Server Guide v15 Server Cluster"
id: 1500009644262
section: "Server Cluster Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644262-Logi-JReport-Server-Guide-v15-Server-Cluster
updated_at: 2021-07-24T20:55:24Z
---

# Logi JReport Server Guide v15 Server Cluster

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673241-Seamless-Integrated-Security-Solution)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668921-Logi-JReport-Server-Guide-v15-Server-Cluster-Main-Features)

# Server Cluster Logi JReport Server Guide v15

A Logi JReport Server Cluster is a distributed cluster in which a group of servers work together to provide cluster-wide shared resources, security, schedules and version services that manage multiple versions of resources. In a Logi JReport Server Cluster, all clustered servers play exactly the same role. New servers can be added to the existing cluster or removed from the cluster at any time. Dynamic load balancing ensures that all servers in the cluster are utilized efficiently and Logi JReport Server Monitor allows administrators to manage utilization for the entire cluster and add and remove resources as needed. Notifications can be set up to ensure administrators are contacted if any servers encounter problems.

The Logi JReport Server Cluster provides the following major benefits:

* **Manageability**: All users and resources can be controlled from a clustered server, remotely.
* **High-Availability**: When one server fails to perform, the tasks running on it will be re-allocated to other servers. If a server has already been fully utilized, the tasks sent to it will be allocated to the other servers.
* **Scalability**: You can add or remove servers dynamically according to your needs.

There can be many clustered servers (nodes) that play the same role in a Logi JReport Server Cluster. The following is a diagram of the Logi JReport Server Cluster infrastructure:

![JReport Server Cluster Infrastructure](https://devnet.logianalytics.com/hc/article_attachments/4404920660887/clstr.gif)

Every clustered server in this distributed cluster has the same responsibility. You can set each clustered server in a Logi JReport Server Cluster by configuring its properties. The following table shows all the tasks each clustered server in the server cluster can complete.

|  | Business tasks | | | **Administrative tasks** | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Run Reports | Submit Scheduled Tasks | Load-Balancing | Fail-over | Load-Balancing Administration | Security Administration | Resource Administration |
| **Clustered Server** | **Y** | **Y** | **Y** | **Y** | **Y** | **Y** | **Y** |

The following topics show you what features the Logi JReport Server Cluster owns, how to set it up, how to manage it and so on:

* [Logi JReport Server Cluster Main Features](https://devnet.logianalytics.com/hc/en-us/articles/1500009668921-Logi-JReport-Server-Guide-v15-Server-Cluster-Main-Features)
* [Setting Up and Starting a Logi JReport Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/1500009644282-Setting-Up-and-Starting-a-Logi-JReport-Server-Guide-v15-Server-Cluster)
* [Managing a Logi JReport Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/1500009668941-Managing-a-Logi-JReport-Server-Guide-v15-Server-Cluster)
* [Clustering Logi JReport Server With Oracle WebLogic Server 12c (12.1.3)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669001-Clustering-Logi-JReport-Server-Guide-v15-Server-with-Oracle-WebLogic-Server-12c-12-1-3-)
* [Dispatching RMI Server Pages Requests in Multiple Server Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009644362-Dispatching-RMI-Server-Pages-Requests-in-Multiple-Server-Environment)

**Note:** A [Logi JReport Server Cluster license](https://devnet.logianalytics.com/hc/en-us/articles/1500009648262-Logi-JReport-Licenses#Cluster) is required in order to use this feature. If you do not have the license, contact your Jinfonet Software account manager to obtain it.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673241-Seamless-Integrated-Security-Solution)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668921-Logi-JReport-Server-Guide-v15-Server-Cluster-Main-Features)
