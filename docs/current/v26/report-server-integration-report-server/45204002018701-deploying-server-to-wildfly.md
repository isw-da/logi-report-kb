---
title: "Deploying Server to WildFly"
id: 45204002018701
section: "Report Server Integration Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204002018701-Deploying-Server-to-WildFly
updated_at: 2026-04-30T14:10:21Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Deploying Server to WildFly 26.1.2

This topic describes how you can deploy Report Server to WildFly 26.1.2.

We use paths based on UNIX path name protocol in our example. The instruction applies to both UNIX and Windows installation. However, the path formats differ. For Windows it is in this format C:\LogiReport\Server instead of /opt/LogiReport/Server. 

Assume that:

- You installed WildFly 26.1.2 in the /opt/wildfly directory.

- The Report Server WAR file jreport.war is in the /opt/LogiReport/Server/bin/distribute folder. To create the WAR file, see Building a WAR/EAR File to Include a Self-contained Report Server. 
     Before creating the WAR, you need to change JRPatternLayout to PatternLayout all over the LogConfig.properties file in /opt/LogiReport/Server/bin. After you generate jreport.war, create a file named jboss-deployment-structure.xml in the jreport.war/META-INF folder with the contents:

<?xml version="1.0" encoding="UTF-8"?>
    <jboss-deployment-structure> 
        <deployment> 
            <exclusions>
                <module name="org.apache.logging.log4j.api"/>
             <module name="org.slf4j" />
                <module name="org.slf4j.impl" />
            </exclusions>
        </deployment>
    </jboss-deployment-structure>

To deploy Report Server to WildFly 26.1.2:

- Start WildFly by running the standalone.sh script in /opt/wildfly/bin. 

- By default, WildFly is distributed with security enabled for the management interface. It means that before you access the Administration Console you need to add a new user. You can achieve this using the add-user.sh script in the bin folder. Set the username and password for the new user. 

- Sign in to the WildFly Administration Console with the specified username and password using the URL http://localhost:9990/console. 

- In the Deployments tab, select Add. 

- In the Create Deployment dialog box, browse to select the jreport.war file. 

- Select Next. 

- In the step 2 of the Create Deployment dialog box, select Enable.

- Select Save. 

- Upon the successful deployment of the Report Server WAR file jreport.war, access Report Server using the following URL:
    http://localhost:8080/jreport/jrserver
    
http://localhost:8080/jreport/jinfonet/index.jsp

 Server does not support WildFly 27.0.0.0 or above.

 If you are launching a WildFly instance on SE 17 and aren't using a bootable jar or WildFly launch scripts, you need to add all the content in java.option in /opt/LogiReport/Server/bin into the standalone.conf file in /opt/wildfly/bin as follows. For each line in java.option, add it into standalone.conf using this format: JAVA_OPTS="$JAVA_OPTS Each_Line_Content", for example, JAVA_OPTS="$JAVA_OPTS --illegal-access=permit".

## Troubleshooting

If you run into problems when using Report Server in WildFly, you may have to send the log files of Report Server to Customer Service. The following procedure illustrates how to generate the log files: 

- Modify the standalone.sh file in /opt/wildfly/bin, by adding -Dlogall=true after the reporthome definition: 
    "$JAVA" $JAVA_OPTS \ -classpath "$WILDFLY_CLASSPATH" -Dreporthome=/opt/LogiReport/Server \ -Dlogall=true \ org.wildfly.Main "$@"

- Start WildFly using the modified standalone.sh. 

- After reproducing the problem, send Customer Service the log files in reporthome/logs.
    The WildFly log files may also help identify the problem. The most useful one is /opt/wildfly/server/default/log/server.log.

 If you encounter the problem that WildFly cannot locate jrenv.jar when you are deploying a WAR/EAR to WildFly, add -Djbossas7=true in makewar.bat/sh.
