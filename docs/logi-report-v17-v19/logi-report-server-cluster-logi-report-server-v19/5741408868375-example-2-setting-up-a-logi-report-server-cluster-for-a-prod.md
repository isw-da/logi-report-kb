---
title: "Example 2: Setting Up a Logi Report Server Cluster for a Production Environment"
id: 5741408868375
section: "Logi Report Server Cluster Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741408868375-Example-2-Setting-Up-a-Logi-Report-Server-Cluster-for-a-Production-Environment
updated_at: 2022-10-31T17:15:55Z
---

# Example 2: Setting Up a Logi Report Server Cluster for a Production Environment

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741408854807-Example-1-Setting-Up-a-Simple-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741386898839-Managing-a-Logi-Report-Server-Cluster)

# Example 2: Setting Up a Logi Report Server Cluster for a Production Environment

This topic describes how you can set up a Logi Report Server Cluster on UNIX by configuring the Cluster UI on each Logi Report Server. We use three computers in the cluster: node1 (IP address: 192.168.0.1), node2 (IP address: 192.168.0.2), and node3 (IP address: 192.168.0.3). All the Logi Report Servers in the cluster use Apache Derby as the server system database.

Take the steps to set up the cluster:

1. Make the time difference between the computers be within one minute.
2. Install Logi Report Server on each of the three nodes in the directories `/home/LogiReport/Server1`, `/home/LogiReport/Server2`, and `/home/LogiReport/Server3` respectively using the appropriate license key for the cluster.
3. Install Logi Report Server Monitor on one of the nodes.
4. Launch the Logi Report Server you installed to `/home/LogiReport/Server1` on node1.
5. Sign in to its Server Console.
6. On the system toolbar, navigate to **Administration** > **Configuration** > **Cluster** > **Configuration**. Server displays the Configuration page.
7. Specify a cluster name.
8. Select **Enable Cluster**.
9. Select **Save** to enable the cluster.
10. Restart the Logi Report Server on node1.
11. Go to the Administration > Configuration > Cluster > Configuration page again.
12. Leave the Load Balancer Type as **Round Robin**.
13. Select **Cluster Scheduler Lease** to enable scheduler leases for the cluster.
14. Set the active count, valid time, and check interval for the cluster scheduler lease respectively. The default two active schedules with a time of 300 seconds and check interval of 30 seconds are a good starting point.
15. Keep the cluster storage history, realm, and CRD result number of copies to 2. This means that the Cluster copies each resource to two of the three servers so there will be no single point of failure for the resources.
16. Keep the default value 2 for Cluster Memory Storage Number of Copies, thus you can share 2 memory copies in the cluster.
17. Select **Notify via E-mail When a Server Is Down**.
18. In the **E-mail Address** text box, type the email addresses of the people to whom you want to send a notification email.
19. Keep the default values for Properties Directory, Realm Directory, Resource Root, History Directory, and Temporary Files Directory.
20. In the **Server's RMI Host** text box, type the IP address or host name of Server1 as **192.168.0.1**.
21. Type the port number in the Server's RMI Port text box as **1129**.
22. Select **Save** to accept all the changes.

    ![Cluster Settings](https://devnet.logianalytics.com/hc/article_attachments/9905831377175/clstr_set_case2_clstr.gif)
23. Navigate to **Administration** > **Configuration** > **Server DB** > **System DB** to open the System DB page of Server1.
24. On the **Configuration** tab, copy the URL in the URL text box to a temporary file.
25. Go to the **Realm DB** page to copy the URL using the same way.

    ![System DB page](https://devnet.logianalytics.com/hc/article_attachments/9905819627415/clstr_set_case2_db.gif)

    To use a Logi Report Server Cluster, all nodes in the cluster must use the same database. In this case, all three nodes will use the database Server1 uses. This ensures that all the servers in the cluster share a single DBMS instance.
26. Shut down the server.
27. Launch the Logi Report Server you installed to `/home/LogiReport/Server2` on node2.
28. Sign in to its Server Console.
29. Access the Administration > Configuration > Cluster > Configuration page.
30. Use the same cluster name as Server1, thus making Server2 join the existing cluster.
31. Select **Enable Cluster**.
32. Select **Save** to enable the cluster.
33. Restart the Logi Report Server on node2.
34. Sign in to its Server Console again.
35. Go to the Administration > Configuration > Server DB > System DB/Realm DB page.
36. Make the system database and realm database in the URL text box the same as those of node1.
37. Go to the Administration > Configuration > Cluster > Configuration page again.
38. In the **Server's RMI Host** text box, type the IP address or host name of Server2 as **192.168.0.2**.
39. Type the port number in the Server's RMI Port text box as **1129**.
40. Select **Save** to accept all the changes.
41. Shut down the server.
42. Copy **rmi.auth** in `/home/LogiReport/Server1/bin` to `/home/LogiReport/Server2/bin`. This authorizes RMI between node1 and node2.
43. Launch the Logi Report Server you installed to `/home/LogiReport/Server3` on node3.
44. Enable Cluster and make node3 join the existing cluster too.
45. Restart the Logi Report Server on node3.
46. Sign in to its Server Console again.
47. Go to the Administration > Configuration > Server DB > System DB/Realm DB page.
48. Make the system database and realm database in the URL text box the same as those of node1.
49. Go to the Administration > Configuration > Cluster > Configuration page.
50. In the **Server's RMI Host** text box, type the IP address or host name of Server3 as **192.168.0.3**.
51. Type the port number in the Server's RMI Port text box as **1129**.
52. Select **Save** to accept all the changes.
53. Shut down the server.
54. Copy **rmi.auth** in `/home/LogiReport/Server1/bin` to `/home/LogiReport/Server3/bin`.
55. Start the server Derby DBMS service by running the **startNetworkServer.sh** file in `/home/LogiReport/Server1/derby/bin`.
56. Launch the server on node1.
57. In the Command Prompt window, you see the information:

    `Logi Report Server is ready for service.`
58. Similarly, launch the servers on node2 and node3.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741408854807-Example-1-Setting-Up-a-Simple-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741386898839-Managing-a-Logi-Report-Server-Cluster)
