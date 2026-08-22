---
title: "Integrating Remote Logi JReport Server"
id: 1500009717481
section: "Integrating Remote Logi JReport Server"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009717481-Integrating-Remote-Logi-JReport-Server
updated_at: 2021-11-03T06:56:59Z
---

# Integrating Remote Logi JReport Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009717461-Deploying-to-WildFly-17-0-1-Final)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009691222-Integrating-Remote-Logi-Report-Server-with-IBM-WebSphere-9-0-0-7-by-a-WAR-File)

# Integrating Remote Logi JReport Server

Normally, Logi JReport servlets are only integrated with other applications on the same machine. However, you can now implement Logi JReport Remote Server API in your JSPs, and integrate the JSPs with the application server to call Logi JReport Server, which is running on a different machine.

See the following cases:

* [Integrating Remote Logi JReport Server With IBM WebSphere 9.0.0.7 by a WAR File](https://devnet.logianalytics.com/hc/en-us/articles/1500009691222-Integrating-Remote-Logi-Report-Server-with-IBM-WebSphere-9-0-0-7-by-a-WAR-File)
* [Integrating Remote Logi JReport Server With WebLogic 12c (12.2.1.3.0) by a WAR File](https://devnet.logianalytics.com/hc/en-us/articles/1500009717501-Integrating-Remote-Logi-Report-Server-with-WebLogic-12c-12-2-1-3-0-by-a-WAR-File)

**Related topic:**

* [Using JSP With a Dedicated Machine](https://devnet.logianalytics.com/hc/en-us/articles/1500009686342-Using-JSP-with-a-Dedicated-Machine)

**Notes:**

* In a remote integration environment, the options for publishing resources are hidden since they are not supported by Logi JReport JSPs. If you want to publish reports or catalogs to Logi JReport Server, use one of the following ways:
  + Access the Logi JReport Server console (not the remote server) as an administrator to perform publish work.
  + Copy the report or catalog files to the computer where Logi JReport Server (not the remote server) is located, and then call the RMI API to publish them.
  + Publish the report or catalog files from Logi JReport Designer to Logi JReport Server.
* In a remote integration environment, the two links Administration > Other > Monitor and Administration > Configuration > Server DB are hidden in the Logi JReport Server console since they are not supported.
* You can change the location of the two folders, skin and dhtmljsp, in the \public\_html directory in the application server side. What is required is to create a file jrserver.properties in the \WEB-INF directory and then add the following two properties and provide the correct paths (the context root is excluded):

  `web.skin.dir  
   web.dhtml_jsp_path`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009717461-Deploying-to-WildFly-17-0-1-Final)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009691222-Integrating-Remote-Logi-Report-Server-with-IBM-WebSphere-9-0-0-7-by-a-WAR-File)
