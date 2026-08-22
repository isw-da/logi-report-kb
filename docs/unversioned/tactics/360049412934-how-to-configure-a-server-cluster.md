---
title: "How to Configure a Server Cluster"
id: 360049412934
section: "Tactics"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360049412934-How-to-Configure-a-Server-Cluster
updated_at: 2020-07-28T12:05:09Z
---

# How to Configure a Server Cluster

This KB article assumes that you already have a general idea about the infrastructure of Logi Report Server Clusters and know the functions of the clustered servers. If this isn’t the case, refer to [Logi Report Server Cluster](https://documentation.logianalytics.com/logireportserverguidev17/content/html/cluster/clstr.htm).

To set up a Logi Report Server Cluster, the following factors should be considered:

### How many servers will be included in the cluster?

The maximum number of servers is unlimited as long as you install Logi Report Server with the license key for clustering. Based on your expected load and protection from system failures you can create 2 or more server nodes for your cluster. Often with multi-CPU and multi-core systems you will get better overall throughput having several nodes on a single machine. Only by testing in your environment will you be able to find the number of nodes to give you the highest performance. Too few and resources will be under utilized and too many will cause thrashing and lower throughput. You may consider these factors: the number of reports to run concurrently, the ways they run, the types of the reports, whether they consume CPU or memory, and so on.

### When to use the distributed storage feature in the cluster?

In a distributed cluster the files may be stored on any node in the cluster. You can set how many copies will be made in the cluster and if you need to access the files from another node, Logi Report Server Cluster will copy them to this node from the node it is stored on. As a result, you can access your required files from anywhere in the cluster. If the copy number is 0, then it means every node of the cluster will get a copy.

The tradeoff is overall system performance versus individual user performance when a user requests a report result. If you set Number of Copies to 0, the system will copy every resource file to every node, slowing overall throughput considerably. However, setting Number of Copies to 1 will keep a single copy just on the node where it was created which provides maximum system throughput but when a user requests a resource which is not on his node he then needs to wait for it to be copied before he can view it. If the node goes down though then the resource is unreachable. A setting of 2 is the default, which allows for failover if a node goes down but just does a single copy.

[Click here](https://documentation.logianalytics.com/logireportserverguidev17/content/html/cluster/clstr_featr.htm) to get more information about distributed storage.

### When to use the default Derby DBMS for the system database or use your own DBMS?

Report includes the Apache Derby DBMS for the server data such as resources and users, groups and roles, and a lot of other system information. By default, each installed node creates its own database in <install\_root>\derby. In order to use a Logi Report Server Cluster, all nodes must use the same database. Select one of the nodes to manage the Derby DBMS and ensure that all the other nodes point to this same instance. For an example, review the sample configuration [Case 1](https://documentation.logianalytics.com/logireportserverguidev17/content/html/cluster/clstr_set_case1.htm).

Another option to consider is using your own DBMS for the system database. If you already have a reliable DBMS which is already being backed up and provides the reliability you need, such as MySQL or Oracle, we recommend you change the system DBMS to use an instance of your own managed DBMS rather than maintain a separate one for Logi Report. For information on how to configure Logi Report to use a different system DBMS, refer to [Configure the server database](https://documentation.logianalytics.com/logireportserverguidev17/content/html/config/config_db.htm).

The following are steps and examples on how to set up and start a Logi Report Server Cluster:

[Setting up and configuring a Logi Report Server Cluster](https://documentation.logianalytics.com/logireportserverguidev17/content/html/cluster/clstr_set_set.htm)  
[Starting a Logi Report Server Cluster](https://documentation.logianalytics.com/logireportserverguidev17/content/html/cluster/clstr_set_start.htm)  
[Example 1: Setting up a simple Logi Report Server Cluster](https://documentation.logianalytics.com/logireportserverguidev17/content/html/cluster/clstr_set_case1.htm)  
[Example 2: Setting up a Logi Report Server Cluster for a production environment](https://documentation.logianalytics.com/logireportserverguidev17/content/html/cluster/clstr_set_case2.htm)
