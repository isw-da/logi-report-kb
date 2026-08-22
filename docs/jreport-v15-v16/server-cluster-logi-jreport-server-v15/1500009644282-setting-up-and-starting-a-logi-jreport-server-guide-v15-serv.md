---
title: "Setting Up and Starting a Logi JReport Server Guide v15 Server Cluster"
id: 1500009644282
section: "Server Cluster Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644282-Setting-Up-and-Starting-a-Logi-JReport-Server-Guide-v15-Server-Cluster
updated_at: 2021-07-24T20:55:24Z
---

# Setting Up and Starting a Logi JReport Server Guide v15 Server Cluster

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668921-Logi-JReport-Server-Guide-v15-Server-Cluster-Main-Features)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644342-Setting-Up-and-Configuring-a-Logi-JReport-Server-Guide-v15-Server-Cluster)

# Setting Up and Starting a Logi JReport Server Cluster

This topic introduces the steps for setting up a Logi JReport Server Cluster and starting it. Here, it is assumed that you already have a general idea about the infrastructure of Logi JReport Server Clusters and know the functions of the clustered servers. If this isn't the case, refer to the previous topics.

To set up a Logi JReport Server Cluster, the following factors should be considered:

* How many servers will be included in the cluster?

  The maximum number of servers is unlimited as long as you install Logi JReport Server with the license key for cluster. Based on your expected load and protection from system failures you can create 2 or more nodes for your cluster. Often with multi-cpu and multi-core systems you will get better overall throughput having several nodes on a single server. Only by testing in your environment will you be able to find the number of nodes to give you the highest performance. Too few and resources will be under utilized and too many will cause thrashing and lower throughput.
* Whether to use the distributed storage feature in the cluster?

  In a distributed cluster the files may be stored on any node in the cluster. You can set how many copies will be made in the cluster and if you need to access the files from another node, Logi JReport cluster will copy them to this node from the node it is stored on. As a result, you can access your required files from anywhere in the cluster. If the copy number is 0, then it means every node of the cluster will get a copy.

  The tradeoff is overall system performance versus individual user performance when a user requests a report result. If you set Number of Copies to 0, the system will copy every resource file to every node, slowing overall throughput considerably. However, setting Number of Copies to 1 will keep a single copy just on the node where it was created which provides maximum system throughput but when a user requests a resource which is not on his node he then needs to wait for it to be copied before he can view it. If the node goes down though then the resource is unreachable. A setting of 2 is the default which allows for failover if a node goes down but just does a single copy.

* Whether to use the default Derby DBMS or use your own DBMS?

  Logi JReport includes the Apache Derby DBMS for the server data such as resources and users, groups and roles and a lot of other information. By default each installed node creates its own database in `<install_root>/derby`. In order to use a Logi JReport cluster, all nodes must use the same database. Select one of the nodes to manage the Derby DBMS and ensure that all the other nodes point to this same instance. For an example, review the sample configuration [Case 1](https://devnet.logianalytics.com/hc/en-us/articles/1500009668961-Example-1-Setting-Up-a-Simple-Logi-JReport-Server-Guide-v15-Server-Cluster).

  Another option to consider is using your own DBMS for the server database. If you already have a reliable DBMS which is already being backed up and provides the reliability you need such as MySQL or Oracle we recommend you change the system DBMS to use your own managed DBMS rather than maintain a separate one for Logi JReport. For information on how to configure Logi JReport to use a different system DBMS, refer to [Configure the Server Database](https://devnet.logianalytics.com/hc/en-us/articles/1500009669081-Configuring-the-Server-Database).

Following are steps and examples on how to set up and start a Logi JReport Server Cluster:

* [Setting Up and Configuring a Logi JReport Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/1500009644342-Setting-Up-and-Configuring-a-Logi-JReport-Server-Guide-v15-Server-Cluster)
* [Starting a Logi JReport Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/1500009668981-Starting-a-Logi-JReport-Server-Guide-v15-Server-Cluster)
* [Example 1: Setting Up a Simple Logi JReport Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/1500009668961-Example-1-Setting-Up-a-Simple-Logi-JReport-Server-Guide-v15-Server-Cluster)
* [Example 2: Setting Up a Logi JReport Server Cluster for a Production Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009644322-Example-2-Setting-Up-a-Logi-JReport-Server-Guide-v15-Server-Cluster-for-a-Production-Environment)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668921-Logi-JReport-Server-Guide-v15-Server-Cluster-Main-Features)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644342-Setting-Up-and-Configuring-a-Logi-JReport-Server-Guide-v15-Server-Cluster)
