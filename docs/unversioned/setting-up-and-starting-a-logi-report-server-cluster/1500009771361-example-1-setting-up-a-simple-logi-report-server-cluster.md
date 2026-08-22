---
title: "Example 1: Setting Up a Simple Logi Report Server Cluster"
id: 1500009771361
section: "Setting Up and Starting a Logi Report Server Cluster"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009771361-Example-1-Setting-Up-a-Simple-Logi-Report-Server-Cluster
updated_at: 2021-07-24T00:49:29Z
---

# Example 1: Setting Up a Simple Logi Report Server Cluster

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743462-Starting-a-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743442-Example-2-Setting-Up-a-Logi-Report-Server-Cluster-for-a-Production-Environment)

# Example 1: Setting Up a Simple Logi Report Server Cluster

This topic describes how you can configure a simple Logi Report Server Cluster by modifying the configuration options in the Console of each Logi Report Server, as an administrator.

Example description:

* Set up a simple Logi Report Server Cluster via the Server Console. Assume that Logi Report Server Monitor has been installed on your computer.
* The cluster consists of two copies of Logi Report Server on one computer.
* The cluster uses one server DBMS.
* The cluster uses shared directories for resources, so no resource copies are required.

Take the following steps to set up the cluster:

1. Install the two Logi Report Servers respectively to `C:\LogiReport\Server1` and `C:\LogiReport\Server2` using the cluster enabled license key.
2. Launch the Logi Report Server installed to `C:\LogiReport\Server2`.
3. [Access the Server Console](https://devnet.logianalytics.com/hc/en-us/articles/1500009777061-Accessing-Logi-Report-Server-via-a-Web-Browser) of Server2 using port 8888 as an administrator, point to **Administration** on the system toolbar, select **Configuration** > **Service** from the drop-down menu, then set Port to **8883** to make it different from that of Server1. You may use any port number which is available on your system.
4. Point to **Administration** on the system toolbar, select **Configuration** > **Cluster** > **Configuration** from the drop-down menu to display the Configuration page.
5. Specify a cluster name and select the **Enable Cluster** option, then select **Save** to enable the cluster.
6. Restart the Logi Report Server installed to `C:\LogiReport\Server2`.
7. Log onto the Server Console of Server2 using the port 8883 specified in step 3 (`http://localhost:8883`) as an administrator.
8. Go to the **Administration** > **Configuration** > **Cluster** > **Configuration** page, leave the Load Balancer Type as Round Robin.
9. Select the **Cluster Scheduler Lease** option to enable lease for the cluster, then set the active count, valid time and check interval for the cluster scheduler lease.
10. Change the Cluster Storage History, Realm and CRD Result Number of Copies to **1**. We will just use one resource directory.
11. Keep the default value 2 for Cluster Memory Storage Number of Copies, thus 2 memory copies will be shared in the cluster.
12. Select the **Notify via E-mail When a Server Is Down** option, and in the E-mail Address text box, type the e-mail addresses of the people to whom you want to send a notification e-mail.
13. Keep the default values for Properties Directory, Realm Directory, Resource Root, History Directory and Temporary Files Directory.
14. Type the IP address or host name of Server2 in the Server's RMI Host text box and type the port number in the Server's RMI Port text box.

    The port is the RMI port of the clustered server. The default port number is 1129. If there are two or more Logi Report Servers started on one machine, the RMI port number of each clustered server must be changed to a unique one, in order to avoid port conflicts.

    In this example, the port number is changed to 1130, since the other server will use the default port number 1129.
15. Select **Save** to accept all the changes, then shut down the server.

    ![Cluster Settings](https://devnet.logianalytics.com/hc/article_attachments/4404885616279/clstr_set_case1.gif)
16. Edit C:\LogiReport\Server2\bin\dbconfig.xml and remove the lines with auto-start-derbyservice. We only want Server1 to start the server DBMS since we will always use the Server1 database.
17. Launch the Logi Report Server installed to `C:\LogiReport\Server1`, log onto its Server Console (`http://localhost:8888`) as an administrator, then point to **Administration** on the system toolbar, select **Configuration** > **Cluster** > **Configuration** from the drop-down menu.
18. Use the same cluster name as Server2, thus making Server1 join the existing cluster. Select the **Enable Cluster** option, then select **Save** to enable the cluster.
19. Restart the Logi Report Server installed to `C:\LogiReport\Server1`, and log onto the Server Console again.
20. Go to the **Administration** > **Configuration** > **Cluster** > **Configuration** page, configure Server's RMI Host and Server's RMI Port. Remember to keep Server's RMI Port to its default value 1129.
21. Upon finish, select **Save** to accept all settings and shut down Server1.
22. Copy rmi.auth in `C:\LogiReport\Server1\bin` to `C:\LogiReport\Server2\bin`. This enables RMI to be authorized between the two systems.
23. Edit server.properties in `C:\LogiReport\Server2\bin` and remove cluster.member.id. It will be recreated when you restart Server2 with a unique number.
24. Start the server Derby DBMS service by double-clicking the startNetworkServer.bat file in `C:\LogiReport\Server1\derby\bin`.
25. Restart Server1 and Server2. It does not matter which one you started first.
26. Access the Server Console of the first server using port 8888 as an administrator, and then submit a scheduled task. In the Scheduled tab, you will see the newly scheduled task.
27. Log onto the Server Console of the second server as an administrator and [create a new user](https://devnet.logianalytics.com/hc/en-us/articles/1500009749862-Managing-User-Accounts) Tom in the Administration > Security > User page.
28. Access the Server Console of the second server using port 8883 as Tom, and then submit another scheduled task.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)

* When you schedule to publish a report on a clustered server to disk, you should first specify a disk in your file system and make sure that every node in the cluster has the same disk name mapping to the same physical location. Then Server saves the publishing result directly to the disk you specify.
* You can only view scheduled tasks that you have submitted.
* From the Server Console of the clustered Logi Report Servers, you can only view completed tasks that you have submitted.
* If there are more than two clustered servers in the cluster, then after you shut down one server, all the scheduled tasks running on this server will run on other servers.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743462-Starting-a-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743442-Example-2-Setting-Up-a-Logi-Report-Server-Cluster-for-a-Production-Environment)
