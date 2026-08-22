---
title: "Integrating Remote Logi JReport Server Guide v15 Server"
id: 1500009648482
section: "Server Integration Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648482-Integrating-Remote-Logi-JReport-Server-Guide-v15-Server
updated_at: 2021-07-24T20:54:10Z
---

# Integrating Remote Logi JReport Server Guide v15 Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673161-Deploying-to-WildFly-10-1-0)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673201-Integrating-Remote-Logi-JReport-Server-Guide-v15-Server-with-IBM-WebSphere-8-5-3-3-by-a-WAR-File)

# Integrating Remote Logi JReport Server

Normally, Logi JReport servlets are only integrated with other applications on the same machine. However, you can now implement Logi JReport Remote Server API in your JSPs, and integrate the JSPs with the application server to call Logi JReport Server, which is running on a different machine.

**Notes:**

* In a remote integration environment, the options for publishing resources are hidden since they are not supported by Logi JReport JSPs. If you want to publish reports or catalogs to Logi JReport Server, use one of the following ways:
  + Access the Logi JReport Server (not the remote server) Administration page with 8889 as the default port to perform publish work.
  + Copy the report or catalog files to the computer where Logi JReport Server (not the remote server) is located, and then call the RMI API to publish them.
  + Publish the report or catalog files from Logi JReport Designer to the Logi JReport Server.
* In a remote integration environment, running reports to the Applet format is not supported.
* In a remote integration environment, the two tabs Monitor and Data are hidden on Logi JReport Administration page since they are not supported.
* You can change the location of the two folders, skin and dhtmljsp, in the \public\_html directory in the application server side. What is required is to create a file jrserver.properties in the \WEB-INF directory and then add the following two properties and provide the correct paths (the context root is excluded):

  `web.skin.dir  
   web.dhtml_jsp_path`

See the following cases:

* [Integrating Remote Logi JReport Server With IBM WebSphere 8.5.3.3 by a WAR File](https://devnet.logianalytics.com/hc/en-us/articles/1500009673201-Integrating-Remote-Logi-JReport-Server-Guide-v15-Server-with-IBM-WebSphere-8-5-3-3-by-a-WAR-File)
* [Integrating Remote Logi JReport Server With WebLogic 11g Release 1 (10.3.2) by a WAR File](https://devnet.logianalytics.com/hc/en-us/articles/1500009673181-Integrating-Remote-Logi-JReport-Server-Guide-v15-Server-with-WebLogic-11g-Release-1-10-3-2-by-a-WAR-File)

**Related topic:**[Using JSP With a Dedicated Machine](https://devnet.logianalytics.com/hc/en-us/articles/1500009644062-Using-JSP-With-a-Dedicated-Machine)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673161-Deploying-to-WildFly-10-1-0)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673201-Integrating-Remote-Logi-JReport-Server-Guide-v15-Server-with-IBM-WebSphere-8-5-3-3-by-a-WAR-File)
