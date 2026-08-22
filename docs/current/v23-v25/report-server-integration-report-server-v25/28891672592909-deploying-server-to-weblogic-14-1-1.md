---
title: "Deploying Server to WebLogic 14.1.1"
id: 28891672592909
section: "Report Server Integration Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891672592909-Deploying-Server-to-WebLogic-14-1-1
updated_at: 2026-02-26T02:13:20Z
source_host: docs-report.zendesk.com
---
# 
Deploying Server to WebLogic 14.1.1

This topic describes how you can deploy Report Server to WebLogic. 

We use paths based on UNIX path name protocol in our example. The instruction applies to both UNIX and Windows installation. However, the path formats differ. For Windows it is in this format C:\LogiReport\Server instead of /opt/LogiReport/Server. 

Assume that:

- You installed WebLogic 14.1.1 in the /opt/bea directory. This is BEA_HOME in the WebLogic documentation. 

- The Report Server WAR file jreport.war is in the /opt/LogiReport/Server/bin/distribute directory. To create the WAR file, see Building a WAR/EAR File to Include a Self-contained Report Server. 

To deploy Report Server to BEA WebLogic:

- If you have not already created a WebLogic Domain for Report Server, you must create one before starting the integration.

- Start WebLogic by running startWeblogic.sh in /opt/bea/user_projects/domains/domain_name/bin.

- Access the WebLogic Administrative Console using the URL http://hostname:7001/console/, where hostname is host name or IP address, and 7001 is the port number.

- After you sign in, in the Domain Structure panel on the left, select Deployments node.

- In the Summary of Deployments panel, select Install.

- In the Install Application Assistant panel, select upload your file(s).

- In the Deployment Archive section, select Browse to select the jreport.war file in C:\LogiReport\Server\bin\distribute, and then select Next.

- Keep selecting Next until the Finish button is enabled, and then select Finish. 

- Start Report Server and then access it using the following URL:
    http://localhost:7001/jreport/

## Troubleshooting

If you run into problems when using Report Server in BEA WebLogic, you may have to send the log files of Report Server to Customer Service. The following procedure illustrates how to generate the log files:

- Add -Dlogall=true on the same line as -Dreporthome in the startWebLogic.sh shell script. 

- Restart the application server

- Try to reproduce the problem. After reproducing the problem, send Customer Service the log files in reporthome/logs.
      The WebLogic log file may also help to identify the problem. It is /opt/bea/user_projects/domains/domain_name/logs.
