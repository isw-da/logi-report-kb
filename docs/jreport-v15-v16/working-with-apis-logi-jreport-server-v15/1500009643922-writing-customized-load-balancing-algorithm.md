---
title: "Writing Customized Load Balancing Algorithm"
id: 1500009643922
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009643922-Writing-Customized-Load-Balancing-Algorithm
updated_at: 2021-07-24T20:55:30Z
---

# Writing Customized Load Balancing Algorithm

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668701-Adding-TaskListener-When-Scheduling-Reports)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668641-Setting-Server-Reporthome-and-Properties-in-a-Java-EE-Environment)

# Writing Customized Load Balancing Algorithm

In a cluster environment, Logi JReport Server provides a [load balancing mechanism](https://devnet.logianalytics.com/hc/en-us/articles/1500009668921-Logi-JReport-Server-Guide-v15-Server-Cluster-Main-Features#LoadBalance) which enables the server to work more effectively. However, you can also write your own load balancing algorithm based on the API included in Logi JReport Server. Note that if you create a load balancing algorithm with the API, it will take effect in place of other built-in load balance algorithms you have set.

A demo DemoLoadBalancer.java has been provided to illustrate how to customize load balancing using APIs. You can find it in `<install_root>\help\samples\APICluster`.

Assuming that you have several clustered servers, take the following steps:

1. Compile DemoLoadBalancer.java to generate the class file as follows (when compiling DemoLoadBalancer.java, you need to add JRESServlets.jar to the class path):  

   `javac -classpath <install_root>\lib\JRESServlets.jar DemoLoadBalancer.java`
2. Add DemoLoadBalancer.class to the class path of setenv.bat in the ADDCLASSPATH variable.
3. Add the parameter `-Dloadbalance.custom_class=DemoLoadBalancer` to the server's startup file JRServer.bat which locates in `<install_root>\bin`. For example:

   `"%JAVAHOME%\bin\java.exe" -Dloadbalance.custom_class=DemoLoadBalancer "-Dinstall.root=%REPORTHOME%" ...`
4. Launch JRServer.bat, the customized loadbalancer DemoLoadBalancer will then be applied.
5. Submit some tasks for running. You will now find that these tasks are allocated to the clustered servers based on the DemoLoadBalancer code.

**Reference:** For more details, see the jet.server.api.cluster.LoadBalancer interface in Logi JReport Javadoc located in  `<install_root>\help\api`.

**Note:** You can choose the load balancing type by setting the API method setLoadBalanceType() at jet.server.api.admin.ClusterAdminService. For example, setting the API method as setLoadBalanceType(0), setLoadBalanceType(1), setLoadBalanceType(2), and setLoadBalanceType(3) means respectively the algorithm Least Current Reports (Min-load), Round Robin, Least Weighted Current Reports (Weighted Min-load) and Random will be chosen.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668701-Adding-TaskListener-When-Scheduling-Reports)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668641-Setting-Server-Reporthome-and-Properties-in-a-Java-EE-Environment)
