---
title: "Deploying Logi JReport Server Guide v15 Server to a Java Application Server"
id: 1500009673041
section: "Server Integration Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673041-Deploying-Logi-JReport-Server-Guide-v15-Server-to-a-Java-Application-Server
updated_at: 2021-07-24T20:54:12Z
---

# Deploying Logi JReport Server Guide v15 Server to a Java Application Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648522-Four-Ways-of-Integrating-Logi-JReport-Server-Guide-v15-Server)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673141-Deploying-to-IBM-WebSphere-9-0-0-4)

# Deploying Logi JReport Server to a Java Application Server

After you have created a [WAR/EAR file](https://devnet.logianalytics.com/hc/en-us/articles/1500009648502-Building-a-WAR-EAR-file-to-Include-a-Self-contained-Logi-JReport-Server-Guide-v15-Server) that includes a self-contained Logi JReport Server, you can deploy the WAR/EAR to an application server following the deploying instructions of the application server.

This section provides examples of deploying Logi JReport Server to several leading Java EE application servers. The instructions are applicable to Unix, z/Linux and Windows platforms. However, the paths for Windows should use the Windows format, for example, `C:\Logi JReport\Server`, while paths for Unix and z/Linux should use the Unix and z/Linux format, for example, `/opt/Logi JReport/Server`.

The following examples are based on the Unix platform with one exception of Sun Application Server on Windows:

* [Deploying to IBM WebSphere 9.0.0.4](https://devnet.logianalytics.com/hc/en-us/articles/1500009673141-Deploying-to-IBM-WebSphere-9-0-0-4)
* [Deploying to WebLogic 12c Release 1 (12.2.1.3.0)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673121-Deploying-to-WebLogic-12c-Release-1-12-2-1-3-0-)
* [Deploying to Tomcat 8.5.23](https://devnet.logianalytics.com/hc/en-us/articles/1500009673101-Deploying-to-Tomcat-8-5-23)
* [Deploying to Jboss-as-7.1.1.Final or JBoss EAP 7.0](https://devnet.logianalytics.com/hc/en-us/articles/1500009648422-Deploying-to-Jboss-as-7-1-1-Final-or-JBoss-EAP-7-0)
* [Deploying to OC4J 10g R3 (10.1.3.5.0)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648442-Deploying-to-OC4J-10g-R3-10-1-3-5-0-)
* [Deploying to Sun Java™ System Application Server Platform Edition 9.1](https://devnet.logianalytics.com/hc/en-us/articles/1500009673081-Deploying-to-Sun-Java-System-Application-Server-Platform-Edition-9-1)
* [Deploying to Jetty 9.4.6](https://devnet.logianalytics.com/hc/en-us/articles/1500009673061-Deploying-to-Jetty-9-4-6)
* [Deploying to GlassFish V3](https://devnet.logianalytics.com/hc/en-us/articles/1500009648402-Deploying-to-GlassFish-V3)
* [Deploying to Resin 4.0.53](https://devnet.logianalytics.com/hc/en-us/articles/1500009648462-Deploying-to-Resin-4-0-53)
* [Deploying to WildFly 10.1.0](https://devnet.logianalytics.com/hc/en-us/articles/1500009673161-Deploying-to-WildFly-10-1-0)

**Notes:** It is supported if you change the location of the two folders, skin and dhtmljsp, which are in the `\public_html` directory in the application server side. What is needed is creating a file jrserver.properties in the \WEB-INF directory and then adding the following two properties and providing the correct paths (the context root is excluded):

`web.skin.dir  
 web.dhtml_jsp_path`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648522-Four-Ways-of-Integrating-Logi-JReport-Server-Guide-v15-Server)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673141-Deploying-to-IBM-WebSphere-9-0-0-4)
