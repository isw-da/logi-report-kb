---
title: "Deploying Server to IBM WebSphere 9.0.5.6"
id: 5741473716631
section: "Logi Report Server Integration Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741473716631-Deploying-Server-to-IBM-WebSphere-9-0-5-6
updated_at: 2022-10-31T17:17:56Z
---

# Deploying Server to IBM WebSphere 9.0.5.6

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741431629463-Deploying-Logi-Report-Server-to-a-Java-Application-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741467821079-Deploying-Server-to-WebLogic-14-1-1)

# Deploying Server to IBM WebSphere 9.0.5.6

This topic describes how you can deploy Logi Report Server to IBM WebSphere 9.0.5.6.

We use paths based on UNIX path name protocol in our example. The instruction applies to both UNIX and Windows installation. However, the path formats differ. For Windows it is in this format `C:\LogiReport\Server` instead of `/opt/LogiReport/Server`.

Assume that:

* You installed WebSphere 9.0.5.6 in the `/opt/IBM/WebSphere/AppServer` directory.
* The Logi Report Server WAR file **jreport.war** is in the `/opt/LogiReport/Server/bin/distribute` directory. To create the WAR file, see [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/5741473837719-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

  ![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/9905614395415/criticalicon.gif) Before creating the WAR, you need to modify the **LogConfig.properties** file in `/opt/LogiReport/Server/bin`:

  + Change **JRPatternLayout** to **PatternLayout** all over the file.
  + Change all the Logger levels from **ERROR** to **TRACE**.

**To deploy Logi Report Server to IBM WebSphere:**

1. Copy Derby jars in `/opt/LogiReport/Server/derby` to the `/opt/IBM/WebSphere/AppServer/lib` directory.
2. Run the shell script `/opt/IBM/WebSphere/AppServer/bin/startServer.sh <servername>` to start the IBM WebSphere server. The default server name is **server1**.
3. Access the WebSphere Administrative Console using the URL `http://hostname:9060/ibm/console`, where **hostname** is host name or IP address and **9060** is the port number.
4. Provide your username and password.
5. After you sign in, expand **Applications**.
6. Select **Application Types**.
7. Select **Websphere enterprise applications**.
8. Select **Install**.
9. Select **Browse** to select the **jreport.war** file.
10. Keep selecting **Next** until you see the requirement for specifying context root.
11. In the **Context Root** field, type a context path such as **/jreport/**.
12. Select **Next**.
13. Select **Finish** in the Summary page. The installing process may take several minutes. Wait until the process completes.
14. Select **Save**.
15. Select **jreport.war**.
16. Select **Start** to start Logi Report Server.
17. Access Logi Report Server using the following URL:

    `http://<hostname>:9080/jreport/jrserver
      
    http://<hostname>:9080/jreport/jinfonet/index.jsp`

## Troubleshooting

If you run into problems when using Logi Report Server in IBM WebSphere, you may have to send the log files of Logi Report Server to [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.). The following procedure illustrates how to generate the log files:

1. Go to **Application servers** > **server1** > **Process Definition** > **Java Virtual Machine**.
2. Type **-Dlogall=true** in the **Generic JVM arguments** field.
3. Restart the application server.
4. Try to reproduce the problem.
5. After reproducing the problem, send [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.) the log files in `reporthome/logs.`

   The WebSphere log files may also help to identify the problem. The most useful one is in `/opt/IBM/WebSphere/AppServer/profiles/AppSrv01/logs/server1/SystemErr.log.`

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) For WebSphere Application Server Liberty Profile, you need to:

* Configure JNDI to generate the reporthome. Add the following lines in **server.xml** in `${WebSphere_home}/usr/servers/defaultServer`:

  `<featureManager>  
  <feature>jndi-1.0</feature>  
  </featureManager>`
* Extract **jreport.war** to `${wlphome}/usr/servers/defaultServer/dropins` and then start WebSphere Application Server Liberty Profile. In this way the sample reports will be able to run well.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741431629463-Deploying-Logi-Report-Server-to-a-Java-Application-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741467821079-Deploying-Server-to-WebLogic-14-1-1)
