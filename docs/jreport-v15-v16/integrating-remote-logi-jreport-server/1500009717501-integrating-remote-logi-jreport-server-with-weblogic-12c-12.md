---
title: "Integrating Remote Logi JReport Server with WebLogic 12c (12.2.1.3.0) by a WAR File"
id: 1500009717501
section: "Integrating Remote Logi JReport Server"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009717501-Integrating-Remote-Logi-JReport-Server-with-WebLogic-12c-12-2-1-3-0-by-a-WAR-File
updated_at: 2021-11-03T06:56:57Z
---

# Integrating Remote Logi JReport Server with WebLogic 12c (12.2.1.3.0) by a WAR File

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691222-Integrating-Remote-Logi-Report-Server-with-IBM-WebSphere-9-0-0-7-by-a-WAR-File)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717541-Seamless-Integrated-Security-Solution)

# Integrating Remote Logi JReport Server With WebLogic 12c (12.2.1.3.0) by a WAR File

Here is an example illustrating the case of using JSPs based on Remote Server APIs to integrate with WebLogic 12c (12.2.1.3.0).

It is assumed that:

* WebLogic is installed in `C:\bea` in computer A.
* Logi JReport Server is installed in `C:\JReport\Server` in computer B. The computer IP is 127.0.0.1.

The procedure for integrating remote Logi JReport Server with WebLogic contains the following major steps:

1. [Generate the WAR file](#Generate)
2. [Configure Logi JReport Server](#Config)
3. [Deploy the WAR file](#Deploy)

**Step 1: Generating the WAR file**

1. In computer B, use the tool makewar.bat to build the Logi JReport Server WAR file as defined by makewar.xml for remote integration. Both makewar.bat and makewar.xml are located in `C:\JReport\Server\bin`. Run the following commands in DOS window and the generated WAR file remote.war will be saved to the directory `C:\JReport\Server\bin\distribute`.

   `makewar.bat buildRemoteWar -Djrs.remote.host=127.0.0.1 -Djrs.remote.rmiport=1129 -Djrs.rmi.auth_file=C:\JReport\Server\bin\rmi.auth`
2. Copy the rmi.auth file from `C:\JReport\Server\bin` in computer B to `C:\JReport\Server\bin` in computer A.

**Step 2: Configuring Logi JReport Server**

1. Make sure Logi JReport Server has been started once so that the server.properties file is generated.
2. Change server.properties file in `C:\JReport\Server\bin` as follows:

   `server.rmiserver.enable=true   
    server.rmiadminservice.enable=true`

**Step 3: Deploying the WAR file**

1. If you have not already created a WebLogic Domain for Logi JReport Server you must create one before starting the integration.
2. In computer A, start WebLogic by running startWeblogic.sh in `C:\bea\user_projects\domains\domain_name\bin`.
3. In computer B, access the WebLogic Administrative Console using the URL `http://hostname:7001/console/`, where the hostname is computer A's host name or IP address, and 7001 is the port number.
4. After your successful login, in the Domain Structure panel on the left, select **Deployments** node.
5. In the Summary of Deployments panel, select **Install**.
6. In the Install Application Assistant panel, select the **upload your file(s)** link.
7. In the Deployment Archive section, select **Browse** to select the **remote.war** file in `C:\JReport\Server\bin\distribute`, and then select **Next**.
8. Keep selecting **Next** until the Finish button is enabled, and then select **Finish**.
9. Start Logi JReport Server in computer B. Then go to computer A and access Logi JReport Server using the following URL:

   `http://localhost:7001/remote/`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691222-Integrating-Remote-Logi-Report-Server-with-IBM-WebSphere-9-0-0-7-by-a-WAR-File)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717541-Seamless-Integrated-Security-Solution)
