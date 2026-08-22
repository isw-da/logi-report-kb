---
title: "Writing Customized Load Balancing Algorithm"
id: 45203869942157
section: "Working with APIs Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203869942157-Writing-Customized-Load-Balancing-Algorithm
updated_at: 2026-04-30T14:07:45Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Writing Customized Load Balancing Algorithm 

Report Server Cluster provides a load balancing mechanism which ensures the servers in the Cluster to work more effectively. You can also write your own load balancing algorithm using the Report Server API. This topic describes how you can apply a customized load balancing algorithm via API.

 If you create a load balancing algorithm via API, it will take effect in place of other built-in load balance algorithms you have set. For more information, see the interface jet.server.api.cluster.LoadBalancer in the Report Javadoc.

The demo file DemoLoadBalancer.java shows how to customize load balancing using API. You can find it in <install_root>\help\samples\APICluster. 

To apply customized load balancing algorithm:

- Compile DemoLoadBalancer.java to generate the class file, and remember to add JRESServlets.jar to the class path.
javac -classpath <install_root>\lib\JRESServlets.jar DemoLoadBalancer.java

- Add DemoLoadBalancer.class to the class path of setenv.bat in the ADDCLASSPATH variable.

- Add the parameter -Dloadbalance.custom_class=DemoLoadBalancer to the server's startup file JRServer.bat in <install_root>\bin. "%JAVAHOME%\bin\java.exe" -Dloadbalance.custom_class=DemoLoadBalancer "-Dinstall.root=%REPORTHOME%" ...

- Launch JRServer.bat. Server applies the customized load balancer DemoLoadBalancer.
  

- Submit some tasks for running. Server allocates these tasks to the clustered servers based on the DemoLoadBalancer.
      

Tip: You can choose the load balancing type by setting the API method setLoadBalanceType() in jet.server.api.admin.ClusterAdminService. For example, setting the API method as setLoadBalanceType(0), setLoadBalanceType(1), setLoadBalanceType(2), and setLoadBalanceType(3) means selecting respectively the algorithm Least Current Reports (Min-load), Round Robin, Least Weighted Current Reports (Weighted Min-load), and Random.
