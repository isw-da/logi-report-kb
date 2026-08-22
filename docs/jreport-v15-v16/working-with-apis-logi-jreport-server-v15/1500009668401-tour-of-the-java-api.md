---
title: "Tour of the Java API"
id: 1500009668401
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009668401-Tour-of-the-Java-API
updated_at: 2021-07-24T20:55:30Z
---

# Tour of the Java API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668361-Technical-Architecture)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644182-Java-API-for-a-Servlet)

# Tour of the Java API

This topic is a high-level survey of the Logi JReport Server API. The intent is to show boundaries of interest so that a developer can narrow down the set of APIs to look at when needing to use Logi JReport Server for a particular task.

Below is a list of the sections covered in this topic:

* [Using Logi JReport Server With an Existing Application](#Existing)
* [Java Application Programming Interface (API)](#API)

## Using Logi JReport Server With an Existing Application

There are three ways to use Logi JReport Server with an application:

* Use the web application composed of Logi JReport Server JSP pages. Allow users to browse to the existing web pages for an interactive session to make report requests, rather than write new programs to offer special features based on calls the Java API.
  The web application components offer a full set of report functions as well as listing available report resources based on the user's identity and permissions.
  These can be used with an application built with any technology including .NET and HTML web pages.
* Use the compiled servlets to make direct requests by URL. Although not technically an API, they serve the same purpose. Action requests are the method calls, with query parameters similar to method parameters. The set of servlet actions is limited to running, scheduling and viewing results. These can be used with an application built with any technology that can request a URL including HTML web pages, .NET applications and Java web applications.
* Use the Java API classes and methods. They are called directly from a Java program to extend existing applications by building in access to Logi JReport functionality. These same Java API classes and methods are used by Logi JReport servlets and JSP web pages. Each Java API method has a Javadoc entry that describes how to use it.

  Every function of Logi JReport is available through classes in the Java API including creating and modifying catalogs and reports, providing security such as Single Sign-On (SSO) authentication and authorization, running reports, scheduling reports and viewing results.

The Logi JReport Server Java API classes provide thousands of methods, each having a Javadoc entry describing the method and parameters. It is this library of classes and methods that is explained below, showing the relationship of classes to particular functional areas.

This tour section categorizes the Java API classes by functionality making it easier to find specific methods to use for particular situations.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Java Application Programming Interface (API)

Logi JReport Server provides a library of classes and methods called the Java API.

The major functional areas in the library are categorized below into sections.

Each functional area will show the class or interface name and have a general description. Below that will be a list of common methods, and other information as needed.

### Initializing and Connecting to Logi JReport Server

Every program that uses Logi JReport Server Java API must start with calls to ensure an instance of the server is running, and then obtain a handle to the server for use in later API calls.

**Class:** [jet.server.api.http.HttpUtil](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/http/HttpUtil.html) - This class provides a variety of utilities for programs running within a Java Servlet container.

Additionally, the two most commonly used methods of the Java API are in this class. These two methods must be called by any program that wants to use Logi JReport Server in order to initialize and connect to Logi JReport Server. These will still be used by programs that run outside a servlet container.

* **Method:**  HttpUtil.initEnv(); - initialize and start the singleton Logi JReport Server running on the machine which all programs will access.
* **Method:**  HttpUtil.getHttpRptServer(); - connect to the running Logi JReport Server and return a handle to the server to use in future API calls.

### Security

Every web application must manage access control, identity of a visitor, permissions for a visitor, and maintain this across multiple HTTP Requests that define the web session for the user.

Logi JReport Server provides built-in methods for doing this based on a protocol using HTTP Authentication and query parameters to pass in log-in credentials. The security mechanism includes a framework system that allows application developers to write code to co-operate with Logi JReport Server's built-in system so that existing applications can provide the security functionality.

* **Control access to web pages**
  + **Class:** [jet.server.api.http.HttpUtil](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/http/HttpUtil.html) - This class provides a variety of utilities for programs running within a Java Servlet container.
    - **Method:**  HttpUtil.checkLogin(); - This method only returns when a validated Logi JReport User is logged into the web session. If a user is already logged in, it returns true. If not, it tries to validate and login a user based on credentials in the current HTTP request. If no logged-in user can be identified, it will send a response to the browser to perform an HTTP Authentication to obtain credentials, using the browser login dialog form. The credentials are sent back to the same JSP page in the next HTTP Request.
  + **Class:** [jet.server.api.http.HttpUserSessionManager](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/http/HttpUserSessionManager.html) - This class provides methods that help to create and manage the UserSession associated with a logged in user.
    - **Method:**  HttpUserSessionManager.checkLogin(); - indicates if a validated Logi JReport User is logged into the web session. If no user is logged in, it tries to validate and login a user based on credentials in the current HTTP request. It does not automatically send a response to the browser to perform an HTTP Authentication.
    - **Method:**  HttpUserSessionManager.sendUnauthorizedResponse(); - sends an Unauthorized response (HTTP 401) to the browser, which initiates a HTTP Authentication process to obtain login credentials from the next HTTP Request.
  + **Sample code:**  APISecurity\LoginLogout\loginIndex.jsp - entry point page for a group of JSP pages that exercise these two versions of checkLogin() to demonstrate how they work. Read the comments in the JSP files.
  + **Network security:**  Using the checkLogin() system for controlling access to the web pages is not an airtight security protocol because login credentials in the HTTP Request are in an insecure stream. If this system is used for production outside a firewall, the network should be secure with URLs to the web pages using *https (SSL)*  instead of *http*. Secure Socket Layer (SSL) can easily be configured using the Logi JReport Administration console.
* **Single Sign-On** - Access control to the Logi JReport web pages is based on logging in to the Logi JReport web session with a user name and password. In the standard setup, Logi JReport Server will cause a popup login dialog on the first attempt to run a Logi JReport web page in a session. This should not happen when a logged-in application user does their first attempt to run a Logi JReport web page. Logi JReport Server provides a framework to allow Single Sign-On,, to avoid this experience. When Single Sign-On is turned on, Logi JReport will just ask the application for the current user name and not challenge the user.
  + **Interface:** [jet.server.api.http.HttpExternalAuthorized](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/http/HttpExternalAuthorized.html). This Java interface defines a class that application developers can write and deploy within Logi JReport Server that co-operates with the checkLogin() methods that control access to web pages.

    This Java interface defines a protocol for the application to tell Logi JReport Server that a user is already logged into the application's web session so that checkLogin() will log in that user to Logi JReport Server. It also has a protocol for asking the application to handle the case where no user is logged in, so that the application can direct the user to the application's login workflow. This allows the application to provide the single place where a user logs into the web application. This also prevents checkLogin() from using the HTTP Authentication process.

    Single Sign-On is turned on when the implementation of this Java interface is compiled and deployed as a jar, and Logi JReport Server is configured to use it.

    - **Method:**  HttpExternalAuthorized.getExternalAuthorizedUser(); - return the Logi JReport User ID (user name) for the user who is currently logged into the web session.
    - **Method:**  HttpExternalAuthorized.handleUnauthorizedRequest(); - build a response to send to the browser redirecting the user to the application login page, and return a true to tell Logi JReport Server to use that response, instead of the HTTP 401 Unauthorized response.
  + **Sample code:**  APISecurity\SingleSignOn\CustomHttpExternalAuthorized.java - example implementation of the interface. Read comments in the source for detailed explanations on the application security model it uses.

    This implementation is perfect for deploying using the command line method of registering it with Logi JReport Server, or when using a servlet to register it with Logi JReport Server by making an API call. Because of limitations in the JSP parser, it is not usable as the class to use when registering it with Logi JReport Server using a JSP page to make the API call.
  + **Sample code:**  APISecurity\SingleSignOn\com\example\MyExternalAuthorized.java - example implementation of the interface. Read comments in the source for detailed explanations on the application security model it uses.

    This implementation is written as a package with a multi-tier package name. This can be registered with Logi JReport Server as the implementation in all possible cases, include from code in a JSP page that calls an API.
  + **Turning on Single Sign-On** - Logi JReport Server will use Single Sign-On when the implementation class of the java interface is registered with it.
    - **Register in command line**  
       Set a system property in the command line that starts up your application or Logi JReport Server. The property *jrs.httpExternalAuthorized* should be set to the name of the implementation class. For example, use *-Djrs.httpExternalAuthorized=CustomHttpExternalAuthorized* when starting the Java JVM for the application containing the JSP pages that call checkLogin().
    - **Register with Java API call**
      * **Class:** [jet.server.api.http.HttpUserSessionManager](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/http/HttpUserSessionManager.html) - This class provides methods that manage the UserSession associated with a logged in user.
        + **Method:**  HttpUserSessionManager.setHttpExternalAuthorized(); - turn on Single Sign-On by setting the class instance object to use for HttpExternalAuthorized. When a null value is used as the class instance to set, this turns off Single Sign-On.
      * **Sample code:**  APISecurity\SingleSignOn\CustomServlet.java - example of a servlet that sets the ExternalAuthorized using the Java API call.
    - **Where to turn on Single Sign-On**  
       The Single Sign-On should be turned on for the JVM where the JSP pages are running. If the application and Logi JReport JSP pages are running on a web server with Logi JReport Server installed on a dedicated back end server, the Single Sign-On should be turned on in the web server machine. Single Sign-On access control to the web pages will be handled properly for the HTTP requests for the web pages, while access to the back end Logi JReport Server will be over RMI, which does not use the checkLogin() or Single Sign-On for access control.
  + **Sample code:**  APISecurity\SingleSignOn\customIndex.jsp - entry point JSP page to a group of JSP pages that demonstrate how Single Sign-On works. Read comments in the JSP page to learn more about the demonstration.
* **Authentication -**  This Java interface defines a class that application developers can write that replaces the built-in user validation system of Logi JReport. Even when using Single Sign-On, the system will check that the user is valid in Logi JReport so it can determine if the credentials identify a registered user. This Java interface is called to check if the user is valid. A custom implementation can use local DBMS data or the application's data to validate the user. Another option rather than to authenticate with Logi JReport's built-in system is to authenticate directly to an LDAP or Active Directory service.
  + **Interface:** [jet.server.api.custom.security.AuthenticationProvider](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/custom/security/AuthenticationProvider.html)
    - **Method:** isValidUser();
  + **Sample code:**  APISecurity\DemoAuthenticationProvider.java
* **Authorization** - This built-in package provides methods for determining authorization rights to resources based on the user's user id, group and role that have been defined using Logi JReport Server's admin web interface for managing users, groups, and roles. Permissions to resources can be placed on any of the 3 levels, user, group or role but role is the preferred method as it is standard for Java applications and provides you with more flexibility as individual users change jobs while roles are stable for long periods of time.
  + **Class:** [jet.server.api.Authenticator](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/Authenticator.html)
    - **Method:** isValidUser();
    - **Method:** isPermissionOK();
    - **Method:** isValidAdminUser();
  + **Sample code:**  none
* **Custom Authorization** - This Java interface defines a class that application developers can implement to replace the built-in Authorization (Authenticator) class. After a user has been validated as a registered Logi JReport User, there is still the question if the user can do the operation requested against the target resource. Methods in this Java interface will be called to determine if the user has permission to do a given action against a given report resource. You can implement your own method for making this decision.
  + **Interface:** [jet.server.api.custom.security.AuthorizationProvider](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/custom/security/AuthorizationProvider.html).
    - **Method:** isPermissionOk();
  + **Sample code:**  - APISecurity\DemoAuthorizationProvider.java
* **Add/Modify/Delete Roles/Groups/Users** - This built-in package allows an application to build a system to synchronize their internal system for managing user identity with Logi JReport Server's DBMS of user identity. By default users are added to Logi JReport Server manually using the Logi JReport Administration interface or by synchronizing with an LDAP service. This package provides a third way, allowing you to add the users, groups and roles into Logi JReport Server by making API calls so that you can utilize Logi JReport Server's built-in authorization, including permissions to resources and row level and column level security. Since users, groups and roles are in the Logi JReport Server DBMS developers are sometimes tempted to directly update the DBMS tables but this is highly discouraged. Since a running Logi JReport Server caches the security information, any updates not using the API will be ignored until the server is restarted.
  + **Class:** [jet.server.api.admin.SecurityAdminService](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/admin/SecurityAdminService.html)
    - **Method:** addRole();
    - **Method:** addGroup();
    - **Method:** addUser();
  + **Sample code:**  APISecurity\AddPrincipal\SecurityGroupCover.java, SecurityRoleCover.java, SecurityUserCover.java

### Event Framework - Task Listener

Logi JReport Server uses an event framework model that allows the application to provide methods that are called at various points in the processing of requests in Logi JReport Server. These include calls to methods before a report is run, after the parameters are entered by the user to validate the parameters or generate new derived parameters, and after a report is run to log information. By using these methods you can keep detailed logs of information about the report in addition to the logging information that Logi JReport provides.

This Java interface defines a class that applications developers can implement and deploy to provide actions tied to processing events happening.

* **Interface:**[jet.server.api.TaskListener](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/TaskListener.html)
  + **Method:** beforeRun
  + **Method:** afterRun
  + **Method:** validateParameter
* **Sample code:** APITaskListener\TestTaskListener.java

### Engine API

Logi JReport Engine allows you to run reports directly in your application without connecting to a Logi JReport Server instance. As long as you don't need the Logi JReport Server features such as Page Report Studio, security and scheduling then this is an efficient way to embed reporting into your application.

* **Class:** [jet.server.api.engine.ReportEngine](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/engine/ReportEngine.html)
  + **Method:** ReportEngineFactory.getInstance - Creates a report server bean
  + **Method:** setReportHome - There are a number of required set methods to set reporthome, catalog, report name, and so on.
  + **Method:** exportToPDF - There are a number of export methods available for each type of export
  + **Method:** runReport - Runs the report and produces a Logi JReport rst file that can be used to export to a user viewable report
* **Sample code:**  APIServer\APIDemoReportEngine.java

### NLS

This Java interface defines an implementation you can build to provide your own methods to do data mapping and text replacement. The implementation that is provided by Logi JReport Server works out of the box, but can be changed easily.

* **Interface:** jet.util.NLSBundleInfo
  + NLSBundleInfo
* **Sample code:** APINLS\MyNLSBundleInfo.java

### Resource Management

The ResourceManager class provides methods to control all aspects of deploying resources to the server and managing resources that are already deployed. Resources include folders, catalogs, reports, and library components.

It does not include publishing results to the version system which are handled by *jet.server.api.RptServer*.

When resources are deployed, the application can set the permissions at the same time. Folder permissions are automatically applied to all contents deployed into the folder unless explicitly overridden.

* **Class:** [jet.server.api.ResourceManage](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/ResourceManager.html)
  + **Intention:** Publish
    - **Method:** createFolder();
    - **Method:** addResource();
    - **Method:** addResourcesToFolder();
  + **Intention:** Security
    - **Method:** getAuthenticator().checkPrivilege();
    - **Method:** checkPermission();
  + **Intention:** Delete
    - **Method:** removeNode();
    - **Method:** removeVersion();
  + **Intention:** List
    - **Method:** getReportsInPath();
    - **Method:** getResultsInPath();
* **Sample code:**  APIServer\APIDemoDeployReport.java

### Trigger Manager API

The TriggerManager class allows the application code to fire a trigger that will start running all of the scheduled tasks waiting on the trigger.

* **Class:** [jet.server.api.TriggerManager](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/trigger/TriggerManager.html) 
  + **Method:** subScheduledTask();
  + **Method:** fire();
* **Sample code:**  APIServer\DemoTrigger.java

### Run Report - RptServer API

This RptServer class is at the core of Logi JReport Server. Although it is documented as a Java interface, it is not intended to be replaced by a custom implementation built by developers. This section will talk about it as a Java class. The class provides methods to start and stop Logi JReport Server, to get information about deployed resources and to run and schedule reports. Report results can also be saved as resources using these methods.

See the section above about initialization and connecting to the Report Server to see that an instance of this class, or the subclass HttpRptServer, is needed by an application program before any other API methods may be called.

* **Class:** [jet.server.api.RptServer](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/RptServer.html)
  + **Method:** runReport() - run on-demand report
  + **Method:** exportResult() - export to one or more export types such as PDF, HTML, and so on.
* **Sample code:** APIServer\APIDemoRunAndExportReport.java

### E-mail

This class is used by programs that want to interface to an SMTP server to export results to e-mail as attachments or as embedded reports in the e-mail body.

* **Sample code:**  APIServer\APIDemoSendEMail.java

### Remote File Service

This class is used by client programs that run a report on a remote Logi JReport Server but then want the generated exported result such as PDF or Excel file to be available to open locally on the client computer.

* **Class:** [jet.server.api.RemoteReportServerToolkit](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/RemoteFileService.html)
  + **Method:** getRemoteFileService()
  + **Method:** copyFromRemote()
* **Sample code:**  APIRemoteServer\RemoteAPIDemoFIleService.java

### Remote Method Invocation - RMI

This class is used by programs that need to request reports to run on a remote server and to copy the results to the local system. The report can be run asynchronously when using the timeout option. Programs written to access RptServer or RemoteRptServer are identical except for initialization so it is easy to write an application that tries to connect remotely before starting a local RptServer.

* **Class:** [jet.server.api.rmi.RemoteReportServerToolkit](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/rmi/RemoteReportServerToolkit.html)
  + **Method:** getRemoteRptServer();
  + **Method:** runTask();
  + **Method:** getResourceManager();
  + **Method:** getRemoteFileService();
* **Sample code:**  APIRemoteServer\RemoteAPIDemoPublishRpt.java, RemoteAPIDemoRunAndExportReport.java, RemoteAPIDemoRunReportWithTimeout.java

### Schedule Report Using RptServer

This class allows programs to add, modify and delete schedules based on time or triggers.

* **Class:** [jet.server.api.RptServer](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/RptServer.html)
  + submitScheduledTask(); - run scheduled report task
* **Sample code:** APIServer\APIDemoPublishReport.java and APIRemoteServer\RemoteAPIDemoPublishRpt.java

### Remote Cluster Dispatcher

The RemoteDispatcher class allows the user's remote application to determine the load balance algorithm, and remotely dispatch reports to be run on specified servers.

* **Class:** [jet.server.api.rmi.RemoteDispatcher](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/rmi/RemoteDispatcher.html)
  + RemoteDispatcher();
* **Sample code:**  APICluster\DemoRemoteDispatcher.java

### Clustering

The Cluster class provides methods to allow the user to build their own algorithm for balancing server loads by assigning new reports to run onto the desired server.

* **Class:** [jet.server.api.cluster.LoadBalancer](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/cluster/LoadBalancer.html)
  + **Method:** LoadBalancer();
  + **Method:** selectMember();
* **Sample code:**  APICluster\DemoLoadBalancer.java

### Server Configuration

This class allows applications to configure the server similar to the Logi JReport Administration console. For programming examples use the actual JSP pages under `public_html\admin`.

- [jet.server.api.admin.cfg](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/admin/cfg/package-tree.html)

### Server Monitor

Logi JReport Server Monitor is a client application that can be downloaded for free from the Logi JReport downloads page. It allows you to monitor activity on a single server or on an entire group of servers in a cluster. The API can be used to start and stop servers as well as configure properties on them remotely.

- [jet.server.api.monitor](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/monitor/MonitorService.html)

### Server Profiling

This is the class used by Logi JReport Server to implement Server Monitor. It allows your application to catch the same types of resource use as Server Monitor using JMX technology.

- [jet.server.api.profiling](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/profiling/ProfilingService.html)

### Server Cached Reusable Data (CRD)

This class is similar to scheduling of reports. The application can schedule just the cached result data and have it available for any number of reports to use it. Often it is for datasets that many reports might need such as month end sales reports.

- [jet.server.api.crd](http://www.jinfonet.com/kbase/jreport15/api/jet/server/api/crd/CRDManager.html)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668361-Technical-Architecture)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644182-Java-API-for-a-Servlet)
