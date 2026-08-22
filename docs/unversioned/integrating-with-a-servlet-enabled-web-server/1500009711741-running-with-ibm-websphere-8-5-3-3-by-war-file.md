---
title: "Running with IBM WebSphere 8.5.3.3 by WAR File"
id: 1500009711741
section: "Integrating With a Servlet-Enabled Web Server"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009711741-Running-with-IBM-WebSphere-8-5-3-3-by-WAR-File
updated_at: 2021-11-03T06:58:39Z
---

# Running with IBM WebSphere 8.5.3.3 by WAR File

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412139637143/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009685842-Running-with-Tomcat-8-0-15)

# Running With IBM WebSphere 8.5.3.3 by WAR File

This topic describes how to run Logi JReport Server Monitor with IBM WebSphere 8.5.3.3 by WAR File.

Assume that:

* WebSphere 8.5.3.3 has been installed to `C:\WebSphere`.
* Logi JReport Server Monitor has been installed to `C:\Logi JReport\Monitor`.

## Generating the WAR File

Use the tool makewar.bat/makewar.sh to build the Logi JReport Server Monitor WAR file as defined by makewar.xml for remote integration. Both makewar.bat/makewar.sh and makewar.xml are located in `C:\Logi JReport\Monitor\bin`. The generated WAR file monitor.war will be saved to the directory `C:\Logi JReport\Monitor\bin\distribute`.

## Deploying the WAR File

To integrate Logi JReport Server Monitor with IBM WebSphere by a WAR file, take the following steps:

1. Start IBM WebSphere.
2. Open the **Administrative Console**. You can open the Administrative Console using the Start menu, or using the URL `http://hostname:9080/ibm/console`, where the hostname is host name or IP address, and 9080 is the port number. Note that the user ID must contain only letters and numbers. You can use any of them as your user ID.
3. After successfully logging in, expand the **Applications** node in the left tree, and then select **New Application**.
4. Select **New Enterprise Application** on the right panel to install a new application.
5. Select **Local file system** , and then use **Browse** to select your monitor.war file. Then select **Next**.
6. Select **Next**.
7. In Step1, type **JReportMonitor** in the Application Name field, and then select **Next**.
8. Select **Next** for Step 2 and 3.
9. In Step 4, in the Context Root section, type **/monitor/**, and then select **Next**.
10. In Step 5, select **Finish**. The installing process may take several minutes. Please wait until the process is complete.
11. After the installation process has been successfully completed, select **Save**.
12. On the left resource tree, expand **Servers**, go through **Server Types > WebSphere application servers** > **Server1** > **Process Definition** (in the Java and Process Management node of the Server Infrastructure section) > **Java Virtual Machine** (in the Additional Properties section), and type **-Dmonitor.home=C:\Logi JReport\Monitor** (Logi JReport Server Monitor installation folder) in Generic JVM arguments field in the Configuration tab.
13. Select **OK**, then select **Save** in the Messages box. Then stop Websphere.
14. Copy rmi.auth from `<server_intall_root>\bin` to `C:\Logi JReport\Monitor\bin`. Enable RMI service for remote connection by setting the property `server.rmiserver.enable=true` in server.properties in `<server_intall_root>\bin`. Then start Logi JReport Server.
15. Start WebSphere.
16. Access Logi JReport Server Monitor using the URL `http://hostname:9080/monitor` or `http://hostname:9080/monitor/monitor/index.jsp`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412139637143/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009685842-Running-with-Tomcat-8-0-15)
