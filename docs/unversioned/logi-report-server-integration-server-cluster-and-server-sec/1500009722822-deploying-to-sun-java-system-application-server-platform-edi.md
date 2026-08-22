---
title: "Deploying to Sun Java\u2122 System Application Server Platform Edition 9.1"
id: 1500009722822
section: "Logi Report Server Integration, Server Cluster, and Server Security Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009722822-Deploying-to-Sun-Java-System-Application-Server-Platform-Edition-9-1
updated_at: 2021-07-25T07:19:03Z
---

# Deploying to Sun Java™ System Application Server Platform Edition 9.1

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722782-Deploying-to-JBoss-EAP-7-3-0)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009722802-Deploying-to-Jetty-9-4-28)

# Deploying to Sun Java™ System Application Server Platform Edition 9.1

This topic introduces how to deploy Logi Report Server to Sun Java™ System Application Server Platform Edition. The example directory paths listed below are based on Windows. The instructions are applicable to both Unix and Windows installations; however, the format of the paths for Unix would use the Unix format, that is, `/opt/LogiReport/Server` instead of `C:\LogiReport\Server`.

It is assumed that:

* Sun Java™ System Application Server Platform Edition 9.1 is installed in the `C:\Sun\AppServer` directory.
* It is assumed that the Logi Report Server WAR file jreport.war is located in the `C:\LogiReport\Server\bin\distribute` directory. To create the WAR file refer to the instructions in [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009749861-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

**To deploy Logi Report Server to Sun Java™ System Application Server Platform Edition 9.1:**

1. Update Sun Application Server's Derby jars using the lib folder in `C:\LogiReport\Server\derby` to replace the lib folder in `C:\Sun\AppServer\javadb\lib`.
2. Start the Sun Application Server by selecting **Start** > **Programs** > **Sun Microsystems** > **Application Server PE** > **Start Default Server.**
3. Launch the Admin Console by selecting **Start** > **Programs** > **Sun Microsystems** > **Application Server PE** > **Admin Console.**
4. In the left console tree, expand the **Applications** node, then select **Web Applications**.
5. In the **Web Applications** page, select **Deploy**.
6. Select the radio button before **Local packaged file or directory that is accessible from the Application Server**, then select **Browse Files** to select the WAR file **jreport.war**.
7. Use the default settings and select **OK**. You will find a new application jreport is listed.
8. Access Logi Report Server using the following URLs:

   `http://<hostname>:8080/jreport/jrserver  
    http://<hostname>:8080/jreport/jinfonet/index.jsp`

## Troubleshooting

If you run into some problems when using the Sun Application Server, send the log files of Logi Report Server to [support@logianalytics.com](mailto:support@logianalytics.com). The following procedure illustrates how to generate the log files:

1. Start the Sun Application Server, and then launch the Admin Console.
2. In the console tree, select **Application Server**.
3. Go to the JVM Settings tab, and then select **JVM Options**.
4. In the JVM Option field, select **Add JVM Option**, and then type **-Dlogall=true**.
5. Select **Save** to save your changes.
6. Restart Sun Application Server and try to reproduce the problem.
7. After reproducing the problem, send [support@logianalytics.com](mailto:support@logianalytics.com) the log files in `reporthome/logs.`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722782-Deploying-to-JBoss-EAP-7-3-0)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009722802-Deploying-to-Jetty-9-4-28)
