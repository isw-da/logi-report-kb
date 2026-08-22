---
title: "Integrating Remote Logi Report Server with WebLogic 12c (12.2.1.3.0) by a WAR File"
id: 1500009749801
section: "Logi Report Server Integration, Server Cluster, and Server Security Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009749801-Integrating-Remote-Logi-Report-Server-with-WebLogic-12c-12-2-1-3-0-by-a-WAR-File
updated_at: 2021-07-25T07:19:02Z
---

# Integrating Remote Logi Report Server with WebLogic 12c (12.2.1.3.0) by a WAR File

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749821-Integrating-Remote-Logi-Report-Server-with-IBM-WebSphere-9-0-0-7-by-a-WAR-File)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009722882-Seamless-Integrated-Security-Solution)

# Integrating Remote Logi Report Server With WebLogic 12c (12.2.1.3.0) by a WAR File

Here is an example illustrating the case of using JSPs based on Remote Server APIs to integrate with WebLogic 12c (12.2.1.3.0).

It is assumed that:

* WebLogic is installed in `C:\bea` in computer A.
* Logi Report Server is installed in `C:\LogiReport\Server` in computer B. The computer IP is 127.0.0.1.

The procedure for integrating remote Logi Report Server with WebLogic contains the following major steps:

1. [Generate the WAR file](#Generate)
2. [Configure Logi Report Server](#Config)
3. [Deploy the WAR file](#Deploy)

**Step 1: Generating the WAR file**

1. In computer B, use the tool makewar.bat to build the Logi Report Server WAR file as defined by makewar.xml for remote integration. Both makewar.bat and makewar.xml are located in `C:\LogiReport\Server\bin`. Run the following commands in DOS window and the generated WAR file remote.war will be saved to the directory `C:\LogiReport\Server\bin\distribute`.

   `makewar.bat buildRemoteWar -Djrs.remote.host=127.0.0.1 -Djrs.remote.rmiport=1129 -Djrs.rmi.auth_file=C:\LogiReport\Server\bin\rmi.auth`
2. Copy the rmi.auth file from `C:\LogiReport\Server\bin` in computer B to `C:\LogiReport\Server\bin` in computer A.

**Step 2: Configuring Logi Report Server**

1. Make sure Logi Report Server has been started once so that the server.properties file is generated.
2. Change server.properties file in `C:\LogiReport\Server\bin` as follows:

   `server.rmiserver.enable=true   
    server.rmiadminservice.enable=true`

**Step 3: Deploying the WAR file**

1. If you have not already created a WebLogic Domain for Logi Report Server you must create one before starting the integration.
2. In computer A, start WebLogic by running startWeblogic.sh in `C:\bea\user_projects\domains\domain_name\bin`.
3. In computer B, access the WebLogic Administrative Console using the URL `http://hostname:7001/console/`, where the hostname is computer A's host name or IP address, and 7001 is the port number.
4. After your successful login, in the Domain Structure panel on the left, select **Deployments** node.
5. In the Summary of Deployments panel, select **Install**.
6. In the Install Application Assistant panel, select the **upload your file(s)** link.
7. In the Deployment Archive section, select **Browse** to select the **remote.war** file in `C:\LogiReport\Server\bin\distribute`, and then select **Next**.
8. Keep selecting **Next** until the Finish button is enabled, and then select **Finish**.
9. Start Logi Report Server in computer B. Then go to computer A and access Logi Report Server using the following URL:

   `http://localhost:7001/remote/`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749821-Integrating-Remote-Logi-Report-Server-with-IBM-WebSphere-9-0-0-7-by-a-WAR-File)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009722882-Seamless-Integrated-Security-Solution)
