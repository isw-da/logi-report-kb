---
title: "Tour of the Java API"
id: 1500009718382
section: "Work With APIs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718382-Tour-of-the-Java-API
updated_at: 2021-07-25T07:20:25Z
---

# Tour of the Java API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744201-Technical-Architecture)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718622-Java-API-for-a-Servlet)

# Tour of the Java API

This tour is a high-level survey of the Logi Report Server Java API. The intent is to show boundaries of interest so that a developer can narrow down the set of APIs to look at when needing to use Logi Report Server for a particular task.

The Logi Report Server Java API classes provide thousands of methods, each having a Javadoc entry describing the method and parameters. This topic categorizes the Java API classes by functionality, making it easier to find specific methods to use for particular situations. Each functional area will show the class or interface name and have a general description. Below that are a list of common methods and other information.

To access the complete Java API documentation, go to `<install_root>\help\api`; to get the referenced sample code, go to `<install_root>\help\samples`.

Select the following links to view the topics:

* [Initializing and Connecting to Server](#Initialize)
* [Security](#Security)
* [Event Framework - Task Listener](#TaskListener)
* [Engine API](#Engine)
* [NLS](#NLS)
* [Resource Management](#Resource)
* [Trigger Manager API](#Trigger)
* [Run Report - RptServer API](#RptServer)
* [E-mail](#Mail)
* [Remote File Service](#RemoteFileService)
* [Remote Method Invocation - RMI](#RMI)
* [Schedule Report Using RptServer](#Schedule)
* [Remote Cluster Dispatcher](#RemoteClusterDispatcher)
* [Cluster](#Cluster)
* [Server Configuration](#ServerConfiguration)
* [Server Monitor](#Monitor)
* [Server Profiling](#Profiling)
* [Server Cached Report Data (CRD)](#CRD)

## Initializing and Connecting to Logi Report Server

Every program that uses Logi Report Server Java API must start with calls to ensure an instance of the server is running, and then obtain a handle to the server for use in later API calls.

* **Class:** jet.server.api.http.HttpUtil - This class provides a variety of utilities for programs running within a Java Servlet container.

Additionally, the two most commonly used methods of the Java API are in this class. These two methods must be called by any program that wants to use Logi Report Server in order to initialize and connect to Logi Report Server. These will still be used by programs that run outside a servlet container.

* **Method:**  HttpUtil.initEnv() - Initializes and starts the singleton Logi Report Server running on the machine which all programs will access.
* **Method:**  HttpUtil.getHttpRptServer() - Connects to the running Logi Report Server and return a handle to the server to use in future API calls.

## Security

Every web application must manage access control, identity of a visitor, permissions for a visitor, and maintain this across multiple HTTP Requests that define the web session for the user.

Logi Report Server provides built-in methods for doing this based on a protocol using HTTP Authentication and query parameters to pass in log-in credentials. The security mechanism includes a framework system that allows application developers to write code to co-operate with Logi Report Server's built-in system so that existing applications can provide the security functionality.

* **Control access to web pages**
  + **Class:** jet.server.api.http.HttpUtil - This class provides a variety of utilities for programs running within a Java Servlet container.
    - **Method:**  HttpUtil.checkLogin() - This method only returns when a validated Logi Report User is logged into the web session. If a user is already logged in, it returns true. If not, it tries to validate and login a user based on credentials in the current HTTP request. If no logged-in user can be identified, it will send a response to the browser to perform an HTTP Authentication to obtain credentials, using the browser login dialog box form. The credentials are sent back to the same JSP page in the next HTTP Request.
  + **Class:** jet.server.api.http.HttpUserSessionManager - This class provides methods that help to create and manage the UserSession associated with a logged in user.
    - **Method:**  HttpUserSessionManager.checkLogin() - Indicates if a validated Logi Report User is logged into the web session. If no user is logged in, it tries to validate and login a user based on credentials in the current HTTP request. It does not automatically send a response to the browser to perform an HTTP Authentication.
    - **Method:**  HttpUserSessionManager.sendUnauthorizedResponse() - Sends an Unauthorized response (HTTP 401) to the browser, which initiates a HTTP Authentication process to obtain login credentials from the next HTTP Request.
  + **Sample code:**  APISecurity\LoginLogout\loginIndex.jsp - Entry point page for a group of JSP pages that exercise these two versions of checkLogin() to demonstrate how they work. Read the comments in the JSP files.
  + **Network security:**  Using the *checkLogin()* system for controlling access to the web pages is not an airtight security protocol because login credentials in the HTTP Request are in an insecure stream. If this system is used for production outside a firewall, the network should be secure with URLs to the web pages using *https* (SSL) instead of *http*. Secure Socket Layer (SSL) can be easily configured in the Logi Report Server console.
* **Single Sign On** - Access control to the Logi Report web pages is based on logging in to the Logi Report web session with a user name and password. In the standard setup, Logi Report Server will cause a popup login dialog box on the first attempt to run a Logi Report web page in a session. This should not happen when a logged-in application user does their first attempt to run a Logi Report web page. Logi Report Server provides a framework to allow Single Sign On, to avoid this experience. When Single Sign On is turned on, Logi Report will just ask the application for the current user name and not challenge the user.
  + **Interface:** jet.server.api.http.HttpExternalAuthorized. This Java interface defines a class that application developers can write and deploy within Logi Report Server that co-operates with the checkLogin() methods that control access to web pages.

    This Java interface defines a protocol for the application to tell Logi Report Server that a user is already logged into the application's web session so that checkLogin() will log in that user to Logi Report Server. It also has a protocol for asking the application to handle the case where no user is logged in, so that the application can direct the user to the application's login workflow. This allows the application to provide the single place where a user logs into the web application. This also prevents checkLogin() from using the HTTP Authentication process.

    Single Sign On is turned on when the implementation of this Java interface is compiled and deployed as a jar, and Logi Report Server is configured to use it.

    - **Method:**  HttpExternalAuthorized.getExternalAuthorizedUser() - Returns the Logi Report User ID (user name) for the user who is currently logged into the web session.
    - **Method:**  HttpExternalAuthorized.handleUnauthorizedRequest() - Builds a response to send to the browser redirecting the user to the application login page, and returns a true to tell Logi Report Server to use that response, instead of the HTTP 401 Unauthorized response.
  + **Sample code:**  APISecurity\SingleSignOn\CustomHttpExternalAuthorized.java - Example implementation of the interface. Read comments in the source for detailed explanations on the application security model it uses.

    This implementation is perfect for deploying using the command line method of registering it with Logi Report Server, or when using a servlet to register it with Logi Report Server by making an API call. Because of limitations in the JSP parser, it is not usable as the class to use when registering it with Logi Report Server using a JSP page to make the API call.
  + **Sample code:**  APISecurity\SingleSignOn\com\example\MyExternalAuthorized.java - Example implementation of the interface. Read comments in the source for detailed explanations on the application security model it uses.

    This implementation is written as a package with a multi-tier package name. This can be registered with Logi Report Server as the implementation in all possible cases, include from code in a JSP page that calls an API.
  + **Turning on Single Sign On** - Logi Report Server will use Single Sign On when the implementation class of the java interface is registered with it.
    - **Register in command line**  
       Set a system property in the command line that starts up your application or Logi Report Server. The property jrs.httpExternalAuthorized should be set to the name of the implementation class. For example, use `-Djrs.httpExternalAuthorized=CustomHttpExternalAuthorized` when starting the Java JVM for the application containing the JSP pages that call checkLogin().
    - **Register with Java API call**
      * **Class:** jet.server.api.http.HttpUserSessionManager - This class provides methods that manage the UserSession associated with a logged in user.
        + **Method:**  HttpUserSessionManager.setHttpExternalAuthorized() - Turns on Single Sign On by setting the class instance object to use for HttpExternalAuthorized. When a null value is used as the class instance to set, this turns off Single Sign On.
      * **Sample code:**  APISecurity\SingleSignOn\CustomServlet.java - Example of a servlet that sets the ExternalAuthorized using the Java API call.
    - **Where to turn on Single Sign On**  
       The Single Sign On should be turned on for the JVM where the JSP pages are running. If the application and Logi Report JSP pages are running on a web server with Logi Report Server installed on a dedicated back end server, the Single Sign On should be turned on in the web server machine. Single Sign On access control to the web pages will be handled properly for the HTTP requests for the web pages, while access to the back end Logi Report Server will be over RMI, which does not use the checkLogin() or Single Sign On for access control.
  + **Sample code:**  APISecurity\SingleSignOn\customIndex.jsp - Entry point JSP page to a group of JSP pages that demonstrate how Single Sign On works. Read comments in the JSP page to learn more about the demonstration.
* **Authentication -**  This Java interface defines a class that application developers can write that replaces the built-in user validation system of Logi Report. Even when using Single Sign On, the system will check that the user is valid in Logi Report so it can determine if the credentials identify a registered user. This Java interface is called to check if the user is valid. A custom implementation can use local DBMS data or the application's data to validate the user. Another option rather than to authenticate with Logi Report's built-in system is to authenticate directly to an LDAP or Active Directory service.
  + **Interface:** jet.server.api.custom.security.AuthenticationProvider
    - **Method:** isValidUser()
  + **Sample code:**  APISecurity\DemoAuthenticationProvider.java
* **Authorization** - This built-in package provides methods for determining authorization rights to resources based on the user's user id, group and role that have been defined by the administrator. Permissions to resources can be placed on any of the 3 levels, user, group, or role, but role is the preferred method as it is standard for Java applications and provides you with more flexibility as individual users change jobs while roles are stable for long periods of time.
  + **Class:** jet.server.api.Authenticator
    - **Method:** isValidUser()
    - **Method:** isPermissionOK()
    - **Method:** isValidAdminUser()
* **Custom Authorization** - This Java interface defines a class that application developers can implement to replace the built-in Authorization (Authenticator) class. After a user has been validated as a registered Logi Report User, there is still the question if the user can do the operation requested against the target resource. Methods in this Java interface will be called to determine if the user has permission to do a given action against a given report resource. You can implement your own method for making this decision.
  + **Interface:** jet.server.api.custom.security.AuthorizationProvider
    - **Method:** isPermissionOk()
  + **Sample code:**  - APISecurity\DemoAuthorizationProvider.java
* **Add/Modify/Delete Roles/Groups/Users** - This built-in package allows an application to build a system to synchronize their internal system for managing user identity with Logi Report Server's DBMS of user identity. By default, users are added to Logi Report Server manually using the server console or by synchronizing with an LDAP service. This package provides a third way, allowing you to add the users, groups and roles into Logi Report Server by making API calls so that you can utilize Logi Report Server's built-in authorization, including permissions to resources and row level and column level security. Since users, groups and roles are in the Logi Report Server DBMS developers are sometimes tempted to directly update the DBMS tables but this is highly discouraged. Since a running Logi Report Server caches the security information, any updates not using the API will be ignored until the server is restarted.
  + **Class:** jet.server.api.admin.SecurityAdminService
    - **Method:** addRole()
    - **Method:** addGroup()
    - **Method:** addUser()
  + **Sample code:**  APISecurity\AddPrincipal\SecurityGroupCover.java, SecurityRoleCover.java, SecurityUserCover.java

## Event Framework - Task Listener

Logi Report Server uses an event framework model that allows the application to provide methods that are called at various points in the processing of requests in Logi Report Server. These include calls to methods before a report is run, after the parameters are entered by the user to validate the parameters or generate new derived parameters, and after a report is run to log information. Using these methods, you can keep detailed logs of information about the report in addition to the logging information that Logi Report provides.

This Java interface defines a class that applications developers can implement and deploy to provide actions tied to processing events happening.

* **Interface:**jet.server.api.TaskListener
  + **Method:** beforeRun
  + **Method:** afterRun
  + **Method:** validateParameter
* **Sample code:** APITaskListener\TestTaskListener.java

## Engine API

Logi Report Engine allows you to run reports directly in your application without connecting to a Logi Report Server instance. As long as you do not need the Logi Report Server features such as Page Report Studio, security and scheduling then this is an efficient way to embed reporting into your application.

* **Class:** jet.server.api.engine.ReportEngine
  + **Method:** ReportEngineFactory.getInstance - Creates a report server bean
  + **Method:** setReportHome - There are a number of required set methods to set reporthome, catalog, report name, and so on.
  + **Method:** exportToPDF - There are a number of export methods available for each type of export
  + **Method:** runReport - Runs the report and produces a Logi Report rst file that can be used to export to a user viewable report
* **Sample code:** APIServer\APIDemoReportEngine.java

## NLS

This Java interface defines an implementation you can build to provide your own methods to do data mapping and text replacement. The implementation that is provided by Logi Report Server works out of the box, but can be changed easily.

* **Interface:** jet.util.NLSBundleInfo
  + NLSBundleInfo
* **Sample code:** APINLS\MyNLSBundleInfo.java

## Resource Management

The ResourceManager class provides methods to control all aspects of deploying resources to the server and managing resources that are already deployed. Resources include folders, catalogs, reports, and library components.

It does not include publishing results to the version system which are handled by **jet.server.api.RptServer**.

When resources are deployed, the application can set the permissions at the same time. Folder permissions are automatically applied to all contents deployed into the folder unless explicitly overridden.

* **Class:** jet.server.api.ResourceManage
  + **Intention:** Publish
    - **Method:** createFolder()
    - **Method:** addResource()
    - **Method:** addResourcesToFolder()
  + **Intention:** Security
    - **Method:** getAuthenticator().checkPrivilege()
    - **Method:** checkPermission()
  + **Intention:** Delete
    - **Method:** removeNode()
    - **Method:** removeVersion()
  + **Intention:** List
    - **Method:** getReportsInPath()
    - **Method:** getResultsInPath()
* **Sample code:** APIServer\APIDemoDeployReport.java

## Trigger Manager API

The TriggerManager class allows the application code to fire a trigger that will start running the scheduled tasks waiting on the trigger.

* **Class:** jet.server.api.TriggerManager
  + **Method:** subScheduledTask()
  + **Method:** fire()
* **Sample code:**  APIServer\DemoTrigger.java

## Run Report - RptServer API

This RptServer class is at the core of Logi Report Server. Although it is documented as a Java interface, it is not intended to be replaced by a custom implementation built by developers. This section will talk about it as a Java class. The class provides methods to start and stop Logi Report Server, to get information about deployed resources and to run and schedule reports. Report results can also be saved as resources using these methods.

See the section above about initialization and connecting to the Report Server to see that an instance of this class, or the subclass HttpRptServer, is needed by an application program before any other API methods may be called.

* **Class:** jet.server.api.RptServer
  + **Method:** runReport() - Runs on-demand report
  + **Method:** exportResult() - Exports to one or more export types such as PDF, HTML, and so on.
* **Sample code:** APIServer\APIDemoRunAndExportReport.java

## E-mail

This class is used by programs that want to interface to an SMTP server to export results to e-mail as attachments or as embedded reports in the e-mail body.

* **Sample code:**  APIServer\APIDemoSendEMail.java

## Remote File Service

This class is used by client programs that run a report on a remote Logi Report Server but then want the generated exported result such as PDF or Excel file to be available to open locally on the client computer.

* **Class:** jet.server.api.RemoteReportServerToolkit
  + **Method:** getRemoteFileService()
  + **Method:** copyFromRemote()
* **Sample code:**  APIRemoteServer\RemoteAPIDemoFIleService.java

## Remote Method Invocation - RMI

This class is used by programs that need to request reports to run on a remote server and to copy the results to the local system. The report can be run asynchronously when using the timeout option. Programs written to access RptServer or RemoteRptServer are identical except for initialization so it is easy to write an application that tries to connect remotely before starting a local RptServer.

* **Class:** jet.server.api.rmi.RemoteReportServerToolkit
  + **Method:** getRemoteRptServer()
  + **Method:** runTask()
  + **Method:** getResourceManager()
  + **Method:** getRemoteFileService()
* **Sample code:**  APIRemoteServer\RemoteAPIDemoPublishRpt.java, RemoteAPIDemoRunAndExportReport.java, RemoteAPIDemoRunReportWithTimeout.java

## Schedule Report Using RptServer

This class allows programs to add, modify and delete schedules based on time or triggers.

* **Class:** jet.server.api.RptServer
  + submitScheduledTask() - Runs scheduled report task
* **Sample code:** APIServer\APIDemoPublishReport.java and APIRemoteServer\RemoteAPIDemoPublishRpt.java

## Remote Cluster Dispatcher

The RemoteDispatcher class allows the user's remote application to determine the load balance algorithm, and remotely dispatch reports to be run on specified servers.

* **Class:** jet.server.api.rmi.RemoteDispatcher
  + RemoteDispatcher()
* **Sample code:**  APICluster\DemoRemoteDispatcher.java

## Cluster

The Cluster class provides methods to allow the user to build their own algorithm for balancing server loads by assigning new reports to run onto the desired server.

* **Class:** jet.server.api.cluster.LoadBalancer
  + **Method:** LoadBalancer()
  + **Method:** selectMember()
* **Sample code:**  APICluster\DemoLoadBalancer.java

## Server Configuration

This allows applications to configure the server similar to the Logi Report Server console. For programming examples use the actual JSP pages under `public_html\admin`.

See the package **jet.server.api.admin.cfg**.

## Server Monitor

Logi Report Server Monitor is a client application that can be downloaded for free from the Logi Report downloads page. It allows you to monitor activity on a single server or on an entire group of servers in a cluster. The API can be used to start and stop servers as well as configure properties on them remotely.

See the package **jet.server.api.monitor**.

## Server Profiling

This is used by Logi Report Server to implement Server Monitor. It allows your application to catch the same types of resource use as Server Monitor using JMX technology.

See the package **jet.server.api.profiling**.

## Server Cached Report Data (CRD)

This is similar to scheduling of reports. The application can schedule just the cached result data and have it available for any number of reports to use it. Often it is for datasets that many reports might need such as month end sales reports.

See the package **jet.server.api.crd**.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744201-Technical-Architecture)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718622-Java-API-for-a-Servlet)
