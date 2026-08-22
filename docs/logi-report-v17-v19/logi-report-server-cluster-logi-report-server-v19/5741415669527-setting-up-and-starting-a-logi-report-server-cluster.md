---
title: "Setting Up and Starting a Logi Report Server Cluster"
id: 5741415669527
section: "Logi Report Server Cluster Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741415669527-Setting-Up-and-Starting-a-Logi-Report-Server-Cluster
updated_at: 2022-10-31T17:15:56Z
---

# Setting Up and Starting a Logi Report Server Cluster

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741415586199-Logi-Report-Server-Cluster-Main-Features)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741400931479-Setting-Up-and-Configuring-a-Logi-Report-Server-Cluster)

# Setting Up and Starting a Logi Report Server Cluster

This topic describes the factors you should consider before setting up a Logi Report Server Cluster: the number of servers you want in the cluster, whether to use the distributed storage feature, and whether to use your DBMS as the system database.

You should already have a general idea about the infrastructure of Logi Report Server Cluster, and know the functions of the clustered servers. If this is not the case, read the [previous Cluster topics](https://devnet.logianalytics.com/hc/en-us/articles/5741415572759-Logi-Report-Server-Cluster-Logi-Report-Server-v19) first.

To set up a Logi Report Server Cluster, you should consider the following factors:

* How many servers will be included in the cluster?

  The maximum number of servers is unlimited as long as you install Logi Report Server with the license key for clustering. Based on your expected load and protection from system failures you can create 2 or more server nodes for your cluster. Often with multi-CPU and multi-core systems you will get better overall throughput having several nodes on a single machine. Only by testing in your environment will you be able to find the number of nodes to give you the highest performance. Too few and resources will be underutilized and too many will cause thrashing and lower throughput. You may consider factors such as the number of reports to run concurrently, the ways they run, the types of the reports, and whether they consume CPU or memory.
* Whether to use the distributed storage feature in the cluster?

  In a distributed cluster the files may be stored on any server node in the cluster. You can set how many copies will be made in the cluster and if you need to access the files from another node, Logi Report Server Cluster will copy them to this node from the node it is stored on. As a result, you can access your required files from anywhere in the cluster. If the copy number is 0, then it means every node of the cluster will get a copy.

  The tradeoff is overall system performance versus individual user performance when a user requests a report. If you set Number of Copies to 0, the system will copy every resource file to every node, slowing overall throughput considerably. However, setting Number of Copies to 1 will keep a single copy just on the node where it was created which provides maximum system throughput but when a user requests a resource which is not on his node he then needs to wait for it to be copied before he can view it. If the node goes down, then the resource is unreachable. A setting of 2 is the default which allows for failover if a node goes down but just does a single copy.

  For more information, see [Distributed Resource Storage](https://devnet.logianalytics.com/hc/en-us/articles/5741415586199-Logi-Report-Server-Cluster-Main-Features#Distribute).

* Whether to use the default Derby DBMS for the system database or use your own DBMS?

  Logi Report includes the Apache Derby DBMS for the server data such as resources and users, groups and roles and a lot of other system information. By default, each installed node creates its own database in `<install_root>\derby`. In order to use a Logi Report Server Cluster, all nodes must use the same database. Select one of the nodes to manage the Derby DBMS and ensure that all the other nodes point to this same instance. For an example, review the sample configuration [Case 1](https://devnet.logianalytics.com/hc/en-us/articles/5741408854807-Example-1-Setting-Up-a-Simple-Logi-Report-Server-Cluster).

  Another option to consider is using your own DBMS for the system database. If you already have a reliable DBMS which is already being backed up, and provides the reliability you need such as MySQL or Oracle, you should change the system DBMS to use an instance of your own managed DBMS rather than maintain a separate one for Logi Report. For information on how to configure Logi Report to use a different system DBMS, refer to [Configuring Server Databases for Server Metadata](https://devnet.logianalytics.com/hc/en-us/articles/5741387194519-Configuring-Server-Databases-for-Server-Metadata).

The following are steps and examples on how to set up and start a Logi Report Server Cluster:

* [Setting Up and Configuring a Logi Report Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/5741400931479-Setting-Up-and-Configuring-a-Logi-Report-Server-Cluster)
* [Starting a Logi Report Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/5741386996247-Starting-a-Logi-Report-Server-Cluster)
* [Example 1: Setting Up a Simple Logi Report Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/5741408854807-Example-1-Setting-Up-a-Simple-Logi-Report-Server-Cluster)
* [Example 2: Setting Up a Logi Report Server Cluster for a Production Environment](https://devnet.logianalytics.com/hc/en-us/articles/5741408868375-Example-2-Setting-Up-a-Logi-Report-Server-Cluster-for-a-Production-Environment)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741415586199-Logi-Report-Server-Cluster-Main-Features)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741400931479-Setting-Up-and-Configuring-a-Logi-Report-Server-Cluster)
