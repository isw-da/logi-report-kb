---
title: "Deploying Logi Report Server to a Java Application Server"
id: 5741431629463
section: "Logi Report Server Integration Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741431629463-Deploying-Logi-Report-Server-to-a-Java-Application-Server
updated_at: 2022-10-31T17:17:55Z
---

# Deploying Logi Report Server to a Java Application Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741453049495-Four-Ways-of-Integrating-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741473716631-Deploying-Server-to-IBM-WebSphere-9-0-5-6)

# Deploying Logi Report Server to a Java Application Server

After you create a [WAR/EAR file](https://devnet.logianalytics.com/hc/en-us/articles/5741473837719-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server) that includes a self-contained Logi Report Server, you can deploy the WAR/EAR to an application server using the application server's instructions. This topic describes how you can deploy Logi Report Server to leading Java EE application servers.

The instructions are applicable to all the platforms that Logi Report Server supports.

Select the following links to view the topics:

* [Deploying Server to IBM WebSphere 9.0.5.6](https://devnet.logianalytics.com/hc/en-us/articles/5741473716631-Deploying-Server-to-IBM-WebSphere-9-0-5-6)
* [Deploying Server to WebLogic 14.1.1](https://devnet.logianalytics.com/hc/en-us/articles/5741467821079-Deploying-Server-to-WebLogic-14-1-1)
* [Deploying Server to Tomcat 9.0.68](https://devnet.logianalytics.com/hc/en-us/articles/5741447811223-Deploying-Server-to-Tomcat)
* [Deploying Server to JBoss EAP 7.4.0](https://devnet.logianalytics.com/hc/en-us/articles/5741437564439-Deploying-Server-to-JBoss-EAP)
* [Deploying Server to Sun Java™ System Application Server Platform Edition 9.1](https://devnet.logianalytics.com/hc/en-us/articles/5741467759639-Deploying-Server-to-Sun-Java-System-Application-Server-Platform-Edition-9-1)
* [Deploying Server to Jetty](https://devnet.logianalytics.com/hc/en-us/articles/5741467690263-Deploying-Server-to-Jetty)
* [Deploying Server to GlassFish Server Open Source Edition 5.0](https://devnet.logianalytics.com/hc/en-us/articles/5741447688983-Deploying-Server-to-GlassFish-Server-Open-Source-Edition-5-0)
* [Deploying Server to Resin 4.0.66](https://devnet.logianalytics.com/hc/en-us/articles/5741452764823-Deploying-Server-to-Resin)
* [Deploying Server to WildFly 26.1.2](https://devnet.logianalytics.com/hc/en-us/articles/5741437708951-Deploying-Server-to-WildFly)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) You can change the location of the two folders, **skin** and **dhtmljsp** in the \public\_html directory, on the application server side. Create the **jrserver.properties** file in the \WEB-INF directory, add the following two properties, and provide the correct paths (excluding the context root):

web.skin.dir  
web.dhtml\_jsp\_path

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741453049495-Four-Ways-of-Integrating-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741473716631-Deploying-Server-to-IBM-WebSphere-9-0-5-6)
