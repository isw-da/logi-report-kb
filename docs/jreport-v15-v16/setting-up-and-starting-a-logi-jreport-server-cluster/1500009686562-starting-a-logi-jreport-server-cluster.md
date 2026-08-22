---
title: "Starting a Logi JReport Server Cluster"
id: 1500009686562
section: "Setting Up and Starting a Logi JReport Server Cluster"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009686562-Starting-a-Logi-JReport-Server-Cluster
updated_at: 2021-11-03T06:58:28Z
---

# Starting a Logi JReport Server Cluster

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686542-Setting-Up-and-Configuring-a-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686522-Example-1-Setting-Up-a-Simple-Logi-Report-Server-Cluster)

# Starting a Logi JReport Server Cluster

To start a Logi JReport Server Cluster, start the servers you have configured for the cluster one by one. If you are using the default Derby DBMS, be sure to start Derby first by running startNetworkServer.bat/sh in the `<install_root>\derby\bin` directory on the server containing the server DBMS.

**Notes:**

* If you are using multiple IP address on a clustered server, you need to add `-Djgroups.bind_addr=IP address` at which Logi JReport Server Cluster can work properly to its JRServer.bat file located in `<install_root>\bin` to make sure the server can be started successfully.
* If you have two Logi JReport Sever Clusters with the same cluster name in a network segment, although the two clusters are pointing to different databases, only the one started earlier can work successfully.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686542-Setting-Up-and-Configuring-a-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686522-Example-1-Setting-Up-a-Simple-Logi-Report-Server-Cluster)
