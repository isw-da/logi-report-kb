---
title: "Java API for an Application"
id: 1500009668201
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009668201-Java-API-for-an-Application
updated_at: 2021-07-24T20:55:31Z
---

# Java API for an Application

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644182-Java-API-for-a-Servlet)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009643642-Installing-the-Server-API)

# Java API for an Application

Logi JReport provides two ways for the application to call Logi JReport directly without using JSP pages and URLs:

* Logi JReport Server API: Logi JReport provides a library of methods to directly start Logi JReport Server as part of the customers application running in the same JVM as the application.
* Logi JReport Remote Server API: Logi JReport provides methods to connect to an already running instance of Logi JReport Server either running on the local machine in a different JVM or running on an entirely different server. Other than the first call to connect either using RMI or directly in the current JVM, the rest of the API is identical so it is easy to write an application that can work either remotely or locally the same as the JSP pages that Logi JReport provides.

**How to write client code using the Server API**

If you want the entire Logi JReport Server to run in the context of your application in the same JVM you can use the Server API. The Server when started this way starts a number of threads and runs exactly the same as when the server is started as a standalone server. The server just starts with the application and stops with the application. All access to the server such as RMI access from other applications is still allowed.

|  |
| --- |
| ```       //set report home   System.getProperties().put("reporthome", "C:\\Logi JReport\\Server");       // Creates instance of RptServer ( this does nothing if Logi JReport Server is already running in this JVM)   HttpUtil.initEnv(System.getProperties());       // Get a handle to the server instance   RptServer server = HttpUtil.getHttpRptServer(); ``` |

**How to write client code using the Remote Server API**

It is exactly the same code as above except you get a remote handle to the RPTServer.

|  |
| --- |
| ```       //set report home for logging and location of rmi.auth file for security   System.getProperties().put("reporthome", "C:\\Logi JReport\\Server");   System.getProperties().put("jrs.rmi.auth_file", "C:\\Logi JReport\\Server\\bin\\rmi.auth");       //search the running server using default host and port   String host = "localhost";   String port = "1129";   RptServer server = RemoteReportServerToolkit.getRemoteWrappedRptServer(host, port); ``` |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644182-Java-API-for-a-Servlet)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009643642-Installing-the-Server-API)
