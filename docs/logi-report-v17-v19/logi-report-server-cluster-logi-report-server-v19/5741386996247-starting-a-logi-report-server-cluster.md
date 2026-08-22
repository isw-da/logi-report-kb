---
title: "Starting a Logi Report Server Cluster"
id: 5741386996247
section: "Logi Report Server Cluster Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741386996247-Starting-a-Logi-Report-Server-Cluster
updated_at: 2022-10-31T17:15:55Z
---

# Starting a Logi Report Server Cluster

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9305227644055/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741400931479-Setting-Up-and-Configuring-a-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9305200977175/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741408854807-Example-1-Setting-Up-a-Simple-Logi-Report-Server-Cluster)

# Starting a Logi Report Server Cluster

This topic describes how you can start a Logi Report Server Cluster. To do this, start the servers you have configured for the cluster one by one.

If you are using the default Derby DBMS, be sure to start Derby first by running **startNetworkServer.bat/sh** in the `<install_root>\derby\bin` directory on the server containing the server DBMS.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9305196643607/noteicon.jpg)

* If you are using multiple IP addresses on a clustered server, you need to add `-Djgroups.bind_addr=IP address` at which Logi Report Server Cluster can work properly to its **JRServer.bat** file in `<install_root>\bin` to make sure the server can start successfully.
* If you have two Logi Report Server Clusters with the same cluster name in a network segment, although the two clusters are pointing to different databases, only the one that started earlier can work successfully.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9305227644055/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741400931479-Setting-Up-and-Configuring-a-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9305200977175/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741408854807-Example-1-Setting-Up-a-Simple-Logi-Report-Server-Cluster)
