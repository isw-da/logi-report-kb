---
title: "Deploying Server to Jetty"
id: 45204001766925
section: "Report Server Integration Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204001766925-Deploying-Server-to-Jetty
updated_at: 2026-04-30T14:10:19Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Deploying Server to Jetty

This topic describes how you can deploy Report Server to Jetty. 

We use paths based on UNIX path name protocol in our example. The instruction applies to both UNIX and Windows installation. However, the path formats differ. For Windows it is in this format C:\LogiReport\Server instead of /opt/LogiReport/Server. 

Assume that the Report Server WAR file jreport.war is in the /opt/LogiReport/Server/bin/distribute directory. To create the WAR file, see Building a WAR/EAR File to Include a Self-contained Report Server. 

Report Server does not support Jetty 11.

To deploy Report Server to Jetty 
            9.4.50:

- Add jreport.war to the /opt/Jetty9.4.50/demo_base/webapps directory. 

- Start Jetty using the command java -jar /start.jar. If your Report uses JDK 9 or above, you need to start Jetty using the command java @/opt/LogiReport/Server/bin/java.option -jar ../start.jar instead. 

- Access Report Server using either URL:
    http://<hostname>:8080/jreport/jrserver
    
http://<hostname>:8080/jreport/jinfonet/index.jsp

To deploy Report Server to Jetty 
            10.0.13:

- 
Create a directory in Jetty for Report Server.

$ export JETTY_HOME=/path/to/jetty-home
$ mkdir /path/to/jetty-base
$ cd /path/to/jetty-base
$ java -jar $JETTY_HOME/start.jar --add-module=server,http,deploy

- 
Add a module LogiReport.mod

$ cd $JETTY_HOME/modules
$ vi ./LogiReport.mod
with the contents (an example):

[description]
logi Report Server Web Application
[depends]
servlet
annotations
apache-jsp
[files]
/path/to/jetty-base/webapps/jreport.war
[ini-template]
jetty.http.host=192.0.0.1

- Add jreport.war to the /path/to/jetty-base/webapps folder.

- 
Run the command to deploy the WAR:

$JAVA_HOME/java @/opt/LogiReport/Server/bin/java.option  -jar $JETTY_HOME/start.jar  --add-module=LogiReport
 You should specify the path of java.option when Report uses JDK 9 or higher.

- Start the Jetty server.
				

$JAVA_HOME/java @/opt/LogiReport/Server/bin/java.option  -jar $JETTY_HOME/start.jar
 You should specify the path of java.option when using JDK 9 or higher.

- Access Report Server using either URL:http://<hostname>:8080/jreport/jrserver
http://<hostname>:8080/jreport/jinfonet/index.jsp
