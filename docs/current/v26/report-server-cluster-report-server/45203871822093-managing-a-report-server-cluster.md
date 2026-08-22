---
title: "Managing a Report Server Cluster"
id: 45203871822093
section: "Report Server Cluster Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203871822093-Managing-a-Report-Server-Cluster
updated_at: 2026-04-30T14:07:54Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Managing a Report Server Cluster 

You can manage the servers in a Report Server cluster if you are an administrator, using the Server Console. This topic describes how to manage your server clusters using the Server Console.

You can configure the performance weight for the clustered servers, balance the server load to make the servers work more effectively, and use Report Server Monitor to monitor the status of each clustered server. 

This topic contains the following sections:

- Configuring Performance Weight

- Balancing the Server Load

- Monitoring Clustered Servers

## 
Configuring Performance Weight

If you have chosen the Weighted Min-load (loadbalance.type=2) algorithm for load balancing when creating a cluster, you will have to configure a performance weight for each clustered server in the cluster. The higher performance weight you set to a clustered server, the higher chance it may get selected by the server that has the active scheduler during load balancing. 

To configure performance weight:

- Start a clustered server in the cluster and sign in to the Server Console.

- On the system toolbar, navigate to Administration > Configuration > Cluster > Weight. Server displays the Weight page.
    

- In the weight table, specify a weight value for each clustered server manually.
 Performance weight is a positive float number.

- Select OK to save the weight values.

- If you want to test each clustered server's performance weight value at current time, specify a catalog and a report that will be used for the testing in the Catalog and Report text boxes and then select Test. 

The following two examples show how Least Weighted Current Reports algorithm works:

Example 1 - when there are free servers:

| Active Servers | ServerA | ServerB | ServerC | Comments |
| --- | --- | --- | --- | --- |
| Is local server | TRUE | FALSE | FALSE |  |
| Maximum concurrent reports | 8 | Unlimited | 5 |  |
| Number of currently running reports | 6 | 6 | 5 |  |
| Performance weight | 10 | 10 | 10 |  |
| Calculation |  |  |  |  |
| Weighted current reports | 0.6 | 0.6 | 0.5 |  |
| Is free | TRUE | TRUE | FALSE | Current Example 2 - when there are no free servers:

| Active Servers | ServerA | ServerB | ServerC | Comments |
| --- | --- | --- | --- | --- |
| Is local server | TRUE | FALSE | FALSE |  |
| Maximum concurrent reports | 10 | 10 | 10 |  |
| Number of currently running reports | 10 | 10 | 10 |  |
| Performance weight | 4 | 5 | 8 |  |
| Calculation |  |  |  |  |
| Weighted current reports | 2.5 | 2 | 1.25 |  |
| Is free | FALSE | FALSE | FALSE | Current 

## 
Balancing the Server Load

In a cluster environment, Report Server provides a load balancing mechanism which enables the server to work more effectively.

Load balancing process

- When the time of a scheduled task arrives, active schedulers compete, and the winner gets to trigger the schedule. 

- The server that has the active scheduler selects a server in the cluster according to the load balancing algorithm specified which can either be a built-in one or a customized one, and then sends the task to the selected server.

Tip: You can also directly specify a server in a cluster to perform a scheduled task instead of using load balancing. To do this, first make sure that you have enabled the Identify Server Preference option  in the server profile, and then use the Specify a preferred server to run the task option in the General tab of the Schedule dialog box to specify a server manually.

 For the load balancing algorithms: the server that holds the active scheduler selects from the servers with the number of concurrently running reports less than maximum number first. However, if all servers are full, it will select from all of them. 

You can also write your own load balancing algorithm based on the API included in Report Server. For more information, see Writing Customized Load Balancing Algorithm via API.

## 
Monitoring Clustered Servers

If you have Report Server Monitor installed, you can use it to monitor the status of each clustered server. First, you should do the following:

- Modify the server.properties file in <monitor_install_root>\bin to configure the IP address and port information of one clustered server.

- Copy rmi.auth from <server_install_root>\bin of the clustered server whose IP address and port information you modified in the last step to <monitor_install_root>\bin, or remove rmi.auth from <server_install_root>\bin of this clustered server.

- Start Report Server. 

- Copy rmi.auth from <server_install_root>\bin to <monitor_install_root>\bin.

- Launch MonitorServer.bat in <monitor_install_root>\bin to start Report Server Monitor.

- Access Report Server Monitor using http://monitorhost:monitorport (default port is 8848), or by selecting Monitor on the Administration > Other drop-down menu on the Server Console.
    You can specify the monitor port by setting monitor.jmx.htmladaptor.port in the server.properties file in <server_install_root>\bin.
