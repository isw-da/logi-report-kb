---
title: "Integrating Remote Logi JReport Server with IBM WebSphere 9.0.0.7 by a WAR File"
id: 1500009691222
section: "Integrating Remote Logi JReport Server"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009691222-Integrating-Remote-Logi-JReport-Server-with-IBM-WebSphere-9-0-0-7-by-a-WAR-File
updated_at: 2021-11-03T06:56:58Z
---

# Integrating Remote Logi JReport Server with IBM WebSphere 9.0.0.7 by a WAR File

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009717481-Integrating-Remote-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717501-Integrating-Remote-Logi-Report-Server-with-WebLogic-12c-12-2-1-3-0-by-a-WAR-File)

# Integrating Remote Logi JReport Server With IBM WebSphere 9.0.0.7 by a WAR File

Here is an example illustrating the case of using JSPs based on Remote Server APIs to integrate with IBM WebSphere 9.0.0.7.

It is assumed that:

* WebSphere 9.0.0.7 is installed in `C:\WebSphere` in computer A.
* Logi JReport Server is installed in `C:\JReport\Server` in computer B. The computer IP is 127.0.0.1.

The procedure for integrating remote Logi JReport Server with IBM WebSphere contains the following major steps:

1. [Generate the WAR file](#Generate)
2. [ConfigureLogi JReport Server](#Config)
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

1. In computer A, start IBM WebSphere.
2. In computer B, access the WebSphere Administrative Console using the URL: `http://hostname:9060/ibm/console`, where the hostname is computer A's host name or IP address, and 9060 is the port number.
3. After successfully log in, expand the **Applications** node, select **Application Types** and then **Websphere enterprise applications**.
4. Select **Install**.
5. Select **Browse** to select the remote.war file, and then select **Next**.
6. Keep selecting **Next** until you see the requirement for specifying context root.
7. In the Context Root field, type a context path such as **/remote/**, then select **Next**.
8. Select **Finish** in the Summary page. The installing process may take several minutes, wait until the process is completed.
9. Select **Save**.
10. Select **remote.war** and then select **Start**.
11. Access Logi JReport Server using the following URL:

    `http://hostname:9080/remote/jinfonet/default.jsp`

    Here the hostname is computer A's host name or IP address.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009717481-Integrating-Remote-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717501-Integrating-Remote-Logi-Report-Server-with-WebLogic-12c-12-2-1-3-0-by-a-WAR-File)
