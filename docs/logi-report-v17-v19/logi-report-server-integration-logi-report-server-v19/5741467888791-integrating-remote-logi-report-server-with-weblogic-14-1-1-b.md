---
title: "Integrating Remote Logi Report Server with WebLogic 14.1.1 by a WAR File"
id: 5741467888791
section: "Logi Report Server Integration Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741467888791-Integrating-Remote-Logi-Report-Server-with-WebLogic-14-1-1-by-a-WAR-File
updated_at: 2022-10-31T17:17:58Z
---

# Integrating Remote Logi Report Server with WebLogic 14.1.1 by a WAR File

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741437761815-Integrating-Remote-Logi-Report-Server-with-IBM-WebSphere-9-0-0-7-by-a-WAR-File)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741461315351-Seamless-Integrated-Security-Solution)

# Integrating Remote Logi Report Server With WebLogic 14.1.1 by a WAR File

This topic describes an example of using JSPs based on Remote Server APIs to integrate with WebLogic 14.1.1.

Assume that:

* You installed WebLogic in `C:\bea` on computer A.
* You installed Logi Report Server in `C:\LogiReport\Server` on computer B. The computer IP is 127.0.0.1.

The procedure for integrating remote Logi Report Server with WebLogic contains the following major steps:

1. [Generate the WAR file](#Generate)
2. [Configure Logi Report Server](#Config)
3. [Deploy the WAR file](#Deploy)

**Step 1: Generate the WAR file**

1. On computer B, use the tool **makewar.bat** to build the Logi Report Server WAR file as defined by makewar.xml for remote integration. Both makewar.bat and makewar.xml are in `C:\LogiReport\Server\bin`. Run the following commands in DOS window and Server saves the generated WAR file **remote.war** to the directory `C:\LogiReport\Server\bin\distribute`.

   `makewar.bat buildRemoteWar -Djrs.remote.host=127.0.0.1 -Djrs.remote.rmiport=1129 -Djrs.rmi.auth_file=C:\LogiReport\Server\bin\rmi.auth`
2. Copy the **rmi.auth** file from `C:\LogiReport\Server\bin` on computer B to `C:\LogiReport\Server\bin` on computer A.

**Step 2: Configure Logi Report Server**

1. Make sure you have started Logi Report Server at least once so that Server generated the server.properties file.
2. Change the **server.properties** file in `C:\LogiReport\Server\bin`:

   `server.rmiserver.enable=true   
    server.rmiadminservice.enable=true`

**Step 3: Deploy the WAR file**

1. If you have not already created a WebLogic Domain for Logi Report Server, you must create one before starting the integration.
2. On computer A, start WebLogic by running **startWeblogic.sh** in `C:\bea\user_projects\domains\domain_name\bin`.
3. On computer B, access the WebLogic Administrative Console using the URL `http://hostname:7001/console/`, where **hostname** is computer A's host name or IP address, and 7001 is the port number.
4. After you sign in, in the Domain Structure panel on the left, select **Deployments** node.
5. In the Summary of Deployments panel, select **Install**.
6. In the Install Application Assistant panel, select the **upload your file(s)** link.
7. In the Deployment Archive section, select **Browse** to select the **remote.war** file in `C:\LogiReport\Server\bin\distribute`, and then select **Next**.
8. Keep selecting **Next** until the Finish button is enabled, and then select **Finish**.
9. Start Logi Report Server on computer B.
10. Go to computer A and access Logi Report Server using the following URL:

    `http://localhost:7001/remote/`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741437761815-Integrating-Remote-Logi-Report-Server-with-IBM-WebSphere-9-0-0-7-by-a-WAR-File)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741461315351-Seamless-Integrated-Security-Solution)
