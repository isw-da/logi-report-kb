---
title: "Deploying Server to Sun Java\u2122 System Application Server Platform Edition 9.1"
id: 4405690628631
section: "Logi Report Server Integration Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690628631-Deploying-Server-to-Sun-Java-System-Application-Server-Platform-Edition-9-1
updated_at: 2022-01-27T07:59:34Z
---

# Deploying Server to Sun Java™ System Application Server Platform Edition 9.1

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683909527-Deploying-Server-to-JBoss-EAP)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683910551-Deploying-Server-to-Jetty)

# Deploying Server to Sun Java™ System Application Server Platform Edition 9.1

This topic describes how you can deploy Logi Report Server to Sun Java™ System Application Server Platform Edition.

We use paths based on UNIX path name protocol in our example. The instruction applies to both UNIX and Windows installation. However, the path formats differ. For Windows it is in this format `C:\LogiReport\Server` instead of `/opt/LogiReport/Server`.

Assume that:

* You installed Sun Java™ System Application Server Platform Edition 9.1 in the `C:\Sun\AppServer` directory.
* The Logi Report Server WAR file **jreport.war** is in the `C:\LogiReport\Server\bin\distribute` directory. To create the WAR file, see [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/4405690635159-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

**To deploy Logi Report Server to Sun Java™ System Application Server Platform Edition 9.1:**

1. Update Sun Application Server's Derby jars using the **lib** folder in `C:\LogiReport\Server\derby` to replace the **lib** folder in `C:\Sun\AppServer\javadb\lib`.
2. Start the Sun Application Server by selecting **Start** > **Programs** > **Sun Microsystems** > **Application Server PE** > **Start Default Server.**
3. Launch the Admin Console by selecting **Start** > **Programs** > **Sun Microsystems** > **Application Server PE** > **Admin Console.**
4. In the left console tree, expand the **Applications** node, then select **Web Applications**.
5. In the **Web Applications** page, select **Deploy**.
6. Select the radio button before **Local packaged file or directory that is accessible from the Application Server**, then select **Browse Files** to select the WAR file **jreport.war**.
7. Select **OK**. You will find a new application **jreport**.
8. Access Logi Report Server using the following URLs:

   `http://<hostname>:8080/jreport/jrserver  
    http://<hostname>:8080/jreport/jinfonet/index.jsp`

## Troubleshooting

If you run into problems when using the Sun Application Server, you may have to send the log files of Logi Report Server to [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.). The following procedure illustrates how to generate the log files:

1. Start the Sun Application Server.
2. Launch the Admin Console.
3. In the console tree, select **Application Server**.
4. Go to the JVM Settings tab, and then select **JVM Options**.
5. In the JVM Option field, select **Add JVM Option**, and then type **-Dlogall=true**.
6. Select **Save** to save your changes.
7. Restart Sun Application Server and try to reproduce the problem.
8. After reproducing the problem, send [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.) the log files in `reporthome/logs.`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683909527-Deploying-Server-to-JBoss-EAP)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683910551-Deploying-Server-to-Jetty)
