---
title: "Deploying Logi Report Server to a Java Application Server"
id: 4405683908375
section: "Logi Report Server Integration Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683908375-Deploying-Logi-Report-Server-to-a-Java-Application-Server
updated_at: 2022-01-27T07:59:33Z
---

# Deploying Logi Report Server to a Java Application Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683916439-Four-Ways-of-Integrating-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690631447-Deploying-Server-to-IBM-WebSphere-9-0-5-6)

# Deploying Logi Report Server to a Java Application Server

After you create a [WAR/EAR file](https://devnet.logianalytics.com/hc/en-us/articles/4405690635159-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server) that includes a self-contained Logi Report Server, you can deploy the WAR/EAR to an application server using the application server's instructions. This topic describes how you can deploy Logi Report Server to leading Java EE application servers.

The instructions are applicable to all the platforms that Logi Report Server supports.

Select the following links to view the topics:

* [Deploying Server to IBM WebSphere 9.0.5.6](https://devnet.logianalytics.com/hc/en-us/articles/4405690631447-Deploying-Server-to-IBM-WebSphere-9-0-5-6)
* [Deploying Server to WebLogic 14.1.1](https://devnet.logianalytics.com/hc/en-us/articles/4405690630551-Deploying-Server-to-WebLogic-14-1-1)
* [Deploying Server to Tomcat 9.0.56](https://devnet.logianalytics.com/hc/en-us/articles/4405690629655-Deploying-Server-to-Tomcat)
* [Deploying Server to JBoss EAP 7.4.0](https://devnet.logianalytics.com/hc/en-us/articles/4405683909527-Deploying-Server-to-JBoss-EAP)
* [Deploying Server to Sun Java™ System Application Server Platform Edition 9.1](https://devnet.logianalytics.com/hc/en-us/articles/4405690628631-Deploying-Server-to-Sun-Java-System-Application-Server-Platform-Edition-9-1)
* [Deploying Server to Jetty](https://devnet.logianalytics.com/hc/en-us/articles/4405683910551-Deploying-Server-to-Jetty)
* [Deploying Server to GlassFish Server Open Source Edition 5.0](https://devnet.logianalytics.com/hc/en-us/articles/4405690626583-Deploying-Server-to-GlassFish-Server-Open-Source-Edition-5-0)
* [Deploying Server to Resin 4.0.66](https://devnet.logianalytics.com/hc/en-us/articles/4405690627735-Deploying-Server-to-Resin-4-0-65)
* [Deploying Server to WildFly 26.0.0](https://devnet.logianalytics.com/hc/en-us/articles/4405683912471-Deploying-Server-to-WildFly)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) You can change the location of the two folders, **skin** and **dhtmljsp** in the \public\_html directory, on the application server side. Create the **jrserver.properties** file in the \WEB-INF directory, add the following two properties, and provide the correct paths (excluding the context root):

web.skin.dir  
web.dhtml\_jsp\_path

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683916439-Four-Ways-of-Integrating-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690631447-Deploying-Server-to-IBM-WebSphere-9-0-5-6)
