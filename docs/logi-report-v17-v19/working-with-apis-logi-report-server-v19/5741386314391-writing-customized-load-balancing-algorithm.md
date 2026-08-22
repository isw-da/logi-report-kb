---
title: "Writing Customized Load Balancing Algorithm"
id: 5741386314391
section: "Working with APIs Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741386314391-Writing-Customized-Load-Balancing-Algorithm
updated_at: 2022-10-31T17:15:47Z
---

# Writing Customized Load Balancing Algorithm

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741395089175-Applying-TaskListener)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741400319639-Setting-Server-Reporthome-and-Properties-in-a-Java-EE-Environment)

# Writing Customized Load Balancing Algorithm

Logi Report Server Cluster provides a [load balancing mechanism](https://devnet.logianalytics.com/hc/en-us/articles/5741415586199-Logi-Report-Server-Cluster-Main-Features#LoadBalance) which ensures the servers in the Cluster to work more effectively. You can also write your own load balancing algorithm using the Logi Report Server API. This topic describes how you can apply a customized load balancing algorithm via API.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) If you create a load balancing algorithm via API, it will take effect in place of other built-in load balance algorithms you have set. For more information, see the interface **jet.server.api.cluster.LoadBalancer** in the Logi Report Javadoc.

The demo file **DemoLoadBalancer.java** shows how to customize load balancing using API. You can find it in `<install_root>\help\samples\APICluster`.

To apply customized load balancing algorithm:

1. Compile **DemoLoadBalancer.java** to generate the class file, and remember to add **JRESServlets.jar** to the class path.  

   `javac -classpath <install_root>\lib\JRESServlets.jar DemoLoadBalancer.java`
2. Add **DemoLoadBalancer.class** to the class path of **setenv.bat** in the ADDCLASSPATH variable.
3. Add the parameter `-Dloadbalance.custom_class=DemoLoadBalancer` to the server's startup file **JRServer.bat** in `<install_root>\bin`.

   `"%JAVAHOME%\bin\java.exe" -Dloadbalance.custom_class=DemoLoadBalancer "-Dinstall.root=%REPORTHOME%" ...`
4. Launch **JRServer.bat**. Server applies the customized load balancer DemoLoadBalancer.
5. Submit some tasks for running. Server allocates these tasks to the clustered servers based on the **DemoLoadBalancer**.

**Tip:** You can choose the load balancing type by setting the API method *setLoadBalanceType()* in jet.server.api.admin.ClusterAdminService. For example, setting the API method as *setLoadBalanceType(0)*, *setLoadBalanceType(1)*, *setLoadBalanceType(2)*, and *setLoadBalanceType(3)* means selecting respectively the algorithm Least Current Reports (Min-load), Round Robin, Least Weighted Current Reports (Weighted Min-load), and Random.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741395089175-Applying-TaskListener)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741400319639-Setting-Server-Reporthome-and-Properties-in-a-Java-EE-Environment)
