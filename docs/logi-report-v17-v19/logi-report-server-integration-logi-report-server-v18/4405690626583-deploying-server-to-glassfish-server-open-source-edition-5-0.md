---
title: "Deploying Server to GlassFish Server Open Source Edition 5.0"
id: 4405690626583
section: "Logi Report Server Integration Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690626583-Deploying-Server-to-GlassFish-Server-Open-Source-Edition-5-0
updated_at: 2022-01-27T07:59:34Z
---

# Deploying Server to GlassFish Server Open Source Edition 5.0

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683910551-Deploying-Server-to-Jetty)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690627735-Deploying-Server-to-Resin-4-0-65)

# Deploying Server to GlassFish Server Open Source Edition 5.0

This topic describes how you can deploy Logi Report Server to GlassFish.

We use paths based on UNIX path name protocol in our example. The instruction applies to both UNIX and Windows installation. However, the path formats differ. For Windows it is in this format `C:\LogiReport\Server` instead of `/opt/LogiReport/Server`.

Assume that the Logi Report Server WAR file **jreport.war** is in the `/opt/LogiReport/Server/bin/distribute` directory. To create the WAR file, see [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/4405690635159-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

**To deploy Logi Report Server to GlassFish Server Open Source Edition 5.0:**

1. Start GlassFish in the default **domain1** and launch the Admin Console.
2. Select the **Applications** node on the left.
3. Select **Deploy** on the displayed page.
4. Select **Choose File** to select the WAR file **jreport.war**.
5. Leave Application Name and Context Root as jreport and jreport. Then select **OK**.
6. Expand the **Deployment** node on the left and you see a new node named **jreport**. Select it and then on the displayed page select **Save**.
7. In the console tree, select **Configuration**.
8. Go to the **JVM Settings** tab and select **JVM Options**.
9. In the JVM Options section, select **Add JVM Option**, and then type **-Djava.awt.headless=true**. Select **Save** to save your changes.

   You need not add this JVM option if you are using Windows.
10. Restart GlassFish and start the application **jreport**.
11. Access Logi Report Server using the following URLs:

    `http://<hostname>:8080/jreport  
     http://<hostname>:8080/jreport/jinfonet/index.jsp`

## Troubleshooting

If you run into problems when using GlassFish, you may have to send the log files of Logi Report Server to [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.). The following procedure illustrates how to generate the log files:

1. Start GlassFish in the default domain1 and then launch the Admin Console.
2. In the console tree, select **Configuration**.
3. Go to the JVM Settings tab, and then select **JVM Options**.
4. In the JVM Options section, select **Add JVM Option**, and then type **-Dlogall=true**. Select **Save** to save your changes.
5. Restart GlassFish and try to reproduce the problem.
6. After reproducing the problem, send [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.) the log files in `reporthome/logs`.

   The GlassFish log file may also help to identify the problem. It is /opt/glassfish/domains/domain1/logs/server.log.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683910551-Deploying-Server-to-Jetty)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690627735-Deploying-Server-to-Resin-4-0-65)
