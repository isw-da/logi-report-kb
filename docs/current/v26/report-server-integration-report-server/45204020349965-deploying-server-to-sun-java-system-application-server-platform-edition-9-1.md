---
title: "Deploying Server to Sun Java™ System Application Server Platform Edition 9.1"
id: 45204020349965
section: "Report Server Integration Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204020349965-Deploying-Server-to-Sun-Java-System-Application-Server-Platform-Edition-9-1
updated_at: 2026-04-30T14:10:20Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Deploying Server to Sun Java™ System Application Server Platform Edition 9.1 

This topic describes how you can deploy Report Server to Sun Java™ System Application Server Platform Edition. 

We use paths based on UNIX path name protocol in our example. The instruction applies to both UNIX and Windows installation. However, the path formats differ. For Windows it is in this format C:\LogiReport\Server instead of /opt/LogiReport/Server. 

Assume that:

- You installed Sun Java™ System Application Server Platform Edition 9.1 in the C:\Sun\AppServer directory. 

- The Report Server WAR file jreport.war is in the C:\LogiReport\Server\bin\distribute directory. To create the WAR file, see Building a WAR/EAR File to Include a Self-contained Report Server. 

To deploy Report Server to Sun Java™ System Application Server Platform Edition 9.1:

- Update Sun Application Server's Derby jars using the lib folder in C:\LogiReport\Server\derby to replace the lib folder in C:\Sun\AppServer\javadb\lib.

- Start the Sun Application Server by selecting Start > Programs > Sun Microsystems > Application Server PE > Start Default Server.

- Launch the Admin Console by selecting Start > Programs > Sun Microsystems > Application Server PE > Admin Console.

- In the left console tree, expand the Applications node, then select Web Applications.

- In the Web Applications page, select Deploy.

- Select the radio button before Local packaged file or directory that is accessible from the Application Server, then select Browse Files to select the WAR file jreport.war.

- Select OK. You will find a new application jreport.

- Access Report Server using the following URLs:
    http://<hostname>:8080/jreport/jrserver
    http://<hostname>:8080/jreport/jinfonet/index.jsp
    

## Troubleshooting

If you run into problems when using the Sun Application Server, you may have to send the log files of Report Server to Customer Service. The following procedure illustrates how to generate the log files:

- Start the Sun Application Server.

- Launch the Admin Console.  

- In the console tree, select Application Server. 

- Go to the JVM Settings tab, and then select JVM Options. 

- In the JVM Option field, select Add JVM Option, and then type -Dlogall=true. 

- Select Save to save your changes.

- Restart Sun Application Server and try to reproduce the problem.

- After reproducing the problem, send Customer Service the log files in reporthome/logs.
