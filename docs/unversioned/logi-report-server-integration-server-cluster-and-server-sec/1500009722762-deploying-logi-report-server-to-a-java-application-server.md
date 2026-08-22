---
title: "Deploying Logi Report Server to a Java Application Server"
id: 1500009722762
section: "Logi Report Server Integration, Server Cluster, and Server Security Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009722762-Deploying-Logi-Report-Server-to-a-Java-Application-Server
updated_at: 2021-07-25T07:19:04Z
---

# Deploying Logi Report Server to a Java Application Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722902-Four-Ways-of-Integrating-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009722842-Deploying-to-IBM-WebSphere-9-0-5-3)

# Deploying Logi Report Server to a Java Application Server

After you have created a [WAR/EAR file](https://devnet.logianalytics.com/hc/en-us/articles/1500009749861-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server) that includes a self-contained Logi Report Server, you can deploy the WAR/EAR to an application server following the deploying instructions of the application server.

The following topics provide examples of deploying Logi Report Server to several leading Java EE application servers. The instructions are applicable to all the platforms Logi Report Server supports.

* [Deploying to IBM WebSphere 9.0.5.3](https://devnet.logianalytics.com/hc/en-us/articles/1500009722842-Deploying-to-IBM-WebSphere-9-0-5-3)
* [Deploying to WebLogic 12c (12.2.1.3.0)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749761-Deploying-to-WebLogic-12c-12-2-1-3-0-)
* [Deploying to Tomcat 9.0.34](https://devnet.logianalytics.com/hc/en-us/articles/1500009749741-Deploying-to-Tomcat-9-0-34)
* [Deploying to JBoss EAP 7.3.0](https://devnet.logianalytics.com/hc/en-us/articles/1500009722782-Deploying-to-JBoss-EAP-7-3-0)
* [Deploying to Sun Java™ System Application Server Platform Edition 9.1](https://devnet.logianalytics.com/hc/en-us/articles/1500009722822-Deploying-to-Sun-Java-System-Application-Server-Platform-Edition-9-1)
* [Deploying to Jetty 9.4.28](https://devnet.logianalytics.com/hc/en-us/articles/1500009722802-Deploying-to-Jetty-9-4-28)
* [Deploying to GlassFish Server Open Source Edition 5.0](https://devnet.logianalytics.com/hc/en-us/articles/1500009749701-Deploying-to-GlassFish-Server-Open-Source-Edition-5-0)
* [Deploying to Resin 4.0.64](https://devnet.logianalytics.com/hc/en-us/articles/1500009749721-Deploying-to-Resin-4-0-64)
* [Deploying to WildFly 19.0.0.0](https://devnet.logianalytics.com/hc/en-us/articles/1500009749781-Deploying-to-WildFly-19-0-0-0)

**Notes:** It is supported if you change the location of the two folders, skin and dhtmljsp, which are in the \public\_html directory in the application server side. What is needed is creating a file jrserver.properties in the \WEB-INF directory and then adding the following two properties and providing the correct paths (the context root is excluded):

web.skin.dir  
web.dhtml\_jsp\_path

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722902-Four-Ways-of-Integrating-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009722842-Deploying-to-IBM-WebSphere-9-0-5-3)
