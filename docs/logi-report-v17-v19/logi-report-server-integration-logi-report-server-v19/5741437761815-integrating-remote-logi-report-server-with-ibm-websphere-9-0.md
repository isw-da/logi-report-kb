---
title: "Integrating Remote Logi Report Server with IBM WebSphere 9.0.0.7 by a WAR File"
id: 5741437761815
section: "Logi Report Server Integration Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741437761815-Integrating-Remote-Logi-Report-Server-with-IBM-WebSphere-9-0-0-7-by-a-WAR-File
updated_at: 2022-10-31T17:17:58Z
---

# Integrating Remote Logi Report Server with IBM WebSphere 9.0.0.7 by a WAR File

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741473756311-Integrating-Remote-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741467888791-Integrating-Remote-Logi-Report-Server-with-WebLogic-14-1-1-by-a-WAR-File)

# Integrating Remote Logi Report Server With IBM WebSphere 9.0.0.7 by a WAR File

This topic describes an example of using JSPs based on Remote Server APIs to integrate with IBM WebSphere 9.0.0.7.

Assume that:

* You installed WebSphere 9.0.0.7 in `C:\WebSphere` on computer A.
* You installed Logi Report Server in `C:\LogiReport\Server` on computer B. The computer IP is 127.0.0.1.

The procedure for integrating remote Logi Report Server with IBM WebSphere contains the following major steps:

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

1. On computer A, start IBM WebSphere.
2. On computer B, access the WebSphere Administrative Console using the URL: `http://hostname:9060/ibm/console`, where **hostname** is computer A's host name or IP address, and 9060 is the port number.
3. After you sign in, expand the **Applications** node, select **Application Types** and then **Websphere enterprise applications**.
4. Select **Install**.
5. Select **Browse** to select the **remote.war** file, and then select **Next**.
6. Keep selecting **Next** until you see the requirement for specifying context root.
7. In the Context Root field, type a context path such as **/remote/**, then select **Next**.
8. Select **Finish** in the Summary page. The installing process may take several minutes, wait until the process is completed.
9. Select **Save**.
10. Select **remote.war** and then select **Start**.
11. Access Logi Report Server using the following URL:

    `http://hostname:9080/remote/jinfonet/default.jsp`

    Here **hostname** is computer A's host name or IP address.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741473756311-Integrating-Remote-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741467888791-Integrating-Remote-Logi-Report-Server-with-WebLogic-14-1-1-by-a-WAR-File)
