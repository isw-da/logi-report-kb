---
title: "Setting Up and Configuring a Logi Report Server Cluster"
id: 5741400931479
section: "Logi Report Server Cluster Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741400931479-Setting-Up-and-Configuring-a-Logi-Report-Server-Cluster
updated_at: 2022-10-31T17:15:56Z
---

# Setting Up and Configuring a Logi Report Server Cluster

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741415669527-Setting-Up-and-Starting-a-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741386996247-Starting-a-Logi-Report-Server-Cluster)

# Setting Up and Configuring a Logi Report Server Cluster

This topic describes how you can set up a Logi Report Server Cluster either during the Logi Report Server installation or after you have installed the servers using the appropriate license key for cluster.

Before setting up a Logi Report Server Cluster, first you need to reduce the time difference between the target computers that will join the cluster to less than one minute, and make sure all servers in the cluster use the same architecture and operating system.

This topic contains the following sections:

* [Creating a Logi Report Server Cluster During Installation](#During)
* [Creating a Logi Report Server Cluster After Installation](#After)

## Creating a Logi Report Server Cluster During Installation

You should create a Logi Report Server Cluster during the installation of servers. This is the easiest way to set up a cluster.

1. Run the Logi Report Server installation file to install Logi Report Server with the Installation Wizard.
2. Type your User ID.
3. In the **License Key** text box, use the cluster enabled license key.
4. When choosing the installation type, select **Custom Installation for Standalone Server**.
5. Specify the installation directory for Logi Report Server.
6. In the **Service** tab of the **Configure System Environment** screen, select **Network Address At** and type the IP address of the server.

   ![Installation - Service tab](https://devnet.logianalytics.com/hc/article_attachments/9905819495831/clstr_set_set_svc.gif)
7. Select the **Cluster** tab.
8. Type a cluster name in the **Cluster Name** text box. You can either make the server join an existing cluster or specify a new cluster name to build another cluster.
9. Clear **Disable Cluster** at the bottom.

   ![Installation - Cluster tab](https://devnet.logianalytics.com/hc/article_attachments/9905819523607/clstr_set_set_clstr.gif)
10. From the **Load Balancer Type** drop-down list, select the built-in [algorithm](https://devnet.logianalytics.com/hc/en-us/articles/5741415586199-Logi-Report-Server-Cluster-Main-Features#Algorithms) for load balancing clustered servers: Min-load, Round Robin, Weighted Min-load, or Random.
11. Select **Cluster Scheduler Lease** to enable lease for the cluster.

    Lease is a semaphore that enables a scheduler to be an active scheduler. If a scheduler is enabled with lease, it becomes an active scheduler and will compete to trigger the schedule. Each active scheduler can hold a lease for a period of time, which depends on the value you set for **Cluster Scheduler Lease Valid Time**, and then transfers it to another scheduler in the cluster. If you do not enable **Cluster Scheduler Lease**, all clustered servers in the cluster will compete for a chance to trigger scheduled tasks which could lower the overall system throughput. See [main features](https://devnet.logianalytics.com/hc/en-us/articles/5741415586199-Logi-Report-Server-Cluster-Main-Features) for more information.
12. In the **Cluster Scheduler Lease** **Active Count** text box, type the active lease number in the cluster. By setting the active lease number, you get to know how many active schedulers there are to compete to trigger the schedule. The property value should be an integer and the default value is 2.
13. In the **Cluster Scheduler Lease Valid Time** text box, type the period that the clustered server can hold a lease before releasing it. The property value should be an integer in seconds and the default value is 300.
14. In the **Cluster Scheduler Lease Check Interval** text box, type the time interval after which the cluster will check the number of active leases. The property value should be an integer in seconds and the default value is 30.
15. In the **Cluster Storage History Number of Copies**,
    **Cluster Storage Realm Number of Copies**, and **Cluster Storage CRD Result Number of Copies** text boxes, specify how many copies you want to make in the cluster when a new file or folder is added to the history, realm, and cached report data (CRD) result folders respectively. If you are using shared disk resources for any of these directories, you should set the value to 1. The default value is 2 which means making one copy plus the original. This enables any node to go down and the system will still be able to find all resources. If you want to allow 2 simultaneous failures, set the number of copies to 3.
16. In the **Cluster Memory Storage Number of Copies** text box, specify how many memory copies you want to share in the cluster. The property value should be a positive integer and the default value is 2. If there are quite a few clustered servers in a Logi Report Server Cluster, sharing memory in all cluster nodes would increase the network load exceedingly, which may lead to poor server performance and scalability.
17. Select **Notify via E-mail When a Server Is Down** if you need to notify somebody via email when a server in the cluster is down. Then in the **E-mail Address** text box, type the email addresses of the people to whom you want to send a notification email.
18. In the following text boxes, you can specify the corresponding directories. If you do not provide them, Server uses the default directories.
    * **Properties Directory**The properties directory for storing system data. The properties directory of each clustered server should better point to a different physical location.
    * **Realm Directory**The realm directory for storing system data. The realm directory of each clustered server should better point to a different physical location.
    * **Resource Root**The report root directory for storing system data. The resource root of each clustered server should better point to a different physical location.
    * **History Directory**The directory for storing report, catalog, and result files. The history directory of each clustered server should better point to a different physical location.
    * **Temporary Files Directory**The directory for storing temporary report files. When you run reports in the background, Server generates temporary report files to the **temp** directory. Each clustered server should use an individual **temp** folder to store its temporary files generated during its working process.
19. In the **Server's RMI Host** text box, type the RMI IP address or host name of the clustered server that other servers in the cluster can access.
20. In the **Server's RMI Port** text box, type the RMI port number of the clustered server.
21. Go on with the installation steps to complete the installation.
22. Install other servers you want to join the cluster.
23. Repeat the preceding steps to configure the cluster settings. When you install multiple servers on the same machine, you need to make sure they use different port numbers. For options that take effect on the cluster level such as Load Balancer Type, Cluster Scheduler Lease, cluster storage copies, and email notification setting, you do not need to set them repeatedly.

    Since Logi Report Server Cluster uses the same server DBMS, you need to make the system database in the **JDBC URL** text box point to the same DBMS as the previous server. You should replace **localhost** with the IP address of the first cluster node that you installed, for example, `jdbc:derby://IP:8886/`.

## Creating a Logi Report Server Cluster After Installation

You can set up a cluster either [via the Cluster UI](#Page)  or [using files](#File) after you have installed Logi Report Servers using the appropriate license key for Cluster.

**To configure a cluster via UI:**

1. Start up the Logi Report Server for which you have not enabled Cluster.
2. [Sign in to its Server Console](https://devnet.logianalytics.com/hc/en-us/articles/5741461387031-Accessing-Logi-Report-Server-via-a-Web-Browser).
3. On the system toolbar, navigate to **Administration** > **Configuration** > **Cluster** > **Configuration**.
4. In the **Cluster Name** text box, type a name for the cluster. You can either make the server join an existing cluster or specify a new cluster name to build another cluster.
5. Select **Enable Cluster**.
6. Select **Save** to enable the cluster.

   Logi Report automatically generates a cluster member ID for the server. You can find it via the property **cluster.member.id** in the **server.properties** file in `<install_root>\bin`. You should not change the auto generated cluster member ID in a Logi Report Server Cluster, because distributed storage uses the member ID to recognize on which clustered server it stores the physical files.
7. Go to the Administration > Configuration > Server DB > System DB/Realm DB/Profiling DB page.
8. Configure the databases to make sure they point to the database that the server will use. For more information, see [Configuring Server Databases for Server Metadata](https://devnet.logianalytics.com/hc/en-us/articles/5741387194519-Configuring-Server-Databases-for-Server-Metadata).
9. Restart the server you have enabled with cluster.
10. Sign in to its Server Console again.
11. Go to the Administration > Configuration > Cluster > Configuration page.

    ![Cluster - Configuration page](https://devnet.logianalytics.com/hc/article_attachments/9905831340439/clstr_set_set_config.gif)
12. Configure the server [as described from step 10 to 20](#Step7).
13. Shut down the server.
14. Start up another server you want to join the cluster.
15. Repeat the preceding steps to configure its cluster settings. If the servers are on the same machine, you need to make sure they use different port numbers. For options that take effect on the cluster level such as Load Balancer Type, Cluster Scheduler Lease, cluster storage copies, and email notification setting, you do not need to set them repeatedly.

**To set up a cluster using files:**

1. In the **server.properties** file in `<install_root>\bin`, set the property **cluster.enabled=true** for each server.
2. Modify the **cluster.name** property in any server's server.properties file to update the cluster name. If you do not do this, the cluster takes **logireport-cluster** as the default name.
3. In the server.properties file of each server, modify the two properties:
   * **server.rmi.host**=localhost IP address  
      The RMI IP address or host name of the server that other servers in the cluster can access.
   * **server.rmi.port**=1129  
      The RMI port number of the server. When the servers in the cluster are on the same machine, you must edit this property to make the servers use different port numbers.
4. Modify the **dbconfig.xml** file in `<install_root>\bin` for each server. Make sure that the system database and realm database for all servers in the cluster point to the same DBMS.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* You cannot use HSQLDB as the server's database in a Logi Report Server Cluster, because HSQLDB does not support the lock function.
* If you have upgraded your Logi Report Server which is cluster enabled and uses HSQLDB as the server database from a version prior to v9 to the current version, to make the server work normally, you need to disable cluster on the server by adding **server.cluster.enable=false** in the **server.properties** file.
* If you set up a Logi Report Server Cluster on one computer, make sure that HTTP Port and Server's RMI Port on each clustered server are different.
* If you want to use resources from [real paths](https://devnet.logianalytics.com/hc/en-us/articles/5741482166807-Getting-and-Using-Resources-From-a-Real-Path) in a Logi Report Server Cluster, you should first specify a disk in your file system and make sure that every clustered server in the cluster has the same disk name mapping to the same physical location.
* To fax reports in a cluster, you need to [configure the fax settings](https://devnet.logianalytics.com/hc/en-us/articles/5741416077591-Configuring-Export-Settings#Fax) for each clustered server respectively.
* When you enable a cluster, Server saves the following properties and their mapping UI options into the system database.
  + The properties in the server.properties file: cluster.enable\_notify\_server\_down, cluster.notify\_server\_down\_address, cluster.scheduler.lease.active\_count, cluster.scheduler.lease.check\_interval, cluster.scheduler.lease.enabled, cluster.scheduler.lease.valid\_time, cluster.send\_concurrent\_reports, cluster.share\_memory.node\_number, cluster.storage.crd\_result.copy\_number, cluster.storage.history.copy\_number, cluster.storage.realm.copy\_number, loadbalance.custom\_class, loadbalance.type, server.autocache.enabled, server.autocache.expired.time, server.autocache.max.disk.usage, server.autocache.never.expire, server.completed.max\_count, server.crd.memory.usage, server.realm.active, server.security, server.version.from.temp.
  + All properties in the **mailconfig.properties** file in `<install_root>\bin`.
  + All properties in the LDAP configuration XML file **LDAPProperties.xml** in `<install_root>\properties`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741415669527-Setting-Up-and-Starting-a-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741386996247-Starting-a-Logi-Report-Server-Cluster)
