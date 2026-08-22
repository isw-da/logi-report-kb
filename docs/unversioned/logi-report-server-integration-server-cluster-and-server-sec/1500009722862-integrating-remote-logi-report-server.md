---
title: "Integrating Remote Logi Report Server"
id: 1500009722862
section: "Logi Report Server Integration, Server Cluster, and Server Security Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009722862-Integrating-Remote-Logi-Report-Server
updated_at: 2021-07-25T07:19:02Z
---

# Integrating Remote Logi Report Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749781-Deploying-to-WildFly-19-0-0-0)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749821-Integrating-Remote-Logi-Report-Server-with-IBM-WebSphere-9-0-0-7-by-a-WAR-File)

# Integrating Remote Logi Report Server

Normally, Logi Report servlets are only integrated with other applications on the same machine. However, you can now implement Logi Report Remote Server API in your JSPs, and integrate the JSPs with the application server to call Logi Report Server, which is running on a different machine.

See the following cases:

* [Integrating Remote Logi Report Server With IBM WebSphere 9.0.0.7 by a WAR File](https://devnet.logianalytics.com/hc/en-us/articles/1500009749821-Integrating-Remote-Logi-Report-Server-with-IBM-WebSphere-9-0-0-7-by-a-WAR-File)
* [Integrating Remote Logi Report Server With WebLogic 12c (12.2.1.3.0) by a WAR File](https://devnet.logianalytics.com/hc/en-us/articles/1500009749801-Integrating-Remote-Logi-Report-Server-with-WebLogic-12c-12-2-1-3-0-by-a-WAR-File)

**Related topic:**

* [Using JSP With a Dedicated Machine](https://devnet.logianalytics.com/hc/en-us/articles/1500009744361-Using-JSP-with-a-Dedicated-Machine)

**Notes:**

* In a remote integration environment, the options for publishing resources are hidden since they are not supported by Logi Report JSPs. If you want to publish reports or catalogs to Logi Report Server, use one of the following ways:
  + Access the Logi Report Server console (not the remote server) as an administrator to perform publish work.
  + Copy the report or catalog files to the computer where Logi Report Server (not the remote server) is located, and then call the RMI API to publish them.
  + Publish the report or catalog files from Logi Report Designer to Logi Report Server.
* In a remote integration environment, the two links Administration > Other > Monitor and Administration > Configuration > Server DB are hidden in the Logi Report Server console since they are not supported.
* You can change the location of the two folders, skin and dhtmljsp, in the \public\_html directory in the application server side. What is required is to create a file jrserver.properties in the \WEB-INF directory and then add the following two properties and provide the correct paths (the context root is excluded):

  `web.skin.dir  
   web.dhtml_jsp_path`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749781-Deploying-to-WildFly-19-0-0-0)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749821-Integrating-Remote-Logi-Report-Server-with-IBM-WebSphere-9-0-0-7-by-a-WAR-File)
