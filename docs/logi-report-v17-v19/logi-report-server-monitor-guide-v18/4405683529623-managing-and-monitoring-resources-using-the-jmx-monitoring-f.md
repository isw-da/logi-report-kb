---
title: "Managing and Monitoring Resources Using the JMX Monitoring Features"
id: 4405683529623
section: "Logi Report Server Monitor Guide v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683529623-Managing-and-Monitoring-Resources-Using-the-JMX-Monitoring-Features
updated_at: 2022-01-27T07:58:25Z
---

# Managing and Monitoring Resources Using the JMX Monitoring Features

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683531799-Creating-Profiling-Reports)   [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690460567-Integrating-Server-Monitor-with-a-Servlet-Enabled-Web-Server)

# Managing and Monitoring Resources Using the JMX Monitoring Features

This topic describes JMX Monitoring features and how you can manage and monitor resources by using these features.

JMX is a Java standard in the aspect of management. It provides a local or remote model for managing Java application systems. Its target is to offer the instrumentation, which all kinds of application management systems can access.

A JMX-compliant application server makes all registered manageable resources possible to be managed, configured, and controlled easily and flexibly. You can dynamically modify and process all those managed resources by third-party management software or other management component systems.

This topic contains the following sections:

* [JMX Monitoring Features of Server](#Feature)
* [Using the JMX Monitoring Features](#Use)
* [JMX Monitoring in an Integration Environment](#Integ)
* [Notes for Using the JMX Monitoring Function](#Note)

## JMX Monitoring Features of Server

This section introduces the infrastructure with which to implement the JMX Monitoring features and the implementing methods that you can use.

**MBeans building principle**

Logi Report adopts a Standard MBean specification for building Server's underlying managed beans.

In the process of creating and registering the JMX MBean, Logi Report designed and abstracted all meta-data of all managed resources and then saved them into their corresponding persistent entities. At runtime, the program changes all these meta-data into MBeanInfo and then adds them to the related Managed Bean.

After all these MBeans have been built, they are then registered into an internal or external MBeanServer Agent. Only when top-level management software or other integration environments can find the MBeanServer agent, can they manage and control all the underlying Managed Beans registered in the MBeanServer.

**Working principle behind the JMX Monitoring function**

With Server Monitor, when all the managed resources objects of Logi Report Server have been initiated and instantiated, the Managed MBeans are then registered into the MbeanServer. Then all the attributes, operations, notifications, and constructors of the associated Managed resource object are exposed to the MBeanServer via the corresponding Managed Bean. The MBeanServer then exposes all these registered Managed Beans to the top-level management system resorted to the related Protocol Adaptors or Connectors.

In Server Monitor's environment, when launching Server Monitor, Logi Report first creates ClusterRuntimeMBean and ServerRuntimeMBean for every active Server in the cluster, and TaskRuntimeMBean, UserSessionRuntimeMBean, DatabaseRuntimeMBean, and AdhocRuntimeMBean for every active running Server. Then you can register all these MBeans into the integrated customized MBeanServer or Standalone MBeanServer agent. At any time, when a Server is launched, the TaskRuntimeMBean, UserSessionMBean, DatabaseRuntimeMBean, and AdhocRuntimeMBean associated with it are created and registered into the MBeanServer agent. Then, all Server's monitoring features can be exposed to top-level management software or other integration environment resorted to the MBeanServer agent.

So, all the Runtime MBeans of Task, User Session, Database, and Ad hoc related are dynamically created in real time and registered into a local MBeanServer. The MBeanServer then invokes all registered MBean operation or attributes to implement the JMX monitoring function.

**Descriptions of MBeans in Server**

When starting, Server Monitor creates the following MBeans:

* **ClusterRuntimeMBean**
  + **Attributes**:  
    ClusterEnable (boolean)  
    ClusterName (java.lang.String)  
    PredefinedServerStatus(jet.server.monitor.api.ServerStatus[])  
    PredefinedServers(jet.server.api.cluster.Member[])
  + **Operations**:  
    ServerStatus getServerStatus(String host, int port);  
    stopServer(String host, int port);
* **ServerRuntimeMBean**
  + **Attributes**:  
    Name (java.lang.String)  
    Host (java.lang.String)  
    Port (int)  
    Status (java.lang.String)  
    Type (java.lang.String)  
    WaitingRptNums (int)  
    RunningRptNums (int)  
    FinishedRptNums (int)  
    FinishedRptPages (int)  
    AvgProcessTimeByRpt (int)  
    AvgWaitTimeByRpt (int)  
    ValidUserSessionNums (int)  
    AvgRptNumsSubmittedByUser (int)  
    CurrentConnectionNums (int)
  + **Operations**:  
    void stop();
* **TaskRuntimeMBean**
  + **Attributes**:  
    AllFailedTaskInfos(jet.server.monitor.api.task.TaskInfo[])  
    AllFinishedTaskInfos(jet.server.monitor.api.task.TaskInfo[])  
    AllRunningTaskInfos(jet.server.monitor.api.task.TaskInfo[])  
    AllWaitingTaskInfos(jet.server.monitor.api.task.TaskInfo[])
  + **Operations**:  
    TaskInfo[] getRunningTaskInfosByUser(String userName);  
    TaskInfo[] getWaitingTaskInfosByUser(String userName);  
    TaskInfo[] getFinishedTaskInfosByUser(String userName);  
    TaskInfo[] getFailedTaskInfosByUser(String userName);  
    void stopTask(String taskID);
* **UserSessionRuntimeMBean**
  + **Attributes**:  
    AllUserSessions(jet.server.api.UserSession[])  
    SessionTimeout (int)
  + **Operations**:  
    UserSession[] getUserSessionsByUser(String userName);  
    void removeUserSessionBySessionID (String sessionID);  
    void removeUserSessionsByUserID (String userID);  
    void removeAllUserSessions ();  
    String getHttpSessionID (String usID);
* **DatabaseRuntimeMBean**
  + **Attributes**:   
    ConnectionProperties(java.util.Properties[])
  + **Operations**:  
    void disconnect (String connInfoID);

**HtmlAdaptor**

Logi Report provides an HtmlAdaptor, which enables all registered Server's MBeans to be viewed from web pages. This HtmlAdaptor is based on the default implementation of Sun's JMX tools. It can process a user's HTTP request and dispatch it to the MBeanServer Agent and respond to client-end web pages according to the MBeanServer's return information.

The HtmlAdaptor is also instantiated as an MBean and registered into the MBeanServer Agent. Due to this, you can modify its listener port or other properties from the MBeanServer just like other MBeans.

By default, the HTMLAdaptor uses the port 8849 for providing web services. You can modify it and specify a distinct port in the **server.properties** file in `<install_root>\bin`. If you have launched Server Monitor and JMX startup has been set to true, a property item named monitor.jmx.htmladaptor.port will then be appended to the server.properties file in `<install_root>\bin`.

After launching Server and Server Monitor, and setting the monitor JMX startup property to true, all registered Server's MBeans will then be available for viewing from a web page (`http://localhost:8849` by default).

**Supporting tips information in the web UI (some auxiliary tools)**

In the default implementation mode, MBeanServer builds all MBean information. The MBeanServer Agent adopts all the descriptions and names of attributes, operations, and parameters displayed in the web UI as the default contents.

For friendly supporting tips information in the web UI, Logi Report has improved all the managed beans with extended methods for supporting customized descriptions and names of the attributes, operations, and parameters. It builds all these customized descriptions and names into the MBeanInfo of all the registered MBeans. The MBeanServer invokes these methods to obtain our customized descriptions and names of all displayed MBeanInfo's attributes, operations, and parameters in the web UI.

## Using the JMX Monitoring Features

Logi Report has created a local MBeanServer for managing all Runtime MBeans in the default mode. The management program within a standalone can directly get an MBeanServer's reference via the default implementation of the MBeanServerFinder interface.

In addition, you can also specify your customized MBeanServerFinder's implementation for obtaining an external MBeanServer agent when launching Server Monitor. You then need only to append the Java option `-Djrs.externalMBeanServerProvider=` with your fully qualified customized class file name to the Java command line that launches Server Monitor.

When Server Monitor has started and the JMX feature supporting has been set to true, it then gets the System property of rs.externalMBeanServerProvider. If this property has been set, Server Monitor uses it to obtain an external MBeanServer Agent. Otherwise, it adopts a default standalone MBeanServerFinder implementation to get the internal default MBeanServer Agent.

After launching Server and Server Monitor, and setting monitor JMX startup property to true, all registered Server's MBeans will be available for view from a web page (default `http://localhost:8849`).

## JMX Monitoring in an Integration Environment

In an integration environment with top-level Java-enabled management software or another JMX-compliant HTTP application server, that application server has probably already provided an MBeanServer Agent for managing its manageable beans. When integrating Server and Server Monitor with that application server, all of Server's MBeans should also be registered into its existing MBeanServer.

We provide an MBeanServerFinder interface to support your customized implementation for obtaining an external MBeanServer Agent.

If you want to integrate Server and Server Monitor with other JMX-enabled application server environment, you should provide an MBeanServerFinder's implementation for obtaining the application server's MBeanServer Agent, and append their implemented fully-qualified class file name with the java option `-Djrs.externalMBeanServerProvider=` to the corresponding application server's launching Java command line. Then, after launching the application server integrated with Server and Server Monitor, if you enable JMX startup, then all Server's MBeans will be built and registered into the application server's MBeanServer Agent. At the same time, the default HtmlAdaptor Logi Report provides will also be built and registered into the external MBeanServer Agent. Then you can view all registered Server's MBeans and the application server's registered managed beans from the HtmlAdaptor or via the application server's provided interface.

In the default implementation, Logi Report has also provided three general integration-related MBeanServerFinder implementations as simple samples: JBossMBeanServerFinderImpl, TomcatMBeanServerFinderImpl, and WebLogicMBeanServerFinderImpl. When you integrate Server and Server Monitor with JBoss, Tomcat, and WebLogic complied with JMX features, they can provide their implemented external MBeanServerFinder implementation to the Java command line option `-Djrs.externalMBeanServerProvider=`, or directly use our default implementation and append it to the Java option.

## Notes for Using the JMX Monitoring Function

When using the JMX Monitoring function, pay attention to the following aspects:

* In the MBeanServerFinder interface, Logi Report has just specified one interface method public MBeanServer getMBeanServer(); You need to implement this interface method and provide a public Constructor method without any parameters.
* When compiling and releasing our JMX features, it is required to append two Sun's JMX standard packages jmxri.jar and jmxtools.jar. Otherwise, you will be required to use JDK V1.8.0 or later version (In J2SE V1.8.0 and later, Sun Co. has also provided a JMX standard API as a part of JDK's standard APIs).
* When compiling our JMX features with the four external integration MBeanServerFinder's implementation(JBossMBeanServerFinderImpl, TomcatMBeanServerFinderImpl, WebLogicMBeanServerFinderImpl, and WebSphereMBeanServerFinderImpl), it is required to append the three integration platform-related packages to the javac class path: "`$jboss-root$\lib\jboss-jmx.jar` (for JBoss V3.2.3)", "`$tomcat-root$\server\lib\catalina.jar` (for Tomcat V4.1.30)" and "`$weblogic-root$\server\lib\weblogic.jar` (for WebLogic V810)". However, these three packages do not need to be appended to our release products.
* Since the JMX monitoring function is based on the currently existing Server Monitor and is built into Server Monitor, then only Server Monitor's release version is required for appending Sun's JMX standard packages to Server Monitor's **lib** folder. The JMX feature of Server does not require to append anything.

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683531799-Creating-Profiling-Reports)   [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690460567-Integrating-Server-Monitor-with-a-Servlet-Enabled-Web-Server)
