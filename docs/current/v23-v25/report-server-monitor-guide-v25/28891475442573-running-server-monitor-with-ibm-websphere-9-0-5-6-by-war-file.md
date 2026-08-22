---
title: "Running Server Monitor with IBM WebSphere 9.0.5.6 by WAR File"
id: 28891475442573
section: "Report Server Monitor Guide v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891475442573-Running-Server-Monitor-with-IBM-WebSphere-9-0-5-6-by-WAR-File
updated_at: 2026-02-26T02:10:54Z
source_host: docs-report.zendesk.com
---
# 
Running Server Monitor with IBM WebSphere 9.0.5.6 by WAR File

This topic describes how you can run Server Monitor with IBM WebSphere 9.0.5.6 by a WAR File.

Assume that:

- You installed WebSphere 9.0.5.6 to C:\WebSphere.
  

- You installed Server Monitor to C:\LogiReport\Monitor.

Step 1: Generating the WAR file

Use the tool makewar.bat/makewar.sh to build the  Server Monitor WAR file as defined by makewar.xml for remote integration. Both makewar.bat/makewar.sh and makewar.xml are in C:\LogiReport\Monitor\bin. Server Monitor generates the WAR file monitor.war to the directory C:\LogiReport\Monitor\bin\distribute.

Step 2: Deploying the WAR file

- Start IBM WebSphere.

- Open the Administrative Console using the Start menu, or using the URL http://hostname:9080/ibm/console, where the hostname is host name or IP address, and 9080 is the port number. The user ID must contain only letters and numbers. You can use any of them as your user ID.

- After you sign in, expand the Applications node in the left tree, and then select New Application.

-  Select New Enterprise Application on the right panel to install a new application. 

- Select Local file system. 

- Select Browse to choose your monitor.war file. 

- Select Next.

- Select Next.

- In Step 1, type LogiReportMonitor in the Application Name field. 

- Select Next.

- Select Next for Step 2 and 3.

- In Step 4, in the Context Root section, type /monitor/.

- Select Next.

- In Step 5, select Finish. The installing process may take several minutes. Please wait until the process is complete.

- After the installation process is successfully completed, select Save.

- On the left resource tree, expand Servers.

- Go through Server Types > WebSphere application servers > Server1 > Process Definition (in the Java and Process Management node of the Server Infrastructure section) > Java Virtual Machine (in the Additional Properties section).

- Type -Dmonitor.home=C:\LogiReport\Monitor (Server Monitor installation folder) in Generic JVM arguments field in the Configuration tab.

- Select OK.

- Select Save in the Messages box.

- Stop Websphere. 

- Copy rmi.auth from <server_intall_root>\bin to C:\LogiReport\Monitor\bin. 

- Enable RMI service for remote connection by setting the property server.rmiserver.enable=true in server.properties in <server_intall_root>\bin. 

- Start Report Server.

- Start WebSphere.

- Access  Server Monitor using the URL http://hostname:9080/monitor or http://hostname:9080/monitor/monitor/index.jsp.
