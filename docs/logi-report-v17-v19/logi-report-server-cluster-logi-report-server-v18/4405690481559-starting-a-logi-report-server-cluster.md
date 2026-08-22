---
title: "Starting a Logi Report Server Cluster"
id: 4405690481559
section: "Logi Report Server Cluster Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690481559-Starting-a-Logi-Report-Server-Cluster
updated_at: 2022-01-27T07:58:30Z
---

# Starting a Logi Report Server Cluster

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683576343-Setting-Up-and-Configuring-a-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683574295-Example-1-Setting-Up-a-Simple-Logi-Report-Server-Cluster)

# Starting a Logi Report Server Cluster

This topic describes how you can start a Logi Report Server Cluster. To do this, start the servers you have configured for the cluster one by one.

If you are using the default Derby DBMS, be sure to start Derby first by running **startNetworkServer.bat/sh** in the `<install_root>\derby\bin` directory on the server containing the server DBMS.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)

* If you are using multiple IP addresses on a clustered server, you need to add `-Djgroups.bind_addr=IP address` at which Logi Report Server Cluster can work properly to its **JRServer.bat** file in `<install_root>\bin` to make sure the server can start successfully.
* If you have two Logi Report Server Clusters with the same cluster name in a network segment, although the two clusters are pointing to different databases, only the one that started earlier can work successfully.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683576343-Setting-Up-and-Configuring-a-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683574295-Example-1-Setting-Up-a-Simple-Logi-Report-Server-Cluster)
