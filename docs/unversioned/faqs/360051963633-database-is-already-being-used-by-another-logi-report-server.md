---
title: "Database is Already Being Used by Another Logi Report Server or Logi Report Cluster"
id: 360051963633
section: "FAQs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360051963633-Database-is-Already-Being-Used-by-Another-Logi-Report-Server-or-Logi-Report-Cluster
updated_at: 2020-07-27T22:39:36Z
---

# Database is Already Being Used by Another Logi Report Server or Logi Report Cluster

**Question:**

Why am I seeing the following error after starting the Logi Report server cluster?  Error Message:  "Database is already being used by another Logi Report Server or Logi Report Cluster".

**Answer:**This error indicates that the two nodes in the cluster can't communicate with each other. Check the following settings to resolve the issue:

1. Network and firewall settings to ensure the two nodes can communicate with each other.  Try pinging each node to ensure it's responding.
2. You can modify the property "**server.rmiserver.fixed\_port**" in **server.properties** file as shown below. When Logi Report Server sits behind the firewall, please open port **1129** and **1130** in the inbound and outbound rules for each server.

```
For Server 1:  
 server.rmi.host=Your IP   
 server.rmi.port=Your Port Number  
 server.rmiadminservice.enable=true  
 server.rmimonitor.enable=true  
 server.rmiserver.enable=true  
 server.rmiserver.fixed_port=Your Port Number  
   
 For Server 2  
 server.rmi.host=Your IP   
 server.rmi.port=Your Port Number  
 server.rmiadminservice.enable=true  
 server.rmimonitor.enable=true  
 server.rmiserver.enable=true  
 server.rmiserver.fixed_port=Your Port Number
```

3. Add the IP address for each cluster to **jgroups.xml** file.

4. If you are using multiple IP addresses on a clustered server, please add **-Djgroups.bind\_addr=IP address** to the **JRServer.bat** and **NTservice.ini** file located in **<install\_root>\bin** to make sure the server can be started successfully.

**Further Reading**

<https://documentation.logianalytics.com/logireportserverguidev17/content/html/cluster/clstr.htm?Highlight=cluster>
