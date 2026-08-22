---
title: "Running Server Monitor with WebLogic 14.1.1"
id: 28891515853837
section: "Report Server Monitor Guide v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891515853837-Running-Server-Monitor-with-WebLogic-14-1-1
updated_at: 2026-02-26T02:10:54Z
source_host: docs-report.zendesk.com
---
# 
Running Server Monitor with WebLogic 14.1.1

This topic describes how you can run Server Monitor with WebLogic 14.1.1.

Assume that:

- You installed WebLogic 14.1.1 to D:\bea.

- You installed Server Monitor to C:\LogiReport\Monitor.

Step 1: Generating the WAR file

Use the tool makewar.bat/makewar.sh to build the Server Monitor WAR file as defined by makewar.xml for remote integration. Both makewar.bat/makewar.sh and makewar.xml are in C:\LogiReport\Monitor\bin. Server Monitor generates the WAR file monitor.war to the directory C:\LogiReport\Monitor\bin\distribute.

Step 2: Deploying the WAR file

- If you have not already created a WebLogic Domain for Report Server, you must create one before starting the integration.

- Start WebLogic by running startWeblogic.cmd in D:\bea\user_projects\domains\domain_name\bin.

- Access the WebLogic Administrative Console using the URL http://hostname:7001/console/, where the hostname is host name or IP address, and 7001 is the port number.

- After you sign in, in the Domain Structure panel on the left, select Deployments.

- In the Summary of Deployments panel, select Install.

- In the Install Application Assistant panel, select upload your file(s).

- In the Deployment Archive section, select Browse to select your monitor.war file.

- Select Next.

- Keep selecting Next until the Finish button is enabled.

- Select Finish. 

- In D:\bea\user_projects\domains\domain_name\bin, edit the file startWebLogic.cmd by adding a line: set JAVA_OPTIONS="-Dmonitor.home=C:\LogiReport\Monitor".

- Copy rmi.auth from <server_intall_root>\bin to C:\LogiReport\Monitor\bin. 

- Enable RMI service for remote connection by setting the property server.rmiserver.enable=true in server.properties in <server_intall_root>\bin. 

- Start Report Server.

- Access Server Monitor from a web browser (the default port of WebLogic is 7001) using the URL http://hostname:7001/monitor or http://hostname:7001/monitor/monitor/index.jsp.
