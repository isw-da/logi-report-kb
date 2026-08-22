---
title: "Creating and Getting Instances of RptServer or HttpRptServer"
id: 1500009668801
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009668801-Creating-and-Getting-Instances-of-RptServer-or-HttpRptServer
updated_at: 2021-07-24T20:55:26Z
---

# Creating and Getting Instances of RptServer or HttpRptServer

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644042-Creating-and-Getting-Instances-of-ReportEngine)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644062-Using-JSP-With-a-Dedicated-Machine)

# Creating and Getting Instances of RptServer or HttpRptServer

You can use the following methods to get access to the instance of Logi JReport Server.
Logi JReport Server is a singleton - only one instance can exist in the system.
Access to the server is through a returned RptServer object or a returned HttpRptServer object, depending on the environment
of the request to get access.
RptServer is designed to be instantiated in a Java Application while HttpRptServer is designed to be instantiated in a JSP page. HttpRptServer has a few extra methods available to use in the HTTP session.

**Method 1**

Use the method jet.server.api.http.HttpUtil.initEnv(Properties props).

The method jet.server.api.http.HttpUtil.initEnv(...) creates and initializes the HttpRptServer object. If the HttpRptServer has already been started in this application, it will use the existing HttpRptServer instance. Use this method to avoid creating more than one HttpRptServer instance.

|  |
| --- |
| ```         //  prepare report server initial properties.         //  set report home minimally.         //  System.getProperties() will bring in all configured settings.     System.getProperties().put("reporthome", "C:\\Logi JReport\\Server");         //creates instance of ReportServer or does nothing if one is running already in this JVM     HttpUtil.initEnv(System.getProperties());          HttpRptServer server = HttpUtil.getHttpRptServer();         // do something using the returned server object. ``` |

**Method 2**

Call the method HttpUtil.checkLogin(HttpServletRequest req, HttpServletResponse res).

The method jet.server.api.http.HttpUtil.checkLogin(...) implicitly calls HttpUtil.initEnv(...) if necessary. So you can get the HttpRptServer after calling HttpUtil.checkLogin(...).

|  |
| --- |
| ```         // use checkLogin to control access to rest of code in JSP file.     if (HttpUtil.checkLogin(request, response))         {             // here, when a Logi JReport user is logged into the current session.             // get the instance of HttpRptServer .         jet.server.api.http.HttpRptServer httpRptServer = HttpUtil.getHttpRptServer();          // do something using the returned httpRptServer object.         } ``` |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644042-Creating-and-Getting-Instances-of-ReportEngine)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644062-Using-JSP-With-a-Dedicated-Machine)
