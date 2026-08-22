---
title: "Clustering Logi JReport Server with Oracle WebLogic Server 12c (12.1.3)"
id: 1500009686602
section: "Server Cluster Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009686602-Clustering-Logi-JReport-Server-with-Oracle-WebLogic-Server-12c-12-1-3
updated_at: 2021-11-03T06:58:29Z
---

# Clustering Logi JReport Server with Oracle WebLogic Server 12c (12.1.3)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712301-Managing-a-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686582-Dispatching-RMI-Server-Pages-Requests-in-Multiple-Server-Environment)

# Clustering Logi JReport Server with Oracle WebLogic Server 12c (12.1.3)

This topic describes how to configure a WebLogic 12c cluster and then integrate Logi JReport Server in the cluster. It is assumed that the server cluster contains an admin server named adminNew (port 7001), a proxy server named proxy, and two managed servers named manage1 and manage2. Each clustered computer should have a unique IP address or host name.

The procedure contains the following major steps:

1. [Install Oracle WebLogic Server 12c (12.1.3)](#Install)
2. [Configure an Oracle WebLogic cluster](#Configure)
3. [Deploy Logi JReport to the Oracle WebLogic cluster](#Deploy)

**Step 1: Installing Oracle WebLogic Server 12c (12.1.3)**

1. As an administrator, run the installation file fmw\_12.1.3.0.0\_wls.jar downloaded from Oracle website to start the Oracle Fusion Middleware 12c WebLogic Server and Coherence Installation wizard. Select **Next**.

   ![Oracle WebLogic Server Installation Wizard](https://devnet.logianalytics.com/hc/article_attachments/4412139617175/clstr_wblgc1.gif)
2. In the Installation Location screen, set the Oracle Home as `C:\Oracle12c\Middleware\Oracle_Home`. Select **Next**.

   ![Installation Location screen](https://devnet.logianalytics.com/hc/article_attachments/4412131511319/clstr_wblgc2.gif)
3. In the Installation Type screen, choose **Coherence**.

   ![Installation Type screen](https://devnet.logianalytics.com/hc/article_attachments/4412139617431/clstr_wblgc3.gif)
4. Keep selecting **Next** till the Installation Complete screen, then select **Finish** to finish the installation.

   ![Installation Complete screen](https://devnet.logianalytics.com/hc/article_attachments/4412131511575/clstr_wblgc4.gif)

**Step 2: Configuring an Oracle WebLogic cluster**

1. Start the Configuration Wizard. On Windows you can start it by selecting **Start** > **Oracle** > **OracleHome** > **WebLogic Server 12c** **(12.1.3)**> **Tools** > **Configuration Wizard**.
2. In the Create Domain page, select **Create a new domain** and then select **Next**.

   ![Create Domain page](https://devnet.logianalytics.com/hc/article_attachments/4412139617815/clstr_wblgc5.gif)
3. In the Templates page, check **Create Domain Using Product Templates** and choose **WebLogic Coherence Cluster Extension - 12.1.3.0 [wlserver]** from the available templates list, and then select **Next**.

   ![Templates page](https://devnet.logianalytics.com/hc/article_attachments/4412139618071/clstr_wblgc6.gif)
4. In the Administrator Account page, enter the name and password, and then select **Next**.

   ![Administrator Account page](https://devnet.logianalytics.com/hc/article_attachments/4412112635799/clstr_wblgc7.gif)
5. In the Domain Mode and JDK page, choose **Production** for Domain Mode and **Oracle HotSpot 1.7.0\_10 C:\Java\JDK17~1.0\_1** for JDK. Select **Next**.

   ![Domain Mode and JDK page](https://devnet.logianalytics.com/hc/article_attachments/4412139618327/clstr_wblgc8.gif)
6. In the Advanced Configuration page, keep the three advanced configuration options selected, then select **Next**.

   ![Advanced Configuration page](https://devnet.logianalytics.com/hc/article_attachments/4412112636055/clstr_wblgc9.gif)
7. In the Administration Server page, enter the IP address of your machine in the Listen Address field. Change or accept the default settings for **Server Name** and **Listen Port**. Then select **Next**.

   ![Administration Server page](https://devnet.logianalytics.com/hc/article_attachments/4412139618583/clstr_wblgc10.gif)
8. In the Node Manager page, choose **Per Domain****Default Location** for Node Manager Type. and then select **Next**.

   ![Node Manager page](https://devnet.logianalytics.com/hc/article_attachments/4412139618839/clstr_wblgc11.gif)
9. In the Managed Servers page, select **Add** to add two managed servers and a proxy server as follows:

   ![Managed Servers page](https://devnet.logianalytics.com/hc/article_attachments/4412112636311/clstr_wblgc12.gif)

   **Note:** Keep in mind that each server instance in your cluster, including the admin server, proxy server and all managed servers, must have a unique Listen Address and Listen Port. If your managed server has the same Listen Address as the admin server, change the default values shown for the listen ports in this page, and enter the same Listen Address as you assigned to the Admin Server. After assigning a unique Listen Address and Listen Port combination, select the **Add** button to create another managed server.
10. In the Clusters page, add a cluster named **Cluster\_28**. Then select **Next**.

    ![Clusters page](https://devnet.logianalytics.com/hc/article_attachments/4412112636567/clstr_wblgc13.gif)
11. In the Assign Servers to Clusters page, highlight the managed servers and the proxy server in the left column, and then use the right arrow button to assign the servers to the cluster listed in the right column. Then select **Next**.

    ![Assign Servers to Clusters page](https://devnet.logianalytics.com/hc/article_attachments/4412112636823/clstr_wblgc14.gif)
12. In the Coherence Clusters page, set the Cluster Name as **defaultCoherenceCluster** and Unicast Listen Port as **0**, and then select **Next**.

    ![Coherence Clusters page](https://devnet.logianalytics.com/hc/article_attachments/4412139619223/clstr_wblgc15.gif)
13. In the Machines page, add two machines as follows:

    ![Machines page](https://devnet.logianalytics.com/hc/article_attachments/4412139619479/clstr_wblgc16.gif)
14. Assign servers to machines. Assign the admin server, server manage1 and the proxy server to the machine Machine\_zjh. Assign server manage2 to the machine Machine\_zwm.

    ![Assign Servers](https://devnet.logianalytics.com/hc/article_attachments/4412112640279/clstr_wblgc17.gif)
15. Review your configuration specifications and configure the domain. Then select **Create**.

    ![Configure Domain](https://devnet.logianalytics.com/hc/article_attachments/4412139620247/clstr_wblgc18.gif)
16. Start the servers on machine Machine\_zjh:

    Start the admin server on the admin server:

    `C:\Oracle12c\Middleware\Oracle_Home\user_projects\domains\base_domain\bin\startWebLogic.cmd.`

    Start the node manager:

    `C:\Oracle12c\Middleware\Oracle_Home\user_projects\domains\base_domain\bin\startNodeManager.cmd.`

    Start and log onto the proxy server on the proxy server:

    `C:\Oracle12c\Middleware\Oracle_Home\user_projects\domains\base_domain\bin\startManagedWebLogic.cmd proxy http://127.0.0.114:7001`.

    Start and log onto the manage1 server on manage1 server:

    `C:\Oracle12c\Middleware\Oracle_Home\user_projects\domains\base_domain\bin\startManagedWebLogic.cmd manage1 http://127.0.0.114:7001`.
17. Now let's configure another managed server. Repeat step 1 to 8 for manage2.
18. Skip the Managed Servers page, the Clusters page and the Assign Servers to Clusters page. In the Coherence Clusters page, set the Cluster Name as **defaultCoherenceCluster** and Unicast Listen Port as **0**, and then select **Next**.

    ![Coherence Clusters page](https://devnet.logianalytics.com/hc/article_attachments/4412139620503/clstr_wblgc19.gif)
19. Skip the Machines page. In the Configuration Summary page, select **Create**.

    ![Configuration Summary page](https://devnet.logianalytics.com/hc/article_attachments/4412131511831/clstr_wblgc20.gif)
20. Start the servers on machine Machine\_zwm:

    Start the admin server on the admin server:

    `C:\Oracle12c\Middleware\Oracle_Home\user_projects\domains\base_domain\bin\startWebLogic.cmd.`

    Start the node manager:

    `C:\Oracle12c\Middleware\Oracle_Home\user_projects\domains\base_domain\bin\startNodeManager.cmd.`

    Start and log onto the manage2 server on manage2 server:

    `C:\Oracle12c\Middleware\Oracle_Home\user_projects\domains\base_domain\bin\startManagedWebLogic.cmd manage2 http://127.0.0.114:7001`.

**Step 3: Deploying Logi JReport to the Oracle WebLogic cluster**

1. Start WebLogic by running startWeblogic.cmd in `C:\Oracle12c\Middleware\Oracle_Home\user_projects\domains\base_domain\bin`.
2. Access the WebLogic Server Administrative Console 12c using the URL `http://127.0.0.114:7001/console/`, where 127.0.0.114 is host name or IP address, and 7001 is the port number.
3. Go to **Home** > **Summary of Environment** > **Summary of Servers** > **Summary of Deployments**. In the Available targets for jreport section, choose the cluster named **Cluster\_28** and check **Part of the cluster**, then choose the two managed servers **manage1** and **manage2** as well as the proxy server **proxy**. Select **Finish** to finish selecting deployment targets.
4. Go to **Home** > **Summary of Environment** > **Summary of Servers** > **Summary of Deployments** > **jreport**, select the **Save** button to save the settings for jreport. When you see the message Settings updated successfully, select the **Activate Changes** button in the Change Center panel on the left.
5. Continue to go to **Home** > **Summary of Environment** > **Summary of Servers** > **Summary of Deployments** > **jreport** > **Summary of Deployments**. In the Deployments section of Control panel, select the **Start** drop-down list and choose **Servicing all requests**. Select the **Lock & Edit**  button in the Change Center panel on the left.
6. Wait until the deployments state of jreport changes to Active.
7. Start Logi JReport Server using the URL `http://127.0.0.114:7008/jreport`. 127.0.0.114 is host name or IP address for the proxy server, and 7008 is its port number.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712301-Managing-a-Logi-Report-Server-Cluster)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686582-Dispatching-RMI-Server-Pages-Requests-in-Multiple-Server-Environment)
