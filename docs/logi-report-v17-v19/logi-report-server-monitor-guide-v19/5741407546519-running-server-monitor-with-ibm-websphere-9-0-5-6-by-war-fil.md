---
title: "Running Server Monitor with IBM WebSphere 9.0.5.6 by WAR File"
id: 5741407546519
section: "Logi Report Server Monitor Guide v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741407546519-Running-Server-Monitor-with-IBM-WebSphere-9-0-5-6-by-WAR-File
updated_at: 2022-10-31T17:15:40Z
---

# Running Server Monitor with IBM WebSphere 9.0.5.6 by WAR File

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741399542167-Running-Server-Monitor-with-Tomcat)

# Running Server Monitor with IBM WebSphere 9.0.5.6 by WAR File

This topic describes how you can run Server Monitor with IBM WebSphere 9.0.5.6 by a WAR File.

Assume that:

* You installed WebSphere 9.0.5.6 to `C:\WebSphere`.
* You installed Server Monitor to `C:\LogiReport\Monitor`.

Step 1: Generating the WAR file

Use the tool makewar.bat/makewar.sh to build the Server Monitor WAR file as defined by makewar.xml for remote integration. Both makewar.bat/makewar.sh and makewar.xml are in `C:\LogiReport\Monitor\bin`. Server Monitor generates the WAR file **monitor.war** to the directory `C:\LogiReport\Monitor\bin\distribute`.

Step 2: Deploying the WAR file

1. Start IBM WebSphere.
2. Open the **Administrative Console** using the Start menu, or using the URL `http://hostname:9080/ibm/console`, where the hostname is host name or IP address, and 9080 is the port number.

   ![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/9905614395415/criticalicon.gif)The user ID must contain only letters and numbers. You can use any of them as your user ID.
3. After you sign in, expand the **Applications** node in the left tree, and then select **New Application**.
4. Select **New Enterprise Application** on the right panel to install a new application.
5. Select **Local file system**.
6. Select **Browse** to choose your **monitor.war** file.
7. Select **Next**.
8. Select **Next**.
9. In Step 1, type **LogiReportMonitor** in the **Application Name** field.
10. Select **Next**.
11. Select **Next** for Step 2 and 3.
12. In Step 4, in the Context Root section, type **/monitor/**.
13. Select **Next**.
14. In Step 5, select **Finish**. The installing process may take several minutes. Please wait until the process is complete.
15. After the installation process is successfully completed, select **Save**.
16. On the left resource tree, expand **Servers**.
17. Go through **Server Types > WebSphere application servers** > **Server1** > **Process Definition** (in the Java and Process Management node of the Server Infrastructure section) > **Java Virtual Machine** (in the Additional Properties section).
18. Type **-Dmonitor.home=C:\LogiReport\Monitor** (Server Monitor installation folder) in Generic JVM arguments field in the Configuration tab.
19. Select **OK**.
20. Select **Save** in the Messages box.
21. Stop Websphere.
22. Copy **rmi.auth** from `<server_intall_root>\bin` to `C:\LogiReport\Monitor\bin`.
23. Enable RMI service for remote connection by setting the property `server.rmiserver.enable=true` in **server.properties** in `<server_intall_root>\bin`.
24. Start Logi Report Server.
25. Start WebSphere.
26. Access Server Monitor using the URL `http://hostname:9080/monitor` or `http://hostname:9080/monitor/monitor/index.jsp`.

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741399542167-Running-Server-Monitor-with-Tomcat)
