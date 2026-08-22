---
title: "Deploying to IBM WebSphere 9.0.0.4"
id: 1500009673141
section: "Server Integration Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673141-Deploying-to-IBM-WebSphere-9-0-0-4
updated_at: 2021-07-24T20:54:10Z
---

# Deploying to IBM WebSphere 9.0.0.4

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673041-Deploying-Logi-JReport-Server-Guide-v15-Server-to-a-Java-Application-Server)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673121-Deploying-to-WebLogic-12c-Release-1-12-2-1-3-0-)

# Deploying to IBM WebSphere 9.0.0.4

This topic introduces how to deploy Logi JReport Server Guide v15 Server to IBM WebSphere 9.0.0.4. The example directory paths listed below are based on Unix. The instructions are applicable to both Unix and Windows installations; however, the format of the paths for Windows would use the Windows format, that is, `C:\Logi JReport\Server` instead of `/opt/Logi JReport/Server`.

It is assumed that:

* WebSphere 9.0.0.4 is installed in the `/opt/IBM/WebSphere9.0.0.4/AppServer` directory.
* The Logi JReport Server WAR file Logi JReport.war is located in the `/opt/Logi JReport/Server/bin/distribute` directory. To create the WAR file, refer to the instructions in [Building a WAR/EAR File to Include a Self-contained Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009648502-Building-a-WAR-EAR-file-to-Include-a-Self-contained-Logi-JReport-Server-Guide-v15-Server).

  **Note:** Before creating the WAR, you need to modify the LogConfig.properties file in `/opt/Logi JReport/Server/bin` as follows:

  + Remove the code `packages = com.jinfonet.util`.
  + Change JRRollingFileAppender to RollingFile all over the file.
  + Change JRPatternLayout to PatternLayout all over the file.
  + Change all the Logger levels from ERROR to trace.

**To deploy Logi JReport Server to IBM WebSphere:**

1. Copy Derby jars in `/opt/Logi JReport/Server/derby` to the `/opt/IBM/WebSphere9.0.0.4/AppServer/lib` directory.
2. Start IBM WebSphere. Use the shell script `/opt/IBM/WebSphere9.0.0.4/AppServer/bin/startServer.sh <servername>` to start the server. The default server name is server1.
3. Access the WebSphere Administrative Console by using the URL: `http://hostname:9060/ibm/console`, where the hostname is host name or IP address, and 9060 is the port number.
4. The login requires user name and password.
5. After successfully log in, expand the **Applications** node, select **Application Types** and then **Websphere enterprise applications**.
6. Select **Install**.
7. Select **Browse** to select the Logi JReport.war file, and then select **Next**.
8. Keep selecting **Next** until you see the requirement for specifying context root.
9. In the Context Root field, type a context path such as **/Logi JReport/**, then select **Next**.
10. Select **Finish** on the Summary page. The installing process may take several minutes, wait until the process is completed.
11. Select **Save**.
12. Select **Logi JReport.war** and then select **Start** to start Logi JReport Server.
13. Access Logi JReport Server using the following URL:

    `http://<hostname>:9080/Logi JReport/jrserver  
    http://<hostname>:9080/Logi JReport/admin/index.jsp  
    http://<hostname>:9080/Logi JReport/jinfonet/index.jsp`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Troubleshooting

If you run into problems when using Logi JReport Server in IBM WebSphere, send the log files of Logi JReport Server to [support@jinfonet.com](mailto:support@jinfonet.com). The following procedure illustrates how to generate the log files:

1. Type **-Dlogall=true** in the Generic JVM arguments field. Go to **Application servers** > **server1** > **Process Definition** > **Java Virtual Machine** to access this field.
2. Restart the application server, and try to reproduce the problem. After reproducing the problem, send [support@jinfonet.com](mailto:support@jinfonet.com) the log files in `reporthome/logs.`

   The WebSphere log files may also help to identify the problem. The most useful one is in `/opt/IBM/WebSphere9.0.0.4/AppServer/profiles/AppSrv01/logs/server1/SystemErr.log.`

**Note:** For WebSphere Application Server Liberty Profile V17.0.0.2, you need to do the following:

* Configure JNDI so as for the reporthome to be generated successfully. Add the following lines in server.xml located in `${WebSphere_home}/usr/servers/defaultServer`:

  `<featureManager>  
  <feature>jndi-1.0</feature>  
  </featureManager>`
* Extract Logi JReport.war to `${wlphome}/usr/servers/defaultServer/dropins` and then start WebSphere Application Server Liberty Profile V17.0.0.1. In this way the sample reports will be able to run well.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673041-Deploying-Logi-JReport-Server-Guide-v15-Server-to-a-Java-Application-Server)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673121-Deploying-to-WebLogic-12c-Release-1-12-2-1-3-0-)
