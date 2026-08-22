---
title: "Creating and Getting Instances"
id: 1500009712061
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009712061-Creating-and-Getting-Instances
updated_at: 2021-11-03T06:58:34Z
---

# Creating and Getting Instances

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686222-Using-the-Server-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686342-Using-JSP-with-a-Dedicated-Machine)

# Creating and Getting Instances

This topic introduces how to create and get instances of the Report Engine and Logi JReport Server.

## Creating and Getting Instances of the Report Engine

To get an instance of the Report Engine, you can use the method *getInstance()* or *getInstance(boolean setDebugLevel)* in the jet.server.api.engine.ReportEngineFactory interface.

For example,

`bean = ReportEngineFactory.getInstance();`

or,

`bean = ReportEngineFactory.getInstance(true);`

## Creating and Getting Instances of Logi JReport Server

You can use the following methods to get access to the instance of Logi JReport Server.
Logi JReport Server is a singleton - only one instance can exist in the system.
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
  System.getProperties().put("reporthome", "C:\\JReport\\Server");  
  
					
    //  Create instance of ReportServer or do nothing if one is running already in this JVM  
  HttpUtil.initEnv(System.getProperties());  
  
    
  HttpRptServer server = HttpUtil.getHttpRptServer();  
  
   
    // Do something using the returned server object.
```

**Method 2**

Call the method *HttpUtil.checkLogin(HttpServletRequest req, HttpServletResponse res)*.

The method *jet.server.api.http.HttpUtil.checkLogin()* implicitly calls *HttpUtil.initEnv()* if necessary. So you can get the HttpRptServer after calling *HttpUtil.checkLogin()*.

```
    // Use checkLogin to control access to the rest of the code in JSP file.  

  if (HttpUtil.checkLogin(request, response))  

    {  

        // When a Logi JReport user logs into the current session  
  

        // get the instance of HttpRptServer .  

    jet.server.api.http.HttpRptServer httpRptServer = HttpUtil.getHttpRptServer();   
  

    // Do something using the returned httpRptServer object.  

    }
```

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686222-Using-the-Server-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686342-Using-JSP-with-a-Dedicated-Machine)
