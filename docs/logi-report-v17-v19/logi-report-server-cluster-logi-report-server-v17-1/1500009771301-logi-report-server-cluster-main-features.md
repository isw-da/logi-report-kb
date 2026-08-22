---
title: "Logi Report Server Cluster Main Features"
id: 1500009771301
section: "Logi Report Server Cluster Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009771301-Logi-Report-Server-Cluster-Main-Features
updated_at: 2021-07-24T00:49:31Z
---

# Logi Report Server Cluster Main Features

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743402-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771341-Setting-Up-and-Starting-a-Logi-Report-Server-Cluster)

# Logi Report Server Cluster Main Features

This topic describes the main features of the Logi Report Server Cluster: administration of security and resources, load balancing algorithms, fail-over mechanism, and distributed resource storage. With these features in mind, you will be able to understand and use Logi Report Server Cluster better. You can also use some of the features via API.

This topic contains the following sections:

* [Administering Security and Resources](#Admin)
* [Load Balancing](#LoadBalance)

+ [Load Balancing for Interactive Reports](#Report)
+ [Load Balancing for Scheduled Tasks](#Task)

* [Failover](#Failover)
* [Distributed Resource Storage](#Distribute)

## Administering Security and Resources

You can accomplish all administrative tasks from any single node in a distributed cluster. Log onto the cluster from a clustered server as an administrator and you can perform the following security tasks:

* Create, remove, and edit users, groups, realms, protections, and ACLs.
* Edit resource nodes and sub resource nodes. Add reachable virtual resource nodes.
* Customize the default page appearance for users.

## Load Balancing

Here are the benefits of deploying load balancing in a Logi Report Server Cluster.

* Automatically allocates tasks to suitable servers according to their current load and performance.
* Makes sure that all of the servers in the cluster are fully utilized.
* Automatically re-balances the network load when one server is added or removed.

For scheduled tasks and tasks submitted from interactive reports (reports that run in Page Report Studio, Web Report Studio, JDashboard, or Visual Analysis), Logi Report adopts different load balancing mechanisms to enable the servers to work more effectively.

### Load Balancing for Interactive Reports

Logi Report has a built-in dispatcher to do load balancing when running interactive reports in a cluster environment. The built-in dispatcher uses an internal load balancing algorithm which relies on computing resources such as memory and CPU usage at report level to balance load. When an interactive report is opened, Logi Report will compute those resources and then allocate the most suitable server to the report. All later requests from the report will be performed on the server thereafter.

You can also implement a customized dispatcher to do load balancing. However, it is difficult to do this. First, you need to provide all server nodes in the cluster in advance. What's more, you can only implement a session-level dispatcher.

### Load Balancing for Scheduled Tasks

**Cluster Scheduler Lease**

Every clustered server has a scheduler, and among the schedulers those with a lease are active schedulers. When the time of a scheduled task arrives, active schedulers compete, and the winner gets to trigger the schedule. When dispatching tasks, the server which has the active scheduler will select a server according to load balancing algorithm and allocate the task to it.

By default, in a Logi Report Server Cluster all nodes of the cluster compete to become the active scheduler when the time of a scheduled task arrives. If the scheduled task has been bound with a trigger, then the node who gets the trigger becomes the active scheduler. The active scheduler for the task will then determine the server that will be asked to run the scheduled report based on load balancing. The Cluster Scheduler Lease option enables you to limit the number of servers competing for each scheduled report by setting a Cluster Scheduler Lease Active Count. If the count is less than the total number of nodes in the cluster, only the nodes holding a lease will compete to become the scheduler for the report that is ready to run. Depending on the number of scheduled reports you have, you may find that setting the Lease Active Count to 1 or 2 will provide more overall throughput on the system so the other nodes never have to be concerned about scheduled tasks.

You can set two additional parameters:

* **Cluster Scheduler Lease Valid Time** will set the amount of time that the lease holder will continue to compete for scheduled tasks to run. The default value is 300 seconds.
* **Cluster Schedule Lease Check Interval** will set the amount of time between when other non-lease nodes will check to see if a lease is available to pick up. The default value is 30 seconds, that is, every 30 seconds all the other nodes will check to see if one of the lease semaphores is available to take. The number of semaphores is set by the **Cluster Scheduler Lease Active Count**.

**Load detection**

There is a Logi Report Server residing in each node of a Logi Report Server Cluster. The main factor that affects load balancing is the number of concurrent reports that are running on every Logi Report Server. To avoid heavy load, every member server in the cluster needs to send the number of concurrently running reports on it to the other cluster nodes.

**Built-In Load Balancing Algorithms**

Logi Report Server Cluster supports several algorithms for load balancing clustered servers. You can choose one of them

* **Min-load (loadbalance.type=0)**  
   The server that has the active scheduler will select the server which has the least number of currently running reports. If the local server is one of the qualified servers, it will be given higher priority.
* **Round Robin (loadbalance.type=1)**  
   The server that has the active scheduler will select each server in sequence one by one until each has been allocated a report to run then will repeat the cycle. This is the default setting.
* **Weighted Min-load (loadbalance.type=2)**  
   The server that has the active scheduler will select the server that has the least weighted current reports. If the local server is one of the qualified servers, it will be given higher priority.

  |  |  |
  | --- | --- |
  |  | Number of currently running reports |
  | Weighted current reports= | --- |
  |  | Performance Weight |

  Performance weight is a positive floating-point number that you set to each server in a cluster on any clustered server. Use the Administration > Configuration > Cluster > Weight page in the Server Console and measure the performance of a typical report on each node of the cluster. The higher performance weight you set to a clustered server, the higher chance it may get selected by the server that holds the active scheduler during load balancing. See [Configuring Performance Weight](https://devnet.logianalytics.com/hc/en-us/articles/1500009771321-Managing-a-Logi-Report-Server-Cluster#Weight) for how to set performance weight and how this algorithm works.

  If you do not set performance weight, by default the algorithm will work the same as Round Robin.
* **Random (loadbalance.type=3)**  
   The server that holds the active scheduler will select the server randomly.

## Failover

You can check the status of the clustered servers on Logi Report Server Monitor and notice the failure of any member server. If a member server is down, Logi Report Server Cluster will remove it from the active clustered server list.

**Member server failure**

* **Effect on load balancing**When Logi Report Server Cluster detects a failed member server, it will remove the member server from the active server list and will not schedule reporting tasks to that server anymore. Load balancing will proceed on the remaining active servers.
* **Effect on incomplete tasks**When Logi Report Server Cluster detects a failed clustered server, it will check the shared table for the list of incomplete tasks and will then reassign all incomplete tasks to other active servers using the load balancer.
* **Effect on completed tasks**Logi Report supports only report level recovery but not session level recovery. Once a report task is completed, it will be written to temporary storage for redirection to the requester. Failure after that will not be recovered.

**Notifying of server down**

If you have enabled the notifying of server down feature, when a member server crashes or is disconnected with the cluster, Logi Report Server Cluster will send a notification e-mail to a specified address.

## Distributed Resource Storage

In a pure distributed cluster, the resource files are not stored in a central place. Each server has its own directories to hold all types of resources including catalogs, templates, dashboards, and report results. The sharing of resources among servers is achieved via a copying mechanism. More copies of resources reduce the possibility of resources being lost if a server goes down. However, too many copies consume system resources when some of them are never used.

There are two copying scenarios. One is when a resource is saved, Logi Report will copy the resource to other randomly selected servers within the cluster, according to an argument: the number of copies allowed for this type of resource. The saved resource itself is regarded as a copy. That is, in the case when copy number is three, two other random servers will each be given a copy of the resource.

The other is on demand when a resource does not exist on the local server. Logi Report will search among the other servers for the resource and copy it to the local server.

The controllable number of copies argument is available to administrator users when configuring the cluster. These types of resources support distribution: history resources which are resources saving into the versioning system, realm resources, CRD results that are cached report results, and memory storage related resources. You will be able to find the number of copies setting for each type.

The best number to use for each resource depends on two factors, how many points of failure do you want to tolerate and how often resources which are not local are requested by users.  For example, on a 10 node system, you might want to still run in case any two nodes go down.  In this case, you would want the number of copies to be three.  Any two nodes could go down and there would still be one with a copy of the resources.  However, if there is a lot of on-demand requests that require copies you might find that a higher number actually provides better average performance for your users since they are not waiting for resources when they make on-demand requests.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743402-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771341-Setting-Up-and-Starting-a-Logi-Report-Server-Cluster)
