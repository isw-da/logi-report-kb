---
title: "Deploying Server to JBoss EAP"
id: 28891701216141
section: "Report Server Integration Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891701216141-Deploying-Server-to-JBoss-EAP
updated_at: 2026-02-26T02:13:19Z
source_host: docs-report.zendesk.com
---
# 
Deploying Server to JBoss EAP 7.4.0

This topic describes how you can deploy Report Server to JBoss EAP 7.4.0. 

We use paths based on UNIX path name protocol in our example. The instruction applies to both UNIX and Windows installation. However, the path formats differ. For Windows it is in this format C:\LogiReport\Server instead of /opt/LogiReport/Server. 

Assumed that:

- You installed JBoss EAP 7.4.0 in the /opt/JBossEAP directory.

- The Report Server WAR file jreport.war is in the /opt/LogiReport/Server/bin/distribute directory. To create the WAR file, see Building a WAR/EAR File to Include a Self-contained Report Server.  
     Before creating the WAR, you need to change JRPatternLayout to PatternLayout all over the LogConfig.properties file in /opt/LogiReport/Server/bin. After you generate jreport.war, create a file named jboss-deployment-structure.xml in the jreport.war/META-INF folder:

<?xml version="1.0" encoding="UTF-8"?>
    <jboss-deployment-structure xmlns="urn:jboss:deployment-structure:1.1"> 
        <deployment> 
            <dependencies>
                <system export="true">
                    <paths>
                        <path name="org/w3c/dom/css"/>
                    </paths>
                </system>
            </dependencies>
        <exclusions>
            <module name="org.apache.logging.log4j.api"/>
         <module name="org.slf4j" />
            <module name="org.slf4j.impl" />
        </exclusions>
        </deployment>
    </jboss-deployment-structure>

To deploy Report Server to JBoss EAP 7.4.0:

- To avoid the problem that JBoss EAP 7 cannot locate jrenv.jar, when you build a WAR/EAR to deploy to JBoss EAP 7, add -Djbossas7=true in makewar.bat/sh like this: 
    

- Start JBoss by running the standalone.sh script. 

- Add a management user to JBoss EAP 7 by running the add-user.sh script. 

- Access the JBoss Management Console to deploy jreport.war and enable it. 
    

- Access Report Server using the following URLs:
    http://localhost:8080/jreport/jrserver
    
    http://localhost:8080/jreport/jinfonet/index.jsp

## Troubleshooting

If you run into problems when using Report Server in JBoss, you may have to send the log files of Report Server to Customer Service. The following procedure illustrates how to generate the log files: 

- Modify the standalone.conf file in /opt/JBossEAP/bin to add -Dlogall=true. 
    

- Start JBoss using the modified file standalone.conf. 

- After you reproduce the problem, send Customer Service the log files in reporthome/logs.
    The JBoss log files may also help to identify the problem. The most useful one is /opt/jbosseap/standalone/log/server.log.
