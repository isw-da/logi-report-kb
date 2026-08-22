---
title: "Deploying Logi JReport Server to a Java Application Server"
id: 1500009717341
section: "Deploying Logi JReport Server to a Java Application Server"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009717341-Deploying-Logi-JReport-Server-to-a-Java-Application-Server
updated_at: 2021-11-03T06:57:00Z
---

# Deploying Logi JReport Server to a Java Application Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691242-Four-Ways-of-Integrating-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717441-Deploying-to-IBM-WebSphere-9-0-5-0)

# Deploying Logi JReport Server to a Java Application Server

After you have created a [WAR/EAR file](https://devnet.logianalytics.com/hc/en-us/articles/1500009717561-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server) that includes a self-contained Logi JReport Server, you can deploy the WAR/EAR to an application server following the deploying instructions of the application server.

The following topics provide examples of deploying Logi JReport Server to several leading Java EE application servers. The instructions are applicable to all the platforms Logi JReport Server supports.

* [Deploying to IBM WebSphere 9.0.5.0](https://devnet.logianalytics.com/hc/en-us/articles/1500009717441-Deploying-to-IBM-WebSphere-9-0-5-0)
* [Deploying to WebLogic 12c (12.2.1.3.0)](https://devnet.logianalytics.com/hc/en-us/articles/1500009691202-Deploying-to-WebLogic-12c-12-2-1-3-0-)
* [Deploying to Tomcat 9.0.24](https://devnet.logianalytics.com/hc/en-us/articles/1500009717421-Deploying-to-Tomcat-9-0-24)
* [Deploying to JBoss EAP 7.2](https://devnet.logianalytics.com/hc/en-us/articles/1500009717381-Deploying-to-JBoss-EAP-7-1)
* [Deploying to Sun Java™ System Application Server Platform Edition 9.1](https://devnet.logianalytics.com/hc/en-us/articles/1500009717401-Deploying-to-Sun-Java-System-Application-Server-Platform-Edition-9-1)
* [Deploying to Jetty 9.4.20](https://devnet.logianalytics.com/hc/en-us/articles/1500009691162-Deploying-to-Jetty-9-4-20)
* [Deploying to GlassFish Server Open Source Edition 5.0](https://devnet.logianalytics.com/hc/en-us/articles/1500009717361-Deploying-to-GlassFish-Server-Open-Source-Edition-5-0)
* [Deploying to Resin 4.0.62](https://devnet.logianalytics.com/hc/en-us/articles/1500009691182-Deploying-to-Resin-4-0-62)
* [Deploying to WildFly 17.0.1.Final](https://devnet.logianalytics.com/hc/en-us/articles/1500009717461-Deploying-to-WildFly-17-0-1-Final)

**Notes:** It is supported if you change the location of the two folders, skin and dhtmljsp, which are in the \public\_html directory in the application server side. What is needed is creating a file jrserver.properties in the \WEB-INF directory and then adding the following two properties and providing the correct paths (the context root is excluded):

web.skin.dir  
web.dhtml\_jsp\_path

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691242-Four-Ways-of-Integrating-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717441-Deploying-to-IBM-WebSphere-9-0-5-0)
