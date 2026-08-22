---
title: "Example 2: Setting Up a Logi Report Server Cluster for a Production Environment"
id: 1500009743442
section: "Setting Up and Starting a Logi Report Server Cluster"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009743442-Example-2-Setting-Up-a-Logi-Report-Server-Cluster-for-a-Production-Environment
updated_at: 2021-07-24T00:49:30Z
---

# Example 2: Setting Up a Logi Report Server Cluster for a Production Environment

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771361-Example-1-Setting-Up-a-Simple-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771321-Managing-a-Logi-Report-Server-Cluster)

# Example 2: Setting Up a Logi Report Server Cluster for a Production Environment

This topic describes how you can set up a Logi Report Server Cluster on Unix by configuring the Cluster UI on each Logi Report Server. There will be three computers in the cluster. They are node1 (IP address: 192.168.0.1), node2 (IP address: 192.168.0.2), and node3 (IP address: 192.168.0.3). All the Logi Report Servers in the cluster use Apache Derby as the server system database.

Take the following steps to set up the cluster:

1. Make the time difference between the target computers be within one minute.
2. Install Logi Report Server on each of the three nodes in directories `/home/LogiReport/Server1`, `/home/LogiReport/Server2` and `/home/LogiReport/Server3` respectively using the appropriate license key for the cluster, and install Logi Report Server Monitor on one of the nodes.
3. Launch the Logi Report Server installed to `/home/LogiReport/Server1` on node1.
4. Log onto its Server Console, point to **Administration** on the system toolbar, select **Configuration** > **Cluster** > **Configuration** from the drop-down menu.
5. In the Configuration page, specify a cluster name and select the **Enable Cluster** option, then select **Save** to enable the cluster.
6. Restart the Logi Report Server on node1 and go to the Administration > Configuration > Cluster > Configuration page again.
7. Leave the Load Balancer Type as Round Robin.
8. Select the **Cluster Scheduler Lease** option to enable scheduler leases for the cluster, then set the active count, valid time and check interval for the cluster scheduler lease respectively. The defaults of 2 active schedules with a time of 300 seconds and check interval of 30 seconds are a good starting point.
9. Keep the cluster storage history, realm and CRD result number of copies to 2. This means that each resource will be copied to 2 of the 3 servers so there will be no single point of failure for the resources.
10. Keep the default value 2 for Cluster Memory Storage Number of Copies, thus 2 memory copies will be shared in the cluster.
11. Select the **Notify via E-mail When a Server Is Down** option, and in the E-mail Address text box, type the e-mail addresses of the people to whom you want to send a notification e-mail.
12. Keep the default values for Properties Directory, Realm Directory, Resource Root, History Directory and Temporary Files Directory.
13. In the Server's RMI Host text box, type the IP address or host name of Server1 as **192.168.0.1**. Type the port number in the Server's RMI Port text box as **1129**.
14. Select **Save** to accept all the changes.

    ![Cluster Settings](https://devnet.logianalytics.com/hc/article_attachments/4404885615767/clstr_set_case2_clstr.gif)
15. Select **Administration** > **Configuration** > **Server DB** > **System DB** to open the System DB page of Server1, then in the Configuration tab, copy the URL in the URL text box to a temporary file. Go to the Realm DB page to copy the URL using the same way.

    ![System DB page](https://devnet.logianalytics.com/hc/article_attachments/4404885616023/clstr_set_case2_db.gif)

    To use a Logi Report Server Cluster, all nodes in the cluster must use the same database. In this case, all three nodes will use the database Server1 uses. This ensures that all servers in the cluster share a single DBMS instance.
16. Shut down the server.
17. Launch the Logi Report Server installed to `/home/LogiReport/Server2` on node2.
18. Log onto its Server Console and access the Administration > Configuration > Cluster > Configuration page.
19. In the Configuration page, use the same cluster name as Server1, thus making Server2 join the existing cluster. Select the **Enable Cluster** option, then select **Save** to enable the cluster.
20. Restart the Logi Report Server on node2 and log onto its Server Console again.
21. Go to the Administration > Configuration > Server DB > System DB/Realm DB page, make the system database and realm database in the URL text box the same as those of node1.
22. Go to the Administration > Configuration > Cluster > Configuration page again.
23. In the Server's RMI Host text box, type the IP address or host name of Server2 as **192.168.0.2**. Type the port number in the Server's RMI Port text box as **1129**.
24. Select **Save** to accept all the changes, then shut down the server.
25. Copy rmi.auth in `/home/LogiReport/Server1/bin` to `/home/LogiReport/Server2/bin`. This enables RMI to be authorized between node1 and node2.
26. Launch the Logi Report Server installed to `/home/LogiReport/Server3` on node3. Just like what we did with node2, enable cluster and make node3 join the existing cluster too.
27. Restart the Logi Report Server on node3 and log onto its Server Console again.
28. Go to the Administration > Configuration > Server DB > System DB/Realm DB page, make the system database and realm database in the URL text box the same as those of node1.
29. Go to the Administration > Configuration > Cluster > Configuration page.
30. In the Server's RMI Host text box, type the IP address or host name of Server3 as **192.168.0.3**. Type the port number in the Server's RMI Port text box as **1129**.
31. Select **Save** to accept all the changes, then shut down the server.
32. Just as we did with node2, copy rmi.auth in `/home/LogiReport/Server1/bin` to `/home/LogiReport/Server3/bin`.
33. Start the server Derby DBMS service by running the startNetworkServer.sh file in `/home/LogiReport/Server1/derby/bin`.
34. Launch the server on node1. In the Command Prompt window, you will see the following information:

    `Logi Report Server is ready for service.`
35. Similarly, launch the server on node2 and node3.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771361-Example-1-Setting-Up-a-Simple-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771321-Managing-a-Logi-Report-Server-Cluster)
