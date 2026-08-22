---
title: "Report Server Cluster Report Server v25"
id: 35498445683341
section: "Report Server Cluster Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/35498445683341-Report-Server-Cluster-Report-Server-v25
updated_at: 2026-02-26T02:11:11Z
source_host: docs-report.zendesk.com
---
# 
Report Server ClusterReport Server v25

A Report Server Cluster is a distributed cluster in which a group of servers work together to provide cluster-wide shared resources, security, schedule, and version services that manage multiple versions of resources.  This topic describes the major benefits and infrastructure of a Report Server Cluster and describes tasks that a clustered server can accomplish.

In a Report Server Cluster, all clustered servers play the same role. Dynamic load balancing ensures that a cluster utilizes all the servers in the cluster efficiently. You can use Report Server Monitor to monitor the entire cluster and add and remove resources. You can also set up notifications to notify administrators if any servers encounter problems.

The Report Server Cluster provides the following major benefits:

- 
Manageability: You can control all users and resources from a clustered server, remotely.

- 
High-Availability: When one server fails, the cluster will re-allocate the tasks running on it to other servers. When a server has already been fully utilized, the cluster will allocate the following tasks to the other servers.

- 
Scalability: You can add or remove servers at any time according to your needs.

The following diagram illustrates the Report Server Cluster infrastructure:

Every server in a distributed cluster has the same responsibility. You can set each server in a Report Server Cluster by configuring its properties. The following table shows the tasks each clustered server in a server cluster can complete.

|  | Business Task | Administrative Task |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Run Reports | Submit Scheduled Tasks | Load-Balancing | Fail-over | Load-Balancing Administration | Security Administration | Resource Administration |
| Clustered Server | Y | Y | Y | Y | Y | Y | Y |

Select the following links to view the topics:

- Report Server Cluster Main Features

- Setting Up and Starting a Report Server Cluster

- Managing a Report Server Cluster

- Clustering Report Server with Oracle WebLogic Server 12c (12.1.3)

- Dispatching RMI Server Pages Requests in Multiple Server Environment

 You need a Report Server Cluster license to use this feature. For more product information, including new purchases and upgrades, contact US Sales or UK Sales.
