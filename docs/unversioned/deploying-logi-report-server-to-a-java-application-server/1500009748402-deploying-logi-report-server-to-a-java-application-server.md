---
title: "Deploying Logi Report Server to a Java Application Server"
id: 1500009748402
section: "Deploying Logi Report Server to a Java Application Server"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009748402-Deploying-Logi-Report-Server-to-a-Java-Application-Server
updated_at: 2021-07-24T00:48:04Z
---

# Deploying Logi Report Server to a Java Application Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777041-Four-Ways-of-Integrating-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748482-Deploying-Server-to-IBM-WebSphere-9-0-5-4)

# Deploying Logi Report Server to a Java Application Server

After you have created a [WAR/EAR file](https://devnet.logianalytics.com/hc/en-us/articles/1500009777021-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server) that includes a self-contained Logi Report Server, you can deploy the WAR/EAR to an application server following the deploying instructions of the application server. This topic describes how you can deploy Logi Report Server to leading Java EE application servers.

The instructions are applicable to all the platforms that Logi Report Server supports.

Select the following links to view the topics:

* [Deploying Server to IBM WebSphere 9.0.5.4](https://devnet.logianalytics.com/hc/en-us/articles/1500009748482-Deploying-Server-to-IBM-WebSphere-9-0-5-4)
* [Deploying Server to WebLogic 14.1.1](https://devnet.logianalytics.com/hc/en-us/articles/1500009748462-Deploying-Server-to-WebLogic-14-1-1)
* [Deploying Server to Tomcat 9.0.38](https://devnet.logianalytics.com/hc/en-us/articles/1500009776881-Deploying-Server-to-Tomcat-9-0-38)
* [Deploying Server to JBoss EAP 7.3.0](https://devnet.logianalytics.com/hc/en-us/articles/1500009776821-Deploying-Server-to-JBoss-EAP-7-3-0)
* [Deploying Server to Sun Java™ System Application Server Platform Edition 9.1](https://devnet.logianalytics.com/hc/en-us/articles/1500009748442-Deploying-Server-to-Sun-Java-System-Application-Server-Platform-Edition-9-1)
* [Deploying Server to Jetty 9.4.31](https://devnet.logianalytics.com/hc/en-us/articles/1500009776841-Deploying-Server-to-Jetty-9-4-31)
* [Deploying Server to GlassFish Server Open Source Edition 5.0](https://devnet.logianalytics.com/hc/en-us/articles/1500009748422-Deploying-Server-to-GlassFish-Server-Open-Source-Edition-5-0)
* [Deploying Server to Resin 4.0.65](https://devnet.logianalytics.com/hc/en-us/articles/1500009776861-Deploying-Server-to-Resin-4-0-65)
* [Deploying Server to WildFly 20.0.1](https://devnet.logianalytics.com/hc/en-us/articles/1500009776901-Deploying-Server-to-WildFly-20-0-1)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)You can change the location of the two folders, **skin** and **dhtmljsp**, which are in the \public\_html directory in the application server side. What you need to do is create a file **jrserver.properties** in the \WEB-INF directory and then add the following two properties and provide the correct paths (excluding the context root):

web.skin.dir  
web.dhtml\_jsp\_path

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777041-Four-Ways-of-Integrating-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748482-Deploying-Server-to-IBM-WebSphere-9-0-5-4)
