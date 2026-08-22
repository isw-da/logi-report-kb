---
title: "Integrating Remote Report Server with IBM WebSphere 9.0.0.7 by a WAR File"
id: 45204004507661
section: "Report Server Integration Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204004507661-Integrating-Remote-Report-Server-with-IBM-WebSphere-9-0-0-7-by-a-WAR-File
updated_at: 2026-04-30T14:10:22Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Integrating Remote Report Server With IBM WebSphere 9.0.0.7 by a WAR File 

This topic describes an example of using JSPs based on Remote Server APIs to integrate with IBM WebSphere 9.0.0.7.

Assume that:

- You installed WebSphere 9.0.0.7 in C:\WebSphere on computer A.

- You installed Report Server in C:\LogiReport\Server on computer B. The computer IP is 127.0.0.1.

The procedure for  integrating remote Report Server with IBM WebSphere contains the following major steps:

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

- On computer A, start IBM WebSphere.

- On computer B, access the WebSphere Administrative Console using the URL: http://hostname:9060/ibm/console, where hostname is computer A's host name or IP address, and 9060 is the port number.

- After you sign in, expand the Applications node, select Application Types and then Websphere enterprise applications.

- Select Install.

- Select Browse to select the remote.war file, and then select Next.

- Keep selecting Next until you see the requirement for specifying context root.

- In the Context Root field, type a context path such as /remote/, then select Next.

- Select Finish in the Summary page. The installing process may take several minutes, wait until the process is completed.

- Select Save.

- Select remote.war and then select Start.

- Access Report Server using the following URL:
      http://hostname:9080/remote/jinfonet/default.jsp

Here hostname is computer A's host name or IP address.
