---
title: "Deploying to IBM WebSphere 9.0.5.3"
id: 1500009722842
section: "Logi Report Server Integration, Server Cluster, and Server Security Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009722842-Deploying-to-IBM-WebSphere-9-0-5-3
updated_at: 2021-07-25T07:19:03Z
---

# Deploying to IBM WebSphere 9.0.5.3

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722762-Deploying-Logi-Report-Server-to-a-Java-Application-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749761-Deploying-to-WebLogic-12c-12-2-1-3-0-)

# Deploying to IBM WebSphere 9.0.5.3

This topic introduces how to deploy Logi Report Server to IBM WebSphere. The example directory paths listed below are based on Unix. The instructions are applicable to both Unix and Windows installations; however, the format of the paths for Windows would use the Windows format, that is, `C:\LogiReport\Server` instead of `/opt/LogiReport/Server`.

It is assumed that:

* WebSphere 9.0.5.3 is installed in the `/opt/IBM/WebSphere9.0.5.3/AppServer` directory.
* The Logi Report Server WAR file jreport.war is located in the `/opt/LogiReport/Server/bin/distribute` directory. To create the WAR file, refer to the instructions in [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009749861-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

  **Note:** Before creating the WAR, you need to modify the LogConfig.properties file in `/opt/LogiReport/Server/bin` as follows:

  + Change JRPatternLayout to PatternLayout all over the file.
  + Change all the Logger levels from ERROR to trace.

**To deploy Logi Report Server to IBM WebSphere:**

1. Copy Derby jars in `/opt/LogiReport/Server/derby` to the `/opt/IBM/WebSphere9.0.5.3/AppServer/lib` directory.
2. Start IBM WebSphere. Use the shell script `/opt/IBM/WebSphere9.0.5.3/AppServer/bin/startServer.sh <servername>` to start the server. The default server name is server1.
3. Access the WebSphere Administrative Console using the URL: `http://hostname:9060/ibm/console`, where the hostname is host name or IP address, and 9060 is the port number.
4. The login requires user name and password.
5. After successfully log in, expand the **Applications** node, select **Application Types** and then **Websphere enterprise applications**.
6. Select **Install**.
7. Select **Browse** to select the jreport.war file, and then select **Next**.
8. Keep selecting **Next** until you see the requirement for specifying context root.
9. In the Context Root field, type a context path such as **/jreport/**, then select **Next**.
10. Select **Finish** in the Summary page. The installing process may take several minutes, wait until the process is completed.
11. Select **Save**.
12. Select **jreport.war** and then select **Start** to start Logi Report Server.
13. Access Logi Report Server using the following URL:

    `http://<hostname>:9080/jreport/jrserver
      
    http://<hostname>:9080/jreport/jinfonet/index.jsp`

## Troubleshooting

If you run into problems when using Logi Report Server in IBM WebSphere, send the log files of Logi Report Server to [support@logianalytics.com](mailto:support@logianalytics.com). The following procedure illustrates how to generate the log files:

1. Type **-Dlogall=true** in the Generic JVM arguments field. Go to **Application servers** > **server1** > **Process Definition** > **Java Virtual Machine** to access this field.
2. Restart the application server, and try to reproduce the problem. After reproducing the problem, send [support@logianalytics.com](mailto:support@logianalytics.com) the log files in `reporthome/logs.`

   The WebSphere log files may also help to identify the problem. The most useful one is in `/opt/IBM/WebSphere9.0.5.3/AppServer/profiles/AppSrv01/logs/server1/SystemErr.log.`

**Note:** For WebSphere Application Server Liberty Profile 20.0.0.3, you need to do the following:

* Configure JNDI so as for the reporthome to be generated successfully. Add the following lines in server.xml located in `${WebSphere_home}/usr/servers/defaultServer`:

  `<featureManager>  
  <feature>jndi-1.0</feature>  
  </featureManager>`
* Extract jreport.war to `${wlphome}/usr/servers/defaultServer/dropins` and then start WebSphere Application Server Liberty Profile 20.0.0.3. In this way the sample reports will be able to run well.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722762-Deploying-Logi-Report-Server-to-a-Java-Application-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749761-Deploying-to-WebLogic-12c-12-2-1-3-0-)
