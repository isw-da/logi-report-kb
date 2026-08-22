---
title: "Example 1: Setting Up a Simple Logi JReport Server Guide v15 Server Cluster"
id: 1500009668961
section: "Server Cluster Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009668961-Example-1-Setting-Up-a-Simple-Logi-JReport-Server-Guide-v15-Server-Cluster
updated_at: 2021-07-24T20:55:24Z
---

# Example 1: Setting Up a Simple Logi JReport Server Guide v15 Server Cluster

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668981-Starting-a-Logi-JReport-Server-Guide-v15-Server-Cluster)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644322-Example-2-Setting-Up-a-Logi-JReport-Server-Guide-v15-Server-Cluster-for-a-Production-Environment)

# Example 1: Setting Up a Simple Logi JReport Server Cluster

This example demonstrates how to configure a simple Logi JReport Server Cluster by modifying the configuration options on the Logi JReport Administration page on each Logi JReport Server.

Example description:

* Set up a simple Logi JReport Server Cluster using the Logi JReport Administration page. Assume that Logi JReport Server Monitor has been installed on your computer.
* The cluster consists of two copies of Logi JReport Server on one computer.
* The cluster uses one server DBMS.
* The cluster uses shared directories for resources so no resource copies are required.

Take the following steps to set up the cluster:

1. Install the two Logi JReport Servers respectively to `C:\Logi JReport\Server1` and `C:\Logi JReport\Server2` using the cluster enabled license key.
2. Launch the Logi JReport Server installed to `C:\Logi JReport\Server2`.
3. Log onto the Logi JReport Administration page of Server2, select **Configuration** > **Service** on the system toolbar, then set Port, Dashboard Port, and Administration Port respectively to **8885**, **8884** and **8883** to make them different from those of Server1. You may use any port numbers which are available on your system.
4. Select **Cluster** > **Configuration** on the system toolbar to display the Cluster - Configuration page.
5. Specify a cluster name and check the **Enable Cluster** option, then select **Save** to enable the cluster.
6. Restart the Logi JReport Server installed to `C:\Logi JReport\Server2`.
7. Log onto the Logi JReport Administration page of Server2 using the administration port 8883 set in Step 3 (`http://localhost:8883`).
8. Go to the **Cluster** > **Configuration** panel, leave the Load Balancer Type as Round Robin.
9. Check the **Cluster Scheduler Lease** option to enable lease for the cluster, then set the active count, valid time and check interval for the cluster scheduler lease.
10. Change the Cluster Storage History, Realm and CRD Result Number of Copies to **1**. We will just use one resource directory.
11. Keep the default value 2 for Cluster Memory Storage Number of Copies, thus 2 memory copies will be shared in the cluster.
12. Check the **Notify via E-mail When a Server Is Down** option, and in the E-mail Address text field, input the e-mail addresses of the people to whom you want to send a notification e-mail.
13. Keep the default values for Properties Directory, Realm Directory, Resource Root, History Directory and Temporary Files Directory.
14. Type the IP address or host name of Server2 in the Server's RMI Host text field, and type the port number in the Server's RMI Port text field.

    The port is the RMI port of the clustered server. The default port number is 1129. If there are two or more Logi JReport Servers started on one machine, the RMI port number of each clustered server must be changed to a unique one, in order to avoid port conflicts.

    In this example, the port number is changed to 1130, since the other server will use the default port number 1129.
15. Select **Save** to accept all the changes, then shut down the server.
16. Edit C:\Logi JReport\Server2\bin\dbconfig.xml and remove the lines with auto-start-derbyservice. We only want Server1 to start the server DBMS since we will always use the Server1 database.
17. Launch the Logi JReport Server installed to `C:\Logi JReport\Server1`, log onto the Logi JReport Administration page (`http://localhost:8889`), then select **Cluster** > **Configuration** on the system toolbar.
18. Use the same cluster name as Server2, thus making Server1 join the existing cluster. Check the **Enable Cluster** option, then select **Save** to enable the cluster.
19. Restart the Logi JReport Server installed to `C:\Logi JReport\Server1`, and then log onto the Logi JReport Administration page.
20. Go to the **Cluster** > **Configuration** page, configure Server's RMI Host and Server's RMI Port. Remember to keep Server's RMI Port to its default value 1129.
21. Upon finish, select **Save** to accept all settings and shut down Server1.
22. Copy rmi.auth in `C:\Logi JReport\Server1\bin` to `C:\Logi JReport\Server2\bin`. This allows RMI to be authorized between the two systems.
23. Edit server.properties in `C:\Logi JReport\Server2\bin` and remove cluster.member.id. It will be recreated when you restart Server2 with a unique number.
24. Start the server Derby DBMS service by double-clicking the startNetworkServer.bat file in `C:\Logi JReport\Server1\derby\bin`.
25. Restart Server1 and Server2. It doesn't matter which one you started first.
26. Access the Logi JReport Console page of the first server using port 8888 as an administrator, and then submit a scheduled task. In the Scheduled tab, you will see the newly scheduled task.
27. Log onto the Logi JReport Administration page of the second server and create a new user Tom in the Security > User page. Access the Logi JReport Console page of the second server using port 8883 as Tom, and then submit another scheduled task.

**Notes:**

* When you schedule to publish a report on a clustered server to disk, you should first specify a disk in your file system and make sure that every node in the cluster has the same disk name mapping to the same physical location. Then the publishing result will be directly saved to the disk you specify.
* You can only view scheduled tasks that you have submitted.
* From the Logi JReport Console page of the clustered servers, you can only view completed tasks that you have submitted.
* If there are more than two clustered servers in the cluster, then after you shut down one server, all the scheduled tasks running on this server will be run on other servers.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668981-Starting-a-Logi-JReport-Server-Guide-v15-Server-Cluster)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644322-Example-2-Setting-Up-a-Logi-JReport-Server-Guide-v15-Server-Cluster-for-a-Production-Environment)
