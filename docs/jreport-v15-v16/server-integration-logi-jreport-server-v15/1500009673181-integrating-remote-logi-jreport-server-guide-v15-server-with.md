---
title: "Integrating Remote Logi JReport Server Guide v15 Server with WebLogic 11g Release 1 (10.3.2) by a WAR File"
id: 1500009673181
section: "Server Integration Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673181-Integrating-Remote-Logi-JReport-Server-Guide-v15-Server-with-WebLogic-11g-Release-1-10-3-2-by-a-WAR-File
updated_at: 2021-07-24T20:54:11Z
---

# Integrating Remote Logi JReport Server Guide v15 Server with WebLogic 11g Release 1 (10.3.2) by a WAR File

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673201-Integrating-Remote-Logi-JReport-Server-Guide-v15-Server-with-IBM-WebSphere-8-5-3-3-by-a-WAR-File)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673241-Seamless-Integrated-Security-Solution)

# Integrating Remote Logi JReport Server with WebLogic 11g Release 1 (10.3.2) by a WAR File

Here is an example illustrating the case of using JSPs based on Remote Server APIs to integrate with WebLogic 11g Release 1 (10.3.2).

It is assumed that:

* WebLogic is installed in `C:\bea` in computer A.
* Logi JReport Server is installed in `C:\Logi JReport\Server` in computer B. The computer IP is 127.0.0.1.

Take the following steps to integrate remote Logi JReport Server with WebLogic:

1. [Generate a WAR file.](#Generate)
2. [Configure Logi JReport Server.](#Config)
3. [Deploy the WAR file.](#Deploy)

Below show the details of each step:

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Generating a WAR File

1. In computer B, use the tool makewar.bat to build the Logi JReport Server WAR file as defined by makewar.xml for remote integration. Both makewar.bat and makewar.xml are located in `C:\Logi JReport\Server\bin`. Run the following commands in DOS window and the generated WAR file remote.war will be saved to the directory `C:\Logi JReport\Server\bin\distribute`.

   `makewar.bat buildRemoteWar -Djrs.remote.host=127.0.0.1 -Djrs.remote.rmiport=1129 -Djrs.rmi.auth_file=C:\Logi JReport\Server\bin\rmi.auth`
2. Copy the rmi.auth file from `C:\Logi JReport\Server\bin` in computer B to `C:\Logi JReport\Server\bin` in computer A.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Configuring Logi JReport Server

1. Make sure Logi JReport Server has been started once so that the server.properties file is generated.
2. Change server.properties file in `C:\Logi JReport\Server\bin` as follows:

   `server.rmiserver.enable=true   
    server.rmiadminservice.enable=true`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Deploying the WAR file

1. If you have not already created a WebLogic Domain for Logi JReport Server you must create one before starting the integration.
2. In computer A, start WebLogic by running startWeblogic.sh in `C:\bea\user_projects\domains\domain_name\bin`.
3. In computer B, access the WebLogic Administrative Console by using URL `http://hostname:7001/console/`, where the hostname is computer A's host name or IP address, and 7001 is the port number.
4. After your successful login, in the Domain Structure panel on the left, select **Deployments** node.
5. In the Summary of Deployments panel, select **Install**.
6. In the Install Application Assistant panel, select the **upload your file(s)** link.
7. In the Deployment Archive section, select **Browse** to select the **remote.war** file in `C:\Logi JReport\Server\bin\distribute`, and then select **Next**.
8. Keep selecting **Next** until the Finish button is enabled, and then select **Finish**.
9. Start Logi JReport Server in computer B. Then go to computer A and access Logi JReport Server using the following URL:

   `http://localhost:7001/remote/`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673201-Integrating-Remote-Logi-JReport-Server-Guide-v15-Server-with-IBM-WebSphere-8-5-3-3-by-a-WAR-File)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673241-Seamless-Integrated-Security-Solution)
