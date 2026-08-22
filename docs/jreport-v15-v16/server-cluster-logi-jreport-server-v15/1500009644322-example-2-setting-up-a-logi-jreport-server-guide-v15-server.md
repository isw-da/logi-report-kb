---
title: "Example 2: Setting Up a Logi JReport Server Guide v15 Server Cluster for a Production Environment"
id: 1500009644322
section: "Server Cluster Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644322-Example-2-Setting-Up-a-Logi-JReport-Server-Guide-v15-Server-Cluster-for-a-Production-Environment
updated_at: 2021-07-24T20:55:24Z
---

# Example 2: Setting Up a Logi JReport Server Guide v15 Server Cluster for a Production Environment

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668961-Example-1-Setting-Up-a-Simple-Logi-JReport-Server-Guide-v15-Server-Cluster)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668941-Managing-a-Logi-JReport-Server-Guide-v15-Server-Cluster)

# Example 2: Setting Up a Logi JReport Server Cluster for a Production Environment

This example demonstrates how to set up a Logi JReport Server Cluster on Unix/Linux by configuring the cluster UI on each Logi JReport Server. There will be three computers in the cluster. They are node1 (IP address: 192.168.0.1), node2 (IP address: 192.168.0.2) and node3 (IP address: 192.168.0.3). All Logi JReport Servers in the cluster use Apache Derby as the server system database.

Take the following steps to set up the cluster:

1. Make the time difference between the target computers be within one minute.
2. Install Logi JReport Server on each of the three nodes in directories `/home/Logi JReport/Server1`, `/home/Logi JReport/Server2` and `/home/Logi JReport/Server3` respectively using the appropriate license key for the cluster, and install Logi JReport Server Monitor on one of the nodes.
3. Launch the Logi JReport Server installed to `/home/Logi JReport/Server1` on node1.
4. Log onto the Logi JReport Administration page and select **Cluster** > **Configuration** on the system toolbar.
5. On the Cluster - Configuration page, specify a cluster name and check the **Enable Cluster** option, then select **Save** to enable the cluster.
6. Restart the Logi JReport Server on node1, and go to the Cluster - Configuration page again.
7. Leave the Load Balancer Type as Round Robin.
8. Check the **Cluster Scheduler Lease** option to enable scheduler leases for the cluster, then set the active count, valid time and check interval for the cluster scheduler lease respectively. The defaults of 2 active schedules with a time of 300 seconds and check interval of 30 seconds are a good starting point.
9. Keep the cluster storage history, realm and CRD result number of copies to 2. This means that each resource will be copied to 2 of the 3 servers so there will be no single point of failure for the resources.
10. Keep the default value 2 for Cluster Memory Storage Number of Copies, thus 2 memory copies will be shared in the cluster.
11. Check the **Notify via E-mail When a Server Is Down** option, and in the E-mail Address text field, input the e-mail addresses of the people to whom you want to send a notification e-mail.
12. Keep the default values for Properties Directory, Realm Directory, Resource Root, History Directory and Temporary Files Directory.
13. In the Server's RMI Host text field, type the IP address or host name of Server1 as **192.168.0.1**. Type the port number in the Server's RMI Port text field as **1129**.
14. Select **Save** to accept all the changes.
15. Go to the **Data** > **System DB** panel of Server1, in the Configuration tab, copy the URL in the URL text field to a temporary file, and go to the Realm DB panel to copy the URL using the same way.

    In order to use a Logi JReport Server Cluster, all nodes in the cluster must use the same database. In this case, all three nodes will use the database Server1 uses. This ensures that all servers in the cluster share a single DBMS instance.
16. Shut down the server.
17. Launch the Logi JReport Server installed to `/home/Logi JReport/Server2` on node2.
18. Log onto the Logi JReport Administration page and select **Cluster** > **Configuration** on the system toolbar.
19. On the Cluster - Configuration page, use the same cluster name as Server1, thus making Server2 join the existing cluster. Check the **Enable Cluster** option, then select **Save** to enable the cluster.
20. Restart the Logi JReport Server on node2. Go to the Logi JReport Administration page > Data > System DB/Realm DB, make the system database and realm database in the URL text field the same as those of node1.
21. Go to the Cluster - Configuration page again.
22. In the Server's RMI Host text field, type the IP address or host name of Server2 as **192.168.0.2**. Type the port number in the Server's RMI Port text field as **1129**.
23. Select **Save** to accept all the changes, then shut down the server.
24. Copy rmi.auth in `/home/Logi JReport/Server1/bin` to `/home/Logi JReport/Server2/bin`. This allows RMI to be authorized between node1 and node2.
25. Launch the Logi JReport Server installed to `/home/Logi JReport/Server3` on node3. Just like what we did with node2, enable cluster and make node3 join the existing cluster too.
26. Restart the Logi JReport Server on node3. Go to the Logi JReport Administration page > Data > System DB/Realm DB, make the system database and realm database in the URL text field the same as those of node1.
27. Go to the Cluster - Configuration page.
28. In the Server's RMI Host text field, type the IP address or host name of Server3 as **192.168.0.3**. Type the port number in the Server's RMI Port text field as **1129**.
29. Select **Save** to accept all the changes, then shut down the server.
30. Just as we did with node2, copy rmi.auth in `/home/Logi JReport/Server1/bin` to `/home/Logi JReport/Server3/bin`.
31. Start the server Derby DBMS service by running the startNetworkServer.sh file in `/home/Logi JReport/Server1/derby/bin`.
32. Launch the server on node1. In the Command Prompt window, you will see the following information:

    `Logi JReport Server is ready for service.`
33. Similarly, launch the server on node2 and node3.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668961-Example-1-Setting-Up-a-Simple-Logi-JReport-Server-Guide-v15-Server-Cluster)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668941-Managing-a-Logi-JReport-Server-Guide-v15-Server-Cluster)
