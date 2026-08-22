---
title: "Deploying Report Server to a Java Application Server"
id: 45203976164109
section: "Report Server Integration Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203976164109-Deploying-Report-Server-to-a-Java-Application-Server
updated_at: 2026-04-30T14:10:18Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Deploying Report Server to a Java Application Server

After you create a WAR/EAR file that includes a self-contained Report Server, you can deploy the WAR/EAR to an application server using the application server's instructions. This topic describes how you can deploy Report Server to leading Java EE application servers.

The instructions are applicable to all the platforms that Report Server supports.

Select the following links to view the topics:

- Deploying Server to IBM WebSphere 9.0.5.6

- Deploying Server to WebLogic 14.1.1

- Deploying Server to Tomcat 9.0.70

- Deploying Server to JBoss EAP 7.4.0

- Deploying Server to Sun Java™ System Application Server Platform Edition 9.1

- Deploying Server to Jetty

- Deploying Server to GlassFish Server Open Source Edition 5.0 

- Deploying Server to Resin 4.0.66

- Deploying Server to WildFly 26.1.2

 You can change the location of the two folders, skin and dhtmljsp in the \public_html directory, on the application server side. Create the jrserver.properties file in the \WEB-INF directory, add the following two properties, and provide the correct paths (excluding the context root): 

web.skin.dir
web.dhtml_jsp_path
