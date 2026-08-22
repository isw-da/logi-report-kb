---
title: "Running Server Monitor with WebLogic 14.1.1"
id: 4405690461463
section: "Logi Report Server Monitor Guide v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690461463-Running-Server-Monitor-with-WebLogic-14-1-1
updated_at: 2022-01-27T07:58:26Z
---

# Running Server Monitor with WebLogic 14.1.1

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690460567-Integrating-Server-Monitor-with-a-Servlet-Enabled-Web-Server)   [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683528215-Running-Server-Monitor-with-Tomcat)

# Running Server Monitor with WebLogic 14.1.1

This topic describes how you can run Server Monitor with WebLogic 14.1.1.

Assume that:

* You installed WebLogic 14.1.1 to `D:\bea`.
* You installed Server Monitor to `C:\LogiReport\Monitor`.

Step 1: Generating the WAR file

Use the tool makewar.bat/makewar.sh to build the Server Monitor WAR file as defined by makewar.xml for remote integration. Both makewar.bat/makewar.sh and makewar.xml are in `C:\LogiReport\Monitor\bin`. Server Monitor generates the WAR file **monitor.war** to the directory `C:\LogiReport\Monitor\bin\distribute`.

Step 2: Deploying the WAR file

1. If you have not already created a WebLogic Domain for Logi Report Server, you must create one before starting the integration.
2. Start WebLogic by running startWeblogic.cmd in `D:\bea\user_projects\domains\domain_name\bin`.
3. Access the WebLogic Administrative Console using the URL `http://hostname:7001/console/`, where the hostname is host name or IP address, and 7001 is the port number.
4. After you sign in, in the Domain Structure panel on the left, select **Deployments**.
5. In the Summary of Deployments panel, select **Install**.
6. In the Install Application Assistant panel, select **upload your file(s)**.
7. In the Deployment Archive section, select **Browse** to select your **monitor.war** file.
8. Select **Next**.
9. Keep selecting **Next** until the Finish button is enabled.
10. Select **Finish**.
11. In `D:\bea\user_projects\domains\domain_name\bin`, edit the file **startWebLogic.cmd** by adding a line: `set JAVA_OPTIONS="-Dmonitor.home=C:\LogiReport\Monitor"`.
12. Copy **rmi.auth** from `<server_intall_root>\bin` to `C:\LogiReport\Monitor\bin`.
13. Enable RMI service for remote connection by setting the property `server.rmiserver.enable=true` in **server.properties** in `<server_intall_root>\bin`.
14. Start Logi Report Server.
15. Access Server Monitor from a web browser (the default port of WebLogic is 7001) using the URL `http://hostname:7001/monitor` or `http://hostname:7001/monitor/monitor/index.jsp`.

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690460567-Integrating-Server-Monitor-with-a-Servlet-Enabled-Web-Server)   [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683528215-Running-Server-Monitor-with-Tomcat)
