---
title: "Running with WebLogic 12c Release 1 (12.1.2)"
id: 1500009685862
section: "Integrating With a Servlet-Enabled Web Server"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009685862-Running-with-WebLogic-12c-Release-1-12-1-2
updated_at: 2021-11-03T06:58:39Z
---

# Running with WebLogic 12c Release 1 (12.1.2)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412139637143/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009711721-Integrating-with-a-Servlet-enabled-Web-Server)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139637399/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009685842-Running-with-Tomcat-8-0-15)

# Running With WebLogic 12c Release 1 (12.1.2)

This topic describes how to run Logi JReport Server Monitor with WebLogic 12c Release 1 (12.1.2).

Assume that:

* WebLogic 12c Release 1 (12.1.2) has been installed in `D:\bea`.
* Logi JReport Server Monitor has been installed in `C:\Logi JReport\Monitor`.

## Generating the WAR File

Use the tool makewar.bat/makewar.sh to build the Logi JReport Server Monitor WAR file as defined by makewar.xml for remote integration. Both makewar.bat/makewar.sh and makewar.xml are located in `C:\Logi JReport\Monitor\bin`. The generated WAR file monitor.war will be saved to the directory `C:\Logi JReport\Monitor\bin\distribute`.

## Deploying the WAR File

1. If you have not already created a WebLogic Domain for Logi JReport Server you must create one before starting the integration.
2. Start WebLogic by running startWeblogic.cmd in `D:\bea\user_projects\domains\domain_name\bin`.
3. Access the WebLogic Administrative Console using the URL `http://hostname:7001/console/`, where the hostname is host name or IP address, and 7001 is the port number.
4. After your successful login, in the Domain Structure panel on the left, select **Deployments** node.
5. In the Summary of Deployments panel, select **Install**.
6. In the Install Application Assistant panel, select the **upload your file(s)** link.
7. In the Deployment Archive section, select **Browse** to select your monitor.war file, and then select **Next**.
8. Keep selecting **Next** until the Finish button is enabled, and then select **Finish**.
9. In `D:\bea\user_projects\domains\domain_name\bin`, edit the file startWebLogic.cmd by adding a line: `set JAVA_OPTIONS="-Dmonitor.home=C:\Logi JReport\Monitor"`.
10. Copy rmi.auth from `<server_intall_root>\bin` to `C:\Logi JReport\Monitor\bin`. Enable RMI service for remote connection by setting the property `server.rmiserver.enable=true` in server.properties in `<server_intall_root>\bin`. Then start Logi JReport Server.
11. Access the Server Monitor from a web browser (the default port of WebLogic is 7001) using the URL `http://hostname:7001/monitor` or `http://hostname:7001/monitor/monitor/index.jsp`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412139637143/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009711721-Integrating-with-a-Servlet-enabled-Web-Server)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139637399/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009685842-Running-with-Tomcat-8-0-15)
