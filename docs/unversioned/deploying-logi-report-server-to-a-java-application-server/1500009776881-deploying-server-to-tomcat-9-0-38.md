---
title: "Deploying Server to Tomcat 9.0.38"
id: 1500009776881
section: "Deploying Logi Report Server to a Java Application Server"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009776881-Deploying-Server-to-Tomcat-9-0-38
updated_at: 2021-07-24T00:48:03Z
---

# Deploying Server to Tomcat 9.0.38

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748462-Deploying-Server-to-WebLogic-14-1-1)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776821-Deploying-Server-to-JBoss-EAP-7-3-0)

# Deploying Server to Tomcat 9.0.38

This topic describes how you can deploy Logi Report Server to Tomcat.

In the example we use directory paths based on Unix. The instructions are applicable to both Unix and Windows installations. However, the format of the paths for Windows should use the Windows format, that is, `C:\LogiReport\Server` instead of `/opt/LogiReport/Server`.

Assume that:

* You installed Tomcat 9.0.38 in the `/opt/apache-tomcat-9.0.38` directory.
* The Logi Report Server WAR file **jreport.war** is in the `/opt/LogiReport/Server/bin/distribute` directory. To create the WAR file, refer to the instructions in [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009777021-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)When you set **unpackWARs="false"** in **server.xml** in the **conf** folder of Tomcat, you need to do the following:

  1. Modify the **LogConfig.properties** file in `/opt/LogiReport/Server/bin` before you create the WAR as follows:
     + Remove the code `packages = com.jinfonet.util`.
     + Change **JRRollingFileAppender** to **RollingFile** all over the file.
     + Change **JRPatternLayout** to **PatternLayout** all over the file.
  2. Add the parameter **-Djbossas7=true** when launching makewar.bat/.sh to build the WAR, for example:

     `makewar.bat -Djbossas7=true`
  3. Move **log4j-api-2.13.3.jar** and **log4j-core-2.13.3.jar** from jreport.war > WEB-INF > lib to the **lib** folder of Tomcat.

**To deploy Logi Report Server to Tomcat 9.0.38:**

1. Shut down Tomcat.
2. Copy **jreport.war** to `/opt/apache-tomcat-9.0.38/webapps`.
3. When running on Java 9 you need to additionally add the arguments in **java.option** in `$REPORTHOME/bin` to **Catalina.sh** in `$CATALINA_HOME/bin`.
4. Start Tomcat by running the script file **startup.sh**.
5. Access Logi Report Server using the following URLs:

   `http://hostname:8080/jreport/jrserver
     
    http://hostname:8080/jreport/jinfonet/index.jsp`

## Troubleshooting

If you run into problems when using Logi Report Server in Tomcat, send the log files of Logi Report Server to [support@logianalytics.com](mailto:support@logianalytics.com). The following procedure illustrates how to generate the log files:

1. Modify the **catalina.sh** file in `/opt/apache-tomcat-9.0.38/bin`, by adding `-Dlogall=true` after the report home definition:

   `JAVA_OPTS="-Dreporthome=/opt/LogiReport/Server-Dlogall=true"  
   Cygwin=false`

   Or if no report home is specified, add as follows:

   `JAVA_OPTS=-Dlogall=true  
   Cygwin=false`
2. Start Tomcat.
3. To get information about the Logi Report Server environment, you can access `http://hostname:8080/jreport/admin/info.jsp?cmd=info`.
4. Save the output to a file.
5. After reproducing the problem, send [support@logianalytics.com](mailto:support@logianalytics.com) the log files in `reporthome/logs.`

   The Tomcat log files may also help to identify the problem. The most useful one is /opt/apache-tomcat-9.0.38/logs/catalina.out.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748462-Deploying-Server-to-WebLogic-14-1-1)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776821-Deploying-Server-to-JBoss-EAP-7-3-0)
