---
title: "Integrating Remote Report Server with WebLogic 14.1.1 by a WAR File"
id: 45204012328077
section: "Report Server Integration Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204012328077-Integrating-Remote-Report-Server-with-WebLogic-14-1-1-by-a-WAR-File
updated_at: 2026-04-30T14:10:21Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Integrating Remote Report Server With WebLogic 14.1.1 by a WAR File

This topic describes an example of using JSPs based on Remote Server APIs to integrate with WebLogic 14.1.1.

Assume that:

- You installed WebLogic in C:\bea on computer A.

- You installed Report Server in C:\LogiReport\Server on computer B. The computer IP is 127.0.0.1.

The procedure for  integrating remote Report Server with WebLogic contains the following major steps:

- Generate the WAR file

- Configure Report Server

- Deploy the WAR file

Step 1: Generate the WAR file

- On computer B, use the tool makewar.bat to build the Report Server WAR file as defined by makewar.xml for remote integration. Both makewar.bat and makewar.xml are in C:\LogiReport\Server\bin. Run the following commands in DOS window and Server saves the generated WAR file remote.war to the directory C:\LogiReport\Server\bin\distribute. 
    makewar.bat buildRemoteWar -Djrs.remote.host=127.0.0.1 -Djrs.remote.rmiport=1129 -Djrs.rmi.auth_file=C:\LogiReport\Server\bin\rmi.auth

- Copy the rmi.auth file from C:\LogiReport\Server\bin on computer B to C:\LogiReport\Server\bin on computer A.

Step 2: Configure Report Server

- Make sure you have started Report Server at least once so that Server generated the server.properties file.

- Change the server.properties file in C:\LogiReport\Server\bin:
    server.rmiserver.enable=true 
    server.rmiadminservice.enable=true

Step 3: Deploy the WAR file

- If you have not already created a WebLogic Domain for Report Server, you must create one before starting the integration.

- On computer A, start WebLogic by running startWeblogic.sh in C:\bea\user_projects\domains\domain_name\bin.

- On computer B, access the WebLogic Administrative Console using the URL http://hostname:7001/console/, where hostname is computer A's host name or IP address, and 7001 is the port number.

- After you sign in, in the Domain Structure panel on the left, select Deployments node.

- In the Summary of Deployments panel, select Install.

- In the Install Application Assistant panel, select the upload your file(s) link.

- In the Deployment Archive section, select Browse to select the remote.war file in C:\LogiReport\Server\bin\distribute, and then select Next.

- Keep selecting Next until the Finish button is enabled, and then select Finish. 

- Start Report Server on computer B. 

- Go to computer A and access Report Server using the following URL:
    http://localhost:7001/remote/
