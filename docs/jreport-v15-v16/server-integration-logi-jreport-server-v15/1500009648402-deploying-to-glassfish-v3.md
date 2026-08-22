---
title: "Deploying to GlassFish V3"
id: 1500009648402
section: "Server Integration Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648402-Deploying-to-GlassFish-V3
updated_at: 2021-07-24T20:54:12Z
---

# Deploying to GlassFish V3

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673061-Deploying-to-Jetty-9-4-6)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648462-Deploying-to-Resin-4-0-53)

# Deploying to GlassFish V3

This topic introduces how to deploy Logi JReport Server Guide v15 Server to GlassFish V3. The example directory paths listed below are based on Unix. The instructions are applicable to both Unix and Windows installations; however, the format of the paths for Windows would use the Windows format, that is, `C:\Logi JReport\Server` instead of `/opt/Logi JReport/Server`.

It is assumed that the Logi JReport Server WAR file Logi JReport.war is located in the `/opt/Logi JReport/Server/bin/distribute` directory. To create the WAR file refer to the instructions in [Building a WAR/EAR File to Include a Self-contained Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009648502-Building-a-WAR-EAR-file-to-Include-a-Self-contained-Logi-JReport-Server-Guide-v15-Server).

**To deploy Logi JReport Server to GlassFish V3:**

1. Start the GlassFish in the default domain1 and then launch the Admin Console**.**
2. Select the **Applications** node on the left.
3. Select **Deploy** on the displayed page.
4. Select **Choose File** to select the WAR file **Logi JReport.war**.
5. Leave Application Name and Context Root as Logi JReport and Logi JReport. Then select **OK**.
6. Expand the Deployment node on the left and you will see a new node named Logi JReport. Select **Logi JReport** and then on the displayed page select **Save**.
7. In the console tree, select **Configuration**. Go to the JVM Settings tab, and then select **JVM Options**. In the JVM Options section, select **Add JVM Option**, and then type **-Djava.awt.headless=true**. Select **Save** to save your changes.

   You need not add this JVM option if you are using Windows.
8. Restart GlassFish, and then start the application **Logi JReport**.
9. Access Logi JReport Server using the following URLs:

   `http://<hostname>:8080/Logi JReport  
    http://<hostname>:8080/Logi JReport/admin/index.jsp  
    http://<hostname>:8080/Logi JReport/jinfonet/index.jsp`

**Note:** GlassFish 3.1.2 uses a different Derby driver from Logi JReport which leads to that the Logi JReport War file does not work in GlassFish 3.1.2. To solve this, you can replace the files in `/opt/glassfish3.1.2/javadb/lib` with the jar files in `/opt/Logi JReport/Server/derby/lib`, or use the folder `/opt/glassfish3.0.2/javadb/lib` to replace the folder `/opt/glassfish3.1.2/javadb/lib` if GlassFish 3.0.2 resources are available.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Troubleshooting

If you run into some problems when using the GlassFish V3, send the log files of Logi JReport Server to [support@jinfonet.com](mailto:support@jinfonet.com). The following procedure illustrates how to generate the log files:

1. Start the GlassFish in the default domain1 and then launch the Admin Console.
2. In the console tree, select **Configuration**.
3. Go to the JVM Settings tab, and then select **JVM Options**.
4. In the JVM Options section, select **Add JVM Option**, and then type **-Dlogall=true**. Select **Save** to save your changes.
5. Restart GlassFish and try to reproduce the problem.
6. After reproducing the problem, send [support@jinfonet.com](mailto:support@jinfonet.com) the log files in `reporthome/logs`.

   The GlassFish log file may also help to identify the problem. It is /opt/glassfish/domains/domain1/logs/server.log.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673061-Deploying-to-Jetty-9-4-6)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648462-Deploying-to-Resin-4-0-53)
