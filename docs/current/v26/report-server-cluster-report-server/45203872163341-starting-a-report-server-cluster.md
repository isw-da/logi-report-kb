---
title: "Starting a Report Server Cluster"
id: 45203872163341
section: "Report Server Cluster Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203872163341-Starting-a-Report-Server-Cluster
updated_at: 2026-04-30T14:07:57Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Starting a Report Server Cluster 

This topic describes how you can start a Report Server Cluster. To do this,  start the servers you have configured for the cluster one by one. 

If you are using the default Derby DBMS, be sure to start Derby first by running startNetworkServer.bat/sh in the <install_root>\derby\bin directory on the server containing the server DBMS.

- If you are using multiple IP addresses on a clustered server, you need to add -Djgroups.bind_addr=IP address at which Report Server Cluster can work properly to its JRServer.bat file in <install_root>\bin to make sure the server can start successfully.

- If you have two Report Server Clusters with the same cluster name in a network segment, although the two clusters are pointing to different databases, only the one that started earlier can work successfully.
