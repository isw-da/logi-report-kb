---
title: "Deploying Server to Tomcat"
id: 4405690629655
section: "Logi Report Server Integration Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690629655-Deploying-Server-to-Tomcat
updated_at: 2022-01-28T14:21:55Z
---

# Deploying Server to Tomcat

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690630551-Deploying-Server-to-WebLogic-14-1-1)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683909527-Deploying-Server-to-JBoss-EAP)

# Deploying Server to Tomcat 9.0.56

This topic describes how you can deploy Logi Report Server to Tomcat 9.0.56.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)Logi Report Server does not support Tomcat 10.

We use paths based on UNIX path name protocol in our example. The instruction applies to both UNIX and Windows installation. However, the path formats differ. For Windows it is in this format `C:\LogiReport\Server` instead of `/opt/LogiReport/Server`.

Assume that:

* You installed Tomcat 9.0.56 in the `/opt/apache-tomcat` directory.
* The Logi Report Server WAR file **jreport.war** is in the `/opt/LogiReport/Server/bin/distribute` directory. To create the WAR file, see [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/4405690635159-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) When you set **unpackWARs="false"** in **server.xml** in the **conf** folder of Tomcat, you need to do the following:

  1. Modify the **LogConfig.properties** file in `/opt/LogiReport/Server/bin` before you create the WAR:
     + Remove the code `packages = com.jinfonet.util`.
     + Replace **JRRollingFileAppender** with **RollingFile** in the file.
     + Replace **JRPatternLayout** with **PatternLayout** in the file.
  2. Add the **-Djbossas7=true** parameter when launching makewar.bat/.sh to build the WAR.

     ```
     makewar.bat -Djbossas7=true
     ```
  3. Move **log4j-api-2.17.1.jar** and **log4j-core-2.17.1.jar** from jreport.war > WEB-INF > lib to the **lib** folder of Tomcat.

**To deploy Logi Report Server to Tomcat 9.0.56:**

1. Shut down Tomcat.
2. Copy **jreport.war** to `/opt/apache-tomcat/webapps`.
3. When running on Java 9 you need to additionally add the arguments in **java.option** in `$REPORTHOME/bin` to **Catalina.sh** in `$CATALINA_HOME/bin`.
4. Start Tomcat by running the script file **startup.sh**.
5. Access Logi Report Server using either URL:

   `http://hostname:8080/jreport/jrserver
   http://hostname:8080/jreport/jinfonet/index.jsp`

## Troubleshooting

If you run into problems when using Logi Report Server in Tomcat, you may have to send your log files of Logi Report Server to [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.):

1. Modify the **catalina.sh** file in `/opt/apache-tomcat/bin`, by adding `-Dlogall=true` after the report home definition:

   ```
   JAVA_OPTS="-Dreporthome=/opt/LogiReport/Server-Dlogall=true"  
   Cygwin=false
   ```

   Or if no report home is specified, add this:

   ```
   JAVA_OPTS=-Dlogall=true  
   Cygwin=false
   ```
2. Start Tomcat.
3. To get information about the Logi Report Server environment, you can access `http://hostname:8080/jreport/admin/info.jsp?cmd=info`.
4. Save the output to a file.
5. After reproducing the problem, send [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.) the log files in `reporthome/logs.`

   The Tomcat log files may also help to identify the problem. The most useful one is /opt/apache-tomcat/logs/catalina.out.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4420453448599/criticalicon.gif)In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: [Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751-Statement-on-Log4j-and-Log4net-Vulnerabilities "Read this article to mitigate or remove a Log4j vulnerability from your version of Logi Report.").

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690630551-Deploying-Server-to-WebLogic-14-1-1)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683909527-Deploying-Server-to-JBoss-EAP)
