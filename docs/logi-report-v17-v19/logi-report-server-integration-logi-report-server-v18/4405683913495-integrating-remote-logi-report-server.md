---
title: "Integrating Remote Logi Report Server"
id: 4405683913495
section: "Logi Report Server Integration Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683913495-Integrating-Remote-Logi-Report-Server
updated_at: 2022-01-27T07:59:34Z
---

# Integrating Remote Logi Report Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683912471-Deploying-Server-to-WildFly)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683914775-Integrating-Remote-Logi-Report-Server-with-IBM-WebSphere-9-0-0-7-by-a-WAR-File)

# Integrating Remote Logi Report Server

You can implement Logi Report Remote Server API in your JSPs and integrate the JSPs with the application server to call Logi Report Server that is running on a different machine. This topic describes how you can integrate remote Logi Report Server with IBM WebSphere and WebLogic.

Select the following links to view the topics:

* [Integrating Remote Logi Report Server With IBM WebSphere 9.0.0.7 by a WAR File](https://devnet.logianalytics.com/hc/en-us/articles/4405683914775-Integrating-Remote-Logi-Report-Server-with-IBM-WebSphere-9-0-0-7-by-a-WAR-File)
* [Integrating Remote Logi Report Server With WebLogic 14.1.1 by a WAR File](https://devnet.logianalytics.com/hc/en-us/articles/4405690632471-Integrating-Remote-Logi-Report-Server-with-WebLogic-14-1-1-by-a-WAR-File)

**Related topic:**

* [Using JSP With a Dedicated Machine](https://devnet.logianalytics.com/hc/en-us/articles/4405683558167-Using-JSP-with-a-Dedicated-Machine)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)

* In a remote integration environment, Logi Report Server hides the options for publishing resources since Logi Report JSPs do not support them. If you want to publish reports or catalogs to Logi Report Server, use one of the following ways:
  + Access the Logi Report Server Console (not the remote server) as an administrator to perform publish work.
  + Copy the report or catalog files to the computer where Logi Report Server (not the remote server) is, and then call the RMI API to publish them.
  + Publish the report or catalog files from Logi Report Designer to Logi Report Server.
* In a remote integration environment, Logi Report Server hides the two links Administration > Other > Monitor and Administration > Configuration > Server DB in the Logi Report Server Console since they are not supported.
* You can change the location of the two folders, **skin** and **dhtmljsp**, in the \public\_html directory in the application server side. What you need to do is create a file **jrserver.properties** in the \WEB-INF directory and then add the following two properties and provide the correct paths (excluding the context root):

  `web.skin.dir  
   web.dhtml_jsp_path`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683912471-Deploying-Server-to-WildFly)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683914775-Integrating-Remote-Logi-Report-Server-with-IBM-WebSphere-9-0-0-7-by-a-WAR-File)
