---
title: "Deploying to Sun Java\u2122 System Application Server Platform Edition 9.1"
id: 1500009673081
section: "Server Integration Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673081-Deploying-to-Sun-Java-System-Application-Server-Platform-Edition-9-1
updated_at: 2021-07-24T20:54:11Z
---

# Deploying to Sun Java™ System Application Server Platform Edition 9.1

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648442-Deploying-to-OC4J-10g-R3-10-1-3-5-0-)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673061-Deploying-to-Jetty-9-4-6)

# Deploying to Sun Java™ System Application Server Platform Edition 9.1

This topic introduces how to deploy Logi JReport Server Guide v15 Server to Sun Java™ System Application Server Platform Edition 9.1. The example directory paths listed below are based on Windows. The instructions are applicable to both Unix and Windows installations; however, the format of the paths for Unix would use the Unix format, that is, `/opt/Logi JReport/Server` instead of `C:\Logi JReport\Server`.

It is assumed that:

* Sun Java™ System Application Server Platform Edition 9.1 is installed in the `C:\Sun\AppServer` directory.
* It is assumed that the Logi JReport Server WAR file Logi JReport.war is located in the `C:\Logi JReport\Server\bin\distribute` directory. To create the WAR file refer to the instructions in [Building a WAR/EAR File to Include a Self-contained Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009648502-Building-a-WAR-EAR-file-to-Include-a-Self-contained-Logi-JReport-Server-Guide-v15-Server).

**To deploy Logi JReport Server to Sun Java™ System Application Server Platform Edition 9.1:**

1. Update Sun Application Server's Derby jars by
   using the lib folder in `C:\Logi JReport\Server\derby` to replace the lib folder in `C:\Sun\AppServer\javadb\lib`.
2. Start the Sun Application Server by selecting **Start** > **Programs** > **Sun Microsystems** > **Application Server PE** > **Start Default Server.**
3. Launch the Admin Console by selecting **Start** > **Programs** > **Sun Microsystems** > **Application Server PE** > **Admin Console.**
4. In the left console tree, expand the **Applications** node, then select **Web Applications**.
5. In the **Web Applications** page, select **Deploy**.
6. Select the radio button before **Local packaged file or directory that is accessible from the Application Server**, then select **Browse Files** to select the WAR file **Logi JReport.war**.
7. Use the default settings and select **OK**. You will find a new application Logi JReport is listed.
8. Access Logi JReport Server using the following URLs:

   `http://<hostname>:8080/Logi JReport/jrserver  
    http://<hostname>:8080/Logi JReport/jinfonet/index.jsp  
    http://<hostname>:8080/Logi JReport/admin/index.jsp`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Troubleshooting

If you run into some problems when using the Sun Application Server, send the log files of Logi JReport Server to [support@jinfonet.com](mailto:support@jinfonet.com). The following procedure illustrates how to generate the log files:

1. Start the Sun Application Server, and then launch the Admin Console.
2. In the console tree, select **Application Server**.
3. Go to the JVM Settings tab, and then select **JVM Options**.
4. In the JVM Option field, select **Add** **JVM Option**, and then type **-Dlogall=true**.
5. Select **Save** to save your changes.
6. Restart Sun Application Server and try to reproduce the problem.
7. After reproducing the problem, send [support@jinfonet.com](mailto:support@jinfonet.com) the log files in `reporthome/logs.`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648442-Deploying-to-OC4J-10g-R3-10-1-3-5-0-)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673061-Deploying-to-Jetty-9-4-6)
