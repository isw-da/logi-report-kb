---
title: "Java API for a Servlet"
id: 1500009644182
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644182-Java-API-for-a-Servlet
updated_at: 2021-07-24T20:55:25Z
---

# Java API for a Servlet

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668401-Tour-of-the-Java-API)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668201-Java-API-for-an-Application)

# Java API for a Servlet

The most common way to use Logi JReport Server when extending a web application is to write code for a JSP file. This turns into a compiled servlet that runs when it is requested by an HTTP request. The context at runtime is within a Java Servlet container which provides the HTTP Request/Response and Session objects.

The Logi JReport Server Java API provides a set of classes and methods for requesting reporting services, as well as a few utilities to handle data processing duties. Examples below will show
the standard patterns for making method calls to handle common tasks.

Below is a list of the sections covered in this topic:

* [HTTP Request for Service](#Service)
* [Connecting to the Report Server](#Connect)
* [Authentication](#Authentication)
* [Authorization](#Authorization)
* [User Session](#Session)
* [Running a Report](#Run)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## HTTP Request for Service

Native Java Servlet technology provide the basic operations needed for servlets. Processing the requesting URL and forming a response are typical activities. Occasionally, doing a redirect is needed. These can be done with native Java Servlet methods. Logi JReport Engine provides other helpful methods to use in the context of a servlet container handling HTTP protocol while preparing to use other Logi JReport Engine methods.

These helper methods are packaged in the HttpUtil class.

**HttpUtil.getParameters(request);  
HttpUtil.getUser(request);**

|  |
| --- |
| ```        // Use native Java Servlet method to get specific parameter values        // that are needed later to run the report     String cat = request.getParameter(APIConst.TAG_CATALOG);     String rptName = request.getParameter(APIConst.TAG_REPORT);        // Use Logi JReport API method to extract parameters from URL,        // and load them into a data structure of the needed type         // for use in a later call to runReport().        // getParameters() transforms multi-valued parameter values        // from a vector of strings into a single string holding delimiter separated values.     Properties ht = HttpUtil.getParameters(request);        // Use Logi JReport API method to identify current user.        // This code snippet assumes that the existence of a current user was checked earlier.        // The method returns an empty string when the session does not have a current user known to Logi JReport.     String user = HttpUtil.getUser(request)        // use the gathered information to run the report.     HttpRptServer httpRptServer = HttpUtil.getHttpRptServer()     String rst = httpRptServer.runReport(user, cat, rptName, ht); ``` |

**HttpUtil.decodeEsc(string);**

|  |
| --- |
| ```     // Decode the URL-encode string.  Replace "%HexHex" with its character.     String rescPath = HttpUtil.decodeEsc(request.getParameter(APIConst.TAG_PATH)); ``` |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Connecting to the Report Server

All java processes that want to use the Logi JReport Engine to process reports must connect to the Logi JReport Server and obtain a RptServer object that enables calls to the server. An instance of this object has methods to get attribute values of the server, submit scheduled tasks and remove them, run a report, and perform other report operations.

A specialized version of the RptServer is available within the Servlet Container. This is the HttpRptServer object.

The HttpRptServer object knows about the HTTP Request, the HTTP Response, and the Servlet Session, as well as the Logi JReport Server. The Servlet Session is used by the Logi JReport Engine to hold Logi JReport state information between HTTP requests. This information can be accessed when using the HttpRptServer object.

### Code Running in the Same JVM as the Report Server

When a web application is deployed to same web server as Logi JReport Server, the application's JSP pages and servlets run in the Java Virtual Machine (JVM) with Logi JReport Server's JSP pages, servlets, and report server (for more information, see [Logi JReport Server - out of the box](https://devnet.logianalytics.com/hc/en-us/articles/1500009668361-Technical-Architecture#Box)).

All programs in the JVM share a single instance of the report server. Each program that requests a connection will either start up an instance of the server if one is not running,
or will connect with the instance that is running.

###### Not sure if the report server is running

An explicit call to start the server is provided in the HttpUtil class - initEnv(). The typical use case is to call this method to be sure a server instance is running, and then call the get-method that returns the HttpRptServer object.

This example uses the simple getHttpRptServer() method without a parameter. It works fine when the code and report server are in the same JVM. This example is not showing best practice for writing portable code. To write code that works in all configurations, use [getHttpRptServer()](#getHttpRptServer).

**HttpUtil.initEnv();**  
**HttpUtil.getHttpRptServer();**

|  |
| --- |
| ```         // Set specific properties while starting a server, then get a handle to it.         // When the server is already started, this does nothing.     System.getProperties().put("reporthome", "C:\\Logi JReport\\Server");     HttpUtil.initEnv(System.getProperties()):         // httpRptServer will be used for report processing within the servlet.     HttpRptServer httpRptServer = HttpUtil.getHttpRptServer();         // it is good practice to verify the connection was successful     if (httpRptServer == null) {         return;         // replace return with code to handle the failure case.     } ``` |

###### Knowing that the report server is running

When working with a JSP file that always includes another JSP file that that calls initEnv(), the code can either contain another call to initEnv(), which will return without doing any added work, or can leave out that call.

**HttpUtil.getHttpRptServer();**

|  |
| --- |
| ``` <%@ include file="AuthCheck.jsp"%>         // This assumes that code above here already did an initEnv();         // Connect to the httpRptServer instance that was established by that call.     HttpRptServer httpRptServer = HttpUtil.getHttpRptServer();         // it is good practice to verify the connection was successful     if (httpRptServer == null) {         return;         // replace return with code to handle the failure case.     } ``` |

### Code Running in a Different JVM than the Report Server

When Logi JReport Server is configured to have the report server running on a remote system from the web server, the JSP code running on the web server will connect to the backend system using RMI (for more information, see [Logi JReport Server - remote dedicated server](https://devnet.logianalytics.com/hc/en-us/articles/1500009668361-Technical-Architecture#Remote)).

The JSP code that is written does not need to change in any way for this to happen. The same code that works with a report server in the same JVM will also work when the report server is
configured to run in another JVM.

A call to initEnv() will notice the REMOTE\_SERVER\_HOST and REMOTE\_SERVER\_PORT properties that define the remote server and will establish a connection with that server. A subsequent call to getHttpRptServer() will return an httpRptServer object to access the server across an RMI connection. No special code is needed to use the server across the RMI channel.

However, if Logi JReport Server is configured to have a cluster of remote servers, then the method for getting an HttpRptServer object must be different. It should use the one with this signature - getHttpRptServer(request). This is the only special call needed in order to work across the RMI channel to the cluster of report servers.

This method also works correctly for all other configurations. Best practice for portable code is to always use this method.

This next snippet of code shows best practice for portable code that can be copied and pasted and will work for all situations within a servlet. It attempts to initialize the server environment in case it is not running, and it gets the server object using the method that works in all configurations.

**HttpUtil.initEnv();**  
**HttpUtil.getHttpRptServer(request);**

|  |
| --- |
| ```         // Set specific properties while starting a server, then get a handle to it.         // When the server is already started, this does nothing.     System.getProperties().put("reporthome", "C:\\Logi JReport\\Server");     HttpUtil.initEnv(System.getProperties()):         // httpRptServer will be used for report processing within the servlet.     HttpRptServer httpRptServer = HttpUtil.getHttpRptServer(request);         // it is good practice to verify the connection was successful     if (httpRptServer == null) {         return;         // replace return with code to handle the failure case.     } ``` |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Authentication

Logi JReport Server's JSP files and servlets follow a [well defined protocol](https://devnet.logianalytics.com/hc/en-us/articles/1500009650182-Security-for-Accessing-Web-Pages) to enforce that they only run when the HTTP Request comes from a Logi JReport user who can login to the web session.

One part of this protocol is defining a set of URL query parameters to use for passing in the user name and password, as a way to submit credentials without needing to have a login form to enter the information (for more information, see [Authentication Parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009650382-Using-the-Authentication-Properties-)).

Another part of the protocol is to use HTTP Authentication for gathering a user name and password from the browser and passing it to the JSP page using a field in the HTTP Request Header.

You can read the details of the protocol at [Security for Accessing Web Pages](https://devnet.logianalytics.com/hc/en-us/articles/1500009650182-Security-for-Accessing-Web-Pages). Any authentication protocol based on passing credentials in the HTTP Request, as this one does, only gives security when used over a secure network (SSL) with a URL having "https".

The Logi JReport Server authentication scheme also provides a framework so developers can use an existing application's login system with Logi JReport's. This Single Sign-On framework lets the developer provide an authorization scheme to control conditional access to JSP pages based on the user logged in to the session through the application.

Logi JReport Server authentication does more than just control access to functionality. On a successful login, Logi JReport data structures associated with the user are created and stored in the Servlet session object. These data structures support several method calls that are useful to developers. It is good practice to use the Logi JReport Server authentication system so that useful session data is created on login.

### Using Logi JReport JSP Style Authentication

If you want your JSP pages to follow the Logi JReport Server protocol, you can include the same JSP file (AuthCheck.jsp) as is included in the Logi JReport Server JSP pages. AuthCheck.jsp calls the HttpUtil.checkLogin() method to manage the authentication protocol that requires a user to be logged in to the web session before the page can run. HttpUtil.checkLogin does nothing if a user is already logged in. If there is no user logged in to the session, it looks in the request for valid login information in the request header or in the URL query parameters, and if so, it logs in the user. If there is no logged in user at that time, it starts an HTTP Authentication dialog with the browser and does not return from the call.

When HttpUtil.checkLogin() returns, there is always a session established with a Logi JReport user logged in. One side effect of calling HttpUtil.checkLogin() is that on return there is an instance of the report server established that can be obtained by a call to HttpUtil.getHttpRptServer() without needing to call HttpUtil.initEnv().

There is more information about checkLogin() below.

**include AuthCheck.jsp;**

|  |
| --- |
| ``` <%@ page import="java.io.*, java.util.*,jet.cs.util.*" %>  <%@ page import="jet.server.api.http.*" %>  <%@ page import="jet.server.api.*" %> <%@ page errorPage="errorpage.jsp" %> <%@ include file="AuthCheck.jsp" %>         // Any code below here will execute if and only if an authenticated Logi JReport user is logged in         // The code can get an instance of HttpRptServer without calling initEnv().     HttpRptServer httpRptServer = HttpUtil.getHttpRptServer(request); .... ``` |

### Using Logi JReport URL Query Parameter Authentication

Alternatively, you can follow the Logi JReport JSP technique allowing login credentials to be passed in as URL query parameters, while maintaining control when a valid user is not identified.

HttpUserSessionManager.checkLogin() will check if a user is already logged in. If not, it will look for valid login credentials in the Request Header or in the URL query parameters. If such credentials exist, it will login that user and establish a logged in session.

It returns false if there is no logged in session found. It does not initiate an HTTP Authentication dialog with the browser. This allows you to handle the failure case in your own way, such as redirecting to the application's login page.

**HttpUserSessionManager.checkLogin()**

|  |
| --- |
| ```         // Use Logi JReport API method to extract parameters from URL and load them into         // an object of the needed type for use in a later call to checkLogin().         // This is here in case we are using the Logi JReport URL Query protocol for passing         // in user name and password as a way to automatically login.     Properties props = HttpUtil.getParameters(request);         // Make sure a Report Server is running.     System.getProperties().put("reporthome", "C:\\Logi JReport\\Server");     HttpUtil.initEnv(System.getProperties()):         // Get a handle to a running Report Server.       HttpRptServer httpRptServer = HttpUtil.getHttpRptServer(request);         // This checkLogin() returns false if the session does not have a current user,         // and the Header and Properties do not contain values that authenticate a user.         // It returns true if the session has a current user or if the Header or Properties         // identifies a valid user name and password that allows checkLogin() to log that user in. try{      if (!httpRptServer.getHttpUserSessionManager().checkLogin(request,                                 httpRptServer.getResourceManager().getRealm(), props)) {         return;         // Replace this return with code to handle the case of an unauthorized request.         // For example: Redirect to the web applications login page.     } }catch(Throwable t){      // failure to authenticate because of an exception     return; }     // code below here will execute if a Logi JReport user is logged in. ``` |

**Note:** HttpUtil.checkLogin() and HttpUserSessionManager.checkLogin() both do more than shown in these examples. They both provide a framework for extending the authentication protocol based on the Java interface class *ExternalAuthorized* provided by Logi JReport Server.

This gives developers a way to have the application's login system handle the login of a user to the web session and have that identity flow into creating a Logi JReport web session for the user without the user doing another login dialog. This is a Single Sign-On system.

**Tip:** See the sample JSP page loginIndex.jsp in `<install_root>\help\samples\APISecurity\LoginLogout`, which demonstrates how checkLogin() works. This is the entry point page. Read the source for more information.

### Using Application Authentication

Another alternative for handling authentication of JSP pages is to only run the page if someone is already logged in, with no support for passing in credentials by URL query parameters nor engaging in HTTP Authentication to login. The approach would support a model that an existing application page is the single point of login to the application.

The example above could handle this approach, but it does not enforce not using URL query parameters to login. If a user were to pass in credentials by URL query parameters when no one is logged in, they would become logged in. If you want to enforce that this cannot happen, don't pass in the URL query parameters to checkLogin().

**HttpUserSessionManager.checkLogin()**

|  |
| --- |
| ```         // Make sure a Report Server is running.     System.getProperties().put("reporthome", "C:\\Logi JReport\\Server");     HttpUtil.initEnv(System.getProperties()):         // Get a handle to a running Report Server.       HttpRptServer httpRptServer = HttpUtil.getHttpRptServer(request);         // Create a properties that holds no credentials from the URL query parameters.     Properties props = new Properties();  try{      if (!httpRptServer.getHttpUserSessionManager().checkLogin(request,                                 httpRptServer.getResourceManager().getRealm(), props)) {             // User is not logged in.             // Redirect this request to the application's login dialog page             // where the user can enter name and password and submit to the login-action page.             // For this example snippet, let's use "login.jsp" as the page name.             // Production code would redirect to a secure login page having a "https" url.             // A sophisticated system would preserve the user's intent to run this page             // and keep that state across HTTP requests so that after a successful login             // the user could be redirected back to this page.             // One way to maintain the user's intent is to pass the URL for this page              // as a parameter to the login page,             // which would in-turn pass that along to the login-action page.             // Another way would be to put the URL into the servlet session object where the              // login-action page could access it before resetting the session to a new one             // after a successful validation of login credentials.         String loginURL="login.jsp";         response.setStatus(HttpServletResponse.SC_MOVED_TEMPORARILY);         response.setHeader("Location", loginURL);         response.setHeader("Content-Location", loginURL)         return;     } }catch(Throwable t){      // failure to authenticate because of an exception     return; }     // code below here will execute if a Logi JReport user is logged in. ``` |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Authorization

Logi JReport Server does not provide any special system for managing authorization to run a particular JSP page. If a user can login to the web session, the can run a JSP page.

However, Logi JReport Server does provide a system for managing authorization at the level of a command and a target resource. For example, the admin can set permissions for a given user,
allowing the user to run only a certain report, or preventing the user from running any report but allowing the user to view reports. So when a JSP page is called to do certain operations,
the operation may or may not be allowed by the user who is logged in.

This level of authorization can be checked by a JSP page. Specific URL query parameters are used to request certain operations and to indicate the target catalog and report resource.
The JSP code can check permissions that the current user can do the requested command against the requested resource and reject requests that are not allowed.

This authorization is performed by a call to HttpUtil.checkPermission(request). The *request* parameter contains user information and the URL query parameters that define the request.

These are the parameters that are used for determining if the current user is authorized for the request.

* &jrs.cmd=
* &jrs.path=
* &jrs.catalog=
* &jrs.lc=
* &jrs.report=
* &jrs.version\_number=

These parameters give three aspects that define the operation and resource to permission-check.

* command
* path to resource
* version number of resource

The *jrs.cmd* parameter holds the operational command (view, delete and so on). *jrs.path*, *jrs.catalog*, *jrs.lc* and *jrs.report* work together to define the the path to the resource. *jrs.version\_number* gives the version of the resource.

**HttpUtil.checkPermission(request)**

|  |
| --- |
| ```          // Assume this JSP file is called with query parameters           // that request an operation and indicate the report resource.         // Make sure a Report Server is running.     System.getProperties().put("reporthome", "C:\\Logi JReport\\Server");     HttpUtil.initEnv(System.getProperties()):         // Get a handle to a running Report Server.       HttpRptServer httpRptServer = HttpUtil.getHttpRptServer(request);         // Create a properties that holds no credentials from the URL query parameters.         // Don't let the current URL do a login of the user.     Properties props = new Properties();  try{      if (!httpRptServer.getHttpUserSessionManager().checkLogin(request,                                 httpRptServer.getResourceManager().getRealm(), props)) {         String url="login.jsp";         response.setStatus(HttpServletResponse.SC_MOVED_TEMPORARILY);         response.setHeader("Location", url);         response.setHeader("Content-Location", url)         return;     } }catch(Throwable t){      // failure to authenticate because of an exception     return; }     // Code below here will execute if a Logi JReport user is logged in.         // request holds session for this user, to provide user for permission check.         // request holds URL for this page, to provide query parameters.         // Parameters give three aspects that form the operation and resource to permission check.         //  cmd, path to resource, version number of resource         //    jrs.cmd param holds the operation request (run, view, )         //    jrs.try_ve and jrs.try_web are two other operations beyond those that might be in jrs.cmd.         //    jrs.path, jrs.catalog, jrs.lc, jrs.report work together to define the the path to the resource.         //    jrs.version_number gives the version of the resource.     boolean allowed = HttpUtil.checkPermission(request);     if (!allowed) {          // reject the requested operation.          return;     }     // code below here will execute if the current user is authorized to perform the request encoded in the query parameters. .... ``` |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## User Session

The native Java Servlet technology provides a Session object that can hold state across HTTP requests. It is used to hold information about the logged in user and the operation that the multiple HTTP requests are performing in the web application.

Logi JReport Engine places a Logi JReport UserSession object into the Servlet Session when a user successfully logins. This is done within both checkLogin() methods. This UserSession object is available to you for accessing information about the user and the session.

**httpRptServer.getHttpUserSessionManager().getUserSession()**

|  |
| --- |
| ``` <%             // Assume this code is below an authentication check, so we know a user is logged in.          // Get httpRptServer using the method that connects to existing server     HttpRptServer httpRptServer = HttpUtil.getHttpRptServer(request);         // User is logged in so the UserSession object exists.     UserSession userSession = httpRptServer.getHttpUserSessionManager().getUserSession(request);     String user = userSession.getUserId();     long startSessionValue = userSession.getCreateTime();     String startSessionTime = dateUtil.getDateTime(startSessionTime); %> <p> User Name: <%=user %><br> Logged in: <%=startSessionTime %> </p> ``` |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Running a Report

A major reason to use Logi JReport Server is to extend an application so that users can run reports and view results. A typical use case is having a front end JSP page interact with a user
to gather control information and another action page or servlet perform the intended operation.

The data entry form for interacting with the user is built with data entry fields having names that the action page will know about when getting parameters to use in running the report request.

Logi JReport Server uses a standard set of parameter names that are defined in the APIUtil class. These are ones used by Logi JReport Server JSP pages and servlets. Use these names for fields in data entry forms and when writing new JSP action pages so that code is standard across application JSP pages and Logi JReport Server JSP pages.

### Running a Report Using Java Method Call

**HttpRptServer.runReport()**

This code shows the basic flow of an action page that makes a Java method call to run a report. The code is for a JSP page called with the intention to run a specified report and show the result to the client through the browser getting a sequence of HTML pages. It will enforce that narrow charter.

The JSP page would be called with a URL of this form:

`http://abc.jsp?jrs.cmd=jrs.try_vw&jrs.result_type=1&jrs.path=/SampleReports/SampleReports.cat&jrs.catalog=/SampleReports/SampleReports.cat&jrs.report=/SampleReports/Employee Information.cls`

The intention of this code snippet is to show how to call an on-demand report using a Java method call, and then get the result from a temporary file and pass the result to the browser where the user can see it. The operation will only be performed for a logged in user who has permission to run an on-demand report for the given report in the given catalog.

|  |
| --- |
| ``` <%@ page import="java.io.*, java.util.*,jet.cs.util.*" %>  <%@ page import="jet.server.api.http.*" %>  <%@ page import="jet.server.api.*" %> <%           // Assume this JSP file is called with query parameters           // that request the operation to run and view a report,           // with the specified report, and result type.           // Only HTML Result type is allowed.         // Make sure a Report Server is running.     System.getProperties().put("reporthome", "C:\\Logi JReport\\Server");     HttpUtil.initEnv(System.getProperties()):         // Get a handle to a running Report Server.       HttpRptServer httpRptServer = HttpUtil.getHttpRptServer(request);         // Create a properties that holds no credentials from the URL query parameters.         // Don't let the current URL do a login of the user.     Properties props = new Properties(); try{      if (!httpRptServer.getHttpUserSessionManager().checkLogin(request,                                 httpRptServer.getResourceManager().getRealm(), props)) {         String url="login.jsp";         response.setStatus(HttpServletResponse.SC_MOVED_TEMPORARILY);         response.setHeader("Location", url);         response.setHeader("Content-Location", url)         return;     } }catch(Throwable t){      // failure to authenticate because of an exception     return; }      // Code below here will execute if a Logi JReport user is logged in.  try{          // request holds session for this user, to provide user for permission check.         // request holds URL for this page, to provide query parameters defining operation and resource.     boolean allowed = HttpUtil.checkPermission(request);     if (!allowed) {          // reject the requested operation.          return;     }      // Code below here will execute if the current user can do the operation on the target resource.     // The intended use is that the operation is jrs.try_vw,     //    jrs.cmd=jrs.try_vw     //  for the Employee Information.cls report in the SampleReports/SampleReports.cat catalog      //  with a HTML result type.     String user = HttpUtil.getUser(request);       String cmd = request.getParameter(APIConst.TAG_CMD);           //   cmd = "jrs.try_vw";      if (! cmd.equals(APIConst.CMD_TRY_VIEW)) {         return;         // this JSP only does one type command     }     String rstType = request.getParameter(APIConst.TAG_RESULT_TYPE);     int intRstType = APIUtil.parseInt(rstType, -1);           //  intRstType = 1; // APIConst.HTML     if (intRstTupe != APIConst.HTML) {         return;         // this JSP only does HTML result type     }     String cat = request.getParameter(APIConst.TAG_CATALOG);           //   cat = "/SampleReports/SampleReports.cat";      if (cat == null || cat.trim().length() < 1) {             // if not passed in, set it to this one.         cat = "/SampleReports/SampleReports.cat";      }     String rptName = request.getParameter(APIConst.TAG_REPORT);           //  rptName = "CustomerAnalysis.cls";      if (rptName == null || rptName.trim().length() < 1) {             // if not passed in, set it to this one.         rptName = "CustomerAnalysis.cls";      }     Properties ht = new Properties();          // Register intent to have HTML result. Property value is a String.      ht.put(APIConst.TAG_RESULT_TYPE, rstType);           // Use Java method to run an on-demand report, and wait for it,           //   with the intent to view the result as HTML.          // runReport() returns the name of the temp file holding the first HTML result page.     String rst = httpRptServer.runReport(user, cat, rptName, ht);     if (rst == null) {          // Failure without throwing an exception.         // Add code to recover.         return;     } else {               // Set the owner of the result file to be the current user.          httpRptServer.getTempResultOwnerManager().registerOwner(user,         HttpUtil.getTempResultKey(new File(rst).getName()));              // make the URL to view the first HTML result page.              // The "/sendfile/" is the path of built-in servlet of SendFileServlet              // of Logi JReport Server. This rstURL will redirect to the SendFileServlet.              // The SendFileServlet will send the HTML result page to the client.          String rstURL = request.getScheme() + "://" + request.getServerName() +                      ":" + request.getServerPort() +                      "/servlet/sendfile/result/" + HttpUtil.encodeEsc(new File(rst).getName());               // redirect to the rstURL         response.setStatus(HttpServletResponse.SC_MOVED_TEMPORARILY);          response.setHeader("Location", rstURL);          response.setHeader("Content-Location", rstURL);      }  }catch(RptServerException e){      // output error      e.printStackTrace();  }catch(Throwable t){      // output error      t.printStackTrace();  } %> ``` |

### Running a Report Using a Servlet URL

**HttpRptServer.runReport() and dhtmljsp servlet**

The code is for a JSP page called with the intention to run a specified report. A parameter is passed in to indicate if it is to be viewed as a sequence of HTML pages or in Page Report Studio. If the request is to view it as a sequence of HTML pages, this will call runReport() in the same way the example above did. If the request is to view the result in Page Report Studio, this will "call" a servlet URL.
The point of this example is to see how a URL to a Logi JReport Server JSP page or servlet can be seen as high level "call".

The JSP page would be called with a URL of this form:

* Requesting the result as a sequence of HTML pages:

  `http://abc.jsp?jrs.cmd=jrs.try_vw&jrs.result_type=1&jrs.path=/SampleReports/SampleReports.cat&jrs.catalog=/SampleReports/SampleReports.cat&jrs.report=/SampleReports/Employee Information.cls`
* Requesting the result in Page Report Studio:

  `http://abc.jsp?jrs.cmd=jrs.try_vw&jrs.result_type=8&jrs.path=/SampleReports/SampleReports.cat&jrs.catalog=/SampleReports/SampleReports.cat&jrs.report=/SampleReports/Employee Information.cls`

The intention of this code snippet is to extend the previous example to show how to pass a request to another servlet that is dedicated to handling the type of request.

|  |
| --- |
| ``` <%@ page import="java.io.*, java.util.*,jet.cs.util.*" %>  <%@ page import="jet.server.api.http.*" %>  <%@ page import="jet.server.api.*" %> <%           // Assume this JSP file is called with query parameters           // that request the operation to run and view a report,           // with the specified report, and result type.           // Only HTML Result type is allowed.         // Make sure a Report Server is running.     System.getProperties().put("reporthome", "C:\\Logi JReport\\Server");     HttpUtil.initEnv(System.getProperties()):         // Get a handle to a running Report Server.       HttpRptServer httpRptServer = HttpUtil.getHttpRptServer(request);         // Create a properties that holds no credentials from the URL query parameters.         // Don't let the current URL do a login of the user.     Properties props = new Properties(); try{      if (!httpRptServer.getHttpUserSessionManager().checkLogin(request,                                 httpRptServer.getResourceManager().getRealm(), props)) {         String url="login.jsp";         response.setStatus(HttpServletResponse.SC_MOVED_TEMPORARILY);         response.setHeader("Location", url);         response.setHeader("Content-Location", url)         return;     } }catch(Throwable t){      // failure to authenticate because of an exception     return; }      // Code below here will execute if a Logi JReport user is logged in.  try{          // request holds session for this user, to provide user for permission check.         // request holds URL for this page, to provide query parameters defining operation and resource.     boolean allowed = HttpUtil.checkPermission(request);     if (!allowed) {          // reject the requested operation.          return;     }      // Code below here will execute if the current user can do the operation on the target resource.     // The intended use is that the operation is jrs.try_vw,     //    jrs.cmd=jrs.try_vw     //  for the Employee Information.cls report in the SampleReports/SampleReports.cat catalog      //  with a HTML result type.     String user = HttpUtil.getUser(request);       String cmd = request.getParameter(APIConst.TAG_CMD);           //   cmd = "jrs.try_vw";      if (! cmd.equals(APIConst.CMD_TRY_VIEW)) {         return;         // this JSP only does one type command     }     String cat = request.getParameter(APIConst.TAG_CATALOG);           //   cat = "/SampleReports/SampleReports.cat";      if (cat == null || cat.trim().length() < 1) {             // if not passed in, set it to this one.         cat = "/SampleReports/SampleReports.cat";      }     String rptName = request.getParameter(APIConst.TAG_REPORT);           //  rptName = "CustomerAnalysis.cls";      if (rptName == null || rptName.trim().length() < 1) {             // if not passed in, set it to this one.         rptName = "CustomerAnalysis.cls";      }     String rstType = request.getParameter(APIConst.TAG_RESULT_TYPE);     int intRstType = APIUtil.parseInt(rstType, -1);           //  intRstType = 1; // APIConst.HTML         //  intRstType = 8; // APIConst.DHTML     if (intRstTupe != APIConst.HTML) {         if (intRstTupe != APIConst.DHTML) {             return;             // this JSP only does HTML or Page Report Result type         }         // Here to handle request for Page Report Result.         // Pass the request to the specialist for this type report.         String dhtmlURL = "/webos/app/pagestudio/run.jsp?jrs.catalog=" + cat + "&jrs.report=" + rptName;         response.setStatus(HttpServletResponse.SC_MOVED_TEMPORARILY);         response.setHeader("Location", dhmtlURL);         response.setHeader("Content-Location", dhmtlURL);         return;     }     // here when request is for HTML     Properties ht = new Properties();          // Register intent to have HTML result. Property value is a String.      ht.put(APIConst.TAG_RESULT_TYPE, rstType);           // Use Java method to run an on-demand report, and wait for it,           //   with the intent to view the result as HTML.          // runReport() returns the name of the temp file holding the first HTML result page.     String rst = httpRptServer.runReport(user, cat, rptName, ht);     if (rst == null) {          // Failure without throwing an exception.         // Add code to recover.         return;     } else {               // Set the owner of the result file to be the current user.          httpRptServer.getTempResultOwnerManager().registerOwner(user,         HttpUtil.getTempResultKey(new File(rst).getName()));              // make the URL to view the first HTML result page.              // The "/sendfile/" is the path of built-in servlet of SendFileServlet              // of Logi JReport Server. This rstURL will redirect to the SendFileServlet.              // The SendFileServlet will send the HTML result page to the client.          String rstURL = request.getScheme() + "://" + request.getServerName() +                      ":" + request.getServerPort() +                      "/servlet/sendfile/result/" + HttpUtil.encodeEsc(new File(rst).getName());               // redirect to the rstURL         response.setStatus(HttpServletResponse.SC_MOVED_TEMPORARILY);          response.setHeader("Location", rstURL);          response.setHeader("Content-Location", rstURL);      }  }catch(RptServerException e){      // output error      e.printStackTrace();  }catch(Throwable t){      // output error      t.printStackTrace();  } %> ``` |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668401-Tour-of-the-Java-API)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668201-Java-API-for-an-Application)
