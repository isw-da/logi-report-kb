---
title: "Dispatching RMI Server Pages Requests in Multiple Server Environment"
id: 28891518489741
section: "Report Server Cluster Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891518489741-Dispatching-RMI-Server-Pages-Requests-in-Multiple-Server-Environment
updated_at: 2026-02-26T02:11:14Z
source_host: docs-report.zendesk.com
---
# 
Dispatching RMI Server Pages Requests in Multiple Server Environment 

You can dispatch RMI Server Pages requests in multiple-server environment, which includes clustered and non-clustered Report servers. This topic describes a sample solution in clustered server environment, which is to visit Server Pages JSPs remotely from WebSphere 7 to Report Clustered Server using customized dispatcher. 

The diagram illustrates the structure: 

You should be able to set up a similar service with any Java EE server by following the same procedure based on your application server documentation. 

This demo dispatcher dispatches requests from different sessions to different Report Servers according to Round-Robin algorithm. The dispatcher has the Fail Over function, which will periodically check whether there is any unavailable server in the cluster. No request will be dispatched to the unavailable server until the server is checked to be available again.

In general, the solution has the following major steps:

- Step 1: Set Up the Server Cluster

- Step 2: Generate a WAR File Containing Server Pages RMI JSP and Dispatcher for WebSphere

- Step 3: Deploy the WAR File to WebSphere

- Step 4: Configure a Clustered Report Server

## 
Step 1: Set Up the Server Cluster

 In this example we will set up two Report Servers into the cluster using the Round-Robin algorithm.

192.168.0.1
192.168.0.2

For more information, see Setting Up and Configuring a Report Server Cluster.

## 
Step 2: Generate a WAR File Containing Server Pages RMI JSP and Dispatcher for WebSphere

- Build a Report Server WAR file as defined by makewar.xml for remote integration. Server saves the generated WAR file to the default directory <install_root>\bin\distribute.
    makewar.sh buildRemoteWar -Djrs.remote.host=192.168.0.1 -Djrs.remote.rmiport=1129 -Djrs.rmi.auth_file=/home/rmi.auth

- Compile the dispatcher DemoRemoteDispatcher.java stored in <server_install_root>\help\samples\APICluster with <server_install_root>\lib\JRESServlets.jar and <server_install_root>\lib\jakarta.servlet-api-4.0.4.jar. The class file DemoRemoteDispatcher.class and some other class files will be generated.

- In the WAR file, drag the class files generated in step 2 to the remote.war\WEB-INF\classes\demodispath folder, assuming that this folder has already been created in the WAR file. 

## 
Step 3: Deploy the WAR File to WebSphere

- Start IBM WebSphere 7.

- Open Administrative Console. You can open Administrative Console using the Start Menu, or using the URL: http://hostname:9060/ibm/console, where hostname is host name or IP address, and 9060 is the port number.

- After signing in, expand the Applications node and then Application Types. Select WebSphere enterprise applications, and then select Install.

- Select Browse to select your .war file. In the Context root field, type a context path such as /remote/ ("/remote" is also OK). Keep selecting Next.

- Select Finish in the Summary page. The installing process may take several minutes, wait until the process is completed.

- After the installation process is completed, select Save directly to the master configuration. Then in the Save directly to the master configuration dialog box, select Save.

- This step is to configure the dispatcher and cluster server. Go to WebSphere Admin Control to add some properties for this dispatcher. Expand Servers, go through Server Types > WebSphere application servers > server1 > Process definition (in the Server Infrastructure table > Java and Process Management) > Java Virtual Machine > Custom properties (in the Additional Properties table).
    Select the New button to add properties for our demo dispatcher com.jinfonet.dispatcher.configFile and jrs.remote.dispatcher.

Figure 1: Add property for com.jinfonet.dispatcher.configFile

Figure 2: Add property for jrs.remote.dispatcher

 The dispatcher DemoRemoteDispatcher.java reads the clustered server information in the hostport.properties file like below:

rmiserver=192.168.0.1:1129
    rmiserver=192.168.0.2:1130
  ...

- If you have set up Report Server in a cluster, you can append their host and port information to the preceding text file.

- Select the Save link in the Messages table to save the changes, and then restart WebSphere 7.

## 
Step 4: Configure a Clustered Report Server

- Make sure you have started a clustered Report Server once so that the server.properties file is generated in <server_install_root>\bin.

- Change server.properties:
    server.rmiserver.enable=true
server.rmiadminservice.enable=true

Then you can start the Report Server and access your Server Pages with a URL: 

http://hostname:9080/remote
