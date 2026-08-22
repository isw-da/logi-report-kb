---
title: "Dispatching RMI Server Pages Requests in Multiple Server Environment"
id: 1500009644362
section: "Server Cluster Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644362-Dispatching-RMI-Server-Pages-Requests-in-Multiple-Server-Environment
updated_at: 2021-07-24T20:55:23Z
---

# Dispatching RMI Server Pages Requests in Multiple Server Environment

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669001-Clustering-Logi-JReport-Server-Guide-v15-Server-with-Oracle-WebLogic-Server-12c-12-1-3-)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674861-Logi-JReport-Server-Guide-v15-Security-System)

# Dispatching RMI Server Pages Requests in Multiple Server Environment

You can dispatch RMI Server Pages requests in multiple server environment, which includes Logi JReport clustered and non-clustered server environment.

**Sample solution: dispatch RMI Server Pages requests in clustered server environment using customized dispatcher**

This sample solution is to visit Server Pages JSPs remotely from WebSphere 7 to Logi JReport Clustered Server using customized dispatcher. See the below diagram for the structure:

![Customized Dispatcher](https://devnet.logianalytics.com/hc/article_attachments/4404920659351/clstr_srvpg1.gif)

You should be able to set up a similar service with any Java EE server by following the same procedure based on your preferred application server documentation.

This demo dispatcher dispatches requests from different sessions to different Logi JReport Servers according to Round-Robin algorithm. The dispatcher has the Fail Over function, which will periodically check whether there is any unavailable server in the cluster. No request will be dispatched to the unavailable server until the server is checked to be available again.

In general, the solution can be categorized into the following major steps:

1. [Set up the server cluster.](#Set)
2. [Generate a WAR file containing Server Pages RMI JSP and dispatcher for WebSphere.](#Generate)
3. [Deploy the WAR file to WebSphere.](#Deploy)
4. [Configure a clustered Logi JReport Server](#Config).

The following explains clearly the exact operations you are expected to make in each of the main steps.

**Step 1: Setting up the server cluster**

In this example we will set up two into the cluster using the Round-Robin algorithm.

192.168.0.1

192.168.0.2

Refer to [Setting up and configuring a Logi JReport Server Cluster](https://devnet.logianalytics.com/hc/en-us/articles/1500009644342-Setting-Up-and-Configuring-a-Logi-JReport-Server-Guide-v15-Server-Cluster) for the specific steps of setting up Logi JReport Server in a cluster.

**Step 2: Generating a WAR file containing Server Pages RMI JSP and dispatcher for WebSphere**

1. Build a Logi JReport Server WAR file as defined by makewar.xml for remote integration. The generated WAR file is saved to the default directory `<install_root>\bin\distribute`.

   `makewar.sh buildRemoteWar -Djrs.remote.host=192.168.0.1 -Djrs.remote.rmiport=1129 -Djrs.rmi.auth_file=/home/rmi.auth`
2. Compile the dispatcher DemoRemoteDispatcher.java stored in `<server_install_root>\help\samples\APICluster` with `<server_install_root>\lib\JRESServlets.jar` and `<server_install_root>\lib\javax.servlet-api-3.1.0.jar`. The class file DemoRemoteDispatcher.class and some other class files will be generated.
3. In the WAR file, drag the class files generated in step 2 to the remote.war\WEB-INF\classes\demodispath folder, assuming that this folder has already been created in the WAR file.

**Step 3: Deploying the WAR file to WebSphere**

1. Start IBM WebSphere 7.
2. Open Administrative Console. You can open Administrative Console by using the Start Menu, or by using the URL: `http://hostname:9060/ibm/console`, where hostname is host name or IP address, and 9060 is the port number.
3. After successfully logging in, expand the **Applications** node and then **Application Types**. Select **WebSphere enterprise applications**, and then select **Install**.
4. Select **Browse** to select your .war file. In the Context root field, type a context path such as /remote/ ("/remote" is also ok). Keep selecting **Next**.
5. Select **Finish** in the Summary page. The installing process may take several minutes, wait until the process is completed.
6. After the installation process is completed, select **Save directly to the master configuration**. Then in the Save directly to the master configuration dialog, select **Save**.
7. This step is to configure the dispatcher and cluster server. Go to WebSphere Admin Control to add some properties for this dispatcher. Expand **Servers**, go through **Server Types > WebSphere application servers** > **server1** > **Process definition** (in the Server Infrastructure table > Java and Process Management) > **Java Virtual Machine > Custom properties** (in the Additional Properties table).

   Select the **New** button to add properties for our demo dispatcher com.jinfonet.dispatcher.configFile and jrs.remote.dispatcher.

   Figure 1: Add property for com.jinfonet.dispatcher.configFile

   ![Add Property for com.jinfonet.dispatcher.configFile](https://devnet.logianalytics.com/hc/article_attachments/4404920659607/clstr_srvpg2.gif)

   Figure 2: Add property for jrs.remote.dispatcher

   ![Add Property for jrs.remote.dispatcher](https://devnet.logianalytics.com/hc/article_attachments/4404920659863/clstr_srvpg3.gif)

   Note that the dispatcher DemoRemoteDispatcher.java will read the clustered server information in the hostport.properties file like below:

   `rmiserver=192.168.0.1:1129  
    rmiserver=192.168.0.2:1130  
    ...`
8. If you have set up Logi JReport Server in a cluster, you can append their host and port information to the above text file.
9. Select the **Save** link in the Messages table to save the changes, and then restart WebSphere 7.

**Step 4: Configuring the Logi JReport Server Cluster**

1. Make sure Logi JReport Server has been started once in order that the server.properties file is generated.
2. Change server.properties file in `<server_install_root>\bin` as follows:

   `server.rmiserver.enable=true  
    server.rmiadminservice.enable=true`

Then you can start Logi JReport Server and access your Server Pages with a URL such as:

`http://hostname:9080/remote`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669001-Clustering-Logi-JReport-Server-Guide-v15-Server-with-Oracle-WebLogic-Server-12c-12-1-3-)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674861-Logi-JReport-Server-Guide-v15-Security-System)
