---
title: "Starting a Logi JReport Server Guide v15 Server Cluster"
id: 1500009668981
section: "Server Cluster Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009668981-Starting-a-Logi-JReport-Server-Guide-v15-Server-Cluster
updated_at: 2021-07-24T20:55:24Z
---

# Starting a Logi JReport Server Guide v15 Server Cluster

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644342-Setting-Up-and-Configuring-a-Logi-JReport-Server-Guide-v15-Server-Cluster)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668961-Example-1-Setting-Up-a-Simple-Logi-JReport-Server-Guide-v15-Server-Cluster)

# Starting a Logi JReport Server Cluster

To start a Logi JReport Server Cluster, start the servers you have configured for the cluster one by one. If you are using the default Derby DBMS, be sure to start Derby first by running startNetworkServer.bat/sh in the `<install_root>\derby\bin` directory on the server containing the server DBMS.

**Notes:**

* If you are using multiple IP address on a clustered server, you need to add `-Djgroups.bind_addr=IP address` at which Logi JReport cluster can work properly to its JRServer.bat file located in `<install_root>\bin` to make sure the server can be started successfully.
* If you have two Logi JReport clusters with the same cluster name in a network segment, although the two clusters are pointing to different databases, only the one started earlier can work successfully.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644342-Setting-Up-and-Configuring-a-Logi-JReport-Server-Guide-v15-Server-Cluster)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668961-Example-1-Setting-Up-a-Simple-Logi-JReport-Server-Guide-v15-Server-Cluster)
