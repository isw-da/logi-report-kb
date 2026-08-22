---
title: "Setting Up and Configuring a Logi Report Server Cluster"
id: 1500009718702
section: "Logi Report Server Integration, Server Cluster, and Server Security Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718702-Setting-Up-and-Configuring-a-Logi-Report-Server-Cluster
updated_at: 2021-07-25T07:20:18Z
---

# Setting Up and Configuring a Logi Report Server Cluster

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744621-Setting-Up-and-Starting-a-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718722-Starting-a-Logi-Report-Server-Cluster)

# Setting Up and Configuring a Logi Report Server Cluster

This topic describes how you can set up a Logi Report Server Cluster either during the Logi Report Server installation or after you have installed the servers using the appropriate license key for cluster.

Before setting up a Logi Report Server Cluster, first you need to make the time difference between the target computers that will join the cluster as small as possible (the time difference between the target computers should be within one minute), and make sure all servers in the cluster use the same architecture and operating system.

Select the following links to view the topics:

* [Creating a Logi Report Server Cluster During Installation](#During)
* [Creating a Logi Report Server Cluster After Installation](#After)

## Creating a Logi Report Server Cluster During Installation

It is recommended that you create a Logi Report Server Cluster during the installation of servers. This is the easiest way to set up a cluster.

1. Run the Logi Report Server installation file to install Logi Report Server with the Installation Wizard.
2. Specifies your User ID. In the License Key text box, use the cluster enabled license key.
3. When choosing the installation type, select **Custom Installation for Standalone Server**. Then specify the installation directory for Logi Report Server.
4. In the **Service** tab of the Configure System Environment screen, select the **Network Address At** option and type the IP address of the server.

   ![Installation - Service tab](https://devnet.logianalytics.com/hc/article_attachments/4404936963991/clstr_set_set_svc.gif)
5. Select the **Cluster** tab. Specify a cluster name in the **Cluster Name** text box. You can either make the server join an existing cluster or specify a new cluster name to build another cluster.
6. Clear the **Disable Cluster** option at the bottom.

   ![Installation - Cluster tab](https://devnet.logianalytics.com/hc/article_attachments/4404936964247/clstr_set_set_clstr.gif)
7. From the Load Balancer Type drop-down list, select the built-in [algorithm](https://devnet.logianalytics.com/hc/en-us/articles/1500009718662-Logi-Report-Server-Cluster-Main-Features#Algorithms) for load balancing clustered servers: Min-load, Round Robin, Weighted Min-load, or Random.
8. Select the **Cluster Scheduler Lease** option to enable lease for the cluster, then set the active count, valid time and check interval in the following text boxes for the cluster scheduler lease.
   * **Cluster Scheduler Lease** **Active Count**  
      Specifies the active lease number in the cluster. By setting the active lease number, you get to know how many active schedulers there are to compete to trigger the schedule. The property value should be an integer and the default value is 2.
   * **Cluster Scheduler Lease Valid Time**  
      Specifies the period that the clustered server can hold a lease before releasing it. The property value should be an integer in seconds and the default value is 300.
   * **Cluster Scheduler Lease Check Interval**  
      Specifies the time interval the cluster will use to check the number of active leases. The property value should be an integer in seconds and the default value is 30.

   Lease is a semaphore that enables a scheduler to be an active scheduler. If a scheduler is enabled with lease, it becomes an active scheduler and will compete to trigger the schedule. Each active scheduler can hold a lease for a period of time, which depends on the value you set in the Cluster Scheduler Lease Valid Time text box, and then transfers it to another scheduler in the cluster. If you do not enable Cluster Scheduler Lease, all clustered servers in the cluster will compete for a chance to trigger scheduled tasks which could lower overall system throughput. See [main features](https://devnet.logianalytics.com/hc/en-us/articles/1500009718662-Logi-Report-Server-Cluster-Main-Features) for more information.
9. In the Cluster Storage History Number of Copies,
   Cluster Storage Realm Number of Copies and Cluster Storage CRD Result Number of Copies text boxes, specify how many copies will be made in the cluster when a new file or folder is added to the history, realm and cached report data (CRD) result folders respectively. If you are using shared disk resources for any of these directories you should set the value to 1. The default value is 2 which means make one copy plus the original. This allows any one node to go down and the system will still be able to find all resources. If you want to allow 2 simultaneous failures, set the number of copies to 3.
10. In the Cluster Memory Storage Number of Copies text box, specify how many memory copies will be shared in the cluster. The property value should be a positive integer and the default value is 2. If there are quite a few clustered servers in a Logi Report Server Cluster, sharing memory in all cluster nodes would increase the network load exceedingly which may lead to poor server performance and scalability.
11. Select **Notify via E-mail When a Server Is Down** if you need to notify somebody via e-mail when a server in the cluster is down, then in the E-mail Address text box, type the e-mail addresses of the people to whom you want to send a notification e-mail.
12. In the following text boxes, you can specify the corresponding directories. If they are not set, the default directories will be used.
    * **Properties Directory**Specifies the properties directory for storing system data. The properties directory of each clustered server should better point to a different physical location.
    * **Realm Directory**Specifies the realm directory for storing system data. The realm directory of each clustered server should better point to a different physical location.
    * **Resource Root**Specifies the report root directory for storing system data. The resource root of each clustered server should better point to a different physical location.
    * **History Directory**Specifies the directory for storing report/catalog/result files. The history directory of each clustered server should better point to a different physical location.
    * **Temporary Files Directory**Specifies the directory for storing temporary result files. Along with the running of Logi Report Server, temporary result files (generated by background run) will be written to the temp directory. Each clustered server should use an individual temp folder to store its temporary files generated during its working process.
13. In the Server's RMI Host text box, type the RMI IP address or host name of the clustered server which can be accessed by other servers that will join the cluster.
14. In the Server's RMI Port text box, type the RMI port number of the clustered server.
15. Go on with the installation steps to complete the installation.
16. Install other servers you want to join the cluster and repeat the above steps to configure the cluster settings. When some servers are installed on the same machine, you need to make sure they use different port numbers. For options that take effect on the cluster level such as Load Balancer Type, Cluster Scheduler Lease, cluster storage copies, e-mail notification setting, you do not need to set them repeatedly.

    Since Logi Report Server Cluster uses the same server DBMS, you need to make the system database in the JDBC URL text box point to the same DBMS as the previous server. This requires that you replace localhost with the IP address of the first cluster node that you installed, for example, `jdbc:derby://IP:8886/`.

## Creating a Logi Report Server Cluster After Installation

You can set up a cluster either [via the Cluster UI](#Page)  or [using files](#File) after you have installed Logi Report Servers using the appropriate license key for cluster.

**To configure a cluster via UI:**

1. Start up the Logi Report Server that has not been enabled for cluster.
2. [Log onto its server console](https://devnet.logianalytics.com/hc/en-us/articles/1500009749881-Accessing-Logi-Report-Server-via-a-Web-Browser).
3. Point to **Administration** on the system toolbar, select **Configuration** > **Cluster** > **Configuration** from the drop-down menu.
4. In the Cluster Name text box, specify a name for the cluster. You can either make the server join an existing cluster or specify a new cluster name to build another cluster.
5. Select the **Enable Cluster** option.
6. Select **Save** to enable the cluster.

   A cluster member ID will be generated automatically for the server. If you need to modify it, you need to go to server.properties located in `<install_root>\bin` and set the property cluster.member.id. However it is strongly recommended that you do not change the auto generated cluster member ID in a Logi Report Server Cluster, because distributed storage uses the member ID to recognize on which clustered server the physical files are stored.
7. Go to the Administration > Configuration > Server DB > System DB/Realm DB/Profiling DB page, configure the databases to make sure they point to the database that the server will use. For more information, see [Configuring the Server Database](https://devnet.logianalytics.com/hc/en-us/articles/1500009744781-Configuring-the-Server-Database).
8. Restart the server you have enabled with cluster and log onto its server console again.
9. Point to **Administration** on the system toolbar, select **Configuration** > **Cluster** > **Configuration** from the drop-down menu to open the Configuration page.

   ![Cluster - Configuration page](https://devnet.logianalytics.com/hc/article_attachments/4404942610583/clstr_set_set_config.gif)
10. Configure the server [as described from step 7 to 14](#Step7) in the above procedure.
11. Shut down the server.
12. Start up another server you want to join the cluster and repeat the above steps to configure its cluster settings. If the servers are on the same machine you need to make sure they use different port numbers. For options that take effect on the cluster level such as Load Balancer Type, Cluster Scheduler Lease, cluster storage copies, e-mail notification setting, you do not need to set them repeatedly.

**To set up a cluster using files:**

1. In the server.properties file located in `<install_root>\bin` of each server, set the property cluster.enabled=true.
2. Modify cluster.name in any server's server.properties file to specify the cluster name. If not specified, it will take logireport-cluster as the default name.
3. In the server.properties file of each server modify the two properties:
   * **server.rmi.host**=localhost IP address  
      Specifies the RMI IP address or host name of the server which can be accessed by other servers in the cluster.
   * **server.rmi.port**=1129  
      Specifies the RMI port number of the server. When the servers in the cluster are on the same machine, you must edit this property to make the servers use different port numbers.
4. Modify dbconfig.xml saved in `<install_root>\bin` for each server. Make sure that the system database and realm database all servers in the cluster use point to the same DBMS.

**Notes:**

* The databases that can be used as the server database in a Logi Report Server Cluster must be able to support the lock function, therefore, you cannot use HSQLDB as the server's database in a Logi Report Server Cluster because HSQLDB doesn't support the function.
* If you have upgraded your Logi Report Server which is cluster enabled and uses HSQLDB as the server database from versions prior to V9 to the current version, in order to make the server work normally, you need to disable cluster on the server by adding the line server.cluster.enable=false to the server.properties file.
* If you set up a Logi Report Server Cluster on one computer, you need to make sure that the settings of HTTP Port and Server's RMI Port on each clustered server are different.
* If you want to use resources from folder [real paths](https://devnet.logianalytics.com/hc/en-us/articles/1500009750141-Getting-and-Using-Resources-from-a-Real-Path) in a Logi Report Server Cluster, you should first specify a disk in your file system and make sure that every clustered server in the cluster has the same disk name mapping to the same physical location.
* In order to fax report result successfully in a cluster, you need to [configure the fax settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009744881-Configuring-Export-Settings#Fax) for each clustered server respectively.
* When a cluster is enabled the following properties and their mapping UI options will also be saved into the system database.
  + The following properties in the server.properties file: cluster.enable\_notify\_server\_down, cluster.notify\_server\_down\_address, cluster.scheduler.lease.active\_count, cluster.scheduler.lease.check\_interval, cluster.scheduler.lease.enabled, cluster.scheduler.lease.valid\_time, cluster.send\_concurrent\_reports, cluster.share\_memory.node\_number, cluster.storage.crd\_result.copy\_number, cluster.storage.history.copy\_number, cluster.storage.realm.copy\_number, loadbalance.custom\_class, loadbalance.type, server.autocache.enabled, server.autocache.expired.time, server.autocache.max.disk.usage, server.autocache.never.expire, server.completed.max\_count, server.crd.memory.usage, server.realm.active, server.security, server.version.from.temp.
  + All properties in the mailconfig.properties file in `<install_root>\bin`.
  + All properties in the LDAP configuration XML file LDAPProperties.xml in `<install_root>\properties`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744621-Setting-Up-and-Starting-a-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718722-Starting-a-Logi-Report-Server-Cluster)
