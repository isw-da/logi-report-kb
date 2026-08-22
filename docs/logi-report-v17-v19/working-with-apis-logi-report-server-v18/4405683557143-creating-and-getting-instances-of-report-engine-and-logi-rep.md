---
title: "Creating and Getting Instances of Report Engine and Logi Report Server"
id: 4405683557143
section: "Working with APIs Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683557143-Creating-and-Getting-Instances-of-Report-Engine-and-Logi-Report-Server
updated_at: 2022-01-27T08:00:03Z
---

# Creating and Getting Instances of Report Engine and Logi Report Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683547287-Using-the-Server-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683558167-Using-JSP-with-a-Dedicated-Machine)

# Creating and Getting Instances of Report Engine and Logi Report Server

This topic describes how to create and get instances of the Report Engine and Logi Report Server.

## Creating and Getting Instances of the Report Engine

To get an instance of the Report Engine, you can use the method *getInstance()* or *getInstance(boolean setDebugLevel)* in the jet.server.api.engine.ReportEngineFactory interface.

For example,

`bean = ReportEngineFactory.getInstance();`

or,

`bean = ReportEngineFactory.getInstance(true);`

## Creating and Getting Instances of Logi Report Server

You can use the following methods to get access to the instance of Logi Report Server.
Logi Report Server is a singleton - only one instance can exist in the system.
Access to the server is through a returned RptServer object or a returned HttpRptServer object, depending on the environment
of the request to get access.
RptServer is designed to be instantiated in a Java Application while HttpRptServer is designed to be instantiated in a JSP page. HttpRptServer has a few extra methods available to use in the HTTP session.

**Method 1**

Use the method *jet.server.api.http.HttpUtil.initEnv(Properties props)*.

The method *jet.server.api.http.HttpUtil.initEnv()* creates and initializes the HttpRptServer object. If the HttpRptServer has already been started in this application, it will use the existing HttpRptServer instance. Use this method to avoid creating more than one HttpRptServer instance.

```
    //  Prepare report server initial properties.  
    //  Set reporthome minimally.  
    //  System.getProperties() will bring in all configured settings.  
  System.getProperties().put("reporthome", "C:\\LogiReport\\Server");  
  
					
    //  Create instance of ReportServer or do nothing if one is running already in this JVM  
  HttpUtil.initEnv(System.getProperties());  
  
    
  HttpRptServer server = HttpUtil.getHttpRptServer();  
  
   
    // Do something using the returned server object.
```

**Method 2**

Call the method *HttpUtil.checkLogin(HttpServletRequest req, HttpServletResponse res)*.

The method *jet.server.api.http.HttpUtil.checkLogin()* implicitly calls *HttpUtil.initEnv()*. So, you can get the HttpRptServer after calling *HttpUtil.checkLogin()*.

```
    // Use checkLogin to control access to the rest of the code in JSP file.  
  if (HttpUtil.checkLogin(request, response))  
    {  
        // When a Logi Report user signs in to the current session  
  
        // get the instance of HttpRptServer.  
    jet.server.api.http.HttpRptServer httpRptServer = HttpUtil.getHttpRptServer();   
  
    // Do something using the returned httpRptServer object.  
    }
```

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683547287-Using-the-Server-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683558167-Using-JSP-with-a-Dedicated-Machine)
