---
title: "Deploying Server to Jetty 9.4.31"
id: 1500009776841
section: "Deploying Logi Report Server to a Java Application Server"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009776841-Deploying-Server-to-Jetty-9-4-31
updated_at: 2023-06-11T21:52:46Z
---

# Deploying Server to Jetty 9.4.31

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748442-Deploying-Server-to-Sun-Java-System-Application-Server-Platform-Edition-9-1)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748422-Deploying-Server-to-GlassFish-Server-Open-Source-Edition-5-0)

# Deploying Server to Jetty 9.4.31

This topic describes how you can deploy Logi Report Server to Jetty.

In the example we use directory paths based on Unix. The instructions are applicable to both Unix and Windows installations. However, the format of the paths for Windows should use the Windows format, that is, `C:\LogiReport\Server` instead of `/opt/LogiReport/Server`.

Assume that the Logi Report Server WAR file jreport.war is in the `/opt/LogiReport/Server/bin/distribute` directory. To create the WAR file, refer to the instructions in [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009777021-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

**To deploy Logi Report Server to Jetty 9.4.31:**

1. Remove or comment out the following code in the **web.xml** of jreport.war if you are integrating Logi Report Server with Jetty in a non-remote environment:

   `<login-config>  
   <auth-method>BASIC</auth-method>  
   </login-config>`
2. Add **jreport.war** to the `/opt/Jetty9.4.31/demo_base/webapps` directory.
3. Start Jetty using the command `java -jar /start.jar`. If your Logi Report uses JDK 9 or above, you need to start Jetty using the command `java @/FolderName/java.option -jar ../start.jar` instead.
4. Access Logi Report Server using the following URLs:

   `http://<hostname>:8080/jreport/jrserver
     
    http://<hostname>:8080/jreport/jinfonet/index.jsp`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748442-Deploying-Server-to-Sun-Java-System-Application-Server-Platform-Edition-9-1)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748422-Deploying-Server-to-GlassFish-Server-Open-Source-Edition-5-0)
