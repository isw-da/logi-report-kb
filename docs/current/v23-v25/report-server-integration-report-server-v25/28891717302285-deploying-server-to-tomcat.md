---
title: "Deploying Server to Tomcat"
id: 28891717302285
section: "Report Server Integration Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891717302285-Deploying-Server-to-Tomcat
updated_at: 2026-02-26T02:13:20Z
source_host: docs-report.zendesk.com
---
# 
Deploying Server to Tomcat 9.0.70

This topic describes how you can deploy Report Server to Tomcat 9.0.70.

- 
Report Server now supports Tomcat 10.Add -Djakartaee=true when make war for Tomcat 10/11.

We use paths based on UNIX path name protocol in our example. The instruction applies to both UNIX and Windows installation. However, the path formats differ. For Windows it is in this format C:\LogiReport\Server instead of /opt/LogiReport/Server. 

Assume that:

- You installed Tomcat 9.0.70 in the /opt/apache-tomcat directory.

- The Report Server WAR file jreport.war is in the /opt/LogiReport/Server/bin/distribute directory. To create the WAR file, see Building a WAR/EAR File to Include a Self-contained Report Server.
     When you set unpackWARs="false" in server.xml in the conf folder of Tomcat, you need to do the following: 

- Modify the LogConfig.properties file in /opt/LogiReport/Server/bin before you create the WAR:
      
- Remove the code packages = com.jinfonet.util.

- Replace JRRollingFileAppender with RollingFile in the file. 

- Replace JRPatternLayout with PatternLayout in the file. 

-  Add the -Djbossas7=true parameter when launching makewar.bat/.sh to build the WAR. 
     

makewar.bat -Djbossas7=true

- Move log4j-api-2.17.2.jar and log4j-core-2.17.2.jar from jreport.war > WEB-INF > lib to the lib folder of Tomcat. See the note concerning Log4J Vulnerability.

To deploy Report Server to Tomcat 9.0.70:

- Shut down Tomcat.

- Copy jreport.war to /opt/apache-tomcat/webapps. 

- When running on Java 9 you need to additionally add the arguments in java.option in $REPORTHOME/bin to Catalina.sh in $CATALINA_HOME/bin.

- Start Tomcat by running the script file startup.sh. 

- Access Report Server using either URL:
    http://hostname:8080/jreport/jrserver
       http://hostname:8080/jreport/jinfonet/index.jsp

## Troubleshooting

If you run into problems when using Report Server in Tomcat, you may have to send your log files of Report Server to Customer Service: 

- Modify the catalina.sh file in /opt/apache-tomcat/bin, by adding -Dlogall=true after the report home definition:

JAVA_OPTS="-Dreporthome=/opt/LogiReport/Server-Dlogall=true"
Cygwin=false
Or if no report home is specified, add this:

JAVA_OPTS=-Dlogall=true
Cygwin=false

- Start Tomcat.

- To get information about the Report Server environment, you can access http://hostname:8080/jreport/admin/info.jsp?cmd=info.

- Save the output to a file.

- After reproducing the problem, send Customer Service the log files in reporthome/logs.The Tomcat log files may also help to identify the problem. The most useful one is /opt/apache-tomcat/logs/catalina.out.

### 
Log4J Vulnerability Notice

In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, see Statement on Log4j and Log4Net Vulnerabilities.
