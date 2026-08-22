---
title: "Starting a Logi Report Server Cluster"
id: 1500009718722
section: "Logi Report Server Integration, Server Cluster, and Server Security Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718722-Starting-a-Logi-Report-Server-Cluster
updated_at: 2021-07-25T07:20:18Z
---

# Starting a Logi Report Server Cluster

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718702-Setting-Up-and-Configuring-a-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744641-Example-1-Setting-Up-a-Simple-Logi-Report-Server-Cluster)

# Starting a Logi Report Server Cluster

This topic describes how you can start a Logi Report Server Cluster. To do this, start the servers you have configured for the cluster one by one.

If you are using the default Derby DBMS, be sure to start Derby first by running **startNetworkServer.bat/sh** in the `<install_root>\derby\bin` directory on the server containing the server DBMS.

**Notes:**

* If you are using multiple IP addresses on a clustered server, you need to add `-Djgroups.bind_addr=IP address` at which Logi Report Server Cluster can work properly to its **JRServer.bat** file located in `<install_root>\bin` to make sure the server can be started successfully.
* If you have two Logi Report Sever Clusters with the same cluster name in a network segment, although the two clusters are pointing to different databases, only the one started earlier can work successfully.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718702-Setting-Up-and-Configuring-a-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744641-Example-1-Setting-Up-a-Simple-Logi-Report-Server-Cluster)
