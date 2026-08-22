---
title: "Deploying to GlassFish Server Open Source Edition 5.0"
id: 1500009717361
section: "Deploying Logi JReport Server to a Java Application Server"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009717361-Deploying-to-GlassFish-Server-Open-Source-Edition-5-0
updated_at: 2021-11-03T06:57:00Z
---

# Deploying to GlassFish Server Open Source Edition 5.0

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691162-Deploying-to-Jetty-9-4-20)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009691182-Deploying-to-Resin-4-0-62)

# Deploying to GlassFish Server Open Source Edition 5.0

This topic introduces how to deploy Logi JReport Server to GlassFish. The example directory paths listed below are based on Unix. The instructions are applicable to both Unix and Windows installations; however, the format of the paths for Windows would use the Windows format, that is, `C:\JReport\Server` instead of `/opt/JReport/Server`.

It is assumed that the Logi JReport Server WAR file jreport.war is located in the `/opt/JReport/Server/bin/distribute` directory. To create the WAR file refer to the instructions in [Building a WAR/EAR File to Include a Self-contained Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009717561-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

**To deploy Logi JReport Server to GlassFish Server Open Source Edition 5.0:**

1. Start GlassFish in the default domain1 and launch the Admin Console.
2. Select the **Applications** node on the left.
3. Select **Deploy** on the displayed page.
4. Select **Choose File** to select the WAR file **jreport.war**.
5. Leave Application Name and Context Root as jreport and jreport. Then select **OK**.
6. Expand the **Deployment** node on the left and you will see a new node named jreport. Select **jreport** and then on the displayed page select **Save**.
7. In the console tree, select **Configuration**. Go to the **JVM Settings** tab and select **JVM Options**. In the JVM Options section, select **Add JVM Option**, and then type **-Djava.awt.headless=true**. Select **Save** to save your changes.

   You need not add this JVM option if you are using Windows.
8. Restart GlassFish and start the application **jreport**.
9. Access Logi JReport Server using the following URLs:

   `http://<hostname>:8080/jreport  
    http://<hostname>:8080/jreport/jinfonet/index.jsp`

## Troubleshooting

If you run into some problems when using GlassFish, send the log files of Logi JReport Server to [support@jinfonet.com](mailto:support@jinfonet.com). The following procedure illustrates how to generate the log files:

1. Start GlassFish in the default domain1 and then launch the Admin Console.
2. In the console tree, select **Configuration**.
3. Go to the JVM Settings tab, and then select **JVM Options**.
4. In the JVM Options section, select **Add JVM Option**, and then type **-Dlogall=true**. Select **Save** to save your changes.
5. Restart GlassFish and try to reproduce the problem.
6. After reproducing the problem, send [support@jinfonet.com](mailto:support@jinfonet.com) the log files in `reporthome/logs`.

   The GlassFish log file may also help to identify the problem. It is /opt/glassfish/domains/domain1/logs/server.log.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691162-Deploying-to-Jetty-9-4-20)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009691182-Deploying-to-Resin-4-0-62)
