---
title: "Deploying Server to GlassFish Server Open Source Edition 5.0"
id: 28891647778829
section: "Report Server Integration Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891647778829-Deploying-Server-to-GlassFish-Server-Open-Source-Edition-5-0
updated_at: 2026-02-26T02:13:20Z
source_host: docs-report.zendesk.com
---
# 
Deploying Server to GlassFish Server Open Source Edition 5.0 

This topic describes how you can deploy Report Server to GlassFish. 

We use paths based on UNIX path name protocol in our example. The instruction applies to both UNIX and Windows installation. However, the path formats differ. For Windows it is in this format C:\LogiReport\Server instead of /opt/LogiReport/Server. 

Assume that the Report Server WAR file jreport.war is in the /opt/LogiReport/Server/bin/distribute directory. To create the WAR file, see Building a WAR/EAR File to Include a Self-contained Report Server. 

To deploy Report Server to GlassFish Server Open Source Edition 5.0:

- Start GlassFish in the default domain1 and launch the Admin Console.

- Select the Applications node on the left.

- Select Deploy on the displayed page.

- Select Choose File to select the WAR file jreport.war. 

- Leave Application Name and Context Root as jreport and jreport. Then select OK.

- Expand the Deployment node on the left and you see a new node named jreport. Select it and then on the displayed page select Save.

- In the console tree, select Configuration. 

- Go to the JVM Settings tab and select JVM Options. 

- In the JVM Options section, select Add JVM Option, and then type -Djava.awt.headless=true. Select Save to save your changes.
    You need not add this JVM option if you are using Windows.     
  

- Restart GlassFish and start the application jreport. 

- Access Report Server using the following URLs:
    http://<hostname>:8080/jreport
    http://<hostname>:8080/jreport/jinfonet/index.jsp

## Troubleshooting

If you run into problems when using GlassFish, you may have to send the log files of Report Server to Customer Service. The following procedure illustrates how to generate the log files:

- Start GlassFish in the default domain1 and then launch the Admin Console.
  

- In the console tree, select Configuration.

- Go to the JVM Settings tab, and then select JVM Options.

- In the JVM Options section, select Add JVM Option, and then type -Dlogall=true. Select Save to save your changes.

- Restart GlassFish and try to reproduce the problem.

- After reproducing the problem, send Customer Service the log files in reporthome/logs.
  The GlassFish log file may also help to identify the problem. It is /opt/glassfish/domains/domain1/logs/server.log.
