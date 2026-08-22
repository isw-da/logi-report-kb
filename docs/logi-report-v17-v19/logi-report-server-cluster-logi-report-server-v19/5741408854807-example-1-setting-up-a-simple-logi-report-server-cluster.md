---
title: "Example 1: Setting Up a Simple Logi Report Server Cluster"
id: 5741408854807
section: "Logi Report Server Cluster Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741408854807-Example-1-Setting-Up-a-Simple-Logi-Report-Server-Cluster
updated_at: 2022-10-31T17:15:56Z
---

# Example 1: Setting Up a Simple Logi Report Server Cluster

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741386996247-Starting-a-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741408868375-Example-2-Setting-Up-a-Logi-Report-Server-Cluster-for-a-Production-Environment)

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
3. [Access the Server Console](https://devnet.logianalytics.com/hc/en-us/articles/5741461387031-Accessing-Logi-Report-Server-via-a-Web-Browser) of Server2 using port 8888 as an administrator.
4. On the system toolbar, navigate to **Administration** > **Configuration** > **Service**. Server displays the Service page.
5. Set **Port** to **8883** to make it different from that of Server1. You can use any port number available on your system.
6. On the system toolbar, navigate to **Administration** > **Configuration** > **Cluster** > **Configuration**. Server displays the Configuration page.
7. Specify a cluster name.
8. Select **Enable Cluster**.
9. Select **Save** to enable the cluster.
10. Restart the Logi Report Server you installed to `C:\LogiReport\Server2`.
11. Sign in to the Server Console of Server2 using the port 8883 you specified in step 3 (`http://localhost:8883`) as an administrator.
12. Navigate to the **Administration** > **Configuration** > **Cluster** > **Configuration** page.
13. Leave **Load Balancer Type** as **Round Robin**.
14. Select **Cluster Scheduler Lease** to enable lease for the cluster.
15. Set the active count, valid time, and check interval for the cluster scheduler lease.
16. Change the Cluster Storage History, Realm and CRD Result Number of Copies to **1**. We just use one resource directory.
17. Keep the default value 2 for Cluster Memory Storage Number of Copies, thus 2 memory copies will be shared in the cluster.
18. Select **Notify via E-mail When a Server Is Down**.
19. In the **E-mail Address** text box, type the email addresses of the people to whom you want to send a notification email.
20. Keep the default values for Properties Directory, Realm Directory, Resource Root, History Directory, and Temporary Files Directory.
21. Type the IP address or host name of Server2 in the Server's RMI Host text box.
22. Type the port number in the Server's RMI Port text box.

    The port is the RMI port of the clustered server. The default port number is 1129. If two or more Logi Report Servers started on one machine, the RMI port number of each clustered server must be a unique one, in order to avoid port conflict.

    In this example, we change the port number to 1130, since the other server will use the default port number 1129.
23. Select **Save** to accept all the changes.

    ![Cluster Settings](https://devnet.logianalytics.com/hc/article_attachments/9905831434903/clstr_set_case1.gif)
24. Shut down the server.
25. Edit C:\LogiReport\Server2\bin\dbconfig.xml and remove the lines with auto-start-derbyservice. We only want Server1 to start the server DBMS since we will always use the Server1 database.
26. Launch the Logi Report Server you installed to `C:\LogiReport\Server1`.
27. Sign in to its Server Console (`http://localhost:8888`) as an administrator.
28. On the system toolbar, navigate to **Administration** > **Configuration** > **Cluster** > **Configuration**.
29. Use the same cluster name as Server2, thus making Server1 join the existing cluster.
30. Select **Enable Cluster**.
31. Select **Save** to enable the cluster.
32. Restart the Logi Report Server you installed to `C:\LogiReport\Server1`.
33. Sign in to the Server Console again.
34. Go to the **Administration** > **Configuration** > **Cluster** > **Configuration** page, configure Server's RMI Host and Server's RMI Port. Remember to keep Server's RMI Port to its default value 1129.
35. Select **Save** to accept all settings.
36. Shut down Server1.
37. Copy rmi.auth in `C:\LogiReport\Server1\bin` to `C:\LogiReport\Server2\bin`. This authorizes RMI between the two systems.
38. Edit the **server.properties** file in `C:\LogiReport\Server2\bin` to remove cluster.member.id. Server2 will recreate the ID with a unique number when it restarts.
39. Start the server Derby DBMS service by double-clicking the **startNetworkServer.bat** file in `C:\LogiReport\Server1\derby\bin`.
40. Restart Server1 and Server2.
41. Access the Server Console of the first server using port 8888 as an administrator.
42. Submit a scheduled task. You see the newly scheduled task on the **Scheduled** tab.
43. Sign in to the Server Console of the second server as an administrator.
44. [Create a new user](https://devnet.logianalytics.com/hc/en-us/articles/5741463728407-Managing-User-Accounts) Tom in the Administration > Security > User page.
45. Access the Server Console of the second server using port 8883 as Tom.
46. Submit another scheduled task.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* When you schedule to publish a report on a clustered server to disk, you should first specify a disk in your file system and make sure that every node in the cluster has the same disk name mapping to the same physical location. Then Server saves the publishing report directly to the disk you specify.
* You can only view scheduled tasks that you have submitted.
* From the Server Console of the clustered Logi Report Servers, you can only view completed tasks that you have submitted.
* If there are more than two clustered servers in the cluster, then after you shut down one server, all the scheduled tasks running on this server will run on other servers.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741386996247-Starting-a-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741408868375-Example-2-Setting-Up-a-Logi-Report-Server-Cluster-for-a-Production-Environment)
