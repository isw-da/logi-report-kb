---
title: "Logi Report Server Cluster  Logi Report Server v18"
id: 4405683570967
section: "Logi Report Server Cluster Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683570967-Logi-Report-Server-Cluster-Logi-Report-Server-v18
updated_at: 2022-01-27T07:58:28Z
---

# Logi Report Server Cluster  Logi Report Server v18

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690634263-Seamless-Integrated-Security-Solution)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683572119-Logi-Report-Server-Cluster-Main-Features)

# Logi Report Server Cluster Logi Report Server v18

A Logi Report Server Cluster is a distributed cluster in which a group of servers work together to provide cluster-wide shared resources, security, schedule, and version services that manage multiple versions of resources. This topic describes the major benefits and infrastructure of a Logi Report Server Cluster and describes tasks that a clustered server can accomplish.

In a Logi Report Server Cluster, all clustered servers play the same role. Dynamic load balancing ensures that a cluster utilizes all the servers in the cluster efficiently. You can use Logi Report Server Monitor to monitor the entire cluster and add and remove resources. You can also set up notifications to notify administrators if any servers encounter problems.

The Logi Report Server Cluster provides the following major benefits:

* **Manageability**: You can control all users and resources from a clustered server, remotely.
* **High-Availability**: When one server fails, the cluster will re-allocate the tasks running on it to other servers. When a server has already been fully utilized, the cluster will allocate the following tasks to the other servers.
* **Scalability**: You can add or remove servers at any time according to your needs.

The following diagram illustrates the Logi Report Server Cluster infrastructure:

![Logi Report Server Cluster Infrastructure](https://devnet.logianalytics.com/hc/article_attachments/4420453677079/clstr.gif)

Every server in a distributed cluster has the same responsibility. You can set each server in a Logi Report Server Cluster by configuring its properties. The following table shows the tasks each clustered server in a server cluster can complete.

|  | Business Task | | | **Administrative Task** | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Run Reports | Submit Scheduled Tasks | Load-Balancing | Fail-over | Load-Balancing Administration | Security Administration | Resource Administration |
| **Clustered Server** | **Y** | **Y** | **Y** | **Y** | **Y** | **Y** | **Y** |

Select the following links to view the topics:

* [Logi Report Server Cluster Main Features](https://devnet.logianalytics.com/hc/en-us/articles/4405683572119-Logi-Report-Server-Cluster-Main-Features)
* [Setting Up and Starting a Logi Report Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/4405683573271-Setting-Up-and-Starting-a-Logi-Report-Server-Cluster)
* [Managing a Logi Report Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/4405690480663-Managing-a-Logi-Report-Server-Cluster)
* [Clustering Logi Report Server with Oracle WebLogic Server 12c (12.1.3)](https://devnet.logianalytics.com/hc/en-us/articles/4405690482711-Clustering-Logi-Report-Server-with-Oracle-WebLogic-Server-12c-12-1-3-)
* [Dispatching RMI Server Pages Requests in Multiple Server Environment](https://devnet.logianalytics.com/hc/en-us/articles/4405683577495-Dispatching-RMI-Server-Pages-Requests-in-Multiple-Server-Environment)

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4420453448599/criticalicon.gif) You need a [Logi Report Server Cluster license](https://devnet.logianalytics.com/hc/en-us/articles/4405683899543-Logi-Report-Licenses#Cluster) to use this feature. For more product information, including new purchases and upgrades, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690634263-Seamless-Integrated-Security-Solution)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683572119-Logi-Report-Server-Cluster-Main-Features)
