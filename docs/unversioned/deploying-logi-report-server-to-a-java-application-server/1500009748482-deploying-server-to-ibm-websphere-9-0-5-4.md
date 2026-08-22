---
title: "Deploying Server to IBM WebSphere 9.0.5.4"
id: 1500009748482
section: "Deploying Logi Report Server to a Java Application Server"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009748482-Deploying-Server-to-IBM-WebSphere-9-0-5-4
updated_at: 2021-07-24T00:48:01Z
---

# Deploying Server to IBM WebSphere 9.0.5.4

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748402-Deploying-Logi-Report-Server-to-a-Java-Application-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748462-Deploying-Server-to-WebLogic-14-1-1)

# Deploying Server to IBM WebSphere 9.0.5.4

This topic describes how you can deploy Logi Report Server to IBM WebSphere.

In the example we use directory paths based on Unix. The instructions are applicable to both Unix and Windows installations. However, the format of the paths for Windows should use the Windows format, that is, `C:\LogiReport\Server` instead of `/opt/LogiReport/Server`.

Assume that:

* You installed WebSphere 9.0.5.4 in the `/opt/IBM/WebSphere9.0.5.4/AppServer` directory.
* The Logi Report Server WAR file **jreport.war** is in the `/opt/LogiReport/Server/bin/distribute` directory. To create the WAR file, refer to the instructions in [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009777021-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

  ![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404885352855/criticalicon.gif)Before creating the WAR, you need to modify the **LogConfig.properties** file in `/opt/LogiReport/Server/bin` as follows:

  + Change **JRPatternLayout** to **PatternLayout** all over the file.
  + Change all the Logger levels from **ERROR** to **trace**.

**To deploy Logi Report Server to IBM WebSphere:**

1. Copy Derby jars in `/opt/LogiReport/Server/derby` to the `/opt/IBM/WebSphere9.0.5.4/AppServer/lib` directory.
2. Start IBM WebSphere. Use the shell script `/opt/IBM/WebSphere9.0.5.4/AppServer/bin/startServer.sh <servername>` to start the server. The default server name is **server1**.
3. Access the WebSphere Administrative Console using the URL: `http://hostname:9060/ibm/console`, where **hostname** is host name or IP address, and 9060 is the port number.
4. The login requires user name and password.
5. After you log in, expand the **Applications** node, select **Application Types** and then **Websphere enterprise applications**.
6. Select **Install**.
7. Select **Browse** to select the **jreport.war** file, and then select **Next**.
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

1. Go to **Application servers** > **server1** > **Process Definition** > **Java Virtual Machine**.
2. Type **-Dlogall=true** in the Generic JVM arguments field.
3. Restart the application server.
4. Try to reproduce the problem. After reproducing the problem, send [support@logianalytics.com](mailto:support@logianalytics.com) the log files in `reporthome/logs.`

   The WebSphere log files may also help to identify the problem. The most useful one is in `/opt/IBM/WebSphere9.0.5.4/AppServer/profiles/AppSrv01/logs/server1/SystemErr.log.`

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)For WebSphere Application Server Liberty Profile, you need to do the following:

* Configure JNDI to generate the reporthome. Add the following lines in **server.xml** in `${WebSphere_home}/usr/servers/defaultServer`:

  `<featureManager>  
  <feature>jndi-1.0</feature>  
  </featureManager>`
* Extract **jreport.war** to `${wlphome}/usr/servers/defaultServer/dropins` and then start WebSphere Application Server Liberty Profile. In this way the sample reports will be able to run well.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748402-Deploying-Logi-Report-Server-to-a-Java-Application-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748462-Deploying-Server-to-WebLogic-14-1-1)
