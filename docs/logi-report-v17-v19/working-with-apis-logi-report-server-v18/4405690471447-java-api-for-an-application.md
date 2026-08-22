---
title: "Java API for an Application"
id: 4405690471447
section: "Working with APIs Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690471447-Java-API-for-an-Application
updated_at: 2022-01-27T08:00:05Z
---

# Java API for an Application

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683569943-Java-API-for-a-Servlet)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683545111-Installing-the-Server-API)

# Java API for an Application

You can call Logi Report Server directly in your application using Logi Report Server API or Remote Server API, instead of using JSP pages and URLs. This topic describes the two types of server APIs and how you can use them to write client code.

* Logi Report **Server API:**Logi Report provides a library of methods to directly start Logi Report Server as part of the customers application running in the same JVM as the application.
* Logi Report **Remote Server API:**Logi Report provides methods to connect to an already running instance of Logi Report Server either running on the local machine in a different JVM or running on an entirely different server. Other than the first call to connect either using RMI or directly in the current JVM, the rest of the API is identical so it is easy to write an application that can work either remotely or locally the same as the JSP pages that Logi Report provides.

This topic contains the following sections:

* [How to Write Client Code Using the Server API](#Server)
* [How to Write Client Code Using the Remote Server API](#Remote)

## How to Write Client Code Using the Server API

If you want the entire Logi Report Server to run in the context of your application in the same JVM you can use the Server API. The Server when started this way starts a number of threads and runs exactly the same as when the server is started as a standalone server. The server starts and stops with the application. The access to the server such as RMI access from other applications is still allowed.

```
//set reporthome  
System.getProperties().put("reporthome", "C:\\LogiReport\\Server");  
// Creates instance of RptServer (this does nothing if Logi Report Server is already running in this JVM)  
HttpUtil.initEnv(System.getProperties());  
// Get a handle to the server instance  
RptServer server = HttpUtil.getHttpRptServer();
```

## How to Write Client Code Using the Remote Server API

It is exactly the same code as above except you get a remote handle to the RPTServer.

```
//set reporthome for logging and location of rmi.auth file for security  
System.getProperties().put("reporthome", "C:\\LogiReport\\Server");  
System.getProperties().put("jrs.rmi.auth_file", "C:\\LogiReport\\Server\\bin\\rmi.auth");  
//search the running server using default host and port  
String host = "localhost";  
String port = "1129";  
RptServer server = :diffupdate  
RemoteReportServerToolkit.getRemoteWrappedRptServer(host, port);
```

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683569943-Java-API-for-a-Servlet)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683545111-Installing-the-Server-API)
