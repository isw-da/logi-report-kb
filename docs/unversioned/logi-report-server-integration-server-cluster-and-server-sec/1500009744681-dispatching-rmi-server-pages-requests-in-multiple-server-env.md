---
title: "Dispatching RMI Server Pages Requests in Multiple Server Environment"
id: 1500009744681
section: "Logi Report Server Integration, Server Cluster, and Server Security Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744681-Dispatching-RMI-Server-Pages-Requests-in-Multiple-Server-Environment
updated_at: 2021-07-25T07:20:18Z
---

# Dispatching RMI Server Pages Requests in Multiple Server Environment

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718742-Clustering-Logi-Report-Server-with-Oracle-WebLogic-Server-12c-12-1-3-)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724342-Logi-Report-Server-Security-System)

# Dispatching RMI Server Pages Requests in Multiple Server Environment

You can dispatch RMI Server Pages requests in multiple-server environment, which includes clustered and non-clustered Logi Report servers. This topic describes a sample solution in clustered server environment, which is to visit Server Pages JSPs remotely from WebSphere 7 to Logi Report Clustered Server using customized dispatcher.

The diagram below illustrates the structure:

![Customized Dispatcher](https://devnet.logianalytics.com/hc/article_attachments/4404942610327/clstr_srvpg1.gif)

You should be able to set up a similar service with any Java EE server by following the same procedure based on your application server documentation.

This demo dispatcher dispatches requests from different sessions to different Logi Report Servers according to Round-Robin algorithm. The dispatcher has the Fail Over function, which will periodically check whether there is any unavailable server in the cluster. No request will be dispatched to the unavailable server until the server is checked to be available again.

In general, the solution has the following major steps:

* [Step 1: Set Up the Server Cluster](#Set)
* [Step 2: Generate a WAR File Containing Server Pages RMI JSP and Dispatcher for WebSphere](#Generate)
* [Step 3: Deploy the WAR File to WebSphere](#Deploy)
* [Step 4: Configure a Clustered Logi Report Server](#Config)

## Step 1: Set Up the Server Cluster

In this example we will set up two Logi Report Servers into the cluster using the Round-Robin algorithm.

192.168.0.1  
192.168.0.2

For more information, refer to [Setting Up and Configuring a Logi Report Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/1500009718702-Setting-Up-and-Configuring-a-Logi-Report-Server-Cluster).

## Step 2: Generate a WAR File Containing Server Pages RMI JSP and Dispatcher for WebSphere

1. Build a Logi Report Server WAR file as defined by makewar.xml for remote integration. Report Server saves the generated WAR file to the default directory `<install_root>\bin\distribute`.

   `makewar.sh buildRemoteWar -Djrs.remote.host=192.168.0.1 -Djrs.remote.rmiport=1129 -Djrs.rmi.auth_file=/home/rmi.auth`
2. Compile the dispatcher DemoRemoteDispatcher.java stored in `<server_install_root>\help\samples\APICluster` with `<server_install_root>\lib\JRESServlets.jar` and `<server_install_root>\lib\jakarta.servlet-api-4.0.3.jar`. The class file DemoRemoteDispatcher.class and some other class files will be generated.
3. In the WAR file, drag the class files generated in step 2 to the remote.war\WEB-INF\classes\demodispath folder, assuming that this folder has already been created in the WAR file.

## Step 3: Deploy the WAR File to WebSphere

1. Start IBM WebSphere 7.
2. Open Administrative Console. You can open Administrative Console using the Start Menu, or using the URL: `http://hostname:9060/ibm/console`, where hostname is host name or IP address, and 9060 is the port number.
3. After successfully logging in, expand the **Applications** node and then **Application Types**. Select **WebSphere enterprise applications**, and then select **Install**.
4. Select **Browse** to select your .war file. In the Context root field, type a context path such as /remote/ ("/remote" is also OK). Keep selecting **Next**.
5. Select **Finish** in the Summary page. The installing process may take several minutes, wait until the process is completed.
6. After the installation process is completed, select **Save directly to the master configuration**. Then in the Save directly to the master configuration dialog box, select **Save**.
7. This step is to configure the dispatcher and cluster server. Go to WebSphere Admin Control to add some properties for this dispatcher. Expand **Servers**, go through **Server Types > WebSphere application servers** > **server1** > **Process definition** (in the Server Infrastructure table > Java and Process Management) > **Java Virtual Machine > Custom properties** (in the Additional Properties table).

   Select the **New** button to add properties for our demo dispatcher com.jinfonet.dispatcher.configFile and jrs.remote.dispatcher.

   Figure 1: Add property for com.jinfonet.dispatcher.configFile

   ![Add Property for com.jinfonet.dispatcher.configFile](https://devnet.logianalytics.com/hc/article_attachments/4404936963479/clstr_srvpg2.gif)

   Figure 2: Add property for jrs.remote.dispatcher

   ![Add Property for jrs.remote.dispatcher](https://devnet.logianalytics.com/hc/article_attachments/4404936963735/clstr_srvpg3.gif)

   Note that the dispatcher DemoRemoteDispatcher.java will read the clustered server information in the hostport.properties file like below:

   rmiserver=192.168.0.1:1129  
    rmiserver=192.168.0.2:1130  
    ...
8. If you have set up Logi Report Server in a cluster, you can append their host and port information to the above text file.
9. Select the **Save** link in the Messages table to save the changes, and then restart WebSphere 7.

## Step 4: Configure a Clustered Logi Report Server

1. Make sure you have started a clustered Logi Report Server once so that the server.properties file is generated in `<server_install_root>\bin`.
2. Change server.properties as follows:

   server.rmiserver.enable=true  
   server.rmiadminservice.enable=true

Then you can start the Logi Report Server and access your Server Pages with a URL as follows:

`http://hostname:9080/remote`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718742-Clustering-Logi-Report-Server-with-Oracle-WebLogic-Server-12c-12-1-3-)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724342-Logi-Report-Server-Security-System)
