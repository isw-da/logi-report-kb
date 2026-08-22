---
title: "Deploying Server to Jetty"
id: 4405683910551
section: "Logi Report Server Integration Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683910551-Deploying-Server-to-Jetty
updated_at: 2022-01-27T07:59:34Z
---

# Deploying Server to Jetty

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690628631-Deploying-Server-to-Sun-Java-System-Application-Server-Platform-Edition-9-1)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690626583-Deploying-Server-to-GlassFish-Server-Open-Source-Edition-5-0)

# Deploying Server to Jetty

This topic describes how you can deploy Logi Report Server to Jetty.

We use paths based on UNIX path name protocol in our example. The instruction applies to both UNIX and Windows installation. However, the path formats differ. For Windows it is in this format `C:\LogiReport\Server` instead of `/opt/LogiReport/Server`.

Assume that the Logi Report Server WAR file **jreport.war** is in the `/opt/LogiReport/Server/bin/distribute` directory. To create the WAR file, see [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/4405690635159-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)Logi Report Server does not support Jetty 11.

**To deploy Logi Report Server to Jetty
9.4.44:**

1. Add **jreport.war** to the `/opt/Jetty9.4.44/demo_base/webapps` directory.
2. Start Jetty using the command `java -jar /start.jar`. If your Logi Report uses JDK 9 or above, you need to start Jetty using the command `java @/opt/LogiReport/Server/bin/java.option -jar ../start.jar` instead.
3. Access Logi Report Server using either URL:

   `http://<hostname>:8080/jreport/jrserver
     
   http://<hostname>:8080/jreport/jinfonet/index.jsp`

**To deploy Logi Report Server to Jetty
10.0.7:**

1. Create a directory in Jetty for Logi Report Server.

   ```
   $ export JETTY_HOME=/path/to/jetty-home  
   $ mkdir /path/to/jetty-base  
   $ cd /path/to/jetty-base  
   $ java -jar $JETTY_HOME/start.jar --add-module=server,http,deploy
   ```
2. Add a module **LogiReport.mod**

   ```
   $ cd $JETTY_HOME/modules  
   $ vi ./LogiReport.mod
   ```

   with the contents (an example):

   ```
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
   ```
3. Add **jreport.war** to the `/path/to/jetty-base/webapps` directory.
4. Run the command to deploy the WAR:

   ```
   $JAVA_HOME/java @/opt/LogiReport/Server/bin/java.option  -jar $JETTY_HOME/start.jar  --add-module=LogiReport
   ```

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) You should specify the path of **java.option** when Logi Report uses JDK 9 or higher.
5. Start the Jetty server.

   ```
   $JAVA_HOME/java @/opt/LogiReport/Server/bin/java.option  -jar $JETTY_HOME/start.jar
   ```

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) You should specify the path of **java.option** when using JDK 9 or higher.
6. Access Logi Report Server using either URL:

   `http://<hostname>:8080/jreport/jrserver  
   http://<hostname>:8080/jreport/jinfonet/index.jsp`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690628631-Deploying-Server-to-Sun-Java-System-Application-Server-Platform-Edition-9-1)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690626583-Deploying-Server-to-GlassFish-Server-Open-Source-Edition-5-0)
