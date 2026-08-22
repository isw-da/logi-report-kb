---
title: "Writing Customized Load Balancing Algorithm"
id: 1500009770981
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009770981-Writing-Customized-Load-Balancing-Algorithm
updated_at: 2021-07-24T00:49:36Z
---

# Writing Customized Load Balancing Algorithm

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771141-Applying-TaskListener)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771061-Setting-Server-Reporthome-and-Properties-in-a-Java-EE-Environment)

# Writing Customized Load Balancing Algorithm

Logi Report Server Cluster provides a [load balancing mechanism](https://devnet.logianalytics.com/hc/en-us/articles/1500009771301-Logi-Report-Server-Cluster-Main-Features#LoadBalance) which ensures the servers in the cluster to work more effectively. You can also write your own load balancing algorithm using the Logi Report Server API. This topic describes how you can apply a customized load balancing algorithm via API.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)If you create a load balancing algorithm via API, it will take effect in place of other built-in load balance algorithms you have set. For more information, see the interface **jet.server.api.cluster.LoadBalancer** in the Logi Report Javadoc.

The demo file **DemoLoadBalancer.java** shows how to customize load balancing using API. You can find it in `<install_root>\help\samples\APICluster`.

Take the following steps to apply customized load balancing algorithm:

1. Compile **DemoLoadBalancer.java** to generate the class file as follows (when compiling DemoLoadBalancer.java, you need to add **JRESServlets.jar** to the class path):  

   `javac -classpath <install_root>\lib\JRESServlets.jar DemoLoadBalancer.java`
2. Add **DemoLoadBalancer.class** to the class path of **setenv.bat** in the ADDCLASSPATH variable.
3. Add the parameter `-Dloadbalance.custom_class=DemoLoadBalancer` to the server's startup file **JRServer.bat** which locates in `<install_root>\bin`. For example:

   `"%JAVAHOME%\bin\java.exe" -Dloadbalance.custom_class=DemoLoadBalancer "-Dinstall.root=%REPORTHOME%" ...`
4. Launch **JRServer.bat**, and the customized load balancer DemoLoadBalancer will then be applied.
5. Submit some tasks for running. You can now find that these tasks are allocated to the clustered servers based on the **DemoLoadBalancer** code.

**Tip:** You can choose the load balancing type by setting the API method *setLoadBalanceType()* in jet.server.api.admin.ClusterAdminService. For example, setting the API method as *setLoadBalanceType(0)*, *setLoadBalanceType(1)*, *setLoadBalanceType(2)*, and *setLoadBalanceType(3)* means respectively the algorithm Least Current Reports (Min-load), Round Robin, Least Weighted Current Reports (Weighted Min-load), and Random will be chosen.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771141-Applying-TaskListener)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771061-Setting-Server-Reporthome-and-Properties-in-a-Java-EE-Environment)
