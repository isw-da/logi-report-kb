---
title: "Writing Customized Load Balancing Algorithm"
id: 1500009686262
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009686262-Writing-Customized-Load-Balancing-Algorithm
updated_at: 2021-11-03T06:58:35Z
---

# Writing Customized Load Balancing Algorithm

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712081-Applying-TaskListener)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712021-Setting-Server-Reporthome-and-Properties-in-a-Java-EE-Environment)

# Writing Customized Load Balancing Algorithm

In a cluster environment, Logi JReport Server provides a [load balancing mechanism](https://devnet.logianalytics.com/hc/en-us/articles/1500009686502-Logi-Report-Server-Cluster-Main-Features#LoadBalance) which enables the server to work more effectively. You can also write your own load balancing algorithm based on the API included in Logi JReport Server. Note that if you create a load balancing algorithm via API, it will take effect in place of other built-in load balance algorithms you have set. For detailed usage about the API, refer to the jet.server.api.cluster.LoadBalancer interface in the Logi JReport Javadoc.

The demo file DemoLoadBalancer.java is provided to show how to customize load balancing using API. You can find it in `<install_root>\help\samples\APICluster`.

Assuming that you have several clustered servers, take the following steps to apply customized load balancing algorithm:

1. Compile DemoLoadBalancer.java to generate the class file as follows (when compiling DemoLoadBalancer.java, you need to add JRESServlets.jar to the class path):  

   `javac -classpath <install_root>\lib\JRESServlets.jar DemoLoadBalancer.java`
2. Add DemoLoadBalancer.class to the class path of setenv.bat in the ADDCLASSPATH variable.
3. Add the parameter `-Dloadbalance.custom_class=DemoLoadBalancer` to the server's startup file JRServer.bat which locates in `<install_root>\bin`. For example:

   `"%JAVAHOME%\bin\java.exe" -Dloadbalance.custom_class=DemoLoadBalancer "-Dinstall.root=%REPORTHOME%" ...`
4. Launch JRServer.bat, the customized load balancer DemoLoadBalancer will then be applied.
5. Submit some tasks for running. You can now find that these tasks are allocated to the clustered servers based on the DemoLoadBalancer code.

**Tip:** You can choose the load balancing type by setting the API method *setLoadBalanceType()* in jet.server.api.admin.ClusterAdminService. For example, setting the API method as *setLoadBalanceType(0)*, *setLoadBalanceType(1)*, *setLoadBalanceType(2)*, and *setLoadBalanceType(3)* means respectively the algorithm Least Current Reports (Min-load), Round Robin, Least Weighted Current Reports (Weighted Min-load) and Random will be chosen.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712081-Applying-TaskListener)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712021-Setting-Server-Reporthome-and-Properties-in-a-Java-EE-Environment)
